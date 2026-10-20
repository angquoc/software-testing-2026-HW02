#!/usr/bin/env python3
"""S6, FR-01: Chạy TC-REG-79 (Họ Tên chứa lệnh DROP TABLE), CUỐI CÙNG trong đợt test.

Nếu EShop bị lỗi SQL injection, request này có thể xóa hoặc làm hỏng dữ liệu người dùng.
Vì vậy (05_final_tc.md mục 10):
  1. Chỉ chạy sau khi mọi test case khác đã xong.
  2. Sau bước 1, làm bước 2 qua giao diện (script in lời nhắc).
  3. Reset dữ liệu EShop ngay sau khi xong.

Cách dùng:
  python run_tc79.py              Hỏi xác nhận rồi gửi
  python run_tc79.py --yes        Không hỏi xác nhận
  python run_tc79.py --dry-run    In request, không gửi
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
SUCCESS_MESSAGE = "User registered successfully"
BODY = {"name": "Robert'); DROP TABLE users;--", "email": "tc79@domain.com", "password": "Abcdef1!"}
STEP2 = ("Bước 2 (làm tay qua giao diện): Đăng ký test@eshop.com, Họ Tên Nguyen Van A, "
         "mật khẩu Abcdef1!. Mong đợi OUT2, ERR4 (dữ liệu có sẵn vẫn còn nguyên)")


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


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default="http://localhost:3000")
    p.add_argument("--yes", action="store_true", help="Không hỏi xác nhận")
    p.add_argument("--dry-run", action="store_true", help="In request, không gửi")
    p.add_argument("--timeout", type=float, default=10)
    args = p.parse_args()

    print("CẢNH BÁO: TC-REG-79 có thể làm hỏng dữ liệu người dùng nếu EShop bị lỗi SQL injection.")
    print("Chỉ chạy khi mọi test case khác đã xong. Reset dữ liệu ngay sau khi chạy.")
    if not args.dry_run and not args.yes:
        if input('Gõ "CHAY" để tiếp tục: ').strip() != "CHAY":
            print("Đã hủy, chưa gửi gì.")
            return

    here = os.path.dirname(os.path.abspath(__file__))
    now = datetime.datetime.now()
    log_path = None
    if not args.dry_run:
        log_dir = os.path.join(here, "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.normpath(os.path.join(log_dir, f"S6_tc79_{now:%Y%m%d_%H%M%S}.log"))
    log = Logger(log_path)

    log("S6, FR-01: TC-REG-79, Họ Tên chứa lệnh DROP TABLE (chạy cuối cùng)")
    log(f"Thời gian: {now:%Y-%m-%d %H:%M:%S}")
    log(f"Chế độ: {'dry-run (không gửi)' if args.dry_run else 'gửi thật'}")
    log("Mong đợi bước 1: OUT3, không xuất hiện lỗi hệ thống")
    log("-" * 78)
    log(f"Request: POST {args.base_url}{ENDPOINT}")
    log("Header: Content-Type: application/json; charset=utf-8")
    log(f"Body: {json.dumps(BODY, ensure_ascii=False)}")
    if not args.dry_run:
        status, resp, err = send(args.base_url, BODY, args.timeout)
        if err:
            log(f"LỖI: {err}")
        else:
            log(f"Response: HTTP {status}")
            try:
                data = json.loads(resp)
                for line in json.dumps(data, ensure_ascii=False, indent=2).splitlines():
                    log("  " + line)
                ok = (status == 200 and isinstance(data, dict) and data.get("message") == SUCCESS_MESSAGE
                      and isinstance(data.get("id"), (int, float)))
            except ValueError:
                log(f"Body phản hồi (không phải JSON): {resp!r}")
                ok = False
            log(f"Gợi ý: {'Khớp OUT3' if ok else 'Không khớp OUT3'}")
    log("")
    log(f">>> VIỆC LÀM TAY: {STEP2}")
    log(">>> Nếu bước 2 KHÔNG cho ERR4: Ghi kết quả, rồi reset trước khi chạy lại bất kỳ test case nào.")
    log(">>> Sau đó: Reset dữ liệu EShop ngay, ghi thời điểm reset vào 06_results.md mục 1.")
    if log_path:
        log(f"Log: {log_path}")
    log.close()


if __name__ == "__main__":
    main()
