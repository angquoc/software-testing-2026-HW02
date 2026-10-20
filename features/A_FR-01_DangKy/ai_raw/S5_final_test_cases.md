# S5: Bộ test case cuối cùng (FR-01 Đăng ký tài khoản)

- Bước: S5 (Review lần cuối, bổ sung test case AI bỏ sót). Bản này do AI gộp `03_tc.md` và `04_bva.md`; sinh viên review và bổ sung ngay trong `05_final_tc.md`
- Thời gian tạo: 2026-10-20 16:02 (+07:00)
- Căn cứ: `03_tc.md` (bản review S3, 72 test case), `04_bva.md` (bản review S4, 24 test case), `ai_raw/S3_test_cases.md` và `ai_raw/S4_bva.md` (để xác định nguồn gốc), `02_ec.md` (lớp), `00_spec.md` (yêu cầu)

---

## 1. Cách gộp và quy ước

### 1.1 Nguồn gốc

| Giá trị | Nghĩa | Ứng với trường `origin` của skill `test-case-writing` |
|---|---|---|
| AI | Test case có trong bản AI (`ai_raw/S3_test_cases.md` hoặc `ai_raw/S4_bva.md`) và giữ nguyên nội dung. Chỉ đổi mã, hoặc email đổi theo số mới một cách máy móc, vẫn tính là AI | `AI` |
| AI có SV sửa | Test case có trong bản AI nhưng đã đổi giá trị kiểm, kết quả mong đợi, bước, hoặc ghi chú giới hạn; hoặc test case mới do AI (phiên này hay phiên khác) đề xuất khi review | `Both` |
| SV thêm | Test case mới do sinh viên phát hiện thiếu khi review, hoặc sinh viên tự viết ở S5 | `Human` |

Chi tiết từng test case không phải "AI" (mã trong bản AI, đã đổi gì, ai phát hiện) ở mục 9.1.

### 1.2 Ký hiệu và kết quả mong đợi

- `␣` là **một dấu cách**. Chuỗi dài viết dạng "`tc118@` + 62 chữ `a` + `.com`".
- Mã test case giữ như `03_tc.md` và `04_bva.md`; mã đã bỏ không dùng lại (mục 9.3).

| Mã | Kết quả mong đợi |
|---|---|
| OUT1 | Đường dẫn đổi thành `/login` và trang hiện form đăng nhập (có ô nhập và nút gửi) |
| OUT2, ERRn | Có thông báo lỗi chỉ ra đúng nguyên nhân ERRn; vẫn ở `/register`. Không ghi câu chữ cụ thể vì đặc tả không nêu |
| ERR1 đến ERR7 | ERR1 thiếu Họ Tên; ERR2 thiếu Email; ERR3 Email sai định dạng; ERR4 Email đã tồn tại; ERR5 thiếu Mật khẩu; ERR6 Mật khẩu không đạt yêu cầu mạnh; ERR7 Mật khẩu và Xác nhận mật khẩu không khớp |
| OUT3 | API trả HTTP 200 OK, body có `"message": "User registered successfully"` và `id` là số |
| OUT4 | API không trả về phản hồi thành công như OUT3. Ghi lại mã HTTP và body thực tế |

### 1.3 Tiền điều kiện chung

- Chưa đăng nhập.
- Dữ liệu EShop đã reset về dữ liệu mẫu (có `test@eshop.com`, `admin@eshop.com`).
- Giao diện: Chrome, mở `http://localhost:5173/register`; ghi phiên bản Chrome ở S6.
- API: `POST http://localhost:3000/api/register`, header `Content-Type: application/json`.

### 1.4 Quy trình chung cho test case giao diện

1. Mở `http://localhost:5173/register`.
2. Nhập Họ Tên, Email, Mật khẩu theo bảng.
3. Nhập Xác nhận mật khẩu theo bảng. Giao diện hiện không có trường này (D01): Với test case không nhắm vào Xác nhận mật khẩu thì bỏ qua bước này và ghi chú vào kết quả; với TC-REG-59 đến TC-REG-62 thì ghi Blocked.
4. Nhấn nút "Đăng Ký".
5. So kết quả với cột "Kết quả mong đợi".

---

## 2. Tổng hợp

| Nhóm | Mã | Số TC | AI | AI có SV sửa | SV thêm |
|---|---|---|---|---|---|
| TS-01 Hợp lệ qua giao diện (EP) | TC-REG-01 đến TC-REG-18 | 18 | 2 | 16 | 0 |
| TS-02 Không hợp lệ qua giao diện (EP) | TC-REG-30 đến TC-REG-62 | 33 | 30 | 3 | 0 |
| TS-03 Giá trị biên qua giao diện (BVA) | TC-REG-101 đến TC-REG-123, TC-REG-131 | 22 | 21 | 0 | 1 |
| TS-04 API (EP, BVA) | TC-REG-70 đến TC-REG-77, TC-REG-80 đến TC-REG-82, TC-REG-129, TC-REG-130 | 13 | 9 | 4 | 0 |
| TS-05 Bảo mật | TC-REG-78, TC-REG-79 | 2 | 0 | 2 | 0 |
| TS-06 Checklist giao diện | TC-REG-90 đến TC-REG-97 | 8 | 8 | 0 | 0 |
| **Tổng** | | **96** | **70** | **25** | **1** |

Theo kỹ thuật: 72 test case Domain Testing (EP) và checklist từ S3, 24 test case BVA từ S4. Dự kiến Blocked: 4 (TC-REG-59 đến TC-REG-62, do D01).

---

## 3. TS-01: Đăng ký hợp lệ qua giao diện (EP)

| TC | Tiêu đề | Lớp | Yêu cầu | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu | Kết quả mong đợi | Nguồn gốc |
|---|---|---|---|---|---|---|---|---|---|
| TC-REG-01 | Kiểm tra đăng ký thành công với dữ liệu hợp lệ cơ sở | EC01, EC04, EC08, EC11, EC20, EC24, EC26, EC28, EC31, EC34, EC36 (`!`), EC41, EC46 | FR01-R01 đến FR01-R10, FR01-R13 | `Nguyen Van A` | `tc01@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-02 | Kiểm tra đăng ký thành công khi Họ Tên có chữ tiếng Việt có dấu | EC05; EC36 (`@`) | FR01-R01, FR01-R10, FR01-R13 | `Nguyễn Thị Ánh` | `tc02@domain.com` | `Abcdef1@` | `Abcdef1@` | OUT1 | AI có SV sửa |
| TC-REG-03 | Kiểm tra đăng ký thành công khi Họ Tên có chữ số | EC06; EC36 (`$`) | FR01-R01, FR01-R10, FR01-R13 | `Nguyen Van A2` | `tc03@domain.com` | `Abcdef1$` | `Abcdef1$` | OUT1 | AI có SV sửa |
| TC-REG-04 | Kiểm tra đăng ký thành công khi Họ Tên có dấu gạch nối | EC56; EC36 (`%`) | FR01-R01, FR01-R10, FR01-R13 | `Anh-Ngoc` | `tc04@domain.com` | `Abcdef1%` | `Abcdef1%` | OUT1 | AI có SV sửa |
| TC-REG-05 | Kiểm tra đăng ký thành công khi Họ Tên chỉ gồm chữ số | EC55; EC36 (`*`) | FR01-R01, FR01-R10, FR01-R13 | `12345` | `tc05@domain.com` | `Abcdef1*` | `Abcdef1*` | OUT1 | AI có SV sửa |
| TC-REG-06 | Kiểm tra đăng ký thành công khi Họ Tên có dấu cách ở đầu và cuối | EC54; EC36 (`?`) | FR01-R01, FR01-R10, FR01-R13 | `␣Nguyen Van A␣` | `tc06@domain.com` | `Abcdef1?` | `Abcdef1?` | OUT1. Giới hạn GH1 | AI có SV sửa |
| TC-REG-07 | Kiểm tra đăng ký thành công khi Họ Tên có 2 dấu cách liền nhau ở giữa | EC70; EC36 (`&`) | FR01-R01, FR01-R10, FR01-R13 | `Nguyen␣␣Van A` | `tc07@domain.com` | `Abcdef1&` | `Abcdef1&` | OUT1. Giới hạn GH1 | AI có SV sửa |
| TC-REG-08 | Kiểm tra đăng ký thành công khi Họ Tên có thẻ HTML và dấu nháy đơn | EC07 | FR01-R01, FR01-R13, FR01-R24, FR01-R25 | `<b>O'Brien</b>` | `tc08@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1, không xuất hiện lỗi hệ thống. Giới hạn GH5 | AI |
| TC-REG-09 | Kiểm tra đăng ký thành công khi Email có dấu chấm ở phần trước `@` và có tên miền con | EC12 | FR01-R04, FR01-R13 | `Nguyen Van A` | `tc.09@mail.domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI có SV sửa |
| TC-REG-10 | Kiểm tra đăng ký thành công khi phần sau `@` không có dấu chấm | EC16 | FR01-R04, FR01-R13 | `Nguyen Van A` | `tc10@domain` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI có SV sửa |
| TC-REG-11 | Kiểm tra đăng ký thành công khi Email có dấu cách ở đầu và cuối | EC19 | FR01-R04, FR01-R05, FR01-R13 | `Nguyen Van A` | `␣tc11@domain.com␣` | `Abcdef1!` | `Abcdef1!` | Bước 1: OUT1. Bước 2: Mở lại `/register`, đăng ký `tc11@domain.com` với Họ Tên `Tran Thi B`, mật khẩu `Abcdef1!`; mong đợi OUT2, ERR4. Giới hạn GH2 | AI có SV sửa |
| TC-REG-12 | Kiểm tra đăng ký thành công khi Email bắt đầu bằng dấu chấm | EC57 | FR01-R04, FR01-R13 | `Nguyen Van A` | `.tc12@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI có SV sửa |
| TC-REG-13 | Kiểm tra đăng ký thành công khi Email có dấu cộng ở phần trước `@` | EC59 | FR01-R04, FR01-R13 | `Nguyen Van A` | `tc+13@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI có SV sửa |
| TC-REG-14 | Kiểm tra đăng ký thành công khi tên miền có chữ có dấu | EC65 | FR01-R04, FR01-R13 | `Nguyen Van A` | `tc14@tênmiền.vn` | `Abcdef1!` | `Abcdef1!` | OUT1. Giới hạn GH6 | AI có SV sửa |
| TC-REG-15 | Kiểm tra đăng ký thành công khi Email có dấu nháy đơn | EC66 | FR01-R04, FR01-R13, FR01-R25 | `Nguyen Van A` | `tc'15@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1, không xuất hiện lỗi hệ thống | AI có SV sửa |
| TC-REG-16 | Kiểm tra đăng ký thành công khi Mật khẩu có dấu cách ở giữa | EC39 | FR01-R06, FR01-R13 | `Nguyen Van A` | `tc16@domain.com` | `Abc def1!` | `Abc def1!` | OUT1. Giới hạn GH3 | AI có SV sửa |
| TC-REG-17 | Kiểm tra đăng ký thành công khi Mật khẩu có ký tự ngoài 4 loại | EC40 | FR01-R06 đến FR01-R10, FR01-R13 | `Nguyen Van A` | `tc17@domain.com` | `Abcdef1!é` | `Abcdef1!é` | OUT1 | AI có SV sửa |
| TC-REG-18 | Kiểm tra đăng ký thành công khi Mật khẩu đủ 8 ký tự nhờ dấu cách ở cuối | EC68 | FR01-R06, FR01-R13 | `Nguyen Van A` | `tc18@domain.com` | `Abcde1!␣` (8 ký tự) | `Abcde1!␣` | OUT1. Giới hạn GH3 | AI có SV sửa |

---

## 4. TS-02: Đăng ký không hợp lệ qua giao diện (EP)

Mỗi test case chỉ vi phạm đúng một lớp không hợp lệ, trừ TC-REG-58 (ngoại lệ đã ghi ở `02_ec.md`, EC69).

| TC | Tiêu đề | Lớp | Yêu cầu | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu | Kết quả mong đợi | Nguồn gốc |
|---|---|---|---|---|---|---|---|---|---|
| TC-REG-30 | Kiểm tra đăng ký bị từ chối khi Họ Tên để trống | EC02 | FR01-R01 | (để trống) | `tc30@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR1 | AI |
| TC-REG-31 | Kiểm tra đăng ký bị từ chối khi Họ Tên chỉ gồm 3 dấu cách | EC03 | FR01-R01 | `␣␣␣` | `tc31@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR1 | AI |
| TC-REG-32 | Kiểm tra đăng ký bị từ chối khi Email để trống | EC09 | FR01-R02 | `Nguyen Van A` | (để trống) | `Abcdef1!` | `Abcdef1!` | OUT2, ERR2 | AI |
| TC-REG-33 | Kiểm tra đăng ký bị từ chối khi Email chỉ gồm 3 dấu cách | EC10 | FR01-R02 | `Nguyen Van A` | `␣␣␣` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR2. Giới hạn GH2 | AI có SV sửa |
| TC-REG-34 | Kiểm tra đăng ký bị từ chối khi Email thiếu `@` | EC13 | FR01-R04 | `Nguyen Van A` | `tc34domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-35 | Kiểm tra đăng ký bị từ chối khi Email thiếu phần trước `@` | EC14 | FR01-R04 | `Nguyen Van A` | `@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-36 | Kiểm tra đăng ký bị từ chối khi Email thiếu phần sau `@` | EC15 | FR01-R04 | `Nguyen Van A` | `tc36@` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-37 | Kiểm tra đăng ký bị từ chối khi Email có 2 dấu `@` | EC17 | FR01-R04 | `Nguyen Van A` | `tc37@@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-38 | Kiểm tra đăng ký bị từ chối khi Email có dấu cách ở giữa | EC18 | FR01-R04 | `Nguyen Van A` | `tc␣38@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-39 | Kiểm tra đăng ký bị từ chối khi có dấu chấm ngay sau `@` | EC58 | FR01-R04 | `Nguyen Van A` | `tc39@.domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-40 | Kiểm tra đăng ký bị từ chối khi phần trước `@` có dấu ngoặc | EC60 | FR01-R04 | `Nguyen Van A` | `tc(40)@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-41 | Kiểm tra đăng ký bị từ chối khi tên miền có dấu gạch dưới | EC61 | FR01-R04 | `Nguyen Van A` | `tc41@do_main.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-42 | Kiểm tra đăng ký bị từ chối khi nhãn tên miền bắt đầu bằng dấu gạch nối | EC62 | FR01-R04 | `Nguyen Van A` | `tc42@-domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-43 | Kiểm tra đăng ký bị từ chối khi nhãn tên miền dài 70 ký tự | EC63 | FR01-R04 | `Nguyen Van A` | `tc43@` + 70 chữ `a` + `.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-44 | Kiểm tra đăng ký bị từ chối khi phần trước `@` có chữ có dấu | EC64 | FR01-R04 | `Nguyen Van A` | `tcđ44@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI có SV sửa |
| TC-REG-45 | Kiểm tra đăng ký bị từ chối khi Email trùng tài khoản có sẵn | EC21 | FR01-R05 | `Nguyen Van A` | `test@eshop.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR4 | AI |
| TC-REG-46 | Kiểm tra đăng ký bị từ chối khi Email trùng email vừa đăng ký | EC22 | FR01-R05 | Lần 1: `Nguyen Van A`; lần 2: `Tran Thi B` | `tc46@domain.com` (cả hai lần) | `Abcdef1!` | `Abcdef1!` | Lần 1: OUT1. Lần 2: OUT2, ERR4 | AI |
| TC-REG-47 | Kiểm tra đăng ký bị từ chối khi Email trùng nhưng khác chữ hoa, chữ thường | EC23 | FR01-R05 | `Nguyen Van A` | `Test@Eshop.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR4 | AI |
| TC-REG-48 | Kiểm tra đăng ký bị từ chối khi Email trùng sau khi cắt dấu cách đầu cuối | EC67 | FR01-R05 | `Nguyen Van A` | `␣test@eshop.com␣` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR4. Giới hạn GH2 | AI có SV sửa |
| TC-REG-49 | Kiểm tra đăng ký bị từ chối khi Mật khẩu để trống | EC25 | FR01-R03 | `Nguyen Van A` | `tc49@domain.com` | (để trống) | (để trống) | OUT2, ERR5 | AI |
| TC-REG-50 | Kiểm tra đăng ký bị từ chối khi Mật khẩu có 6 ký tự | EC27 | FR01-R06 | `Nguyen Van A` | `tc50@domain.com` | `Abcd1!` | `Abcd1!` | OUT2, ERR6 | AI |
| TC-REG-51 | Kiểm tra đăng ký bị từ chối khi Mật khẩu không có chữ hoa | EC29 | FR01-R07 | `Nguyen Van A` | `tc51@domain.com` | `abcdef1!` | `abcdef1!` | OUT2, ERR6 | AI |
| TC-REG-52 | Kiểm tra đăng ký bị từ chối khi chữ hoa duy nhất của Mật khẩu là chữ có dấu | EC30 | FR01-R07 | `Nguyen Van A` | `tc52@domain.com` | `Ăbcdef1!` | `Ăbcdef1!` | OUT2, ERR6 | AI |
| TC-REG-53 | Kiểm tra đăng ký bị từ chối khi Mật khẩu không có chữ thường | EC32 | FR01-R08 | `Nguyen Van A` | `tc53@domain.com` | `ABCDEF1!` | `ABCDEF1!` | OUT2, ERR6 | AI |
| TC-REG-54 | Kiểm tra đăng ký bị từ chối khi chữ thường duy nhất của Mật khẩu là chữ có dấu | EC33 | FR01-R08 | `Nguyen Van A` | `tc54@domain.com` | `ABCDEă1!` | `ABCDEă1!` | OUT2, ERR6 | AI |
| TC-REG-55 | Kiểm tra đăng ký bị từ chối khi Mật khẩu không có chữ số | EC35 | FR01-R09 | `Nguyen Van A` | `tc55@domain.com` | `Abcdefg!` | `Abcdefg!` | OUT2, ERR6 | AI |
| TC-REG-56 | Kiểm tra đăng ký bị từ chối khi Mật khẩu không có ký tự đặc biệt | EC37 | FR01-R10 | `Nguyen Van A` | `tc56@domain.com` | `Abcdefg1` | `Abcdefg1` | OUT2, ERR6 | AI |
| TC-REG-57 | Kiểm tra đăng ký bị từ chối khi ký tự đặc biệt duy nhất nằm ngoài tập cho phép | EC38 | FR01-R10 | `Nguyen Van A` | `tc57@domain.com` | `Abcdef1#` | `Abcdef1#` | OUT2, ERR6 | AI |
| TC-REG-58 | Kiểm tra đăng ký bị từ chối khi Mật khẩu chỉ gồm 8 dấu cách | EC69 (ngoại lệ) | FR01-R03, FR01-R06 đến FR01-R10 | `Nguyen Van A` | `tc58@domain.com` | `␣␣␣␣␣␣␣␣` | `␣␣␣␣␣␣␣␣` | OUT2, **ERR6** (không phải ERR5) | AI |
| TC-REG-59 | Kiểm tra đăng ký bị từ chối khi Xác nhận mật khẩu khác Mật khẩu | EC42 | FR01-R11, FR01-R12 | `Nguyen Van A` | `tc59@domain.com` | `Abcdef1!` | `Abcdef2!` | OUT2, ERR7. Dự kiến Blocked (D01) | AI |
| TC-REG-60 | Kiểm tra đăng ký bị từ chối khi Xác nhận mật khẩu để trống | EC43 | FR01-R11, FR01-R12 | `Nguyen Van A` | `tc60@domain.com` | `Abcdef1!` | (để trống) | OUT2, ERR7. Dự kiến Blocked (D01) | AI |
| TC-REG-61 | Kiểm tra đăng ký bị từ chối khi Xác nhận mật khẩu chỉ khác chữ hoa, chữ thường | EC44 | FR01-R11, FR01-R12 | `Nguyen Van A` | `tc61@domain.com` | `Abcdef1!` | `abcdef1!` | OUT2, ERR7. Dự kiến Blocked (D01) | AI |
| TC-REG-62 | Kiểm tra đăng ký bị từ chối khi Xác nhận mật khẩu thừa dấu cách ở cuối | EC45 | FR01-R11, FR01-R12 | `Nguyen Van A` | `tc62@domain.com` | `Abcdef1!` | `Abcdef1!␣` | OUT2, ERR7. Dự kiến Blocked (D01) | AI |

---

## 5. TS-03: Giá trị biên qua giao diện (BVA)

| TC | Tiêu đề | Biên | Yêu cầu | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu | Kết quả mong đợi | Nguồn gốc |
|---|---|---|---|---|---|---|---|---|---|
| TC-REG-101 | Kiểm tra đăng ký thành công khi Họ Tên dài 1 ký tự | P1, LB | FR01-R01 | `A` | `tc101@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-131 | Kiểm tra đăng ký thành công khi Họ Tên 1 ký tự có dấu cách hai bên | P1, LB có khoảng trắng | FR01-R01 | `␣A␣` | `tc131@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | SV thêm |
| TC-REG-102 | Kiểm tra đăng ký thành công khi Họ Tên dài 2 ký tự | P1, LB+1 | FR01-R01 | `An` | `tc102@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-103 | Kiểm tra đăng ký với Họ Tên dài 1000 ký tự | P1, lớn nhất giao diện cho nhập | FR01-R01 | 1000 chữ `a` (dán vào ô) | `tc103@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1. Ghi số ký tự ô thực sự nhận. Giới hạn GH7 | AI |
| TC-REG-104 | Kiểm tra đăng ký bị từ chối khi Họ Tên là 1 dấu cách | P7, LB | FR01-R01 | `␣` | `tc104@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR1 | AI |
| TC-REG-106 | Kiểm tra đăng ký bị từ chối khi Mật khẩu dài 4 ký tự | P2, nhỏ nhất chỉ vi phạm độ dài | FR01-R06 | `Nguyen Van A` | `tc106@domain.com` | `Aa1!` | `Aa1!` | OUT2, ERR6 | AI |
| TC-REG-107 | Kiểm tra đăng ký bị từ chối khi Mật khẩu dài 7 ký tự | P2, LB-1 | FR01-R06 | `Nguyen Van A` | `tc107@domain.com` | `Abcde1!` | `Abcde1!` | OUT2, ERR6 | AI |
| TC-REG-108 | Kiểm tra đăng ký thành công khi Mật khẩu dài 9 ký tự | P2, LB+1 | FR01-R06 | `Nguyen Van A` | `tc108@domain.com` | `Abcdefg1!` | `Abcdefg1!` | OUT1 | AI |
| TC-REG-110 | Kiểm tra đăng ký với Mật khẩu dài 1000 ký tự | P2, lớn nhất giao diện cho nhập | FR01-R06 | `Nguyen Van A` | `tc110@domain.com` | `Abcdef1!` + 992 chữ `a` | Giống Mật khẩu | OUT1. Ghi số ký tự ô thực sự nhận. Giới hạn GH3, GH7 | AI |
| TC-REG-111 | Kiểm tra đăng ký thành công khi Mật khẩu đủ 8 ký tự nhờ dấu cách ở đầu | P2, LB có khoảng trắng ở đầu | FR01-R06 | `Nguyen Van A` | `tc111@domain.com` | `␣Abcde1!` | `␣Abcde1!` | OUT1. Giới hạn GH3 | AI |
| TC-REG-112 | Kiểm tra đăng ký thành công khi Mật khẩu có đúng 1 chữ thường | P3, LB | FR01-R08 | `Nguyen Van A` | `tc112@domain.com` | `ABCDEf1!` | `ABCDEf1!` | OUT1 | AI |
| TC-REG-113 | Kiểm tra đăng ký thành công khi Mật khẩu có đúng 2 ký tự mỗi loại | P3, LB+1 | FR01-R07 đến FR01-R10 | `Nguyen Van A` | `tc113@domain.com` | `AAbb11!!` | `AAbb11!!` | OUT1 | AI |
| TC-REG-114 | Kiểm tra đăng ký thành công khi phần trước `@` dài 1 ký tự | P4, LB | FR01-R04 | `Nguyen Van A` | `t@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-115 | Kiểm tra đăng ký thành công khi phần trước `@` dài 2 ký tự | P4, LB+1 | FR01-R04 | `Nguyen Van A` | `tc@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-116 | Kiểm tra đăng ký thành công khi nhãn tên miền dài 1 ký tự | P5, LB | FR01-R04 | `Nguyen Van A` | `tc116@a.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-117 | Kiểm tra đăng ký thành công khi nhãn tên miền dài 2 ký tự | P5, LB+1 | FR01-R04 | `Nguyen Van A` | `tc117@ab.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-118 | Kiểm tra đăng ký thành công khi nhãn tên miền dài 62 ký tự | P5, UB-1 | FR01-R04 | `Nguyen Van A` | `tc118@` + 62 chữ `a` + `.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-119 | Kiểm tra đăng ký thành công khi nhãn tên miền dài 63 ký tự | P5, UB | FR01-R04 | `Nguyen Van A` | `tc119@` + 63 chữ `a` + `.com` | `Abcdef1!` | `Abcdef1!` | OUT1 | AI |
| TC-REG-120 | Kiểm tra đăng ký bị từ chối khi nhãn tên miền dài 64 ký tự | P5, UB+1 | FR01-R04 | `Nguyen Van A` | `tc120@` + 64 chữ `a` + `.com` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3 | AI |
| TC-REG-121 | Kiểm tra đăng ký thành công khi nhãn tên miền có dấu dài 63 ký tự ở dạng punycode | P5, UB (punycode) | FR01-R04 | `Nguyen Van A` | `tc121@tên` + 53 chữ `a` + `.vn` | `Abcdef1!` | `Abcdef1!` | OUT1. Giới hạn GH6 | AI |
| TC-REG-122 | Kiểm tra đăng ký bị từ chối khi nhãn tên miền có dấu dài 64 ký tự ở dạng punycode | P5, UB+1 (punycode) | FR01-R04 | `Nguyen Van A` | `tc122@tên` + 54 chữ `a` + `.vn` | `Abcdef1!` | `Abcdef1!` | OUT2, ERR3. Giới hạn GH6 | AI |
| TC-REG-123 | Kiểm tra đăng ký với Email dài 1011 ký tự | P6, lớn nhất giao diện cho nhập | FR01-R04 | `Nguyen Van A` | `tc123` + 995 chữ `a` + `@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1. Ghi số ký tự ô thực sự nhận. Nếu bị từ chối: Ghi là khác giả định A05, xét lại ở S7 trước khi coi là bug. Giới hạn GH7 | AI |

---

## 6. TS-04: API (EP, BVA)

Gửi `POST http://localhost:3000/api/register`. Trong cột body, `␣` là một dấu cách nằm **bên trong** chuỗi JSON.

"Kiểm chứng không tạo tài khoản": Sau khi nhận OUT4, gửi lại request với cùng email và dữ liệu hợp lệ (`name` là `Nguyen Van A`, `password` là `Abcdef1!`); mong đợi OUT3. Nếu nhận lỗi trùng email thì request trước đã tạo tài khoản.

| TC | Tiêu đề | Lớp hoặc biên | Kỹ thuật | Yêu cầu | `name` | `email` | `password` | Kết quả mong đợi | Nguồn gốc |
|---|---|---|---|---|---|---|---|---|---|
| TC-REG-70 | Kiểm tra API đăng ký thành công với dữ liệu hợp lệ | EC01, EC08, EC11, EC20, EC24, EC26, EC28, EC31, EC34, EC36 | EP | FR01-R22, FR01-R23 | `"Nguyen Van A"` | `"tc70@domain.com"` | `"Abcdef1!"` | OUT3. Body phản hồi không chứa mật khẩu ở bất kỳ dạng nào. Giới hạn GH5 | AI có SV sửa |
| TC-REG-71 | Kiểm tra API từ chối khi `name` rỗng | EC02 | EP | FR01-R01 | `""` | `"tc71@domain.com"` | `"Abcdef1!"` | OUT4; kiểm chứng không tạo tài khoản | AI |
| TC-REG-72 | Kiểm tra API từ chối khi `name` chỉ gồm 3 dấu cách | EC03 | EP | FR01-R01 | `"␣␣␣"` | `"tc72@domain.com"` | `"Abcdef1!"` | OUT4; kiểm chứng không tạo tài khoản | AI |
| TC-REG-73 | Kiểm tra API từ chối khi `email` rỗng | EC09 | EP | FR01-R02 | `"Nguyen Van A"` | `""` | `"Abcdef1!"` | OUT4 | AI |
| TC-REG-74 | Kiểm tra API từ chối khi `email` thiếu `@` | EC13 | EP | FR01-R04 | `"Nguyen Van A"` | `"tc74domain.com"` | `"Abcdef1!"` | OUT4 | AI |
| TC-REG-75 | Kiểm tra API từ chối khi `password` rỗng | EC25 | EP | FR01-R03 | `"Nguyen Van A"` | `"tc75@domain.com"` | `""` | OUT4; kiểm chứng không tạo tài khoản | AI |
| TC-REG-76 | Kiểm tra API từ chối khi `password` có 6 ký tự | EC27 | EP | FR01-R06 | `"Nguyen Van A"` | `"tc76@domain.com"` | `"Abcd1!"` | OUT4; kiểm chứng không tạo tài khoản | AI |
| TC-REG-77 | Kiểm tra API từ chối khi `password` không có ký tự đặc biệt | EC37 | EP | FR01-R10 | `"Nguyen Van A"` | `"tc77@domain.com"` | `"Abcdefg1"` | OUT4; kiểm chứng không tạo tài khoản | AI |
| TC-REG-80 | Kiểm tra API từ chối khi `email` chỉ gồm 3 dấu cách | EC10 | EP | FR01-R02 | `"Nguyen Van A"` | `"␣␣␣"` | `"Abcdef1!"` | OUT4 | AI có SV sửa |
| TC-REG-81 | Kiểm tra API lưu email đã cắt dấu cách đầu cuối | EC19 | EP | FR01-R04, FR01-R05 | `"Nguyen Van A"` | `"␣tc81@domain.com␣"` | `"Abcdef1!"` | Bước 1: OUT3. Bước 2: Qua giao diện, đăng ký `tc81@domain.com` với Họ Tên `Tran Thi B`, mật khẩu `Abcdef1!`; mong đợi OUT2, ERR4 | AI có SV sửa |
| TC-REG-82 | Kiểm tra API từ chối email trùng sau khi cắt dấu cách đầu cuối | EC67 | EP | FR01-R05 | `"Nguyen Van A"` | `"␣test@eshop.com␣"` | `"Abcdef1!"` | OUT4. Nếu OUT3 thì EShop không cắt dấu cách khi so trùng | AI có SV sửa |
| TC-REG-129 | Kiểm tra API từ chối khi `password` dài 7 ký tự | P2, LB-1 | BVA | FR01-R06 | `"Nguyen Van A"` | `"tc129@domain.com"` | `"Abcde1!"` | OUT4; kiểm chứng không tạo tài khoản | AI |
| TC-REG-130 | Kiểm tra API từ chối khi nhãn tên miền dài 64 ký tự | P5, UB+1 | BVA | FR01-R04 | `"Nguyen Van A"` | `"tc130@` + 64 chữ `a` + `.com"` | `"Abcdef1!"` | OUT4 | AI |

---

## 7. TS-05: Bảo mật (API và giao diện)

**TC-REG-79 chạy cuối cùng trong đợt test và reset dữ liệu ngay sau đó** (mục 10).

| TC | Tiêu đề | Lớp | Yêu cầu | Bước | Kết quả mong đợi | Nguồn gốc |
|---|---|---|---|---|---|---|
| TC-REG-78 | Kiểm tra email chứa chuỗi SQL được lưu và so sánh nguyên văn | EC66 | FR01-R04, FR01-R05, FR01-R25 | 1. Gửi API: `name` `"Nguyen Van A"`, `email` `"tc78'or'1'='1@domain.com"`, `password` `"Abcdef1!"`. 2. Qua giao diện, đăng ký lại đúng email `tc78'or'1'='1@domain.com` với Họ Tên `Tran Thi B`, mật khẩu `Abcdef1!` | Bước 1: OUT3, không xuất hiện lỗi hệ thống. Bước 2: OUT2, ERR4 | AI có SV sửa |
| TC-REG-79 | Kiểm tra Họ Tên chứa lệnh `DROP TABLE` không làm hỏng dữ liệu người dùng | EC07 | FR01-R01, FR01-R05, FR01-R25 | 1. Gửi API: `name` `"Robert'); DROP TABLE users;--"`, `email` `"tc79@domain.com"`, `password` `"Abcdef1!"`. 2. Qua giao diện, đăng ký `test@eshop.com` với Họ Tên `Nguyen Van A`, mật khẩu `Abcdef1!` | Bước 1: OUT3, không xuất hiện lỗi hệ thống. Bước 2: OUT2, ERR4 (dữ liệu có sẵn vẫn còn nguyên) | AI có SV sửa |

Ghi chú: `users` trong chuỗi tấn công là tên bảng giả định, không lấy từ mã nguồn; bước 2 có giá trị bất kể tên bảng thật là gì.

---

## 8. TS-06: Checklist giao diện

| TC | Tiêu đề | Yêu cầu | Điểm kiểm tra | Kết quả mong đợi | Cách kiểm tra | Nguồn gốc |
|---|---|---|---|---|---|---|
| TC-REG-90 | Kiểm tra form Đăng ký có trường Xác nhận mật khẩu | FR01-R11 | Các ô trên form | Có trường Xác nhận mật khẩu | Quan sát (liên quan D01) | AI |
| TC-REG-91 | Kiểm tra ngôn ngữ của trang Đăng ký và tiêu đề tab | FR01-R14 | Mọi chữ trên trang và tiêu đề tab | Toàn bộ tiếng Việt, trừ "EShop", "Email", "SUT" đã chấp nhận | Quan sát (liên quan D04) | AI |
| TC-REG-92 | Kiểm tra màu nút "Đăng Ký" | FR01-R15 | Màu nền nút submit | Màu xanh dương | Quan sát (liên quan D03) | AI |
| TC-REG-93 | Kiểm tra trang Đăng ký có đúng 1 thẻ `<h1>` | FR01-R16 | Số thẻ `<h1>` và nội dung | Đúng 1 thẻ, mô tả nội dung trang | DevTools ở S6 | AI |
| TC-REG-94 | Kiểm tra thứ tự focus khi nhấn Tab | FR01-R17 | Nhấn Tab từ đầu trang | Họ Tên, Email, Mật khẩu, (Xác nhận mật khẩu), nút "Đăng Ký", liên kết "Đăng nhập", theo thứ tự trên xuống dưới, trái sang phải | Nhấn Tab | AI |
| TC-REG-95 | Kiểm tra dấu `*` cạnh nhãn trường bắt buộc | FR01-R18 | Nhãn Họ Tên, Email, Mật khẩu (và Xác nhận mật khẩu) | Có dấu `*` | Quan sát (liên quan D02) | AI |
| TC-REG-96 | Kiểm tra loại ô Email và ô Mật khẩu | FR01-R19, FR01-R20 | Thuộc tính `type`; ký tự gõ vào ô Mật khẩu | Email: `type="email"`; Mật khẩu: `type="password"`, ký tự bị che | DevTools ở S6 và quan sát khi gõ | AI |
| TC-REG-97 | Kiểm tra vị trí thông báo lỗi | FR01-R21 | Thông báo khi chạy dữ liệu của TC-REG-30 | Thông báo nằm phía trên nút "Đăng Ký" | Quan sát | AI |

---

## 9. Nguồn gốc chi tiết

### 9.1 Test case không phải "AI"

| TC | Nguồn gốc | Mã trong bản AI | Đã đổi gì so với bản AI | Người phát hiện | Căn cứ |
|---|---|---|---|---|---|
| TC-REG-02 | AI có SV sửa | TC-REG-02 (S3) | Tách: Bỏ EC12 ra test case riêng; email `an.nguyen@mail.domain.com` thành `tc02@domain.com`; ký tự đặc biệt của mật khẩu `*` thành `@` | Sinh viên (S3, câu hỏi 3: tách lớp bất thường; quyết định xoay vòng ký tự đặc biệt) | `03_tc.md` mục 12 |
| TC-REG-03 | AI có SV sửa | TC-REG-03 (S3) | Tách: Bỏ EC16; email `tc03@domain` thành `tc03@domain.com` | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-04 | AI có SV sửa | TC-REG-05 (S3) | Tách: Bỏ EC59, EC39; email `tc+05@domain.com` thành `tc04@domain.com`; mật khẩu `Abc def1?` thành `Abcdef1%` | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-05 | AI có SV sửa | TC-REG-06 (S3) | Tách: Bỏ EC19, EC40; email `␣tc06@domain.com␣` thành `tc05@domain.com`; mật khẩu `Abcdef1&é` thành `Abcdef1*` | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-06 | AI có SV sửa | TC-REG-04 (S3) | Tách: Bỏ EC57; email `.tc04@domain.com` thành `tc06@domain.com`; mật khẩu `Abcdef1%` thành `Abcdef1?`; thêm giới hạn GH1 | Sinh viên (S3, câu hỏi 2, 3) | `03_tc.md` mục 12 |
| TC-REG-07 | AI có SV sửa | TC-REG-07 (S3) | Tách: Bỏ EC65, EC68; email `tc07@tênmiền.vn` thành `tc07@domain.com`; mật khẩu `Abcde1@␣` thành `Abcdef1&`; thêm giới hạn GH1 | Sinh viên (S3, câu hỏi 2, 3) | `03_tc.md` mục 12 |
| TC-REG-09 | AI có SV sửa | TC-REG-02 (S3) | Tách riêng EC12; email `an.nguyen@mail.domain.com` thành `tc.09@mail.domain.com`; Họ Tên, mật khẩu về giá trị cơ sở | Sinh viên (S3, câu hỏi 3, 4) | `03_tc.md` mục 12 |
| TC-REG-10 | AI có SV sửa | TC-REG-03 (S3) | Tách riêng EC16; Họ Tên, mật khẩu về giá trị cơ sở | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-11 | AI có SV sửa | TC-REG-06 (S3) | Tách riêng EC19; thêm bước 2 đăng ký lại email đã cắt dấu cách; thêm ghi chú trình duyệt tự cắt dấu cách (GH2) | Sinh viên (S3, câu hỏi 2: bước 2); Claude ở phiên điều phối, session `305c705a` (ghi chú `type="email"`) | `03_tc.md` mục 10.2, 12 |
| TC-REG-12 | AI có SV sửa | TC-REG-04 (S3) | Tách riêng EC57; Họ Tên, mật khẩu về giá trị cơ sở | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-13 | AI có SV sửa | TC-REG-05 (S3) | Tách riêng EC59; Họ Tên, mật khẩu về giá trị cơ sở | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-14 | AI có SV sửa | TC-REG-07 (S3) | Tách riêng EC65; Họ Tên, mật khẩu về giá trị cơ sở | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-15 | AI có SV sửa | TC-REG-09 (S3) | Email `o'brien@domain.com` thành `tc'15@domain.com` | Sinh viên (S3, câu hỏi 4) | `03_tc.md` mục 12 |
| TC-REG-16 | AI có SV sửa | TC-REG-05 (S3) | Tách riêng EC39; mật khẩu `Abc def1?` thành `Abc def1!`; thêm giới hạn GH3 | Sinh viên (S3, câu hỏi 2, 3) | `03_tc.md` mục 12 |
| TC-REG-17 | AI có SV sửa | TC-REG-06 (S3) | Tách riêng EC40; mật khẩu `Abcdef1&é` thành `Abcdef1!é` | Sinh viên (S3, câu hỏi 3) | `03_tc.md` mục 12 |
| TC-REG-18 | AI có SV sửa | TC-REG-07 (S3) | Tách riêng EC68; mật khẩu `Abcde1@␣` thành `Abcde1!␣`; thêm giới hạn GH3 | Sinh viên (S3, câu hỏi 2, 3) | `03_tc.md` mục 12 |
| TC-REG-33 | AI có SV sửa | TC-REG-13 (S3) | Thêm ghi chú trình duyệt tự cắt dấu cách (GH2) | Claude ở phiên điều phối, session `305c705a` | `03_tc.md` mục 10.2, 12 |
| TC-REG-44 | AI có SV sửa | TC-REG-24 (S3) | Email `nguyễn24@domain.com` thành `tcđ44@domain.com` | Sinh viên (S3, câu hỏi 4) | `03_tc.md` mục 12 |
| TC-REG-48 | AI có SV sửa | TC-REG-28 (S3) | Thêm ghi chú trình duyệt tự cắt dấu cách (GH2) | Claude ở phiên điều phối, session `305c705a` | `03_tc.md` mục 10.2, 12 |
| TC-REG-70 | AI có SV sửa | TC-REG-50 (S3) | Thêm kiểm tra body phản hồi không chứa mật khẩu (FR01-R23 một phần) | Sinh viên hỏi vì sao FR01-R23 chưa được phủ (S3, câu hỏi 5); AI ở phiên này đề xuất; sinh viên chọn (quyết định 4 (b)) | `03_tc.md` mục 12 |
| TC-REG-78 | AI có SV sửa | Không có (thêm khi review S3) | Test case bảo mật: Email chứa chuỗi SQL | Sinh viên yêu cầu thêm test bảo mật (quyết định 4 (b)); AI ở phiên này đề xuất cụ thể | `03_tc.md` mục 12 |
| TC-REG-79 | AI có SV sửa | Không có (thêm khi review S3) | Test case bảo mật: Họ Tên chứa `DROP TABLE`; chạy cuối, reset ngay sau đó | Sinh viên yêu cầu thêm test bảo mật (quyết định 4 (b)); AI ở phiên này đề xuất cụ thể; Claude ở phiên điều phối, session `305c705a`, phát hiện rủi ro phá dữ liệu | `03_tc.md` mục 10.2, 12 |
| TC-REG-80 | AI có SV sửa | Không có (thêm khi review S3) | Test case API cho Email chỉ gồm dấu cách | Claude ở phiên điều phối, session `305c705a` | `03_tc.md` mục 10.2, 12 |
| TC-REG-81 | AI có SV sửa | Không có (thêm khi review S3) | Test case API cho Email có dấu cách đầu cuối | Claude ở phiên điều phối, session `305c705a` | `03_tc.md` mục 10.2, 12 |
| TC-REG-82 | AI có SV sửa | Không có (thêm khi review S3) | Test case API cho Email trùng sau khi cắt dấu cách | Claude ở phiên điều phối, session `305c705a` | `03_tc.md` mục 10.2, 12 |
| TC-REG-131 | SV thêm | Không có (thêm khi review S4) | Họ Tên `␣A␣` (1 ký tự sau khi cắt dấu cách) | Sinh viên (S4, câu hỏi 1) | `04_bva.md` mục 10 |

### 9.2 Test case "AI" có lớp do sinh viên bổ sung ở S2

Các test case dưới đây giữ nguyên bản AI của S3 (nên nguồn gốc là "AI"), nhưng lớp mà chúng phủ không có trong bản AI của S2; lớp được thêm khi review S2. Ghi lại để phần gap analysis (S8) thấy đầy đủ đóng góp ở bước chia lớp.

| Lớp | Thêm khi review S2 do | Test case phủ |
|---|---|---|
| EC54, EC55, EC56 | Sinh viên (câu hỏi Họ Tên 2, 3, 5) | TC-REG-06, TC-REG-05, TC-REG-04 |
| EC57, EC58, EC59, EC60, EC61 | Sinh viên (câu hỏi Email 1, 2) | TC-REG-12, TC-REG-39, TC-REG-13, TC-REG-40, TC-REG-41 |
| EC64, EC65, EC66 | Sinh viên (câu hỏi Email 3, 4) | TC-REG-44, TC-REG-14, TC-REG-15 |
| EC69, EC70 | Sinh viên (câu hỏi bổ sung lần 2) | TC-REG-58, TC-REG-07 |
| EC62, EC63, EC67, EC68 | AI bổ sung khi viết bản review S2 | TC-REG-42, TC-REG-43, TC-REG-48, TC-REG-18 |

### 9.3 Test case đã bỏ (không có trong bộ cuối)

| Mã | Có trong | Lý do bỏ | Người phát hiện |
|---|---|---|---|
| TC-REG-105 | `ai_raw/S4_bva.md` | Mật khẩu 1 ký tự vi phạm cùng lúc độ dài và 3 điều kiện loại ký tự | Sinh viên (S4, câu hỏi 2) |
| TC-REG-109 | `ai_raw/S4_bva.md` | Mật khẩu 20 ký tự làm điểm "giữa" của phân vùng không có cận trên, cùng lớp với 9 ký tự | Sinh viên (S4, câu hỏi 3) |
| TC-REG-124 | `ai_raw/S4_bva.md` | Email 1 dấu cách: Qua giao diện trùng TC-REG-32 vì trình duyệt cắt thành rỗng; qua API đã có TC-REG-80 | Claude ở phiên điều phối phát hiện vấn đề `type="email"`; sinh viên quyết định bỏ |
| TC-REG-125 đến TC-REG-128 | `ai_raw/S4_bva.md` | So khớp Xác nhận mật khẩu không có thứ tự, không thuộc BVA; đều dự kiến Blocked | Sinh viên (S4, câu hỏi 4) |

Các test case hợp lệ gộp nhiều lớp trong `ai_raw/S3_test_cases.md` không bị bỏ mà được tách; bảng đổi mã ở `03_tc.md` mục 11.

---

## 10. Thứ tự chạy

1. Reset dữ liệu EShop về dữ liệu mẫu.
2. Chạy mọi test case trừ TC-REG-79, thứ tự tùy ý. Các test case hợp lệ thêm email mới nhưng không đụng tới `test@eshop.com`, nên không ảnh hưởng TC-REG-45, TC-REG-47, TC-REG-48, TC-REG-82.
3. Chạy TC-REG-79 cuối cùng.
4. Reset dữ liệu EShop ngay sau khi chạy xong TC-REG-79. Nếu bước 2 của TC-REG-79 không cho ERR4, ghi kết quả rồi reset trước khi chạy lại bất kỳ test case nào.

---

## 11. Giới hạn quan sát

| Mã | Giới hạn | Test case |
|---|---|---|
| GH1 | OUT1 chỉ chứng minh hệ thống chấp nhận Họ Tên có dấu cách; việc cắt hay gộp dấu cách khi lưu không quan sát được trong FR-01 | TC-REG-06, TC-REG-07 |
| GH2 | Nếu ô Email dùng `type="email"` (kiểm ở TC-REG-96), trình duyệt tự cắt dấu cách đầu cuối trước khi gửi, nên kết quả qua giao diện phản ánh hành vi chung của trình duyệt và EShop. Hành vi riêng của EShop kiểm ở TC-REG-80 đến TC-REG-82 | TC-REG-11, TC-REG-33, TC-REG-48 |
| GH3 | Mật khẩu có dấu cách được lưu đúng nguyên văn hay không chỉ kiểm được khi đăng nhập (FR-02), đã loại khỏi phạm vi; rủi ro người dùng không đăng nhập được bằng chính mật khẩu đã đăng ký | TC-REG-16, TC-REG-18, TC-REG-110, TC-REG-111 |
| GH4 | Giao diện không có trường Xác nhận mật khẩu (D01): Các test case hợp lệ có thể Pass mà FR01-R11, FR01-R12 vẫn chưa được kiểm chứng; kết luận dựa vào TC-REG-59 đến TC-REG-62 và TC-REG-90 | TC-REG-01 đến TC-REG-18, TC-REG-59 đến TC-REG-62 |
| GH5 | FR01-R23 chỉ kiểm được phản hồi API không chứa mật khẩu; FR01-R24 chỉ kiểm được hệ thống chấp nhận dữ liệu, việc escape khi hiển thị thuộc feature có hiển thị tên | TC-REG-08, TC-REG-70 |
| GH6 | Phụ thuộc trình duyệt chuyển tên miền có dấu sang punycode (giả định A15 (b)); ghi phiên bản trình duyệt; chỉ chạy qua giao diện | TC-REG-14, TC-REG-121, TC-REG-122 |
| GH7 | Giới hạn thật của ô chưa biết khi thiết kế. Nếu khi chạy thấy ô chỉ nhận tối đa N ký tự, quay lại S5 bổ sung các điểm N-1, N, N+1 | TC-REG-103, TC-REG-110, TC-REG-123 |

---

## 12. Ma trận truy vết yêu cầu

| Yêu cầu | Nội dung ngắn | Test case | Mức phủ |
|---|---|---|---|
| FR01-R01 | Họ Tên bắt buộc | TC-REG-01 đến TC-REG-08, TC-REG-30, TC-REG-31, TC-REG-71, TC-REG-72, TC-REG-79, TC-REG-101 đến TC-REG-104, TC-REG-131 | Đủ |
| FR01-R02 | Email bắt buộc | TC-REG-32, TC-REG-33, TC-REG-73, TC-REG-80 | Đủ |
| FR01-R03 | Mật khẩu bắt buộc | TC-REG-49, TC-REG-58, TC-REG-75 | Đủ |
| FR01-R04 | Email đúng định dạng | TC-REG-09 đến TC-REG-15, TC-REG-34 đến TC-REG-44, TC-REG-74, TC-REG-78, TC-REG-81, TC-REG-114 đến TC-REG-123, TC-REG-130 | Đủ |
| FR01-R05 | Email duy nhất | TC-REG-11, TC-REG-45 đến TC-REG-48, TC-REG-78, TC-REG-79, TC-REG-81, TC-REG-82 | Đủ |
| FR01-R06 | Mật khẩu tối thiểu 8 ký tự | TC-REG-16 đến TC-REG-18, TC-REG-50, TC-REG-58, TC-REG-76, TC-REG-106 đến TC-REG-108, TC-REG-110, TC-REG-111, TC-REG-129 | Đủ |
| FR01-R07 | Có chữ hoa | TC-REG-51, TC-REG-52, TC-REG-113 | Đủ |
| FR01-R08 | Có chữ thường | TC-REG-53, TC-REG-54, TC-REG-112, TC-REG-113 | Đủ |
| FR01-R09 | Có chữ số | TC-REG-55, TC-REG-113 | Đủ |
| FR01-R10 | Có ký tự đặc biệt trong tập | TC-REG-01 đến TC-REG-07 (đủ 7 ký tự), TC-REG-56, TC-REG-57, TC-REG-77, TC-REG-113 | Đủ |
| FR01-R11 | Có trường Xác nhận mật khẩu | TC-REG-59 đến TC-REG-62, TC-REG-90 | Đủ trên thiết kế; dự kiến Blocked do D01 |
| FR01-R12 | Từ chối nếu không khớp | TC-REG-59 đến TC-REG-62 | Đủ trên thiết kế; dự kiến Blocked do D01 |
| FR01-R13 | Chuyển tới trang Đăng nhập | TC-REG-01 đến TC-REG-18 | Đủ |
| FR01-R14 | Giao diện tiếng Việt | TC-REG-91 | Đủ |
| FR01-R15 | Màu nút | TC-REG-92 | Đủ |
| FR01-R16 | Đúng 1 thẻ `<h1>` | TC-REG-93 | Đủ |
| FR01-R17 | Thứ tự Tab | TC-REG-94 | Đủ |
| FR01-R18 | Dấu `*` | TC-REG-95 | Đủ |
| FR01-R19 | `type="email"` | TC-REG-96 | Đủ |
| FR01-R20 | `type="password"` | TC-REG-96 | Đủ |
| FR01-R21 | Thông báo lỗi trên nút submit | TC-REG-97 | Đủ |
| FR01-R22 | Phản hồi API khi thành công | TC-REG-70 (và mọi test case API có OUT3) | Đủ |
| FR01-R23 | Mật khẩu không lưu plaintext | TC-REG-70 | Một phần (GH5) |
| FR01-R24 | Escape khi hiển thị | TC-REG-08 | Một phần (GH5) |
| FR01-R25 | Parameterized Query | TC-REG-08, TC-REG-15, TC-REG-78, TC-REG-79 | Một phần: Kiểm qua hành vi bên ngoài |

---

## 13. Phần sinh viên bổ sung ở S5

Sinh viên ghi test case AI bỏ sót vào bảng dưới đây (trong `05_final_tc.md`), nguồn gốc là "SV thêm". Dùng mã trong các dải còn trống: 19 đến 29 (hợp lệ qua giao diện), 63 đến 69 (không hợp lệ qua giao diện), 83 đến 89 (API), 98, 99 (checklist), 132 trở đi (biên). Mỗi test case nên ghi lớp hoặc biên mà nó nhắm tới; nếu nó cho thấy một lớp mới, ghi lại để đưa vào gap analysis ở S8.

| TC | Tiêu đề | Lớp hoặc biên | Yêu cầu | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu | Kết quả mong đợi | Nguồn gốc | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | SV thêm | |
