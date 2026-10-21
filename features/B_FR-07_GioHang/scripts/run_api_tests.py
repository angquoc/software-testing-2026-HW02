#!/usr/bin/env python3
"""S6, FR-07: Chạy nhóm test case API (nhóm D, E của 06_results.md) theo 05_final_tc.md.

Sinh viên tự chạy script này. Mỗi request: In method, đường dẫn, header (token đã che),
body và phản hồi (mã HTTP, body), ghi cùng nội dung vào file log trong ../logs/. Trước và
sau mỗi test case, script gọi GET /api/cart (token test) để ghi số dòng của giỏ.

Script KHÔNG reset dữ liệu và KHÔNG xóa giỏ (API spec không mô tả API xóa giỏ).

Mặc định chạy nhóm API không hợp lệ (giỏ không đổi nếu hệ thống đúng):
  TC-CART-30, 31, 32, 33, 34, 35, 102, 36 (36 thêm 1 dòng ở bước 1 nên chạy cuối nhóm)
Chỉ chạy khi chỉ định bằng --only (mỗi lệnh một test case, xóa hết giỏ qua giao diện trước):
  50, 51, 54, 52   API hợp lệ
  53               Chuỗi SQL: Chạy CUỐI CÙNG trong đợt test, reset dữ liệu ngay sau đó

Cách dùng (chạy từ bất kỳ thư mục nào):
  python run_api_tests.py                  Chạy nhóm API không hợp lệ
  python run_api_tests.py --only 50        Chỉ chạy TC-CART-50
  python run_api_tests.py --only 53        Chạy TC-CART-53 (cuối cùng), log riêng S6_tc53_...
  python run_api_tests.py --show-cart      Chỉ in GET /api/cart (kiểm chứng K1 cho test case giao diện)
  python run_api_tests.py --dry-run        In request, không gửi gì (để kiểm script)
  python run_api_tests.py --base-url http://localhost:3000

Dòng "Gợi ý" trong log chỉ so máy móc (nhóm mã HTTP, số dòng và số lượng trong giỏ).
Trạng thái Pass, Fail, Khác giả định do sinh viên quyết định khi điền 06_results.md.
"""
import argparse
import datetime
import http.client
import json
import os
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

USER = ("test@eshop.com", "Test1234!")
ADMIN = ("admin@eshop.com", "Admin123!")
LOGIN = "/api/login"
CART = "/api/cart"
PRODUCT = "/api/products/{}"
JSON_CT = "application/json"
REMOVE = object()  # Đánh dấu bỏ hẳn một trường khỏi body
BASE_ID, BASE_NAME, BASE_PRICE = 1, "iPhone 15 Pro Max", 30000000


def body(**over):
    """Body cơ sở (05_final_tc.md mục 1.4), thay hoặc bỏ trường theo over."""
    b = {"id": BASE_ID, "name": BASE_NAME, "price": BASE_PRICE, "quantity": 1}
    for k, v in over.items():
        if v is REMOVE:
            b.pop(k, None)
        else:
            b[k] = v
    return b


class Logger:
    def __init__(self, path):
        self.f = open(path, "w", encoding="utf-8") if path else None

    def __call__(self, text=""):
        print(text)
        if self.f:
            self.f.write(text + "\n")
            self.f.flush()

    def close(self):
        if self.f:
            self.f.close()


def first(d, keys):
    for k in keys:
        if isinstance(d, dict) and k in d:
            return d[k]
    return None


def cart_items(parsed):
    """API spec không mô tả cấu trúc phản hồi (Q27): Lấy danh sách đối tượng đầu tiên tìm thấy."""
    if isinstance(parsed, list):
        return [x for x in parsed if isinstance(x, dict)]
    if isinstance(parsed, dict):
        for v in parsed.values():
            if isinstance(v, list) and all(isinstance(x, dict) for x in v):
                return v
        for v in parsed.values():
            found = cart_items(v) if isinstance(v, dict) else None
            if found:
                return found
    return []


def item_id(it):
    return first(it, ["product_id", "productId", "id"])


def summarize(items):
    if not items:
        return "giỏ trống (0 dòng)"
    parts = []
    for it in items:
        parts.append(f"[id={item_id(it)}, name={first(it, ['name', 'product_name', 'productName'])!r}, "
                     f"price={first(it, ['price', 'unit_price'])}, quantity={first(it, ['quantity', 'qty'])}]")
    return f"{len(items)} dòng: " + ", ".join(parts)


class Ctx:
    def __init__(self, base_url, timeout, dry, log):
        u = urllib.parse.urlparse(base_url)
        self.host, self.port = u.hostname, u.port or 80
        self.base_url, self.timeout, self.dry, self.log = base_url, timeout, dry, log
        self.tokens = {"test": "<token test>", "admin": "<token admin>"}

    def mask(self, text):
        for name, tok in self.tokens.items():
            if tok and not tok.startswith("<"):
                text = text.replace(tok, f"<token {name}>")
                text = text.replace(tok[:-1], f"<token {name}, bỏ ký tự cuối>")
        return text

    def http(self, method, path, json_body=None, auth="test", quiet=False):
        """auth: 'test', 'admin', None (không header), hoặc ('bad', tên) để gửi token bị sửa 1 ký tự."""
        headers = {}
        shown_auth = None
        if auth in ("test", "admin"):
            headers["Authorization"] = f"Bearer {self.tokens[auth]}"
            shown_auth = f"Bearer <token {auth}>"
        elif isinstance(auth, tuple) and auth[0] == "bad":
            tok = self.tokens[auth[1]]
            bad = tok[:-1] + ("A" if tok[-1:] != "A" else "B")
            headers["Authorization"] = f"Bearer {bad}"
            shown_auth = f"Bearer <token {auth[1]}, ký tự cuối bị sửa>"
        data = json.dumps(json_body, ensure_ascii=False) if json_body is not None else None
        if data is not None:
            headers["Content-Type"] = JSON_CT + "; charset=utf-8"
        if not quiet:
            self.log(f"  Request: {method} {self.base_url}{path}")
            shown = dict(headers)
            if shown_auth:
                shown["Authorization"] = shown_auth
            self.log(f"  Header: {json.dumps(shown, ensure_ascii=False) if shown else '(không có header)'}")
            self.log(f"  Body: {data if data is not None else '(không có body)'}")
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
                lines = self.mask(json.dumps(parsed, ensure_ascii=False, indent=2)).splitlines()
                for line in lines[:60]:
                    self.log("    " + line)
                if len(lines) > 60:
                    self.log(f"    ... (cắt bớt, còn {len(lines) - 60} dòng)")
            else:
                self.log(f"  Body phản hồi (không phải JSON): {self.mask(text[:500])!r}")
        return status, text, parsed

    def hint(self, status, expect):
        """expect: '2xx' hoặc 'không 2xx'."""
        if status is None:
            return "(dry-run)" if self.dry else "Không có phản hồi"
        group = f"{status // 100}xx"
        if status >= 500:
            return f"HTTP {status} (5xx): Lỗi hệ thống"
        ok = (group == "2xx") if expect == "2xx" else (group != "2xx")
        return f"HTTP {status} ({group}): {'khớp' if ok else 'KHÔNG khớp'} mong đợi {expect}"

    def login(self):
        for name, (email, pw) in (("test", USER), ("admin", ADMIN)):
            self.log(f"Đăng nhập {name}: POST {LOGIN} với {email}")
            status, text, parsed = self.http("POST", LOGIN, {"email": email, "password": pw}, auth=None, quiet=True)
            tok = parsed.get("token") if isinstance(parsed, dict) else None
            if not tok:
                self.log(f"  LỖI: Không lấy được token {name} (HTTP {status}): {text[:300]!r}")
                return False
            self.tokens[name] = tok
            self.log(f"  Lấy được token {name} (HTTP {status})")
        return True

    def cart(self, who="test", label="Giỏ"):
        """GET /api/cart bằng token hợp lệ; trả về danh sách dòng và ghi tóm tắt."""
        if self.dry:
            self.log(f"  {label} ({who}): (dry-run)")
            return []
        status, text, parsed = self.http("GET", CART, auth=who, quiet=True)
        items = cart_items(parsed)
        self.log(f"  {label} ({who}, GET HTTP {status}): {summarize(items)}")
        return items

    def require_empty(self):
        items = self.cart(label="Giỏ trước test case")
        if items:
            self.log("  CẢNH BÁO: Giỏ chưa trống, khác tiền điều kiện. Xóa hết giỏ qua giao diện rồi chạy lại, "
                     "hoặc ghi chú vào 06_results.md")
        return items


def qty_of(items, pid=BASE_ID):
    for it in items:
        if str(item_id(it)) == str(pid):
            return first(it, ["quantity", "qty"])
    return None


def invalid_post(payload, err, auth="test"):
    def fn(x):
        before = x.cart(label="Giỏ trước")
        status, _, _ = x.http("POST", CART, payload, auth=auth)
        x.log(f"  Gợi ý: {x.hint(status, 'không 2xx')} ({err})")
        after = x.cart(label="Giỏ sau")
        if not x.dry:
            same = summarize(before) == summarize(after)
            x.log("  Gợi ý: Giỏ " + ("không đổi" if same else "THAY ĐỔI so với trước request"))
    return fn


def t30(x):
    x.log("  Kiểm trước: GET /api/products/9999 không trả về sản phẩm")
    status, _, parsed = x.http("GET", PRODUCT.format(9999), auth=None)
    if not x.dry:
        x.log(f"  Gợi ý: {'Có vẻ không có sản phẩm 9999' if status != 200 or not parsed else 'CÓ phản hồi 200 có dữ liệu, kiểm lại tiền điều kiện'}")
    invalid_post(body(id=9999), "ERR3")(x)


def t36(x):
    x.log("  Bước 1: POST /api/cart body cơ sở với token hợp lệ")
    status, _, _ = x.http("POST", CART, body())
    x.log(f"  Gợi ý bước 1: {x.hint(status, '2xx')}")
    x.log("  Bước 2: GET /api/cart với token test bị sửa ký tự cuối")
    status, _, parsed = x.http("GET", CART, auth=("bad", "test"))
    x.log(f"  Gợi ý bước 2: {x.hint(status, 'không 2xx')} (ERR1); "
          + ("" if x.dry else f"dữ liệu giỏ trong phản hồi: {summarize(cart_items(parsed))}"))


def t50(x):
    x.require_empty()
    status, _, _ = x.http("POST", CART, body())
    x.log(f"  Gợi ý POST: {x.hint(status, '2xx')}")
    x.log("  GET /api/cart:")
    _, _, parsed = x.http("GET", CART)
    items = cart_items(parsed)
    if not x.dry:
        x.log(f"  Gợi ý: Số lượng của id {BASE_ID} = {qty_of(items)} (mong đợi 1); {summarize(items)}")
    x.log("  Làm tay: Mở trang Giỏ hàng, chụp S6_TC-CART-50.png (mong đợi như TC-CART-01)")


def t51(x):
    x.require_empty()
    status, _, _ = x.http("POST", CART, body(price=1))
    x.log(f"  Gợi ý POST: {x.hint(status, '2xx')} (bị từ chối cũng chấp nhận được theo A24)")
    items = x.cart(label="Giỏ sau")
    if not x.dry:
        prices = [first(it, ["price", "unit_price"]) for it in items if str(item_id(it)) == str(BASE_ID)]
        bad = [p for p in prices if str(p) in ("1", "1.0")]
        x.log("  Gợi ý: " + ("CÓ dòng giá 1" if bad else f"Không có dòng giá 1; giá dòng id {BASE_ID}: {prices or 'không có dòng'}"))
    x.log("  Làm tay: Mở trang Giỏ hàng, xem Đơn giá, Thành tiền (mong đợi 30,000,000 ₫ nếu có dòng)")


def t52(x):
    x.require_empty()
    status, _, _ = x.http("POST", CART, body(name="<b>X</b>"))
    x.log(f"  Gợi ý POST: {x.hint(status, '2xx')}")
    x.cart(label="Giỏ sau")
    x.log("  Làm tay: Mở trang Giỏ hàng, chụp S6_TC-CART-52.png. Mong đợi: Tên là chuỗi <b>X</b> nguyên văn "
          "hoặc tên trong CSDL; không có chữ X in đậm")


def t53(x):
    x.require_empty()
    status, _, _ = x.http("POST", CART, body(name="X' OR '1'='1"))
    x.log(f"  Gợi ý POST: {x.hint(status, '2xx')} (mong đợi không phải 5xx)")
    x.log("  GET /api/cart:")
    _, _, parsed = x.http("GET", CART)
    items = cart_items(parsed)
    if not x.dry:
        x.log(f"  Gợi ý: {summarize(items)}; mong đợi đúng 1 dòng id {BASE_ID}, số lượng 1, không có dòng lạ")
    x.log("  NHẮC: Reset dữ liệu EShop ngay sau test case này; ghi thời điểm reset vào 06_results.md mục 1")


def t54(x):
    x.require_empty()
    x.log("  Bước 1: POST /api/cart body cơ sở với token test@eshop.com")
    status, _, _ = x.http("POST", CART, body())
    x.log(f"  Gợi ý bước 1: {x.hint(status, '2xx')}")
    x.cart(label="Giỏ của test sau bước 1")
    x.log("  Bước 2: GET /api/cart với token admin@eshop.com")
    _, _, parsed = x.http("GET", CART, auth="admin")
    items = cart_items(parsed)
    if not x.dry:
        x.log(f"  Gợi ý: Giỏ của admin: {summarize(items)}; "
              + ("CÓ dòng id 1, kiểm xem có phải do admin tự thêm không" if qty_of(items) is not None
                 else "không có dòng id 1"))


# (số, tiêu đề, hàm, chạy mặc định)
TESTS = [
    (30, "Thêm sản phẩm không tồn tại (id 9999)", t30, True),
    (31, "Số lượng 0", invalid_post(body(quantity=0), "ERR2"), True),
    (32, "Số lượng thập phân 1.5", invalid_post(body(quantity=1.5), "ERR2"), True),
    (33, "Số lượng không phải số \"abc\"", invalid_post(body(quantity="abc"), "ERR2"), True),
    (34, "Thiếu trường quantity", invalid_post(body(quantity=REMOVE), "ERR3"), True),
    (35, "Thiếu header Authorization", invalid_post(body(), "ERR1", auth=None), True),
    (102, "Số lượng âm -1 (BVA)", invalid_post(body(quantity=-1), "ERR2"), True),
    (36, "Xem giỏ với token sai", t36, True),
    (50, "Thêm và xem giỏ qua API", t50, False),
    (51, "price khác giá CSDL (price = 1)", t51, False),
    (54, "Người dùng khác không thấy giỏ của test", t54, False),
    (52, "name có thẻ HTML", t52, False),
    (53, "name có ký tự SQL (CHẠY CUỐI CÙNG)", t53, False),
]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default="http://localhost:3000")
    p.add_argument("--only", help="Danh sách số test case, ví dụ 50 hoặc 31,102")
    p.add_argument("--show-cart", action="store_true", help="Chỉ in GET /api/cart của test@eshop.com (K1)")
    p.add_argument("--dry-run", action="store_true", help="In request, không gửi")
    p.add_argument("--timeout", type=float, default=10)
    args = p.parse_args()

    if args.show_cart:
        tests, kind = [], "cart"
    elif args.only:
        wanted = {int(n) for n in args.only.split(",") if n.strip()}
        tests = [t for t in TESTS if t[0] in wanted]
        unknown = wanted - {t[0] for t in TESTS}
        if unknown:
            print(f"Không có trong script (không thuộc nhóm API): {sorted(unknown)}")
        kind = "tc53" if wanted == {53} else "api"
        if 53 in wanted and len(wanted) > 1:
            print("Lưu ý: TC-CART-53 nên chạy riêng và cuối cùng (--only 53).")
    else:
        tests, kind = [t for t in TESTS if t[3]], "api"

    here = os.path.dirname(os.path.abspath(__file__))
    now = datetime.datetime.now()
    log_path = None
    if not args.dry_run:
        log_dir = os.path.join(here, "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.normpath(os.path.join(log_dir, f"S6_{kind}_{now:%Y%m%d_%H%M%S}.log"))
    log = Logger(log_path)
    x = Ctx(args.base_url, args.timeout, args.dry_run, log)

    log("S6, FR-07: " + ("Kiểm chứng K1 (GET /api/cart)" if kind == "cart" else "Nhóm test case API"))
    log(f"Thời gian bắt đầu: {now:%Y-%m-%d %H:%M:%S}")
    log(f"Base URL: {args.base_url}")
    log(f"Chế độ: {'dry-run (không gửi)' if args.dry_run else 'gửi thật'}")
    if kind != "cart":
        log(f"Test case: {', '.join(f'TC-CART-{t[0]:02d}' for t in tests) or '(không có)'}")
    log("Script không reset dữ liệu, không xóa giỏ.")

    if not args.dry_run:
        log("")
        if not x.login():
            log("Dừng: Không đăng nhập được, chưa gửi request nào của test case.")
            log.close()
            sys.exit(1)

    if kind == "cart":
        log("")
        x.http("GET", CART)
        x.cart(label="Tóm tắt")

    for n, title, fn, _ in tests:
        log("")
        log("=" * 78)
        log(f"TC-CART-{n:02d}: {title}")
        log("Mong đợi: Xem 05_final_tc.md và 06_results.md")
        log("-" * 78)
        fn(x)

    log("")
    log("=" * 78)
    log(f"Kết thúc: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
    if log_path:
        log(f"Log: {log_path}")
    log.close()


if __name__ == "__main__":
    main()
