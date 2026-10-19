# S0: Trích đặc tả và khảo sát giao diện (FR-01 Đăng ký tài khoản)

- Bước: S0 (Trích đặc tả, khảo sát giao diện)
- Bản này: Bản review của S0. Bản gốc của AI: `ai_raw/S0_khao_sat.md` (lần đầu) và `ai_raw/S0_khao_sat_v2.md` (sửa lần 1)
- Thời gian tạo bản AI: 2026-10-19 11:21 (+07:00)
- Cập nhật sau quan sát giao diện: 2026-10-19 15:45 (+07:00). Sinh viên điền bảng quan sát và chụp ảnh; AI đối chiếu với ảnh, sửa chỗ ghi nhầm (mục 4.6), cập nhật câu hỏi mở (mục 3.8), ghi khác biệt giữa giao diện và đặc tả (mục 5)
- Cập nhật theo ảnh chụp lại: 2026-10-19 16:03 (+07:00). Sinh viên chụp lại cả 3 ảnh, có thanh tab trình duyệt; AI sửa O03, O06, mục 4.5, 4.6 và thêm D04
- Ghi quyết định của sinh viên: 2026-10-19 16:50 (+07:00). Q26, Q27, chữ tiếng Anh và D04 (mục 3.9)
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

### 3.8 Cập nhật sau quan sát giao diện

Chỉ ghi những gì nhìn thấy được trên ảnh. Câu nào chưa trả lời được thì vẫn để mở; sinh viên quyết định giả định ở bản review.

| Mã | Trạng thái sau quan sát | Căn cứ |
|---|---|---|
| Q01 | Vẫn mở. Giao diện không hiển thị giới hạn độ dài nào cho Họ Tên | O07 |
| Q05 | Vẫn mở. Giao diện không hiển thị giới hạn độ dài nào cho Email | O08 |
| Q08 | Vẫn mở. Dòng hướng dẫn chỉ nêu "Tối thiểu 8 ký tự", không nêu độ dài tối đa | O05 |
| Q09 | Vẫn mở. Dòng hướng dẫn chỉ ghi "ký tự đặc biệt", không liệt kê tập ký tự như đặc tả | O05 |
| Q12 | Chưa áp dụng được ở hiện trạng: Form không có trường Xác nhận mật khẩu. Giữ câu hỏi vì đặc tả vẫn yêu cầu trường này | O10 |
| Q13 | Chưa áp dụng được, cùng lý do với Q12. Ghi thêm: Cả ba trường đang có (Họ Tên, Email, Mật khẩu) đều không có dấu `*` | O07 đến O10 |
| Q14 | Vẫn mở; hiện chưa áp dụng được vì không có trường Xác nhận mật khẩu | O10 |
| Q15 | Vẫn mở. Vì giao diện không có trường Xác nhận mật khẩu, FR01-R12 hiện không thực thi được qua giao diện | O10 |
| Q24 | Đã trả lời bằng quan sát: Trong khung form có đúng 1 nút là "Đăng Ký" (nút submit, hành động tích cực) và 1 liên kết "Đăng nhập". Không có nút hủy bỏ | O12 đến O14 |
| Q25 | Vẫn mở. Tiêu đề lớn nhìn thấy trên form là "Đăng Ký Tài Khoản"; việc đó có phải thẻ `<h1>` hay không sẽ kiểm tra ở S6 | O04 |

Các câu Q02 đến Q04, Q06, Q07, Q10, Q11, Q16 đến Q23 không thay đổi, vì ảnh chụp không cho thêm thông tin.

Câu hỏi mới phát sinh từ quan sát:

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q26 | Form không có trường Xác nhận mật khẩu, trong khi đặc tả yêu cầu có. Từ S1 đến S4 có vẫn đưa trường này vào biến Input và chia lớp tương đương theo đặc tả không? | FR01-R11, FR01-R12 | Sinh viên quyết định |
| Q27 | FR01-R13 yêu cầu chuyển tới "trang Đăng nhập". Dấu hiệu nào dùng để xác nhận đã ở trang Đăng nhập? Trang có đường dẫn `/login` hiện hiển thị tiêu đề "Đăng Ký", nhãn "Username" và nút "Sign In" (ảnh `S0_03_duong_vao_trang_2.png`) | FR01-R13 | Sinh viên quyết định |

### 3.9 Quyết định của sinh viên

| Mục | Quyết định | Lý do |
|---|---|---|
| Q26 | Vẫn đưa trường Xác nhận mật khẩu vào biến Input và chia lớp tương đương từ S1 đến S4 | Test case được thiết kế từ đặc tả, không từ hiện trạng giao diện. FR01-R11 và FR01-R12 vẫn là yêu cầu cần kiểm thử |
| Q27 | Dấu hiệu xác nhận đã chuyển tới trang Đăng nhập (FR01-R13): (1) Đường dẫn trên thanh địa chỉ đổi thành `/login`; (2) Trang hiển thị form đăng nhập (có ô nhập và nút gửi). Không dựa vào chữ trên trang đó | Tiêu đề "Đăng Ký", nhãn "Username" và nút "Sign In" trên trang `/login` là vấn đề của FR-02 và FR-21, không thuộc FR-01 |
| Chữ không phải tiếng Việt (O06) | "EShop" và "Email": Chấp nhận. "SUT": Chấp nhận; nếu xét khắt khe thì chỉ ghi chú, không tính là lỗi | "EShop" là tên hệ thống; "Email" là thuật ngữ thông dụng, SRS cũng dùng |
| D04 | Tiêu đề tab "frontend-web" là ứng viên bug về ngôn ngữ (FR01-R14) | Không phải tiếng Việt và không mô tả nội dung trang đang mở |

---

## 4. Bảng quan sát giao diện

Phạm vi: Chỉ ghi những gì nhìn thấy được bằng mắt khi mở trang Đăng ký, **không nhập dữ liệu, không bấm nút submit, không dùng DevTools**. Những gì chỉ thấy khi nhập hoặc khi xem HTML (thông báo lỗi, vị trí thông báo lỗi, giới hạn ký tự, ký tự gõ vào có bị che không, thứ tự Tab, thuộc tính `type`, số thẻ `<h1>`) để tới S6.

Trạng thái khi quan sát: Chưa đăng nhập; trình duyệt mở `http://localhost:5173`.

Sinh viên điền bảng; AI đối chiếu với ảnh và sửa. Các chỗ đã sửa liệt kê ở mục 4.6.

### 4.1 Đường vào trang

| # | Mục quan sát | Kết quả quan sát | Ảnh |
|---|---|---|---|
| O01 | Cách mở trang Đăng ký | Có 3 cách: (1) Mục "Đăng ký" trên navbar, góc phải, sau "Giỏ hàng" và "Đăng nhập"; (2) Liên kết "Đăng ký ngay" sau dòng "Chưa có tài khoản?" ở trang Đăng nhập (`localhost:5173/login`); (3) Gõ trực tiếp đường dẫn `http://localhost:5173/register` | `S0_02_duong_vao_trang_1.png`, `S0_03_duong_vao_trang_2.png` |
| O02 | Đường dẫn trên thanh địa chỉ khi đang ở trang Đăng ký | `http://localhost:5173/register` (thanh địa chỉ hiển thị `localhost:5173/register`) | `S0_01_form_dang_ky.png` |
| O03 | Tiêu đề tab trình duyệt | frontend-web (giống nhau ở trang `/register` và trang `/login`) | `S0_01_form_dang_ky.png`, `S0_03_duong_vao_trang_2.png` |

### 4.2 Tiêu đề và chữ hiển thị sẵn

| # | Mục quan sát | Kết quả quan sát | Ảnh |
|---|---|---|---|
| O04 | Các tiêu đề nhìn thấy trên trang | Tiêu đề form: "Đăng Ký Tài Khoản" (chữ to, đậm, căn giữa khung form). Trên navbar, góc trái: Logo chữ "EShop" | `S0_01_form_dang_ky.png` |
| O05 | Các dòng chữ hiển thị sẵn | Dưới ô Mật khẩu, chữ nhỏ màu xám: "Yêu cầu: Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt." Không có chú thích cho dấu `*`. Chữ khác ngoài form: Navbar có "Giỏ hàng", "Đăng nhập", "Đăng ký"; footer có "© 2026 EShop SUT. Dành cho mục đích kiểm thử." | `S0_01_form_dang_ky.png` |
| O06 | Chữ tiếng Anh trên trang | Không có câu tiếng Anh. Các từ không phải tiếng Việt: "EShop" (logo navbar, footer), "Email" (nhãn ô nhập; SRS cũng dùng từ này), "SUT" (footer). Ngoài trang, tiêu đề tab trình duyệt là "frontend-web" (O03). Sinh viên chấp nhận "EShop", "Email", "SUT"; tiêu đề tab xử lý ở D04 (xem mục 3.9) | `S0_01_form_dang_ky.png` |

### 4.3 Các ô nhập

Theo thứ tự từ trên xuống dưới trên form.

| # | Nhãn hiển thị (nguyên văn) | Có `*` cạnh nhãn? | Placeholder (nguyên văn) | Giá trị mặc định | Loại ô nhìn thấy được | Có biểu tượng hoặc nút nào trong ô? | Ảnh |
|---|---|---|---|---|---|---|---|
| O07 (Họ Tên) | Họ Tên | Không có | Không có | Không có (ô trống) | Ô chữ một dòng | Không có | `S0_01_form_dang_ky.png` |
| O08 (Email) | Email | Không có | Không có | Không có (ô trống) | Ô chữ một dòng | Không có | `S0_01_form_dang_ky.png` |
| O09 (Mật khẩu) | Mật khẩu | Không có | Không có | Không có (ô trống) | Ô chữ một dòng | Không có | `S0_01_form_dang_ky.png` |
| O10 (Xác nhận mật khẩu) | Không có ô này trên form | | | | | | `S0_01_form_dang_ky.png` |
| O11 (trường khác) | Không có. Form chỉ có 3 ô: Họ Tên, Email, Mật khẩu | | | | | | `S0_01_form_dang_ky.png` |

### 4.4 Nút và liên kết

| # | Nhãn (nguyên văn) | Loại | Màu nền và màu chữ | Vị trí trên form | Ảnh |
|---|---|---|---|---|---|
| O12 (nút submit) | Đăng Ký | Nút | Nền đỏ, chữ trắng | Ngay dưới dòng "Yêu cầu: ...", rộng bằng ô nhập | `S0_01_form_dang_ky.png` |
| O13 (liên kết sang Đăng nhập) | Đã có tài khoản? Đăng nhập | Liên kết (chỉ phần "Đăng nhập") | "Đã có tài khoản?" chữ đen; "Đăng nhập" chữ xanh dương; không có nền | Dưới nút "Đăng Ký", căn giữa | `S0_01_form_dang_ky.png` |
| O14 (nút/liên kết khác) | Không có nút hay liên kết nào khác trong khung form | | | | `S0_01_form_dang_ky.png` |

### 4.5 Ảnh đã chụp

| Tên file | Nội dung |
|---|---|
| `S0_01_form_dang_ky.png` | Toàn bộ cửa sổ trình duyệt ở trang Đăng ký (`localhost:5173/register`) khi vừa mở, chưa nhập gì; thấy tiêu đề tab và thanh địa chỉ |
| `S0_02_duong_vao_trang_1.png` | Góc phải navbar với 3 mục "Giỏ hàng", "Đăng nhập", "Đăng ký"; không mục nào có kiểu hiển thị khác các mục còn lại |
| `S0_03_duong_vao_trang_2.png` | Toàn bộ cửa sổ trình duyệt ở trang Đăng nhập (`localhost:5173/login`), có liên kết "Đăng ký ngay"; thấy tiêu đề tab và thanh địa chỉ |

### 4.6 Các chỗ AI đã sửa so với bản sinh viên điền

| # | Sinh viên ghi | Đã sửa thành | Lý do |
|---|---|---|---|
| O01 | "nút Đang Ký trên navbar", "nút Đăng ký ngay ở trang Đăng nhập" | Mục "Đăng ký" trên navbar; liên kết "Đăng ký ngay" sau "Chưa có tài khoản?" | Ảnh: Navbar ghi "Đăng ký" (chữ k thường); "Đăng ký ngay" là liên kết chữ xanh, không phải nút |
| O03 | "EShop" (xuống dòng làm vỡ bảng) | "frontend-web" | Ảnh chụp lại (`S0_01`, `S0_03`) thấy thanh tab ghi "frontend-web"; "EShop" là chữ logo trên navbar |
| O04 | "EShop, Đăng Ký Tài Khoản, Họ Tên, Email, Mật khẩu" | Tiêu đề form "Đăng Ký Tài Khoản"; logo navbar "EShop" | "Họ Tên", "Email", "Mật khẩu" là nhãn ô nhập, đã ghi ở O07 đến O09 |
| O05 | Chỉ có dòng "Yêu cầu: ..." | Thêm vị trí, kiểu chữ; thêm chữ trên navbar và footer | Ảnh `S0_01` |
| O06 | "Không có" | Liệt kê "EShop", "Email", "SUT" | Ảnh có các từ này; không kết luận vi phạm |
| O07 đến O09 | "Ô chữ" | "Ô chữ một dòng"; giá trị mặc định ghi "Không có (ô trống)" | Ghi rõ hơn, nội dung không đổi |
| O10 | "KHÔNG CÓ Ô NÀY" | "Không có ô này trên form" | Chỉ đổi cách viết, nội dung không đổi |
| O11 | Để trống | "Không có" | Ảnh: Form chỉ có 3 ô |
| O12 | Vị trí "Dưới dòng Yêu cầu" | Thêm "rộng bằng ô nhập" | Ảnh `S0_01` |
| O13 | "Dưới nút Đăng ký"; "màu xanh biển" | "Dưới nút "Đăng Ký""; "xanh dương"; ghi rõ chỉ "Đăng nhập" là liên kết | Nút ghi "Đăng Ký" (chữ K hoa); "xanh dương" là chữ FR-21 dùng |
| O14 | Dòng bị xóa | Khôi phục, ghi "Không có" | Giữ đủ mã quan sát để truy vết |
| Cột Ảnh | Để trống | Điền tên ảnh cho từng dòng | WORKFLOW mục 3.1 |

---

## 5. Khác biệt giữa giao diện và đặc tả

### 5.1 Trong phạm vi FR-01

Đây là khác biệt nhìn thấy được ở S0, **chưa phải kết luận bug**. Xác nhận và ghi kết quả thực tế ở S6, báo bug ở S7.

| Mã | Yêu cầu | Đặc tả | Quan sát | Căn cứ |
|---|---|---|---|---|
| D01 | FR01-R11 | Phải có trường Xác nhận mật khẩu | Form chỉ có 3 ô: Họ Tên, Email, Mật khẩu | O10, `S0_01_form_dang_ky.png` |
| D02 | FR01-R18 | Mọi trường bắt buộc có ký hiệu `*` bên cạnh nhãn | Không nhãn nào có `*`, trong khi Họ Tên, Email, Mật khẩu là bắt buộc theo FR01-R01 đến FR01-R03 | O07 đến O09, `S0_01_form_dang_ky.png` |
| D03 | FR01-R15 | Nút hành động tích cực (Submit) dùng màu xanh dương | Nút "Đăng Ký" nền đỏ, chữ trắng | O12, `S0_01_form_dang_ky.png` |
| D04 | FR01-R14 | Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn) | Tiêu đề tab trình duyệt là "frontend-web", không phải tiếng Việt và không mô tả trang. Sinh viên xác định đây là ứng viên bug về ngôn ngữ (mục 3.9) | O03, `S0_01_form_dang_ky.png` |

### 5.2 Ngoài phạm vi FR-01 (chỉ ghi lại để tham khảo)

Trang Đăng nhập (`localhost:5173/login`, ảnh `S0_03_duong_vao_trang_2.png`) thuộc FR-02 và FR-21, không xử lý trong feature này. Những điểm nhìn thấy: Tiêu đề form là "Đăng Ký"; nhãn ô đầu tiên là "Username" (FR-02 nói người dùng nhập Email); nút submit là "Sign In" (tiếng Anh). Điểm này chỉ ảnh hưởng tới FR-01 qua câu hỏi Q27.

---

## 6. Thay đổi so với bản AI

Bản AI của S0 là `ai_raw/S0_khao_sat.md` (lần đầu) và `ai_raw/S0_khao_sat_v2.md` (sửa lần 1). Phạm vi của bảng:

- Việc sinh viên điền bảng quan sát (mục 4) là đầu vào theo quy trình S0, không phải sửa bản AI. Các chỗ AI sửa lại trên bản sinh viên điền đã ghi ở mục 4.6.
- Mục 3.8, 4.6 và 5 do AI viết ở bước 3 của S0 (đối chiếu ảnh), không phải phần sinh viên sửa.

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 3 (Q01, Q05, Q08, Q12, Q25); mục 4 (phần mở đầu, mục đếm `<h1>`, bảng ô nhập, danh sách ảnh) | Bỏ mọi chỗ yêu cầu xem thuộc tính HTML (`type`, `required`, `minlength`/`maxlength`, `pattern`), đếm thẻ `<h1>` bằng DevTools, và 5 ảnh chụp DevTools. Bản sửa lưu ở `ai_raw/S0_khao_sat_v2.md` | Thừa | Vi phạm WORKFLOW mục 1.1 và 3.1: Thuộc tính HTML là quy tắc do lập trình viên cài, không thuộc đặc tả; S0 chỉ quan sát bằng mắt. Sinh viên phát hiện khi review |
| Mục 3.8, Q24 | Đóng câu hỏi: Trong khung form có đúng 1 nút "Đăng Ký" và 1 liên kết "Đăng nhập", không có nút hủy bỏ | Quyết định của SV | Sinh viên quan sát giao diện (O12 đến O14) |
| Mục 3.8, 3.9, Q26 | Vẫn đưa trường Xác nhận mật khẩu vào thiết kế từ S1 đến S4 dù giao diện không có | Quyết định của SV | Test case thiết kế từ đặc tả (FR01-R11, FR01-R12) |
| Mục 3.8, 3.9, Q27 | Dấu hiệu xác nhận đã chuyển tới trang Đăng nhập: Đường dẫn đổi thành `/login` và trang hiện form đăng nhập; không dựa vào chữ trên trang đó | Quyết định của SV | Chữ trên trang `/login` thuộc FR-02 và FR-21, không thuộc FR-01 |
| Mục 3.9, O06 | Chấp nhận "EShop", "Email"; "SUT" chấp nhận, nếu khắt khe chỉ ghi chú | Quyết định của SV | Chốt cách hiểu "thuật ngữ kỹ thuật chuẩn" (FR-21) |
| Mục 3.9, mục 5.1 (D04) | Tiêu đề tab "frontend-web" là ứng viên bug về ngôn ngữ | Quyết định của SV | Không phải tiếng Việt, không mô tả nội dung trang (FR01-R14) |
| Mục 4.5 | Ảnh đường vào trang chụp thành 2 file `S0_02_duong_vao_trang_1.png` (navbar) và `S0_03_duong_vao_trang_2.png` (trang Đăng nhập), thay cho một file `S0_02_duong_vao_trang.png` như bản AI đề xuất | Quyết định của SV | Đường vào trang có 2 nơi khác nhau |
