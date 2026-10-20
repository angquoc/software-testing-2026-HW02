# S3: Chọn test case (FR-01 Đăng ký tài khoản)

- Bước: S3 (Chọn test case: Bảng phủ lớp tương đương và Minimum Set, theo Step 3 của slide S04)
- Thời gian tạo: 2026-10-20 10:44 (+07:00)
- Căn cứ: `02_ec.md` (70 lớp EC01 đến EC70), `01_io.md` (OUT1 đến OUT4, ERR1 đến ERR7, mục 3.4), `00_spec.md` (yêu cầu FR01-R01 đến FR01-R25)

---

## 1. Cách thực thi đã chốt trước khi viết

| Vấn đề | Lựa chọn của sinh viên |
|---|---|
| Có test qua API không | Giao diện là chính, cộng một nhóm nhỏ test case API cho các lớp mà trình duyệt hoặc giao diện có thể chặn trước, để biết hệ thống có tự kiểm tra lại không (Q22). EC65 chỉ test qua giao diện (`02_ec.md` mục 7.3) |
| Lớp của Xác nhận mật khẩu (EC41 đến EC45) | Viết đủ test case theo đặc tả, ghi chú dự kiến bị chặn (Blocked) ở S6 do giao diện và API đều không có trường này (D01) |
| Trình bày | S3, S4 viết bảng Markdown theo slide; S5 mới dùng skill `test-case-writing` để xuất Word, Excel |

## 2. Quy tắc chọn (slide S04, WORKFLOW mục 3.2)

- Mỗi lớp có ít nhất 1 test case.
- Test case hợp lệ phủ càng nhiều lớp hợp lệ càng tốt.
- Mỗi test case không hợp lệ chỉ phủ đúng 1 lớp không hợp lệ; các input còn lại lấy giá trị hợp lệ cơ sở.

---

## 3. Quy ước và dữ liệu nền

### 3.1 Ký hiệu

- `␣` là **một dấu cách**. Dùng ký hiệu này cho mọi giá trị có khoảng trắng ở đầu, cuối hoặc nhiều dấu cách liền nhau, để không bị mất khi hiển thị Markdown.
- Mã test case: `TC-REG-NN`. Dải số: 01 đến 09 hợp lệ (giao diện), 10 đến 49 không hợp lệ (giao diện), 50 đến 59 API, 60 đến 69 checklist giao diện.

### 3.2 Giá trị hợp lệ cơ sở

Dùng cho các input không phải đối tượng của test case.

| Input | Giá trị cơ sở | Lớp hợp lệ mà giá trị này thuộc về |
|---|---|---|
| IN1 Họ Tên | `Nguyen Van A` | EC01, EC04 |
| IN2 Email | `tcNN@domain.com`, với `NN` là số của test case | EC08, EC11, EC20 |
| IN3 Mật khẩu | `Abcdef1!` | EC24, EC26, EC28, EC31, EC34, EC36 |
| IN4 Xác nhận mật khẩu | Giống hệt Mật khẩu của test case | EC41 |

Mỗi test case dùng một email riêng (`tc01@domain.com`, `tc02@domain.com`...). Lý do: Một lần đăng ký thành công sẽ thêm email vào hệ thống (IN5); nếu dùng chung email, test case sau sẽ bị ERR4 thay vì kết quả cần kiểm tra.

### 3.3 Tiền điều kiện chung

- Chưa đăng nhập (`01_io.md` mục 1.1).
- Dữ liệu EShop đã reset về dữ liệu mẫu trước đợt test; dữ liệu mẫu có `test@eshop.com` và `admin@eshop.com`.
- Test qua giao diện: Trình duyệt Chrome, mở `http://localhost:5173/register`. Ghi phiên bản Chrome ở S6 (hệ quả 1 của A15).

### 3.4 Quy trình chung cho test case giao diện

1. Mở `http://localhost:5173/register`.
2. Nhập Họ Tên, Email, Mật khẩu theo bảng.
3. Nhập Xác nhận mật khẩu theo bảng. **Hiện giao diện không có trường này (D01):** Với test case không nhắm vào IN4 thì bỏ qua bước này và ghi chú vào kết quả; với test case nhắm vào IN4 (TC-REG-39 đến TC-REG-42) thì ghi Blocked.
4. Nhấn nút "Đăng Ký".
5. Quan sát kết quả theo bảng.

Kết quả mong đợi:

- **OUT1:** Đường dẫn đổi thành `/login` và trang hiện form đăng nhập (có ô nhập và nút gửi).
- **OUT2 kèm ERRn:** Có thông báo lỗi chỉ ra đúng nguyên nhân ERRn; vẫn ở `/register`. Không ghi câu chữ cụ thể (Q16).

---

## 4. Bảng phủ lớp (Test Cases Providing Coverage of Partitions)

Mỗi lớp và test case phủ nó. Lớp hợp lệ thường được phủ bởi nhiều test case; bảng chỉ ghi test case chính.

### 4.1 Lớp Input

| Lớp | Mô tả ngắn | Loại | Test case |
|---|---|---|---|
| EC01 | Họ Tên có ít nhất 1 ký tự sau khi cắt khoảng trắng | H | TC-REG-01 |
| EC02 | Họ Tên rỗng | KH | TC-REG-10 |
| EC03 | Họ Tên chỉ gồm khoảng trắng | KH | TC-REG-11 |
| EC04 | Họ Tên chỉ chữ Latin không dấu | H | TC-REG-01 |
| EC05 | Họ Tên có chữ tiếng Việt có dấu | H | TC-REG-02 |
| EC06 | Họ Tên có chữ số kèm chữ cái | H | TC-REG-03 |
| EC07 | Họ Tên có ký tự HTML hoặc SQL | H | TC-REG-08 |
| EC08 | Email có giá trị | H | TC-REG-01 |
| EC09 | Email rỗng | KH | TC-REG-12 |
| EC10 | Email chỉ gồm khoảng trắng | KH | TC-REG-13 |
| EC11 | Email đúng dạng như ví dụ đặc tả | H | TC-REG-01 |
| EC12 | Email có dấu chấm ở giữa phần trước `@` hoặc có tên miền con | H | TC-REG-02 |
| EC13 | Email thiếu `@` | KH | TC-REG-14 |
| EC14 | Email thiếu phần trước `@` | KH | TC-REG-15 |
| EC15 | Email thiếu phần sau `@` | KH | TC-REG-16 |
| EC16 | Email không có dấu chấm ở phần sau `@` | H | TC-REG-03 |
| EC17 | Email có từ 2 dấu `@` | KH | TC-REG-17 |
| EC18 | Email có khoảng trắng ở giữa | KH | TC-REG-18 |
| EC19 | Email có khoảng trắng đầu cuối | H | TC-REG-06 |
| EC20 | Email chưa có trong hệ thống | H | TC-REG-01 |
| EC21 | Email trùng dữ liệu mẫu | KH | TC-REG-25 |
| EC22 | Email trùng email vừa đăng ký | KH | TC-REG-26 |
| EC23 | Email trùng nhưng khác hoa thường | KH | TC-REG-27 |
| EC24 | Mật khẩu có giá trị | H | TC-REG-01 |
| EC25 | Mật khẩu rỗng | KH | TC-REG-29 |
| EC26 | Mật khẩu từ 8 ký tự | H | TC-REG-01 |
| EC27 | Mật khẩu từ 1 đến 7 ký tự | KH | TC-REG-30 |
| EC28 | Mật khẩu có chữ hoa `A-Z` | H | TC-REG-01 |
| EC29 | Mật khẩu không có chữ hoa | KH | TC-REG-31 |
| EC30 | Chữ hoa duy nhất là chữ có dấu | KH | TC-REG-32 |
| EC31 | Mật khẩu có chữ thường `a-z` | H | TC-REG-01 |
| EC32 | Mật khẩu không có chữ thường | KH | TC-REG-33 |
| EC33 | Chữ thường duy nhất là chữ có dấu | KH | TC-REG-34 |
| EC34 | Mật khẩu có chữ số | H | TC-REG-01 |
| EC35 | Mật khẩu không có chữ số | KH | TC-REG-35 |
| EC36 | Mật khẩu có ký tự trong tập `@ $ ! % * ? &` | H | TC-REG-01 đến TC-REG-07 (mỗi test case một ký tự, đủ 7 ký tự) |
| EC37 | Mật khẩu không có ký tự đặc biệt | KH | TC-REG-36 |
| EC38 | Ký tự đặc biệt duy nhất nằm ngoài tập | KH | TC-REG-37 |
| EC39 | Mật khẩu có khoảng trắng ở giữa | H | TC-REG-05 |
| EC40 | Mật khẩu có ký tự ngoài 4 loại | H | TC-REG-06 |
| EC41 | Xác nhận mật khẩu giống hệt Mật khẩu | H | TC-REG-01 đến TC-REG-09 (chỉ phủ trên thiết kế, xem mục 7) |
| EC42 | Xác nhận mật khẩu khác Mật khẩu | KH | TC-REG-39 |
| EC43 | Xác nhận mật khẩu rỗng | KH | TC-REG-40 |
| EC44 | Chỉ khác ở hoa thường | KH | TC-REG-41 |
| EC45 | Chỉ khác ở khoảng trắng đầu cuối | KH | TC-REG-42 |
| EC54 | Họ Tên có khoảng trắng đầu cuối | H | TC-REG-04 |
| EC55 | Họ Tên không có chữ cái nào | H | TC-REG-06 |
| EC56 | Họ Tên có ký tự đặc biệt thông thường | H | TC-REG-05 |
| EC57 | Dấu chấm ở đầu, cuối, hoặc liền nhau ở phần trước `@` | H | TC-REG-04 |
| EC58 | Dấu chấm tạo nhãn rỗng ở phần sau `@` | KH | TC-REG-19 |
| EC59 | Ký tự đặc biệt thuộc tập HTML5 ở phần trước `@` | H | TC-REG-05 |
| EC60 | Ký tự ngoài tập HTML5 ở phần trước `@` | KH | TC-REG-20 |
| EC61 | Ký tự không cho phép ở phần sau `@` | KH | TC-REG-21 |
| EC62 | Nhãn tên miền bắt đầu hoặc kết thúc bằng `-` | KH | TC-REG-22 |
| EC63 | Nhãn tên miền dài hơn 63 ký tự | KH | TC-REG-23 |
| EC64 | Unicode ở phần trước `@` | KH | TC-REG-24 |
| EC65 | Tên miền có chữ có dấu | H | TC-REG-07 |
| EC66 | Email có dấu nháy đơn | H | TC-REG-09 |
| EC67 | Email trùng sau khi cắt khoảng trắng | KH | TC-REG-28 |
| EC68 | Mật khẩu chỉ đủ 8 ký tự khi tính khoảng trắng đầu cuối | H | TC-REG-07 |
| EC69 | Mật khẩu chỉ gồm khoảng trắng | H (điều kiện bắt buộc) | TC-REG-38 |
| EC70 | Họ Tên có nhiều khoảng trắng liền nhau ở giữa | H | TC-REG-07 |

### 4.2 Lớp Output

| Lớp | Output | Test case |
|---|---|---|
| EC46 | OUT1 | TC-REG-01 đến TC-REG-09 |
| EC47 | ERR1 | TC-REG-10, TC-REG-11 |
| EC48 | ERR2 | TC-REG-12, TC-REG-13 |
| EC49 | ERR3 | TC-REG-14 đến TC-REG-24 |
| EC50 | ERR4 | TC-REG-25 đến TC-REG-28 |
| EC51 | ERR5 | TC-REG-29 |
| EC52 | ERR6 | TC-REG-30 đến TC-REG-38 |
| EC53 | ERR7 | TC-REG-39 đến TC-REG-42 |

---

## 5. Minimum Set

### 5.1 Test case hợp lệ (giao diện)

Mỗi test case ghép 1 lớp đặc biệt của Họ Tên, 1 của Email, 1 của Mật khẩu để phủ nhiều lớp nhất. Các lớp mang rủi ro SQL, HTML (EC07, EC66) được tách riêng, ghép với giá trị cơ sở, để nếu lỗi thì biết ngay nguyên nhân. Ký tự đặc biệt của mật khẩu được xoay vòng để đủ 7 ký tự trong tập (quyết định 1 ở `02_ec.md`).

| TC | Lớp phủ | Họ Tên | Email | Mật khẩu | Xác nhận mật khẩu | Kết quả mong đợi |
|---|---|---|---|---|---|---|
| TC-REG-01 | EC01, EC04, EC08, EC11, EC20, EC24, EC26, EC28, EC31, EC34, EC36 (`!`), EC41, EC46 | `Nguyen Van A` | `tc01@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1 |
| TC-REG-02 | EC05, EC12, EC36 (`*`) | `Nguyễn Thị Ánh` | `an.nguyen@mail.domain.com` | `Abcdef1*` | `Abcdef1*` | OUT1 |
| TC-REG-03 | EC06, EC16, EC36 (`$`) | `Nguyen Van A2` | `tc03@domain` | `Abcdef1$` | `Abcdef1$` | OUT1 |
| TC-REG-04 | EC54, EC57, EC36 (`%`) | `␣Nguyen Van A␣` | `.tc04@domain.com` | `Abcdef1%` | `Abcdef1%` | OUT1 |
| TC-REG-05 | EC56, EC59, EC39, EC36 (`?`) | `Anh-Ngoc` | `tc+05@domain.com` | `Abc def1?` | `Abc def1?` | OUT1 |
| TC-REG-06 | EC55, EC19, EC40, EC36 (`&`) | `12345` | `␣tc06@domain.com␣` | `Abcdef1&é` | `Abcdef1&é` | OUT1 |
| TC-REG-07 | EC70, EC65, EC68, EC36 (`@`) | `Nguyen␣␣Van A` | `tc07@tênmiền.vn` | `Abcde1@␣` (8 ký tự, cuối là dấu cách) | `Abcde1@␣` | OUT1 |
| TC-REG-08 | EC07 | `<b>O'Brien</b>` | `tc08@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1, không xuất hiện lỗi hệ thống |
| TC-REG-09 | EC66 | `Nguyen Van A` | `o'brien@domain.com` | `Abcdef1!` | `Abcdef1!` | OUT1, không xuất hiện lỗi hệ thống |

Ghi chú:

- TC-REG-08 dùng một giá trị gộp cả hai rủi ro của EC07 (thẻ HTML và dấu nháy đơn), vì EC07 là một lớp.
- TC-REG-07 phụ thuộc trình duyệt chuyển tên miền sang punycode (A15 (b)); chỉ chạy qua giao diện.

### 5.2 Test case không hợp lệ (giao diện)

Mỗi test case chỉ có 1 input thuộc lớp không hợp lệ; các input khác lấy giá trị cơ sở (mục 3.2). Cột "Input thay đổi" và "Giá trị" chỉ ghi input khác giá trị cơ sở.

| TC | Lớp không hợp lệ phủ | Input thay đổi | Giá trị | Email của test case | Kết quả mong đợi |
|---|---|---|---|---|---|
| TC-REG-10 | EC02 | Họ Tên | (để trống) | `tc10@domain.com` | OUT2, ERR1 |
| TC-REG-11 | EC03 | Họ Tên | `␣␣␣` (3 dấu cách) | `tc11@domain.com` | OUT2, ERR1 |
| TC-REG-12 | EC09 | Email | (để trống) | (để trống) | OUT2, ERR2 |
| TC-REG-13 | EC10 | Email | `␣␣␣` (3 dấu cách) | `␣␣␣` | OUT2, ERR2 |
| TC-REG-14 | EC13 | Email | `tc14domain.com` | `tc14domain.com` | OUT2, ERR3 |
| TC-REG-15 | EC14 | Email | `@domain.com` | `@domain.com` | OUT2, ERR3 |
| TC-REG-16 | EC15 | Email | `tc16@` | `tc16@` | OUT2, ERR3 |
| TC-REG-17 | EC17 | Email | `tc17@@domain.com` | `tc17@@domain.com` | OUT2, ERR3 |
| TC-REG-18 | EC18 | Email | `tc␣18@domain.com` | `tc␣18@domain.com` | OUT2, ERR3 |
| TC-REG-19 | EC58 | Email | `tc19@.domain.com` | `tc19@.domain.com` | OUT2, ERR3 |
| TC-REG-20 | EC60 | Email | `tc(20)@domain.com` | `tc(20)@domain.com` | OUT2, ERR3 |
| TC-REG-21 | EC61 | Email | `tc21@do_main.com` | `tc21@do_main.com` | OUT2, ERR3 |
| TC-REG-22 | EC62 | Email | `tc22@-domain.com` | `tc22@-domain.com` | OUT2, ERR3 |
| TC-REG-23 | EC63 | Email | `tc23@` + 70 chữ `a` + `.com` | (như cột Giá trị) | OUT2, ERR3 |
| TC-REG-24 | EC64 | Email | `nguyễn24@domain.com` | `nguyễn24@domain.com` | OUT2, ERR3 |
| TC-REG-25 | EC21 | Email | `test@eshop.com` | `test@eshop.com` | OUT2, ERR4 |
| TC-REG-26 | EC22 | Email | `tc26@domain.com`, đăng ký 2 lần (xem ghi chú) | `tc26@domain.com` | Lần 1: OUT1. Lần 2: OUT2, ERR4 |
| TC-REG-27 | EC23 | Email | `Test@Eshop.com` | `Test@Eshop.com` | OUT2, ERR4 |
| TC-REG-28 | EC67 | Email | `␣test@eshop.com␣` | `␣test@eshop.com␣` | OUT2, ERR4 |
| TC-REG-29 | EC25 | Mật khẩu và Xác nhận mật khẩu | (để trống cả hai) | `tc29@domain.com` | OUT2, ERR5 |
| TC-REG-30 | EC27 | Mật khẩu và Xác nhận mật khẩu | `Abcd1!` (6 ký tự) | `tc30@domain.com` | OUT2, ERR6 |
| TC-REG-31 | EC29 | Mật khẩu và Xác nhận mật khẩu | `abcdef1!` | `tc31@domain.com` | OUT2, ERR6 |
| TC-REG-32 | EC30 | Mật khẩu và Xác nhận mật khẩu | `Ăbcdef1!` | `tc32@domain.com` | OUT2, ERR6 |
| TC-REG-33 | EC32 | Mật khẩu và Xác nhận mật khẩu | `ABCDEF1!` | `tc33@domain.com` | OUT2, ERR6 |
| TC-REG-34 | EC33 | Mật khẩu và Xác nhận mật khẩu | `ABCDEă1!` | `tc34@domain.com` | OUT2, ERR6 |
| TC-REG-35 | EC35 | Mật khẩu và Xác nhận mật khẩu | `Abcdefg!` | `tc35@domain.com` | OUT2, ERR6 |
| TC-REG-36 | EC37 | Mật khẩu và Xác nhận mật khẩu | `Abcdefg1` | `tc36@domain.com` | OUT2, ERR6 |
| TC-REG-37 | EC38 | Mật khẩu và Xác nhận mật khẩu | `Abcdef1#` | `tc37@domain.com` | OUT2, ERR6 |
| TC-REG-38 | EC69 (ngoại lệ) | Mật khẩu và Xác nhận mật khẩu | `␣␣␣␣␣␣␣␣` (8 dấu cách) | `tc38@domain.com` | OUT2, **ERR6** (không phải ERR5) |
| TC-REG-39 | EC42 | Xác nhận mật khẩu | `Abcdef2!` | `tc39@domain.com` | OUT2, ERR7. Dự kiến Blocked (D01) |
| TC-REG-40 | EC43 | Xác nhận mật khẩu | (để trống) | `tc40@domain.com` | OUT2, ERR7. Dự kiến Blocked (D01) |
| TC-REG-41 | EC44 | Xác nhận mật khẩu | `abcdef1!` | `tc41@domain.com` | OUT2, ERR7. Dự kiến Blocked (D01) |
| TC-REG-42 | EC45 | Xác nhận mật khẩu | `Abcdef1!␣` | `tc42@domain.com` | OUT2, ERR7. Dự kiến Blocked (D01) |

Ghi chú:

- Với TC-REG-29 đến TC-REG-38, Xác nhận mật khẩu nhập giống hệt Mật khẩu, để lỗi duy nhất là ở Mật khẩu (không phát sinh ERR7).
- TC-REG-26: Bước 1 đăng ký `tc26@domain.com` với dữ liệu cơ sở, mong đợi OUT1. Bước 2 mở lại `/register`, đăng ký lại `tc26@domain.com` với Họ Tên `Tran Thi B`, mong đợi ERR4. Test case tự tạo dữ liệu nó cần, không phụ thuộc test case khác.
- TC-REG-38 vi phạm cả EC29, EC32, EC35, EC37 cùng lúc, là ngoại lệ đã ghi ở `02_ec.md` (EC69). Mục đích duy nhất: Phân biệt ERR5 với ERR6.
- TC-REG-23: 70 chữ `a` để giá trị nằm giữa lớp; biên 63, 64 để S4 xét.

### 5.3 Test case API

Gửi `POST http://localhost:3000/api/register`, header `Content-Type: application/json`, bằng Postman hoặc curl. Chọn các lớp mà phía giao diện có thể chặn trước khi gửi (bắt buộc cung cấp, định dạng email, độ mạnh mật khẩu). Không có test case API cho IN4 (API không có trường này) và EC65 (hệ quả 2 của A15).

Kết quả mong đợi:

- **OUT3:** HTTP 200 OK, body có `"message": "User registered successfully"` và `id` là số.
- **OUT4:** Không trả về phản hồi thành công như OUT3. Đặc tả không nêu mã HTTP và nội dung lỗi (Q21), nên ghi lại mã và body thực tế ở S6.
- **Kiểm chứng không tạo tài khoản** (`01_io.md` mục 3.4): Sau mỗi test case OUT4 có email hợp lệ, gửi lại request với cùng email và dữ liệu hợp lệ; mong đợi OUT3. Nếu nhận lỗi trùng email thì request trước đã tạo tài khoản.

| TC | Lớp phủ | Body JSON | Kết quả mong đợi |
|---|---|---|---|
| TC-REG-50 | EC01, EC08, EC11, EC20, EC24, EC26, EC28, EC31, EC34, EC36; OUT3 | `{"name": "Nguyen Van A", "email": "tc50@domain.com", "password": "Abcdef1!"}` | OUT3 |
| TC-REG-51 | EC02 | `{"name": "", "email": "tc51@domain.com", "password": "Abcdef1!"}` | OUT4; kiểm chứng không tạo tài khoản |
| TC-REG-52 | EC03 | `{"name": "   ", "email": "tc52@domain.com", "password": "Abcdef1!"}` (name là 3 dấu cách) | OUT4; kiểm chứng không tạo tài khoản |
| TC-REG-53 | EC09 | `{"name": "Nguyen Van A", "email": "", "password": "Abcdef1!"}` | OUT4 |
| TC-REG-54 | EC13 | `{"name": "Nguyen Van A", "email": "tc54domain.com", "password": "Abcdef1!"}` | OUT4 |
| TC-REG-55 | EC25 | `{"name": "Nguyen Van A", "email": "tc55@domain.com", "password": ""}` | OUT4; kiểm chứng không tạo tài khoản |
| TC-REG-56 | EC27 | `{"name": "Nguyen Van A", "email": "tc56@domain.com", "password": "Abcd1!"}` | OUT4; kiểm chứng không tạo tài khoản |
| TC-REG-57 | EC37 | `{"name": "Nguyen Van A", "email": "tc57@domain.com", "password": "Abcdefg1"}` | OUT4; kiểm chứng không tạo tài khoản |

### 5.4 Checklist giao diện (ngoài Domain Testing)

Theo quyết định 5 ở `01_io.md`. Không chia lớp; mỗi dòng là một điểm kiểm tra.

| TC | Yêu cầu | Điểm kiểm tra | Kết quả mong đợi | Cách kiểm tra |
|---|---|---|---|---|
| TC-REG-60 | FR01-R11 | Form có trường Xác nhận mật khẩu | Có trường này trên form | Quan sát (liên quan D01) |
| TC-REG-61 | FR01-R14 | Ngôn ngữ trên trang Đăng ký và tiêu đề tab | Toàn bộ tiếng Việt, trừ "EShop", "Email", "SUT" đã chấp nhận | Quan sát (liên quan D04) |
| TC-REG-62 | FR01-R15 | Màu nút "Đăng Ký" | Màu xanh dương | Quan sát (liên quan D03) |
| TC-REG-63 | FR01-R16 | Số thẻ `<h1>` trên trang | Đúng 1 thẻ, mô tả nội dung trang | DevTools ở S6 |
| TC-REG-64 | FR01-R17 | Thứ tự focus khi nhấn Tab từ đầu trang | Đi từ trên xuống dưới, trái sang phải: Họ Tên, Email, Mật khẩu, (Xác nhận mật khẩu), nút "Đăng Ký", liên kết "Đăng nhập" | Nhấn Tab |
| TC-REG-65 | FR01-R18 | Dấu `*` cạnh nhãn Họ Tên, Email, Mật khẩu (và Xác nhận mật khẩu) | Có dấu `*` | Quan sát (liên quan D02) |
| TC-REG-66 | FR01-R19, FR01-R20 | Thuộc tính `type` của ô Email và ô Mật khẩu; ký tự gõ vào ô Mật khẩu | Email: `type="email"`; Mật khẩu: `type="password"`, ký tự bị che | DevTools ở S6 và quan sát khi gõ |
| TC-REG-67 | FR01-R21 | Vị trí thông báo lỗi khi đăng ký bị từ chối (dùng dữ liệu của TC-REG-10) | Thông báo nằm phía trên nút "Đăng Ký" | Quan sát |

---

## 6. Kiểm tra lại quy tắc chọn

| Quy tắc | Kết quả |
|---|---|
| Mỗi lớp có ít nhất 1 test case | Đạt: 62 lớp Input và 8 lớp Output đều có test case (mục 4) |
| Test case hợp lệ phủ nhiều lớp hợp lệ | 9 test case hợp lệ phủ 29 lớp hợp lệ (trừ EC69, phủ bởi TC-REG-38) |
| Mỗi test case không hợp lệ phủ đúng 1 lớp không hợp lệ | Đạt, trừ TC-REG-38 (ngoại lệ đã ghi ở `02_ec.md`). TC-REG-26 có 2 bước nhưng chỉ bước 2 là không hợp lệ |

Tổng số test case: 9 hợp lệ và 33 không hợp lệ qua giao diện, 8 qua API, 8 checklist; cộng 58.

---

## 7. Lưu ý khi thực thi

- **EC41 chỉ được phủ trên thiết kế:** Các test case hợp lệ đều ghi Xác nhận mật khẩu giống Mật khẩu, nhưng giao diện không có trường này nên khi chạy sẽ bỏ qua bước nhập. Do đó TC-REG-01 đến TC-REG-09 có thể Pass mà FR01-R11, FR01-R12 vẫn chưa được kiểm chứng; kết luận về hai yêu cầu này dựa vào TC-REG-39 đến TC-REG-42 và TC-REG-60.
- **Thứ tự chạy:** Chạy TC-REG-25, TC-REG-27, TC-REG-28 trên dữ liệu mẫu chưa bị sửa. Các test case hợp lệ thêm email mới vào hệ thống, nhưng không đụng tới `test@eshop.com`, nên thứ tự giữa chúng không ảnh hưởng.
- **Khi test case hợp lệ thất bại:** Vì mỗi test case hợp lệ ghép nhiều lớp, nếu bị từ chối thì tách thành các test case nhỏ hơn (mỗi test case một lớp đặc biệt, phần còn lại dùng giá trị cơ sở) để tìm lớp gây lỗi.
- **Lỗi hệ thống:** "Không xuất hiện lỗi hệ thống" ở TC-REG-08, TC-REG-09 nghĩa là không có trang lỗi, không có thông báo lỗi chung chung không gắn với nguyên nhân nào trong ERR1 đến ERR7, và đăng ký hoàn tất như OUT1.

---

## 8. Điểm cần sinh viên quyết định khi review

| # | Vấn đề | Các lựa chọn |
|---|---|---|
| 1 | Cách ghép lớp trong test case hợp lệ (mục 5.1) | (a) Giữ cách ghép hiện tại; (b) Ghép khác (sinh viên chỉ rõ) |
| 2 | Lớp có nhiều đại diện ở `02_ec.md` (EC57, EC58, EC59, EC60, EC61, EC62, EC07) chỉ chọn 1 giá trị theo đúng EP. Có thêm test case cho các đại diện còn lại không? | (a) Giữ 1 giá trị mỗi lớp; (b) Thêm test case cho các đại diện còn lại ở S5 |
| 3 | Kiểm chứng "không tạo tài khoản" bằng đăng ký lại | (a) Chỉ áp cho test case API (mục 5.3), vì giao diện đã có dấu hiệu `/register` không đổi; (b) Áp cho cả test case không hợp lệ qua giao diện |
| 4 | Nhóm API: Đủ 8 test case như mục 5.3 chưa? | (a) Đủ; (b) Thêm lớp khác (ví dụ EC67, EC69, Q23 về trường `role`) |
| 5 | Checklist giao diện (mục 5.4) để ở S3 hay chuyển sang S5 | (a) Giữ ở S3; (b) Chuyển sang S5 |
