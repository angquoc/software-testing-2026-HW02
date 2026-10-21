#!/usr/bin/env python3
"""Chạy các test case API của FR-04 (Hồ sơ cá nhân) và đặt trạng thái chuẩn S_CHUAN.

Căn cứ: `05_final_tc.md` (mục 1.3 S_CHUAN, giá trị cơ sở, B(NN); mục 6 TS-04; mục 9 thứ tự chạy).
Chỉ dùng thư viện chuẩn của Python. Token bị che trong log và trên màn hình.

Lệnh:
  chuan   [--tag TC]          Đặt S_CHUAN bằng PUT /api/users/me rồi kiểm bằng GET (dùng trước mỗi test case giao diện)
  get     [--tag TC]          EV3: GET /api/users/me, in name, phone, shipping_address (dùng sau mỗi test case giao diện)
  run     [--only TC,...]     Nhóm A và E: TC-PROF-70 trước, rồi 71 đến 75, 78, 79, 80, 102
  last    [--only TC,...]     Nhóm G, chạy cuối cùng: TC-PROF-77 rồi TC-PROF-76. Reset dữ liệu mẫu ngay sau

Tùy chọn chung: --base URL (mặc định http://localhost:3000), --dry-run (chỉ in yêu cầu, không gửi, không đăng nhập).

Cột "Gợi ý" trong log chỉ là so sánh máy móc với kết quả mong đợi; trạng thái cuối do sinh viên review.
"""
import argparse
import datetime
import io
import json
import os
import sys
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(os.path.dirname(HERE), "logs")

# Tài khoản mặc định theo SRS mục 1
TEST_USER = ("test@eshop.com", "Test1234!")
ADMIN_USER = ("admin@eshop.com", "Admin123!")

# 05_final_tc.md mục 1.3
S_CHUAN = {"name": "Test User", "phone": "0900000000", "shipping_address": "1 Nguyen Hue, Quận 1"}
BASE_PHONE = "0912345678"
BASE_ADDRESS = "12/3 Lê Lợi, Quận 1, TP.HCM"
FIELDS = ("name", "phone", "shipping_address")
SECRET_KEYS = ("token", "password", "password_hash", "hash")


def body_b(nn, **override):
    """B(NN): Body đủ 3 trường cơ sở, Họ Tên gắn số test case."""
    body = {"name": f"Nguyen Van An {nn}", "phone": BASE_PHONE, "shipping_address": BASE_ADDRESS}
    body.update(override)
    return body


# ---------------------------------------------------------------- log, che token
class Log:
    def __init__(self, command, dry_run):
        self.secrets = set()
        self.lines = []
        stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.path = None if dry_run else os.path.join(LOG_DIR, f"S6_{command}_{stamp}.log")

    def add_secret(self, value):
        if value:
            self.secrets.add(value)

    def mask(self, text):
        for s in self.secrets:
            text = text.replace(s, s[:6] + "...<đã che>")
        return text

    def __call__(self, text=""):
        text = self.mask(str(text))
        print(text)
        self.lines.append(text)

    def save(self):
        if not self.path:
            return
        os.makedirs(LOG_DIR, exist_ok=True)
        with io.open(self.path, "w", encoding="utf-8") as f:
            f.write("\n".join(self.lines) + "\n")
        print(f"\nĐã ghi log: {os.path.relpath(self.path, os.path.dirname(HERE))}")


def mask_json(obj):
    if isinstance(obj, dict):
        return {k: ("<đã che>" if k.lower() in SECRET_KEYS else mask_json(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [mask_json(v) for v in obj]
    return obj


def show(value):
    """Hiện dấu cách ở đầu, cuối bằng ký hiệu ␣ để đọc log không nhầm."""
    if isinstance(value, str) and value != value.strip(" "):
        return repr(value).replace(" ", "␣")
    return repr(value)


# ---------------------------------------------------------------- HTTP
class Client:
    def __init__(self, base, log, dry_run):
        self.base = base.rstrip("/")
        self.log = log
        self.dry_run = dry_run

    def request(self, method, path, body=None, auth="none", token=None):
        """auth: 'bearer' (dùng token), 'raw' (token là nguyên giá trị header), 'none' (không có header)."""
        url = self.base + path
        headers = {"Content-Type": "application/json"}
        if auth == "bearer":
            headers["Authorization"] = f"Bearer {token}"
        elif auth == "raw":
            headers["Authorization"] = token
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        self.log(f"  -> {method} {path}  Authorization: {headers.get('Authorization', '(không có)')}")
        if body is not None:
            self.log(f"     body: {json.dumps(mask_json(body), ensure_ascii=False)}")
        if self.dry_run:
            return None, None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                status, raw = resp.status, resp.read()
        except urllib.error.HTTPError as e:
            status, raw = e.code, e.read()
        except urllib.error.URLError as e:
            self.log(f"  <- LỖI KẾT NỐI: {e.reason}")
            return None, None
        text = raw.decode("utf-8", errors="replace")
        try:
            parsed = json.loads(text) if text else None
        except ValueError:
            parsed = text
        self.log(f"  <- HTTP {status}  body: {json.dumps(mask_json(parsed), ensure_ascii=False) if not isinstance(parsed, str) else parsed}")
        return status, parsed


def ok(status):
    return status is not None and 200 <= status < 300


def find_profile(body):
    """Tìm object hồ sơ trong phản hồi (cấu trúc không có trong API spec, Q20)."""
    if isinstance(body, dict):
        if any(k in body for k in FIELDS + ("email",)):
            return body
        for key in ("user", "data", "profile"):
            if isinstance(body.get(key), dict):
                found = find_profile(body[key])
                if found:
                    return found
    return None


def login(client, user):
    status, body = client.request("POST", "/api/login", {"email": user[0], "password": user[1]})
    if client.dry_run:
        return "DRYRUN_TOKEN_" + user[0]
    token = body.get("token") if isinstance(body, dict) else None
    if not ok(status) or not token:
        client.log(f"  !! Không đăng nhập được {user[0]}; dừng.")
        return None
    client.log.add_secret(token)
    return token


def get_profile(client, token, label="EV3"):
    client.log(f"  [{label}] GET /api/users/me")
    status, body = client.request("GET", "/api/users/me", auth="bearer", token=token)
    prof = find_profile(body)
    if prof is not None:
        client.log("     " + ", ".join(f"{k}={show(prof.get(k))}" for k in FIELDS + ("email", "role", "id") if k in prof))
    return status, prof


def same_as(prof, expected):
    return prof is not None and all(prof.get(k) == v for k, v in expected.items())


def set_chuan(client, token):
    client.log("  [S_CHUAN] Đặt trạng thái chuẩn")
    status, _ = client.request("PUT", "/api/users/me", S_CHUAN, auth="bearer", token=token)
    if client.dry_run:
        return True
    _, prof = get_profile(client, token, "S_CHUAN kiểm")
    if not ok(status) or not same_as(prof, S_CHUAN):
        client.log("  !! Không đặt được S_CHUAN. Theo 05_final_tc.md mục 9: Reset dữ liệu mẫu thay cho bước này rồi chạy lại.")
        return False
    return True


# ---------------------------------------------------------------- kết luận gợi ý
def verdict(log, tc, passed, detail):
    text = {True: "ĐẠT", False: "KHÔNG ĐẠT", None: "CẦN XEM"}[passed]
    log(f"  => Gợi ý {tc}: {text}. {detail}")
    return text


def check_update(client, token, tc, body, expect_saved):
    """PUT body hợp lệ; expect_saved: dict giá trị EV3 phải trả."""
    status, _ = client.request("PUT", "/api/users/me", body, auth="bearer", token=token)
    if client.dry_run:
        return
    _, prof = get_profile(client, token)
    good = ok(status) and same_as(prof, expect_saved)
    verdict(client.log, tc, good, f"Mong đợi OUT2 và EV3 trả {expect_saved}")


def check_reject(client, token, tc, body):
    status, _ = client.request("PUT", "/api/users/me", body, auth="bearer", token=token)
    if client.dry_run:
        return
    _, prof = get_profile(client, token)
    good = (not ok(status)) and same_as(prof, S_CHUAN)
    verdict(client.log, tc, good, "Mong đợi ERR2 (API): Không thành công, EV3 trả S_CHUAN")


# ---------------------------------------------------------------- test case
def tc70(c, t):
    b = body_b(70)
    status, _ = c.request("PUT", "/api/users/me", b, auth="bearer", token=t)
    if c.dry_run:
        return
    _, prof = get_profile(c, t)
    good = ok(status) and same_as(prof, b) and prof.get("email") == TEST_USER[0]
    verdict(c.log, "TC-PROF-70", good, "Mong đợi OUT2, EV3 trả đúng B(70) và email test@eshop.com (OUT3)")


def tc71(c, t):
    check_update(c, t, "TC-PROF-71", body_b(71, phone=" 0912345678 "),
                 {"name": "Nguyen Van An 71", "phone": "0912345678"})


def tc72(c, t):
    status, _ = c.request("PUT", "/api/users/me", {"name": "Nguyen Van An 72"}, auth="bearer", token=t)
    if c.dry_run:
        return
    _, prof = get_profile(c, t)
    kept = {"phone": S_CHUAN["phone"], "shipping_address": S_CHUAN["shipping_address"]}
    if ok(status):
        good = same_as(prof, dict(kept, name="Nguyen Van An 72"))
        detail = "Phản hồi thành công: phone, shipping_address phải giữ S_CHUAN, name đổi"
    else:
        good = same_as(prof, S_CHUAN)
        detail = "Phản hồi thất bại: EV3 phải trả S_CHUAN"
    verdict(c.log, "TC-PROF-72", good, detail + " (A16 (d))")


def tc73(c, t):
    check_reject(c, t, "TC-PROF-73", body_b(73, phone="0912-345678"))


def tc74(c, t):
    check_reject(c, t, "TC-PROF-74", body_b(74, phone="1912345678"))


def tc75(c, t):
    check_reject(c, t, "TC-PROF-75", body_b(75, phone="091234567"))


def no_auth_case(c, t, tc, auth, raw):
    b = body_b(tc[-2:])
    s1, _ = c.request("PUT", "/api/users/me", b, auth=auth, token=raw)
    s2, body2 = c.request("GET", "/api/users/me", auth=auth, token=raw)
    if c.dry_run:
        return
    _, prof = get_profile(c, t)
    good = (not ok(s1)) and (not ok(s2)) and find_profile(body2) is None and same_as(prof, S_CHUAN)
    verdict(c.log, tc, good, "Mong đợi ERR4 cho PUT và GET; EV3 (token hợp lệ) trả S_CHUAN")


def tc78(c, t):
    no_auth_case(c, t, "TC-PROF-78", "none", None)


def tc79(c, t):
    no_auth_case(c, t, "TC-PROF-79", "raw", "Bearer abc")


def tc80(c, t):
    c.log("  (1) Đăng nhập admin")
    ta = login(c, ADMIN_USER)
    if not ta:
        return
    _, before = get_profile(c, ta, "(2) EV3 admin trước")
    if c.dry_run:
        admin_id = "<id admin>"
    else:
        if before is None or "id" not in before:
            verdict(c.log, "TC-PROF-80", None, "BLOCKED: Phản hồi GET của admin không có id")
            return
        admin_id = before["id"]
    c.request("PUT", "/api/users/me", body_b(80, id=admin_id), auth="bearer", token=t)
    _, after = get_profile(c, ta, "(3) EV3 admin sau")
    get_profile(c, t, "EV3 test (ghi nhận)")
    if c.dry_run:
        return
    good = before is not None and after is not None and all(before.get(k) == after.get(k) for k in FIELDS + ("email", "role"))
    verdict(c.log, "TC-PROF-80", good, "Mong đợi OUT4: Hồ sơ admin không đổi")


def tc102(c, t):
    check_update(c, t, "TC-PROF-102", body_b(102, phone="09123456789"),
                 {"name": "Nguyen Van An 102", "phone": "09123456789"})


def tc76(c, t):
    c.request("PUT", "/api/users/me", body_b(76, email="tc76@eshop.com"), auth="bearer", token=t)
    if c.dry_run:
        return
    _, prof = get_profile(c, t)
    email = prof.get("email") if prof else None
    good = email == TEST_USER[0]
    verdict(c.log, "TC-PROF-76", good, f"Mong đợi OUT4: email vẫn test@eshop.com (EV3 trả {show(email)})")
    if not good:
        c.log("  !! Email có thể đã bị đổi: Ghi kết quả, reset dữ liệu mẫu ngay.")


def tc77(c, t):
    _, before = get_profile(c, t, "EV3 trước, ghi role")
    c.request("PUT", "/api/users/me", body_b(77, role="admin"), auth="bearer", token=t)
    _, after = get_profile(c, t, "EV3 sau")
    if c.dry_run:
        return
    if before is None or "role" not in before or after is None or "role" not in after:
        verdict(c.log, "TC-PROF-77", None, "KHÔNG QUAN SÁT ĐƯỢC: GET /api/users/me không trả role (giới hạn quan sát)")
        return
    good = before["role"] == after["role"]
    verdict(c.log, "TC-PROF-77", good, f"Mong đợi OUT4: role trước {show(before['role'])}, sau {show(after['role'])}")
    if not good:
        c.log("  !! Vai trò bị đổi: Ghi kết quả, reset dữ liệu mẫu ngay.")


RUN = [("TC-PROF-70", tc70), ("TC-PROF-71", tc71), ("TC-PROF-72", tc72), ("TC-PROF-73", tc73),
       ("TC-PROF-74", tc74), ("TC-PROF-75", tc75), ("TC-PROF-78", tc78), ("TC-PROF-79", tc79),
       ("TC-PROF-80", tc80), ("TC-PROF-102", tc102)]
LAST = [("TC-PROF-77", tc77), ("TC-PROF-76", tc76)]


# ---------------------------------------------------------------- main
def run_list(client, cases, only):
    wanted = {x.strip().upper() for x in only.split(",")} if only else None
    unknown = (wanted or set()) - {name for name, _ in cases}
    if unknown:
        client.log(f"!! Mã không thuộc lệnh này: {', '.join(sorted(unknown))}")
        return
    token = login(client, TEST_USER)
    if not token:
        return
    for name, fn in cases:
        if wanted and name not in wanted:
            continue
        client.log(f"\n=== {name} ===")
        if not set_chuan(client, token):
            return
        fn(client, token)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["chuan", "get", "run", "last"])
    p.add_argument("--only", help="Danh sách mã test case, cách nhau bằng dấu phẩy (lệnh run, last)")
    p.add_argument("--tag", help="Mã test case giao diện để ghi vào log (lệnh chuan, get)")
    p.add_argument("--base", default="http://localhost:3000")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    log = Log(a.command + (f"_{a.tag}" if a.tag else ""), a.dry_run)
    client = Client(a.base, log, a.dry_run)
    log(f"# FR-04 S6 {a.command}{' ' + a.tag if a.tag else ''}  {datetime.datetime.now():%Y-%m-%d %H:%M:%S}  base={a.base}"
        f"{'  (DRY RUN)' if a.dry_run else ''}")
    try:
        if a.command in ("chuan", "get"):
            token = login(client, TEST_USER)
            if token:
                if a.command == "chuan":
                    set_chuan(client, token)
                else:
                    get_profile(client, token)
        elif a.command == "run":
            run_list(client, RUN, a.only)
        else:
            log("Nhóm G: Chạy cuối cùng; reset dữ liệu mẫu ngay sau (05_final_tc.md mục 9 bước 6)")
            run_list(client, LAST, a.only)
    finally:
        log.save()


if __name__ == "__main__":
    main()
