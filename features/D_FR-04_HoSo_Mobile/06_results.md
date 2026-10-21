# S6: Kết quả chạy test (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test trên điện thoại, chụp ảnh và chạy script; AI chuẩn bị khung và điền kết quả theo ảnh, log và ghi chú của sinh viên; sinh viên review và sửa
- Bản này: AI điền theo ảnh, log của sinh viên, sinh viên review. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-21 08:14 (UTC+07:00)
- 2026-10-21 08:16 (UTC+07:00): AI điền sẵn TC-PROF-90 điểm (1) đến (5) và một phần điểm (6) bằng cách đối chiếu ảnh S0 (`S0_01`, `S0_02`; giờ trên thanh trạng thái 06:59, cùng ngày chạy, SUT commit `85af3ba`) và thông tin sinh viên cung cấp ở S0 (O02, O12). Trạng thái do AI đề xuất; sinh viên xác nhận trên ứng dụng hiện tại. Các test case còn lại chờ sinh viên chạy
- 2026-10-21 09:03 (UTC+07:00): AI điền nhóm A theo log `S6_run_20261021_084416.log`; điền TC-PROF-01, 04, 30, 32, 33, 34, 101, 91 theo 11 ảnh `S6_TC-PROF-*.png` và log `chuan`, `get`. Theo ghi chú của sinh viên: Log `S6_chuan_TC-PROF-33_20261021_085321.log` thực ra là của TC-PROF-101; log `S6_get_TC-PROF-101_20261021_085329.log` chạy trước khi thao tác nên bỏ qua; TC-PROF-01, 04, 33 không có log `get`, EV3 lấy từ phản hồi đăng nhập trong log `chuan` của test case kế tiếp (hồ sơ trước khi đặt lại `S_CHUAN`). Dòng không có ảnh hoặc log ghi Not run. Trạng thái do AI đề xuất, sinh viên review
- 2026-10-21 09:11 (UTC+07:00): AI điền nhóm E theo log `S6_run_20261021_090657.log`, nhóm G theo log `S6_last_20261021_090658.log`; ghi thời điểm reset do sinh viên báo (08:11 trước đợt, 09:07 sau nhóm G, phiên điều phối reset); TC-PROF-91 Pass theo quyết định của sinh viên; QS03 sinh viên xác nhận; TC-PROF-90 điểm (6), (7) Not run (sinh viên bỏ vì thiếu thời gian); sửa giả thuyết ở QS01 theo kết quả nhóm E, thêm QS04; đếm lại mục 5
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
| Reset dữ liệu mẫu trước đợt test (thời điểm) | 08:11 21/10/2026. Phản hồi đăng nhập lúc 08:44:16 cho thấy hồ sơ ban đầu: Họ Tên `Test User`, `phone` và `shipping_address` là `null`, khớp dữ liệu mẫu (Q23) |
| File log API | Nhóm A: `logs/S6_run_20261021_084416.log`. Giao diện: `logs/S6_chuan_TC-PROF-*.log`, `logs/S6_get_TC-PROF-*.log` (08:44 đến 08:54). Nhóm E: `logs/S6_run_20261021_090657.log`. Nhóm G: `logs/S6_last_20261021_090658.log` |
| Reset dữ liệu sau nhóm G (thời điểm) | 09:07 21/10/2026, phiên điều phối reset ngay sau nhóm G. Sau TC-PROF-77, `test@eshop.com` có `role` `admin`; reset đưa về `user` |
| `GET /api/users/me` có trả `role`, `id` không (điền sau nhóm A) | Có: `id` = 2, `role` = `user`. Phản hồi còn có `password` (script đã che giá trị), `login_attempts`, `locked_until`, `reset_token` (QS02) |
| Số chữ số ô Số điện thoại thực sự nhận (điền sau TC-PROF-34) | Ít nhất 12: Gõ `091234567890` thì ô hiển thị đủ 12 chữ số (`S6_TC-PROF-34_1.png`) |
| Chức năng nút "Thoát" (điền sau TC-PROF-90 điểm 7, trả lời Q26) | Không xác định: TC-PROF-90 điểm (7) Not run, Q26 vẫn mở |

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
| 1 | TC-PROF-70 | API cập nhật hồ sơ hợp lệ cơ sở | `B(70)` | OUT2, OUT3 | `PUT` trả HTTP 200, body `{"message": "Profile updated"}`. EV3 trả `name` `Nguyen Van An 70`, `phone` `0912345678`, `shipping_address` `12/3 Lê Lợi, Quận 1, TP.HCM`, `email` `test@eshop.com`. Đặt `S_CHUAN` cũng thành công | Pass | Log | Nếu không đạt: Dùng reset dữ liệu mẫu thay cho `chuan` |

### B. Hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 2 | TC-PROF-01 | Cập nhật hợp lệ cơ sở | `Nguyen Van An 01`, `0912345678`, `12/3 Lê Lợi, Quận 1, TP.HCM` | OUT1, OUT3 | Hộp thoại "Lỗi": "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.", nút "OK". Không lưu: Phản hồi đăng nhập lúc 08:47:03 (log `chuan` của TC-PROF-04) trả `S_CHUAN` | Fail | `S6_TC-PROF-01_1.png` (đã nhập), `S6_TC-PROF-01_2.png` (thông báo) | Số `0912345678` (10 chữ số, bắt đầu bằng `0`) hợp lệ theo FR04-R04, FR04-R05 nhưng bị ứng dụng từ chối; cùng số qua API được lưu (TC-PROF-70), nên lỗi nằm ở kiểm tra của ứng dụng. Ứng viên bug S7. Chạy cùng TC-PROF-91 |
| 3 | TC-PROF-02 | Họ Tên có dấu | `Trần Thị Bích 02` | OUT1, lưu đúng dấu | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 4 | TC-PROF-03 | Họ Tên khoảng trắng đầu cuối | `␣Nguyen Van An 03␣` | OUT1, lưu `Nguyen Van An 03` | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 5 | TC-PROF-04 | Họ Tên có thẻ HTML | `<b>An 04</b>` | OUT1, hiển thị nguyên văn | Hộp thoại "Lỗi" về Số điện thoại như TC-PROF-01. Không lưu: Phản hồi đăng nhập lúc 08:48:33 (log `chuan` của TC-PROF-30) trả `S_CHUAN`. Sau khi đóng hộp thoại, ô Họ Tên hiển thị đúng chuỗi `<b>An 04</b>`, không in đậm (đây là giá trị đang gõ, chưa phải giá trị đã lưu) | Blocked | `S6_TC-PROF-04_1.png`, `S6_TC-PROF-04_2.png` | Bị chặn bởi lỗi của TC-PROF-01: Số điện thoại cơ sở bị ứng dụng từ chối nên không kiểm được việc lưu và hiển thị lại Họ Tên có thẻ HTML |
| 6 | TC-PROF-05 | Họ Tên có dấu nháy đơn | `O'Neil An 05` | OUT1, lưu nguyên văn | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 7 | TC-PROF-06 | Xóa trống Số điện thoại | Số điện thoại (để trống) | OUT1, lưu trống | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 8 | TC-PROF-07 | Xóa trống Địa chỉ | Địa chỉ (để trống) | OUT1, lưu trống | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 9 | TC-PROF-08 | Địa chỉ nhiều dòng | `12 Lê Lợi` `↵` `Quận 1` | OUT1, 2 dòng | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 10 | TC-PROF-09 | Địa chỉ chỉ khoảng trắng | `␣␣␣` | OUT1, lưu trống | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 11 | TC-PROF-10 | Địa chỉ có thẻ HTML | `<i>Kho A</i>, Quận 1` | OUT1, hiển thị nguyên văn | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |

### C. Không hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 12 | TC-PROF-30 | Họ Tên rỗng | Họ Tên (để trống), `0912345678` | ERR1 | Hộp thoại "Lỗi" về Số điện thoại ("... đúng 9-10 chữ số."), không nhắc Họ Tên. EV3 (`get` 08:51:28) trả `S_CHUAN` | Blocked | `S6_TC-PROF-30.png` | Bị chặn bởi lỗi của TC-PROF-01: Thông báo là về Số điện thoại cơ sở, nên không biết ứng dụng có từ chối Họ Tên rỗng không (A01). Vì vậy chưa kết luận được TC-PROF-90 điểm (4) |
| 13 | TC-PROF-31 | Họ Tên chỉ khoảng trắng | `␣␣␣`, `0912345678` | ERR1 | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 14 | TC-PROF-32 | Không bắt đầu bằng 0 | `Nguyen Van An 32`, `1912345678` | ERR2 | Hộp thoại "Lỗi": "Lỗi cập nhật", nút "OK". EV3 (`get` 08:52:37) trả `S_CHUAN` | Pass | `S6_TC-PROF-32.png` | Thông báo khác các test case khác: Số `1912345678` qua được kiểm tra của ứng dụng, bị hệ thống từ chối; thông báo không nêu nguyên nhân (đặc tả không quy định câu chữ). Chạy cùng TC-PROF-91 |
| 15 | TC-PROF-33 | Ít hơn 10 chữ số | `091234567` | ERR2 | Hộp thoại "Lỗi": "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.". Không lưu: Phản hồi đăng nhập lúc 08:53:21 (log `chuan` mang nhãn TC-PROF-33, thực ra của TC-PROF-101) trả `S_CHUAN` | Pass | `S6_TC-PROF-33.png` | Kết quả đúng mong đợi, nhưng thông báo nói cho phép 9 chữ số trong khi 9 chữ số bị từ chối (QS01) |
| 16 | TC-PROF-34 | Nhiều hơn 11 chữ số | `091234567890` | ERR2; ghi số chữ số ô nhận | Ô nhận đủ 12 chữ số. Hộp thoại "Lỗi": "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.". EV3 (`get` 08:54:40) trả `S_CHUAN` | Pass | `S6_TC-PROF-34_1.png`, `S6_TC-PROF-34_2.png` | |
| 17 | TC-PROF-35 | Có ký tự `*` | `0912*345678` | ERR2 | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 18 | TC-PROF-91 | Vị trí và ngôn ngữ của thông báo | Theo TC-PROF-01, TC-PROF-32 | Lỗi phía trên nút "Cập nhật" (R14); tiếng Việt (R10) | R14: Thông báo lỗi là hộp thoại của hệ thống, nằm giữa màn hình, phía trên nút "Cập nhật", không nằm bên dưới. R10: "Lỗi", "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.", "Lỗi cập nhật" bằng tiếng Việt; "OK" là chữ của hộp thoại hệ thống. Thông báo thành công chưa quan sát được (TC-PROF-01 không thành công) | Pass | `S6_TC-PROF-32.png`, `S6_TC-PROF-01_2.png` | Sinh viên chốt: Hộp thoại của hệ thống nằm phía trên nút, không nằm bên dưới, tính là đạt FR04-R14. Phần thông báo thành công chưa kiểm |

### D. Giá trị biên qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 19 | TC-PROF-100 | Số điện thoại 1 chữ số | `0` | ERR2 | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 20 | TC-PROF-101 | Số điện thoại 11 chữ số | `09123456789` | OUT1, lưu `09123456789` | Đã gõ `09123453789` (11 chữ số, bắt đầu bằng `0`). Hộp thoại "Lỗi": "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.". EV3 (`get` 08:53:58) trả `S_CHUAN` | Fail | `S6_TC-PROF-101_1.png`, `S6_TC-PROF-101_2.png` | Giá trị gõ khác kế hoạch một chữ số nhưng vẫn đúng điểm biên UB (11 chữ số, bắt đầu bằng `0`), nên kết quả vẫn dùng được. Số 11 chữ số hợp lệ theo FR04-R05 bị ứng dụng từ chối. Ứng viên bug S7 |
| 21 | TC-PROF-103 | Họ Tên 1 ký tự | `A` | OUT1, lưu `A` | | Not run | | Ngoài danh sách chạy tối thiểu (mục 7) |
| 22 | TC-PROF-104 | Họ Tên 1 ký tự có khoảng trắng hai bên | `␣B␣` | OUT1, lưu `B` | | Not run | | Lưu `␣B␣` là Khác giả định (A04). Ngoài danh sách chạy tối thiểu (mục 7) |

### E. API (script `run`)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 23 | TC-PROF-71 | Cắt khoảng trắng Số điện thoại | `"␣0912345678␣"` | OUT2, lưu `0912345678` | `PUT` trả HTTP 200 `{"message": "Profile updated"}`. EV3 trả `phone` là `␣0912345678␣` (giữ nguyên khoảng trắng hai đầu) | Fail | Log | Không cắt khoảng trắng (khác A08 (a)); giá trị được lưu bắt đầu bằng dấu cách, không bắt đầu bằng `0`, nên trái FR04-R04 theo cả hai phương án của A08. Ứng viên bug S7 |
| 24 | TC-PROF-72 | Body thiếu trường | Chỉ `name` | Giữ `phone`, `shipping_address`, hoặc từ chối | `PUT` chỉ có `name` trả HTTP 200. EV3 trả `name` `Nguyen Van An 72`, `phone` `null`, `shipping_address` `null`: Hai trường không gửi bị xóa | Khác giả định | Log | Khác A16 (d): Trường không gửi bị xóa (kết quả mong đợi ghi không đạt). Đặc tả không nói về body thiếu trường; sinh viên xét ở S7 |
| 25 | TC-PROF-73 | Dấu phân cách `-` | `0912-345678` | ERR2 (API) | `PUT` với `phone` `0912-345678` trả HTTP 200. EV3 trả `phone` `0912-345678`, `name` `Nguyen Van An 73` | Khác giả định | Log | Khác A06 (a): Hệ thống nhận và lưu dấu `-` nguyên văn. Số vẫn đủ 10 chữ số và bắt đầu bằng `0`, nên chữ đặc tả không bị vi phạm trực tiếp; sinh viên xét ở S7 |
| 26 | TC-PROF-74 | Không bắt đầu bằng 0 | `1912345678` | ERR2 (API) | `PUT` với `phone` `1912345678` trả HTTP 200. EV3 trả `phone` `1912345678` | Fail | Log | Hệ thống lưu số không bắt đầu bằng `0` (trái FR04-R04). Ứng viên bug S7 |
| 27 | TC-PROF-75 | Ít hơn 10 chữ số | `091234567` | ERR2 (API) | `PUT` với `phone` `091234567` (9 chữ số) trả HTTP 200. EV3 trả `phone` `091234567` | Fail | Log | Hệ thống lưu số 9 chữ số (trái FR04-R05, biên LB-1). Ứng viên bug S7 |
| 28 | TC-PROF-78 | Không có header Authorization | PUT và GET không header | ERR4 | `PUT` và `GET` không có header: Cả hai trả HTTP 401 `{"error": "Unauthorized"}`. EV3 (token hợp lệ) trả `S_CHUAN` | Pass | Log | |
| 29 | TC-PROF-79 | Token không hợp lệ | `Bearer abc` | ERR4 | `PUT` và `GET` với `Bearer abc`: Cả hai trả HTTP 403 `{"error": "Forbidden"}`. EV3 trả `S_CHUAN` | Pass | Log | Mã 403 cho token sai, 401 cho thiếu token; đặc tả không nêu mã |
| 30 | TC-PROF-80 | Gửi `id` của admin | `"id": <id admin>` | OUT4 (hồ sơ admin không đổi) | Admin `id` = 1. `PUT` bằng token test kèm `"id": 1` trả HTTP 200. Hồ sơ admin trước và sau giống hệt (`Admin User`, `phone` `null`, `shipping_address` `null`). Hồ sơ test được cập nhật thành `B(80)` | Pass | Log | Hệ thống bỏ qua `id`, cập nhật hồ sơ của chủ token (A15 (c)) |
| 31 | TC-PROF-102 | Số điện thoại 11 chữ số qua API | `09123456789` | OUT2 | `PUT` với `phone` `09123456789` trả HTTP 200. EV3 trả `phone` `09123456789` | Pass | Log | Hệ thống nhận 11 chữ số; ứng dụng từ chối cùng biên (TC-PROF-101) |

### F. Checklist giao diện (sau các test case giao diện khác)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 32 | TC-PROF-90 (1) | Mở màn Hồ sơ (R09) | Bấm "Chào, Test User" | Mở "Hồ sơ của bạn" | Bấm "Chào, Test User" mở màn có tiêu đề "Hồ sơ của bạn" (cách mở do sinh viên cung cấp ở S0, O02) | Pass | `S0_02_ho_so.png` | AI điền từ ảnh S0 |
| 33 | TC-PROF-90 (2) | Ngôn ngữ (R10) | Chữ tĩnh | Tiếng Việt, trừ tên sản phẩm và thuật ngữ | Chữ tĩnh: "Hồ sơ của bạn", "Email (Không đổi)", "Họ Tên", "Số điện thoại", "VD: 0912345678", "Địa chỉ giao hàng", "Cập nhật", "Thoát", "Lịch sử đơn hàng", "Bạn chưa có đơn hàng nào.", "Chào, Test User", "Giỏ (0)". Không phải tiếng Việt: "EShop Mobile", "EShop SUT" (tên sản phẩm), "Email" (thuật ngữ) | Pass | `S0_02_ho_so.png` | AI điền từ ảnh S0. Thông báo thành công, lỗi xét ở TC-PROF-91 |
| 34 | TC-PROF-90 (3) | Màu nút "Cập nhật" (R11) | | Xanh dương | Nút "Cập nhật" nền xanh dương, chữ trắng đậm | Pass | `S0_02_ho_so.png` | AI điền từ ảnh S0 |
| 35 | TC-PROF-90 (4) | Dấu `*` (R13) | Nhãn các ô | "Họ Tên" có `*` (A01 (a)) | Không nhãn nào có `*`: "Email (Không đổi)", "Họ Tên", "Số điện thoại", "Địa chỉ giao hàng" | Fail (đề xuất) | `S0_02_ho_so.png` | AI điền từ ảnh S0. D03. Xét lại sau TC-PROF-30: Nếu hệ thống chấp nhận Họ Tên rỗng (TC-PROF-30 là Khác giả định) thì điểm này chuyển thành Khác giả định |
| 36 | TC-PROF-90 (5) | Làm nổi mục đang chọn (R15) | So "Chào, Test User" ở Hồ sơ và ở "Danh sách sản phẩm" | Được làm nổi | "Chào, Test User" ở màn Hồ sơ giống hệt ở màn "Danh sách sản phẩm": Chữ trắng, không gạch chân, không có nền riêng | Fail (đề xuất) | `S0_01_sau_dang_nhap.png`, `S0_02_ho_so.png` | AI điền từ ảnh S0. D02; thanh trên được coi là thanh điều hướng (`01_io.md` quyết định 9) |
| 37 | TC-PROF-90 (6) | Không sửa được Email (R06) | Chạm, nhấn giữ, thử dán | Không hiện bàn phím, không dán được, Email giữ nguyên |  | Not run |  | Sinh viên bỏ vì thiếu thời gian. Phần chạm (không hiện bàn phím) đã có từ S0, O12 |
| 38 | TC-PROF-90 (7) | Nút "Thoát" (R12, R16) | Bấm "Thoát" (bước cuối) | Nút hủy, nguy hiểm thì đỏ là đạt (R12); nếu đăng xuất thì nhãn phải là "Đăng xuất" (R16) |  | Not run |  | Sinh viên bỏ vì thiếu thời gian. D01, Q26 chưa kết luận; FR04-R12, FR04-R16 chưa kiểm |

### G. Chạy cuối cùng (script `last`), reset dữ liệu ngay sau

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 39 | TC-PROF-77 | Gửi `role` | `"role": "admin"` | OUT4 (vai trò không đổi) | EV3 trước: `role` `user`. `PUT` `B(77)` kèm `"role": "admin"` trả HTTP 200. EV3 sau: `role` `admin` | Fail | Log | Người dùng tự nâng vai trò lên `admin` (trái FR04-R08, SEC-06). Phiên điều phối reset lúc 09:07. Ứng viên bug S7, mức nghiêm trọng cao |
| 40 | TC-PROF-76 | Gửi `email` | `"email": "tc76@eshop.com"` | OUT4 (Email không đổi) | `PUT` `B(76)` kèm `"email": "tc76@eshop.com"` trả HTTP 200. EV3: `email` vẫn `test@eshop.com`; các trường khác cập nhật theo `B(76)` | Pass | Log | Hệ thống bỏ qua `email` (A13 (c)). Lúc chạy, `role` đang là `admin` do TC-PROF-77; không ảnh hưởng điểm kiểm Email |

## 5. Tổng hợp

Đếm từ bảng ở mục 4 sau khi sinh viên review xong. TC-PROF-90 tính là 1 test case: Pass khi mọi điểm Pass hoặc Không áp dụng; Fail khi có điểm Fail.

| Nhóm | Số TC | Pass | Fail | Khác giả định | Blocked | Not run |
|---|---|---|---|---|---|---|
| A. Chuẩn bị và API cơ sở | 1 | 1 | 0 | 0 | 0 | 0 |
| B. Hợp lệ qua giao diện | 10 | 0 | 1 | 0 | 1 | 8 |
| C. Không hợp lệ qua giao diện | 7 | 4 | 0 | 0 | 1 | 2 |
| D. Giá trị biên qua giao diện | 4 | 0 | 1 | 0 | 0 | 3 |
| E. API | 9 | 4 | 3 | 2 | 0 | 0 |
| F. Checklist | 1 | 0 | 1 | 0 | 0 | 0 |
| G. Chạy cuối | 2 | 1 | 1 | 0 | 0 | 0 |
| **Tổng** | **34** | **10** | **7** | **2** | **2** | **13** |

Chốt lúc 2026-10-21 09:11. Đã chạy (gồm Pass, Fail, Khác giả định, Blocked): 21; Not run: 13 test case giao diện ngoài danh sách tối thiểu (TC-PROF-02, 03, 05 đến 10, 31, 35, 100, 103, 104; sinh viên bỏ TC-PROF-06 vì thiếu thời gian). TC-PROF-90 tính Fail vì điểm (4), (5) Fail; điểm (6), (7) Not run. Fail: TC-PROF-01, 101, 90, 71, 74, 75, 77. Khác giả định: TC-PROF-72, 73. Blocked: TC-PROF-04, 30 (do lỗi của TC-PROF-01)

## 6. Quan sát ngoài test case (cân nhắc ở S7)

Những điều nhìn thấy trong lúc chạy test nhưng không thuộc kết quả mong đợi của test case nào.

| Mã | Quan sát | Thấy khi chạy | Ảnh | Yêu cầu có thể liên quan |
|---|---|---|---|---|
| QS01 | Thông báo lỗi của ứng dụng nêu quy tắc "đúng 9-10 chữ số", khác FR-04 ("từ 10–11 chữ số"). Mọi số bắt đầu bằng `0` đã thử (9, 10, 11, 12 chữ số) đều bị từ chối với thông báo này; số `1912345678` qua được kiểm tra của ứng dụng (bị hệ thống từ chối với "Lỗi cập nhật"). Cập nhật sau nhóm E: Hệ thống không kiểm Số điện thoại (lưu `1912345678`, `091234567`, `0912-345678`, TC-PROF-73 đến 75), nên giả thuyết ban đầu của AI ("hệ thống đòi bắt đầu bằng `0`") là sai. Qua ứng dụng, chưa có lần lưu Số điện thoại nào thành công (QS04) | TC-PROF-01, 30, 32, 33, 34, 101 | `S6_TC-PROF-33.png`, `S6_TC-PROF-32.png` | FR04-R02, FR04-R04, FR04-R05 |
| QS02 | Phản hồi `POST /api/login` và `GET /api/users/me` có trường `password` (script che giá trị nên không biết là văn bản rõ hay đã băm), cùng `reset_token`, `login_attempts`, `locked_until` | Nhóm A, mọi log | Log | SEC-01 (tham khảo); có thể thuộc FR-02, FR-19 |
| QS03 | Màn Hồ sơ không hiển thị Địa chỉ đã lưu: `S6_TC-PROF-04_2` (chụp sau khi mở lại màn Hồ sơ) có ô Địa chỉ trống, trong khi hệ thống đang lưu `1 Nguyen Hue, Quận 1` (`S_CHUAN`, log `chuan` 08:47:03). Sinh viên xác nhận. Các ảnh `S6_TC-PROF-101_1`, `S6_TC-PROF-34_1` cũng có ô Địa chỉ trống | TC-PROF-04, 101, 34 | `S6_TC-PROF-04_2.png` | FR04-R03 (EV4) |
| QS04 | Qua ứng dụng, số `1912345678` nhận "Lỗi cập nhật" và không được lưu (TC-PROF-32), trong khi cùng số gửi qua API được lưu (TC-PROF-74). Nguyên nhân lần lưu thất bại không quan sát được bằng hộp đen. Cùng QS01, chưa có lần cập nhật hồ sơ có Số điện thoại nào thành công qua ứng dụng | TC-PROF-32, TC-PROF-74 | `S6_TC-PROF-32.png`, log | FR04-R01 đến FR04-R03 |

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
