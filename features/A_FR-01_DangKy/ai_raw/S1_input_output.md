# S1: Xác định biến Input và Output (FR-01 Đăng ký tài khoản)

- Bước: S1 (Xác định biến Input và Output, theo Step 1 của slide S04)
- Thời gian tạo: 2026-10-19 22:26 (+07:00)
- Căn cứ: `00_spec.md` (yêu cầu FR01-R01 đến FR01-R25, câu hỏi mở, quyết định của sinh viên ở mục 3.9)

---

## 1. Cách xác định

Theo slide S04, Step 1 dựa trên đặc tả: Input là mọi thứ ảnh hưởng tới kết quả của chức năng, Output là mọi kết quả quan sát được, gồm cả thông báo lỗi. Theo WORKFLOW mục 3.2, Input gồm cả yếu tố không nhập trực tiếp (dữ liệu đã có, trạng thái hệ thống, người thao tác).

Ở bước này chỉ xác định **biến** và **các ràng buộc đặc tả đặt lên biến**. Việc chia lớp tương đương để tới S2.

---

## 2. Biến Input

### 2.1 Input nhập trực tiếp trên form

| Mã | Biến | Tên trên giao diện | Trường API tương ứng | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|
| IN1 | Họ Tên | "Họ Tên" (O07) | `name` | Bắt buộc cung cấp | FR01-R01 |
| IN2 | Email | "Email" (O08) | `email` | Bắt buộc cung cấp; đúng định dạng (`user@domain.com`); duy nhất trong hệ thống (so với IN5) | FR01-R02, FR01-R04, FR01-R05 |
| IN3 | Mật khẩu | "Mật khẩu" (O09) | `password` | Bắt buộc cung cấp; tối thiểu 8 ký tự; có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt trong tập `@ $ ! % * ? &` | FR01-R03, FR01-R06 đến FR01-R10 |
| IN4 | Xác nhận mật khẩu | Không có trên giao diện (D01). Dùng tên theo đặc tả | Không có trong API spec (Q15) | Phải khớp với IN3 | FR01-R11, FR01-R12 |

Ghi chú:

- IN4 được giữ theo quyết định Q26: Thiết kế từ đặc tả, dù giao diện hiện không có trường này.
- IN4 không có ràng buộc riêng về nội dung; ràng buộc duy nhất là quan hệ với IN3 ("khớp"). Đặc tả không nói IN4 có bắt buộc riêng hay không (Q13), và không định nghĩa "khớp" chính xác tới mức nào (Q14).
- Các ràng buộc chưa có trong đặc tả, sẽ phải đặt giả định ở S2: Độ dài và tập ký tự của Họ Tên (Q01 đến Q03); quy tắc định dạng email cụ thể, độ dài tối đa, phân biệt hoa thường khi so trùng, xử lý khoảng trắng đầu cuối (Q04 đến Q07); độ dài tối đa mật khẩu, tập ký tự đặc biệt là đóng hay mở, ký tự ngoài 4 loại, chữ có dấu (Q08 đến Q11).

### 2.2 Input không nhập trực tiếp

| Mã | Biến | Mô tả | Ảnh hưởng tới | Yêu cầu |
|---|---|---|---|---|
| IN5 | Danh sách email đã có trong hệ thống | Dữ liệu có sẵn trước khi đăng ký. Dữ liệu mẫu có ít nhất `admin@eshop.com` và `test@eshop.com` (SRS mục 1). Danh sách thay đổi sau mỗi lần đăng ký thành công | Kết quả kiểm tra email duy nhất của IN2 | FR01-R05 |
| IN6 | Trạng thái đăng nhập của người thao tác | Chưa đăng nhập, hoặc đang đăng nhập bằng một tài khoản | Đặc tả không ràng buộc (Q20). Chỉ là ứng viên, xem mục 5 | Không có |

### 2.3 Sự kiện kích hoạt

Hành động gửi form bằng nút "Đăng Ký" (O12), hoặc gửi request `POST /api/register` nếu ở S3 quyết định test qua API. Đây là sự kiện để hệ thống xử lý, không phải biến có miền giá trị, nên không chia lớp.

---

## 3. Biến Output

### 3.1 Bảng Output

| Mã | Output | Khi nào xảy ra | Dấu hiệu quan sát được | Yêu cầu |
|---|---|---|---|---|
| OUT1 | Đăng ký thành công | Mọi input thỏa ràng buộc | (1) Đường dẫn trên thanh địa chỉ đổi thành `/login`; (2) Trang hiển thị form đăng nhập (có ô nhập và nút gửi) (theo Q27). Hệ quả: Email vừa dùng được thêm vào IN5 | FR01-R13 |
| OUT2 | Đăng ký bị từ chối, kèm thông báo lỗi | Có ít nhất một input vi phạm ràng buộc | Có thông báo lỗi; vẫn ở trang Đăng ký (`/register`); không có tài khoản mới được tạo | FR01-R01 đến FR01-R12 |
| OUT3 | Phản hồi API khi thành công | Chỉ khi test qua API (quyết định ở S3) | HTTP 200 OK, body `{"message": "User registered successfully", "id": <số>}` | FR01-R22 |
| OUT4 | Phản hồi API khi thất bại | Chỉ khi test qua API | Đặc tả không nêu mã HTTP và nội dung (Q21) | Không có |

### 3.2 Các loại thông báo lỗi của OUT2

Đặc tả không nêu câu chữ của thông báo lỗi nào (Q16). Bảng dưới đây chỉ chia theo **nguyên nhân bị từ chối** mà đặc tả xác định; nội dung chính xác sẽ ghi ở S6.

| Mã | Nguyên nhân bị từ chối | Biến gây ra | Yêu cầu |
|---|---|---|---|
| ERR1 | Thiếu Họ Tên | IN1 | FR01-R01 |
| ERR2 | Thiếu Email | IN2 | FR01-R02 |
| ERR3 | Email sai định dạng | IN2 | FR01-R04 |
| ERR4 | Email đã tồn tại | IN2, IN5 | FR01-R05 |
| ERR5 | Thiếu Mật khẩu | IN3 | FR01-R03 |
| ERR6 | Mật khẩu không đạt yêu cầu mạnh (thiếu độ dài, chữ hoa, chữ thường, chữ số hoặc ký tự đặc biệt) | IN3 | FR01-R06 đến FR01-R10 |
| ERR7 | Mật khẩu và Xác nhận mật khẩu không khớp | IN3, IN4 | FR01-R12 |

Ghi chú:

- ERR6 gộp 5 điều kiện vì đặc tả gọi chung là "Yêu cầu mật khẩu mạnh" và không nói mỗi điều kiện có thông báo riêng. Có tách thành 5 loại hay không, xem mục 5.
- Không có loại lỗi riêng cho "thiếu Xác nhận mật khẩu" vì đặc tả không nêu (Q13). Khi IN3 có giá trị mà IN4 để trống, theo đặc tả đó là trường hợp "không khớp" (ERR7). Cách xử lý chính thức sẽ chốt ở S2.

### 3.3 Thuộc tính của thông báo lỗi

| Thuộc tính | Đặc tả nói gì | Yêu cầu |
|---|---|---|
| Vị trí | Phải nằm **trên** nút submit ("Đăng Ký") | FR01-R21 |
| Nội dung | Không nêu (Q16) | Không có |
| Số lượng khi nhiều input cùng sai | Không nêu (Q17) | Không có |
| Dữ liệu đã nhập có được giữ lại sau khi bị từ chối | Không nêu (Q19) | Không có |

---

## 4. Yêu cầu không mô hình hóa thành biến Input/Output

Các yêu cầu sau là thuộc tính tĩnh của trang, không phụ thuộc giá trị nhập, nên không có miền giá trị để chia lớp tương đương.

| Yêu cầu | Nội dung | Đề xuất xử lý |
|---|---|---|
| FR01-R14 | Giao diện dùng tiếng Việt | Kiểm tra dạng checklist trong nhóm phụ giao diện |
| FR01-R15 | Màu nút | Như trên |
| FR01-R16 | Đúng 1 thẻ `<h1>` | Như trên (kiểm tra bằng DevTools ở S6) |
| FR01-R17 | Thứ tự Tab | Như trên |
| FR01-R18 | Dấu `*` ở trường bắt buộc | Như trên |
| FR01-R19, FR01-R20 | `type="email"`, `type="password"` | Như trên (kiểm tra bằng DevTools ở S6) |
| FR01-R23 | Mật khẩu không lưu plaintext | Không quan sát được qua giao diện; chưa thuộc phạm vi |
| FR01-R25 | Parameterized Query | Không quan sát được trực tiếp; chốt ở S2 cùng câu hỏi về dữ liệu chứa ký tự đặc biệt |

FR01-R21 (vị trí thông báo lỗi) đã đưa vào thuộc tính của OUT2 ở mục 3.3. FR01-R24 (escape khi hiển thị) liên quan tới IN1 nếu Họ Tên được hiển thị lại ở đâu đó; chốt ở S2.

---

## 5. Điểm cần sinh viên quyết định khi review

| # | Vấn đề | Các lựa chọn |
|---|---|---|
| 1 | IN6 (trạng thái đăng nhập) có giữ làm biến Input không? Đặc tả FR-01 không ràng buộc | (a) Bỏ, ghi điều kiện "chưa đăng nhập" vào tiền điều kiện của mọi test case; (b) Giữ, ghi là ngoài đặc tả |
| 2 | OUT2 chia theo từng nguyên nhân (ERR1 đến ERR7) hay gộp thành một Output "thông báo lỗi" như ví dụ "Invalid Input" trong slide? | (a) Chia theo nguyên nhân, để kết quả mong đợi chỉ rõ input nào bị từ chối; (b) Gộp một loại |
| 3 | ERR6 có tách thành 5 loại theo FR01-R06 đến FR01-R10 không? | (a) Gộp, vì đặc tả gọi chung; (b) Tách 5 loại |
| 4 | Xác nhận "không có tài khoản mới được tạo" (OUT2) và "tài khoản đã được tạo" (OUT1) bằng cách nào? Đặc tả FR-01 chỉ nêu dấu hiệu chuyển trang | (a) Chỉ dùng dấu hiệu chuyển trang (Q27); (b) Thêm bước đăng nhập thử bằng email và mật khẩu vừa nhập (dùng FR-02); (c) Thêm bước đăng ký lại cùng email để xem có báo trùng không |
| 5 | Các yêu cầu ở mục 4 có kiểm tra thành nhóm checklist riêng (ngoài Domain Testing) như đề xuất không? | (a) Đồng ý; (b) Cách khác |
