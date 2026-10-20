# S2: Chia lớp tương đương

Theo Step 2 của slide S04: Hai giá trị thuộc cùng một lớp nếu kết quả mong đợi giống nhau; chạy nhiều test case trong cùng một lớp là thừa. Bước này lập **Complete Set of Partitions** cho mọi biến Input và Output.

**Đầu ra:** `ai_raw/S2_equivalence_classes.md`, `02_ec.md`.

## Hỏi trước khi viết

Những câu sau thường quyết định cấu trúc của cả bảng lớp. Hỏi trước nếu đặc tả không nói và sinh viên chưa chốt ở bước trước:

- **Nguyên tắc khoảng trắng theo loại trường:** Trường định danh (tên, email, mã) có cắt khoảng trắng đầu cuối không, chỉ khoảng trắng có tính như rỗng không, khoảng trắng ở giữa có được chuẩn hóa không. Trường bí mật (mật khẩu) có cắt không, khoảng trắng có tính vào độ dài không.
- **Chuẩn định dạng** cho trường có định dạng (email, số điện thoại, ngày): Theo ví dụ của đặc tả, theo chuẩn chung, hay theo hành vi của loại ô nhập mà đặc tả yêu cầu.
- **Phân biệt hoa thường** khi so trùng.

Nếu sinh viên muốn để AI đề xuất trước, ghi các điểm này thành giả định có phương án (mục "Giả định") thay vì hỏi.

## 1. Guideline của slide

| Guideline | Lớp |
|---|---|
| Khoảng giá trị ("từ 1 đến 999") | 1 lớp hợp lệ, 2 lớp không hợp lệ (dưới, trên). Chỉ có một cận thì chỉ có 1 lớp không hợp lệ |
| Số lượng giá trị ("từ 1 đến 6 chủ sở hữu") | 1 lớp hợp lệ, 2 lớp không hợp lệ (không có, quá nhiều) |
| Tập giá trị, có lý do tin mỗi phần tử được xử lý khác nhau | Mỗi phần tử 1 lớp hợp lệ, cộng 1 lớp không hợp lệ (phần tử ngoài tập) |
| Điều kiện "must be" | 1 lớp hợp lệ, 1 lớp không hợp lệ |
| Có lý do tin các phần tử trong một lớp được xử lý khác nhau | Tách lớp |

## 2. Quy ước bảng lớp

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|

- **Loại:** H (hợp lệ), KH (không hợp lệ), GĐ (phụ thuộc giả định chưa chốt, ghi mã giả định). Loại xét **theo điều kiện của dòng đó**; một lớp có thể hợp lệ với điều kiện của nó nhưng đại diện vẫn vi phạm điều kiện khác (ghi rõ trong ghi chú).
- **Kết quả mong đợi:** Mã Output của S1. Lớp hợp lệ cho kết quả thành công khi mọi input khác cũng hợp lệ.
- **Đại diện:** Chỉ để minh họa; giá trị cụ thể chọn ở S3, S4. Dùng `␣` cho dấu cách.
- Mã lớp bổ sung khi review đánh số tiếp; không đánh số lại.

## 3. Khi nào tách lớp

Mỗi chỗ tách phải có **lý do tin rằng được xử lý khác nhau**, ghi ở cột cuối. Các lý do thường gặp:

| Lý do | Ví dụ lớp |
|---|---|
| Bước chuẩn hóa là một nhánh xử lý riêng | Có khoảng trắng đầu cuối; chỉ khoảng trắng; nhiều khoảng trắng liền nhau ở giữa |
| Ký tự ngoài ASCII có thể bị mã hóa, lưu, so sánh khác | Chữ tiếng Việt có dấu; Unicode khác |
| Hệ thống có thể có luật mà đặc tả không nêu | Chữ số trong tên; tên không có chữ cái; dấu câu thường gặp trong tên |
| Rủi ro bảo mật (risk-based equivalence) | Ký tự đặc biệt của HTML, SQL (`<`, `>`, `'`, `"`) ở trường được lưu và có thể hiển thị lại |
| Kiểm tra ở hai nơi (trình duyệt hoặc ứng dụng, và hệ thống) có thể bắt luật khác nhau | Mỗi luật định dạng một lớp không hợp lệ |
| Dữ liệu được tạo theo hai đường khác nhau | Trùng với dữ liệu mẫu; trùng với dữ liệu vừa tạo bằng chính chức năng |

Đừng gộp hai nhóm ký tự hay hai trường hợp vào một lớp chỉ vì chúng "cùng không phải chữ cái"; nếu một hệ thống có thể cho phép nhóm này mà cấm nhóm kia thì phải tách.

Không tách khi không có lý do (ví dụ tên viết toàn chữ thường, khi đặc tả không có điều kiện nào về hoa thường); ghi chú nó thuộc lớp nào.

## 4. Lớp Output

Theo slide (ví dụ "SUM" và "Invalid Input"), mỗi Output và mỗi loại lỗi là một lớp; ghi lớp Input nào dẫn tới nó.

## 5. Giả định

Theo mẫu ở `rules.md` mục 8. Mã giả định trùng số câu hỏi mở gốc. Mỗi phương án nêu rõ lớp nào thành H, KH. Lớp GĐ sẽ thành H hoặc KH sau khi sinh viên chốt; bản review phải không còn lớp GĐ, hoặc ghi rõ giả định nào còn mở.

Khi dùng một chuẩn bên ngoài làm giả định (ví dụ quy tắc `type="email"` của HTML): Ghi lại quy tắc cụ thể trong bản review, và kiểm tra các hệ quả bất ngờ (ví dụ chuẩn HTML cho phép dấu chấm ở đầu phần trước `@`, giới hạn 63 ký tự mỗi nhãn tên miền). Báo các hệ quả đó cho sinh viên.

## 6. Dữ liệu có rủi ro bảo mật

Xét riêng từng trường: Ký tự HTML, SQL có **đi tới được** bước lưu không (hay đã bị luật định dạng chặn)? Kiểm tra lập luận này theo **giả định đã chốt**, không theo cảm giác. Ghi giới hạn quan sát: Nếu màn hình không hiển thị lại dữ liệu, việc escape khi hiển thị không kiểm được trong feature này.

## 7. Tổng hợp

Bảng: Biến, lớp hợp lệ, lớp không hợp lệ, lớp phụ thuộc giả định; tổng số theo loại. **Đếm bằng script** (`check_step.py classes`), không đếm tay.

## 8. Ghi chú cho bước sau

Bắt buộc ghi cho S3, S4:

- Cận dưới, cận trên của từng trường có thứ tự (kể cả cận suy ra, ví dụ "phải cung cấp" nghĩa là tối thiểu 1 ký tự sau khi chuẩn hóa).
- Các biến thể giá trị cần xét tại biên (ví dụ một ký tự có khoảng trắng hai bên).
- Lớp không thể có đại diện chỉ vi phạm một điều kiện (ngoại lệ cho S3).
- Hệ quả của giả định lên cách thực thi (ví dụ phụ thuộc trình duyệt, khác nhau giữa giao diện và API).
