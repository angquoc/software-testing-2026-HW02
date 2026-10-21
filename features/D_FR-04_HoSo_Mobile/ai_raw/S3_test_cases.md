# S3: Chọn test case (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S3 (Chọn test case: Bảng phủ lớp, Minimum Set, ma trận truy vết; theo Step 3 của slide S04)
- Thời gian tạo: 2026-10-21 07:45 (UTC+07:00)
- Căn cứ: `00_spec.md` (yêu cầu FR04-R01 đến FR04-R23, quan sát O01 đến O20), `01_io.md` (biến, Output, tiền điều kiện PC1 đến PC3, sự kiện EV1 đến EV4, checklist mục 7), `02_ec.md` (38 lớp EC01 đến EC38, giả định đã chốt, ghi chú mục 10)

---

## 1. Cách làm

- Theo Step 3 của slide S04: Mỗi lớp có ít nhất một test case. Một test case cơ sở gộp mọi lớp hợp lệ cơ sở; mỗi lớp hợp lệ bất thường một test case riêng; **mỗi test case không hợp lệ chỉ vi phạm đúng một lớp không hợp lệ**, các input khác lấy giá trị cơ sở hoặc giữ nguyên.
- Cách thực thi: Giao diện là chính; nhóm API cho các lớp chỉ đi được qua API (`02_ec.md` cột "Kênh") và hai test case kiểm lại ràng buộc Số điện thoại ở phía hệ thống (`02_ec.md` mục 10).
- Trình bày gọn: Quy trình chung viết một lần (mục 2); mỗi nhóm là một bảng dữ liệu (data matrix). Markdown ở S3, S4; xuất Word và Excel bằng skill `test-case-writing` ở S5 (mục 10 điểm 6).
- Mã test case `TC-PROF-NN`: 01 đến 29 giao diện hợp lệ, 30 đến 69 giao diện không hợp lệ, 70 đến 89 API, 90 đến 99 checklist, 100 trở đi để S4.
- `␣` là một dấu cách; `↵` là phím xuống dòng. Mọi giá trị chép đúng ký tự, không thêm dấu nháy (trừ body JSON).
- Theo yêu cầu của sinh viên, các điểm nhỏ ở mục 10 đã **áp tạm phương án đề xuất**; sinh viên duyệt ở lượt review.

## 2. Tiền điều kiện, giá trị cơ sở và quy trình chung

### 2.1 Trạng thái chuẩn và giá trị cơ sở

| Trường | Trạng thái chuẩn `S_CHUAN` (trước mỗi test case) | Giá trị cơ sở (dùng khi trường không phải đối tượng test) |
|---|---|---|
| Họ Tên | `Test User` | `Nguyen Van An NN` (NN là số test case, ví dụ `Nguyen Van An 01`) |
| Số điện thoại | `0900000000` | `0912345678` |
| Địa chỉ giao hàng | `1 Nguyen Hue, Quận 1` | `12/3 Lê Lợi, Quận 1, TP.HCM` |
| `email`, `role`, `id` | Không gửi | Không gửi |

- `S_CHUAN` có đủ 3 giá trị, khác giá trị cơ sở, để mọi test case thấy được "đã đổi" hay "không đổi", kể cả test case xóa trống (EC09, EC17) và body thiếu trường (EC29). Đây là cách áp PC3 của `01_io.md` (mục 10 điểm 1).
- Đặt `S_CHUAN` bằng `PUT /api/users/me` với 3 giá trị trên, rồi kiểm bằng `GET /api/users/me`. Nếu chính việc này không thành công thì reset dữ liệu mẫu và ghi lại.
- Họ Tên cơ sở có số test case ở cuối để biết giá trị nào do test case nào ghi (A03 (a): Chữ số thuộc lớp cơ sở EC01).

### 2.2 Tiền điều kiện chung

- PC1 (giao diện): Ứng dụng EShop mở bằng Expo Go; đã đăng nhập `test@eshop.com`; đang ở màn hình Hồ sơ (bấm "Chào, Test User").
- PC2 (API): Có token của `test@eshop.com` lấy từ `POST /api/login`.
- PC3: Hồ sơ đang ở `S_CHUAN` (mục 2.1).

### 2.3 Quy trình chung

**QT-GD (giao diện):**

1. Đặt `S_CHUAN` (mục 2.1); mở lại màn hình Hồ sơ để các ô hiển thị `S_CHUAN`.
2. Với mỗi trường trong bảng của test case: Xóa nội dung ô, nhập giá trị. Ô có giá trị "(để trống)" thì chỉ xóa. Trường ghi "giữ" thì không chạm vào.
3. Giá trị có chữ tiếng Việt có dấu: Dán, hoặc dùng bàn phím tiếng Việt (bàn phím đang là "English (US)", O10). Trước khi bấm, nhìn lại ô để chắc giá trị đúng (bàn phím có thể tự viết hoa, O16).
4. Ẩn bàn phím (bàn phím che nút, O20), bấm "Cập nhật".
5. Ghi lại thông báo hiện ra: Câu chữ, hình thức, vị trí so với nút "Cập nhật".
6. EV4: Rời màn hình Hồ sơ, bấm "Chào, Test User" để mở lại; ghi giá trị trong các ô.
7. EV3: `GET /api/users/me` bằng token của PC2; ghi `name`, `phone`, `shipping_address` (và `email`, `role`, `id` nếu có).

**QT-API:**

1. Đặt `S_CHUAN`; với TC-PROF-77, TC-PROF-80 làm thêm bước riêng ghi trong bảng.
2. Gửi yêu cầu theo bảng của test case (`Content-Type: application/json`).
3. Ghi lại mã HTTP và body phản hồi (đặc tả không nêu, Q20).
4. EV3 bằng token của PC2; ghi các trường như QT-GD bước 7.

### 2.4 Cách đọc kết quả mong đợi

| Mã | Đạt khi |
|---|---|
| OUT1 | Có thông báo thành công (ghi câu chữ); sau EV4 các ô hiển thị giá trị mới; EV3 trả giá trị mới ở dạng ghi trong cột "Lưu là" |
| OUT2 | Phản hồi thành công (mã 2xx); EV3 trả giá trị mới ở dạng ghi trong cột "Lưu là" |
| OUT3 | EV3 trả hồ sơ có Email đúng của chủ token |
| OUT4 | Trường được bảo vệ (`email`, `role`, hồ sơ người khác) sau yêu cầu giống hệt trước yêu cầu. Phản hồi của chính yêu cầu thành công hay thất bại đều chấp nhận (A13, A14, A15 (c)); nếu thành công thì các trường hợp lệ khác có thể đã đổi |
| ERR1, ERR2 | Có thông báo lỗi (ghi câu chữ); sau EV4 và EV3, **cả 3 trường** vẫn là `S_CHUAN` (không lưu trường sai, không lưu một phần trường hợp lệ đi kèm, A19 (a)) |
| ERR2 (API) | Không trả phản hồi thành công; EV3 trả `S_CHUAN` |
| ERR4 | Không trả phản hồi thành công; `GET` không trả hồ sơ; EV3 (token hợp lệ) trả `S_CHUAN` |

## 3. Test case giao diện hợp lệ (QT-GD)

| TC | Lớp phủ | Họ Tên | Số điện thoại | Địa chỉ giao hàng | Kết quả mong đợi | Lưu là (EV3) |
|---|---|---|---|---|---|---|
| TC-PROF-01 | EC01, EC08, EC16, EC21, EC23, EC32, EC34 (cơ sở) | `Nguyen Van An 01` | `0912345678` | `12/3 Lê Lợi, Quận 1, TP.HCM` | OUT1; EV3 trả Email `test@eshop.com` (OUT3) | Đúng 3 giá trị đã nhập |
| TC-PROF-02 | EC02 | `Trần Thị Bích 02` | `0912345678` | giữ | OUT1 | `Trần Thị Bích 02`, đúng dấu |
| TC-PROF-03 | EC03 | `␣Nguyen Van An 03␣` | `0912345678` | giữ | OUT1 | `Nguyen Van An 03` (đã cắt, A04 (a)) |
| TC-PROF-04 | EC04 | `<b>An 04</b>` | `0912345678` | giữ | OUT1; ô Họ Tên sau EV4 hiển thị đúng chuỗi `<b>An 04</b>`, không in đậm; ghi lại lời chào trên thanh trên | `<b>An 04</b>` nguyên văn |
| TC-PROF-05 | EC05 | `O'Neil An 05` | `0912345678` | giữ | OUT1; không có lỗi hệ thống | `O'Neil An 05` nguyên văn |
| TC-PROF-06 | EC09 | `Nguyen Van An 06` | (để trống) | giữ | OUT1 | Số điện thoại trống (ghi lại là chuỗi rỗng hay `null`) |
| TC-PROF-07 | EC17 | `Nguyen Van An 07` | giữ | (để trống) | OUT1 | Địa chỉ trống |
| TC-PROF-08 | EC18 | `Nguyen Van An 08` | giữ | `12 Lê Lợi` `↵` `Quận 1` | OUT1; ô Địa chỉ sau EV4 hiển thị 2 dòng | Có ký tự xuống dòng giữa `12 Lê Lợi` và `Quận 1` |
| TC-PROF-09 | EC19 | `Nguyen Van An 09` | giữ | `␣␣␣` | OUT1 | Địa chỉ trống (A11 (a)) |
| TC-PROF-10 | EC20 | `Nguyen Van An 10` | giữ | `<i>Kho A</i>, Quận 1` | OUT1; ô Địa chỉ sau EV4 hiển thị nguyên văn, không in nghiêng | `<i>Kho A</i>, Quận 1` nguyên văn |

Ghi chú: TC-PROF-02 đến TC-PROF-05 nhập Số điện thoại cơ sở để test case cũng đổi một trường khác `S_CHUAN`; TC-PROF-06 đến TC-PROF-10 đổi Họ Tên cơ sở. Các lớp cơ sở EC01, EC08, EC16 vì vậy được dùng lại, không ghi thêm vào cột "Lớp phủ".

## 4. Test case giao diện không hợp lệ (QT-GD)

Mỗi test case vi phạm đúng 1 lớp; trường còn lại được đổi sang giá trị cơ sở (hợp lệ) để phát hiện lưu một phần (A19 (a)). Địa chỉ giữ `S_CHUAN`.

| TC | Lớp không hợp lệ | Họ Tên | Số điện thoại | Kết quả mong đợi |
|---|---|---|---|---|
| TC-PROF-30 | EC06 (Họ Tên rỗng) | (để trống) | `0912345678` | ERR1; EV3: Họ Tên `Test User`, Số điện thoại `0900000000` |
| TC-PROF-31 | EC07 (Họ Tên chỉ khoảng trắng) | `␣␣␣` | `0912345678` | ERR1; EV3 như TC-PROF-30 |
| TC-PROF-32 | EC10 (không bắt đầu bằng `0`) | `Nguyen Van An 32` | `1912345678` | ERR2; EV3: Họ Tên `Test User`, Số điện thoại `0900000000` |
| TC-PROF-33 | EC11 (ít hơn 10 chữ số) | `Nguyen Van An 33` | `091234567` (9 chữ số) | ERR2; EV3 như TC-PROF-32 |
| TC-PROF-34 | EC12 (nhiều hơn 11 chữ số) | `Nguyen Van An 34` | `091234567890` (12 chữ số) | ERR2; EV3 như TC-PROF-32 |
| TC-PROF-35 | EC13 (có ký tự không phải chữ số) | `Nguyen Van An 35` | `0912*345678` (10 chữ số và `*`, gõ bằng phím `*` của bàn phím điện thoại) | ERR2; EV3 như TC-PROF-32 |

Ghi chú: Nếu ứng dụng chặn không cho gõ ký tự `*` hoặc chữ số thứ 12, ghi giá trị thực tế trong ô ở bước 3 của QT-GD; kết quả khi đó phản ánh ứng dụng chứ không phải hệ thống (`platforms.md` mục 4). TC-PROF-74, TC-PROF-75 kiểm lại phía hệ thống.

## 5. Test case API (QT-API)

Body dùng giá trị cơ sở trừ trường ghi trong bảng. `B(NN)` viết tắt cho body đủ 3 trường cơ sở: `{"name": "Nguyen Van An NN", "phone": "0912345678", "shipping_address": "12/3 Lê Lợi, Quận 1, TP.HCM"}`.

| TC | Lớp phủ | Yêu cầu gửi | Kết quả mong đợi |
|---|---|---|---|
| TC-PROF-70 | EC01, EC08, EC16, EC21, EC23, EC25, EC28, EC30, EC33, EC34 (cơ sở API) | `PUT /api/users/me`, token PC2, body `B(70)` | OUT2; EV3 trả đúng 3 giá trị của `B(70)` và Email `test@eshop.com` (OUT3) |
| TC-PROF-71 | EC15 | Như `B(71)` nhưng `"phone": "␣0912345678␣"` | OUT2; EV3 trả `phone` là `0912345678` (A08 (a)) |
| TC-PROF-72 | EC29 | Body chỉ có `{"name": "Nguyen Van An 72"}` | Đạt khi một trong hai: (1) phản hồi thành công, EV3 trả `name` mới, `phone` `0900000000`, `shipping_address` `1 Nguyen Hue, Quận 1`; (2) phản hồi thất bại, EV3 trả `S_CHUAN`. Không đạt nếu `phone` hoặc `shipping_address` bị xóa hay đổi (A16 (d)) |
| TC-PROF-73 | EC14 | Như `B(73)` nhưng `"phone": "0912-345678"` | ERR2 (API); EV3 trả `S_CHUAN` |
| TC-PROF-74 | EC10 (kiểm phía hệ thống) | Như `B(74)` nhưng `"phone": "1912345678"` | ERR2 (API); EV3 trả `S_CHUAN` |
| TC-PROF-75 | EC11 (kiểm phía hệ thống) | Như `B(75)` nhưng `"phone": "091234567"` | ERR2 (API); EV3 trả `S_CHUAN` |
| TC-PROF-76 | EC22 | `B(76)` thêm `"email": "tc76@eshop.com"` | OUT4: EV3 trả Email `test@eshop.com`. Nếu Email bị đổi: Ghi kết quả, reset dữ liệu ngay (mục 8) |
| TC-PROF-77 | EC24 | Bước riêng trước khi gửi: EV3, ghi giá trị `role` (nếu có). Gửi `B(77)` thêm `"role": "admin"` | OUT4: EV3 trả `role` như trước khi gửi. Nếu EV3 không có trường `role`: Ghi "không quan sát được" (giới hạn quan sát, `01_io.md` mục 8 điểm 7). Nếu vai trò bị đổi: Ghi kết quả, reset dữ liệu ngay |
| TC-PROF-78 | EC26 | (1) `PUT /api/users/me` không có header `Authorization`, body `B(78)`; (2) `GET /api/users/me` không có header | ERR4 cho cả hai yêu cầu; EV3 trả `S_CHUAN` |
| TC-PROF-79 | EC27 | Như TC-PROF-78 nhưng header `Authorization: Bearer abc` | ERR4 cho cả hai yêu cầu; EV3 trả `S_CHUAN` |
| TC-PROF-80 | EC31 | Bước riêng: (1) `POST /api/login` bằng `admin@eshop.com`, lấy token admin; (2) EV3 bằng token admin, ghi `id` và hồ sơ admin. Gửi: `PUT /api/users/me` bằng token của `test@eshop.com`, body `B(80)` thêm `"id": <id admin>`; (3) EV3 bằng token admin | OUT4: Hồ sơ admin ở bước (3) giống hệt bước (2); bước (2) cũng là OUT3 cho token admin (trả hồ sơ admin, không phải test). Nếu phản hồi ở bước (2) không có `id`: Blocked |

Ghi chú: Tên trường `id` không có trong API spec (`01_io.md` IN9); test case chỉ thử tên này.

## 6. Checklist giao diện

| TC | Yêu cầu | Điểm kiểm tra | Kết quả mong đợi | Cách kiểm |
|---|---|---|---|---|
| TC-PROF-90 | FR04-R09, FR04-R10, FR04-R11, FR04-R13, FR04-R15, FR04-R06, FR04-R12, FR04-R16 | (1) Bấm "Chào, Test User"; (2) đọc mọi chữ tĩnh trên màn hình Hồ sơ; (3) màu nút "Cập nhật"; (4) nhãn các ô; (5) so "Chào, Test User" khi ở Hồ sơ và khi ở "Danh sách sản phẩm"; (6) chạm, nhấn giữ ô Email, thử dán một chuỗi; (7) **bước cuối:** Bấm "Thoát", ghi chức năng (Q26) | (1) Mở màn hình "Hồ sơ của bạn" (R09); (2) tiếng Việt, trừ tên sản phẩm và thuật ngữ (R10); (3) xanh dương (R11); (4) nhãn "Họ Tên" có `*` vì Họ Tên bắt buộc theo A01 (a) (R13); (5) mục đang chọn được làm nổi (R15); (6) không hiện bàn phím, không dán được, Email giữ `test@eshop.com` (R06); (7) nếu "Thoát" là nút hủy hoặc nguy hiểm thì màu đỏ là đạt (R12); nếu "Thoát" là đăng xuất thì nhãn phải là "Đăng xuất" (R16), nhãn "Thoát" là không đạt | Quan sát, chụp ảnh từng điểm. Chạy sau các test case giao diện khác vì bước (7) có thể đăng xuất |
| TC-PROF-91 | FR04-R14, FR04-R10 | Chạy cùng TC-PROF-32 (thông báo lỗi) và TC-PROF-01 (thông báo thành công) | Thông báo lỗi của TC-PROF-32 nằm phía trên nút "Cập nhật" (R14); thông báo lỗi và thông báo thành công bằng tiếng Việt (R10) | Chụp ảnh khi thông báo đang hiện |

## 7. Bảng phủ lớp

| Lớp | Mô tả ngắn | Loại | Test case |
|---|---|---|---|
| EC01 | Họ Tên cơ sở | H | TC-PROF-01, TC-PROF-70 |
| EC02 | Họ Tên có dấu | H | TC-PROF-02 |
| EC03 | Họ Tên khoảng trắng đầu cuối | H | TC-PROF-03 |
| EC04 | Họ Tên có thẻ HTML | H | TC-PROF-04 |
| EC05 | Họ Tên có dấu nháy đơn | H | TC-PROF-05 |
| EC06 | Họ Tên rỗng | KH | TC-PROF-30 |
| EC07 | Họ Tên chỉ khoảng trắng | KH | TC-PROF-31 |
| EC08 | Số điện thoại cơ sở | H | TC-PROF-01, TC-PROF-70 |
| EC09 | Số điện thoại trống | H | TC-PROF-06 |
| EC10 | Không bắt đầu bằng `0` | KH | TC-PROF-32, TC-PROF-74 |
| EC11 | Ít hơn 10 chữ số | KH | TC-PROF-33, TC-PROF-75 |
| EC12 | Nhiều hơn 11 chữ số | KH | TC-PROF-34 |
| EC13 | Ký tự không phải chữ số | KH | TC-PROF-35 |
| EC14 | Dấu phân cách ở giữa | KH | TC-PROF-73 |
| EC15 | Số điện thoại khoảng trắng đầu cuối | H | TC-PROF-71 |
| EC16 | Địa chỉ cơ sở | H | TC-PROF-01, TC-PROF-70 |
| EC17 | Địa chỉ trống | H | TC-PROF-07 |
| EC18 | Địa chỉ nhiều dòng | H | TC-PROF-08 |
| EC19 | Địa chỉ chỉ khoảng trắng | H | TC-PROF-09 |
| EC20 | Địa chỉ có thẻ HTML | H | TC-PROF-10 |
| EC21 | Không gửi `email` | H | TC-PROF-01, TC-PROF-70 |
| EC22 | Gửi `email` khác | KH | TC-PROF-76 |
| EC23 | Không gửi `role` | H | TC-PROF-01, TC-PROF-70 |
| EC24 | Gửi `role` khác | KH | TC-PROF-77 |
| EC25 | Token hợp lệ | H | TC-PROF-70 |
| EC26 | Không có header | KH | TC-PROF-78 |
| EC27 | Token sai | KH | TC-PROF-79 |
| EC28 | Body đủ 3 trường | H | TC-PROF-70 |
| EC29 | Body thiếu trường | H | TC-PROF-72 |
| EC30 | Không gửi mã người khác | H | TC-PROF-70 |
| EC31 | Gửi `id` của admin | KH | TC-PROF-80 |
| EC32 | OUT1 | Output | TC-PROF-01 đến TC-PROF-10 |
| EC33 | OUT2 | Output | TC-PROF-70, TC-PROF-71 |
| EC34 | OUT3 | Output | TC-PROF-01, TC-PROF-70, TC-PROF-80 |
| EC35 | OUT4 | Output | TC-PROF-76, TC-PROF-77, TC-PROF-80 |
| EC36 | ERR1 | Output | TC-PROF-30, TC-PROF-31 |
| EC37 | ERR2 | Output | TC-PROF-32 đến TC-PROF-35, TC-PROF-73 đến TC-PROF-75 |
| EC38 | ERR4 | Output | TC-PROF-78, TC-PROF-79 |

Mỗi test case không hợp lệ (TC-PROF-30 đến TC-PROF-35, TC-PROF-73 đến TC-PROF-80) chỉ có đúng một lớp KH. Không có ngoại lệ.

## 8. Ma trận truy vết

| Yêu cầu | Test case | Mức phủ |
|---|---|---|
| FR04-R01 | TC-PROF-01 đến TC-PROF-05, TC-PROF-30, TC-PROF-31, TC-PROF-70 | Đủ |
| FR04-R02 | TC-PROF-01, TC-PROF-06, TC-PROF-70 | Đủ |
| FR04-R03 | TC-PROF-01, TC-PROF-07 đến TC-PROF-10, TC-PROF-70 | Đủ |
| FR04-R04 | TC-PROF-32, TC-PROF-74 | Đủ |
| FR04-R05 | TC-PROF-33 đến TC-PROF-35, TC-PROF-73, TC-PROF-75 | Đủ (biên thêm ở S4) |
| FR04-R06 | TC-PROF-76, TC-PROF-90 | Đủ |
| FR04-R07 | TC-PROF-80 | Một phần: Chỉ thử trường `id` (tên trường không có trong API spec); có thể Blocked nếu không lấy được `id` của admin |
| FR04-R08 | TC-PROF-77 | Đủ trên thiết kế; có thể không quan sát được nếu EV3 không trả `role` |
| FR04-R09 | TC-PROF-90 | Đủ |
| FR04-R10 | TC-PROF-90, TC-PROF-91 | Đủ |
| FR04-R11 | TC-PROF-90 | Đủ |
| FR04-R12 | TC-PROF-90 | Đủ trên thiết kế; kết luận phụ thuộc chức năng nút "Thoát" (Q26) |
| FR04-R13 | TC-PROF-90 | Đủ |
| FR04-R14 | TC-PROF-91 | Đủ |
| FR04-R15 | TC-PROF-90 | Đủ |
| FR04-R16 | TC-PROF-90 | Đủ trên thiết kế; chỉ áp dụng nếu "Thoát" là đăng xuất (Q26) |
| FR04-R17 | TC-PROF-01, TC-PROF-70, TC-PROF-80 | Đủ |
| FR04-R18 | TC-PROF-70, TC-PROF-72 | Đủ |
| FR04-R19 | TC-PROF-76, TC-PROF-77 | Đủ |
| FR04-R20 | TC-PROF-78, TC-PROF-79 | Một phần: Không thiết kế token hết hạn (`02_ec.md` quyết định 4) |
| FR04-R21 | TC-PROF-77 | Như FR04-R08 |
| FR04-R22 | TC-PROF-04, TC-PROF-10 | Một phần: Chỉ quan sát hiển thị trên ứng dụng Mobile; hiển thị trên Web, Web Admin thuộc feature khác |
| FR04-R23 | TC-PROF-05 | Một phần: Chỉ suy ra qua hành vi (lưu đúng nguyên văn, không lỗi hệ thống) |

Yêu cầu chưa phủ đủ: FR04-R07, FR04-R20, FR04-R22, FR04-R23 (Một phần); FR04-R08, FR04-R12, FR04-R16, FR04-R21 phụ thuộc điều kiện quan sát.

## 9. Thứ tự chạy và giới hạn quan sát

### 9.1 Thứ tự chạy

1. Reset dữ liệu mẫu (WORKFLOW mục 3.3). Ghi tên thiết bị, phiên bản Android, phiên bản Expo Go, ngày chạy.
2. TC-PROF-70 trước tiên: Việc đặt `S_CHUAN` dùng cùng API; nếu TC-PROF-70 không đạt thì dùng reset dữ liệu mẫu thay cho bước đặt `S_CHUAN`.
3. Giao diện: TC-PROF-01 đến TC-PROF-10, TC-PROF-30 đến TC-PROF-35 (chạy TC-PROF-91 cùng TC-PROF-01 và TC-PROF-32).
4. API: TC-PROF-71 đến TC-PROF-75, TC-PROF-78, TC-PROF-79, TC-PROF-80.
5. TC-PROF-90 (bước cuối bấm "Thoát" có thể đăng xuất).
6. TC-PROF-76, TC-PROF-77 cuối cùng: Nếu hệ thống đổi Email hoặc vai trò thì tài khoản `test@eshop.com` không còn như dữ liệu mẫu. Reset dữ liệu mẫu ngay sau hai test case này.

Không test case nào có chuỗi phá dữ liệu (chuỗi SQL của TC-PROF-05 chỉ là một dấu nháy đơn).

### 9.2 Giới hạn quan sát

- EV4 có thể hiển thị giá trị ứng dụng còn giữ trong bộ nhớ; kết luận về dữ liệu lưu dựa vào EV3.
- Test case giao diện của Số điện thoại có thể chỉ kiểm ứng dụng (ứng dụng chặn trước khi gửi); TC-PROF-74, TC-PROF-75 kiểm phía hệ thống cho FR04-R04, FR04-R05.
- TC-PROF-04, TC-PROF-10: Theo hiểu biết chung về React Native, thành phần hiển thị chữ không diễn giải HTML, nên trên Mobile hai test case này nhiều khả năng đạt; rủi ro hiển thị HTML thật nằm ở Web, Web Admin (ngoài phạm vi).
- TC-PROF-77, TC-PROF-80 phụ thuộc cấu trúc phản hồi của `GET /api/users/me` (Q20).

## 10. Điểm cần sinh viên quyết định

Các điểm dưới đây đã áp tạm phương án (a); sinh viên duyệt ở lượt review.

| # | Vấn đề | Các lựa chọn | Đã áp tạm |
|---|---|---|---|
| 1 | Cách áp PC3 | (a) `S_CHUAN` có đủ 3 giá trị, đặt bằng API trước mỗi test case; (b) dùng giá trị ban đầu (Số điện thoại, Địa chỉ trống), test case cần giá trị thì tự đặt | (a) |
| 2 | Mẫu dữ liệu Họ Tên | (a) `Nguyen Van An NN` gắn số test case; (b) một giá trị cố định | (a) |
| 3 | Kiểm Số điện thoại phía hệ thống | (a) Hai test case API: EC10 (TC-PROF-74), EC11 (TC-PROF-75); (b) thêm EC12, EC13 qua API | (a) |
| 4 | Checklist | (a) Ở S3, gộp thành 2 test case; (b) để S5 | (a) |
| 5 | Nút "Thoát" | (a) Bấm ở bước cuối TC-PROF-90 để trả lời Q26; (b) không bấm, FR04-R12, FR04-R16 ghi "chưa xác định" | (a) |
| 6 | Trình bày | (a) Markdown ở S3, S4, xuất Word và Excel bằng `test-case-writing` ở S5; (b) xuất ngay | (a) |
| 7 | TC-PROF-76, TC-PROF-77 | (a) Chạy cuối, reset ngay sau; (b) chạy theo thứ tự số | (a) |

## 11. Ghi chú cho bước sau

- **Số lượng:** 29 test case (10 giao diện hợp lệ, 6 giao diện không hợp lệ, 11 API, 2 checklist). S4 còn khoảng 6 test case trong mục tiêu 35.
- **Biên đã hẹn từ `02_ec.md` mục 10:**
  - Số chữ số của Số điện thoại: LB-1 = 9 (TC-PROF-33 đã có), LB = 10 (TC-PROF-01 đã có), UB = 11 (chưa có), UB+1 = 12 (TC-PROF-34 đã có); nhỏ nhất chỉ vi phạm số chữ số là `0` (chưa có). LB+1 trùng UB, UB-1 trùng LB.
  - Họ Tên: Cận dưới 1 ký tự sau khi cắt: `A`, `␣A␣` (chưa có); `␣` (1 dấu cách, cùng lớp EC07 với TC-PROF-31).
  - Địa chỉ: Không có cận, không làm BVA.
- **Đường thực thi:** Biên Số điện thoại chạy qua giao diện (bàn phím điện thoại gõ được đủ chữ số); S4 cân nhắc thêm UB = 11 qua API vì TC-PROF-74, TC-PROF-75 chỉ kiểm phía hệ thống ở chữ số đầu và cận dưới. Biên Họ Tên `␣A␣` qua giao diện được (bàn phím chữ có phím cách).
- **Giá trị đại diện nằm giữa lớp:** Không có; giá trị cơ sở `0912345678` đã ở LB.
