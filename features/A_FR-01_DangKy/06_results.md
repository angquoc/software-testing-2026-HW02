# S6: Kết quả chạy test (FR-01 Đăng ký tài khoản)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test và điền file này; AI chỉ chuẩn bị khung
- Bản này: Sinh viên điền. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-20 16:57 (+07:00)
- Căn cứ: `05_final_tc.md` (96 test case, thứ tự chạy ở mục 10, giới hạn quan sát ở mục 11)

---

## 1. Môi trường

| Mục | Giá trị |
|---|---|
| Ngày chạy | |
| Người chạy | |
| Hệ điều hành | |
| Trình duyệt và phiên bản | |
| SUT | EShop, commit `85af3ba` |
| Backend | `http://localhost:3000` |
| Web | `http://localhost:5173` |
| Reset dữ liệu mẫu trước đợt test (thời điểm) | |
| Ô Email có dùng `type="email"` không (điền sau TC-REG-96) | |
| Ô Mật khẩu có dùng `type="password"` không (điền sau TC-REG-96) | |
| File log API | `logs/S6_api_<thời gian>.log`, `logs/S6_tc79_<thời gian>.log` |
| Reset dữ liệu sau TC-REG-79 (thời điểm) | |

## 2. Cách điền

- **Kết quả thực tế:** Ghi đúng những gì quan sát được: Đường dẫn sau khi nhấn "Đăng Ký", nguyên văn thông báo lỗi (ghi luôn đó là thông báo của trang hay của trình duyệt), số ký tự ô thực sự nhận nếu test case yêu cầu. Test case API: Mã HTTP và body, lấy từ log.
- **Trạng thái:** Pass, Fail, Blocked hoặc Not run.
  - Pass: Kết quả thực tế khớp kết quả mong đợi.
  - Fail: Không khớp. Mô tả khác ở đâu trong cột Ghi chú; đây là ứng viên bug cho S7.
  - Blocked: Không chạy được vì điều kiện bên ngoài test case (ví dụ thiếu trường trên giao diện). Ghi lý do.
  - Not run: Chưa chạy.
- **Ảnh:** Tên file `S6_<mã>.png` trong `screenshots/`, ví dụ `S6_TC-REG-01.png`. Test case nhiều bước: `S6_TC-REG-11_1.png`, `S6_TC-REG-11_2.png`.
- **Xác nhận mật khẩu:** Giao diện hiện không có trường này (D01). Với test case không nhắm vào trường này thì bỏ qua bước nhập; không cần ghi chú lại ở từng dòng.
- **Kết quả mong đợi:** Đọc theo bảng mã ở mục 3.
- **DevTools:** Chỉ dùng cho TC-REG-93 và TC-REG-96 (thuộc tính mà đặc tả yêu cầu).

## 3. Mã kết quả mong đợi

| Mã | Kết quả mong đợi |
|---|---|
| OUT1 | Đường dẫn đổi thành `/login` và trang hiện form đăng nhập (có ô nhập và nút gửi) |
| OUT2, ERRn | Có thông báo lỗi chỉ ra đúng nguyên nhân ERRn; vẫn ở `/register` |
| ERR1 đến ERR7 | ERR1 thiếu Họ Tên; ERR2 thiếu Email; ERR3 Email sai định dạng; ERR4 Email đã tồn tại; ERR5 thiếu Mật khẩu; ERR6 Mật khẩu không đạt yêu cầu mạnh; ERR7 Mật khẩu và Xác nhận mật khẩu không khớp |
| OUT3 | API trả HTTP 200 OK, body có `"message": "User registered successfully"` và `id` là số |
| OUT4 | API không trả về phản hồi thành công như OUT3 |

Giá trị cơ sở khi cột "Giá trị nhập chính" không nhắc tới: Họ Tên `Nguyen Van A`, Email `tc<số của test case>@domain.com`, Mật khẩu `Abcdef1!`. `␣` là một dấu cách. Giá trị đầy đủ của từng test case ở `05_final_tc.md`.

## 4. Kết quả theo thứ tự chạy

Thứ tự theo mục 10 của `05_final_tc.md`: Reset dữ liệu; chạy nhóm A đến E (thứ tự trong nhóm tùy ý); chạy nhóm F (TC-REG-79) cuối cùng; reset dữ liệu ngay sau đó. Nhóm A chạy trước vì TC-REG-96 cho biết ô Email có dùng `type="email"` hay không, cần để đọc kết quả của các test case có dấu cách trong Email (giới hạn GH2).

### A. Checklist giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1 | TC-REG-90 | Form Đăng ký có trường Xác nhận mật khẩu | Không nhập | Có trường Xác nhận mật khẩu |  |  |  |  |
| 2 | TC-REG-91 | Ngôn ngữ của trang Đăng ký và tiêu đề tab | Không nhập | Toàn bộ tiếng Việt, trừ "EShop", "Email", "SUT" đã chấp nhận |  |  |  |  |
| 3 | TC-REG-92 | Màu nút "Đăng Ký" | Không nhập | Màu xanh dương |  |  |  |  |
| 4 | TC-REG-93 | Trang Đăng ký có đúng 1 thẻ `<h1>` | Không nhập | Đúng 1 thẻ, mô tả nội dung trang |  |  |  | DevTools |
| 5 | TC-REG-94 | Thứ tự focus khi nhấn Tab | Không nhập | Họ Tên, Email, Mật khẩu, (Xác nhận mật khẩu), nút "Đăng Ký", liên kết "Đăng nhập", theo thứ tự trên xuống dưới, trái sang phải |  |  |  |  |
| 6 | TC-REG-95 | Dấu `*` cạnh nhãn trường bắt buộc | Không nhập | Có dấu `*` |  |  |  |  |
| 7 | TC-REG-96 | Loại ô Email và ô Mật khẩu | Không nhập | Email: `type="email"`; Mật khẩu: `type="password"`, ký tự bị che |  |  |  | DevTools; điền kết quả vào phần Môi trường |

### B. Không hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 8 | TC-REG-30 | Bị từ chối khi Họ Tên để trống | Họ Tên: (để trống) | OUT2, ERR1 |  |  |  |  |
| 9 | TC-REG-97 | Vị trí thông báo lỗi | Dữ liệu của TC-REG-30 (Họ Tên để trống) | Thông báo nằm phía trên nút "Đăng Ký" |  |  |  | Quan sát khi chạy TC-REG-30 |
| 10 | TC-REG-31 | Bị từ chối khi Họ Tên chỉ gồm 3 dấu cách | Họ Tên: `␣␣␣` | OUT2, ERR1 |  |  |  |  |
| 11 | TC-REG-32 | Bị từ chối khi Email để trống | Email: (để trống) | OUT2, ERR2 |  |  |  |  |
| 12 | TC-REG-33 | Bị từ chối khi Email chỉ gồm 3 dấu cách | Email: `␣␣␣` | OUT2, ERR2. Giới hạn GH2 |  |  |  |  |
| 13 | TC-REG-34 | Bị từ chối khi Email thiếu `@` | Email: `tc34domain.com` | OUT2, ERR3 |  |  |  |  |
| 14 | TC-REG-35 | Bị từ chối khi Email thiếu phần trước `@` | Email: `@domain.com` | OUT2, ERR3 |  |  |  |  |
| 15 | TC-REG-36 | Bị từ chối khi Email thiếu phần sau `@` | Email: `tc36@` | OUT2, ERR3 |  |  |  |  |
| 16 | TC-REG-37 | Bị từ chối khi Email có 2 dấu `@` | Email: `tc37@@domain.com` | OUT2, ERR3 |  |  |  |  |
| 17 | TC-REG-38 | Bị từ chối khi Email có dấu cách ở giữa | Email: `tc␣38@domain.com` | OUT2, ERR3 |  |  |  |  |
| 18 | TC-REG-39 | Bị từ chối khi có dấu chấm ngay sau `@` | Email: `tc39@.domain.com` | OUT2, ERR3 |  |  |  |  |
| 19 | TC-REG-40 | Bị từ chối khi phần trước `@` có dấu ngoặc | Email: `tc(40)@domain.com` | OUT2, ERR3 |  |  |  |  |
| 20 | TC-REG-41 | Bị từ chối khi tên miền có dấu gạch dưới | Email: `tc41@do_main.com` | OUT2, ERR3 |  |  |  |  |
| 21 | TC-REG-42 | Bị từ chối khi nhãn tên miền bắt đầu bằng dấu gạch nối | Email: `tc42@-domain.com` | OUT2, ERR3 |  |  |  |  |
| 22 | TC-REG-43 | Bị từ chối khi nhãn tên miền dài 70 ký tự | Email: `tc43@` + 70 chữ `a` + `.com` | OUT2, ERR3 |  |  |  |  |
| 23 | TC-REG-44 | Bị từ chối khi phần trước `@` có chữ có dấu | Email: `tcđ44@domain.com` | OUT2, ERR3 |  |  |  |  |
| 24 | TC-REG-45 | Bị từ chối khi Email trùng tài khoản có sẵn | Email: `test@eshop.com` | OUT2, ERR4 |  |  |  |  |
| 25 | TC-REG-46 | Bị từ chối khi Email trùng email vừa đăng ký | Họ Tên: Lần 1: `Nguyen Van A`; lần 2: `Tran Thi B`; Email: `tc46@domain.com` (cả hai lần) | Lần 1: OUT1. Lần 2: OUT2, ERR4 |  |  |  | 2 lần đăng ký |
| 26 | TC-REG-47 | Bị từ chối khi Email trùng nhưng khác chữ hoa, chữ thường | Email: `Test@Eshop.com` | OUT2, ERR4 |  |  |  |  |
| 27 | TC-REG-48 | Bị từ chối khi Email trùng sau khi cắt dấu cách đầu cuối | Email: `␣test@eshop.com␣` | OUT2, ERR4. Giới hạn GH2 |  |  |  |  |
| 28 | TC-REG-49 | Bị từ chối khi Mật khẩu để trống | Mật khẩu: (để trống) | OUT2, ERR5 |  |  |  |  |
| 29 | TC-REG-50 | Bị từ chối khi Mật khẩu có 6 ký tự | Mật khẩu: `Abcd1!` | OUT2, ERR6 |  |  |  |  |
| 30 | TC-REG-51 | Bị từ chối khi Mật khẩu không có chữ hoa | Mật khẩu: `abcdef1!` | OUT2, ERR6 |  |  |  |  |
| 31 | TC-REG-52 | Bị từ chối khi chữ hoa duy nhất của Mật khẩu là chữ có dấu | Mật khẩu: `Ăbcdef1!` | OUT2, ERR6 |  |  |  |  |
| 32 | TC-REG-53 | Bị từ chối khi Mật khẩu không có chữ thường | Mật khẩu: `ABCDEF1!` | OUT2, ERR6 |  |  |  |  |
| 33 | TC-REG-54 | Bị từ chối khi chữ thường duy nhất của Mật khẩu là chữ có dấu | Mật khẩu: `ABCDEă1!` | OUT2, ERR6 |  |  |  |  |
| 34 | TC-REG-55 | Bị từ chối khi Mật khẩu không có chữ số | Mật khẩu: `Abcdefg!` | OUT2, ERR6 |  |  |  |  |
| 35 | TC-REG-56 | Bị từ chối khi Mật khẩu không có ký tự đặc biệt | Mật khẩu: `Abcdefg1` | OUT2, ERR6 |  |  |  |  |
| 36 | TC-REG-57 | Bị từ chối khi ký tự đặc biệt duy nhất nằm ngoài tập cho phép | Mật khẩu: `Abcdef1#` | OUT2, ERR6 |  |  |  |  |
| 37 | TC-REG-58 | Bị từ chối khi Mật khẩu chỉ gồm 8 dấu cách | Mật khẩu: `␣␣␣␣␣␣␣␣` | OUT2, **ERR6** (không phải ERR5) |  |  |  |  |
| 38 | TC-REG-59 | Bị từ chối khi Xác nhận mật khẩu khác Mật khẩu | Xác nhận mật khẩu: `Abcdef2!` | OUT2, ERR7. Dự kiến Blocked (D01) |  |  |  | Dự kiến Blocked: Giao diện không có trường Xác nhận mật khẩu (D01). Sinh viên xác nhận |
| 39 | TC-REG-60 | Bị từ chối khi Xác nhận mật khẩu để trống | Xác nhận mật khẩu: (để trống) | OUT2, ERR7. Dự kiến Blocked (D01) |  |  |  | Dự kiến Blocked: Giao diện không có trường Xác nhận mật khẩu (D01). Sinh viên xác nhận |
| 40 | TC-REG-61 | Bị từ chối khi Xác nhận mật khẩu chỉ khác chữ hoa, chữ thường | Xác nhận mật khẩu: `abcdef1!` | OUT2, ERR7. Dự kiến Blocked (D01) |  |  |  | Dự kiến Blocked: Giao diện không có trường Xác nhận mật khẩu (D01). Sinh viên xác nhận |
| 41 | TC-REG-62 | Bị từ chối khi Xác nhận mật khẩu thừa dấu cách ở cuối | Xác nhận mật khẩu: `Abcdef1!␣` | OUT2, ERR7. Dự kiến Blocked (D01) |  |  |  | Dự kiến Blocked: Giao diện không có trường Xác nhận mật khẩu (D01). Sinh viên xác nhận |

### C. Hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 42 | TC-REG-01 | Thành công với dữ liệu hợp lệ cơ sở | Dữ liệu cơ sở, email `tc01@domain.com` | OUT1 |  |  |  |  |
| 43 | TC-REG-02 | Thành công khi Họ Tên có chữ tiếng Việt có dấu | Họ Tên: `Nguyễn Thị Ánh`; Mật khẩu: `Abcdef1@` | OUT1 |  |  |  |  |
| 44 | TC-REG-03 | Thành công khi Họ Tên có chữ số | Họ Tên: `Nguyen Van A2`; Mật khẩu: `Abcdef1$` | OUT1 |  |  |  |  |
| 45 | TC-REG-04 | Thành công khi Họ Tên có dấu gạch nối | Họ Tên: `Anh-Ngoc`; Mật khẩu: `Abcdef1%` | OUT1 |  |  |  |  |
| 46 | TC-REG-05 | Thành công khi Họ Tên chỉ gồm chữ số | Họ Tên: `12345`; Mật khẩu: `Abcdef1*` | OUT1 |  |  |  |  |
| 47 | TC-REG-06 | Thành công khi Họ Tên có dấu cách ở đầu và cuối | Họ Tên: `␣Nguyen Van A␣`; Mật khẩu: `Abcdef1?` | OUT1. Giới hạn GH1 |  |  |  |  |
| 48 | TC-REG-07 | Thành công khi Họ Tên có 2 dấu cách liền nhau ở giữa | Họ Tên: `Nguyen␣␣Van A`; Mật khẩu: `Abcdef1&` | OUT1. Giới hạn GH1 |  |  |  |  |
| 49 | TC-REG-08 | Thành công khi Họ Tên có thẻ HTML và dấu nháy đơn | Họ Tên: `<b>O'Brien</b>` | OUT1, không xuất hiện lỗi hệ thống. Giới hạn GH5 |  |  |  |  |
| 50 | TC-REG-09 | Thành công khi Email có dấu chấm ở phần trước `@` và có tên miền con | Email: `tc.09@mail.domain.com` | OUT1 |  |  |  |  |
| 51 | TC-REG-10 | Thành công khi phần sau `@` không có dấu chấm | Email: `tc10@domain` | OUT1 |  |  |  |  |
| 52 | TC-REG-11 | Thành công khi Email có dấu cách ở đầu và cuối | Email: `␣tc11@domain.com␣` | Bước 1: OUT1. Bước 2: Mở lại `/register`, đăng ký `tc11@domain.com` với Họ Tên `Tran Thi B`, mật khẩu `Abcdef1!`; mong đợi OUT2, ERR4. Giới hạn GH2 |  |  |  | 2 bước |
| 53 | TC-REG-12 | Thành công khi Email bắt đầu bằng dấu chấm | Email: `.tc12@domain.com` | OUT1 |  |  |  |  |
| 54 | TC-REG-13 | Thành công khi Email có dấu cộng ở phần trước `@` | Email: `tc+13@domain.com` | OUT1 |  |  |  |  |
| 55 | TC-REG-14 | Thành công khi tên miền có chữ có dấu | Email: `tc14@tênmiền.vn` | OUT1. Giới hạn GH6 |  |  |  | Phụ thuộc trình duyệt (A15) |
| 56 | TC-REG-15 | Thành công khi Email có dấu nháy đơn | Email: `tc'15@domain.com` | OUT1, không xuất hiện lỗi hệ thống |  |  |  |  |
| 57 | TC-REG-16 | Thành công khi Mật khẩu có dấu cách ở giữa | Mật khẩu: `Abc def1!` | OUT1. Giới hạn GH3 |  |  |  |  |
| 58 | TC-REG-17 | Thành công khi Mật khẩu có ký tự ngoài 4 loại | Mật khẩu: `Abcdef1!é` | OUT1 |  |  |  |  |
| 59 | TC-REG-18 | Thành công khi Mật khẩu đủ 8 ký tự nhờ dấu cách ở cuối | Mật khẩu: `Abcde1!␣` (8 ký tự) | OUT1. Giới hạn GH3 |  |  |  |  |

### D. Giá trị biên qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 60 | TC-REG-101 | Thành công khi Họ Tên dài 1 ký tự | Họ Tên: `A` | OUT1 |  |  |  |  |
| 61 | TC-REG-131 | Thành công khi Họ Tên 1 ký tự có dấu cách hai bên | Họ Tên: `␣A␣` | OUT1 |  |  |  |  |
| 62 | TC-REG-102 | Thành công khi Họ Tên dài 2 ký tự | Họ Tên: `An` | OUT1 |  |  |  |  |
| 63 | TC-REG-103 | Với Họ Tên dài 1000 ký tự | Họ Tên: 1000 chữ `a` (dán vào ô) | OUT1. Ghi số ký tự ô thực sự nhận. Giới hạn GH7 |  |  |  | Ghi số ký tự ô nhận |
| 64 | TC-REG-104 | Bị từ chối khi Họ Tên là 1 dấu cách | Họ Tên: `␣` | OUT2, ERR1 |  |  |  |  |
| 65 | TC-REG-106 | Bị từ chối khi Mật khẩu dài 4 ký tự | Mật khẩu: `Aa1!` | OUT2, ERR6 |  |  |  |  |
| 66 | TC-REG-107 | Bị từ chối khi Mật khẩu dài 7 ký tự | Mật khẩu: `Abcde1!` | OUT2, ERR6 |  |  |  |  |
| 67 | TC-REG-108 | Thành công khi Mật khẩu dài 9 ký tự | Mật khẩu: `Abcdefg1!` | OUT1 |  |  |  |  |
| 68 | TC-REG-110 | Với Mật khẩu dài 1000 ký tự | Mật khẩu: `Abcdef1!` + 992 chữ `a` | OUT1. Ghi số ký tự ô thực sự nhận. Giới hạn GH3, GH7 |  |  |  | Ghi số ký tự ô nhận |
| 69 | TC-REG-111 | Thành công khi Mật khẩu đủ 8 ký tự nhờ dấu cách ở đầu | Mật khẩu: `␣Abcde1!` | OUT1. Giới hạn GH3 |  |  |  |  |
| 70 | TC-REG-112 | Thành công khi Mật khẩu có đúng 1 chữ thường | Mật khẩu: `ABCDEf1!` | OUT1 |  |  |  |  |
| 71 | TC-REG-113 | Thành công khi Mật khẩu có đúng 2 ký tự mỗi loại | Mật khẩu: `AAbb11!!` | OUT1 |  |  |  |  |
| 72 | TC-REG-114 | Thành công khi phần trước `@` dài 1 ký tự | Email: `t@domain.com` | OUT1 |  |  |  |  |
| 73 | TC-REG-115 | Thành công khi phần trước `@` dài 2 ký tự | Email: `tc@domain.com` | OUT1 |  |  |  |  |
| 74 | TC-REG-116 | Thành công khi nhãn tên miền dài 1 ký tự | Email: `tc116@a.com` | OUT1 |  |  |  |  |
| 75 | TC-REG-117 | Thành công khi nhãn tên miền dài 2 ký tự | Email: `tc117@ab.com` | OUT1 |  |  |  |  |
| 76 | TC-REG-118 | Thành công khi nhãn tên miền dài 62 ký tự | Email: `tc118@` + 62 chữ `a` + `.com` | OUT1 |  |  |  |  |
| 77 | TC-REG-119 | Thành công khi nhãn tên miền dài 63 ký tự | Email: `tc119@` + 63 chữ `a` + `.com` | OUT1 |  |  |  |  |
| 78 | TC-REG-120 | Bị từ chối khi nhãn tên miền dài 64 ký tự | Email: `tc120@` + 64 chữ `a` + `.com` | OUT2, ERR3 |  |  |  |  |
| 79 | TC-REG-121 | Thành công khi nhãn tên miền có dấu dài 63 ký tự ở dạng punycode | Email: `tc121@tên` + 53 chữ `a` + `.vn` | OUT1. Giới hạn GH6 |  |  |  | Phụ thuộc trình duyệt (A15) |
| 80 | TC-REG-122 | Bị từ chối khi nhãn tên miền có dấu dài 64 ký tự ở dạng punycode | Email: `tc122@tên` + 54 chữ `a` + `.vn` | OUT2, ERR3. Giới hạn GH6 |  |  |  | Phụ thuộc trình duyệt (A15) |
| 81 | TC-REG-123 | Với Email dài 1011 ký tự | Email: `tc123` + 995 chữ `a` + `@domain.com` | OUT1. Ghi số ký tự ô thực sự nhận. Nếu bị từ chối: Ghi là khác giả định A05, xét lại ở S7 trước khi coi là bug. Giới hạn GH7 |  |  |  | Ghi số ký tự ô nhận; nếu bị từ chối ghi "khác giả định A05" |

### E. API (script `scripts/run_api_tests.py`)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 82 | TC-REG-70 | API đăng ký thành công với dữ liệu hợp lệ | `email`: `"tc70@domain.com"` | OUT3. Body phản hồi không chứa mật khẩu ở bất kỳ dạng nào. Giới hạn GH5 |  |  |  | Bằng chứng: log API |
| 83 | TC-REG-71 | API từ chối khi `name` rỗng | `name`: `""`; `email`: `"tc71@domain.com"` | OUT4; kiểm chứng không tạo tài khoản |  |  |  | Bằng chứng: log API |
| 84 | TC-REG-72 | API từ chối khi `name` chỉ gồm 3 dấu cách | `name`: `"␣␣␣"`; `email`: `"tc72@domain.com"` | OUT4; kiểm chứng không tạo tài khoản |  |  |  | Bằng chứng: log API |
| 85 | TC-REG-73 | API từ chối khi `email` rỗng | `email`: `""` | OUT4 |  |  |  | Bằng chứng: log API |
| 86 | TC-REG-74 | API từ chối khi `email` thiếu `@` | `email`: `"tc74domain.com"` | OUT4 |  |  |  | Bằng chứng: log API |
| 87 | TC-REG-75 | API từ chối khi `password` rỗng | `email`: `"tc75@domain.com"`; `password`: `""` | OUT4; kiểm chứng không tạo tài khoản |  |  |  | Bằng chứng: log API |
| 88 | TC-REG-76 | API từ chối khi `password` có 6 ký tự | `email`: `"tc76@domain.com"`; `password`: `"Abcd1!"` | OUT4; kiểm chứng không tạo tài khoản |  |  |  | Bằng chứng: log API |
| 89 | TC-REG-77 | API từ chối khi `password` không có ký tự đặc biệt | `email`: `"tc77@domain.com"`; `password`: `"Abcdefg1"` | OUT4; kiểm chứng không tạo tài khoản |  |  |  | Bằng chứng: log API |
| 90 | TC-REG-78 | Email chứa chuỗi SQL được lưu và so sánh nguyên văn | `email`: `"tc78'or'1'='1@domain.com"` | Bước 1: OUT3, không xuất hiện lỗi hệ thống. Bước 2: OUT2, ERR4 |  |  |  | Script API in bước 1; bước 2 làm tay qua giao diện |
| 91 | TC-REG-80 | API từ chối khi `email` chỉ gồm 3 dấu cách | `email`: `"␣␣␣"` | OUT4 |  |  |  | Bằng chứng: log API |
| 92 | TC-REG-81 | API lưu email đã cắt dấu cách đầu cuối | `email`: `"␣tc81@domain.com␣"` | Bước 1: OUT3. Bước 2: Qua giao diện, đăng ký `tc81@domain.com` với Họ Tên `Tran Thi B`, mật khẩu `Abcdef1!`; mong đợi OUT2, ERR4 |  |  |  | Script API in bước 1; bước 2 làm tay qua giao diện |
| 93 | TC-REG-82 | API từ chối email trùng sau khi cắt dấu cách đầu cuối | `email`: `"␣test@eshop.com␣"` | OUT4. Nếu OUT3 thì EShop không cắt dấu cách khi so trùng |  |  |  | Bằng chứng: log API |
| 94 | TC-REG-129 | API từ chối khi `password` dài 7 ký tự | `email`: `"tc129@domain.com"`; `password`: `"Abcde1!"` | OUT4; kiểm chứng không tạo tài khoản |  |  |  | Bằng chứng: log API |
| 95 | TC-REG-130 | API từ chối khi nhãn tên miền dài 64 ký tự | `email`: `"tc130@` + 64 chữ `a` + `.com"` | OUT4 |  |  |  | Bằng chứng: log API |

### F. Bảo mật, chạy cuối cùng (script `scripts/run_tc79.py`)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 96 | TC-REG-79 | Họ Tên chứa lệnh `DROP TABLE` không làm hỏng dữ liệu người dùng | `name`: `"Robert'); DROP TABLE users;--"` | Bước 1: OUT3, không xuất hiện lỗi hệ thống. Bước 2: OUT2, ERR4 (dữ liệu có sẵn vẫn còn nguyên) |  |  |  | Script riêng, chạy cuối cùng; bước 2 làm tay; reset ngay sau |
## 5. Tổng hợp

Điền sau khi chạy xong (có thể nhờ AI đếm lại từ bảng ở mục 4).

| Nhóm | Số TC | Pass | Fail | Blocked | Not run |
|---|---|---|---|---|---|
| A. Checklist giao diện | 7 | | | | |
| B. Không hợp lệ qua giao diện | 34 | | | | |
| C. Hợp lệ qua giao diện | 18 | | | | |
| D. Giá trị biên qua giao diện | 22 | | | | |
| E. API | 14 | | | | |
| F. Bảo mật, chạy cuối cùng | 1 | | | | |
| **Tổng** | **96** | | | | |
