#!/usr/bin/env python3
"""S6, FR-17: Chạy nhóm test case API (nhóm F của 06_results.md) theo 05_final_tc.md.

Sinh viên tự chạy script này. Mỗi request: In method, đường dẫn, header, body và phản hồi
(mã HTTP, body), ghi cùng nội dung vào file log trong ../logs/. Sau request, script tra
GET /api/coupons (token admin) để ghi mã có được tạo, xóa hay không và giá trị đã lưu.

Script KHÔNG reset dữ liệu, KHÔNG xóa mã mẫu, KHÔNG chạy nhóm H (TC-CPN-54, 55, 56).

Mặc định chạy nhóm F theo thứ tự ở mục 10 của 05_final_tc.md:
  TC-CPN-60, 62 đến 81, 118, 131, 140 đến 143.
Chỉ chạy khi chỉ định bằng --only:
  61   GET danh sách ngay sau reset (nhóm A): Chạy trước nhóm B
  82   Dự phòng số lẻ, số âm (S3): Chỉ các dòng có test case giao diện bị trình duyệt chặn (--rows)
  130  Dự phòng điểm biên số lẻ, số âm (S4): Như trên
  144  Tạo 100 mã cho test case danh sách rất dài (nhóm G): Lệnh riêng, sau nhóm F

Cách dùng (chạy từ bất kỳ thư mục nào):
  python run_api_tests.py                       Chạy nhóm F
  python run_api_tests.py --only 61             Chỉ chạy TC-CPN-61 (trước nhóm B)
  python run_api_tests.py --only 69,143         Chỉ chạy TC-CPN-69 và TC-CPN-143
  python run_api_tests.py --only 82 --rows A,C  Chỉ chạy dòng A, C của TC-CPN-82
  python run_api_tests.py --only 144            Tạo 100 mã cho TC-CPN-144
  python run_api_tests.py --dry-run             In request, không gửi gì (để kiểm script)
  python run_api_tests.py --base-url http://localhost:3000

Chạy lại một test case có tạo mã (ví dụ TC-CPN-60) mà chưa reset dữ liệu thì mã đã tồn tại,
nên sẽ gặp lỗi trùng; khi đó ghi chú vào 06_results.md hoặc reset rồi chạy lại.

Dòng "Gợi ý" trong log chỉ so máy móc (nhóm mã HTTP, mã có trong GET không, giá trị lưu).
Trạng thái Pass, Fail, Khác giả định do sinh viên quyết định khi điền 06_results.md.
"""
import argparse
import datetime
import http.client
import json
import os
import sys
import urllib.parse
from decimal import Decimal, InvalidOperation

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ADMIN = ("admin@eshop.com", "Admin123!")
USER = ("test@eshop.com", "Test1234!")
LOGIN = "/api/login"
LIST = "/api/coupons"
CREATE = "/api/admin/coupons"
DELETE = "/api/admin/coupons/{}"
FR12_CREATE = "/api/coupons"
FR12_DELETE = "/api/coupons/{}"
SEED = ["SAVE10", "BIGBUY", "VIP100", "EXPIRED"]
FIELDS = ["code", "type", "discount_value", "min_order_amount", "expired_at", "max_uses_per_user"]
JSON_CT = "application/json"
REMOVE = object()  # Đánh dấu bỏ hẳn một trường khỏi body


def code(n):
    return f"FR17TC{n}"


def body(c, **over):
    """Body cơ sở (05_final_tc.md mục 1.4), thay hoặc bỏ trường theo over."""
    b = {"code": c, "type": "percent", "discount_value": 15, "min_order_amount": 300000,
         "expired_at": "2099-12-31", "max_uses_per_user": 3}
    for k, v in over.items():
        if v is REMOVE:
            b.pop(k, None)
        else:
            b[k] = v
    return b


class Logger:
    def __init__(self, path):
        self.path = path
        self.f = open(path, "w", encoding="utf-8") if path else None

    def __call__(self, text=""):
        print(text)
        if self.f:
            self.f.write(text + "\n")
            self.f.flush()

    def close(self):
        if self.f:
            self.f.close()


def num_eq(a, b):
    """So hai giá trị số chính xác (không qua số thực), chấp nhận số dạng chuỗi."""
    try:
        return Decimal(str(a)) == Decimal(str(b))
    except (InvalidOperation, ValueError):
        return False


class Ctx:
    def __init__(self, base_url, timeout, dry, log):
        u = urllib.parse.urlparse(base_url)
        self.host, self.port = u.hostname, u.port or 80
        self.base_url, self.timeout, self.dry, self.log = base_url, timeout, dry, log
        self.tokens = {"admin": "<token admin>", "user": "<token user thường>"}
        self.manual = []
        self.fake_id = 900000

    # ---------- HTTP
    def http(self, method, path, json_body=None, raw=None, ct=JSON_CT, auth="admin", quiet=False):
        """Gửi request. auth: 'admin', 'user', None (không header), hoặc chuỗi header Authorization nguyên văn.
        json_body: đối tượng Python (gửi dạng JSON). raw: chuỗi gửi nguyên văn. ct=None: không gửi Content-Type."""
        headers = {}
        if auth in ("admin", "user"):
            headers["Authorization"] = f"Bearer {self.tokens[auth]}"
        elif isinstance(auth, str):
            headers["Authorization"] = auth.replace("<token admin>", self.tokens["admin"])
        data = None
        if json_body is not None:
            data = json.dumps(json_body, ensure_ascii=False)
        elif raw is not None:
            data = raw
        if data is not None and ct:
            headers["Content-Type"] = ct + ("; charset=utf-8" if ct == JSON_CT else "")
        if not quiet:
            self.log(f"  Request: {method} {self.base_url}{path}")
            shown = dict(headers)
            if "Authorization" in shown:
                v = shown["Authorization"]
                for name, tok in self.tokens.items():
                    v = v.replace(tok, f"<token {name}>")
                shown["Authorization"] = v
            self.log(f"  Header: {json.dumps(shown, ensure_ascii=False) if shown else '(không có header)'}")
            if data is None:
                self.log("  Body: (không có body)")
            else:
                self.log(f"  Body: {data}")
        if self.dry:
            if not quiet:
                self.log("  (dry-run: không gửi)")
            return None, "", None
        try:
            conn = http.client.HTTPConnection(self.host, self.port, timeout=self.timeout)
            conn.request(method, path, body=data.encode("utf-8") if data is not None else None, headers=headers)
            resp = conn.getresponse()
            status, text = resp.status, resp.read().decode("utf-8", errors="replace")
            conn.close()
        except (OSError, http.client.HTTPException) as e:
            self.log(f"  LỖI: Không gửi được request: {e}")
            return None, "", None
        try:
            parsed = json.loads(text)
        except ValueError:
            parsed = None
        if not quiet:
            self.log(f"  Response: HTTP {status}")
            if parsed is not None:
                pretty = json.dumps(parsed, ensure_ascii=False, indent=2)
                lines = pretty.splitlines()
                for line in lines[:60]:
                    self.log("    " + line)
                if len(lines) > 60:
                    self.log(f"    ... (cắt bớt, còn {len(lines) - 60} dòng)")
            else:
                self.log(f"  Body phản hồi (không phải JSON): {text[:500]!r}")
        return status, text, parsed

    def hint_status(self, status, expect):
        """expect: '2xx', '4xx', '2xx|4xx' hoặc 'không 5xx'."""
        if status is None:
            return "Không có phản hồi" if not self.dry else "(dry-run)"
        if status >= 500:
            return f"HTTP {status}: 5xx, theo quy ước là Fail"
        group = f"{status // 100}xx"
        ok = expect == "không 5xx" or group in expect.split("|")
        return f"HTTP {status} ({group}): {'khớp' if ok else 'KHÔNG khớp'} mong đợi {expect}"

    # ---------- Đăng nhập
    def login(self):
        for name, (email, pw) in (("admin", ADMIN), ("user", USER)):
            self.log(f"Đăng nhập {name}: POST {LOGIN} với {email}")
            status, text, parsed = self.http("POST", LOGIN, {"email": email, "password": pw}, auth=None, quiet=True)
            tok = parsed.get("token") if isinstance(parsed, dict) else None
            if not tok:
                self.log(f"  LỖI: Không lấy được token {name} (HTTP {status}): {text[:300]!r}")
                return False
            self.tokens[name] = tok
            self.log(f"  Lấy được token {name} (HTTP {status})")
        return True

    # ---------- Tra danh sách
    def coupons(self):
        if self.dry:
            return []
        status, text, parsed = self.http("GET", LIST, auth="admin", quiet=True)
        if isinstance(parsed, list):
            return parsed
        if isinstance(parsed, dict):
            for v in parsed.values():
                if isinstance(v, list) and all(isinstance(x, dict) for x in v):
                    return v
        self.log(f"  CẢNH BÁO: Không đọc được danh sách từ GET {LIST} (HTTP {status})")
        return []

    def find(self, c, ci=False, items=None):
        items = self.coupons() if items is None else items
        for it in items:
            v = it.get("code")
            if v is None:
                continue
            if str(v) == str(c) or (ci and str(v).lower() == str(c).lower()):
                return it
        return None

    def id_of(self, c):
        if self.dry:
            self.fake_id += 1
            self.log(f"  (dry-run: dùng id giả định {self.fake_id} cho {c})")
            return self.fake_id
        rec = self.find(c)
        if rec is None or rec.get("id") is None:
            self.log(f"  BLOCKED: Không lấy được id của {c} từ GET {LIST} (A17)")
            return None
        return rec["id"]

    def count(self):
        return None if self.dry else len(self.coupons())

    def report_present(self, c, expected=None, ci=False):
        """Ghi mã có trong GET không; nếu có thì so giá trị với expected (dict)."""
        if self.dry:
            return
        rec = self.find(c, ci=ci)
        if rec is None:
            self.log(f"  GET: Không có mã {c!r}" + (" (không phân biệt hoa thường)" if ci else ""))
            return None
        self.log(f"  GET: Có mã {rec.get('code')!r}; bản ghi: {json.dumps(rec, ensure_ascii=False)}")
        if expected:
            bad = []
            for k, v in expected.items():
                got = rec.get(k)
                if k == "expired_at":
                    ok = isinstance(got, str) and got[:10] == v
                elif isinstance(v, (int, float)) and not isinstance(v, bool):
                    ok = num_eq(got, v)
                else:
                    ok = got == v
                if not ok:
                    bad.append(f"{k}: gửi {v!r}, lưu {got!r}")
            missing = [f for f in FIELDS + ["id"] if f not in rec]
            self.log("  Gợi ý giá trị lưu: " + ("khớp giá trị đã gửi" if not bad else "KHÁC: " + "; ".join(bad)))
            if missing:
                self.log(f"  Gợi ý: Bản ghi thiếu trường {missing} (A17, GH11)")
        return rec

    def note_manual(self, tc, text):
        self.log(f"  >>> VIỆC LÀM TAY: {text}")
        self.manual.append(f"{tc}: {text}")


# ====================================================================== Test case
def expected_fields(b):
    return {k: v for k, v in b.items() if k in FIELDS and k != "code"}


def create_ok(x, c, b=None, label=""):
    """Tạo mã bằng token admin (bước chuẩn bị), trả id."""
    b = b or body(c)
    x.log(f"  Chuẩn bị{label}: Tạo {c} bằng token admin")
    status, _, _ = x.http("POST", CREATE, b)
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    return x.id_of(c)


def t60(x, rows):
    b = body(code(60))
    status, _, _ = x.http("POST", CREATE, b)
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    x.report_present(code(60), expected_fields(b))
    x.note_manual("TC-CPN-60", "Mở trang Mã Giảm Giá, kiểm dòng FR17TC60 có đúng giá trị")


def t61(x, rows):
    status, _, parsed = x.http("GET", LIST)
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    if x.dry:
        return
    items = x.coupons()
    x.log(f"  Số mã trong danh sách: {len(items)}")
    for s in SEED:
        rec = x.find(s, items=items)
        if rec is None:
            x.log(f"  {s}: KHÔNG có trong danh sách")
            continue
        missing = [f for f in FIELDS + ["id"] if f not in rec]
        x.log(f"  {s}: Có; " + ("đủ 6 trường và id" if not missing else f"THIẾU trường {missing}"))
    x.log("  Điền mục 1 của 06_results.md: GET có trả id và đủ 6 trường không")


def t62(x, rows):
    i = create_ok(x, code(62))
    if i is None:
        return
    status, _, _ = x.http("DELETE", DELETE.format(i))
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    x.report_present(code(62))


def t63(x, rows):
    b = body(2026)
    status, _, _ = x.http("POST", CREATE, b)
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    x.report_present("2026", expected_fields(b))


def run_rows(x, rows, table, fn):
    for r, *args in table:
        if rows and r not in rows:
            continue
        x.log(f"  --- Dòng {r}")
        fn(x, r, *args)


def post_row(expect, check_present=True):
    def fn(x, r, c, b, ec=None):
        before = x.count() if c is None else None
        status, _, _ = x.http("POST", CREATE, b)
        x.log(f"  Gợi ý: {x.hint_status(status, expect)}")
        if c is None:
            after = x.count()
            if after is not None:
                x.log(f"  Số mã trước {before}, sau {after}: " + ("không đổi" if before == after else "THAY ĐỔI"))
        elif check_present:
            x.report_present(c, ec)
    return fn


def t64(x, rows):
    run_rows(x, rows, [
        ("A", code("64A"), body(code("64A"), discount_value="15"), {"discount_value": 15}),
        ("B", code("64B"), body(code("64B"), min_order_amount="300000"), {"min_order_amount": 300000}),
        ("C", code("64C"), body(code("64C"), max_uses_per_user="3"), {"max_uses_per_user": 3}),
    ], post_row("2xx"))


def t65(x, rows):
    run_rows(x, rows, [
        ("A", code("65A"), body(code("65A"), type=REMOVE)),
        ("B", code("65B"), body(code("65B"), type="free")),
        ("C", code("65C"), body(code("65C"), type="PERCENT")),
    ], post_row("4xx"))


def t66(x, rows):
    run_rows(x, rows, [
        ("A", None, body(None)),
        ("B", code("66B"), body(code("66B"), type="")),
        ("C", code("66C"), body(code("66C"), discount_value=None)),
        ("D", code("66D"), body(code("66D"), min_order_amount=None)),
        ("E", code("66E"), body(code("66E"), expired_at="")),
        ("F", code("66F"), body(code("66F"), max_uses_per_user=None)),
    ], post_row("4xx"))


def t67(x, rows):
    run_rows(x, rows, [
        ("A", code("67A"), body(code("67A"), discount_value="abc")),
        ("B", code("67B"), body(code("67B"), min_order_amount="abc")),
        ("C", code("67C"), body(code("67C"), max_uses_per_user="abc")),
    ], post_row("4xx"))


def t68(x, rows):
    run_rows(x, rows, [
        ("A", code("68A"), body(code("68A"), expired_at="12/31/2027")),
        ("B", code("68B"), body(code("68B"), expired_at="2027-02-30")),
        ("C", code("68C"), body(code("68C"), expired_at="2027-12-31T10:00:00Z")),
    ], post_row("4xx"))


def t69(x, rows):
    def fn(x, r, c, raw, ct):
        before = x.count() if c is None else None
        status, _, _ = x.http("POST", CREATE, raw=raw, ct=ct)
        x.log(f"  Gợi ý: {x.hint_status(status, '4xx')}")
        if c is None:
            after = x.count()
            if after is not None:
                x.log(f"  Số mã trước {before}, sau {after}: " + ("không đổi" if before == after else "THAY ĐỔI"))
        else:
            x.report_present(c)
    run_rows(x, rows, [
        ("A", code("69A"), '{"code": "FR17TC69A",', JSON_CT),
        ("B", code("69B"), json.dumps(body(code("69B"))), None),
        ("C", code("69C"), json.dumps(body(code("69C"))), "text/plain"),
        ("D", None, None, None),
    ], fn)


def t70(x, rows):
    before = x.count()
    status, _, _ = x.http("POST", CREATE, {})
    x.log(f"  Gợi ý: {x.hint_status(status, '4xx')}")
    after = x.count()
    if after is not None:
        x.log(f"  Số mã trước {before}, sau {after}: " + ("không đổi" if before == after else "THAY ĐỔI"))
    x.log("  Ghi lại: Thông báo liệt kê đủ 6 trường thiếu hay chỉ một")


def t71(x, rows):
    def fn(x, r, prep):
        if prep == "missing":
            target = 999999
            if not x.dry and any(str(it.get("id")) == str(target) for it in x.coupons()):
                target = max(int(it["id"]) for it in x.coupons() if str(it.get("id")).isdigit()) + 1000
                x.log(f"  id 999999 đang tồn tại, dùng {target}")
        elif prep == "abc":
            target = "abc"
        else:
            target = create_ok(x, code("71C"), label=" dòng C")
            if target is None:
                return
            st, _, _ = x.http("DELETE", DELETE.format(target))
            x.log(f"  Chuẩn bị: Xóa lần 1, {x.hint_status(st, '2xx')}")
        before = x.count()
        status, _, _ = x.http("DELETE", DELETE.format(target))
        x.log(f"  Gợi ý: {x.hint_status(status, '2xx|4xx')}")
        after = x.count()
        if after is not None:
            x.log(f"  Số mã trước {before}, sau {after}: " + ("không đổi" if before == after else "THAY ĐỔI"))
    run_rows(x, rows, [("A", "missing"), ("B", "abc"), ("C", "deleted")], fn)


def auth_post(n, auth, expect_err):
    def t(x, rows):
        status, _, _ = x.http("POST", CREATE, body(code(n)), auth=auth)
        x.log(f"  Gợi ý: {x.hint_status(status, '4xx')} ({expect_err})")
        x.report_present(code(n))
    return t


def auth_get(auth, expect_err, note=""):
    def t(x, rows):
        status, _, parsed = x.http("GET", LIST, auth=auth)
        x.log(f"  Gợi ý: {x.hint_status(status, '4xx')} ({expect_err}){note}")
        if isinstance(parsed, list) or (isinstance(parsed, dict) and any(isinstance(v, list) for v in parsed.values())):
            x.log("  Gợi ý: Phản hồi CÓ chứa danh sách")
    return t


def auth_delete(n, auth, expect_err, path=DELETE, expect="4xx"):
    def t(x, rows):
        i = create_ok(x, code(n))
        if i is None:
            return
        status, _, _ = x.http("DELETE", path.format(i), auth=auth)
        x.log(f"  Gợi ý: {x.hint_status(status, expect)} ({expect_err})")
        rec = x.report_present(code(n))
        if not x.dry:
            x.log("  Gợi ý: Mã " + ("vẫn còn (đúng mong đợi)" if rec else "ĐÃ BỊ XÓA"))
    return t


def t80(x, rows):
    status, _, _ = x.http("POST", FR12_CREATE, body(code(80)), auth=None)
    x.log(f"  Gợi ý: {x.hint_status(status, 'không 5xx')}; 404 cũng Pass")
    rec = x.report_present(code(80))
    if not x.dry:
        x.log("  Gợi ý: Mã " + ("ĐÃ ĐƯỢC TẠO" if rec else "không được tạo (đúng mong đợi)"))


def backup_rows(table):
    def t(x, rows):
        if not rows:
            x.log("  Không có --rows: Chạy mọi dòng. Theo 05_final_tc.md chỉ cần dòng có test case giao diện bị chặn")
        run_rows(x, rows, table, lambda x, r, c, b, exp, ec: (
            x.log(f"  Gợi ý: {x.hint_status(x.http('POST', CREATE, b)[0], exp)}"),
            x.report_present(c, ec if exp == "2xx" else None)))
    return t


t82 = backup_rows([
    ("A", code("82A"), body(code("82A"), discount_value=12.5), "2xx", {"discount_value": 12.5}),
    ("B", code("82B"), body(code("82B"), type="fixed", discount_value=1000.5), "2xx", {"discount_value": 1000.5}),
    ("C", code("82C"), body(code("82C"), min_order_amount=1000.5), "2xx", {"min_order_amount": 1000.5}),
    ("D", code("82D"), body(code("82D"), max_uses_per_user=1.5), "4xx", None),
    ("E", code("82E"), body(code("82E"), min_order_amount=-1), "4xx", None),
    ("F", code("82F"), body(code("82F"), max_uses_per_user=0), "4xx", None),
])

t130 = backup_rows([
    ("A", code("130A"), body(code("130A"), discount_value=-1), "4xx", None),
    ("B", code("130B"), body(code("130B"), discount_value=0.01), "2xx", {"discount_value": 0.01}),
    ("C", code("130C"), body(code("130C"), discount_value=100.01), "4xx", None),
    ("D", code("130D"), body(code("130D"), type="fixed", discount_value=-1), "4xx", None),
    ("E", code("130E"), body(code("130E"), type="fixed", discount_value=0.01), "2xx", {"discount_value": 0.01}),
    ("F", code("130F"), body(code("130F"), min_order_amount=-0.01), "4xx", None),
    ("G", code("130G"), body(code("130G"), max_uses_per_user=-1), "4xx", None),
])


def t118(x, rows):
    b = body(code(118), max_uses_per_user=1.0)
    status, _, _ = x.http("POST", CREATE, b)
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    x.report_present(code(118), {"max_uses_per_user": 1})


def t131(x, rows):
    big = 9007199254740993
    run_rows(x, rows, [
        ("A", code("131A"), body(code("131A"), type="fixed", discount_value=big), {"discount_value": big}),
        ("B", code("131B"), body(code("131B"), min_order_amount=big), {"min_order_amount": big}),
        ("C", code("131C"), body(code("131C"), max_uses_per_user=big), {"max_uses_per_user": big}),
    ], post_row("2xx|4xx"))
    x.log("  Đọc cùng TC-CPN-111, 114, 119 theo bảng ở 05_final_tc.md mục 7.1; lưu 9007199254740992 là Fail")


def t140(x, rows):
    status, _, _ = x.http("POST", CREATE, body("fr17tc140"))
    x.log(f"  Gợi ý bước 1: {x.hint_status(status, '2xx')}")
    x.report_present("fr17tc140", ci=True)
    x.log("  Bước 2 (K5): Gửi lại FR17TC140")
    status, _, _ = x.http("POST", CREATE, body("FR17TC140"))
    x.log(f"  Gợi ý bước 2: {x.hint_status(status, '4xx')} (ERR2)")


def t141(x, rows):
    before = None if x.dry else x.find("SAVE10")
    status, _, _ = x.http("POST", CREATE, body("save10"))
    x.log(f"  Gợi ý: {x.hint_status(status, '4xx')} (ERR2)")
    if not x.dry:
        rec = x.find("save10")
        x.log("  GET: " + ("CÓ mã 'save10' (chữ thường)" if rec else "Không có mã 'save10' viết thường"))
        after = x.find("SAVE10")
        x.log("  Gợi ý: SAVE10 " + ("giữ nguyên" if before == after else f"THAY ĐỔI: trước {before}, sau {after}"))


def t142(x, rows):
    status, _, _ = x.http("POST", CREATE, body("m"))
    x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
    x.report_present("m", ci=True)


def t143(x, rows):
    def fn(x, r, sent, stored):
        if r in ("A", "B"):
            status, _, _ = x.http("POST", CREATE, body(sent))
            x.log(f"  Gợi ý: {x.hint_status(status, '2xx')}")
            if not x.dry:
                exact = x.find(sent)
                x.log("  GET: " + (f"CÓ mã lưu nguyên dấu cách {sent!r}" if exact else "Không có mã còn dấu cách"))
            x.report_present(stored)
            x.log(f"  K5: Gửi lại {stored!r}")
            status, _, _ = x.http("POST", CREATE, body(stored))
            x.log(f"  Gợi ý K5: {x.hint_status(status, '4xx')} (ERR2)")
        elif r == "C":
            before = x.count()
            status, _, _ = x.http("POST", CREATE, body(sent))
            x.log(f"  Gợi ý: {x.hint_status(status, '4xx')} (ERR1)")
            after = x.count()
            if after is not None:
                x.log(f"  Số mã trước {before}, sau {after}: " + ("không đổi" if before == after else "THAY ĐỔI"))
        else:
            before = None if x.dry else x.find("SAVE10")
            status, _, _ = x.http("POST", CREATE, body(sent))
            x.log(f"  Gợi ý: {x.hint_status(status, '4xx')} (ERR2)")
            if not x.dry:
                after = x.find("SAVE10")
                x.log("  Gợi ý: SAVE10 " + ("giữ nguyên" if before == after else f"THAY ĐỔI: trước {before}, sau {after}"))
                x.log("  GET: " + ("CÓ mã ' SAVE10'" if x.find(sent) else "Không có mã ' SAVE10'"))
    run_rows(x, rows, [
        ("A", " FR17TC143A", "FR17TC143A"),
        ("B", "FR17TC143B ", "FR17TC143B"),
        ("C", "   ", None),
        ("D", " SAVE10", "SAVE10"),
    ], fn)


def t144(x, rows):
    codes = [f"FR17TC144N{i:03d}" for i in range(1, 101)]
    x.log(f"  Tạo {len(codes)} mã từ {codes[0]} đến {codes[-1]} bằng token admin (chỉ log tóm tắt)")
    tally = {}
    for c in codes:
        status, _, _ = x.http("POST", CREATE, body(c), quiet=True)
        key = "dry-run" if x.dry else (f"HTTP {status}" if status is not None else "không phản hồi")
        tally[key] = tally.get(key, 0) + 1
    x.log(f"  Kết quả tạo: {tally}")
    if not x.dry:
        items = x.coupons()
        n = sum(1 for it in items if str(it.get("code", "")).startswith("FR17TC144N"))
        x.log(f"  GET: {len(items)} mã, trong đó {n} mã FR17TC144N...")
    x.note_manual("TC-CPN-144", "Mở trang Mã Giảm Giá; cuộn hoặc chuyển trang tới cuối; đếm số dòng so với số mã "
                  "trong GET ở trên; kiểm FR17TC144N001, FR17TC144N100, bố cục, nút Xóa ở dòng cuối; chụp ảnh")


# (mã, tiêu đề, hàm, chạy mặc định)
TESTS = [
    ("TC-CPN-61", "API trả danh sách mã đủ trường (nhóm A, chạy trước nhóm B)", t61, False),
    ("TC-CPN-60", "API tạo mã thành công", t60, True),
    ("TC-CPN-62", "API xóa mã vừa tạo", t62, True),
    ("TC-CPN-63", "API nhận Mã là số JSON", t63, True),
    ("TC-CPN-64", "API nhận chuỗi chứa số (3 dòng)", t64, True),
    ("TC-CPN-65", "API từ chối type không hợp lệ (3 dòng)", t65, True),
    ("TC-CPN-66", "API từ chối null, chuỗi rỗng (6 dòng)", t66, True),
    ("TC-CPN-67", "API từ chối trường số không phải số (3 dòng)", t67, True),
    ("TC-CPN-68", "API từ chối ngày sai định dạng (3 dòng)", t68, True),
    ("TC-CPN-69", "API từ chối request không đọc được (4 dòng)", t69, True),
    ("TC-CPN-70", "API từ chối body {}", t70, True),
    ("TC-CPN-71", "API xóa với id không hợp lệ (3 dòng)", t71, True),
    ("TC-CPN-72", "Tạo mã không có header Authorization", auth_post(72, None, "ERR12"), True),
    ("TC-CPN-73", "Tạo mã khi header thiếu Bearer", auth_post(73, "<token admin>", "ERR12"), True),
    ("TC-CPN-74", "Tạo mã khi token không hợp lệ", auth_post(74, "Bearer abc.def.ghi", "ERR12"), True),
    ("TC-CPN-75", "Tạo mã bằng token user thường", auth_post(75, "user", "ERR13"), True),
    ("TC-CPN-76", "Xem danh sách không có header", auth_get(None, "ERR12"), True),
    ("TC-CPN-77", "Xem danh sách bằng token user thường", auth_get("user", "ERR13", "; 2xx là Khác giả định A28"), True),
    ("TC-CPN-78", "Xóa mã không có header", auth_delete(78, None, "ERR12"), True),
    ("TC-CPN-79", "Xóa mã bằng token user thường", auth_delete(79, "user", "ERR13"), True),
    ("TC-CPN-80", "POST /api/coupons (FR-12) không header", t80, True),
    ("TC-CPN-81", "DELETE /api/coupons/:id (FR-12) bằng user thường",
     auth_delete(81, "user", "404 cũng Pass", path=FR12_DELETE, expect="không 5xx"), True),
    ("TC-CPN-82", "Dự phòng số lẻ, số âm (S3)", t82, False),
    ("TC-CPN-118", "Số lần dùng tối đa viết là 1.0", t118, True),
    ("TC-CPN-130", "Dự phòng điểm biên số lẻ, số âm (S4)", t130, False),
    ("TC-CPN-131", "Server lưu chính xác 2^53 + 1 (3 dòng)", t131, True),
    ("TC-CPN-140", "API tạo mã có chữ thường", t140, True),
    ("TC-CPN-141", "API từ chối mã khác mã mẫu ở hoa thường", t141, True),
    ("TC-CPN-142", "API tạo mã là 1 chữ thường", t142, True),
    ("TC-CPN-143", "API cắt dấu cách đầu cuối của Mã (4 dòng)", t143, True),
    ("TC-CPN-144", "Tạo 100 mã cho danh sách rất dài (nhóm G)", t144, False),
]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default="http://localhost:3000")
    p.add_argument("--only", help="Danh sách số test case, ví dụ 69,143 hoặc 61")
    p.add_argument("--rows", help="Chỉ chạy các dòng này của test case dạng bảng, ví dụ A,C")
    p.add_argument("--dry-run", action="store_true", help="In request, không gửi")
    p.add_argument("--timeout", type=float, default=10)
    args = p.parse_args()

    if args.only:
        wanted = {f"TC-CPN-{int(n):02d}" for n in args.only.split(",") if n.strip()}
        tests = [t for t in TESTS if t[0] in wanted]
        unknown = wanted - {t[0] for t in TESTS}
        if unknown:
            print(f"Không có trong script (không thuộc nhóm API): {sorted(unknown)}")
    else:
        tests = [t for t in TESTS if t[3]]
    rows = {r.strip().upper() for r in args.rows.split(",")} if args.rows else None

    here = os.path.dirname(os.path.abspath(__file__))
    now = datetime.datetime.now()
    log_path = None
    if not args.dry_run:
        log_dir = os.path.join(here, "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.normpath(os.path.join(log_dir, f"S6_api_{now:%Y%m%d_%H%M%S}.log"))
    log = Logger(log_path)
    x = Ctx(args.base_url, args.timeout, args.dry_run, log)

    log("S6, FR-17: Nhóm test case API")
    log(f"Thời gian bắt đầu: {now:%Y-%m-%d %H:%M:%S}")
    log(f"Base URL: {args.base_url}")
    log(f"Chế độ: {'dry-run (không gửi)' if args.dry_run else 'gửi thật'}")
    log(f"Test case: {', '.join(t[0] for t in tests) or '(không có)'}")
    if rows:
        log(f"Chỉ các dòng: {', '.join(sorted(rows))}")
    log("Script không reset dữ liệu, không xóa mã mẫu, không chạy nhóm H.")

    if not args.dry_run and tests:
        log("")
        if not x.login():
            log("Dừng: Không đăng nhập được, chưa gửi request nào của test case.")
            log.close()
            sys.exit(1)

    for tc, title, fn, _ in tests:
        log("")
        log("=" * 78)
        log(f"{tc}: {title}")
        log("Mong đợi: Xem 05_final_tc.md và 06_results.md")
        log("-" * 78)
        fn(x, rows)

    log("")
    log("=" * 78)
    log(f"Kết thúc: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
    if x.manual:
        log("Việc làm tay qua giao diện còn lại:")
        for m in x.manual:
            log(f"  - {m}")
    log("Nhắc: Nhóm H (TC-CPN-54, 55, 56) làm tay qua giao diện, sau cùng; reset trước và sau TC-CPN-56.")
    if log_path:
        log(f"Log: {log_path}")
    log.close()


if __name__ == "__main__":
    main()
