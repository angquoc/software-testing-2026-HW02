# S3: Chọn test case

Theo Step 3 của slide S04: Chọn ít nhất một test case cho mỗi lớp; test case hợp lệ phủ càng nhiều lớp hợp lệ càng tốt; mỗi test case không hợp lệ chỉ phủ đúng một lớp không hợp lệ. Lập bảng phủ lớp (Test Cases Providing Coverage of Partitions) và bộ test case được chọn (Minimum Set).

**Đầu ra:** `ai_raw/S3_test_cases.md`, `03_tc.md`.

## Hỏi trước khi viết

Ba câu sau quyết định cấu trúc cả bản; hỏi trước, vì `ai_raw/` không sửa được:

1. **Cách thực thi:** Chỉ qua giao diện, hay thêm nhóm qua API? Đề xuất: Giao diện là chính, thêm nhóm API nhỏ cho các lớp mà giao diện, trình duyệt hay nền tảng có thể chặn hoặc sửa giá trị trước khi gửi (xem `platforms.md`), để biết hệ thống có tự kiểm tra lại không.
2. **Lớp không thực thi được** (trường đặc tả yêu cầu mà giao diện không có, API spec không mô tả): Viết đủ test case và ghi dự kiến Blocked, hay gộp thành một test case kiểm sự tồn tại của trường.
3. **Trình bày:** Markdown ở S3, S4, xuất Word và Excel bằng `test-case-writing` ở S5; hay dùng skill đó ngay.

## 1. Quy ước

- Mã test case `TC-<MÔĐUN>-NN`, chia dải theo nhóm, chừa khoảng trống (ví dụ 01 đến 29 hợp lệ, 30 đến 69 không hợp lệ, 70 đến 89 API, 90 đến 99 checklist, 100 trở đi cho S4).
- **Giá trị cơ sở** cho mỗi input: Một giá trị hợp lệ bình thường, dùng cho các input không phải đối tượng của test case.
- Dữ liệu có tính duy nhất (email, mã): Mỗi test case một giá trị riêng theo **một mẫu thống nhất** gắn với số test case (ví dụ `tcNN@domain.com`, `CODE_NN`), trừ khi chính giá trị đó là đối tượng test. Lý do: Lần tạo thành công trước sẽ làm test case sau bị lỗi trùng.
- `␣` cho dấu cách; chuỗi dài viết dạng "`x` + N chữ `a`".
- Tiền điều kiện chung, quy trình chung, cách đọc từng Output: Viết một lần ở đầu.

## 2. Test case hợp lệ

- **TC cơ sở:** Một test case gộp mọi lớp hợp lệ **cơ sở** (happy path).
- **Mỗi lớp hợp lệ bất thường một test case riêng** (lớp không phải giá trị cơ sở, dễ bị xử lý sai: Ký tự đặc biệt, Unicode, khoảng trắng, định dạng hiếm). Các input còn lại lấy giá trị cơ sở. Lý do: Quy tắc "phủ càng nhiều càng tốt" của slide cho số test case tối thiểu, nhưng gộp nhiều lớp bất thường thì khi thất bại không biết lớp nào gây lỗi (tiêu chí "không quá phức tạp" của Kaner). Không thiết kế theo kiểu "lỗi rồi mới tách".
- **Giá trị rủi ro thấp** cần thử đủ (ví dụ từng phần tử của một tập giá trị được giữ chung một lớp): Có thể xoay vòng vào các test case hợp lệ khác, nhưng không gắn vào test case rủi ro cao.

## 3. Test case không hợp lệ

- Mỗi test case chỉ có **một** input thuộc lớp không hợp lệ; các input khác lấy giá trị cơ sở. Với trường có trường đi kèm (ví dụ xác nhận mật khẩu), chỉnh trường đi kèm sao cho không phát sinh lỗi thứ hai.
- Lớp không thể có đại diện chỉ vi phạm một lớp (đã ghi ở S2): Ghi rõ là **ngoại lệ** và mục đích duy nhất của test case.
- Test case cần dữ liệu có sẵn: Tự tạo dữ liệu trong các bước của chính nó (ví dụ bước 1 tạo, bước 2 tạo trùng), không phụ thuộc test case khác.

## 4. Nhóm API (nếu có)

- Chọn lớp mà phía giao diện có thể chặn hoặc sửa giá trị trước khi gửi: Bắt buộc cung cấp, định dạng, độ mạnh, khoảng trắng của trường bị chuẩn hóa bởi trình duyệt hoặc nền tảng.
- Kết quả mong đợi khi thất bại: Đặc tả thường không nêu mã HTTP, nên ghi "không trả về phản hồi thành công", ghi lại mã và body thực tế ở S6.
- Lớp mà kết quả qua API khác qua giao diện (ví dụ phụ thuộc trình duyệt chuyển đổi giá trị): Ghi rõ chỉ test qua đường nào.
- Không tự đoán tên trường mà API spec không mô tả.

## 5. Test case bảo mật

- Chỉ thêm khi sinh viên đồng ý; mỗi test case nêu yêu cầu bảo mật và cách kiểm chứng **trong phạm vi feature** (ví dụ lưu chuỗi có dấu nháy rồi tạo lại đúng chuỗi đó để thấy lỗi trùng; sau chuỗi tấn công vẫn tạo trùng được dữ liệu mẫu).
- **Test case có thể phá dữ liệu** (chuỗi SQL injection có lệnh xóa, thao tác xóa hàng loạt): **Chạy cuối cùng** trong đợt test và **reset dữ liệu ngay sau đó**. Nếu kết quả bất thường, ghi kết quả rồi reset trước khi chạy lại bất kỳ test case nào. Lý do: Dữ liệu bị hỏng làm sai kết quả mọi test case chạy sau, dẫn tới ghi nhận bug không có thật.
- Bước kiểm chứng nên chạy qua đường cho thấy được **nguyên nhân** (thường là giao diện), vì API spec hiếm khi nêu nội dung lỗi.

## 6. Checklist giao diện

Yêu cầu tĩnh đã tách ở S1: Mỗi yêu cầu một dòng (điểm kiểm tra, kết quả mong đợi, cách kiểm tra). Mục nào cần DevTools thì ghi "DevTools ở S6".

## 7. Giới hạn quan sát

- Kết quả thành công chỉ chứng minh hệ thống **chấp nhận**. Với mỗi test case mà điều cần kiểm là **dữ liệu được lưu thế nào**, ghi rõ: Kiểm chứng được bằng cách nào trong feature (thêm bước), hay không quan sát được và vì sao.
- Rủi ro không kiểm được trong feature (ví dụ khoảng trắng của mật khẩu chỉ kiểm được khi đăng nhập): Ghi thành giới hạn, chuyển cho S8 hoặc feature liên quan.
- Kết quả qua giao diện có thể phản ánh hành vi của trình duyệt chứ không phải hệ thống (`platforms.md`): Ghi chú và kiểm thêm qua API.

## 8. Bảng phủ lớp và ma trận truy vết

- **Bảng phủ lớp:** Mỗi lớp (Input và Output) một dòng, ghi test case phủ. Không lớp nào trống.
- **Ma trận truy vết:** Mỗi yêu cầu `FRxx-Rnn` một dòng: Test case phủ, mức phủ (Đủ; Đủ trên thiết kế, dự kiến Blocked; Một phần, kèm lý do; Chưa phủ, kèm lý do). Cuối bảng liệt kê yêu cầu chưa phủ đủ.
- Kiểm bằng script: `check_step.py coverage`.

## 9. Thứ tự chạy

Ghi các bước: Reset dữ liệu; chạy các test case bình thường (nêu test case nào cần dữ liệu mẫu chưa bị sửa); chạy test case phá dữ liệu cuối cùng; reset ngay sau đó. Với trường ngày giờ, ghi ngày chạy vì kết quả phụ thuộc thời điểm.

## 10. Nếu đánh số lại khi review

Thêm bảng đổi mã (mã trong bản AI, mã trong bản review, ghi chú) để truy vết về `ai_raw/`.

## 11. Điểm cần sinh viên quyết định (gợi ý)

Cách ghép lớp trong test case hợp lệ; số đại diện cho lớp có nhiều đại diện; áp bước kiểm chứng tác động cho nhóm nào; nhóm API đủ chưa, có thêm test case bảo mật không; checklist để ở S3 hay S5.

## 12. Ghi chú cho bước sau

Ghi cho S4: Các biên đã hẹn (từ S2); giá trị đại diện đang nằm giữa lớp mà S4 cần xét biên; đường thực thi (giao diện hay API) cho từng loại biên.
