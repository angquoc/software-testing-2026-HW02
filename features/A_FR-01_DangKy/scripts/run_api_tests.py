#!/usr/bin/env python3
"""S6, FR-01: Chạy nhóm test case API (TS-04 và TC-REG-78) của 05_final_tc.md.

Sinh viên tự chạy script này. Mỗi test case: In request và response (mã HTTP, body),
ghi cùng nội dung vào file log trong ../logs/. Test case có bước làm tay qua giao diện
thì script in lời nhắc (cả lúc chạy và trong danh sách cuối log).

Không gồm TC-REG-79 (chuỗi DROP TABLE): Chạy riêng bằng run_tc79.py, cuối cùng.

Cách dùng (chạy từ bất kỳ thư mục nào):
  python run_api_tests.py                      Chạy tất cả theo thứ tự
  python run_api_tests.py --only 70,81         Chỉ chạy TC-REG-70 và TC-REG-81
  python run_api_tests.py --dry-run            In request, không gửi gì (để kiểm script)
  python run_api_tests.py --base-url http://localhost:3000

Cột "Gợi ý" trong log chỉ so máy móc với OUT3 (HTTP 200, message đúng, id là số).
Trạng thái Pass, Fail do sinh viên quyết định khi điền 06_results.md.
"""
import argparse
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ENDPOINT = "/api/register"
BASE_NAME = "Nguyen Van A"
BASE_PASSWORD = "Abcdef1!"
SUCCESS_MESSAGE = "User registered successfully"

# Mỗi test case: id, tiêu đề, body, kết quả mong đợi, có kiểm chứng "không tạo tài khoản" không,
# lời nhắc bước làm tay (nếu có). Khoảng trắng trong chuỗi là dấu cách thật.
TESTS = [
    ("TC-REG-70", "API đăng ký thành công với dữ liệu hợp lệ",
     {"name": BASE_NAME, "email": "tc70@domain.com", "password": BASE_PASSWORD},
     "OUT3. Body không chứa mật khẩu ở bất kỳ dạng nào", False, None),
    ("TC-REG-71", "API từ chối khi name rỗng",
     {"name": "", "email": "tc71@domain.com", "password": BASE_PASSWORD},
     "OUT4; kiểm chứng không tạo tài khoản", True, None),
    ("TC-REG-72", "API từ chối khi name chỉ gồm 3 dấu cách",
     {"name": "   ", "email": "tc72@domain.com", "password": BASE_PASSWORD},
     "OUT4; kiểm chứng không tạo tài khoản", True, None),
    ("TC-REG-73", "API từ chối khi email rỗng",
     {"name": BASE_NAME, "email": "", "password": BASE_PASSWORD},
     "OUT4", False, None),
    ("TC-REG-74", "API từ chối khi email thiếu @",
     {"name": BASE_NAME, "email": "tc74domain.com", "password": BASE_PASSWORD},
     "OUT4", False, None),
    ("TC-REG-75", "API từ chối khi password rỗng",
     {"name": BASE_NAME, "email": "tc75@domain.com", "password": ""},
     "OUT4; kiểm chứng không tạo tài khoản", True, None),
    ("TC-REG-76", "API từ chối khi password có 6 ký tự",
     {"name": BASE_NAME, "email": "tc76@domain.com", "password": "Abcd1!"},
     "OUT4; kiểm chứng không tạo tài khoản", True, None),
    ("TC-REG-77", "API từ chối khi password không có ký tự đặc biệt",
     {"name": BASE_NAME, "email": "tc77@domain.com", "password": "Abcdefg1"},
     "OUT4; kiểm chứng không tạo tài khoản", True, None),
    ("TC-REG-78", "Email chứa chuỗi SQL được lưu và so sánh nguyên văn (bước 1)",
     {"name": BASE_NAME, "email": "tc78'or'1'='1@domain.com", "password": BASE_PASSWORD},
     "Bước 1: OUT3, không xuất hiện lỗi hệ thống", False,
     "Bước 2 (làm tay qua giao diện): Đăng ký lại đúng email tc78'or'1'='1@domain.com, "
     "Họ Tên Tran Thi B, mật khẩu Abcdef1!. Mong đợi OUT2, ERR4"),
    ("TC-REG-80", "API từ chối khi email chỉ gồm 3 dấu cách",
     {"name": BASE_NAME, "email": "   ", "password": BASE_PASSWORD},
     "OUT4", False, None),
    ("TC-REG-81", "API lưu email đã cắt dấu cách đầu cuối (bước 1)",
     {"name": BASE_NAME, "email": " tc81@domain.com ", "password": BASE_PASSWORD},
     "Bước 1: OUT3", False,
     "Bước 2 (làm tay qua giao diện): Đăng ký tc81@domain.com (không có dấu cách), "
     "Họ Tên Tran Thi B, mật khẩu Abcdef1!. Mong đợi OUT2, ERR4"),
    ("TC-REG-82", "API từ chối email trùng sau khi cắt dấu cách đầu cuối",
     {"name": BASE_NAME, "email": " test@eshop.com ", "password": BASE_PASSWORD},
     "OUT4. Nếu OUT3 thì EShop không cắt dấu cách khi so trùng", False, None),
    ("TC-REG-129", "API từ chối khi password dài 7 ký tự",
     {"name": BASE_NAME, "email": "tc129@domain.com", "password": "Abcde1!"},
     "OUT4; kiểm chứng không tạo tài khoản", True, None),
    ("TC-REG-130", "API từ chối khi nhãn tên miền dài 64 ký tự",
     {"name": BASE_NAME, "email": "tc130@" + "a" * 64 + ".com", "password": BASE_PASSWORD},
     "OUT4", False, None),
]


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


def show_body(body):
    """JSON, kèm chú thích độ dài và dấu cách đầu cuối của từng trường chuỗi."""
    text = json.dumps(body, ensure_ascii=False)
    notes = []
    for k, v in body.items():
        if isinstance(v, str):
            extra = []
            if v != v.strip():
                extra.append("có dấu cách đầu hoặc cuối")
            if v and not v.strip():
                extra.append("chỉ gồm dấu cách")
            notes.append(f"{k}: {len(v)} ký tự" + (f" ({', '.join(extra)})" if extra else ""))
    return text, "; ".join(notes)


def send(base_url, body, timeout):
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(base_url + ENDPOINT, data=data, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace"), None
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace"), None
    except (urllib.error.URLError, OSError) as e:
        return None, "", f"Không gửi được request: {e}"


def hint(status, text):
    """So máy móc với OUT3; không thay cho đánh giá của sinh viên."""
    if status is None:
        return "Không có phản hồi"
    try:
        data = json.loads(text)
    except ValueError:
        data = None
    ok = (status == 200 and isinstance(data, dict) and data.get("message") == SUCCESS_MESSAGE
          and isinstance(data.get("id"), (int, float)) and not isinstance(data.get("id"), bool))
    return "Khớp OUT3" if ok else "Không khớp OUT3 (tức là OUT4 nếu test case mong đợi bị từ chối)"


def password_leak(text, password):
    """Gợi ý cho TC-REG-70: Body có chứa mật khẩu nguyên văn hay trường tên giống mật khẩu không."""
    found = []
    if password and password in text:
        found.append("có chuỗi mật khẩu nguyên văn")
    try:
        data = json.loads(text)
    except ValueError:
        data = None

    def walk(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if any(w in k.lower() for w in ("pass", "pwd", "hash", "secret")):
                    found.append(f"có trường {path + k}")
                walk(v, path + k + ".")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk(v, f"{path}[{i}].")
    walk(data)
    return "; ".join(found) if found else "Không thấy mật khẩu hay trường giống mật khẩu"


def run_one(log, base_url, timeout, dry, label, body):
    text, notes = show_body(body)
    log(f"  Request: POST {base_url}{ENDPOINT}")
    log("  Header: Content-Type: application/json; charset=utf-8")
    log(f"  Body: {text}")
    log(f"  Ghi chú body: {notes}")
    if dry:
        log("  (dry-run: không gửi)")
        return None, ""
    status, resp, err = send(base_url, body, timeout)
    if err:
        log(f"  LỖI: {err}")
        return None, ""
    log(f"  Response: HTTP {status}")
    try:
        pretty = json.dumps(json.loads(resp), ensure_ascii=False, indent=2)
        log("  Body phản hồi:")
        for line in pretty.splitlines():
            log("    " + line)
    except ValueError:
        log(f"  Body phản hồi (không phải JSON): {resp!r}")
    log(f"  Gợi ý ({label}): {hint(status, resp)}")
    return status, resp


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default="http://localhost:3000")
    p.add_argument("--only", help="Danh sách số test case, ví dụ 70,81,129")
    p.add_argument("--dry-run", action="store_true", help="In request, không gửi")
    p.add_argument("--timeout", type=float, default=10)
    args = p.parse_args()

    tests = TESTS
    if args.only:
        wanted = {f"TC-REG-{int(x):02d}" for x in args.only.split(",") if x.strip()}
        tests = [t for t in TESTS if t[0] in wanted]

    here = os.path.dirname(os.path.abspath(__file__))
    now = datetime.datetime.now()
    log_path = None
    if not args.dry_run:
        log_dir = os.path.join(here, "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.normpath(os.path.join(log_dir, f"S6_api_{now:%Y%m%d_%H%M%S}.log"))
    log = Logger(log_path)

    log("S6, FR-01: Nhóm test case API")
    log(f"Thời gian bắt đầu: {now:%Y-%m-%d %H:%M:%S}")
    log(f"Base URL: {args.base_url}")
    log(f"Chế độ: {'dry-run (không gửi)' if args.dry_run else 'gửi thật'}")
    log(f"Số test case: {len(tests)}")
    manual = []

    for tc, title, body, expected, verify, manual_step in tests:
        log("")
        log("=" * 78)
        log(f"{tc}: {title}")
        log(f"Mong đợi: {expected}")
        log("-" * 78)
        status, resp = run_one(log, args.base_url, args.timeout, args.dry_run, "request chính", body)
        if tc == "TC-REG-70" and not args.dry_run and status is not None:
            log(f"  Gợi ý FR01-R23: {password_leak(resp, body['password'])}")
        if verify:
            vbody = {"name": BASE_NAME, "email": body["email"], "password": BASE_PASSWORD}
            log("  Kiểm chứng không tạo tài khoản: Gửi lại cùng email với dữ liệu hợp lệ; mong đợi OUT3")
            run_one(log, args.base_url, args.timeout, args.dry_run, "kiểm chứng", vbody)
        if manual_step:
            log(f"  >>> VIỆC LÀM TAY: {manual_step}")
            manual.append(f"{tc}: {manual_step}")

    log("")
    log("=" * 78)
    log(f"Kết thúc: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
    if manual:
        log("Việc làm tay qua giao diện còn lại:")
        for m in manual:
            log(f"  - {m}")
    log("Nhắc: TC-REG-79 chạy riêng bằng run_tc79.py, sau cùng, rồi reset dữ liệu.")
    if log_path:
        log(f"Log: {log_path}")
    log.close()


if __name__ == "__main__":
    main()
