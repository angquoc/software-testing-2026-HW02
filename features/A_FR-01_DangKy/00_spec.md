# S0: Trích đặc tả và khảo sát giao diện (FR-01 Đăng ký tài khoản)

- Bước: S0 (Trích đặc tả, khảo sát giao diện)
- Thời gian tạo: 2026-10-19 11:21 (+07:00)
- Sửa lần 1: 2026-10-19 15:01 (+07:00). Bỏ mọi mục cần DevTools hoặc thuộc tính HTML khỏi câu hỏi mở và bảng quan sát, theo WORKFLOW mục 1.1 và 3.1
- Nền tảng: Web, `http://localhost:5173`

---

## 1. Trích nguyên văn đặc tả

Phần trích dưới đây giữ nguyên văn từ tài liệu gốc, kể cả dấu câu và định dạng.

### 1.1 FR-01 (nguồn: `eshop-sut/README.md`, mục 2)

> ### FR-01: Đăng ký tài khoản
>
> - Người dùng phải cung cấp: **Họ Tên**, **Email**, **Mật khẩu**.
> - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
> - **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
> - Phải có trường **Xác nhận mật khẩu** — hệ thống từ chối nếu hai trường không khớp.
> - Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### 1.2 Tài khoản mặc định (nguồn: `eshop-sut/README.md`, mục 1)

Liên quan tới yêu cầu email là duy nhất: Hai email này đã tồn tại sẵn trong hệ thống.

> **Tài khoản mặc định:**
>
> - Admin: `admin@eshop.com` / `Admin123!`
> - User test: `test@eshop.com` / `Test1234!`

### 1.3 FR-21 (nguồn: `eshop-sut/README.md`, mục 8)

> ### FR-21: Tiêu chuẩn Giao diện Chung
>
> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
> - **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
> - **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
> - **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

### 1.4 FR-22 (nguồn: `eshop-sut/README.md`, mục 8)

> ### FR-22: Form Requirements
>
> - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
> - Trường Email phải dùng `type="email"`.
> - Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
> - Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
> - Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

### 1.5 API đăng ký (nguồn: `eshop-sut/api_specification.md`, mục 1.1)

> ### 1.1 Đăng ký tài khoản
> - **Endpoint:** `POST /api/register`
> - **Body (JSON):**
>   ```json
>   {
>     "name": "Nguyen Van A",
>     "email": "test@domain.com",
>     "password": "Password123!"
>   }
>   ```
> - **Phản hồi thành công (200 OK):** `{"message": "User registered successfully", "id": 1}`

### 1.6 Yêu cầu bảo mật, chỉ để tham khảo (nguồn: `eshop-sut/README.md`, mục 9)

Phần này chưa thuộc phạm vi chính. Việc có tạo lớp tương đương cho dữ liệu chứa HTML hoặc ký tự đặc biệt hay không sẽ quyết định ở S2.

> | ID     | Yêu cầu                                                                                                         |
> | ------ | --------------------------------------------------------------------------------------------------------------- |
> | SEC-01 | Mật khẩu **không** được lưu dưới dạng plaintext.                                                                |
> | SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
> | SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp.                                         |

---

## 2. Danh sách yêu cầu có mã

### 2.1 Nhóm chính: FR-01

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| FR01-R01 | Người dùng phải cung cấp Họ Tên | FR-01, ý 1 |
| FR01-R02 | Người dùng phải cung cấp Email | FR-01, ý 1 |
| FR01-R03 | Người dùng phải cung cấp Mật khẩu | FR-01, ý 1 |
| FR01-R04 | Email phải có định dạng hợp lệ (`user@domain.com`) | FR-01, ý 2 |
| FR01-R05 | Email phải là duy nhất trong hệ thống | FR-01, ý 2; mục 1.2 |
| FR01-R06 | Mật khẩu có tối thiểu 8 ký tự | FR-01, ý 3 |
| FR01-R07 | Mật khẩu có ít nhất 1 chữ hoa | FR-01, ý 3 |
| FR01-R08 | Mật khẩu có ít nhất 1 chữ thường | FR-01, ý 3 |
| FR01-R09 | Mật khẩu có ít nhất 1 chữ số | FR-01, ý 3 |
| FR01-R10 | Mật khẩu có ít nhất 1 ký tự đặc biệt trong tập `@`, `$`, `!`, `%`, `*`, `?`, `&` | FR-01, ý 3 |
| FR01-R11 | Form phải có trường Xác nhận mật khẩu | FR-01, ý 4 |
| FR01-R12 | Hệ thống từ chối đăng ký nếu Mật khẩu và Xác nhận mật khẩu không khớp | FR-01, ý 4 |
| FR01-R13 | Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập | FR-01, ý 5 |

### 2.2 Nhóm phụ: Giao diện (FR-21, FR-22)

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| FR01-R14 | Toàn bộ giao diện trang Đăng ký dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn) | FR-21, ý 1 |
| FR01-R15 | Nút hành động tích cực (nút submit đăng ký) dùng màu xanh dương; nút nguy hiểm/hủy bỏ (nếu có) dùng màu đỏ | FR-21, ý 2 |
| FR01-R16 | Trang Đăng ký có đúng 1 thẻ `<h1>` mô tả nội dung trang | FR-21, ý 4 |
| FR01-R17 | Thứ tự focus theo Tab đi từ trên xuống dưới, trái sang phải | FR-21, ý 5 |
| FR01-R18 | Mọi trường bắt buộc có ký hiệu `*` bên cạnh nhãn | FR-22, ý 1 |
| FR01-R19 | Trường Email dùng `type="email"` | FR-22, ý 2 |
| FR01-R20 | Trường Mật khẩu dùng `type="password"` (không hiển thị rõ) | FR-22, ý 3 |
| FR01-R21 | Thông báo lỗi xuất hiện phía trên nút submit | FR-22, ý 4 |

Không áp dụng cho FR-01: "Nhất quán đơn vị tiền" (FR-21, ý 3) vì form không có giá tiền; "Step Indicator" (FR-22, ý 5) vì đặc tả mô tả đăng ký là form một bước.

### 2.3 Nhóm API

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| FR01-R22 | `POST /api/register` nhận body JSON gồm `name`, `email`, `password`; khi thành công trả về 200 OK với `{"message": "User registered successfully", "id": <số>}` | API spec, mục 1.1 |

### 2.4 Nhóm tham khảo: Bảo mật (chốt ở S2)

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| FR01-R23 | Mật khẩu không được lưu dạng plaintext | SEC-01 |
| FR01-R24 | Dữ liệu người dùng nhập (ví dụ Họ Tên) khi hiển thị trên UI phải được escape, không render HTML | SEC-04 |
| FR01-R25 | Truy vấn CSDL dùng Parameterized Query | SEC-05 |

Ghi chú: FR01-R23 và FR01-R25 không quan sát trực tiếp được bằng kiểm thử hộp đen qua giao diện.

---

## 3. Câu hỏi mở

Đây là những điểm đặc tả chưa nói rõ. Chưa có câu trả lời; sinh viên quyết định ở bản review (trả lời bằng quan sát, hoặc ghi thành giả định). Cột "Có thể làm rõ bằng" chỉ cho biết nguồn thông tin, không phải câu trả lời.

### 3.1 Họ Tên

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q01 | Họ Tên có độ dài tối thiểu và tối đa là bao nhiêu? | FR01-R01 | Không có trong đặc tả |
| Q02 | Họ Tên được phép chứa những ký tự nào (chữ có dấu tiếng Việt, chữ số, ký tự đặc biệt, thẻ HTML)? | FR01-R01, FR01-R24 | Không có trong đặc tả |
| Q03 | Họ Tên chỉ gồm khoảng trắng có được coi là "đã cung cấp" không? | FR01-R01 | Không có trong đặc tả |

### 3.2 Email

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q04 | "Định dạng hợp lệ (`user@domain.com`)" chỉ là ví dụ. Quy tắc định dạng cụ thể là gì? Ví dụ: `user@domain` (không có phần đuôi tên miền) có hợp lệ không, trong khi `type="email"` của HTML5 chấp nhận dạng này? | FR01-R04, FR01-R19 | Không có trong đặc tả |
| Q05 | Email có độ dài tối đa là bao nhiêu? | FR01-R04 | Không có trong đặc tả |
| Q06 | Kiểm tra trùng email có phân biệt chữ hoa, chữ thường không (`Test@eshop.com` so với `test@eshop.com`)? | FR01-R05 | Không có trong đặc tả |
| Q07 | Khoảng trắng ở đầu hoặc cuối email có được cắt bỏ trước khi kiểm tra định dạng và kiểm tra trùng không? | FR01-R04, FR01-R05 | Không có trong đặc tả |

### 3.3 Mật khẩu

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q08 | Mật khẩu có độ dài tối đa không? Nếu có thì là bao nhiêu? | FR01-R06 | Không có trong đặc tả |
| Q09 | Tập ký tự đặc biệt `@ $ ! % * ? &` là danh sách đóng hay chỉ là ví dụ? Mật khẩu mà ký tự đặc biệt duy nhất nằm ngoài tập này (ví dụ `#`, `_`, `-`) có đạt điều kiện "1 ký tự đặc biệt" không? | FR01-R10 | Không có trong đặc tả |
| Q10 | Mật khẩu đã đủ 4 loại ký tự nhưng có thêm ký tự khác (khoảng trắng, `#`, chữ có dấu) thì được chấp nhận hay bị từ chối? Đặc tả chỉ nói "có ít nhất", không nói có cấm ký tự khác hay không. | FR01-R06 đến FR01-R10 | Không có trong đặc tả |
| Q11 | "Chữ hoa" và "chữ thường" chỉ gồm `A-Z`, `a-z`, hay tính cả chữ có dấu (ví dụ `Ă`, `ă`)? | FR01-R07, FR01-R08 | Không có trong đặc tả |

### 3.4 Xác nhận mật khẩu

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q12 | Trường Xác nhận mật khẩu có phải dùng `type="password"` không? FR-22 chỉ nhắc "Trường Mật khẩu". | FR01-R11, FR01-R20 | Không có trong đặc tả |
| Q13 | Trường Xác nhận mật khẩu có bắt buộc (có dấu `*`) không? Đặc tả FR-01 ý 1 chỉ liệt kê Họ Tên, Email, Mật khẩu. | FR01-R11, FR01-R18 | Quan sát S0 cho biết hiện trạng; đặc tả không nói yêu cầu |
| Q14 | "Khớp" có nghĩa là trùng khớp chính xác từng ký tự (phân biệt hoa thường, tính cả khoảng trắng) không? | FR01-R12 | Không có trong đặc tả |
| Q15 | Body của `POST /api/register` không có trường xác nhận mật khẩu. Việc so khớp chỉ diễn ra ở phía giao diện? (Liên quan tới quyết định có gọi API ở S3.) | FR01-R12, FR01-R22 | Không có trong đặc tả |

### 3.5 Kết quả và thông báo

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q16 | Nội dung chính xác của từng thông báo lỗi là gì? Đặc tả không nêu câu chữ nào. | FR01-R04 đến FR01-R12 | Chạy thử S6 |
| Q17 | Khi nhiều trường cùng sai, hệ thống báo một lỗi hay tất cả? Nếu một lỗi thì theo thứ tự nào? | FR01-R01 đến FR01-R12 | Chạy thử S6 |
| Q18 | Sau khi đăng ký thành công: Có thông báo thành công không? Người dùng có được tự đăng nhập không, hay chỉ chuyển sang trang Đăng nhập? | FR01-R13 | Chạy thử S6 |
| Q19 | Khi đăng ký thất bại, dữ liệu đã nhập có được giữ lại trên form không? | FR01-R01 đến FR01-R12 | Chạy thử S6 |
| Q20 | Người dùng đang đăng nhập có truy cập được trang Đăng ký không? | Không có yêu cầu tương ứng | Không có trong đặc tả |

### 3.6 API

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q21 | Khi đăng ký thất bại, API trả về mã HTTP và nội dung gì? Đặc tả chỉ nêu phản hồi 200 OK. | FR01-R22 | Không có trong đặc tả |
| Q22 | Backend có tự kiểm tra lại định dạng email, độ mạnh mật khẩu và tính duy nhất không, hay chỉ giao diện kiểm tra? | FR01-R04 đến FR01-R10, FR01-R22 | Không có trong đặc tả |
| Q23 | API có bỏ qua các trường không có trong đặc tả (ví dụ `role`) khi gửi kèm trong body không? SEC-06 chỉ nói về API cập nhật hồ sơ. | FR01-R22 | Không có trong đặc tả |

### 3.7 Giao diện

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q24 | Trang Đăng ký có những nút nào? Nút nào được coi là "hành động tích cực", nút nào là "hủy bỏ"? | FR01-R15 | Quan sát S0 |
| Q25 | Thẻ `<h1>` của trang Đăng ký phải có nội dung gì để được coi là "mô tả nội dung trang"? | FR01-R16 | Không có trong đặc tả |

---

## 4. Bảng quan sát giao diện (sinh viên điền)

Phạm vi: Chỉ ghi những gì nhìn thấy được bằng mắt khi mở trang Đăng ký, **không nhập dữ liệu, không bấm nút submit, không dùng DevTools**. Những gì chỉ thấy khi nhập hoặc khi xem HTML (thông báo lỗi, vị trí thông báo lỗi, giới hạn ký tự, ký tự gõ vào có bị che không, thứ tự Tab, thuộc tính `type`, số thẻ `<h1>`) để tới S6.

Trạng thái khi quan sát: Chưa đăng nhập; trình duyệt mở `http://localhost:5173`.

Ghi đúng chữ như trên giao diện, kể cả hoa thường và dấu câu. Ô nào không có thì ghi "Không có".

### 4.1 Đường vào trang

| # | Mục quan sát | Kết quả quan sát | Ảnh |
|---|---|---|---|
| O01 | Cách mở trang Đăng ký (nút hoặc liên kết nào, nằm ở đâu: navbar, trang Đăng nhập...) | Ở nút Đang Ký trên navbar hoặc nút Đăng ký ngay ở trang Đăng nhập hoặc đường dẫn http://localhost:5173/register | |
| O02 | Đường dẫn trên thanh địa chỉ khi đang ở trang Đăng ký | http://localhost:5173/register | |
| O03 | Tiêu đề tab trình duyệt | EShop
 | |

### 4.2 Tiêu đề và chữ hiển thị sẵn

| # | Mục quan sát | Kết quả quan sát | Ảnh |
|---|---|---|---|
| O04 | Các tiêu đề nhìn thấy trên trang (tiêu đề lớn của form và tiêu đề khác nếu có), ghi đúng chữ | EShop, Đăng Ký Tài Khoản, Họ Tên, Email, Mật khẩu | |
| O05 | Các dòng chữ hướng dẫn hiển thị sẵn (ví dụ gợi ý quy tắc mật khẩu, chú thích dấu `*`), ghi nguyên văn | Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt. | |
| O06 | Có chữ tiếng Anh nào trên trang không? Ghi nguyên văn từng chỗ | Không có | |

### 4.3 Các ô nhập

Ghi theo thứ tự từ trên xuống dưới trên form. Nếu form có thêm trường khác ngoài 4 trường dưới đây, thêm dòng ở cuối bảng.

| # | Nhãn hiển thị (nguyên văn) | Có `*` cạnh nhãn? | Placeholder (nguyên văn) | Giá trị mặc định | Loại ô nhìn thấy được (ô chữ, dropdown, ô chọn ngày...) | Có biểu tượng hoặc nút nào trong ô (ví dụ nút hiện/ẩn mật khẩu)? | Ảnh |
|---|---|---|---|---|---|---|---|
| O07 (Họ Tên) | Họ Tên | Không có | Không có | Không có | Ô chữ | Không có | |
| O08 (Email) | Email | Không có | Không có | Không có | Ô chữ | Không có | |
| O09 (Mật khẩu) | Mật khẩu | Không có | Không có | Không có | Ô chữ | Không có | |
| O10 (Xác nhận mật khẩu) | KHÔNG CÓ Ô NÀY | | | | | | |
| O11 (trường khác, nếu có) | | | | | | | |

### 4.4 Nút và liên kết

| # | Nhãn (nguyên văn) | Loại (nút hay liên kết) | Màu nền và màu chữ | Vị trí trên form | Ảnh |
|---|---|---|---|---|---|
| O12 (nút submit) | Đăng Ký | Nút | Nền đỏ, chữ trắng | Dưới dòng Yêu cầu | |
| O13 (liên kết sang Đăng nhập) | Đã có tài khoản? Đăng nhập | Liên kết | Màu đen, chữ Đăng nhập màu xanh biển | Dưới nút Đăng ký | |

### 4.5 Ảnh cần chụp

| Tên file | Nội dung |
|---|---|
| `S0_01_form_dang_ky.png` | Toàn bộ trang Đăng ký khi vừa mở, chưa nhập gì |
| `S0_02_duong_vao_trang.png` | Nút hoặc liên kết dẫn tới trang Đăng ký (navbar hoặc trang Đăng nhập) |

Có thể thêm ảnh nếu thấy chi tiết nào cần lưu bằng chứng (ví dụ phóng to một nhãn hoặc một nút); đánh số tiếp từ `S0_03_`.
