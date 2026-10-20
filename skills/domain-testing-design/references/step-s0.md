# S0: Trích đặc tả và khảo sát giao diện

**Mục tiêu:** Có một bản đặc tả của feature đủ để thiết kế: Yêu cầu trích nguyên văn, danh sách yêu cầu có mã để truy vết, câu hỏi mở, và những gì thực sự nhìn thấy trên giao diện (qua ảnh sinh viên chụp).

**Đầu ra:** `ai_raw/S0_khao_sat.md` (bản gốc của AI, giữ nguyên), `00_spec.md` (sinh viên điền rồi AI viết lại), `screenshots/S0_*.png`.

## Hỏi trước khi viết

- Phạm vi trích: Ngoài FR chính, có lấy các yêu cầu chung áp cho màn hình này (giao diện, form, điều hướng), yêu cầu API, yêu cầu bảo mật không? Đề xuất: Lấy FR chính làm trọng tâm, yêu cầu chung làm nhóm phụ, bảo mật ghi là "tham khảo" để S2 quyết định.
- Nền tảng và đường vào màn hình (đăng nhập với vai trò nào, qua menu nào).
- Màn hình có nhiều trạng thái không (danh sách và form thêm, form một bước hay nhiều bước, hộp thoại xác nhận)? Mỗi trạng thái cần ảnh riêng.

## Pha 1: AI viết bản gốc

### 1. Trích nguyên văn đặc tả

- Chép nguyên văn từng đoạn liên quan, ghi nguồn (file, mục). Giữ nguyên dấu câu, kể cả ký tự mà quy tắc định dạng không cho dùng; ghi chú "trích nguyên văn".
- Gồm: FR chính; dữ liệu mẫu liên quan (tài khoản, bản ghi có sẵn); yêu cầu chung áp cho màn hình; API tương ứng; yêu cầu bảo mật tham khảo.

### 2. Danh sách yêu cầu có mã

- Mã `FRxx-Rnn`, mỗi mã **một** điều kiện kiểm được (tách câu có nhiều điều kiện thành nhiều mã).
- Chia nhóm: Chính, phụ (giao diện chung), API, tham khảo (bảo mật).
- Yêu cầu chung **không áp dụng** cho màn hình này: Ghi rõ là không áp dụng và lý do.
- Yêu cầu không quan sát được bằng kiểm thử hộp đen: Ghi chú ngay.

### 3. Câu hỏi mở

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|

- Nhóm theo trường hoặc chủ đề.
- Hỏi mọi điểm đặc tả không nói mà ảnh hưởng tới kết quả: Độ dài tối thiểu, tối đa; tập ký tự cho phép; danh sách đóng hay mở; phân biệt hoa thường; khoảng trắng đầu, cuối, giữa; chuẩn định dạng; thông báo lỗi; nhiều lỗi cùng lúc; dữ liệu có được giữ lại khi bị từ chối; phản hồi API khi thất bại; quyền truy cập.
- Cột "Có thể làm rõ bằng" chỉ nhận: "Quan sát S0", "Chạy thử S6", "Không có trong đặc tả". **Không** ghi thuộc tính HTML hay DevTools.
- **Không trả lời** câu hỏi bằng cách đoán.

### 4. Bảng quan sát cho sinh viên điền

Chỉ hỏi những gì **nhìn thấy được** mà **không cần nhập dữ liệu** và **không cần DevTools**:

| Nhóm | Mục quan sát |
|---|---|
| Đường vào | Mở màn hình bằng cách nào (menu, nút, liên kết, đường dẫn); đường dẫn trên thanh địa chỉ (Web); tiêu đề tab (Web) hoặc tiêu đề màn hình (Mobile) |
| Tiêu đề và chữ | Các tiêu đề nhìn thấy; dòng hướng dẫn hiển thị sẵn; chữ không phải tiếng Việt |
| Ô nhập (mỗi ô một dòng) | Nhãn nguyên văn; có dấu `*` không; placeholder; giá trị mặc định; loại ô nhìn thấy được (ô chữ, dropdown, ô chọn ngày, ô số...); biểu tượng hay nút trong ô |
| Nút và liên kết | Nhãn nguyên văn; loại; màu nền và màu chữ; vị trí |
| Danh sách, bảng (nếu có) | Tên cột; dữ liệu đang hiển thị; nút thao tác trên từng dòng |
| Ảnh cần chụp | Tên file theo quy ước, nội dung từng ảnh |

Theo nền tảng (chi tiết ở `platforms.md`):

- **Web, Web Admin:** Ảnh chụp **cả cửa sổ trình duyệt** để thấy tiêu đề tab và thanh địa chỉ. Nhắc sinh viên có thể che thanh bookmark, ảnh đại diện nếu không muốn lộ thông tin cá nhân.
- **Mobile:** Được chạm vào ô để xem **loại bàn phím** hiện ra (chữ, số, email) nhưng **không gõ**. Ảnh chụp màn hình điện thoại, có thanh trạng thái nếu được.

Không đưa vào bảng: Thông báo lỗi, giới hạn ký tự, ký tự gõ vào có bị che không, thứ tự Tab, thuộc tính HTML, số thẻ `<h1>`. Những mục này để S6.

### 5. Ghi file và dừng

- Ghi `ai_raw/S0_khao_sat.md`, chép thành `00_spec.md` giống hệt; kiểm tra hai file giống nhau.
- Báo sinh viên: Danh sách ảnh cần chụp, nhắc điền bảng ngay trong `00_spec.md`, commit message. Dừng.

## Pha 2: Sinh viên

Sinh viên chụp ảnh vào `screenshots/`, điền bảng quan sát trong `00_spec.md`, commit.

## Pha 3: AI đối chiếu và viết lại `00_spec.md`

1. **Kiểm tra ảnh trước.** Đọc từng ảnh. Thiếu ảnh cho mục nào, ảnh bị cắt không thấy được mục cần đối chiếu (ví dụ không thấy thanh tab), ảnh sai màn hình: Liệt kê cụ thể cần chụp thêm hoặc chụp lại, rồi **dừng**. Không viết tiếp với ảnh thiếu, không tự bổ sung bằng suy đoán.
2. **Nhắc commit trước khi sửa.** Bản sinh viên điền phải được commit trước khi AI viết lại, để lịch sử git tách được phần sinh viên và phần AI. Không biết đã commit chưa thì hỏi.
3. **Đối chiếu từng ô** với ảnh:
   - Sửa chỗ ghi nhầm (chữ sai, hoa thường sai, nhầm nút với liên kết, nhầm nhãn ô với tiêu đề, bỏ sót chữ hiển thị sẵn).
   - Điền cột Ảnh cho mọi dòng.
   - Khôi phục dòng sinh viên lỡ xóa, ghi "Không có" nếu đúng là không có.
   - Liệt kê **mọi** chỗ đã sửa trong mục "Các chỗ AI đã sửa so với bản sinh viên điền" (cột: Mã, sinh viên ghi, đã sửa thành, lý do).
4. **Cập nhật câu hỏi mở:** Bảng trạng thái sau quan sát (đã trả lời bằng quan sát, vẫn mở, chưa áp dụng được). Câu hỏi mới phát sinh đánh số tiếp, chờ sinh viên quyết định.
5. **Khác biệt giữa giao diện và đặc tả** (`Dnn`): Mỗi khác biệt ghi yêu cầu, đặc tả nói gì, quan sát thấy gì, căn cứ. Ghi là "chờ xác nhận ở S6", **chưa kết luận bug**. Khác biệt thuộc feature khác ghi riêng ở mục "Ngoài phạm vi".
6. **Bảng thay đổi so với bản AI:** Phạm vi gồm các chỗ sinh viên thay đổi hoặc chốt so với bản AI (quyết định, câu hỏi được đóng, bản `_vN`). Việc sinh viên điền bảng quan sát là đầu vào theo quy trình, không phải sửa bản AI; các mục AI viết ở pha 3 cũng không phải phần sinh viên sửa. Ghi rõ phạm vi này ở đầu bảng.
7. Đưa commit message, dừng. Các quyết định sinh viên đưa ra sau đó được ghi vào mục "Quyết định của sinh viên" và bảng thay đổi.

## Ghi chú cho bước sau

Cuối `00_spec.md` ghi những gì S1 cần biết: Trường đặc tả yêu cầu mà giao diện không có (hỏi sinh viên có giữ trong thiết kế không), dấu hiệu nhận biết kết quả thành công (không dựa vào chữ thuộc feature khác), các câu hỏi mở sẽ thành giả định ở S2.
