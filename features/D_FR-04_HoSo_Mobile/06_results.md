# S6: Kết quả chạy test (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test trên điện thoại, chụp ảnh và chạy script; AI chuẩn bị khung và điền kết quả theo ảnh, log và ghi chú của sinh viên; sinh viên review và sửa
- Bản này: AI điền theo ảnh, log của sinh viên, sinh viên review. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-21 08:14 (UTC+07:00)
- 2026-10-21 08:16 (UTC+07:00): AI điền sẵn TC-PROF-90 điểm (1) đến (5) và một phần điểm (6) bằng cách đối chiếu ảnh S0 (`S0_01`, `S0_02`; giờ trên thanh trạng thái 06:59, cùng ngày chạy, SUT commit `85af3ba`) và thông tin sinh viên cung cấp ở S0 (O02, O12). Trạng thái do AI đề xuất; sinh viên xác nhận trên ứng dụng hiện tại. Các test case còn lại chờ sinh viên chạy
- Căn cứ: `05_final_tc.md` (34 test case, quy trình mục 1.4, thứ tự chạy mục 9, giới hạn quan sát mục 10, khác biệt chờ xác nhận mục 12). Cấu trúc theo `features/A_FR-01_DangKy/06_results.md` (sinh viên cho phép đọc riêng file này; chỉ lấy cấu trúc, không dùng kết quả của FR-01)
- Cách chạy gọn (theo yêu cầu của sinh viên): Nhóm API chạy bằng `scripts/run_api_tests.py`; giao diện chỉ chạy danh sách tối thiểu ở mục 7, các test case giao diện khác ghi Not run

---

## 1. Môi trường

| Mục | Giá trị |
|---|---|
| Ngày chạy | 21/10/2026 |
| Người chạy | Nguyễn Thị Ánh Ngọc |
| Thiết bị | Samsung Galaxy S21 Ultra (Android 15) |
| Ứng dụng | EShop chạy bằng Expo Go 54.0.8 |
| SUT | EShop, commit `85af3ba` |
| Backend | `http://localhost:3000`, điện thoại truy cập qua `adb reverse` |
| Reset dữ liệu mẫu trước đợt test (thời điểm) | (sinh viên báo) |
| File log API | (điền sau khi chạy script) |
| Reset dữ liệu sau nhóm G (thời điểm) | (sinh viên báo) |
| `GET /api/users/me` có trả `role`, `id` không (điền sau nhóm A) | |
| Số chữ số ô Số điện thoại thực sự nhận (điền sau TC-PROF-34) | |
| Chức năng nút "Thoát" (điền sau TC-PROF-90 điểm 7, trả lời Q26) | |

## 2. Cách điền

- **Kết quả thực tế:** Ghi đúng những gì quan sát được: Nguyên văn thông báo, hình thức (hộp thoại, chữ dưới ô...), vị trí so với nút "Cập nhật"; giá trị trong ô sau khi mở lại màn Hồ sơ (EV4); giá trị EV3 lấy từ log của lệnh `get`. Test case API: Mã HTTP và body, lấy từ log của script.
- **Trạng thái:**
  - Pass: Kết quả thực tế khớp kết quả mong đợi.
  - Fail: Không khớp đặc tả. Mô tả khác ở đâu trong cột Ghi chú; ứng viên bug cho S7.
  - Khác giả định: Hệ thống làm khác giả định đã chốt ở S2 (A01 đến A19), không trái chữ đặc tả. Xét ở S7 trước khi coi là bug (`04_bva.md` quyết định 5).
  - Blocked: Không chạy được vì điều kiện ngoài test case (ví dụ TC-PROF-80 không lấy được `id`). Ghi lý do.
  - Không áp dụng: Điểm kiểm không áp dụng theo kết quả quan sát (ví dụ FR04-R16 nếu "Thoát" không phải đăng xuất).
  - Not run: Chưa chạy, hoặc sinh viên chọn không chạy.
- **Script:** Cột "Gợi ý" trong log là so sánh máy móc; trạng thái cuối do sinh viên review.
- **Ảnh:** `screenshots/S6_TC-PROF-<số>.png`; test case nhiều ảnh thêm `_1`, `_2`. Ảnh chụp cả màn hình điện thoại.
- **Kết quả mong đợi:** Đọc theo bảng mã ở mục 3.

## 3. Mã kết quả mong đợi

| Mã | Đạt khi |
|---|---|
| OUT1 | Có thông báo thành công; sau EV4 các ô hiển thị giá trị mới; EV3 trả giá trị mới |
| OUT2 | API trả mã 2xx; EV3 trả giá trị mới |
| OUT3 | EV3 trả hồ sơ có Email đúng của chủ token |
| OUT4 | `email`, `role`, hồ sơ người khác không đổi; phản hồi thành công hay thất bại đều chấp nhận |
| ERR1, ERR2 (giao diện) | Có thông báo lỗi; sau EV4 và EV3, cả 3 trường vẫn là `S_CHUAN` |
| ERR2 (API) | Không trả phản hồi thành công; EV3 trả `S_CHUAN` |
| ERR4 | Không trả phản hồi thành công; `GET` không trả hồ sơ; EV3 (token hợp lệ) trả `S_CHUAN` |

`S_CHUAN`: Họ Tên `Test User`, Số điện thoại `0900000000`, Địa chỉ `1 Nguyen Hue, Quận 1`. Giá trị cơ sở: Họ Tên `Nguyen Van An <số>`, Số điện thoại `0912345678`, Địa chỉ `12/3 Lê Lợi, Quận 1, TP.HCM`. `␣` là một dấu cách. Giá trị đầy đủ ở `05_final_tc.md`.

## 4. Kết quả theo thứ tự chạy

Thứ tự theo `05_final_tc.md` mục 9: Reset dữ liệu; nhóm A; nhóm B đến D (giao diện, mỗi test case trước khi làm chạy `chuan`, sau khi làm chạy `get`); nhóm E; nhóm F; nhóm G cuối cùng; reset dữ liệu ngay sau đó.

### A. Chuẩn bị và API cơ sở (script `run`, chạy đầu tiên)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1 | TC-PROF-70 | API cập nhật hồ sơ hợp lệ cơ sở | `B(70)` | OUT2, OUT3 | | | Log | Nếu không đạt: Dùng reset dữ liệu mẫu thay cho `chuan` |

### B. Hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 2 | TC-PROF-01 | Cập nhật hợp lệ cơ sở | `Nguyen Van An 01`, `0912345678`, `12/3 Lê Lợi, Quận 1, TP.HCM` | OUT1, OUT3 | | | | Chạy cùng TC-PROF-91 (thông báo thành công) |
| 3 | TC-PROF-02 | Họ Tên có dấu | `Trần Thị Bích 02` | OUT1, lưu đúng dấu | | | | |
| 4 | TC-PROF-03 | Họ Tên khoảng trắng đầu cuối | `␣Nguyen Van An 03␣` | OUT1, lưu `Nguyen Van An 03` | | | | |
| 5 | TC-PROF-04 | Họ Tên có thẻ HTML | `<b>An 04</b>` | OUT1, hiển thị nguyên văn | | | | |
| 6 | TC-PROF-05 | Họ Tên có dấu nháy đơn | `O'Neil An 05` | OUT1, lưu nguyên văn | | | | |
| 7 | TC-PROF-06 | Xóa trống Số điện thoại | Số điện thoại (để trống) | OUT1, lưu trống | | | | |
| 8 | TC-PROF-07 | Xóa trống Địa chỉ | Địa chỉ (để trống) | OUT1, lưu trống | | | | |
| 9 | TC-PROF-08 | Địa chỉ nhiều dòng | `12 Lê Lợi` `↵` `Quận 1` | OUT1, 2 dòng | | | | |
| 10 | TC-PROF-09 | Địa chỉ chỉ khoảng trắng | `␣␣␣` | OUT1, lưu trống | | | | |
| 11 | TC-PROF-10 | Địa chỉ có thẻ HTML | `<i>Kho A</i>, Quận 1` | OUT1, hiển thị nguyên văn | | | | |

### C. Không hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 12 | TC-PROF-30 | Họ Tên rỗng | Họ Tên (để trống), `0912345678` | ERR1 | | | | |
| 13 | TC-PROF-31 | Họ Tên chỉ khoảng trắng | `␣␣␣`, `0912345678` | ERR1 | | | | |
| 14 | TC-PROF-32 | Không bắt đầu bằng 0 | `Nguyen Van An 32`, `1912345678` | ERR2 | | | | Chạy cùng TC-PROF-91 (vị trí thông báo lỗi) |
| 15 | TC-PROF-33 | Ít hơn 10 chữ số | `091234567` | ERR2 | | | | |
| 16 | TC-PROF-34 | Nhiều hơn 11 chữ số | `091234567890` | ERR2; ghi số chữ số ô nhận | | | | |
| 17 | TC-PROF-35 | Có ký tự `*` | `0912*345678` | ERR2 | | | | |
| 18 | TC-PROF-91 | Vị trí và ngôn ngữ của thông báo | Theo TC-PROF-01, TC-PROF-32 | Lỗi phía trên nút "Cập nhật" (R14); tiếng Việt (R10) | | | | |

### D. Giá trị biên qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 19 | TC-PROF-100 | Số điện thoại 1 chữ số | `0` | ERR2 | | | | |
| 20 | TC-PROF-101 | Số điện thoại 11 chữ số | `09123456789` | OUT1, lưu `09123456789` | | | | |
| 21 | TC-PROF-103 | Họ Tên 1 ký tự | `A` | OUT1, lưu `A` | | | | |
| 22 | TC-PROF-104 | Họ Tên 1 ký tự có khoảng trắng hai bên | `␣B␣` | OUT1, lưu `B` | | | | Lưu `␣B␣` là Khác giả định (A04) |

### E. API (script `run`)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 23 | TC-PROF-71 | Cắt khoảng trắng Số điện thoại | `"␣0912345678␣"` | OUT2, lưu `0912345678` | | | Log | |
| 24 | TC-PROF-72 | Body thiếu trường | Chỉ `name` | Giữ `phone`, `shipping_address`, hoặc từ chối | | | Log | |
| 25 | TC-PROF-73 | Dấu phân cách `-` | `0912-345678` | ERR2 (API) | | | Log | |
| 26 | TC-PROF-74 | Không bắt đầu bằng 0 | `1912345678` | ERR2 (API) | | | Log | |
| 27 | TC-PROF-75 | Ít hơn 10 chữ số | `091234567` | ERR2 (API) | | | Log | |
| 28 | TC-PROF-78 | Không có header Authorization | PUT và GET không header | ERR4 | | | Log | |
| 29 | TC-PROF-79 | Token không hợp lệ | `Bearer abc` | ERR4 | | | Log | |
| 30 | TC-PROF-80 | Gửi `id` của admin | `"id": <id admin>` | OUT4 (hồ sơ admin không đổi) | | | Log | Blocked nếu GET admin không có `id` |
| 31 | TC-PROF-102 | Số điện thoại 11 chữ số qua API | `09123456789` | OUT2 | | | Log | |

### F. Checklist giao diện (sau các test case giao diện khác)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 32 | TC-PROF-90 (1) | Mở màn Hồ sơ (R09) | Bấm "Chào, Test User" | Mở "Hồ sơ của bạn" | Bấm "Chào, Test User" mở màn có tiêu đề "Hồ sơ của bạn" (cách mở do sinh viên cung cấp ở S0, O02) | Pass | `S0_02_ho_so.png` | AI điền từ ảnh S0 |
| 33 | TC-PROF-90 (2) | Ngôn ngữ (R10) | Chữ tĩnh | Tiếng Việt, trừ tên sản phẩm và thuật ngữ | Chữ tĩnh: "Hồ sơ của bạn", "Email (Không đổi)", "Họ Tên", "Số điện thoại", "VD: 0912345678", "Địa chỉ giao hàng", "Cập nhật", "Thoát", "Lịch sử đơn hàng", "Bạn chưa có đơn hàng nào.", "Chào, Test User", "Giỏ (0)". Không phải tiếng Việt: "EShop Mobile", "EShop SUT" (tên sản phẩm), "Email" (thuật ngữ) | Pass | `S0_02_ho_so.png` | AI điền từ ảnh S0. Thông báo thành công, lỗi xét ở TC-PROF-91 |
| 34 | TC-PROF-90 (3) | Màu nút "Cập nhật" (R11) | | Xanh dương | Nút "Cập nhật" nền xanh dương, chữ trắng đậm | Pass | `S0_02_ho_so.png` | AI điền từ ảnh S0 |
| 35 | TC-PROF-90 (4) | Dấu `*` (R13) | Nhãn các ô | "Họ Tên" có `*` (A01 (a)) | Không nhãn nào có `*`: "Email (Không đổi)", "Họ Tên", "Số điện thoại", "Địa chỉ giao hàng" | Fail (đề xuất) | `S0_02_ho_so.png` | AI điền từ ảnh S0. D03. Xét lại sau TC-PROF-30: Nếu hệ thống chấp nhận Họ Tên rỗng (TC-PROF-30 là Khác giả định) thì điểm này chuyển thành Khác giả định |
| 36 | TC-PROF-90 (5) | Làm nổi mục đang chọn (R15) | So "Chào, Test User" ở Hồ sơ và ở "Danh sách sản phẩm" | Được làm nổi | "Chào, Test User" ở màn Hồ sơ giống hệt ở màn "Danh sách sản phẩm": Chữ trắng, không gạch chân, không có nền riêng | Fail (đề xuất) | `S0_01_sau_dang_nhap.png`, `S0_02_ho_so.png` | AI điền từ ảnh S0. D02; thanh trên được coi là thanh điều hướng (`01_io.md` quyết định 9) |
| 37 | TC-PROF-90 (6) | Không sửa được Email (R06) | Chạm, nhấn giữ, thử dán | Không hiện bàn phím, không dán được, Email giữ nguyên | Chạm: Không hiện bàn phím (sinh viên cung cấp ở S0, O12). Nhấn giữ, dán: Chưa thử | | | Một phần do AI điền từ thông tin S0; phần nhấn giữ, dán chạy ở mục 7 thứ tự 8 |
| 38 | TC-PROF-90 (7) | Nút "Thoát" (R12, R16) | Bấm "Thoát" (bước cuối) | Nút hủy, nguy hiểm thì đỏ là đạt (R12); nếu đăng xuất thì nhãn phải là "Đăng xuất" (R16) | | | | D01; ghi chức năng vào mục 1 |

### G. Chạy cuối cùng (script `last`), reset dữ liệu ngay sau

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 39 | TC-PROF-77 | Gửi `role` | `"role": "admin"` | OUT4 (vai trò không đổi) | | | Log | Không quan sát được nếu GET không trả `role` |
| 40 | TC-PROF-76 | Gửi `email` | `"email": "tc76@eshop.com"` | OUT4 (Email không đổi) | | | Log | |

## 5. Tổng hợp

Đếm từ bảng ở mục 4 sau khi sinh viên review xong. TC-PROF-90 tính là 1 test case: Pass khi mọi điểm Pass hoặc Không áp dụng; Fail khi có điểm Fail.

| Nhóm | Số TC | Pass | Fail | Khác giả định | Blocked | Not run |
|---|---|---|---|---|---|---|
| A. Chuẩn bị và API cơ sở | 1 | | | | | |
| B. Hợp lệ qua giao diện | 10 | | | | | |
| C. Không hợp lệ qua giao diện | 7 | | | | | |
| D. Giá trị biên qua giao diện | 4 | | | | | |
| E. API | 9 | | | | | |
| F. Checklist | 1 | | | | | |
| G. Chạy cuối | 2 | | | | | |
| **Tổng** | **34** | | | | | |

## 6. Quan sát ngoài test case (cân nhắc ở S7)

Những điều nhìn thấy trong lúc chạy test nhưng không thuộc kết quả mong đợi của test case nào.

| Mã | Quan sát | Thấy khi chạy | Ảnh | Yêu cầu có thể liên quan |
|---|---|---|---|---|

## 7. Danh sách chạy tối thiểu trên điện thoại

Mỗi test case: Trước khi làm chạy `python scripts/run_api_tests.py chuan --tag TC-PROF-<số>`, rồi bấm "Chào, Test User" để mở lại màn Hồ sơ; làm theo cột "Làm gì" (ẩn bàn phím trước khi bấm "Cập nhật"); chụp ảnh; sau đó chạy `python scripts/run_api_tests.py get --tag TC-PROF-<số>` (EV3, ghi log). Lệnh chạy từ thư mục `features/D_FR-04_HoSo_Mobile/`.

| Thứ tự | Test case | Làm gì | Chụp màn hình nào | Tên ảnh |
|---|---|---|---|---|
| 1 | TC-PROF-01 (kèm TC-PROF-91) | Họ Tên `Nguyen Van An 01`; Số điện thoại `0912345678`; Địa chỉ `12/3 Lê Lợi, Quận 1, TP.HCM` (dán); bấm "Cập nhật" | (1) Khi thông báo thành công đang hiện; (2) màn Hồ sơ sau khi rời đi và mở lại | `S6_TC-PROF-01_1.png`, `S6_TC-PROF-01_2.png` |
| 2 | TC-PROF-04 | Họ Tên `<b>An 04</b>`; Số điện thoại `0912345678`; bấm "Cập nhật"; rời màn rồi mở lại | Màn Hồ sơ sau khi mở lại, thấy ô Họ Tên và lời chào trên thanh trên | `S6_TC-PROF-04.png` |
| 3 | TC-PROF-30 | Xóa trống Họ Tên; Số điện thoại `0912345678`; bấm "Cập nhật" | Khi thông báo lỗi đang hiện, thấy cả nút "Cập nhật" | `S6_TC-PROF-30.png` |
| 4 | TC-PROF-32 (kèm TC-PROF-91) | Họ Tên `Nguyen Van An 32`; Số điện thoại `1912345678`; bấm "Cập nhật" | Khi thông báo lỗi đang hiện, thấy vị trí thông báo so với nút "Cập nhật" | `S6_TC-PROF-32.png` |
| 5 | TC-PROF-33 | Họ Tên `Nguyen Van An 33`; Số điện thoại `091234567` (9 chữ số); bấm "Cập nhật" | Khi thông báo hiện | `S6_TC-PROF-33.png` |
| 6 | TC-PROF-101 | Họ Tên `Nguyen Van An 101`; Số điện thoại `09123456789` (11 chữ số); bấm "Cập nhật" | (1) Ô Số điện thoại trước khi bấm, thấy đủ số đã gõ; (2) khi thông báo hiện | `S6_TC-PROF-101_1.png`, `S6_TC-PROF-101_2.png` |
| 7 | TC-PROF-34 | Họ Tên `Nguyen Van An 34`; gõ `091234567890` (12 chữ số); bấm "Cập nhật" | (1) Ô Số điện thoại sau khi gõ, để đếm số chữ số ô nhận; (2) khi thông báo hiện | `S6_TC-PROF-34_1.png`, `S6_TC-PROF-34_2.png` |
| 8 | TC-PROF-90 điểm (6), (7) | (6) Chạm, nhấn giữ ô Email, thử dán một chuỗi; (7) cuối cùng bấm "Thoát" | (6) Sau khi nhấn giữ hoặc thử dán; (7) màn hình ngay sau khi bấm "Thoát" | `S6_TC-PROF-90_6.png`, `S6_TC-PROF-90_7.png` |

Thứ tự lệnh script cho cả đợt:

1. `python scripts/run_api_tests.py run --dry-run` (xem trước yêu cầu, không gửi).
2. `python scripts/run_api_tests.py run --only TC-PROF-70` (nhóm A).
3. Danh sách giao diện ở bảng trên (thứ tự 1 đến 7).
4. `python scripts/run_api_tests.py run --only TC-PROF-71,TC-PROF-72,TC-PROF-73,TC-PROF-74,TC-PROF-75,TC-PROF-78,TC-PROF-79,TC-PROF-80,TC-PROF-102` (nhóm E).
5. Thứ tự 8 của bảng trên (TC-PROF-90; nếu "Thoát" đăng xuất thì không cần đăng nhập lại cho bước sau).
6. `python scripts/run_api_tests.py last` (nhóm G), rồi reset dữ liệu mẫu ngay.
