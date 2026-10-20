# Lưu ý theo nền tảng

Đặc tả mô tả hệ thống, nhưng giá trị sinh viên nhập phải đi qua **môi trường thực thi** (trình duyệt, ứng dụng di động, hệ điều hành) trước khi tới hệ thống. Môi trường có thể chặn, sửa hoặc chuyển đổi giá trị. Khi đó, test case qua giao diện có thể chỉ đang kiểm môi trường chứ không kiểm hệ thống.

Mọi điều dưới đây là hiểu biết chung về chuẩn và nền tảng, không phải thông tin lấy từ mã nguồn của hệ thống. Ghi rõ nguồn khi dùng; chỉ biết loại ô nhập thật sự là gì khi chạy ở S6.

## 1. Cách xử lý chung

1. Ở S2, S3, S4, với mỗi lớp hoặc biên, tự hỏi: Môi trường có thể chặn, sửa, chuyển đổi giá trị này trước khi gửi không?
2. Nếu có:
   - Ghi chú ở test case qua giao diện: "Kết quả phản ánh hành vi chung của môi trường và hệ thống".
   - Thêm test case qua đường không đi qua môi trường đó (thường là API), nếu sinh viên đồng ý.
   - Với biên: Tính trên dạng sau biến đổi; bỏ test case nếu sau biến đổi nó trùng test case khác.
3. Kết quả phụ thuộc môi trường: Ghi trình duyệt, thiết bị, phiên bản cần ghi lại ở S6.

## 2. Web

| Tình huống | Ảnh hưởng | Gợi ý |
|---|---|---|
| Ô `type="email"` (khi đặc tả yêu cầu) | Theo chuẩn HTML, trình duyệt cắt khoảng trắng đầu cuối, chặn gửi nếu sai định dạng HTML5 và hiện thông báo của chính trình duyệt; tên miền có dấu có thể được chuyển sang punycode | Test khoảng trắng và định dạng thêm qua API; tính biên nhãn tên miền trên dạng punycode |
| Ô `type="number"` | Trình duyệt có thể chặn ký tự không phải số, làm tròn theo bước nhảy, cho phép `e`, `-` | Test giá trị không phải số, số thập phân, số âm qua API |
| Ô ngày (`type="date"`) | Trình duyệt chỉ cho chọn ngày hợp lệ, định dạng hiển thị theo ngôn ngữ máy | Test ngày không hợp lệ, định dạng khác qua API; ghi ngày chạy |
| Ô `type="password"` | Chỉ bỏ ký tự xuống dòng, không cắt khoảng trắng | Test khoảng trắng của mật khẩu qua giao diện vẫn kiểm đúng hệ thống |
| Giới hạn số ký tự của ô | Chỉ biết khi chạy (không dùng DevTools khi thiết kế) | Dùng chuỗi dài để thăm dò; ghi số ký tự ô nhận ở S6 |
| Ảnh chụp ở S0 | Cần thấy tiêu đề tab và thanh địa chỉ | Chụp cả cửa sổ trình duyệt; có thể che thanh bookmark, ảnh đại diện |

## 3. Web Admin

Như Web, cộng thêm:

| Tình huống | Gợi ý |
|---|---|
| Phải đăng nhập admin | Ghi thành tiền điều kiện chung; quyền truy cập thuộc feature kiểm soát truy cập, không chia lớp ở đây trừ khi sinh viên muốn |
| Thao tác thêm, sửa, xóa làm thay đổi dữ liệu | Dữ liệu tạo ra phải có mẫu tên riêng theo test case; có thứ tự chạy; test case xóa hàng loạt hoặc có thể phá dữ liệu chạy cuối và reset ngay sau đó |
| Trường mã duy nhất | Kiểm chứng tạo thành công bằng tạo lại cùng mã; xét hoa thường và khoảng trắng khi so trùng |
| Trường ngày (hạn dùng, ngày bắt đầu) | Kết quả phụ thuộc thời điểm chạy: Biên tương đối theo ngày chạy (hôm qua, hôm nay, ngày mai); ghi ngày chạy ở S6 |
| Dropdown (loại, trạng thái) | Áp guideline "tập giá trị"; giá trị ngoài tập chỉ gửi được qua API |
| Trường số (giá trị, ngưỡng, số lần) | Phân vùng có thứ tự rõ ràng, áp BVA đầy đủ; xét số thập phân, số âm, số 0 qua cả giao diện và API |

## 4. Mobile

| Tình huống | Ảnh hưởng | Gợi ý |
|---|---|---|
| Không có DevTools | Thuộc tính ô nhập chỉ suy ra từ hành vi | Ở S0, được chạm vào ô để xem loại bàn phím (chữ, số, email, điện thoại) nhưng không gõ; ghi vào bảng quan sát |
| Bàn phím số, bàn phím điện thoại | Có thể không gõ được chữ, dấu cách, ký tự đặc biệt | Lớp chứa ký tự không gõ được: Ghi là không nhập được qua giao diện; kiểm qua API hoặc dán (paste) nếu ứng dụng cho phép |
| Tự viết hoa chữ đầu, tự sửa chính tả, gợi ý từ | Giá trị gửi đi có thể khác giá trị định gõ | Ghi chú tắt các tính năng này khi chạy, hoặc ghi lại giá trị thực tế trong ô trước khi gửi |
| Ứng dụng dùng chung hệ thống phía sau với Web | Có đường API để vượt qua ứng dụng | Dùng nhóm API như Web |
| Ảnh chụp | Ảnh từ điện thoại | Chụp đủ màn hình, kể cả khi bàn phím đang mở để thấy loại bàn phím; đặt tên theo quy ước `S0_NN_<nội dung>.png` |
| Chạy test | Kết quả phụ thuộc thiết bị và phiên bản hệ điều hành | Ghi tên thiết bị, phiên bản Android, phiên bản ứng dụng ở S6 |
