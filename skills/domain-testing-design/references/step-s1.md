# S1: Xác định biến Input và Output

Theo Step 1 của slide S04: Dựa trên đặc tả, xác định mọi thứ ảnh hưởng tới kết quả (Input) và mọi kết quả quan sát được (Output, gồm cả thông báo lỗi). Bước này chỉ xác định **biến** và **ràng buộc đặc tả đặt lên biến**; chưa chia lớp.

**Đầu ra:** `ai_raw/S1_input_output.md`, `01_io.md`.

## Hỏi trước khi viết

- Trường mà đặc tả yêu cầu nhưng giao diện không có (từ `00_spec.md`): Có giữ làm biến Input theo đặc tả không? Đề xuất: Giữ, vì test case thiết kế từ đặc tả; ghi chú sẽ bị chặn khi chạy.
- Thao tác cần tiền điều kiện về quyền (đăng nhập, vai trò admin): Đây là tiền điều kiện chung hay biến Input? Thường là tiền điều kiện, vì kiểm soát truy cập thuộc feature khác.

## 1. Biến Input

### 1.1 Input nhập trực tiếp

| Mã | Biến | Tên trên giao diện | Trường API tương ứng | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|

- Tên trên giao diện lấy từ bảng quan sát (`Onn`), không lấy từ đặc tả nếu hai bên khác nhau.
- Trường API lấy từ API spec. Đặc tả API không mô tả trường nào thì ghi "Không có trong API spec", **không** viết "API không có trường này" (kiểm thử hộp đen không biết API thật nhận gì).
- Ràng buộc nào đặc tả không nêu: Ghi trỏ về câu hỏi mở (`Qnn`), để S2 đặt giả định.

### 1.2 Input không nhập trực tiếp

Dữ liệu đã có (bản ghi có sẵn, dữ liệu mẫu), trạng thái hệ thống, người thao tác (vai trò), thời điểm (với trường ngày giờ). Mỗi biến ghi ảnh hưởng tới yêu cầu nào. Biến không có ràng buộc trong đặc tả: Ghi là ứng viên, để sinh viên quyết định giữ hay chuyển thành tiền điều kiện.

### 1.3 Sự kiện kích hoạt

Nút gửi, thao tác vuốt, gọi API. Không phải biến, không chia lớp.

## 2. Biến Output

| Mã | Output | Khi nào xảy ra | Dấu hiệu quan sát được | Yêu cầu |
|---|---|---|---|---|

- **Thành công:** Dấu hiệu phải quan sát được và thuộc chính feature này (đường dẫn đổi, thông báo, bản ghi xuất hiện trong danh sách của chính màn hình). Không dựa vào chữ trên màn hình của feature khác.
- **Bị từ chối:** Chia **loại lỗi theo nguyên nhân** mà đặc tả xác định (`ERRn`). Đặc tả không nêu câu chữ thông báo thì kết quả mong đợi chỉ ghi nguyên nhân, không bịa câu chữ.
- **Phản hồi API:** Thành công theo API spec; thất bại thường không được đặc tả nêu, ghi trỏ về câu hỏi mở.
- **Thuộc tính của thông báo lỗi:** Vị trí, nội dung, số lượng khi nhiều lỗi, dữ liệu có được giữ lại. Mục nào đặc tả không nói thì trỏ về câu hỏi mở.

## 3. Cách kiểm chứng tác động

Kết quả "thành công" chỉ chứng minh hệ thống **chấp nhận**; chưa chứng minh dữ liệu đã được tạo, sửa, xóa đúng hay được lưu ở dạng nào. Đề xuất cách kiểm chứng **trong phạm vi chính feature**, không dựa vào feature khác (để khi lỗi thì biết lỗi thuộc feature nào):

| Tác động cần kiểm chứng | Cách thường dùng |
|---|---|
| Bản ghi đã được tạo | Tạo lại với cùng giá trị khóa duy nhất, mong đợi lỗi trùng; hoặc bản ghi xuất hiện trong danh sách của chính màn hình |
| Bản ghi chưa được tạo (khi bị từ chối) | Tạo lại với cùng khóa và dữ liệu hợp lệ, mong đợi thành công |
| Dữ liệu được lưu ở dạng nào (đã cắt khoảng trắng, đã chuẩn hóa) | Tạo lại với dạng đã chuẩn hóa, mong đợi lỗi trùng; hoặc xem trên chính màn hình nếu có hiển thị lại |
| Bản ghi đã bị xóa | Không còn trong danh sách; tạo lại cùng khóa thành công |

Cách nào cần feature khác (đăng nhập thử, xem ở trang khác): Nêu ra như một phương án, ghi rõ phụ thuộc, để sinh viên chọn.

## 4. Yêu cầu không mô hình hóa thành biến

Yêu cầu là thuộc tính tĩnh của màn hình (ngôn ngữ, màu nút, số thẻ tiêu đề, dấu `*`, thứ tự Tab, loại ô nhập): Không có miền giá trị để chia lớp. Đề xuất kiểm tra thành nhóm checklist riêng, ngoài Domain Testing.

## 5. Điểm cần sinh viên quyết định (gợi ý)

- Giữ hay bỏ từng Input gián tiếp không có ràng buộc trong đặc tả.
- Chia Output lỗi theo nguyên nhân hay gộp một loại.
- Gộp hay tách các điều kiện cùng nhóm ở phía Output (ví dụ các điều kiện độ mạnh mật khẩu). Lưu ý: Gộp ở Output không có nghĩa là gộp ở Input; phía Input vẫn có thể tách lớp riêng ở S2.
- Cách kiểm chứng tác động (mục 3).
- Nhóm checklist (mục 4).

## 6. Ghi chú cho bước sau

Ghi cho S2: Các câu hỏi mở sẽ thành giả định; biến có ràng buộc độ dài, tập giá trị, định dạng; tiền điều kiện chung đã chốt.
