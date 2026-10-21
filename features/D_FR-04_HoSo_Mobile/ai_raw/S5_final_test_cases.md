# S5: Bộ test case cuối cùng (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S5 (Review lần cuối, trình bày bộ test case). Bản này do AI gộp `03_tc.md` và `04_bva.md`; không đổi nội dung test case
- Thời gian tạo: 2026-10-21 07:58 (UTC+07:00), lấy từ giờ máy
- Căn cứ: `03_tc.md` (bản review S3, 29 test case), `04_bva.md` (bản review S4, 5 test case), `ai_raw/S3_test_cases.md` và `ai_raw/S4_bva.md` (để xác định nguồn gốc), `02_ec.md` (lớp), `00_spec.md` (yêu cầu, khác biệt D01 đến D03). Quy ước cột "Nguồn gốc", "Phát hiện" lấy theo `features/A_FR-01_DangKy/05_final_tc.md` mục 1.1 (sinh viên cho phép đọc riêng file này; chỉ dùng quy ước cột, không dùng nội dung test case của FR-01)
- Trình bày: Chỉ Markdown, không xuất Word, Excel (`03_tc.md` quyết định 6)

---

## 1. Cách gộp và quy ước

### 1.1 Nguồn gốc

| Giá trị | Nghĩa | Ứng với trường `origin` của skill `test-case-writing` |
|---|---|---|
| AI | Test case có trong bản AI (`ai_raw/S3_test_cases.md` hoặc `ai_raw/S4_bva.md`) và giữ nguyên nội dung | `AI` |
| AI có SV sửa | Test case có trong bản AI nhưng đã đổi giá trị kiểm, kết quả mong đợi, bước, hoặc ghi chú giới hạn; hoặc test case mới do AI đề xuất khi review | `Both` |
| SV thêm | Test case mới do sinh viên phát hiện thiếu khi review, hoặc sinh viên tự viết ở S5 | `Human` |

Cột **"Phát hiện"** ghi ai phát hiện điều gì dẫn tới test case đó, kể cả khi nguồn gốc vẫn là "AI":

| Ghi | Nghĩa |
|---|---|
| AI | Không có thay đổi hay bổ sung nào khi review; test case và lớp nó phủ đều có trong bản AI |
| SV: ... | Sinh viên phát hiện (lớp thiếu, việc cần tách test case, bước kiểm chứng, giới hạn quan sát...). Ghi bước và số câu hỏi |
| AI bổ sung ... | AI ở phiên thiết kế tự bổ sung khi viết bản review |

Ở feature này, ở mọi bước từ S1 đến S4, sinh viên đều chọn phương án AI đã đề xuất và không thêm, sửa test case nào (`01_io.md` mục 12, `02_ec.md` mục 11, `03_tc.md` mục 14, `04_bva.md` mục 10). Hai dòng loại "Sai" trong các bảng thay đổi (cột tham chiếu ở `02_ec.md`, giờ tạo ở `03_tc.md`) không đổi nội dung test case nào. Vì vậy cả 34 test case có nguồn gốc "AI" và cột "Phát hiện" ghi "AI".

Thông tin sinh viên cung cấp ở S0 (đường vào màn Hồ sơ O02, chạm vào Email O12) là đầu vào của bước khảo sát, không phải phát hiện khi review; được dùng trong QT-GD và TC-PROF-90.

### 1.2 Ký hiệu và kết quả mong đợi

- `␣` là **một dấu cách**; `↵` là phím xuống dòng.
- Mã test case giữ như `03_tc.md` và `04_bva.md`; không có mã nào bị bỏ.

| Mã | Đạt khi |
|---|---|
| OUT1 | Có thông báo thành công (ghi câu chữ); sau EV4 các ô hiển thị giá trị mới; EV3 trả giá trị mới ở dạng ghi trong cột "Kết quả mong đợi" |
| OUT2 | Phản hồi thành công (mã 2xx); EV3 trả giá trị mới |
| OUT3 | EV3 trả hồ sơ có Email đúng của chủ token |
| OUT4 | Trường được bảo vệ (`email`, `role`, hồ sơ người khác) sau yêu cầu giống hệt trước yêu cầu. Phản hồi thành công hay thất bại đều chấp nhận (A13, A14, A15 (c)) |
| ERR1, ERR2 (giao diện) | Có thông báo lỗi (ghi câu chữ); sau EV4 và EV3, cả 3 trường vẫn là `S_CHUAN` (A19 (a)) |
| ERR2 (API) | Không trả phản hồi thành công; EV3 trả `S_CHUAN` |
| ERR4 | Không trả phản hồi thành công; `GET` không trả hồ sơ; EV3 (token hợp lệ) trả `S_CHUAN` |
| Khác giả định | Hệ thống làm khác giả định đã chốt ở S2 (không phải khác đặc tả); ghi lại, xét ở S7 trước khi coi là bug (`04_bva.md` quyết định 5) |

ERR1: Họ Tên không hợp lệ (rỗng sau khi cắt). ERR2: Số điện thoại không hợp lệ. ERR4: Không xác thực được. Đặc tả không nêu câu chữ thông báo nên kết quả mong đợi không ghi câu chữ.

### 1.3 Tiền điều kiện chung, trạng thái chuẩn, giá trị cơ sở

- PC1 (giao diện): Ứng dụng EShop mở bằng Expo Go trên Samsung Galaxy S21 Ultra; đã đăng nhập `test@eshop.com`; đang ở màn hình Hồ sơ (bấm "Chào, Test User").
- PC2 (API): Có token của `test@eshop.com` lấy từ `POST /api/login`, gửi trong header `Authorization: Bearer <token>`.
- PC3: Trước mỗi test case, hồ sơ ở `S_CHUAN`, đặt bằng `PUT /api/users/me` rồi kiểm bằng `GET /api/users/me`.

| Trường | `S_CHUAN` | Giá trị cơ sở |
|---|---|---|
| Họ Tên | `Test User` | `Nguyen Van An NN` (NN là số test case) |
| Số điện thoại | `0900000000` | `0912345678` |
| Địa chỉ giao hàng | `1 Nguyen Hue, Quận 1` | `12/3 Lê Lợi, Quận 1, TP.HCM` |
| `email`, `role`, `id` | Không gửi | Không gửi |

`B(NN)`: Body đủ 3 trường cơ sở `{"name": "Nguyen Van An NN", "phone": "0912345678", "shipping_address": "12/3 Lê Lợi, Quận 1, TP.HCM"}`.

### 1.4 Quy trình chung

**QT-GD (giao diện):**

1. Đặt `S_CHUAN`; mở lại màn hình Hồ sơ để các ô hiển thị `S_CHUAN`.
2. Với mỗi trường trong bảng: Xóa nội dung ô, nhập giá trị. "(để trống)" thì chỉ xóa; "giữ" thì không chạm vào.
3. Giá trị có chữ tiếng Việt có dấu: Dán, hoặc dùng bàn phím tiếng Việt. Trước khi bấm, nhìn lại ô để chắc giá trị đúng (bàn phím có thể tự viết hoa, chặn ký tự).
4. Ẩn bàn phím (bàn phím che nút), bấm "Cập nhật".
5. Ghi thông báo: Câu chữ, hình thức, vị trí so với nút "Cập nhật".
6. EV4: Rời màn hình Hồ sơ, bấm "Chào, Test User" để mở lại; ghi giá trị trong các ô.
7. EV3: `GET /api/users/me` bằng token của PC2; ghi `name`, `phone`, `shipping_address` (và `email`, `role`, `id` nếu có).

**QT-API:**

1. Đặt `S_CHUAN`; làm bước riêng nếu bảng có ghi.
2. Gửi yêu cầu theo bảng (`Content-Type: application/json`).
3. Ghi mã HTTP và body phản hồi.
4. EV3 bằng token của PC2.

---

## 2. Tổng hợp

| Nhóm | Mã | Số TC | AI | AI có SV sửa | SV thêm | Có phần do SV phát hiện |
|---|---|---|---|---|---|---|
| TS-01 Hợp lệ qua giao diện (EP) | TC-PROF-01 đến TC-PROF-10 | 10 | 10 | 0 | 0 | 0 |
| TS-02 Không hợp lệ qua giao diện (EP) | TC-PROF-30 đến TC-PROF-35 | 6 | 6 | 0 | 0 | 0 |
| TS-03 Giá trị biên qua giao diện (BVA) | TC-PROF-100, TC-PROF-101, TC-PROF-103, TC-PROF-104 | 4 | 4 | 0 | 0 | 0 |
| TS-04 API (EP, BVA) | TC-PROF-70 đến TC-PROF-80, TC-PROF-102 | 12 | 12 | 0 | 0 | 0 |
| TS-05 Checklist giao diện | TC-PROF-90, TC-PROF-91 | 2 | 2 | 0 | 0 | 0 |
| **Tổng** | | **34** | **34** | **0** | **0** | **0** |

Theo kỹ thuật: 29 test case Domain Testing (EP) và checklist từ S3, 5 test case BVA từ S4. Có thể Blocked hoặc không quan sát được: TC-PROF-80 (nếu không lấy được `id` của admin), TC-PROF-77 (nếu `GET /api/users/me` không trả `role`).

---

## 3. TS-01: Cập nhật hồ sơ hợp lệ qua giao diện (EP, QT-GD)

| TC | Tiêu đề | Lớp | Yêu cầu | Họ Tên | Số điện thoại | Địa chỉ giao hàng | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|---|---|
| TC-PROF-01 | Kiểm tra cập nhật hồ sơ thành công với dữ liệu hợp lệ cơ sở | EC01, EC08, EC16, EC21, EC23, EC32, EC34 | FR04-R01, FR04-R02, FR04-R03, FR04-R17 | `Nguyen Van An 01` | `0912345678` | `12/3 Lê Lợi, Quận 1, TP.HCM` | OUT1, lưu đúng 3 giá trị; EV3 trả Email `test@eshop.com` (OUT3) | AI | AI |
| TC-PROF-02 | Kiểm tra cập nhật thành công khi Họ Tên có chữ tiếng Việt có dấu | EC02 | FR04-R01 | `Trần Thị Bích 02` | `0912345678` | giữ | OUT1, lưu `Trần Thị Bích 02` đúng dấu | AI | AI |
| TC-PROF-03 | Kiểm tra cập nhật thành công khi Họ Tên có khoảng trắng đầu và cuối | EC03 | FR04-R01 | `␣Nguyen Van An 03␣` | `0912345678` | giữ | OUT1, lưu `Nguyen Van An 03` (đã cắt) | AI | AI |
| TC-PROF-04 | Kiểm tra cập nhật thành công và hiển thị an toàn khi Họ Tên có thẻ HTML | EC04 | FR04-R01, FR04-R22 | `<b>An 04</b>` | `0912345678` | giữ | OUT1; ô Họ Tên sau EV4 hiển thị đúng chuỗi, không in đậm; ghi lại lời chào; lưu nguyên văn | AI | AI |
| TC-PROF-05 | Kiểm tra cập nhật thành công khi Họ Tên có dấu nháy đơn | EC05 | FR04-R01, FR04-R23 | `O'Neil An 05` | `0912345678` | giữ | OUT1, không có lỗi hệ thống, lưu nguyên văn | AI | AI |
| TC-PROF-06 | Kiểm tra cập nhật thành công khi xóa trống Số điện thoại | EC09 | FR04-R02 | `Nguyen Van An 06` | (để trống) | giữ | OUT1, Số điện thoại lưu trống (ghi là chuỗi rỗng hay `null`) | AI | AI |
| TC-PROF-07 | Kiểm tra cập nhật thành công khi xóa trống Địa chỉ | EC17 | FR04-R03 | `Nguyen Van An 07` | giữ | (để trống) | OUT1, Địa chỉ lưu trống | AI | AI |
| TC-PROF-08 | Kiểm tra cập nhật thành công khi Địa chỉ có nhiều dòng | EC18 | FR04-R03 | `Nguyen Van An 08` | giữ | `12 Lê Lợi` `↵` `Quận 1` | OUT1; ô Địa chỉ sau EV4 hiển thị 2 dòng; lưu có ký tự xuống dòng | AI | AI |
| TC-PROF-09 | Kiểm tra cập nhật thành công khi Địa chỉ chỉ gồm khoảng trắng | EC19 | FR04-R03 | `Nguyen Van An 09` | giữ | `␣␣␣` | OUT1, Địa chỉ lưu trống | AI | AI |
| TC-PROF-10 | Kiểm tra cập nhật thành công và hiển thị an toàn khi Địa chỉ có thẻ HTML | EC20 | FR04-R03, FR04-R22 | `Nguyen Van An 10` | giữ | `<i>Kho A</i>, Quận 1` | OUT1; ô Địa chỉ sau EV4 hiển thị nguyên văn, không in nghiêng; lưu nguyên văn | AI | AI |

## 4. TS-02: Cập nhật hồ sơ không hợp lệ qua giao diện (EP, QT-GD)

Mỗi test case vi phạm đúng 1 lớp; trường còn lại đổi sang giá trị cơ sở để phát hiện lưu một phần; Địa chỉ giữ `S_CHUAN`.

| TC | Tiêu đề | Lớp | Yêu cầu | Họ Tên | Số điện thoại | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|---|
| TC-PROF-30 | Kiểm tra từ chối cập nhật khi Họ Tên rỗng | EC06, EC36 | FR04-R01 | (để trống) | `0912345678` | ERR1; EV3: Họ Tên `Test User`, Số điện thoại `0900000000` | AI | AI |
| TC-PROF-31 | Kiểm tra từ chối cập nhật khi Họ Tên chỉ gồm khoảng trắng | EC07, EC36 | FR04-R01 | `␣␣␣` | `0912345678` | ERR1; EV3 như TC-PROF-30 | AI | AI |
| TC-PROF-32 | Kiểm tra từ chối cập nhật khi Số điện thoại không bắt đầu bằng 0 | EC10, EC37 | FR04-R04 | `Nguyen Van An 32` | `1912345678` | ERR2; EV3: Họ Tên `Test User`, Số điện thoại `0900000000` | AI | AI |
| TC-PROF-33 | Kiểm tra từ chối cập nhật khi Số điện thoại ít hơn 10 chữ số | EC11, EC37 | FR04-R05 | `Nguyen Van An 33` | `091234567` (9 chữ số) | ERR2; EV3 như TC-PROF-32 | AI | AI |
| TC-PROF-34 | Kiểm tra từ chối cập nhật khi Số điện thoại nhiều hơn 11 chữ số | EC12, EC37 | FR04-R05 | `Nguyen Van An 34` | `091234567890` (12 chữ số) | ERR2; EV3 như TC-PROF-32. Ghi số chữ số ô thực sự nhận (điểm thăm dò, `04_bva.md` quyết định 2) | AI | AI |
| TC-PROF-35 | Kiểm tra từ chối cập nhật khi Số điện thoại có ký tự không phải chữ số | EC13, EC37 | FR04-R05 | `Nguyen Van An 35` | `0912*345678` (10 chữ số và `*`) | ERR2; EV3 như TC-PROF-32 | AI | AI |

Nếu ứng dụng chặn không cho gõ `*` hoặc chữ số thứ 12, ghi giá trị thực tế trong ô; kết quả khi đó phản ánh ứng dụng chứ không phải hệ thống.

## 5. TS-03: Giá trị biên qua giao diện (BVA, QT-GD)

Địa chỉ giữ `S_CHUAN`.

| TC | Tiêu đề | Biên | Yêu cầu | Họ Tên | Số điện thoại | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|---|
| TC-PROF-100 | Kiểm tra từ chối cập nhật khi Số điện thoại chỉ có 1 chữ số | P1, nhỏ nhất chỉ vi phạm số chữ số (EC11) | FR04-R05 | `Nguyen Van An 100` | `0` | ERR2; EV3: Họ Tên `Test User`, Số điện thoại `0900000000` | AI | AI |
| TC-PROF-101 | Kiểm tra cập nhật thành công khi Số điện thoại có đúng 11 chữ số | P1, UB (EC08) | FR04-R05 | `Nguyen Van An 101` | `09123456789` | OUT1, lưu `09123456789` | AI | AI |
| TC-PROF-103 | Kiểm tra cập nhật thành công khi Họ Tên có đúng 1 ký tự | P2, LB (EC01) | FR04-R01 | `A` | `0912345678` | OUT1, lưu `A` | AI | AI |
| TC-PROF-104 | Kiểm tra cập nhật thành công khi Họ Tên 1 ký tự có khoảng trắng hai bên | P2, LB có khoảng trắng hai bên (EC03) | FR04-R01 | `␣B␣` | `0912345678` | OUT1, lưu `B`; lưu nguyên văn `␣B␣` là khác giả định A04 (a) | AI | AI |

Biên dùng lại test case đã có: P1 LB-1 (TC-PROF-33, TC-PROF-75), LB và UB-1 (TC-PROF-01), UB+1 (TC-PROF-34), nhỏ nhất giao diện cho nhập (TC-PROF-06); P2 nhỏ nhất giao diện cho nhập (TC-PROF-30), LB-1 dạng chỉ khoảng trắng (TC-PROF-31).

## 6. TS-04: API (EP, BVA, QT-API)

| TC | Tiêu đề | Lớp hoặc biên | Kỹ thuật | Yêu cầu | Yêu cầu gửi | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|---|
| TC-PROF-70 | Kiểm tra API cập nhật hồ sơ thành công với dữ liệu hợp lệ cơ sở | EC01, EC08, EC16, EC21, EC23, EC25, EC28, EC30, EC33, EC34 | EP | FR04-R17, FR04-R18 | `PUT /api/users/me`, token PC2, body `B(70)` | OUT2, EV3 trả đúng `B(70)` và Email `test@eshop.com` | AI | AI |
| TC-PROF-71 | Kiểm tra API cắt khoảng trắng đầu và cuối của Số điện thoại | EC15, EC33 | EP | FR04-R02, FR04-R05 | `B(71)` với `"phone": "␣0912345678␣"` | OUT2, EV3 trả `phone` là `0912345678` | AI | AI |
| TC-PROF-72 | Kiểm tra API khi body thiếu trường không xóa dữ liệu cũ | EC29 | EP | FR04-R18 | Body chỉ có `{"name": "Nguyen Van An 72"}` | Đạt khi: (1) thành công, `phone` `0900000000`, `shipping_address` `1 Nguyen Hue, Quận 1` giữ nguyên; hoặc (2) thất bại, EV3 trả `S_CHUAN`. Không đạt nếu `phone`, `shipping_address` bị xóa hay đổi | AI | AI |
| TC-PROF-73 | Kiểm tra API từ chối Số điện thoại có dấu phân cách | EC14, EC37 | EP | FR04-R05 | `B(73)` với `"phone": "0912-345678"` | ERR2 (API) | AI | AI |
| TC-PROF-74 | Kiểm tra API từ chối Số điện thoại không bắt đầu bằng 0 | EC10, EC37 | EP | FR04-R04 | `B(74)` với `"phone": "1912345678"` | ERR2 (API) | AI | AI |
| TC-PROF-75 | Kiểm tra API từ chối Số điện thoại ít hơn 10 chữ số | EC11, EC37 | EP, BVA (P1 LB-1) | FR04-R05 | `B(75)` với `"phone": "091234567"` | ERR2 (API) | AI | AI |
| TC-PROF-76 | Kiểm tra API không đổi Email khi body có trường `email` | EC22, EC35 | EP | FR04-R06, FR04-R19 | `B(76)` thêm `"email": "tc76@eshop.com"` | OUT4: EV3 trả Email `test@eshop.com`. Email bị đổi: Ghi kết quả, reset ngay | AI | AI |
| TC-PROF-77 | Kiểm tra API không đổi vai trò khi body có trường `role` | EC24, EC35 | EP | FR04-R08, FR04-R19, FR04-R21 | Trước: EV3, ghi `role`. Gửi `B(77)` thêm `"role": "admin"` | OUT4: EV3 trả `role` như trước. EV3 không có `role`: Ghi "không quan sát được". Vai trò bị đổi: Ghi kết quả, reset ngay | AI | AI |
| TC-PROF-78 | Kiểm tra API từ chối khi không có header Authorization | EC26, EC38 | EP | FR04-R20 | (1) `PUT /api/users/me` không header, body `B(78)`; (2) `GET /api/users/me` không header | ERR4 cho cả hai; EV3 trả `S_CHUAN` | AI | AI |
| TC-PROF-79 | Kiểm tra API từ chối khi token không hợp lệ | EC27, EC38 | EP | FR04-R20 | Như TC-PROF-78 với `Authorization: Bearer abc` | ERR4 cho cả hai; EV3 trả `S_CHUAN` | AI | AI |
| TC-PROF-80 | Kiểm tra API không sửa hồ sơ người khác khi body có `id` của người khác | EC31, EC34, EC35 | EP | FR04-R07, FR04-R17 | (1) `POST /api/login` bằng `admin@eshop.com`; (2) EV3 bằng token admin, ghi `id` và hồ sơ; gửi `PUT /api/users/me` bằng token test, body `B(80)` thêm `"id": <id admin>`; (3) EV3 bằng token admin | OUT4: Hồ sơ admin ở (3) giống (2); (2) trả hồ sơ admin (OUT3). Không có `id` ở (2): Blocked | AI | AI |
| TC-PROF-102 | Kiểm tra API cập nhật thành công khi Số điện thoại có đúng 11 chữ số | P1, UB (EC08) | BVA | FR04-R05 | `B(102)` với `"phone": "09123456789"` | OUT2, EV3 trả `phone` là `09123456789` | AI | AI |

Tên trường `id` không có trong API spec; TC-PROF-80 chỉ thử tên này.

## 7. TS-05: Checklist giao diện

| TC | Tiêu đề | Yêu cầu | Điểm kiểm tra | Kết quả mong đợi | Cách kiểm tra | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|
| TC-PROF-90 | Kiểm tra các yêu cầu giao diện tĩnh của màn hình Hồ sơ | FR04-R06, FR04-R09 đến FR04-R13, FR04-R15, FR04-R16 | (1) Bấm "Chào, Test User"; (2) đọc mọi chữ tĩnh; (3) màu nút "Cập nhật"; (4) nhãn các ô; (5) so "Chào, Test User" khi ở Hồ sơ và khi ở "Danh sách sản phẩm"; (6) chạm, nhấn giữ ô Email, thử dán; (7) bước cuối: Bấm "Thoát", ghi chức năng | (1) Mở "Hồ sơ của bạn" (R09); (2) tiếng Việt, trừ tên sản phẩm và thuật ngữ (R10); (3) xanh dương (R11); (4) "Họ Tên" có `*` (R13, A01 (a)); (5) mục đang chọn được làm nổi (R15); (6) không hiện bàn phím, không dán được, Email giữ nguyên (R06); (7) nút hủy hoặc nguy hiểm thì màu đỏ là đạt (R12); nếu là đăng xuất thì nhãn phải là "Đăng xuất" (R16) | Quan sát, chụp ảnh từng điểm; chạy sau các test case giao diện khác | AI | AI |
| TC-PROF-91 | Kiểm tra vị trí và ngôn ngữ của thông báo khi cập nhật | FR04-R10, FR04-R14 | Chạy cùng TC-PROF-32 (lỗi) và TC-PROF-01 (thành công) | Thông báo lỗi nằm phía trên nút "Cập nhật" (R14); thông báo lỗi và thành công bằng tiếng Việt (R10) | Chụp ảnh khi thông báo đang hiện | AI | AI |

---

## 8. Nguồn gốc chi tiết

### 8.1 Test case không phải "AI"

Không có.

### 8.2 Test case đã bỏ

Không có. Mọi test case trong `ai_raw/S3_test_cases.md` và `ai_raw/S4_bva.md` đều có trong bộ cuối, giữ nguyên mã.

## 9. Thứ tự chạy

1. Reset dữ liệu mẫu (WORKFLOW mục 3.3). Ghi tên thiết bị, phiên bản Android, phiên bản Expo Go, ngày chạy.
2. TC-PROF-70 trước tiên (việc đặt `S_CHUAN` dùng cùng API); nếu không đạt thì dùng reset dữ liệu mẫu thay cho bước đặt `S_CHUAN`.
3. Giao diện: TC-PROF-01 đến TC-PROF-10, TC-PROF-30 đến TC-PROF-35, TC-PROF-100, TC-PROF-101, TC-PROF-103, TC-PROF-104 (chạy TC-PROF-91 cùng TC-PROF-01 và TC-PROF-32).
4. API: TC-PROF-71 đến TC-PROF-75, TC-PROF-78, TC-PROF-79, TC-PROF-80, TC-PROF-102.
5. TC-PROF-90 (bước cuối bấm "Thoát" có thể đăng xuất).
6. TC-PROF-76, TC-PROF-77 cuối cùng; reset dữ liệu mẫu ngay sau.

## 10. Giới hạn quan sát

- EV4 có thể hiển thị giá trị ứng dụng còn giữ trong bộ nhớ; kết luận về dữ liệu lưu dựa vào EV3.
- Test case giao diện của Số điện thoại có thể chỉ kiểm ứng dụng. Phía hệ thống được kiểm ở TC-PROF-73 đến TC-PROF-75, TC-PROF-102; cận trên UB+1 (12 chữ số) chỉ kiểm qua giao diện (TC-PROF-34), nếu ứng dụng chặn chữ số thứ 12 thì cận trên phía hệ thống chưa được kiểm (`04_bva.md` quyết định 1).
- TC-PROF-04, TC-PROF-10: Theo hiểu biết chung về React Native, thành phần hiển thị chữ không diễn giải HTML, nên trên Mobile nhiều khả năng đạt; rủi ro hiển thị HTML thật nằm ở Web, Web Admin (ngoài phạm vi).
- TC-PROF-77, TC-PROF-80 phụ thuộc cấu trúc phản hồi của `GET /api/users/me` (Q20).
- Kết quả mong đợi có phần dựa trên giả định (A01 đến A19 ở `02_ec.md`); hệ thống làm khác giả định thì ghi "khác giả định".

## 11. Ma trận truy vết yêu cầu

| Yêu cầu | Test case | Mức phủ |
|---|---|---|
| FR04-R01 | TC-PROF-01 đến TC-PROF-05, TC-PROF-30, TC-PROF-31, TC-PROF-70, TC-PROF-103, TC-PROF-104 | Đủ |
| FR04-R02 | TC-PROF-01, TC-PROF-06, TC-PROF-70, TC-PROF-71 | Đủ |
| FR04-R03 | TC-PROF-01, TC-PROF-07 đến TC-PROF-10, TC-PROF-70 | Đủ |
| FR04-R04 | TC-PROF-32, TC-PROF-74 | Đủ |
| FR04-R05 | TC-PROF-33 đến TC-PROF-35, TC-PROF-71, TC-PROF-73, TC-PROF-75, TC-PROF-100 đến TC-PROF-102 | Đủ |
| FR04-R06 | TC-PROF-76, TC-PROF-90 | Đủ |
| FR04-R07 | TC-PROF-80 | Một phần: Chỉ thử trường `id`; có thể Blocked |
| FR04-R08 | TC-PROF-77 | Đủ trên thiết kế; có thể không quan sát được |
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
| FR04-R20 | TC-PROF-78, TC-PROF-79 | Một phần: Không thiết kế token hết hạn |
| FR04-R21 | TC-PROF-77 | Như FR04-R08 |
| FR04-R22 | TC-PROF-04, TC-PROF-10 | Một phần: Chỉ quan sát hiển thị trên ứng dụng Mobile |
| FR04-R23 | TC-PROF-05 | Một phần: Chỉ suy ra qua hành vi |

So với bản AI của S3: FR04-R01 thêm TC-PROF-103, TC-PROF-104 và FR04-R05 thêm TC-PROF-100 đến TC-PROF-102 (từ `04_bva.md` mục 4). TC-PROF-71 cho FR04-R02, FR04-R05 thiếu trong ma trận của bản AI S3; AI phát hiện khi gộp và đã bổ sung vào `03_tc.md` (cập nhật lần 1).

## 12. Khác biệt chờ xác nhận ở S6

| Mã (`00_spec.md`) | Yêu cầu | Test case kiểm | Dự kiến |
|---|---|---|---|
| D01 | FR04-R16 | TC-PROF-90 điểm (7) | Không đạt nếu "Thoát" là đăng xuất |
| D02 | FR04-R15 | TC-PROF-90 điểm (5) | Không đạt nếu "Chào, Test User" không được làm nổi |
| D03 | FR04-R13 | TC-PROF-90 điểm (4) | Không đạt nếu nhãn "Họ Tên" vẫn không có `*` |

Chưa kết luận bug; kết quả chỉ lấy từ lần chạy thật ở S6.

## 13. Phần sinh viên bổ sung ở S5

Sinh viên cho biết không bổ sung test case nào ở S5. Bộ test case cuối cùng của FR-04 gồm 34 test case như mục 2.

## 14. Ghi chú cho bước sau (S6)

- Ghi tên thiết bị, phiên bản Android, phiên bản Expo Go, ngày chạy; reset dữ liệu mẫu trước đợt chạy.
- Chụp ảnh theo mã test case: `screenshots/S6_TC-PROF-NN.png`.
- Ghi số chữ số ô Số điện thoại thực sự nhận (TC-PROF-34). Nếu ô giới hạn N ký tự, sinh viên có thể bổ sung N-1, N, N+1.
- Ghi câu chữ thông báo thành công, lỗi (Q17), hành vi sau khi lưu (Q21), mã HTTP và body phản hồi (Q20), chức năng nút "Thoát" (Q26).
