# Bug report HW02: Domain Testing trên EShop

- Sinh viên: Nguyễn Thị Ánh Ngọc, MSSV 23120061
- SUT: EShop, commit `85af3ba`
- Repo nhóm (GitHub Issues): https://github.com/angquoc/software-testing-2026-HW02-group

Mỗi bug dưới đây là nội dung để dán vào issue GitHub theo template **Bug report**, theo quy ước ở mục 4 README của repo nhóm. Sau khi tạo issue, ghi số issue vào bảng tổng hợp của feature và vào dòng "Issue" của bug. Đường dẫn ảnh và log tính từ thư mục `Homeworks/HW02/`.

## Mục lục

| Feature | Pool | Nền tảng | Mục |
|---|---|---|---|
| FR-01 Đăng ký tài khoản | A | Web | [FR-01](#fr-01-đăng-ký-tài-khoản) |
| FR-07 Giỏ hàng | B | Web | [FR-07](#fr-07-giỏ-hàng) |
| FR-17 Quản lý mã giảm giá | C | Web Admin | [FR-17](#fr-17-quản-lý-mã-giảm-giá) |
| FR-04 Quản lý hồ sơ cá nhân | D | Mobile | [FR-04](#fr-04-quản-lý-hồ-sơ-cá-nhân) |

---

## FR-01: Đăng ký tài khoản

- Nguồn: `features/A_FR-01_DangKy/06_results.md` (kết quả chạy ngày 20/10/2026), bộ test case ở `features/A_FR-01_DangKy/05_final_tc.md`
- Môi trường chung: Windows 11 Home Single Language 10.0.26200; Google Chrome 155.0.8059.85; EShop commit `85af3ba`; backend `http://localhost:3000`; web `http://localhost:5173`
- Điều kiện tiên quyết chung: Đã reset dữ liệu EShop về dữ liệu mẫu (có `test@eshop.com`, `admin@eshop.com`); chưa đăng nhập

### Tổng hợp

| Bug | Tiêu đề ngắn | Severity | Technique | Test case | Issue |
|---|---|---|---|---|---|
| BUG-FR01-01 | Giao diện từ chối mật khẩu hợp lệ, không đăng ký được | Critical | EP, BVA | TC-REG-01, TC-REG-108 | #42 |
| BUG-FR01-02 | Form không có trường Xác nhận mật khẩu | High | EP | TC-REG-90 (chặn TC-REG-59 đến 62) | #43 |
| BUG-FR01-03 | API nhận Họ Tên rỗng hoặc chỉ có dấu cách | High | EP | TC-REG-71, TC-REG-72 | #44 |
| BUG-FR01-04 | API nhận Email rỗng hoặc chỉ có dấu cách | High | EP | TC-REG-73, TC-REG-80 | #45 |
| BUG-FR01-05 | API nhận Mật khẩu rỗng | High | EP | TC-REG-75 | #46 |
| BUG-FR01-06 | API nhận Email sai định dạng | High | EP, BVA | TC-REG-74, TC-REG-130 | #47 |
| BUG-FR01-07 | API cho tạo nhiều tài khoản cùng một Email | High | EP | TC-REG-82; bước kiểm chứng của TC-REG-71, 72, 75, 76, 77, 129 | #48 |
| BUG-FR01-08 | API nhận Mật khẩu không đạt yêu cầu mạnh | High | EP, BVA | TC-REG-76, TC-REG-77, TC-REG-129 | #49 |
| BUG-FR01-09 | Ô Email không dùng `type="email"` | Medium | EP | TC-REG-96 | #50 |
| BUG-FR01-10 | Trường bắt buộc không có dấu `*` | Low | EP | TC-REG-95 | #51 |
| BUG-FR01-11 | Nút "Đăng Ký" màu đỏ thay vì xanh dương | Low | EP | TC-REG-92 | #52 |
| BUG-FR01-12 | Trang Đăng ký không có thẻ `<h1>` | Low | EP | TC-REG-93 | #53 |
| BUG-FR01-13 | Có chữ không phải tiếng Việt trên trang Đăng ký | Low | EP | TC-REG-91 | #54 |

Label chung cho mọi bug của FR-01: `bug` (template tự gắn), `platform: web`, `pool: A`. Label `severity` và `technique` theo bảng trên.

---

### BUG-FR01-01: Giao diện từ chối mật khẩu hợp lệ, không đăng ký được

- **Issue:** #42 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_42.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Đăng ký với mật khẩu hợp lệ: Báo "Mật khẩu quá yếu" và không tạo được tài khoản`
- **Labels:** `bug`, `severity: critical`, `platform: web`, `technique: EP`, `technique: BVA`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-01 (EP, dữ liệu hợp lệ cơ sở), TC-REG-108 (BVA, mật khẩu 9 ký tự)

**Mức độ:** Critical

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; chưa đăng nhập; mở `http://localhost:5173/register`

**Các bước tái hiện:**
1. Nhập Họ Tên `Nguyen Van A`.
2. Nhập Email `tc01@domain.com`.
3. Nhập Mật khẩu `Abcdef1!`.
4. Nhấn nút "Đăng Ký".

**Dữ liệu test:** Mật khẩu `Abcdef1!` (TC-REG-01), `Abcdefg1!` (TC-REG-108), `Test1234!` (mật khẩu của tài khoản mẫu `test@eshop.com` trong SRS). Cả ba đều dài từ 8 ký tự, có chữ hoa, chữ thường, chữ số và `!`

**Kết quả mong đợi (theo đặc tả):** Đăng ký thành công, chuyển tới trang Đăng nhập (`/login`). README của EShop, FR-01:

> - **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
> - Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

**Kết quả thực tế:** Trang hiện khung đỏ "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT.", vẫn ở `/register`, không tạo tài khoản. Xảy ra với cả 3 mật khẩu ở mục Dữ liệu test. Gửi cùng mật khẩu `Abcdef1!` thẳng qua API (`POST /api/register`, TC-REG-70) thì được chấp nhận (HTTP 200), nên lỗi nằm ở phía giao diện.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-01.png`, `S6_TC-REG-108.png`, `S6_TC-REG-31.png` (với `Test1234!`)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Lỗi này chặn luồng đăng ký qua giao diện: Không có mật khẩu hợp lệ nào đăng ký được. Nó cũng làm 14 test case khác không quan sát được điều kiện cần kiểm (bị Blocked): TC-REG-31, 33 đến 39, 45, 78, 79, 81, 101, 104.

---

### BUG-FR01-02: Form không có trường Xác nhận mật khẩu

- **Issue:** #43 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_43.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Form Đăng ký: Không có trường Xác nhận mật khẩu`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-90

**Mức độ:** High

**Điều kiện tiên quyết:** Mở `http://localhost:5173/register`

**Các bước tái hiện:**
1. Quan sát các ô nhập trên form Đăng ký.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Form có trường Xác nhận mật khẩu và từ chối đăng ký khi hai trường không khớp. README của EShop, FR-01:

> - Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.

**Kết quả thực tế:** Form chỉ có 3 ô: Họ Tên, Email, Mật khẩu. Không có trường Xác nhận mật khẩu, nên hệ thống không thể từ chối khi người dùng gõ nhầm mật khẩu.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S0_01_form_dang_ky.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Các test case EP của trường này (TC-REG-59 đến TC-REG-62: Xác nhận khác mật khẩu, để trống, chỉ khác hoa thường, thừa dấu cách) không thực hiện được (Blocked). API spec cũng không mô tả trường xác nhận mật khẩu.

---

### BUG-FR01-03: API nhận Họ Tên rỗng hoặc chỉ có dấu cách

- **Issue:** #44 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_44.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] API đăng ký: Tạo tài khoản khi Họ Tên rỗng hoặc chỉ có dấu cách`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-71, TC-REG-72

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, body `{"name": "", "email": "tc71@domain.com", "password": "Abcdef1!"}`.
2. Gửi tiếp với body `{"name": "   ", "email": "tc72@domain.com", "password": "Abcdef1!"}` (`name` là 3 dấu cách).

**Dữ liệu test:** `name` rỗng; `name` là 3 dấu cách

**Kết quả mong đợi (theo đặc tả):** Từ chối đăng ký vì thiếu Họ Tên. README của EShop, FR-01:

> - Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.

**Kết quả thực tế:** Cả hai request đều nhận HTTP 200, body `{"message": "User registered successfully", "id": ...}` (id 4 và 6): Tài khoản được tạo dù không có Họ Tên.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-71_log.png`, `S6_TC-REG-72_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Tái hiện qua API vì giao diện đang bị BUG-FR01-01 chặn mọi lần đăng ký. Các bug BUG-FR01-03 đến 08 cho thấy API đăng ký không kiểm tra dữ liệu đầu vào. Related: #45, #46, #47, #48, #49

---

### BUG-FR01-04: API nhận Email rỗng hoặc chỉ có dấu cách

- **Issue:** #45 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_45.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] API đăng ký: Tạo tài khoản khi Email rỗng hoặc chỉ có dấu cách`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-73, TC-REG-80

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, body `{"name": "Nguyen Van A", "email": "", "password": "Abcdef1!"}`.
2. Gửi tiếp với body `{"name": "Nguyen Van A", "email": "   ", "password": "Abcdef1!"}` (`email` là 3 dấu cách).

**Dữ liệu test:** `email` rỗng; `email` là 3 dấu cách

**Kết quả mong đợi (theo đặc tả):** Từ chối đăng ký vì thiếu Email. README của EShop, FR-01:

> - Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.

**Kết quả thực tế:** Cả hai request đều nhận HTTP 200, body `{"message": "User registered successfully", "id": ...}` (id 8 và 17): Tài khoản được tạo dù không có Email.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-73_log.png`, `S6_TC-REG-80_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, ô Email để trống bị trình duyệt chặn (TC-REG-32 Pass); lỗi nằm ở phía API. Related: #44

---

### BUG-FR01-05: API nhận Mật khẩu rỗng

- **Issue:** #46 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_46.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] API đăng ký: Tạo tài khoản khi Mật khẩu rỗng`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-75

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, body `{"name": "Nguyen Van A", "email": "tc75@domain.com", "password": ""}`.

**Dữ liệu test:** `password` rỗng

**Kết quả mong đợi (theo đặc tả):** Từ chối đăng ký vì thiếu Mật khẩu. README của EShop, FR-01:

> - Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.

**Kết quả thực tế:** HTTP 200, body `{"message": "User registered successfully", "id": 10}`: Tài khoản được tạo với mật khẩu rỗng.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-75_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, ô Mật khẩu để trống bị trình duyệt chặn (TC-REG-49 Pass); lỗi nằm ở phía API. Related: #44

---

### BUG-FR01-06: API nhận Email sai định dạng

- **Issue:** #47 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_47.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] API đăng ký: Tạo tài khoản với Email sai định dạng`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `technique: BVA`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-74 (EP, thiếu `@`), TC-REG-130 (BVA, nhãn tên miền 64 ký tự)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, body `{"name": "Nguyen Van A", "email": "tc74domain.com", "password": "Abcdef1!"}`.
2. Gửi tiếp với `email` là `tc130@` + 64 chữ `a` + `.com`.

**Dữ liệu test:** `tc74domain.com` (không có `@`); `tc130@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com` (nhãn tên miền 64 ký tự)

**Kết quả mong đợi (theo đặc tả):** Từ chối đăng ký vì Email sai định dạng. README của EShop, FR-01:

> - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.

**Kết quả thực tế:** Cả hai request đều nhận HTTP 200, body `{"message": "User registered successfully", "id": ...}` (id 9 và 22): Tài khoản được tạo với Email sai định dạng.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-74_log.png`, `S6_TC-REG-130_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Đặc tả chỉ nêu ví dụ `user@domain.com`. Quy tắc định dạng dùng khi thiết kế là quy tắc của `type="email"` trong HTML5 (FR-22 yêu cầu ô Email dùng `type="email"`), theo đó mỗi nhãn tên miền dài tối đa 63 ký tự. TC-REG-74 sai định dạng theo mọi cách hiểu. Related: #44, #50

---

### BUG-FR01-07: API cho tạo nhiều tài khoản cùng một Email

- **Issue:** #48 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_48.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] API đăng ký: Tạo được nhiều tài khoản trùng Email`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-82; bước kiểm chứng (đăng ký lại cùng email) của TC-REG-71, 72, 75, 76, 77, 129

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, body `{"name": "Nguyen Van A", "email": "tc71@domain.com", "password": "Abcdef1!"}`.
2. Gửi lại đúng request ở bước 1 (cùng email `tc71@domain.com`).
3. Gửi body `{"name": "Nguyen Van A", "email": " test@eshop.com ", "password": "Abcdef1!"}` (email có 1 dấu cách ở đầu và cuối; `test@eshop.com` có sẵn trong dữ liệu mẫu).

**Dữ liệu test:** Email lặp lại `tc71@domain.com` (tương tự với `tc72`, `tc75`, `tc76`, `tc77`, `tc129@domain.com`); `␣test@eshop.com␣` (`␣` là một dấu cách)

**Kết quả mong đợi (theo đặc tả):** Lần đăng ký thứ hai với cùng email bị từ chối. README của EShop, FR-01:

> - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.

**Kết quả thực tế:** Gửi 2 lần cùng một email đều nhận HTTP 200 "User registered successfully" với 2 `id` khác nhau (ví dụ `tc71@domain.com`: id 4 và 5), tức cùng email được tạo 2 lần; lặp lại với 6 email. Email `␣test@eshop.com␣` (`␣` là một dấu cách) cũng được chấp nhận (id 19).

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-71_log.png` (gồm cả bước kiểm chứng, id 4 và 5), `S6_TC-REG-82_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Bằng chứng chính là việc trùng email chính xác (bước 1, 2), không phụ thuộc giả định nào. Với TC-REG-82, việc coi `␣test@eshop.com␣` (`␣` là một dấu cách) là trùng dựa trên giả định A07 (cắt dấu cách đầu cuối của Email) ở `features/A_FR-01_DangKy/02_ec.md`. Qua giao diện chưa kiểm được (TC-REG-45 bị BUG-FR01-01 chặn). Related: #44

---

### BUG-FR01-08: API nhận Mật khẩu không đạt yêu cầu mạnh

- **Issue:** #49 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_49.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] API đăng ký: Tạo tài khoản với mật khẩu ngắn hơn 8 ký tự hoặc không có ký tự đặc biệt`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `technique: BVA`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-76 (EP, 6 ký tự), TC-REG-77 (EP, không có ký tự đặc biệt), TC-REG-129 (BVA, 7 ký tự)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, body `{"name": "Nguyen Van A", "email": "tc76@domain.com", "password": "Abcd1!"}`.
2. Gửi tiếp với `email` `tc77@domain.com`, `password` `Abcdefg1`.
3. Gửi tiếp với `email` `tc129@domain.com`, `password` `Abcde1!`.

**Dữ liệu test:** `Abcd1!` (6 ký tự); `Abcdefg1` (không có ký tự đặc biệt); `Abcde1!` (7 ký tự, ngay dưới cận 8)

**Kết quả mong đợi (theo đặc tả):** Từ chối đăng ký vì mật khẩu không đạt yêu cầu mạnh. README của EShop, FR-01:

> - **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).

**Kết quả thực tế:** Cả ba request đều nhận HTTP 200, body `{"message": "User registered successfully", "id": ...}` (id 12, 14, 20): Tài khoản được tạo với mật khẩu yếu.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-76_log.png`, `S6_TC-REG-77_log.png`, `S6_TC-REG-129_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, các mật khẩu này bị từ chối (TC-REG-50, 56, 107 Pass), nhưng giao diện cũng từ chối cả mật khẩu hợp lệ (BUG-FR01-01). Phía API thì không kiểm tra độ mạnh mật khẩu. Related: #42, #44

---

### BUG-FR01-09: Ô Email không dùng `type="email"`

- **Issue:** #50 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_50.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Form Đăng ký: Ô Email dùng type="text" thay vì type="email"`
- **Labels:** `bug`, `severity: medium`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-96

**Mức độ:** Medium

**Điều kiện tiên quyết:** Mở `http://localhost:5173/register`; mở DevTools (F12), thẻ Console

**Các bước tái hiện:**
1. Chạy trong Console: `console.table([...document.querySelectorAll('input')].map(i => ({type_trong_HTML: i.getAttribute('type'), type_trinh_duyet_hieu: i.type})))`.
2. Đọc giá trị của ô thứ 2 (ô Email).

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Ô Email dùng `type="email"`. README của EShop, FR-22:

> - Trường Email phải dùng `type="email"`.

**Kết quả thực tế:** Ô Email có `type="text"` (3 ô trên form lần lượt là `text`, `text`, `password`). Hệ quả quan sát được: Trình duyệt không chặn email sai định dạng như `tc34domain.com`, `@domain.com`, `tc36@` khi nhấn "Đăng Ký" (TC-REG-34, 35, 36).

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-96_1.png`; `S6_TC-REG-34.png` (trình duyệt không chặn email thiếu `@`)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Ô Mật khẩu đạt yêu cầu tương ứng (`type="password"`, ký tự bị che). Related: #47

---

### BUG-FR01-10: Trường bắt buộc không có dấu `*`

- **Issue:** #51 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_51.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Form Đăng ký: Nhãn trường bắt buộc không có dấu *`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-95

**Mức độ:** Low

**Điều kiện tiên quyết:** Mở `http://localhost:5173/register`

**Các bước tái hiện:**
1. Quan sát nhãn của các ô Họ Tên, Email, Mật khẩu.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Nhãn của mọi trường bắt buộc có dấu `*`. README của EShop, FR-22 (Họ Tên, Email, Mật khẩu là bắt buộc theo FR-01):

> - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.

**Kết quả thực tế:** Nhãn "Họ Tên", "Email", "Mật khẩu" đều không có dấu `*`.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S0_01_form_dang_ky.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có

---

### BUG-FR01-11: Nút "Đăng Ký" màu đỏ thay vì xanh dương

- **Issue:** #52 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_52.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Form Đăng ký: Nút "Đăng Ký" màu đỏ thay vì xanh dương`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-92

**Mức độ:** Low

**Điều kiện tiên quyết:** Mở `http://localhost:5173/register`

**Các bước tái hiện:**
1. Quan sát màu nút "Đăng Ký".

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Nút hành động tích cực (Submit) màu xanh dương. README của EShop, FR-21:

> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.

**Kết quả thực tế:** Nút "Đăng Ký" (nút submit) nền đỏ, chữ trắng, là màu dành cho nút nguy hiểm hoặc hủy bỏ.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S0_01_form_dang_ky.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có

---

### BUG-FR01-12: Trang Đăng ký không có thẻ `<h1>`

- **Issue:** #53 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_53.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Trang Đăng ký: Không có thẻ h1`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-93

**Mức độ:** Low

**Điều kiện tiên quyết:** Mở `http://localhost:5173/register`; mở DevTools (F12), thẻ Console

**Các bước tái hiện:**
1. Chạy trong Console: `[location.pathname, document.querySelectorAll('h1').length]`.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Trang có đúng 1 thẻ `<h1>` mô tả nội dung trang. README của EShop, FR-21:

> - **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.

**Kết quả thực tế:** Console trả về `['/register', 0]`: Trang Đăng ký không có thẻ `<h1>` nào. Tiêu đề "Đăng Ký Tài Khoản" nhìn thấy trên trang không phải thẻ `<h1>`.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S6_TC-REG-93.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có

---

### BUG-FR01-13: Có chữ không phải tiếng Việt trên trang Đăng ký

- **Issue:** #54 (ảnh trang issue: `features/A_FR-01_DangKy/screenshots/S7_issue_54.png`)
- **Tiêu đề:** `[23120061][FR-01][Web] Trang Đăng ký: Tiêu đề tab "frontend-web" và thông báo bắt buộc nhập bằng tiếng Anh`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: A`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-01: Đăng ký tài khoản

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-REG-91

**Mức độ:** Low

**Điều kiện tiên quyết:** Mở `http://localhost:5173/register`

**Các bước tái hiện:**
1. Quan sát tiêu đề tab của trình duyệt.
2. Để trống ô Họ Tên, nhập Email `tc30@domain.com`, Mật khẩu `Abcdef1!`, nhấn "Đăng Ký".

**Dữ liệu test:** Họ Tên để trống

**Kết quả mong đợi (theo đặc tả):** Toàn bộ giao diện dùng tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn. README của EShop, FR-21:

> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).

**Kết quả thực tế:** (1) Tiêu đề tab là `frontend-web`, không phải tiếng Việt và không mô tả trang. (2) Khi bỏ trống ô bắt buộc, thông báo là bong bóng "Please fill out this field." bằng tiếng Anh. Các chữ còn lại trên trang, kể cả thông báo lỗi của trang (khung đỏ), là tiếng Việt.

**Ảnh chụp:** `features/A_FR-01_DangKy/screenshots/S0_01_form_dang_ky.png` (tiêu đề tab), `S6_TC-REG-30.png` (bong bóng tiếng Anh)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85 (giao diện trình duyệt tiếng Anh), EShop commit `85af3ba`

**Ghi chú:** Bong bóng là thông báo kiểm tra bắt buộc nhập của trình duyệt, hiện theo ngôn ngữ của trình duyệt; được tính vào lỗi vì người dùng thấy nó trên trang Đăng ký và trang không cung cấp thông báo tiếng Việt thay thế. Các chữ "EShop", "Email", "SUT" được chấp nhận là tên riêng hoặc thuật ngữ thông dụng.

---

### Quan sát ngoài test case: Có thành bug không

Xét 3 quan sát ở mục 6 của `06_results.md`:

| Mã | Quan sát | Kết luận | Lý do |
|---|---|---|---|
| QS01 | Bong bóng "Please fill out this field." của ô Mật khẩu đè một phần lên nút "Đăng Ký" | Không thành bug | FR-22 chỉ yêu cầu thông báo lỗi nằm **trên** nút submit, không phải bên dưới; bong bóng vẫn nằm phía trên nút (TC-REG-97 Pass). Vị trí bong bóng do trình duyệt vẽ, không phải bố cục của trang |
| QS02 | Mật khẩu hợp lệ `Test1234!` (mật khẩu của tài khoản mẫu) bị từ chối | Đưa vào BUG-FR01-01 | Cùng lỗi với TC-REG-01, 108 (mật khẩu hợp lệ bị giao diện từ chối); dùng làm dữ liệu test bổ sung |
| QS03 | Qua API, cùng một email được tạo 2 lần | Đưa vào BUG-FR01-07 | Vi phạm trực tiếp FR-01 ("là duy nhất trong hệ thống"), có bằng chứng trong log với 6 email; là bằng chứng chính của bug này |

### Test case Blocked và bug gây chặn

| Bug gây chặn | Test case bị chặn |
|---|---|
| BUG-FR01-01 | TC-REG-31, 33, 34, 35, 36, 37, 38, 39, 45, 78, 79, 81, 101, 104 |
| BUG-FR01-02 | TC-REG-59, 60, 61, 62 |

---

## FR-07: Giỏ hàng

- Nguồn: `features/B_FR-07_GioHang/06_results.md` (kết quả chạy ngày 21/10/2026, S6 rút gọn), bộ test case ở `features/B_FR-07_GioHang/05_final_tc.md`
- Môi trường chung: Windows 11 Home Single Language 10.0.26200; Google Chrome 155.0.8059.85; EShop commit `85af3ba`; backend `http://localhost:3000`; web `http://localhost:5173`
- Điều kiện tiên quyết chung: Đã reset dữ liệu EShop về dữ liệu mẫu. Giao diện: Đăng nhập Web bằng `test@eshop.com` / `Test1234!`, giỏ trống. API: Lấy token bằng `POST /api/login`
- Body cơ sở khi gọi `POST /api/cart`: `{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}` (`id` 1 là iPhone 15 Pro Max, giá 30,000,000 ₫)

### Tổng hợp

| Bug | Tiêu đề ngắn | Severity | Technique | Test case | Issue |
|---|---|---|---|---|---|
| BUG-FR07-01 | API thêm vào giỏ nhận số lượng không hợp lệ | High | EP, BVA | TC-CART-31, 32, 33, 34, 102 | #67 |
| BUG-FR07-02 | API giỏ hàng lưu đơn giá do client gửi | High | EP | TC-CART-51 | #68 |
| BUG-FR07-03 | API thêm vào giỏ nhận sản phẩm không tồn tại | High | EP | TC-CART-30 | #69 |
| BUG-FR07-04 | Thêm sản phẩm đã có trong giỏ tạo dòng mới thay vì tăng số lượng | Medium | EP | TC-CART-03, TC-CART-02, TC-CART-08 | #70 |
| BUG-FR07-05 | Cột Số lượng không có nút +/- | Medium | EP, BVA | TC-CART-04, 05, 06 (Blocked) | #71 |
| BUG-FR07-06 | Xóa sản phẩm không có dialog xác nhận | Medium | EP | TC-CART-07, 08, 09 | #72 |
| BUG-FR07-07 | Nút "Thêm vào giỏ hàng" không thêm khi giữ số lượng mặc định 1 | Medium | EP, BVA | TC-CART-01 | #73 |
| BUG-FR07-08 | Giỏ trên Web mất sau khi tải lại trang, không khớp giỏ của API | Medium | EP | TC-CART-50 | #74 |
| BUG-FR07-09 | Nhãn tổng tiền là "Tổng tạm tính" thay vì "Tổng cộng" | Low | EP | TC-CART-90 | #75 |
| BUG-FR07-10 | Cột "Giá" thay vì "Đơn giá" | Low | EP | TC-CART-90 | #76 |
| BUG-FR07-11 | Giỏ có hàng không có nút "Tiếp tục mua sắm" | Low | EP | TC-CART-11 | #77 |
| BUG-FR07-12 | Không có toast hay badge sau khi thêm vào giỏ | Low | EP | TC-CART-01, TC-CART-02 | #78 |
| BUG-FR07-13 | Link "Giỏ hàng" không có badge số lượng | Low | EP | TC-CART-02 | #79 |
| BUG-FR07-14 | Giỏ trống không có hình minh họa | Low | EP | TC-CART-91, TC-CART-10, TC-CART-09 | #80 |
| BUG-FR07-15 | Tiêu đề tab không phải tiếng Việt | Low | EP | TC-CART-92 | #81 |
| BUG-FR07-16 | Nút "Tiến hành thanh toán" màu xanh lá thay vì xanh dương | Low | EP | TC-CART-93 | #82 |
| BUG-FR07-17 | Navbar không highlight mục "Giỏ hàng" | Low | EP | TC-CART-95 | #83 |
| BUG-FR07-18 | Trang Giỏ hàng không có breadcrumb | Low | EP | TC-CART-95 | #84 |

Label chung cho mọi bug của FR-07: `bug` (template tự gắn), `platform: web`, `pool: B`. Label `severity` và `technique` theo bảng trên.

BUG-FR07-02, 03, 08, 11 và phần TC-CART-34 của BUG-FR07-01 dựa trên giả định hoặc quan sát; sinh viên đã quyết định đưa thành bug (mục "Khác giả định và quan sát" cuối mục FR-07).

---

### BUG-FR07-01: API thêm vào giỏ nhận số lượng không hợp lệ

- **Issue:** #67 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_67.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] API thêm vào giỏ hàng: Nhận số lượng 0, âm, thập phân, không phải số hoặc thiếu số lượng`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `technique: BVA`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-31 (`quantity` 0), TC-CART-32 (1.5), TC-CART-33 (`"abc"`), TC-CART-34 (thiếu `quantity`), TC-CART-102 (-1)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token của `test@eshop.com`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/cart`, header `Authorization: Bearer <token>`, `Content-Type: application/json`, body cơ sở với `"quantity": 0`.
2. Lặp lại bước 1 với `"quantity": 1.5`, `"quantity": "abc"`, `"quantity": -1`, và với body bỏ hẳn trường `quantity`.
3. Gọi `GET http://localhost:3000/api/cart` (cùng token).

**Dữ liệu test:** `quantity` = `0`, `1.5`, `"abc"`, `-1`, không có trường `quantity`

**Kết quả mong đợi (theo đặc tả):** Từ chối, không thêm vào giỏ khi số lượng không phải số nguyên dương. README của EShop, FR-06 (ô Số lượng dùng để thêm vào giỏ):

> - Có ô nhập **Số lượng** (chỉ nhận số nguyên dương, tối thiểu là 1).

**Kết quả thực tế:** Cả 5 request nhận HTTP 200 `{"message": "Added to cart"}`. `GET /api/cart` có các dòng `id` 1 với `quantity` là `0`, `1.5`, `"abc"`, `-1` và một dòng không có trường `quantity`.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-31_log.png` (request `quantity` 0), `S6_TC-CART-50_log_1.png`, `S6_TC-CART-50_log_2.png` (phản hồi `GET /api/cart` với các dòng đã lưu) (ảnh chụp đoạn log); log đầy đủ: `features/B_FR-07_GioHang/logs/S6_api_20261021_074419.log` (5 request), `features/B_FR-07_GioHang/logs/S6_api_20261021_075653.log` (phản hồi `GET /api/cart` liệt kê các dòng đã lưu)

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/B_FR-07_GioHang/scripts/run_api_tests.py`)

**Ghi chú:** API spec mục 4.2 không nêu ràng buộc riêng cho `quantity`; ràng buộc lấy theo FR-06 vì đây là số lượng được thêm vào giỏ (giả định A25 ở `features/B_FR-07_GioHang/02_ec.md`). Request thiếu token bị từ chối đúng (HTTP 401, TC-CART-35). Các bug BUG-FR07-01, 02, 03 cho thấy API thêm vào giỏ không kiểm tra dữ liệu đầu vào

---

### BUG-FR07-02: API giỏ hàng lưu đơn giá do client gửi

- **Issue:** #68 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_68.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] API thêm vào giỏ hàng: Lưu đơn giá do client gửi thay vì giá của sản phẩm`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-51

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token của `test@eshop.com`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/cart`, header `Authorization: Bearer <token>`, body cơ sở với `"price": 1`.
2. Gọi `GET http://localhost:3000/api/cart`.

**Dữ liệu test:** `id` 1 (iPhone 15 Pro Max, giá 30,000,000 ₫), `price` = `1`

**Kết quả mong đợi (theo đặc tả):** Giỏ dùng giá của sản phẩm trong hệ thống (30,000,000 ₫), không dùng giá client gửi; hoặc request bị từ chối. Suy ra từ nguyên tắc ở README của EShop, FR-08:

> - Backend phải tự tính lại tổng tiền; không chấp nhận giá trị `total_amount` do client gửi lên.

**Kết quả thực tế:** HTTP 200 `{"message": "Added to cart"}`; `GET /api/cart` có dòng `id` 1, `name` "iPhone 15 Pro Max", `price` 1, `quantity` 1.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-51_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/B_FR-07_GioHang/logs/S6_api_20261021_080006.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/B_FR-07_GioHang/scripts/run_api_tests.py`)

**Ghi chú:** FR-07 và API spec không nói rõ giỏ dùng giá nào; mong đợi dựa trên giả định A24 (`features/B_FR-07_GioHang/02_ec.md`). `name` do client gửi cũng được lưu nguyên văn (TC-CART-52, 53). Chưa kiểm việc thanh toán (FR-08) có dùng giá này không

---

### BUG-FR07-03: API thêm vào giỏ nhận sản phẩm không tồn tại

- **Issue:** #69 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_69.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] API thêm vào giỏ hàng: Nhận id sản phẩm không tồn tại`
- **Labels:** `bug`, `severity: high`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-30

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token của `test@eshop.com`

**Các bước tái hiện:**
1. Gửi `GET http://localhost:3000/api/products/9999`.
2. Gửi `POST http://localhost:3000/api/cart`, header `Authorization: Bearer <token>`, body cơ sở với `"id": 9999`.
3. Gọi `GET http://localhost:3000/api/cart`.

**Dữ liệu test:** `id` = `9999`

**Kết quả mong đợi (theo đặc tả):** Từ chối, không thêm vào giỏ vì sản phẩm không tồn tại. API spec mục 4.2 mô tả API này là thêm một sản phẩm vào giỏ:

> ### 4.2 Thêm vào giỏ hàng
> - **Endpoint:** `POST /api/cart`

**Kết quả thực tế:** Bước 1: HTTP 200, body `{}` (không có sản phẩm 9999). Bước 2: HTTP 200 `{"message": "Added to cart"}`. Bước 3: Giỏ có dòng `id` 9999 với `name` "iPhone 15 Pro Max", `price` 30000000 do client gửi.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-30_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/B_FR-07_GioHang/logs/S6_api_20261021_074419.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/B_FR-07_GioHang/scripts/run_api_tests.py`)

**Ghi chú:** Đặc tả không nêu trực tiếp; mong đợi dựa trên giả định A24 (`features/B_FR-07_GioHang/02_ec.md`). Related: #67 (BUG-FR07-01), #68 (BUG-FR07-02)

---

### BUG-FR07-04: Thêm sản phẩm đã có trong giỏ tạo dòng mới thay vì tăng số lượng

- **Issue:** #70 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_70.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Giỏ hàng: Thêm sản phẩm đã có trong giỏ tạo dòng mới thay vì tăng số lượng`
- **Labels:** `bug`, `severity: medium`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-03 (trang chi tiết), TC-CART-02, TC-CART-08 (trang chủ)

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ trống

**Các bước tái hiện:**
1. Ở trang chủ, bấm "Thêm vào giỏ" của Samsung Galaxy S24 Ultra 2 lần; mở trang Giỏ hàng.
2. Mở trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 3, bấm "Thêm vào giỏ hàng" (bấm lại nếu nút chưa đổi thành "Đã thêm").
3. Ở trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 2, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng.

**Dữ liệu test:** Samsung Galaxy S24 Ultra × 1 hai lần; iPhone 15 Pro Max × 3 rồi × 2

**Kết quả mong đợi (theo đặc tả):** Mỗi sản phẩm một dòng; thêm lại thì số lượng tăng (Samsung Số lượng 2; iPhone Số lượng 5). README của EShop, FR-07:

> - Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.

**Kết quả thực tế:** Bước 1: 2 dòng "Samsung Galaxy S24 Ultra" riêng, mỗi dòng Số lượng 1. Bước 3: 2 dòng "iPhone 15 Pro Max" riêng, Số lượng 2 và 3.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png` (2 dòng Samsung), `S6_TC-CART-03_3.png` (2 dòng iPhone)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Qua API cũng vậy: Mỗi lần `POST /api/cart` cùng `id` 1 tạo một dòng mới (`features/B_FR-07_GioHang/logs/S6_api_20261021_075653.log`). Tổng tiền vẫn bằng tổng các dòng

---

### BUG-FR07-05: Cột Số lượng không có nút +/-

- **Issue:** #71 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_71.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Cột Số lượng không có nút +/- để chỉnh số lượng`
- **Labels:** `bug`, `severity: medium`, `platform: web`, `technique: EP`, `technique: BVA`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-04, TC-CART-05, TC-CART-06 (Blocked vì không có nút)

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có ít nhất 1 sản phẩm

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Quan sát cột "Số lượng" ở mỗi dòng.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Cột Số lượng có nút + và - để chỉnh. README của EShop, FR-07:

> - Hiển thị danh sách sản phẩm với các cột: **Sản phẩm**, **Đơn giá**, **Số lượng** (có nút +/- để chỉnh), **Thành tiền**, **Thao tác**.

**Kết quả thực tế:** Cột "Số lượng" chỉ hiện con số (ví dụ "1", "250"), không có nút + hay -, không có ô nhập. Không có cách chỉnh số lượng trên trang Giỏ hàng.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S0_03_gio_hang_co_hang.png`, `S6_TC-CART-03_3.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Muốn đổi số lượng phải xóa dòng rồi thêm lại. API spec cũng không mô tả API đổi số lượng

---

### BUG-FR07-06: Xóa sản phẩm không có dialog xác nhận

- **Issue:** #72 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_72.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Bấm Xóa xóa sản phẩm ngay, không có dialog xác nhận`
- **Labels:** `bug`, `severity: medium`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-07, TC-CART-08, TC-CART-09

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có 2 dòng Samsung Galaxy S24 Ultra

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Bấm "Xóa" ở một dòng.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Hiện dialog xác nhận; sản phẩm chỉ bị xóa sau khi xác nhận. README của EShop, FR-07 và FR-24:

> - Nút **Xóa sản phẩm** phải có dialog xác nhận trước khi thực hiện.
>
> - Khi xóa item khỏi giỏ phải có dialog xác nhận.

**Kết quả thực tế:** Không có dialog; dòng bị xóa ngay, "Tổng tạm tính:" giảm từ 56,000,000 ₫ xuống 28,000,000 ₫. Xóa dòng cuối cùng cũng không có dialog.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png` (trước khi xóa), `S6_TC-CART-08.png` (sau khi bấm "Xóa")

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có bước hủy nên không lấy lại được sản phẩm đã bấm nhầm

---

### BUG-FR07-07: Nút "Thêm vào giỏ hàng" không thêm khi giữ số lượng mặc định 1

- **Issue:** #73 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_73.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang chi tiết sản phẩm: Nút Thêm vào giỏ hàng không thêm khi giữ số lượng mặc định 1`
- **Labels:** `bug`, `severity: medium`, `platform: web`, `technique: EP`, `technique: BVA`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-01

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ trống

**Các bước tái hiện:**
1. Mở trang chi tiết iPhone 15 Pro Max (`localhost:5173/product/1`).
2. Giữ nguyên "Số lượng:" = 1, bấm "Thêm vào giỏ hàng".
3. Mở trang Giỏ hàng.

**Dữ liệu test:** "Số lượng:" = 1 (giá trị mặc định)

**Kết quả mong đợi (theo đặc tả):** Sản phẩm được thêm vào giỏ với số lượng 1 (1 là số lượng hợp lệ nhỏ nhất) và có phản hồi trực quan. README của EShop, FR-06:

> - Có ô nhập **Số lượng** (chỉ nhận số nguyên dương, tối thiểu là 1).
> - Nút **Thêm vào giỏ hàng** — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).

**Kết quả thực tế:** Không có gì thay đổi: Nút vẫn là "Thêm vào giỏ hàng", giỏ vẫn trống. Chỉ khi đổi số lượng rồi bấm thì nút mới thành "Đã thêm" và sản phẩm vào giỏ; khi đó cũng phải bấm 2 lần (lần đầu không có phản hồi), giỏ chỉ thêm một lần.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-01_1.png` (sau khi bấm, nút không đổi), `S0_05_gio_hang_trong.png` (giỏ trống; trang giống ảnh này nên không chụp lại), `S6_TC-CART-03_1.png` (nút "Đã thêm" sau khi đổi số lượng)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Lỗi nằm ở nút của trang chi tiết (FR-06), là đường vào chính của giỏ hàng; trong nhóm không ai làm FR-06 nên báo ở FR-07. Đi vòng được bằng cách đổi số lượng hoặc thêm từ trang chủ

---

### BUG-FR07-08: Giỏ trên Web mất sau khi tải lại trang, không khớp giỏ của API

- **Issue:** #74 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_74.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Giỏ hàng: Sản phẩm trong giỏ mất sau khi tải lại trang, giỏ trên Web không khớp GET /api/cart`
- **Labels:** `bug`, `severity: medium`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-50

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`; có token của `test@eshop.com` để gọi API

**Các bước tái hiện:**
1. Trên Web, thêm vài sản phẩm vào giỏ (ví dụ Bàn phím cơ Keychron Q1 × 250 từ trang chi tiết); mở trang Giỏ hàng, thấy các dòng.
2. Gọi `GET http://localhost:3000/api/cart` (token của `test@eshop.com`).
3. Gửi `POST http://localhost:3000/api/cart` với body cơ sở; gọi lại `GET /api/cart`.
4. Trên Web, bấm F5 ở trang Giỏ hàng.

**Dữ liệu test:** Body cơ sở

**Kết quả mong đợi (theo đặc tả):** Trang Giỏ hàng và `GET /api/cart` là cùng một giỏ của người dùng; sản phẩm đã thêm vẫn còn khi tải lại trang. API spec mục 4.1 và README của EShop, FR-08:

> ### 4.1 Lấy giỏ hàng
> - **Endpoint:** `GET /api/cart`
>
> - **Tổng tiền thanh toán** được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp.

**Kết quả thực tế:** Bước 1: Trang có 3 dòng (07:38). Bước 2: `GET /api/cart` trả giỏ trống (07:44). Bước 3: `GET /api/cart` có dòng vừa thêm. Bước 4: Trang Giỏ hàng trống, không có 3 dòng đã thêm trên Web, cũng không có các dòng của API.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-03_3.png` (giỏ trên Web có hàng), `S0_05_gio_hang_trong.png` (trang trống sau F5; trang giống ảnh này nên không chụp lại), `S6_TC-CART-50_log_1.png`, `S6_TC-CART-50_log_2.png` (đoạn log `GET /api/cart`); log đầy đủ: `features/B_FR-07_GioHang/logs/S6_api_20261021_074419.log`, `features/B_FR-07_GioHang/logs/S6_api_20261021_075653.log`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`; API gọi bằng script Python (`features/B_FR-07_GioHang/scripts/run_api_tests.py`)

**Ghi chú:** Đặc tả không nói rõ giỏ phải được giữ khi tải lại trang (câu hỏi mở Q14 ở `features/B_FR-07_GioHang/00_spec.md`); mong đợi dựa trên việc API spec có API "Lấy giỏ hàng" theo người dùng. Hệ quả: Người dùng mất giỏ khi tải lại trang; chưa kiểm thanh toán (FR-08) dùng giỏ nào

---

### BUG-FR07-09: Nhãn tổng tiền là "Tổng tạm tính" thay vì "Tổng cộng"

- **Issue:** #75 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_75.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Nhãn tổng tiền là "Tổng tạm tính" thay vì "Tổng cộng"`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-90

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có ít nhất 1 sản phẩm

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Quan sát nhãn bên trái giá trị tổng tiền.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Nhãn là "Tổng cộng". README của EShop, FR-07:

> - Tổng tiền hiển thị nhãn chính xác: **"Tổng cộng"** (không phải "Tổng tạm tính").

**Kết quả thực tế:** Nhãn là "Tổng tạm tính:", đúng chữ mà đặc tả ghi là không được dùng.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png`, `S0_03_gio_hang_co_hang.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có

---

### BUG-FR07-10: Cột "Giá" thay vì "Đơn giá"

- **Issue:** #76 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_76.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Cột đơn giá có nhãn "Giá" thay vì "Đơn giá"`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-90

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có ít nhất 1 sản phẩm

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Quan sát tên các cột của bảng.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Các cột "Sản phẩm", "Đơn giá", "Số lượng", "Thành tiền", "Thao tác". README của EShop, FR-07:

> - Hiển thị danh sách sản phẩm với các cột: **Sản phẩm**, **Đơn giá**, **Số lượng** (có nút +/- để chỉnh), **Thành tiền**, **Thao tác**.

**Kết quả thực tế:** Các cột là "Sản phẩm", "Giá", "Số lượng", "Thành tiền", "Thao tác".

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png`, `S0_03_gio_hang_co_hang.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Phần nút +/- của cùng câu đặc tả báo riêng ở BUG-FR07-05

---

### BUG-FR07-11: Giỏ có hàng không có nút "Tiếp tục mua sắm"

- **Issue:** #77 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_77.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Khi giỏ có hàng, nút quay về trang chủ có nhãn "← Mua tiếp" thay vì "Tiếp tục mua sắm"`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-11

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có ít nhất 1 sản phẩm

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Quan sát các nút dưới bảng.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Có nút "Tiếp tục mua sắm" để quay về trang chủ. README của EShop, FR-07:

> - Có nút **Tiếp tục mua sắm** để quay về trang chủ.

**Kết quả thực tế:** Chỉ có nút "← Mua tiếp" (bấm vào thì về trang chủ). Nhãn "Tiếp tục mua sắm" chỉ có ở trạng thái giỏ trống.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png` (giỏ có hàng), `S0_05_gio_hang_trong.png` (giỏ trống)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Chức năng quay về trang chủ hoạt động (TC-CART-11 Pass về điều hướng); chỉ sai nhãn

---

### BUG-FR07-12: Không có toast hay badge sau khi thêm vào giỏ

- **Issue:** #78 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_78.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Thêm vào giỏ hàng: Không có toast hay badge cập nhật sau khi bấm Thêm vào giỏ`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-01, TC-CART-02

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`

**Các bước tái hiện:**
1. Ở trang chủ, bấm "Thêm vào giỏ" của Samsung Galaxy S24 Ultra; quan sát trang.
2. Ở trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 3, bấm "Thêm vào giỏ hàng"; quan sát trang.

**Dữ liệu test:** Samsung Galaxy S24 Ultra (trang chủ); iPhone 15 Pro Max, số lượng 3 (trang chi tiết)

**Kết quả mong đợi (theo đặc tả):** Có phản hồi trực quan: Toast hoặc badge cập nhật. README của EShop, FR-24:

> - Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).

**Kết quả thực tế:** Trang chủ: Không có gì thay đổi (sản phẩm vẫn vào giỏ). Trang chi tiết: Chỉ nhãn nút đổi thành "Đã thêm". Không có toast, không có badge ở cả hai trang.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-03_1.png` (trang chi tiết, chỉ đổi nhãn nút), `S6_TC-CART-02.png` (giỏ đã có Samsung nhưng navbar không có badge). Trang chủ sau khi bấm không thay đổi gì nên sinh viên không chụp

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Nhãn nút "Đã thêm" không tính là phản hồi theo đặc tả vì FR-06 nêu rõ dạng "toast notification hoặc badge cập nhật" (quyết định của sinh viên ở S6). Badge báo riêng ở BUG-FR07-13

---

### BUG-FR07-13: Link "Giỏ hàng" không có badge số lượng

- **Issue:** #79 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_79.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Navbar: Link Giỏ hàng không có badge số lượng sản phẩm trong giỏ`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-02

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có ít nhất 1 sản phẩm

**Các bước tái hiện:**
1. Mở trang Giỏ hàng (hoặc bất kỳ trang nào).
2. Quan sát link "Giỏ hàng" trên navbar.

**Dữ liệu test:** Giỏ có 2 dòng Samsung Galaxy S24 Ultra

**Kết quả mong đợi (theo đặc tả):** Link "Giỏ hàng" có badge số lượng sản phẩm trong giỏ. README của EShop, FR-23:

> - Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.

**Kết quả thực tế:** Link chỉ có chữ "Giỏ hàng", không có badge, dù giỏ có 2 dòng.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png`, `S0_03_gio_hang_co_hang.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có

---

### BUG-FR07-14: Giỏ trống không có hình minh họa

- **Issue:** #80 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_80.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Giỏ trống không có hình minh họa`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-91, TC-CART-10, TC-CART-09

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ trống

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Có hình minh họa và thông báo rõ ràng. README của EShop, FR-07 và FR-24:

> - Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng.
>
> - Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.

**Kết quả thực tế:** Chỉ có dòng chữ "Giỏ hàng của bạn đang trống" và liên kết "Tiếp tục mua sắm"; không có hình hay biểu tượng.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S0_05_gio_hang_trong.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Phần thông báo đạt yêu cầu

---

### BUG-FR07-15: Tiêu đề tab không phải tiếng Việt

- **Issue:** #81 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_81.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Tiêu đề tab là "frontend-web", không phải tiếng Việt`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-92

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Quan sát tiêu đề tab của trình duyệt.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Toàn bộ giao diện dùng tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn. README của EShop, FR-21:

> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).

**Kết quả thực tế:** Tiêu đề tab là "frontend-web" (cả khi giỏ có hàng và khi trống). Chữ trên trang là tiếng Việt, trừ tên riêng "EShop", "SUT".

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png`, `S0_05_gio_hang_trong.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Related: #54 (FR-01, BUG-FR01-13), #57 (FR-17, BUG-FR17-10)

---

### BUG-FR07-16: Nút "Tiến hành thanh toán" màu xanh lá thay vì xanh dương

- **Issue:** #82 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_82.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Nút "Tiến hành thanh toán" màu xanh lá thay vì xanh dương`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-93

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`, giỏ có ít nhất 1 sản phẩm

**Các bước tái hiện:**
1. Mở trang Giỏ hàng.
2. Quan sát màu nút "Tiến hành thanh toán".

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Nút hành động tích cực (Mua hàng) màu xanh dương. README của EShop, FR-21:

> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.

**Kết quả thực tế:** Nút "Tiến hành thanh toán" nền xanh lá, chữ trắng.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Nút "Xóa" chữ đỏ, đạt yêu cầu tương ứng. Coi "Tiến hành thanh toán" là nút tích cực theo giả định A22 (`features/B_FR-07_GioHang/02_ec.md`). Related: #52 (FR-01, BUG-FR01-11), #58 (FR-17, BUG-FR17-11)

---

### BUG-FR07-17: Navbar không highlight mục "Giỏ hàng"

- **Issue:** #83 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_83.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Navbar: Không highlight mục Giỏ hàng khi đang ở trang Giỏ hàng`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-95

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`

**Các bước tái hiện:**
1. Ở trang chủ, quan sát link "Giỏ hàng" trên navbar.
2. Bấm link "Giỏ hàng", quan sát lại link đó.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Mục "Giỏ hàng" được highlight khi đang ở trang Giỏ hàng. README của EShop, FR-23:

> - Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.

**Kết quả thực tế:** Link "Giỏ hàng" chữ trắng, giống hệt ở trang chủ; không đổi màu, không gạch chân, không in đậm.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-10.png` (trang chủ), `S6_TC-CART-02.png` (trang Giỏ hàng)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Không có

---

### BUG-FR07-18: Trang Giỏ hàng không có breadcrumb

- **Issue:** #84 (ảnh trang issue: `features/B_FR-07_GioHang/screenshots/S7_issue_84.png`)
- **Tiêu đề:** `[23120061][FR-07][Web] Trang Giỏ hàng: Không có breadcrumb`
- **Labels:** `bug`, `severity: low`, `platform: web`, `technique: EP`, `pool: B`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-07: Giỏ hàng

**Nền tảng:** Web

**Test case phát hiện lỗi:** TC-CART-95

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web bằng `test@eshop.com`

**Các bước tái hiện:**
1. Mở trang Giỏ hàng (khi có hàng và khi trống).
2. Quan sát phần đầu trang, dưới navbar.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Có breadcrumb. README của EShop, FR-23:

> - Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).

**Kết quả thực tế:** Không có breadcrumb; dưới navbar là tiêu đề "Giỏ Hàng" (giỏ có hàng) hoặc dòng thông báo giỏ trống.

**Ảnh chụp:** `features/B_FR-07_GioHang/screenshots/S6_TC-CART-02.png`, `S0_05_gio_hang_trong.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Trang chi tiết sản phẩm cũng không có breadcrumb (`S6_TC-CART-01_1.png`); phần đó thuộc FR-06, không báo ở đây

---

### Khác giả định và quan sát: Quyết định của sinh viên

Cột "Đề xuất" là của AI; cột "Quyết định" là của sinh viên.

| Mã | Nguồn | Hành vi quan sát | Đề xuất | Lý do | Quyết định |
|---|---|---|---|---|---|
| KG01 | TC-CART-51 (A24) | API lưu `price` 1 do client gửi | Thành bug riêng, High: BUG-FR07-02 | Đặc tả không nói giỏ dùng giá nào; theo nguyên tắc FR-08 (backend không tin số tiền client gửi), giá do client đặt là dữ liệu sai mà người dùng thường không tránh được (lưu đồ mục 4.3, câu 2) | Theo đề xuất: BUG-FR07-02, High |
| KG02 | TC-CART-30 (A24) | API nhận `id` 9999 không tồn tại | Thành bug riêng, High: BUG-FR07-03 | Hệ thống chấp nhận dữ liệu sai (lưu đồ câu 2); khác nguyên nhân với số lượng | Theo đề xuất: BUG-FR07-03, High |
| KG03 | TC-CART-34 (A25) | API nhận body thiếu `quantity`, lưu dòng không có số lượng | Gộp vào BUG-FR07-01 | Cùng trường `quantity`, cùng hệ quả (dòng có số lượng không hợp lệ) | Theo đề xuất: Gộp vào BUG-FR07-01 |
| KG04 | TC-CART-11 (Q28) | Giỏ có hàng chỉ có nút "← Mua tiếp"; TC-CART-11 Pass vì phần điều hướng đúng | Thành bug riêng, Low: BUG-FR07-11; giữ trạng thái Pass của TC-CART-11 | Q28 đã chốt xét FR07-R12 ở cả hai trạng thái; checklist TC-CART-91 chỉ xét giỏ trống | Theo đề xuất: BUG-FR07-11, Low; TC-CART-11 giữ Pass |
| QS01 | `06_results.md` mục 4.F, ghi nhận 8 | Giỏ trên Web mất sau F5 và không khớp `GET /api/cart` | Thành bug, Medium: BUG-FR07-08 | Theo lưu đồ, giỏ mất có thể xem là "mất dữ liệu" (Critical), nhưng đặc tả không nói về lưu giỏ (Q14) và có cách đi vòng (không tải lại trang) nên đề xuất Medium | Theo đề xuất: BUG-FR07-08, Medium |
| QS02 | Mục 4.F, ghi nhận 2 | Nút ở trang chi tiết phải bấm 2 lần mới thêm | Gộp vào BUG-FR07-07 | Cùng nút, cùng hệ quả (bấm mà không thêm) | Theo đề xuất: Gộp vào BUG-FR07-07 |
| QS03 | Mục 4.F, ghi nhận 7 | Qua API, mỗi lần `POST` cùng `id` tạo dòng mới | Gộp vào BUG-FR07-04 (Ghi chú) | Cùng yêu cầu FR07-R08, R09 | Theo đề xuất: Gộp vào BUG-FR07-04 |

### Test case Blocked và bug gây chặn

| Bug gây chặn | Test case bị chặn |
|---|---|
| BUG-FR07-05 | TC-CART-04, 05, 06 |
| BUG-FR07-08 | TC-CART-52 (không xem được tên trên trang Giỏ hàng vì trang không hiển thị giỏ của API) |

---

## FR-17: Quản lý mã giảm giá

- Nguồn: `features/C_FR-17_QuanLyCoupon/06_results.md` (kết quả chạy ngày 21/10/2026, S6 rút gọn), bộ test case ở `features/C_FR-17_QuanLyCoupon/05_final_tc.md`
- Môi trường chung: Windows 11 Home Single Language 10.0.26200; Google Chrome 155.0.8059.85; EShop commit `85af3ba`; backend `http://localhost:3000`; Web Admin `http://localhost:5174`
- Điều kiện tiên quyết chung: Đã reset dữ liệu EShop về dữ liệu mẫu (có 4 mã `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`). Giao diện: Đăng nhập Web Admin bằng `admin@eshop.com` / `Admin123!`, mở menu "Mã Giảm Giá". API: Lấy token bằng `POST /api/login`
- Body cơ sở khi gọi API: `{"code": "<mã>", "type": "percent", "discount_value": 15, "min_order_amount": 300000, "expired_at": "2099-12-31", "max_uses_per_user": 3}`

### Tổng hợp

| Bug | Tiêu đề ngắn | Severity | Technique | Test case | Issue |
|---|---|---|---|---|---|
| BUG-FR17-01 | User thường tạo và xóa được mã qua API Admin | Critical | EP | TC-CPN-75, TC-CPN-79 | #60 |
| BUG-FR17-02 | API tạo được mã khi thiếu trường bắt buộc | High | EP | TC-CPN-66, TC-CPN-70, TC-CPN-65 (dòng A), TC-CPN-143 (dòng C) | #61 |
| BUG-FR17-03 | API nhận `type` không phải `percent` hoặc `fixed` | High | EP | TC-CPN-65 (dòng B) | #62 |
| BUG-FR17-04 | Giao diện tạo được mã giảm 0% | High | EP | TC-CPN-38 | #55 |
| BUG-FR17-05 | API nhận giá trị không phải số ở các trường số | High | EP | TC-CPN-67 | #63 |
| BUG-FR17-06 | Số `9007199254740993` bị lưu thành `9007199254740992` | High | BVA | TC-CPN-131 | #64 |
| BUG-FR17-07 | Request không phải JSON gây lỗi 500, lộ đường dẫn tệp trên máy chủ | Medium | EP | TC-CPN-69 | #65 |
| BUG-FR17-08 | Giao diện tạo được mã giảm 150% | Medium | EP | TC-CPN-37 | #56 |
| BUG-FR17-09 | API lưu `expired_at` không phải ngày hợp lệ | Medium | EP | TC-CPN-68 | #66 |
| BUG-FR17-10 | Có chữ không phải tiếng Việt trên trang Quản lý Mã Giảm Giá | Low | EP | TC-CPN-91, TC-CPN-32 | #57 |
| BUG-FR17-11 | Nút "Tạo mã" màu cam thay vì xanh dương | Low | EP | TC-CPN-92 | #58 |
| BUG-FR17-12 | Trường bắt buộc không có dấu `*` | Low | EP | TC-CPN-90 | #59 |

Label chung cho mọi bug của FR-17: `bug` (template tự gắn), `platform: admin`, `pool: C`. Label `severity` và `technique` theo bảng trên.

---

### BUG-FR17-01: User thường tạo và xóa được mã qua API Admin

- **Issue:** #60 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_60.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API quản lý mã giảm giá: Tài khoản user thường tạo và xóa được mã`
- **Labels:** `bug`, `severity: critical`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-75 (tạo mã), TC-CPN-79 (xóa mã)

**Mức độ:** Critical

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/login`, body `{"email": "test@eshop.com", "password": "Test1234!"}`; lấy `token` (tài khoản user thường).
2. Gửi `POST http://localhost:3000/api/admin/coupons`, header `Authorization: Bearer <token user thường>`, `Content-Type: application/json`, body cơ sở với `"code": "FR17TC75"`.
3. Bằng token admin, tạo mã `FR17TC79` (body cơ sở) và lấy `id` của nó từ `GET /api/coupons`.
4. Gửi `DELETE http://localhost:3000/api/admin/coupons/<id của FR17TC79>`, header `Authorization: Bearer <token user thường>`.

**Dữ liệu test:** Token của `test@eshop.com` (tài khoản user thường trong dữ liệu mẫu)

**Kết quả mong đợi (theo đặc tả):** Cả hai request của user thường bị từ chối; không tạo, không xóa được mã. README của EShop, FR-12 và mục 9:

> - Phân hệ Admin chỉ dành cho tài khoản có `role = 'admin'`.
> - **Tất cả** các API Admin (`/api/admin/*`) và các API có tính ảnh hưởng dữ liệu (`POST/PUT/DELETE /api/products`, `/api/categories`, `/api/coupons`) đều phải yêu cầu:
>   1. Token JWT hợp lệ.
>   2. `role = 'admin'` trong Token.
>
> SEC-03: API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token.

**Kết quả thực tế:** Bước 2: HTTP 200 `{"message": "Coupon created", "id": 28}`; `GET /api/coupons` có mã `FR17TC75`. Bước 4: HTTP 200 `{"message": "Coupon deleted"}`; mã `FR17TC79` (id 30) không còn trong danh sách.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-75_log.png`, `S6_TC-CPN-79_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** Request không có header `Authorization` hoặc có token sai bị từ chối (HTTP 401, 403 ở TC-CPN-72, 73, 74, 78), nhưng token hợp lệ của user thường thì được chấp nhận: Đúng tình huống SEC-03 mô tả. Hệ quả: Bất kỳ người dùng đã đăng ký nào cũng tạo được mã giảm giá tùy ý cho mình, hoặc xóa mã của cửa hàng. Hành vi liên quan, không tính là bằng chứng của bug này vì dựa trên giả định A28 (`features/C_FR-17_QuanLyCoupon/05_final_tc.md` mục 1.5): Token user thường gọi `GET /api/coupons` nhận HTTP 200 và toàn bộ danh sách mã (TC-CPN-77); API spec mục 5.2 ghi API này "Dành cho Admin", còn FR-12 không nói về `GET`.

---

### BUG-FR17-02: API tạo được mã khi thiếu trường bắt buộc

- **Issue:** #61 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_61.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API thêm mã giảm giá: Tạo được mã khi thiếu trường bắt buộc hoặc body rỗng`
- **Labels:** `bug`, `severity: high`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-66 (6 dòng: Từng trường bắt buộc là `null` hoặc chuỗi rỗng), TC-CPN-70 (body `{}`), TC-CPN-65 dòng A (không có trường `type`), TC-CPN-143 dòng C (`code` chỉ gồm 3 dấu cách)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token admin

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/admin/coupons`, header `Authorization: Bearer <token admin>`, `Content-Type: application/json`, body `{}`.
2. Gửi tiếp body cơ sở nhưng `"code": null`.
3. Gửi tiếp body cơ sở với `"code": "FR17TC66C"`, `"discount_value": null`.
4. Gửi tiếp body cơ sở với `"code": "FR17TC65A"` và bỏ hẳn trường `type`.
5. Gửi tiếp body cơ sở với `"code": "   "` (3 dấu cách).
6. Gọi `GET /api/coupons` (token admin) để xem các mã vừa tạo.

**Dữ liệu test:** `{}`; `"code": null`; `"code": "␣␣␣"` (`␣` là một dấu cách); `"type": ""`; `"discount_value": null`; `"min_order_amount": null`; `"expired_at": ""`; `"max_uses_per_user": null`; không có trường `type`

**Kết quả mong đợi (theo đặc tả):** Từ chối, không tạo mã khi thiếu bất kỳ trường bắt buộc nào. README của EShop, FR-17:

> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).

**Kết quả thực tế:** Mọi request đều nhận HTTP 200 `{"message": "Coupon created", ...}`. Body `{}` tạo mã id 26 (số mã từ 24 thành 25). `GET /api/coupons` có các mã với `code` là `null` (id 14), `type` là `null` (id 11) hoặc `""` (id 15), `discount_value` là `null` (id 16), `min_order_amount` là `null` (id 17), `expired_at` là `""` (id 18); khi gửi `"max_uses_per_user": null`, mã được tạo với giá trị `1` (id 19). `code` chỉ gồm 3 dấu cách cũng tạo được mã (id 44, số mã từ 40 thành 41).

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-65_log.png`, `S6_TC-CPN-66_log_1.png`, `S6_TC-CPN-66_log_2.png`, `S6_TC-CPN-70_log.png`, `S6_TC-CPN-143_log_2.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, ô Mã coupon để trống bị trình duyệt chặn (TC-CPN-30 Pass); các ô bắt buộc khác chưa chạy qua giao diện. Mã chỉ gồm dấu cách không nhìn thấy trên bảng và không nhập được khi thanh toán, nên tương đương thiếu `code`. Các bug BUG-FR17-02, 03, 05, 06, 09 cho thấy API thêm mã không kiểm tra dữ liệu đầu vào. Related: #62, #63

---

### BUG-FR17-03: API nhận `type` không phải `percent` hoặc `fixed`

- **Issue:** #62 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_62.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API thêm mã giảm giá: Nhận type không phải percent hoặc fixed`
- **Labels:** `bug`, `severity: high`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-65 dòng B

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token admin

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/admin/coupons`, header `Authorization: Bearer <token admin>`, `Content-Type: application/json`, body cơ sở với `"code": "FR17TC65B"`, `"type": "free"`.
2. Gọi `GET /api/coupons` (token admin).

**Dữ liệu test:** `"type": "free"`

**Kết quả mong đợi (theo đặc tả):** Từ chối, không tạo mã vì `type` chỉ nhận `percent` hoặc `fixed`. README của EShop, FR-17:

> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).

**Kết quả thực tế:** HTTP 200 `{"message": "Coupon created", "id": 12}`; `GET /api/coupons` có mã `FR17TC65B` với `"type": "free"`.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-65_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** Trên giao diện, dropdown chỉ có 2 lựa chọn nên lỗi chỉ tái hiện qua API. Giá trị `PERCENT` (khác hoa thường, dòng C) cũng được nhận và lưu nguyên; đặc tả không nói rõ có phân biệt hoa thường không nên không tính vào bug này. Related: #61

---

### BUG-FR17-04: Giao diện tạo được mã giảm 0%

- **Issue:** #55 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_55.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] Form Tạo mã giảm giá: Tạo được mã có giá trị giảm 0%`
- **Labels:** `bug`, `severity: high`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-38

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; đăng nhập Web Admin bằng `admin@eshop.com`, mở menu "Mã Giảm Giá"

**Các bước tái hiện:**
1. Trên form "Tạo mã giảm giá mới", nhập Mã `FR17TC38`, chọn "Phần trăm (%)", Giá trị `0`, Đơn tối thiểu `300000`, ngày `12/31/2099`, Số lần dùng tối đa `3`.
2. Bấm "Tạo mã".

**Dữ liệu test:** Giá trị giảm `0` (loại phần trăm)

**Kết quả mong đợi (theo đặc tả):** Từ chối, không tạo mã vì `discount_value` phải dương. README của EShop, FR-17:

> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).

**Kết quả thực tế:** Mã `FR17TC38` được tạo, bảng hiện "Phần trăm", `0%`, `300,000 ₫`, `2099-12-31`, `3 lần`.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-38_1.png`, `S6_TC-CPN-38_2.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Mã giảm 0% không giảm được gì cho người mua. Lỗi tái hiện ngay trên giao diện, không cần công cụ ngoài. Related: #63

---

### BUG-FR17-05: API nhận giá trị không phải số ở các trường số

- **Issue:** #63 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_63.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API thêm mã giảm giá: Nhận giá trị không phải số ở discount_value, min_order_amount, max_uses_per_user`
- **Labels:** `bug`, `severity: high`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-67 (3 dòng)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token admin

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/admin/coupons` (token admin), body cơ sở với `"code": "FR17TC67A"`, `"discount_value": "abc"`.
2. Gửi tiếp body cơ sở với `"code": "FR17TC67B"`, `"min_order_amount": "abc"`.
3. Gửi tiếp body cơ sở với `"code": "FR17TC67C"`, `"max_uses_per_user": "abc"`.
4. Gọi `GET /api/coupons` (token admin).

**Dữ liệu test:** Chuỗi `"abc"` ở `discount_value`, `min_order_amount`, `max_uses_per_user`

**Kết quả mong đợi (theo đặc tả):** Từ chối, không tạo mã vì `discount_value` phải dương, `min_order_amount` phải >= 0, `max_uses_per_user` phải >= 1; chuỗi `"abc"` không thỏa điều kiện nào. README của EShop, FR-17:

> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).

**Kết quả thực tế:** Cả 3 request nhận HTTP 200 `Coupon created` (id 20, 21, 22); `GET /api/coupons` lưu nguyên chuỗi `"abc"` ở trường số tương ứng.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-67_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** Chưa chạy qua giao diện (các ô này là ô số). Related: #61, #55

---

### BUG-FR17-06: Số `9007199254740993` bị lưu thành `9007199254740992`

- **Issue:** #64 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_64.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API thêm mã giảm giá: Giá trị 9007199254740993 bị lưu thành 9007199254740992`
- **Labels:** `bug`, `severity: high`, `platform: admin`, `technique: BVA`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-131 (BVA, 3 dòng)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token admin

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/admin/coupons` (token admin), body cơ sở với `"code": "FR17TC131A"`, `"type": "fixed"`, `"discount_value": 9007199254740993`.
2. Gửi tiếp body cơ sở với `"code": "FR17TC131B"`, `"min_order_amount": 9007199254740993`.
3. Gửi tiếp body cơ sở với `"code": "FR17TC131C"`, `"max_uses_per_user": 9007199254740993`.
4. Gọi `GET /api/coupons` (token admin).

**Dữ liệu test:** `9007199254740993` (2^53 + 1) gửi dạng số JSON

**Kết quả mong đợi (theo đặc tả):** Mã được lưu đúng giá trị đã nhập; nếu giá trị vượt giới hạn của hệ thống thì bị từ chối với thông báo rõ, không được lưu thành giá trị khác. README của EShop, FR-17:

> - Admin có thể Thêm / Xem / Xóa mã giảm giá.
> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).

**Kết quả thực tế:** Cả 3 request nhận HTTP 200 `Coupon created` (id 33, 34, 35). `GET /api/coupons` trả `9007199254740992` ở cả 3 trường, khác giá trị đã gửi 1 đơn vị, không có thông báo nào.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-131_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** `9007199254740993` là số nguyên nhỏ nhất không biểu diễn chính xác được bằng số thực 64 bit. Đặc tả không nêu giới hạn trên của các trường này; giả định khi thiết kế (A03, A25 ở `features/C_FR-17_QuanLyCoupon/02_ec.md`) cho phép hệ thống từ chối số quá lớn, nhưng không cho phép lưu thành giá trị khác. Test case qua giao diện tương ứng (TC-CPN-111, 114, 119) chưa chạy.

---

### BUG-FR17-07: Request không phải JSON gây lỗi 500, lộ đường dẫn tệp trên máy chủ

- **Issue:** #65 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_65.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API thêm mã giảm giá: Request không phải JSON gây lỗi 500 và trả về đường dẫn tệp trên máy chủ`
- **Labels:** `bug`, `severity: medium`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-69 (4 dòng)

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token admin

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/admin/coupons` (token admin), body cơ sở với `"code": "FR17TC69B"`, **không** gửi header `Content-Type`.
2. Gửi lại với `"code": "FR17TC69C"` và header `Content-Type: text/plain`.
3. Gửi `POST` không có body.
4. Gửi body `{"code": "FR17TC69A",` (JSON sai cú pháp) với header `Content-Type: application/json`.

**Dữ liệu test:** Body JSON đúng nhưng thiếu hoặc sai `Content-Type`; không có body; JSON sai cú pháp

**Kết quả mong đợi (theo đặc tả):** Request không gửi đúng dạng JSON bị từ chối như lỗi phía người gọi, không gây lỗi máy chủ và không trả về chi tiết bên trong máy chủ. API spec của EShop, mục 6.4:

> - **Thêm mới mã:** `POST /api/admin/coupons`
>   - **Body (JSON):**

**Kết quả thực tế:** Bước 1, 2, 3: HTTP 500, body là trang HTML lỗi `TypeError: Cannot destructure property 'code' of 'req.body' as it is undefined.` kèm stack trace có đường dẫn tệp trên máy chủ (`...\eshop-sut\backend\server.js:459:5`, `node_modules\router\...`). Bước 4: HTTP 400, body là trang HTML lỗi `SyntaxError: Expected double-quoted property name in JSON at position 21` cũng kèm đường dẫn tệp. Không request nào tạo mã.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-69_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** Đặc tả không nêu mã HTTP khi request sai; mong đợi "4xx, không 5xx" là giả định A20, A23 ở `features/C_FR-17_QuanLyCoupon/02_ec.md`. Rủi ro lộ thông tin máy chủ: Ở cả lỗi 400 lẫn 500, body trả về stack trace với thư mục cài đặt, tên tệp, số dòng và thư viện đang dùng (`body-parser`, `router`); các thông tin này giúp kẻ tấn công biết cấu trúc máy chủ để dò các lỗ hổng khác. Lần chạy này chỉ gửi request có token admin; chưa kiểm request không có token có trả về cùng thông tin không.

---

### BUG-FR17-08: Giao diện tạo được mã giảm 150%

- **Issue:** #56 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_56.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] Form Tạo mã giảm giá: Tạo được mã loại phần trăm có giá trị giảm 150%`
- **Labels:** `bug`, `severity: medium`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-37

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; đăng nhập Web Admin bằng `admin@eshop.com`, mở menu "Mã Giảm Giá"

**Các bước tái hiện:**
1. Trên form "Tạo mã giảm giá mới", nhập Mã `FR17TC37`, chọn "Phần trăm (%)", Giá trị `150`, Đơn tối thiểu `300000`, ngày `12/31/2099`, Số lần dùng tối đa `3`.
2. Bấm "Tạo mã".

**Dữ liệu test:** Giá trị giảm `150` (loại phần trăm)

**Kết quả mong đợi (theo đặc tả):** Từ chối, không tạo mã loại phần trăm có giá trị lớn hơn 100, vì theo công thức áp mã, giá trị đó làm số tiền phải trả bị âm. README của EShop, FR-17 và FR-09:

> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).
>
> - Loại `percent`: `discount_amount = total × discount_value / 100`
> - `final_amount = total - discount_amount`

**Kết quả thực tế:** Mã `FR17TC37` được tạo, bảng hiện "Phần trăm", `150%`, `300,000 ₫`, `2099-12-31`, `3 lần`.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-37_1.png`, `S6_TC-CPN-37_2.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** FR-17 chỉ ghi `discount_value` dương, không ghi trực tiếp giới hạn 100%; mong đợi được suy ra từ công thức của FR-09 (giả định A01 ở `features/C_FR-17_QuanLyCoupon/02_ec.md`). Theo công thức đó, đơn 300.000 ₫ dùng mã này có `discount_amount` 450.000 ₫ và `final_amount` -150.000 ₫; việc áp mã ở FR-09 chưa được kiểm.

---

### BUG-FR17-09: API lưu `expired_at` không phải ngày hợp lệ

- **Issue:** #66 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_66.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] API thêm mã giảm giá: Lưu expired_at sai định dạng hoặc không phải ngày có thật`
- **Labels:** `bug`, `severity: medium`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-68 (3 dòng)

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token admin

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/admin/coupons` (token admin), body cơ sở với `"code": "FR17TC68A"`, `"expired_at": "12/31/2027"`.
2. Gửi tiếp body cơ sở với `"code": "FR17TC68B"`, `"expired_at": "2027-02-30"`.
3. Gửi tiếp body cơ sở với `"code": "FR17TC68C"`, `"expired_at": "2027-12-31T10:00:00Z"`.
4. Gọi `GET /api/coupons` (token admin).

**Dữ liệu test:** `"12/31/2027"` (khác dạng `yyyy-mm-dd`); `"2027-02-30"` (không phải ngày có thật); `"2027-12-31T10:00:00Z"` (có kèm giờ)

**Kết quả mong đợi (theo đặc tả):** Từ chối, không tạo mã khi `expired_at` không phải ngày hợp lệ dạng `yyyy-mm-dd`, vì `expired_at` là ngày dùng để so với ngày hiện tại khi áp mã. README của EShop (FR-17, FR-09) và API spec mục 6.4:

> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).
>
> | #   | Điều kiện              | Mô tả                                                       |
> | --- | ---------------------- | ----------------------------------------------------------- |
> | C2  | **Còn hạn sử dụng**    | Ngày hiện tại phải trước `expired_at`                       |
>
> `"expired_at": "2025-01-31",`

**Kết quả thực tế:** Cả 3 request nhận HTTP 200 `Coupon created` (id 23, 24, 25); `GET /api/coupons` lưu nguyên `"12/31/2027"`, `"2027-02-30"`, `"2027-12-31T10:00:00Z"`.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-68_log.png` (ảnh chụp đoạn log); log đầy đủ: `features/C_FR-17_QuanLyCoupon/logs/S6_api_20261021_003400.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py`)

**Ghi chú:** `2027-02-30` không phải ngày có thật theo bất kỳ định dạng nào. Dạng `yyyy-mm-dd` lấy theo ví dụ của API spec mục 6.4 (giả định A13 ở `features/C_FR-17_QuanLyCoupon/02_ec.md`). Ảnh hưởng tới điều kiện C2 khi áp mã ở FR-09 chưa được kiểm. Qua giao diện, ô chọn ngày chỉ cho chọn ngày có thật nên lỗi chỉ tái hiện qua API. Related: #61

---

### BUG-FR17-10: Có chữ không phải tiếng Việt trên trang Quản lý Mã Giảm Giá

- **Issue:** #57 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_57.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] Trang Quản lý Mã Giảm Giá: Tiêu đề tab, menu, thông báo lỗi và lịch chọn ngày không phải tiếng Việt`
- **Labels:** `bug`, `severity: low`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-91, TC-CPN-32

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web Admin bằng `admin@eshop.com`, mở menu "Mã Giảm Giá"

**Các bước tái hiện:**
1. Quan sát tiêu đề tab của trình duyệt và menu bên trái.
2. Để trống ô Mã coupon, nhập các ô còn lại ("Phần trăm (%)", `15`, `300000`, `12/31/2099`, `3`), bấm "Tạo mã".
3. Nhập Mã `SAVE10` (trùng mã mẫu), các ô còn lại như bước 2, bấm "Tạo mã".
4. Bấm biểu tượng lịch ở ô ngày hết hạn.

**Dữ liệu test:** Mã để trống; Mã `SAVE10`

**Kết quả mong đợi (theo đặc tả):** Toàn bộ giao diện dùng tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn. README của EShop, FR-21:

> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).

**Kết quả thực tế:** (1) Tiêu đề tab là `frontend-admin`; menu có mục "Dashboard". (2) Bong bóng "Please fill out this field." (3) Hộp thoại "Lỗi: SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code": Chuỗi lỗi kỹ thuật của CSDL bằng tiếng Anh, chỉ có tiền tố "Lỗi:". (4) Lịch hiện "October 2026", "Su" đến "Sa", "Clear", "Today"; ô ngày hiện `mm/dd/yyyy`. Các tiêu đề, cột, nút, placeholder còn lại là tiếng Việt.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-91.png` (tiêu đề tab, menu), `S6_TC-CPN-30.png` (bong bóng), `S6_TC-CPN-32.png` (thông báo trùng mã), `S0_06_chon_ngay_expired.png` (lịch)

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85 (giao diện trình duyệt tiếng Anh), EShop commit `85af3ba`

**Ghi chú:** Bong bóng và lịch là thành phần của trình duyệt, hiện theo ngôn ngữ của trình duyệt; được tính vào lỗi vì người dùng thấy chúng trên trang và trang không cung cấp chữ tiếng Việt thay thế. Thông báo ở bước 3 còn lộ tên hệ CSDL, tên bảng và cột (`SQLITE`, `coupons.code`). Related: #54 (FR-01, BUG-FR01-13)

---

### BUG-FR17-11: Nút "Tạo mã" màu cam thay vì xanh dương

- **Issue:** #58 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_58.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] Form Tạo mã giảm giá: Nút "Tạo mã" màu cam thay vì xanh dương`
- **Labels:** `bug`, `severity: low`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-92

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web Admin bằng `admin@eshop.com`, mở menu "Mã Giảm Giá"

**Các bước tái hiện:**
1. Quan sát màu nút "Tạo mã" dưới form "Tạo mã giảm giá mới".

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Nút hành động tích cực (Submit) màu xanh dương. README của EShop, FR-21:

> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.

**Kết quả thực tế:** Nút "Tạo mã" (nút submit của form) nền cam, chữ trắng.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-91.png`, `S0_07_nut_thao_tac_tao_ma.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Nút "Xóa" ở cột "Hành động" màu đỏ, đạt yêu cầu tương ứng. Related: #52 (FR-01, BUG-FR01-11)

---

### BUG-FR17-12: Trường bắt buộc không có dấu `*`

- **Issue:** #59 (ảnh trang issue: `features/C_FR-17_QuanLyCoupon/screenshots/S7_issue_59.png`)
- **Tiêu đề:** `[23120061][FR-17][Admin] Form Tạo mã giảm giá: Trường bắt buộc không có dấu *`
- **Labels:** `bug`, `severity: low`, `platform: admin`, `technique: EP`, `pool: C`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-17: Quản lý mã giảm giá

**Nền tảng:** Web Admin

**Test case phát hiện lỗi:** TC-CPN-90

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập Web Admin bằng `admin@eshop.com`, mở menu "Mã Giảm Giá"

**Các bước tái hiện:**
1. Quan sát 6 ô của form "Tạo mã giảm giá mới".

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Mọi trường bắt buộc có dấu `*` bên cạnh nhãn. README của EShop, FR-22 (6 trường của form là bắt buộc theo FR-17):

> - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.

**Kết quả thực tế:** Form không có nhãn, chỉ có placeholder ("Mã coupon (VD: SAVE10)", "Giá trị % (VD: 10)", "Đơn tối thiểu (₫)", "Số lần dùng tối đa/người"...); không ô nào có dấu `*`.

**Ảnh chụp:** `features/C_FR-17_QuanLyCoupon/screenshots/S6_TC-CPN-91.png`, `S0_04_form_them_coupon_khong_noi_dung.png`

**Môi trường:** Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba`

**Ghi chú:** Related: #51 (FR-01, BUG-FR01-10)

---

### Khác giả định và quan sát: Quyết định của sinh viên

Cột "Đề xuất" là của AI; cột "Quyết định" là của sinh viên.

| Mã | Nguồn | Hành vi quan sát | Đề xuất | Lý do | Quyết định |
|---|---|---|---|---|---|
| KG01 | TC-CPN-37 (A01) | Giá trị giảm `150%` tạo được qua giao diện | Thành bug riêng, Medium | FR-17 chỉ ghi "dương", nhưng theo công thức FR-09 (`discount_amount = total × discount_value / 100`), giảm hơn 100% làm `final_amount` âm; ghi rõ mong đợi là suy ra từ FR-09 | Thành bug riêng, Medium: BUG-FR17-08 |
| KG02 | TC-CPN-68 (A13) | API lưu nguyên `"12/31/2027"`, `"2027-02-30"`, `"2027-12-31T10:00:00Z"` làm `expired_at` | Thành bug riêng, Medium, gộp 3 dòng | `2027-02-30` không phải ngày có thật; một chuỗi không phải ngày không dùng được cho điều kiện C2 của FR-09 ("Ngày hiện tại phải trước `expired_at`"). Định dạng `yyyy-mm-dd` lấy theo ví dụ API spec | Thành bug riêng, Medium: BUG-FR17-09 |
| KG03 | TC-CPN-77 (A28) | Token user thường gọi `GET /api/coupons` nhận HTTP 200 và toàn bộ danh sách mã | Thành bug, gộp vào BUG-FR17-01 | Cùng nguyên nhân (không kiểm tra `role`); căn cứ là nhãn "(Dành cho Admin)" ở API spec mục 5.2, ghi rõ trong ghi chú vì FR-12 không nói về `GET` | Không gộp làm bằng chứng của BUG-FR17-01; chỉ ghi trong Ghi chú của BUG-FR17-01 là hành vi liên quan, dựa trên giả định A28 |
| KG04 | TC-CPN-140, TC-CPN-141 (A04) | Mã chỉ khác hoa thường cùng tồn tại (`fr17tc140` và `FR17TC140`; `save10` và `SAVE10`) | Không thành bug | Đặc tả không nói so trùng có phân biệt hoa thường không; ghi lại cho S8 | Theo đề xuất: Không thành bug |
| KG05 | TC-CPN-143 (A09) | Dấu cách đầu cuối được lưu nguyên; `␣SAVE10` tồn tại cùng `SAVE10`; mã chỉ gồm 3 dấu cách tạo được (`␣` là một dấu cách) | Dòng C (chỉ dấu cách) gộp vào BUG-FR17-02; dòng A, B, D không thành bug | Mã chỉ gồm dấu cách không nhìn thấy và không nhập được khi thanh toán, tương đương thiếu `code`; việc cắt dấu cách đầu cuối là giả định A09, đặc tả không nói | Theo đề xuất: Dòng C gộp vào BUG-FR17-02; dòng A, B, D không thành bug |
| QS01 | Mục 6: Placeholder ô "Giá trị" | Đổi theo loại ("Giá trị % (VD: 10)", "Số tiền (VD: 50000)") | Không thành bug | Hành vi hợp lý, không trái đặc tả | Theo đề xuất: Không thành bug |
| QS02 | Mục 6: Tải lại trang | F5 ở bất kỳ trang nào của Web Admin đều về Dashboard; URL luôn là `localhost:5174` | Không thành bug của FR-17 | Đặc tả không yêu cầu; thuộc điều hướng chung của Web Admin, không phải FR được phân công | Theo đề xuất: Không thành bug của FR-17 |
| QS03 | Mục 6: Trang đăng nhập admin | "Admin Login", "Password", "Login" bằng tiếng Anh | Không báo trong FR-17 | Ngoài phạm vi FR-17 (trang đăng nhập admin); nếu nhóm muốn báo thì thuộc FR-21 ở trang đó | Theo đề xuất: Không báo trong FR-17 |

### Test case Blocked và bug gây chặn

Không có test case Blocked trong lần chạy này.

---

## FR-04: Quản lý hồ sơ cá nhân

- Nguồn: `features/D_FR-04_HoSo_Mobile/06_results.md` (kết quả chạy ngày 21/10/2026, S6 rút gọn), bộ test case ở `features/D_FR-04_HoSo_Mobile/05_final_tc.md`
- Môi trường chung: Samsung Galaxy S21 Ultra (Android 15); ứng dụng EShop chạy bằng Expo Go 54.0.8; EShop commit `85af3ba`; backend `http://localhost:3000`, điện thoại truy cập qua `adb reverse`; API gọi bằng script Python trên Windows 11
- Điều kiện tiên quyết chung: Đã reset dữ liệu EShop về dữ liệu mẫu. Giao diện: Đăng nhập ứng dụng bằng `test@eshop.com` / `Test1234!`, bấm "Chào, Test User" để mở màn "Hồ sơ của bạn". API: Lấy token bằng `POST /api/login`
- Body cơ sở khi gọi `PUT /api/users/me`: `{"name": "Nguyen Van An <số test case>", "phone": "0912345678", "shipping_address": "12/3 Lê Lợi, Quận 1, TP.HCM"}`. Trạng thái hồ sơ trước mỗi test case (`S_CHUAN`): Họ Tên `Test User`, Số điện thoại `0900000000`, Địa chỉ `1 Nguyen Hue, Quận 1`

### Tổng hợp

| Bug | Tiêu đề ngắn | Severity | Technique | Test case | Issue |
|---|---|---|---|---|---|
| BUG-FR04-01 | Người dùng tự đổi `role` thành `admin` qua API cập nhật hồ sơ | Critical | EP | TC-PROF-77 | #85 |
| BUG-FR04-02 | Ứng dụng từ chối Số điện thoại hợp lệ 10 và 11 chữ số | High | EP, BVA | TC-PROF-01, TC-PROF-101 | #86 |
| BUG-FR04-03 | API lưu Số điện thoại không hợp lệ | Medium | EP, BVA | TC-PROF-74, TC-PROF-75, TC-PROF-71 | #87 |
| BUG-FR04-04 | Màn Hồ sơ không hiển thị Địa chỉ giao hàng đã lưu | Medium | EP | TC-PROF-04 (quan sát QS03) | #88 |
| BUG-FR04-05 | Thanh trên không làm nổi mục đang chọn khi ở màn Hồ sơ | Low | EP | TC-PROF-90 (điểm 5) | #89 |

Label chung cho mọi bug của FR-04: `bug` (template tự gắn), `platform: mobile`, `pool: D`. Label `severity` và `technique` theo bảng trên. BUG-FR04-04 lấy từ quan sát QS03, sinh viên đã duyệt (bảng "Khác giả định và quan sát" cuối mục).

---

### BUG-FR04-01: Người dùng tự đổi `role` thành `admin` qua API cập nhật hồ sơ

- **Issue:** #85 (ảnh trang issue: `features/D_FR-04_HoSo_Mobile/screenshots/S7_issue_85.png`)
- **Tiêu đề:** `[23120061][FR-04][Mobile] API cập nhật hồ sơ: Người dùng tự đổi role thành admin`
- **Labels:** `bug`, `severity: critical`, `platform: mobile`, `technique: EP`, `pool: D`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-04: Quản lý hồ sơ cá nhân

**Nền tảng:** Mobile

**Test case phát hiện lỗi:** TC-PROF-77

**Mức độ:** Critical

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`

**Các bước tái hiện:**
1. Gửi `POST http://localhost:3000/api/login`, body `{"email": "test@eshop.com", "password": "Test1234!"}`; lấy `token` (tài khoản user thường).
2. Gửi `GET http://localhost:3000/api/users/me`, header `Authorization: Bearer <token>`; ghi giá trị `role`.
3. Gửi `PUT http://localhost:3000/api/users/me`, header `Authorization: Bearer <token>`, `Content-Type: application/json`, body `{"name": "Nguyen Van An 77", "phone": "0912345678", "shipping_address": "12/3 Lê Lợi, Quận 1, TP.HCM", "role": "admin"}`.
4. Gửi lại `GET http://localhost:3000/api/users/me` với cùng token.

**Dữ liệu test:** Token của `test@eshop.com`; trường `"role": "admin"` trong body

**Kết quả mong đợi (theo đặc tả):** `role` vẫn là `user` sau bước 4; yêu cầu có thể bị từ chối hoặc được chấp nhận nhưng bỏ qua `role`. README của EShop, FR-04 và mục 9:

> - Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`.
>
> SEC-06: API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client.

**Kết quả thực tế:** Bước 2: `"role": "user"`. Bước 3: HTTP 200 `{"message": "Profile updated"}`. Bước 4: `"role": "admin"` (cùng `id` 2, `email` `test@eshop.com`).

**Ảnh chụp:** `features/D_FR-04_HoSo_Mobile/screenshots/S6_TC-PROF-77_log.png` (ảnh cần chụp: S6_TC-PROF-77_log.png); log đầy đủ: `features/D_FR-04_HoSo_Mobile/logs/S6_last_20261021_090658.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/D_FR-04_HoSo_Mobile/scripts/run_api_tests.py`)

**Ghi chú:** Hệ quả: Bất kỳ người dùng đã đăng ký nào cũng tự nâng mình thành `admin`. Sau test case này, tài khoản `test@eshop.com` giữ `role` `admin` cho tới khi reset dữ liệu (đã reset lúc 09:07 21/10/2026). Hai trường được bảo vệ khác được xử lý đúng: `email` gửi trong body bị bỏ qua (TC-PROF-76), `id` của người khác bị bỏ qua (TC-PROF-80). Chưa kiểm token đăng nhập lại sau khi đổi `role` có gọi được API Admin không

---

### BUG-FR04-02: Ứng dụng từ chối Số điện thoại hợp lệ 10 và 11 chữ số

- **Issue:** #86 (ảnh trang issue: `features/D_FR-04_HoSo_Mobile/screenshots/S7_issue_86.png`)
- **Tiêu đề:** `[23120061][FR-04][Mobile] Màn Hồ sơ: Từ chối Số điện thoại hợp lệ 10 và 11 chữ số bắt đầu bằng 0`
- **Labels:** `bug`, `severity: high`, `platform: mobile`, `technique: EP`, `technique: BVA`, `pool: D`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-04: Quản lý hồ sơ cá nhân

**Nền tảng:** Mobile

**Test case phát hiện lỗi:** TC-PROF-01 (10 chữ số, EP), TC-PROF-101 (11 chữ số, BVA cận trên)

**Mức độ:** High

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; đăng nhập ứng dụng bằng `test@eshop.com`; mở màn "Hồ sơ của bạn" bằng cách bấm "Chào, Test User"

**Các bước tái hiện:**
1. Nhập Họ Tên `Nguyen Van An 01`, Số điện thoại `0912345678`, Địa chỉ giao hàng `12/3 Lê Lợi, Quận 1, TP.HCM`.
2. Ẩn bàn phím, bấm "Cập nhật".
3. Bấm "OK", đổi Họ Tên thành `Nguyen Van An 101`, Số điện thoại thành `09123453789` (11 chữ số), bấm "Cập nhật".
4. Gửi `GET http://localhost:3000/api/users/me` bằng token của `test@eshop.com` để xem hồ sơ đã lưu.

**Dữ liệu test:** `0912345678` (10 chữ số), `09123453789` (11 chữ số); cả hai bắt đầu bằng `0`

**Kết quả mong đợi (theo đặc tả):** Cả hai số hợp lệ, hồ sơ được cập nhật. README của EShop, FR-04:

> - Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
> - **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.

**Kết quả thực tế:** Ở bước 2 và bước 3, ứng dụng hiện hộp thoại "Lỗi" với nội dung "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."; hồ sơ không đổi (bước 4 trả Họ Tên `Test User`, Số điện thoại `0900000000`).

**Ảnh chụp:** `features/D_FR-04_HoSo_Mobile/screenshots/S6_TC-PROF-01_1.png`, `S6_TC-PROF-01_2.png`, `S6_TC-PROF-101_1.png`, `S6_TC-PROF-101_2.png`

**Môi trường:** Samsung Galaxy S21 Ultra (Android 15), Expo Go 54.0.8, EShop commit `85af3ba`

**Ghi chú:** Cùng hai giá trị gửi qua API thì được lưu (`0912345678` ở TC-PROF-70, `09123456789` ở TC-PROF-102), nên lỗi nằm ở kiểm tra của ứng dụng. Thông báo nêu quy tắc "9-10 chữ số", khác đặc tả "10–11 chữ số", và số 9 chữ số `091234567` cũng bị từ chối với cùng thông báo (TC-PROF-33). Số `1912345678` (không bắt đầu bằng `0`) qua được kiểm tra này nhưng nhận "Lỗi cập nhật" và không được lưu (TC-PROF-32), dù API lưu được số đó; vì vậy trong lần chạy này chưa có cách nào lưu Số điện thoại qua ứng dụng. Lỗi này chặn TC-PROF-04 và TC-PROF-30. Số 11 chữ số đã gõ là `09123453789` (khác kế hoạch `09123456789` một chữ số, vẫn 11 chữ số bắt đầu bằng `0`)

---

### BUG-FR04-03: API lưu Số điện thoại không hợp lệ

- **Issue:** #87 (ảnh trang issue: `features/D_FR-04_HoSo_Mobile/screenshots/S7_issue_87.png`)
- **Tiêu đề:** `[23120061][FR-04][Mobile] API cập nhật hồ sơ: Lưu Số điện thoại không bắt đầu bằng 0, ít hơn 10 chữ số hoặc có dấu cách`
- **Labels:** `bug`, `severity: medium`, `platform: mobile`, `technique: EP`, `technique: BVA`, `pool: D`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-04: Quản lý hồ sơ cá nhân

**Nền tảng:** Mobile

**Test case phát hiện lỗi:** TC-PROF-74 (không bắt đầu bằng `0`, EP), TC-PROF-75 (9 chữ số, BVA LB-1), TC-PROF-71 (có dấu cách ở đầu và cuối, EP)

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; backend chạy ở `http://localhost:3000`; có token của `test@eshop.com`

**Các bước tái hiện:**
1. Gửi `PUT http://localhost:3000/api/users/me`, header `Authorization: Bearer <token>`, `Content-Type: application/json`, body cơ sở với `"phone": "1912345678"`; rồi `GET /api/users/me`.
2. Lặp lại với `"phone": "091234567"`.
3. Lặp lại với `"phone": " 0912345678 "` (một dấu cách ở đầu và ở cuối).

**Dữ liệu test:** `1912345678` (10 chữ số, bắt đầu bằng `1`); `091234567` (9 chữ số); `␣0912345678␣` (`␣` là một dấu cách)

**Kết quả mong đợi (theo đặc tả):** Hệ thống không lưu các số này. README của EShop, FR-04:

> - **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.

**Kết quả thực tế:** Cả ba yêu cầu nhận HTTP 200 `{"message": "Profile updated"}`; `GET /api/users/me` trả `phone` đúng như đã gửi: `1912345678`, `091234567`, `␣0912345678␣` (giữ nguyên dấu cách).

**Ảnh chụp:** `features/D_FR-04_HoSo_Mobile/screenshots/S6_TC-PROF-74_log.png`, `S6_TC-PROF-75_log.png`, `S6_TC-PROF-71_log.png` (ảnh cần chụp: S6_TC-PROF-74_log.png, S6_TC-PROF-75_log.png, S6_TC-PROF-71_log.png); log đầy đủ: `features/D_FR-04_HoSo_Mobile/logs/S6_run_20261021_090657.log`

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/D_FR-04_HoSo_Mobile/scripts/run_api_tests.py`)

**Ghi chú:** Ứng dụng lại từ chối cả số hợp lệ (BUG-FR04-02), nên kiểm tra Số điện thoại ở ứng dụng và ở hệ thống đều không khớp đặc tả. Hành vi liên quan, không tính là bằng chứng của bug này vì dựa trên giả định A06 (`features/D_FR-04_HoSo_Mobile/02_ec.md`): `"0912-345678"` cũng được lưu nguyên văn (TC-PROF-73)

---

### BUG-FR04-04: Màn Hồ sơ không hiển thị Địa chỉ giao hàng đã lưu

- **Issue:** #88 (ảnh trang issue: `features/D_FR-04_HoSo_Mobile/screenshots/S7_issue_88.png`)
- **Tiêu đề:** `[23120061][FR-04][Mobile] Màn Hồ sơ: Ô Địa chỉ giao hàng trống dù hồ sơ đang có địa chỉ`
- **Labels:** `bug`, `severity: medium`, `platform: mobile`, `technique: EP`, `pool: D`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-04: Quản lý hồ sơ cá nhân

**Nền tảng:** Mobile

**Test case phát hiện lỗi:** TC-PROF-04 (quan sát QS03 trong `features/D_FR-04_HoSo_Mobile/06_results.md`)

**Mức độ:** Medium

**Điều kiện tiên quyết:** Đã reset dữ liệu EShop về dữ liệu mẫu; đăng nhập ứng dụng bằng `test@eshop.com`

**Các bước tái hiện:**
1. Gửi `PUT http://localhost:3000/api/users/me` (token của `test@eshop.com`), body `{"name": "Test User", "phone": "0900000000", "shipping_address": "1 Nguyen Hue, Quận 1"}`; gửi `GET /api/users/me` để xác nhận địa chỉ đã lưu.
2. Trên ứng dụng, rời màn Hồ sơ rồi bấm "Chào, Test User" để mở lại.
3. Quan sát ô "Địa chỉ giao hàng".

**Dữ liệu test:** Địa chỉ đã lưu `1 Nguyen Hue, Quận 1`

**Kết quả mong đợi (theo đặc tả):** Ô "Địa chỉ giao hàng" hiển thị địa chỉ đang lưu để người dùng cập nhật. Mong đợi suy ra từ README của EShop, FR-04 (đặc tả không nói trực tiếp về việc hiển thị giá trị hiện tại):

> - Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.

**Kết quả thực tế:** Ô "Địa chỉ giao hàng" trống, trong khi `GET /api/users/me` (08:47:03) trả `"shipping_address": "1 Nguyen Hue, Quận 1"`. Ô Email hiển thị đúng `test@eshop.com`.

**Ảnh chụp:** `features/D_FR-04_HoSo_Mobile/screenshots/S6_TC-PROF-04_2.png`; log: `features/D_FR-04_HoSo_Mobile/logs/S6_chuan_TC-PROF-04_20261021_084703.log`

**Môi trường:** Samsung Galaxy S21 Ultra (Android 15), Expo Go 54.0.8, EShop commit `85af3ba`

**Ghi chú:** Ô Địa chỉ cũng trống ở `S6_TC-PROF-101_1.png` và `S6_TC-PROF-34_1.png` trong cùng đợt chạy. Chưa kiểm ô Số điện thoại có hiển thị giá trị đã lưu không (các ảnh chụp sau khi đã gõ số mới). Nếu bấm "Cập nhật" khi ô trống, địa chỉ đang lưu có thể bị ghi đè bằng chuỗi rỗng; chưa kiểm được vì BUG-FR04-02 chặn mọi lần lưu qua ứng dụng

---

### BUG-FR04-05: Thanh trên không làm nổi mục đang chọn khi ở màn Hồ sơ

- **Issue:** #89 (ảnh trang issue: `features/D_FR-04_HoSo_Mobile/screenshots/S7_issue_89.png`)
- **Tiêu đề:** `[23120061][FR-04][Mobile] Màn Hồ sơ: Thanh điều hướng không highlight mục "Chào, Test User" đang được chọn`
- **Labels:** `bug`, `severity: low`, `platform: mobile`, `technique: EP`, `pool: D`

**MSSV người báo:** 23120061

**Feature (mã FR):** FR-04: Quản lý hồ sơ cá nhân

**Nền tảng:** Mobile

**Test case phát hiện lỗi:** TC-PROF-90 (điểm 5)

**Mức độ:** Low

**Điều kiện tiên quyết:** Đăng nhập ứng dụng bằng `test@eshop.com`

**Các bước tái hiện:**
1. Ở màn "Danh sách sản phẩm", quan sát thanh trên ("EShop Mobile", "Chào, Test User", "Giỏ (0)").
2. Bấm "Chào, Test User" để mở màn "Hồ sơ của bạn".
3. Quan sát lại thanh trên.

**Dữ liệu test:** Không cần nhập

**Kết quả mong đợi (theo đặc tả):** Ở màn Hồ sơ, mục "Chào, Test User" trên thanh điều hướng được làm nổi. README của EShop, FR-23:

> - Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.

**Kết quả thực tế:** Thanh trên giống hệt ở hai màn: "Chào, Test User" vẫn là chữ trắng, không gạch chân, không có nền riêng.

**Ảnh chụp:** `features/D_FR-04_HoSo_Mobile/screenshots/S0_01_sau_dang_nhap.png`, `S0_02_ho_so.png`

**Môi trường:** Samsung Galaxy S21 Ultra (Android 15), Expo Go 54.0.8, EShop commit `85af3ba`

**Ghi chú:** Ứng dụng không có thanh tab; thanh trên được coi là thanh điều hướng theo FR-23 (quyết định của sinh viên ở `features/D_FR-04_HoSo_Mobile/01_io.md` mục 8 điểm 9). Ảnh chụp ở bước khảo sát S0 cùng ngày, cùng commit; điểm kiểm này của TC-PROF-90 được điền từ hai ảnh đó

---

### Khác giả định và quan sát: Quyết định của sinh viên

Cột "Đề xuất" là của AI; cột "Quyết định" là của sinh viên.

| Mã | Nguồn | Hành vi quan sát | Đề xuất | Lý do | Quyết định |
|---|---|---|---|---|---|
| KG01 | TC-PROF-72 (A16) | Body `PUT` chỉ có `name` làm `phone` và `shipping_address` thành `null` | Không thành bug | Đặc tả không nói về body thiếu trường; theo RFC 9110, `PUT` thay toàn bộ tài nguyên nên xóa trường không gửi là hành vi chuẩn; ví dụ ở API spec gửi đủ 3 trường | Theo đề xuất: Không thành bug |
| KG02 | TC-PROF-73 (A06) | API lưu nguyên `0912-345678` | Không thành bug riêng; ghi trong Ghi chú của BUG-FR04-03 là hành vi liên quan | Số vẫn đủ 10 chữ số và bắt đầu bằng `0`; việc coi dấu `-` là không hợp lệ là giả định A06 | Theo đề xuất: Không thành bug riêng; ghi trong Ghi chú của BUG-FR04-03 |
| KG03 | TC-PROF-90 điểm 4 (A01) | Không ô nào có dấu `*` | Không thành bug | FR-04 không nói Họ Tên bắt buộc; Họ Tên bắt buộc là giả định A01, và TC-PROF-30 Blocked nên chưa biết ứng dụng có coi Họ Tên là bắt buộc không | Theo đề xuất: Không thành bug |
| QS01 | Mục 6: Thông báo "đúng 9-10 chữ số" | Thông báo nêu quy tắc khác đặc tả; số 9 chữ số vẫn bị từ chối | Gộp vào BUG-FR04-02 (đã ghi trong Kết quả thực tế và Ghi chú) | Cùng chỗ kiểm tra Số điện thoại sai của ứng dụng | Theo đề xuất: Gộp vào BUG-FR04-02 |
| QS02 | Mục 6: Phản hồi API có trường `password` | `POST /api/login`, `GET /api/users/me` trả `password` (script đã che giá trị), `reset_token`, `login_attempts`, `locked_until` | Không báo trong FR-04; ghi cho S8 | Chưa thấy giá trị (không biết là văn bản rõ hay đã băm); FR-04 không yêu cầu về các trường này; nếu nhóm muốn báo thì thuộc SEC-01 hoặc FR-19 | Theo đề xuất: Không báo trong FR-04; ghi cho S8 |
| QS03 | Mục 6: Ô Địa chỉ trống dù đã lưu | Màn Hồ sơ không hiển thị địa chỉ đang lưu (sinh viên xác nhận) | Thành bug riêng, Medium: BUG-FR04-04 | Người dùng không thấy địa chỉ hiện tại để cập nhật; có nguy cơ ghi đè bằng chuỗi rỗng | Theo đề xuất: Thành bug riêng, Medium: BUG-FR04-04 |
| QS04 | Mục 6: "Lỗi cập nhật" với `1912345678` | Qua ứng dụng không lưu, qua API lưu được | Không thành bug riêng; ghi trong Ghi chú của BUG-FR04-02 | Kết quả của TC-PROF-32 đúng mong đợi (số không hợp lệ không được lưu); nguyên nhân thất bại không quan sát được | Theo đề xuất: Không thành bug riêng; ghi trong Ghi chú của BUG-FR04-02 |

### Test case Blocked và bug gây chặn

| Test case | Lý do Blocked | Bug gây chặn |
|---|---|---|
| TC-PROF-04 | Số điện thoại cơ sở `0912345678` bị ứng dụng từ chối, không kiểm được việc lưu và hiển thị Họ Tên có thẻ HTML | BUG-FR04-02 (#86) |
| TC-PROF-30 | Thông báo là về Số điện thoại cơ sở, không biết ứng dụng có từ chối Họ Tên rỗng không | BUG-FR04-02 (#86) |
