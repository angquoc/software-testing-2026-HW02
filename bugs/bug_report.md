# Bug report HW02: Domain Testing trên EShop

- Sinh viên: Nguyễn Thị Ánh Ngọc, MSSV 23120061
- SUT: EShop, commit `85af3ba`
- Repo nhóm (GitHub Issues): https://github.com/angquoc/software-testing-2026-HW02-group

Mỗi bug dưới đây là nội dung để dán vào issue GitHub theo template **Bug report**, theo quy ước ở mục 4 README của repo nhóm. Sau khi tạo issue, ghi số issue vào bảng tổng hợp của feature và vào dòng "Issue" của bug. Đường dẫn ảnh và log tính từ thư mục `Homeworks/HW02/`.

## Mục lục

| Feature | Pool | Nền tảng | Mục |
|---|---|---|---|
| FR-01 Đăng ký tài khoản | A | Web | [FR-01](#fr-01-đăng-ký-tài-khoản) |
| FR-07 Giỏ hàng | B | Web | (bổ sung sau) |
| FR-17 Quản lý mã giảm giá | C | Web Admin | (bổ sung sau) |
| FR-04 Quản lý hồ sơ cá nhân | D | Mobile | (bổ sung sau) |

---

## FR-01: Đăng ký tài khoản

- Nguồn: `features/A_FR-01_DangKy/06_results.md` (kết quả chạy ngày 20/10/2026), bộ test case ở `features/A_FR-01_DangKy/05_final_tc.md`
- Môi trường chung: Windows 11 Home Single Language 10.0.26200; Google Chrome 155.0.8059.85; EShop commit `85af3ba`; backend `http://localhost:3000`; web `http://localhost:5173`
- Điều kiện tiên quyết chung: Đã reset dữ liệu EShop về dữ liệu mẫu (có `test@eshop.com`, `admin@eshop.com`); chưa đăng nhập

### Tổng hợp

| Bug | Tiêu đề ngắn | Severity | Technique | Test case | Issue |
|---|---|---|---|---|---|
| BUG-FR01-01 | Giao diện từ chối mật khẩu hợp lệ, không đăng ký được | Critical | EP, BVA | TC-REG-01, TC-REG-108 | #___ |
| BUG-FR01-02 | Form không có trường Xác nhận mật khẩu | High | EP | TC-REG-90 (chặn TC-REG-59 đến 62) | #___ |
| BUG-FR01-03 | API nhận Họ Tên rỗng hoặc chỉ có dấu cách | High | EP | TC-REG-71, TC-REG-72 | #___ |
| BUG-FR01-04 | API nhận Email rỗng hoặc chỉ có dấu cách | High | EP | TC-REG-73, TC-REG-80 | #___ |
| BUG-FR01-05 | API nhận Mật khẩu rỗng | High | EP | TC-REG-75 | #___ |
| BUG-FR01-06 | API nhận Email sai định dạng | High | EP, BVA | TC-REG-74, TC-REG-130 | #___ |
| BUG-FR01-07 | API cho tạo nhiều tài khoản cùng một Email | High | EP | TC-REG-82; bước kiểm chứng của TC-REG-71, 72, 75, 76, 77, 129 | #___ |
| BUG-FR01-08 | API nhận Mật khẩu không đạt yêu cầu mạnh | High | EP, BVA | TC-REG-76, TC-REG-77, TC-REG-129 | #___ |
| BUG-FR01-09 | Ô Email không dùng `type="email"` | Medium | EP | TC-REG-96 | #___ |
| BUG-FR01-10 | Trường bắt buộc không có dấu `*` | Low | EP | TC-REG-95 | #___ |
| BUG-FR01-11 | Nút "Đăng Ký" màu đỏ thay vì xanh dương | Low | EP | TC-REG-92 | #___ |
| BUG-FR01-12 | Trang Đăng ký không có thẻ `<h1>` | Low | EP | TC-REG-93 | #___ |
| BUG-FR01-13 | Có chữ không phải tiếng Việt trên trang Đăng ký | Low | EP | TC-REG-91 | #___ |

Label chung cho mọi bug của FR-01: `bug` (template tự gắn), `platform: web`, `pool: A`. Label `severity` và `technique` theo bảng trên.

---

### BUG-FR01-01: Giao diện từ chối mật khẩu hợp lệ, không đăng ký được

- **Issue:** #___
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

- **Issue:** #___
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

- **Issue:** #___
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

**Ảnh chụp:** Log `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`, đoạn TC-REG-71 và TC-REG-72

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Tái hiện qua API vì giao diện đang bị BUG-FR01-01 chặn mọi lần đăng ký. Các bug BUG-FR01-03 đến 08 cho thấy API đăng ký không kiểm tra dữ liệu đầu vào. Related: (số issue của BUG-FR01-04 đến 08)

---

### BUG-FR01-04: API nhận Email rỗng hoặc chỉ có dấu cách

- **Issue:** #___
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

**Ảnh chụp:** Log `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`, đoạn TC-REG-73 và TC-REG-80

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, ô Email để trống bị trình duyệt chặn (TC-REG-32 Pass); lỗi nằm ở phía API. Related: (số issue của BUG-FR01-03)

---

### BUG-FR01-05: API nhận Mật khẩu rỗng

- **Issue:** #___
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

**Ảnh chụp:** Log `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`, đoạn TC-REG-75

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, ô Mật khẩu để trống bị trình duyệt chặn (TC-REG-49 Pass); lỗi nằm ở phía API. Related: (số issue của BUG-FR01-03)

---

### BUG-FR01-06: API nhận Email sai định dạng

- **Issue:** #___
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

**Ảnh chụp:** Log `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`, đoạn TC-REG-74 và TC-REG-130

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Đặc tả chỉ nêu ví dụ `user@domain.com`. Quy tắc định dạng dùng khi thiết kế là quy tắc của `type="email"` trong HTML5 (FR-22 yêu cầu ô Email dùng `type="email"`), theo đó mỗi nhãn tên miền dài tối đa 63 ký tự. TC-REG-74 sai định dạng theo mọi cách hiểu. Related: (số issue của BUG-FR01-03, BUG-FR01-09)

---

### BUG-FR01-07: API cho tạo nhiều tài khoản cùng một Email

- **Issue:** #___
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

**Dữ liệu test:** Email lặp lại `tc71@domain.com` (tương tự với `tc72`, `tc75`, `tc76`, `tc77`, `tc129@domain.com`); ` test@eshop.com `

**Kết quả mong đợi (theo đặc tả):** Lần đăng ký thứ hai với cùng email bị từ chối. README của EShop, FR-01:

> - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.

**Kết quả thực tế:** Gửi 2 lần cùng một email đều nhận HTTP 200 "User registered successfully" với 2 `id` khác nhau (ví dụ `tc71@domain.com`: id 4 và 5), tức cùng email được tạo 2 lần; lặp lại với 6 email. Email ` test@eshop.com ` cũng được chấp nhận (id 19).

**Ảnh chụp:** Log `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`, đoạn TC-REG-71 (bước kiểm chứng) và TC-REG-82

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Bằng chứng chính là việc trùng email chính xác (bước 1, 2), không phụ thuộc giả định nào. Với TC-REG-82, việc coi ` test@eshop.com ` là trùng dựa trên giả định A07 (cắt dấu cách đầu cuối của Email) ở `features/A_FR-01_DangKy/02_ec.md`. Qua giao diện chưa kiểm được (TC-REG-45 bị BUG-FR01-01 chặn). Related: (số issue của BUG-FR01-03)

---

### BUG-FR01-08: API nhận Mật khẩu không đạt yêu cầu mạnh

- **Issue:** #___
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

**Ảnh chụp:** Log `features/A_FR-01_DangKy/logs/S6_api_20261020_233042.log`, đoạn TC-REG-76, TC-REG-77, TC-REG-129

**Môi trường:** Windows 11, EShop commit `85af3ba`, gọi API bằng script Python (`features/A_FR-01_DangKy/scripts/run_api_tests.py`)

**Ghi chú:** Qua giao diện, các mật khẩu này bị từ chối (TC-REG-50, 56, 107 Pass), nhưng giao diện cũng từ chối cả mật khẩu hợp lệ (BUG-FR01-01). Phía API thì không kiểm tra độ mạnh mật khẩu. Related: (số issue của BUG-FR01-01, BUG-FR01-03)

---

### BUG-FR01-09: Ô Email không dùng `type="email"`

- **Issue:** #___
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

**Ghi chú:** Ô Mật khẩu đạt yêu cầu tương ứng (`type="password"`, ký tự bị che). Related: (số issue của BUG-FR01-06)

---

### BUG-FR01-10: Trường bắt buộc không có dấu `*`

- **Issue:** #___
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

- **Issue:** #___
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

- **Issue:** #___
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

- **Issue:** #___
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
