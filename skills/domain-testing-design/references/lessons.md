# Bài học: Checklist tự kiểm trước khi giao

Rút từ các bảng "Thay đổi so với bản AI" của feature đầu tiên (FR-01 Đăng ký, EShop). Mỗi mục ghi lỗi đã gặp để hiểu vì sao có quy tắc. Đi qua checklist của bước đang làm **trước khi giao** bản AI và bản review.

## Chung cho mọi bước

- [ ] Đã đọc "Ghi chú cho bước sau" của mọi bước trước, và xử lý hết hoặc ghi lý do không xử lý.
  *Đã gặp:* S2 ghi biến thể "một ký tự có khoảng trắng hai bên" cho S4 xét; bản AI của S4 bỏ qua (loại Thiếu).
- [ ] Các quyết định ảnh hưởng tới cấu trúc cả bản đã được hỏi **trước** khi viết.
  *Đã gặp:* Ở S3, cách thực thi (giao diện hay API), cách xử lý lớp không thực thi được và cách trình bày quyết định toàn bộ cấu trúc; phải hỏi trước vì `ai_raw/` không sửa được.
- [ ] Không khẳng định quá căn cứ. Đặc tả "không mô tả" khác với hệ thống "không có".
  *Đã gặp:* "API không có trường xác nhận mật khẩu" trong khi API spec chỉ không mô tả trường đó (loại Thừa).
- [ ] Chỗ đặc tả không nói đã thành câu hỏi mở hoặc giả định có phương án; AI không tự chọn.
- [ ] Mọi lập luận dựa trên giả định đã được kiểm lại theo **phương án sinh viên đã chọn**, không theo phương án mặc định trong đầu.
  *Đã gặp:* Lập luận "ký tự SQL làm email sai định dạng" đúng với chuẩn email chặt, nhưng sai với quy tắc HTML5 mà sinh viên chọn (dấu nháy đơn vẫn hợp lệ) (loại Sai).
- [ ] Đã xét môi trường thực thi (trình duyệt, nền tảng) có làm thay đổi giá trị trước khi tới hệ thống không (`platforms.md`).
  *Đã gặp:* Ô `type="email"` tự cắt khoảng trắng nên test case khoảng trắng qua giao diện chỉ kiểm trình duyệt; một test case biên trùng với test case "rỗng" (loại Thiếu, Thừa).
- [ ] Đếm, đánh mã, tham chiếu bằng `scripts/check_step.py`, không đếm tay.
  *Đã gặp:* Hai lần ghi sai tổng số lớp và sai bảng đổi mã, phát hiện nhờ script.
- [ ] Giá trị có dấu cách dùng ký hiệu `␣`.
  *Đã gặp:* Markdown làm mất dấu cách ở hai đầu đoạn code, đại diện của lớp "khoảng trắng đầu cuối" hiển thị như giá trị bình thường.
- [ ] Bảng thay đổi ghi đúng loại và **đúng người phát hiện** theo thông tin sinh viên cung cấp; không rõ thì hỏi.
  *Đã gặp:* Ghi "sinh viên phát hiện" cho điểm do một phiên AI khác phát hiện; sinh viên phải sửa lại.
- [ ] Đã kiểm tra mâu thuẫn giữa các quyết định của sinh viên (bản review).
  *Đã gặp:* Quyết định "giữ 2 test case biên qua API" vướng với việc chuyển một test case khác sang API.

## S0

- [ ] Bảng quan sát và câu hỏi mở không có mục nào cần DevTools hay phải nhập dữ liệu.
  *Đã gặp:* Bản đầu hỏi `type`, `required`, `maxlength`, số thẻ `<h1>` và yêu cầu 5 ảnh DevTools; phải làm bản `_v2` (loại Thừa).
- [ ] Trước khi đối chiếu, đã kiểm tra ảnh đủ chưa (thấy thanh tab, không bị cắt, đúng màn hình); thiếu thì yêu cầu chụp thêm.
  *Đã gặp:* Ảnh đầu không thấy thanh tab; giá trị sinh viên ghi cho tiêu đề tab sai, chỉ phát hiện sau khi chụp lại.
- [ ] Đã nhắc sinh viên commit bản điền tay trước khi AI viết lại `00_spec.md`.
- [ ] Khác biệt giữa giao diện và đặc tả ghi là "chờ xác nhận ở S6", không kết luận bug.

## S1

- [ ] Có Input gián tiếp (dữ liệu có sẵn, trạng thái, vai trò, thời điểm).
- [ ] Output lỗi chia theo nguyên nhân; không bịa câu chữ thông báo.
- [ ] Có cách kiểm chứng tác động trong phạm vi chính feature.
  *Đã gặp:* Đăng nhập thử để kiểm tài khoản đã tạo bị loại vì phụ thuộc feature khác; thay bằng tạo lại cùng khóa duy nhất.

## S2

- [ ] Mỗi chỗ tách lớp có lý do; không gộp hai nhóm có thể bị xử lý khác nhau.
  *Đã gặp:* Gộp "chữ số" và "dấu câu" của tên vào một lớp không có lý do (loại Thiếu).
- [ ] Đã hỏi hoặc đặt giả định cho cách xử lý khoảng trắng theo từng loại trường (đầu, cuối, giữa, chỉ khoảng trắng).
  *Đã gặp:* Phải bổ sung nhiều lớp khoảng trắng sau khi sinh viên chốt nguyên tắc (loại Thiếu).
- [ ] Khi dùng một chuẩn bên ngoài làm giả định, đã ghi lại quy tắc cụ thể và các hệ quả bất ngờ.
  *Đã gặp:* Quy tắc HTML5 cho email có giới hạn 63 ký tự mỗi nhãn tên miền và cho phép dấu chấm ở đầu phần trước `@`; bản AI chưa đưa vào (loại Thiếu).
- [ ] Có lớp Output; có "Ghi chú cho bước sau" với các cận và biến thể giá trị cho S4.

## S3

- [ ] Mỗi lớp có ít nhất một test case; mỗi test case không hợp lệ chỉ vi phạm một lớp không hợp lệ; ngoại lệ ghi rõ.
- [ ] Mỗi lớp hợp lệ bất thường có test case riêng; chỉ test case cơ sở gộp các lớp cơ sở.
  *Đã gặp:* Một test case hợp lệ gộp 3 lớp bất thường; sinh viên yêu cầu tách.
- [ ] Có ma trận truy vết yêu cầu, ghi rõ yêu cầu phủ một phần và lý do.
  *Đã gặp:* Không có ma trận nên không thấy một yêu cầu bảo mật chưa được phủ (loại Thiếu).
- [ ] Đã ghi giới hạn quan sát cho test case mà kết quả thành công không chứng minh được dữ liệu lưu đúng.
- [ ] Test case có thể phá dữ liệu chạy cuối, reset ngay sau đó.
  *Đã gặp:* Chuỗi `DROP TABLE` ban đầu không có ràng buộc thứ tự chạy (loại Thiếu).
- [ ] Dữ liệu test theo một mẫu thống nhất.
  *Đã gặp:* Vài email không theo mẫu `tcNN` mà không có lý do.

## S4

- [ ] Chỉ BVA cho phân vùng có thứ tự.
  *Đã gặp:* Tạo phân vùng "mức khác biệt" cho phép so khớp bằng nhau, trái với chính nguyên tắc của bản AI (loại Thừa).
- [ ] Không áp máy móc 9 điểm; không có điểm "giữa" khi phân vùng không có cận trên.
  *Đã gặp:* Thêm mật khẩu 20 ký tự làm "giữa", cùng lớp với 9 ký tự (loại Thừa).
- [ ] Mỗi điểm biên chỉ vi phạm một điều kiện.
  *Đã gặp:* Mật khẩu 1 ký tự vi phạm cùng lúc độ dài và 3 điều kiện loại ký tự (loại Thừa).
- [ ] Đã dùng lại test case có sẵn khi trùng điểm biên.
- [ ] Biên của giá trị bị môi trường biến đổi được tính trên dạng sau biến đổi, bằng công cụ chuẩn.
