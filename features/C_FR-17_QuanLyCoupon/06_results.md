# S6: Kết quả chạy test (FR-17 Quản lý mã giảm giá)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test, chụp ảnh và chạy script; AI chuẩn bị khung và điền kết quả theo ảnh, log và ghi chú của sinh viên; sinh viên review và sửa
- Bản này: AI điền theo ảnh, log của sinh viên, sinh viên review. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-20 22:35 (UTC+07:00)
- 2026-10-20 22:35 (UTC+07:00): AI điền sẵn TC-CPN-50, TC-CPN-90, TC-CPN-92, TC-CPN-93, TC-CPN-94 và phần quan sát của TC-CPN-91 bằng cách đối chiếu ảnh S0 (chụp 18/10/2026); trạng thái ghi "(đề xuất)", sinh viên xác nhận trên trang hiện tại. Điền dòng "Ô Mã coupon có tự chuyển chữ hoa" ở mục 1 theo thông tin sinh viên cung cấp ở S5; thêm một quan sát ngoài phạm vi ở mục 6. Mọi test case cần nhập dữ liệu hay gọi API do sinh viên chạy và điền
- 2026-10-20 22:50 (UTC+07:00): Theo yêu cầu của sinh viên, AI điền ngày chạy, người chạy, hệ điều hành, trình duyệt (giống `A_FR-01_DangKy/06_results.md`) và múi giờ ở mục 1; bỏ chữ "(đề xuất)" ở các trạng thái; điền trạng thái TC-CPN-91. Sinh viên review và tự sửa nếu sai
- 2026-10-21 00:01 (UTC+07:00): AI viết script `scripts/run_api_tests.py` cho nhóm F (và TC-CPN-61, 82, 130, 144 chạy bằng `--only`); sửa dòng "Bước", "Bản này" cho đúng cách làm thực tế; điền ngày chạy 21/10/2026, thời điểm reset 23:41 20/10/2026, đường dẫn log ở mục 1; ghi lệnh chạy ở nhóm A, F, G
- 2026-10-21 01:14 (UTC+07:00): AI điền kết quả theo 21 ảnh `screenshots/S6_*`, 3 log trong `logs/` và ghi chú của sinh viên (S6 rút gọn): Mục 1, thứ tự chạy thực tế ở mục 4, kết quả theo dòng ở mục 5, 2 quan sát ở mục 2 và 6, tổng hợp ở mục 7. Test case không có ảnh hay log ghi Not run. TC-CPN-02 để trống trạng thái, chờ sinh viên chọn
- 2026-10-21 01:21 (UTC+07:00): AI cập nhật theo trả lời của sinh viên: TC-CPN-02 theo 3 ảnh chụp lại; không có hộp thoại xác nhận khi xóa nên TC-CPN-52 là Không áp dụng; ghi chú TC-CPN-69 về quy ước 5xx; bong bóng tiếng Anh của trình duyệt tính vào FR17-R14 ở TC-CPN-91 (như FR-01); điền quan sát placeholder ở mục 6; đếm lại mục 7
- 2026-10-21 01:25 (UTC+07:00): AI cập nhật theo trả lời của sinh viên: Ghi việc xóa dòng `FR17TC02` cũ trước khi chạy lại; tính lịch chọn ngày bằng tiếng Anh vào lý do Fail của TC-CPN-91
- 2026-10-21 01:30 (UTC+07:00): Claude (phiên điều phối) sửa theo yêu cầu của sinh viên: Ghi giờ cụ thể cho 3 dòng lịch sử ở trên (theo thời điểm AI ghi file); điền 4 ô trống ở mục 1 (không có bằng chứng, nhóm H không chạy); ghi "Không chạy" ở cột Kết quả thực tế của 69 dòng Not run (như FR-01). Không đổi trạng thái nào
- Căn cứ: `05_final_tc.md` (115 test case, thứ tự chạy ở mục 10, giới hạn quan sát ở mục 11); cấu trúc theo `A_FR-01_DangKy/06_results.md` (sinh viên cho phép tham khảo)

---

## 1. Môi trường

| Mục | Giá trị |
|---|---|
| Ngày chạy | 21/10/2026 |
| Người chạy | Nguyễn Thị Ánh Ngọc |
| Hệ điều hành | Windows 11 (Windows 11 Home Single Language, bản 10.0.26200) |
| Trình duyệt và phiên bản | Google Chrome, phiên bản: 155.0.8059.85 |
| Múi giờ của máy | UTC+07:00. Dùng để đọc TC-CPN-22, TC-CPN-127, TC-CPN-128 (chữ "Hết hạn" so với hôm nay, A18) và kiểm ngày hiển thị có lệch so với ngày nhập không (A13, S1 quyết định 6) |
| SUT | EShop, commit `85af3ba` (theo `00_spec.md`; sinh viên xác nhận commit lúc chạy) |
| Backend | `http://localhost:3000` |
| Web Admin | `http://localhost:5174` |
| Reset dữ liệu mẫu trước đợt test (thời điểm) | 23:41 20/10/2026 |
| Ô Mã coupon có tự chuyển chữ hoa khi gõ không (GH9) | Có, theo quan sát của sinh viên khi nhập thử ở S0 (cung cấp ở S5). Khi chạy: Ô hiện `FR17TC06` (`S6_TC-CPN-06_1.png`) và `<B>FR17TC10</B>` (`S6_TC-CPN-10_1.png`) |
| Ô số có chặn hoặc sửa số thập phân, số âm không (điền sau TC-CPN-15, TC-CPN-41; quyết định chạy dòng dự phòng của TC-CPN-82, TC-CPN-130) | Không xác định: TC-CPN-15, TC-CPN-41 Not run, không có bằng chứng |
| Ô `code` nhận tối đa bao nhiêu ký tự (điền sau TC-CPN-12, TC-CPN-125; GH10) | Không xác định: TC-CPN-12, TC-CPN-125 Not run, không có bằng chứng |
| Có hộp thoại xác nhận khi bấm "Xóa" không (điền sau TC-CPN-51; quyết định TC-CPN-52) | Không. Bấm "Xóa" là xóa ngay, không có thông báo hay hộp thoại xác nhận (sinh viên xác nhận; `S6_TC-CPN-51_1.png`, `S6_TC-CPN-51_2.png`) |
| `GET /api/coupons` có trả `id` và đủ 6 trường không (điền sau TC-CPN-61; quyết định Blocked cho TC-CPN-62, 71, 78, 79, 81 và cách kiểm GH11) | Có. Mỗi mã có `id` và đủ 6 trường, thêm trường `is_active` (log `S6_api_20261021_005438.log`, TC-CPN-61) |
| File log API | `logs/S6_api_20261021_003400.log` (nhóm F, 00:34); `logs/S6_api_20261021_005438.log` (TC-CPN-61, 00:54); `logs/S6_api_20261021_005520.log` (TC-CPN-144, 00:55) |
| Reset dữ liệu trước TC-CPN-56 (thời điểm) | Không reset (nhóm H Not run) |
| Reset dữ liệu sau TC-CPN-56 (thời điểm) | Không reset (nhóm H Not run) |

## 2. Cách điền

- **Kết quả thực tế:** Ghi đúng những gì quan sát được: Dòng mới có xuất hiện không (và còn sau khi tải lại trang không), nguyên văn thông báo lỗi (ghi rõ là thông báo của trang hay bong bóng của trình duyệt, và vị trí so với nút "Tạo mã"), giá trị hiển thị trong bảng. Test case API: Mã HTTP và body, lấy từ log; với test case dạng bảng, ghi từng dòng ở mục 5.
- **Trạng thái:**
  - Pass: Kết quả thực tế khớp kết quả mong đợi.
  - Fail: Không khớp với kết quả mong đợi theo đặc tả. Mô tả khác ở đâu trong cột Ghi chú; đây là ứng viên bug cho S7.
  - Khác giả định (Ann): Không khớp, nhưng chỗ khác nằm ở điều đặc tả không nói và chỉ trái với giả định Ann đã chốt (S4, quyết định 7). Xét ở S7 trước khi coi là bug.
  - Blocked: Không chạy được vì điều kiện bên ngoài test case (ví dụ `GET` không trả `id`). Ghi lý do.
  - Không áp dụng: Điều kiện của test case không tồn tại và đó là hành vi đúng (TC-CPN-52 khi không có hộp thoại, A07).
  - Not run: Chưa chạy.
- **Ảnh:** Tên file `S6_<mã>.png` trong `screenshots/`, ví dụ `S6_TC-CPN-01.png`. Test case nhiều bước: `S6_TC-CPN-13_1.png`, `S6_TC-CPN-13_2.png`.
- **Ngày chạy:** TC-CPN-22, TC-CPN-127, TC-CPN-128 tạo và xem trong cùng ngày; ghi ngày ở mục 1.
- **Tải lại trang:** Với FR-17, "sau khi tải lại trang" nghĩa là tải lại (F5) rồi bấm "Mã Giảm Giá" để quay về trang, vì tải lại ở bất kỳ trang nào của Web Admin đều quay về Dashboard (mục 6).
- **DevTools:** Chỉ dùng cho TC-CPN-95 (số thẻ `<h1>`, đặc tả yêu cầu).
- **Kết quả mong đợi:** Đọc theo bảng mã ở mục 3. Giá trị đầy đủ của từng test case ở `05_final_tc.md`.

## 3. Mã kết quả mong đợi

| Mã | Kết quả mong đợi |
|---|---|
| OUT1 | Bảng có dòng mới với đúng giá trị (tiền có `₫`, phân cách hàng nghìn); còn sau khi tải lại trang |
| OUT2 | API 2xx; `GET /api/coupons` có mã với đúng giá trị |
| OUT4 + ERRn | Không có dòng mới, kể cả sau khi tải lại; thông báo bằng tiếng Việt, chỉ ra đúng nguyên nhân ERRn, nằm **trên** nút "Tạo mã" (bong bóng của trình duyệt cũng tính, vẫn xét vị trí) |
| 4xx | API trả mã 4xx (không phải 5xx); mã của test case không có trong `GET` |
| OUT5 | Danh sách đủ cột, đúng giá trị |
| OUT6 | Trang trống có icon hoặc hình minh họa và message thân thiện |
| OUT7 | `GET /api/coupons` 2xx; mỗi mã đủ 6 trường và `id` |
| OUT8, OUT9 | Xóa thành công (giao diện, API): Mã không còn, kể cả sau khi tải lại |
| OUT10 | Hủy ở hộp thoại: Mã còn nguyên |
| ERR1 đến ERR11 | ERR1 thiếu `code`; ERR2 `code` trùng; ERR3 thiếu `type`; ERR4 `type` ngoài tập; ERR5 thiếu `discount_value`; ERR6 `discount_value` không dương; ERR7 thiếu `expired_at`; ERR8 thiếu `min_order_amount`; ERR9 `min_order_amount` âm; ERR10 thiếu `max_uses_per_user`; ERR11 `max_uses_per_user` nhỏ hơn 1 |
| ERR12 đến ERR17, ERR20, ERR22 | ERR12 chưa xác thực; ERR13 không đủ quyền; ERR14 xóa mã không tồn tại; ERR15 sai kiểu, sai định dạng; ERR16 request không đọc được; ERR17 `percent` lớn hơn 100; ERR20 `max_uses_per_user` không phải số nguyên; ERR22 vượt giới hạn mà đặc tả không nêu (thông báo chỉ ra trường) |

Mọi phản hồi 5xx đều là Fail. Giá trị cơ sở khi cột "Giá trị nhập chính" không nhắc tới: `code` `FR17TC<số>`, "Phần trăm (%)", `15` (với "Số tiền cố định (₫)" là `50000`), `300000`, `12/31/2099`, `3`. `␣` là một dấu cách.

## 4. Kết quả theo thứ tự chạy

Thứ tự theo mục 10 của `05_final_tc.md`: Reset dữ liệu; nhóm A (cần dữ liệu mẫu nguyên vẹn); nhóm B đến F; nhóm G; nhóm H (phá dữ liệu mẫu) cuối cùng, có reset riêng trước TC-CPN-56 và reset ngay sau đó.

Thứ tự chạy thực tế ngày 21/10/2026 (khác thứ tự trên; S6 rút gọn):

1. 00:31 đến 00:32: TC-CPN-91, TC-CPN-95 (giờ trên ảnh; danh sách lúc này chỉ có 4 mã mẫu).
2. 00:34: Nhóm F bằng script (log `S6_api_20261021_003400.log`), trước khi test giao diện của nhóm B, C, E.
3. Test giao diện TC-CPN-01, 02, 06, 10, 30, 32, 37, 38, 51 và bước kiểm tay của TC-CPN-60 (ảnh cắt, không có giờ).
4. 00:54: TC-CPN-61 (log `S6_api_20261021_005438.log`), sau test giao diện, không phải ngay sau reset.
5. 00:55: Tạo 100 mã cho TC-CPN-144 (log `S6_api_20261021_005520.log`); 00:56 ảnh kiểm tay trên giao diện.
6. Khoảng 01:17 đến 01:18 (giờ tạo tệp ảnh): Xóa dòng `FR17TC02` của lần chạy đầu qua giao diện, rồi chạy lại TC-CPN-02 theo đúng dữ liệu kế hoạch.
7. TC-CPN-50, 90, 92, 93, 94: Sinh viên xác nhận trên trang hiện tại ngày 21/10/2026 giống ảnh S0. Không chạy nhóm D, H và các test case khác không có ảnh hay log.

### A. Cần dữ liệu mẫu nguyên vẹn, checklist giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1 | TC-CPN-50 | Danh sách hiển thị đúng 4 mã mẫu | Không nhập (ngay sau reset) | OUT5: 4 dòng `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`, đủ 7 cột, khớp bảng mã mẫu FR-09; `SAVE10` hiện `2099-12-31`; `EXPIRED` hiện chữ "Hết hạn" | 4 dòng, đủ 7 cột "Mã", "Loại", "Giá trị", "Đơn tối thiểu", "Hết hạn", "Giới hạn/người", "Hành động": `SAVE10` (Phần trăm, `10%`, `300,000 ₫`, `2099-12-31`, `1 lần`); `BIGBUY` (Cố định, `50,000 ₫`, `500,000 ₫`, `2099-12-31`, `1 lần`); `VIP100` (Cố định, `100,000 ₫`, `300,000 ₫`, `2099-12-31`, `2 lần`); `EXPIRED` (Phần trăm, `20%`, `100,000 ₫`, chữ "Hết hạn" màu đỏ, `1 lần`); mỗi dòng có nút "Xóa". Ảnh lúc 00:31 ngày 21/10/2026 (trước khi chạy test case nào sau lần reset 23:41) cũng có đúng 4 dòng này | Pass | `S6_TC-CPN-91.png` (00:31 21/10/2026), `S0_03_giao_dien_quan_ly_ma_giam_gia.png` (chụp 18/10/2026) | Khớp bảng mã mẫu của FR-09; `EXPIRED` hiện "Hết hạn" đúng A18. Sinh viên xác nhận trên trang hiện tại ngày 21/10/2026 giống ảnh S0 |
| 2 | TC-CPN-61 | API trả danh sách mã đủ trường | `GET /api/coupons`, token admin | OUT7 | HTTP 200, trả mảng 48 mã. 4 mã mẫu đều có `id` và đủ 6 trường; mỗi mã có thêm trường `is_active` (giá trị `1`). Giá trị của 4 mã mẫu khớp bảng mã mẫu FR-09 (`EXPIRED` có `expired_at` `"2020-01-01"`) | Pass | Log `S6_api_20261021_005438.log` | Chạy lúc 00:54, sau nhóm F và test giao diện, không phải ngay sau reset; danh sách có 48 mã thay vì 4 |
| 3 | TC-CPN-90 | Dấu `*` cạnh trường bắt buộc | Không nhập | 6 ô có `*` cạnh nhãn | Không ô nào có dấu `*`; form không có nhãn, chỉ có placeholder | Fail | `S6_TC-CPN-91.png` (21/10/2026), `S0_03_giao_dien_quan_ly_ma_giam_gia.png`, `S0_04_form_them_coupon_khong_noi_dung.png` (chụp 18/10/2026) | Ứng với điểm đối chiếu ở `00_spec.md` mục 4.4 (FR-22). Sinh viên xác nhận trên trang hiện tại ngày 21/10/2026 giống ảnh S0 |
| 4 | TC-CPN-91 | Ngôn ngữ của trang | Không nhập | Tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn | Tiêu đề tab: `frontend-admin`. Mục menu "Dashboard". Lịch chọn ngày ("October 2026", "Su" đến "Sa", "Clear", "Today") và chữ gợi ý `mm/dd/yyyy` trong ô ngày (thành phần của trình duyệt). Thông báo khi bỏ trống Mã (TC-CPN-30): Bong bóng của trình duyệt "Please fill out this field.". Thông báo khi Mã trùng (TC-CPN-32): "Lỗi: SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code". Các tiêu đề, cột, nút, placeholder còn lại bằng tiếng Việt | Fail | `S6_TC-CPN-91.png`, `S6_TC-CPN-30.png`, `S6_TC-CPN-32.png`, `S0_06_chon_ngay_expired.png` | Fail vì tiêu đề tab `frontend-admin`, mục menu "Dashboard", thông báo ở TC-CPN-32, bong bóng "Please fill out this field." và lịch chọn ngày ("October 2026", "Clear", "Today", `mm/dd/yyyy`) không phải tiếng Việt (FR-21). Bong bóng và lịch là thành phần của trình duyệt, hiện theo ngôn ngữ của trình duyệt; vẫn tính vào FR17-R14 vì người dùng thấy chúng trên trang (như TC-REG-91 của FR-01) |
| 5 | TC-CPN-92 | Màu nút "Tạo mã" và "Xóa" | Không nhập | "Tạo mã" xanh dương; "Xóa" đỏ | Nút "Tạo mã" nền cam, chữ trắng; nút "Xóa" nền đỏ, chữ trắng | Fail | `S6_TC-CPN-91.png` (21/10/2026), `S0_07_nut_thao_tac_tao_ma.png`, `S0_07_nut_thao_tac_xoa.png` (chụp 18/10/2026) | Fail vì nút "Tạo mã" (hành động tích cực) không phải màu xanh dương (FR-21); nút "Xóa" đạt. Sinh viên xác nhận trên trang hiện tại ngày 21/10/2026 giống ảnh S0 |
| 6 | TC-CPN-93 | Định dạng tiền trong bảng | Không nhập | Cột "Giá trị" (loại cố định), "Đơn tối thiểu" có `₫` và phân cách hàng nghìn | Cột "Giá trị" của loại cố định: `50,000 ₫`, `100,000 ₫`; cột "Đơn tối thiểu": `300,000 ₫`, `500,000 ₫`, `300,000 ₫`, `100,000 ₫`. Đều có `₫` và dấu phẩy phân cách hàng nghìn | Pass | `S6_TC-CPN-91.png` (21/10/2026), `S0_03_giao_dien_quan_ly_ma_giam_gia.png` (chụp 18/10/2026) | Chỉ xét dữ liệu mẫu. Sinh viên xác nhận trên trang hiện tại ngày 21/10/2026 giống ảnh S0 |
| 7 | TC-CPN-94 | Menu "Mã Giảm Giá" được highlight | Không nhập | Mục "Mã Giảm Giá" highlight khi đang ở trang này | Ở trang "Quản lý Mã Giảm Giá", mục "Mã Giảm Giá" chữ xanh, các mục khác chữ trắng; ở trang "Dashboard", mục "Dashboard" chữ xanh, "Mã Giảm Giá" chữ trắng | Pass | `S6_TC-CPN-91.png` (21/10/2026), `S0_03_giao_dien_quan_ly_ma_giam_gia.png`, `S0_02_menu_admin.png` (chụp 18/10/2026) | Highlight đổi theo trang đang mở (FR-23). Sinh viên xác nhận trên trang hiện tại ngày 21/10/2026 giống ảnh S0 |
| 8 | TC-CPN-95 | Trang có đúng 1 thẻ `<h1>` | Không nhập | Đúng 1 thẻ, mô tả nội dung trang | Lệnh `[location.pathname, document.querySelectorAll('h1').length]` trong Console khi đang mở trang "Quản lý Mã Giảm Giá" trả về `['/', 1]`: Có 1 thẻ `<h1>`. Ảnh không cho thấy nội dung của thẻ | Pass | `S6_TC-CPN-95.png` | DevTools. Đường dẫn là `/` vì URL không đổi khi chuyển trang (mục 6) |

### B. Thêm mã hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 9 | TC-CPN-01 | Dữ liệu hợp lệ cơ sở, loại phần trăm | Cơ sở | OUT1: `FR17TC01`, "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | Ô nhập: `FR17TC01`, "Phần trăm (%)", `15`, `300000`, `12/31/2099`, `3`. Bảng có dòng `FR17TC01`, "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | Pass | `S6_TC-CPN-01_1.png`, `S6_TC-CPN-01_2.png` | Ảnh không cho thấy bước tải lại trang (K1) |
| 10 | TC-CPN-02 | Dữ liệu hợp lệ cơ sở, loại số tiền cố định | "Số tiền cố định (₫)", `50000` | OUT1; "Giá trị" `50,000 ₫` | Chọn "Số tiền cố định (₫)": Ô "Giá trị" đổi placeholder thành "Số tiền (VD: 50000)"; nhập `50000`. Bảng có dòng `FR17TC02`, "Cố định", `50,000 ₫`, `300,000 ₫`, `2099-12-31`, `3 lần` | Pass | `S6_TC-CPN-02_1.png`, `S6_TC-CPN-02_2.png`, `S6_TC-CPN-02_3.png` (chụp lại) | Chạy lại. Lần chạy đầu dữ liệu khác kế hoạch (loại "Phần trăm", nhập `50000` vào ô "Đơn tối thiểu"); sinh viên xóa dòng `FR17TC02` đó qua giao diện trước khi chạy lại; ảnh của lần đó đã được thay bằng ảnh chụp lại. Ảnh không cho thấy bước tải lại trang (K1) |
| 11 | TC-CPN-03 | Mã có dấu cách ở đầu | `␣FR17TC03` | OUT1; "Mã" hiện `FR17TC03`. K5: Tạo lại `FR17TC03`, mong đợi ERR2 | Không chạy | Not run |  | GH14. Sinh viên không chạy do không đủ thời gian |
| 12 | TC-CPN-04 | Mã có dấu cách ở cuối | `FR17TC04␣` | OUT1; "Mã" hiện `FR17TC04`. K5: Tạo lại `FR17TC04`, mong đợi ERR2 | Không chạy | Not run |  | GH14. Sinh viên không chạy do không đủ thời gian |
| 13 | TC-CPN-05 | Mã có dấu cách ở giữa | `FR17␣TC05` | OUT1; giữ dấu cách. K5: Tạo `FR17TC05`, mong đợi OUT1 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 14 | TC-CPN-06 | Mã gõ bằng chữ thường | `fr17tc06` | OUT1; hiện `fr17tc06` hoặc `FR17TC06`. K5: Tạo lại `FR17TC06`, mong đợi ERR2 | Ô Mã coupon hiện `FR17TC06` (chữ hoa). Bảng có dòng `FR17TC06`, "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | Pass | `S6_TC-CPN-06_1.png`, `S6_TC-CPN-06_2.png` | Ảnh không cho thấy bước K5 (tạo lại `FR17TC06`). Lớp chữ thường kiểm qua API ở TC-CPN-140 (GH9) |
| 15 | TC-CPN-07 | Mã chỉ gồm chữ số có số 0 ở đầu | `0017007` | OUT1; hiện đúng `0017007` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 16 | TC-CPN-08 | Mã có gạch ngang và gạch dưới | `FR17-TC_08` | OUT1; hiện đúng | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 17 | TC-CPN-09 | Mã có chữ tiếng Việt có dấu | `TẾTFR17TC09` | OUT1; hiện đúng ký tự | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 18 | TC-CPN-10 | Mã có thẻ HTML hiển thị dạng chữ | `<b>FR17TC10</b>` | OUT1; hiện nguyên chuỗi (chữ thường hoặc hoa), không in đậm | Ô Mã coupon hiện `<B>FR17TC10</B>`. Bảng hiện nguyên chuỗi `<B>FR17TC10</B>` dạng chữ, không in đậm; "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | Pass | `S6_TC-CPN-10_1.png`, `S6_TC-CPN-10_2.png` | GH9 |
| 19 | TC-CPN-11 | Mã có ký tự SQL lưu nguyên văn | `FR17TC11'OR'1` | OUT1; 4 mã mẫu giữ nguyên. K2: Tạo lại đúng chuỗi, mong đợi ERR2 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 20 | TC-CPN-12 | Mã dài 255 ký tự | `FR17TC12` + 247 chữ `X` | OUT1 đủ 255 ký tự, hoặc ERR22 rõ ràng; cắt cụt là Fail | Không chạy | Not run |  | Ghi số ký tự ô nhận ở mục 1. Sinh viên không chạy do không đủ thời gian |
| 21 | TC-CPN-13 | Tạo lại mã trùng mã đã xóa | `FR17TC13`: Tạo, xóa, tạo lại | Bước 3: OUT1 | Không chạy | Not run |  | 3 bước. Sinh viên không chạy do không đủ thời gian |
| 22 | TC-CPN-14 | Phần trăm bằng 100 | `discount_value` `100` | OUT1; `100%` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 23 | TC-CPN-15 | Phần trăm là số thập phân | `discount_value` `12.5` | OUT1; `12.5%` | Không chạy | Not run |  | Bị trình duyệt chặn thì chạy TC-CPN-82 dòng A. Sinh viên không chạy do không đủ thời gian |
| 24 | TC-CPN-16 | Số tiền cố định là số thập phân | Cố định, `1000.5` | OUT1; K6 `GET` có `1000.5` | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-82 dòng B. Sinh viên không chạy do không đủ thời gian |
| 25 | TC-CPN-17 | Số tiền cố định lớn hơn đơn tối thiểu | Cố định, `500000` | OUT1 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 26 | TC-CPN-18 | Số tiền cố định rất lớn | Cố định, `10000000000000000` | OUT1 hiện đúng, hoặc ERR22 rõ ràng | Không chạy | Not run |  | GH8. Sinh viên không chạy do không đủ thời gian |
| 27 | TC-CPN-19 | Đơn tối thiểu bằng 0 | `min_order_amount` `0` | OUT1; `0 ₫` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 28 | TC-CPN-20 | Đơn tối thiểu là số thập phân | `min_order_amount` `1000.5` | OUT1; K6 `GET` có `1000.5` | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-82 dòng C. Sinh viên không chạy do không đủ thời gian |
| 29 | TC-CPN-21 | Đơn tối thiểu rất lớn | `min_order_amount` `10000000000000000` | Như TC-CPN-18 | Không chạy | Not run |  | GH8. Sinh viên không chạy do không đủ thời gian |
| 30 | TC-CPN-22 | Ngày hết hạn là hôm nay | `expired_at` ngày chạy | OUT1; cột "Hết hạn" hiện chữ "Hết hạn" | Không chạy | Not run |  | Ghi ngày chạy. Sinh viên không chạy do không đủ thời gian |
| 31 | TC-CPN-23 | Ngày hết hạn trong quá khứ | `expired_at` `01/31/2025` | OUT1; hiện chữ "Hết hạn" | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 32 | TC-CPN-24 | Ngày 29/02 năm nhuận | `expired_at` `02/29/2028` | OUT1; hiện `2028-02-29` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 33 | TC-CPN-25 | Số lần dùng tối đa rất lớn | `max_uses_per_user` `10000000000000000` | Như TC-CPN-18 | Không chạy | Not run |  | GH8. Sinh viên không chạy do không đủ thời gian |

### C. Thêm mã không hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 34 | TC-CPN-30 | Mã để trống | `code` trống | OUT4, ERR1 | Bong bóng của trình duyệt "Please fill out this field." trỏ vào ô Mã coupon, nằm trên nút "Tạo mã". Các ô khác: "Phần trăm (%)", `15`, `300000`, `12/31/2099`, `3` | Pass | `S6_TC-CPN-30.png` | Thông báo của trình duyệt, tiếng Anh (TC-CPN-91). Ảnh không cho thấy bước tải lại (K3) |
| 35 | TC-CPN-31 | Mã chỉ gồm 3 dấu cách | `␣␣␣` | OUT4, ERR1 | Không chạy | Not run |  | GH14. Sinh viên không chạy do không đủ thời gian |
| 36 | TC-CPN-32 | Mã trùng mã mẫu | `SAVE10` | OUT4, ERR2; `SAVE10` giữ nguyên | Hộp thoại "localhost:5174 says" ở đầu trang, nội dung "Lỗi: SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code". Form vẫn giữ `SAVE10`, "Phần trăm (%)", `15`, `300000`, `12/31/2099`, `3`. Dòng `SAVE10` vẫn là "Phần trăm", `10%`, `300,000 ₫`, `2099-12-31`, `1 lần` | Fail | `S6_TC-CPN-32.png` | Fail vì thông báo không phải tiếng Việt: Chuỗi lỗi kỹ thuật của CSDL, chỉ có tiền tố "Lỗi:" (R14). Thông báo lộ tên hệ CSDL và tên bảng, cột (`SQLITE`, `coupons.code`). Ảnh không cho thấy bước tải lại (K3) |
| 37 | TC-CPN-33 | Mã trùng mã vừa tạo | `FR17TC33` tạo 2 lần | Lần 1: OUT1. Lần 2: OUT4, ERR2 | Không chạy | Not run |  | 2 bước. Sinh viên không chạy do không đủ thời gian |
| 38 | TC-CPN-34 | Mã chỉ khác mã mẫu ở hoa thường | `save10` | OUT4, ERR2 | Không chạy | Not run |  | GH9: Ghi giá trị thực tế trong ô. Sinh viên không chạy do không đủ thời gian |
| 39 | TC-CPN-35 | Mã trùng mã mẫu sau khi cắt dấu cách | `␣SAVE10` | OUT4, ERR2 | Không chạy | Not run |  | GH14. Sinh viên không chạy do không đủ thời gian |
| 40 | TC-CPN-36 | Mã trùng mã đã hết hạn | `EXPIRED` | OUT4, ERR2 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 41 | TC-CPN-37 | Phần trăm là 150 | `discount_value` `150` | OUT4, ERR17 | Ô "Giá trị" `150` với "Phần trăm (%)". Bảng có dòng `FR17TC37`, "Phần trăm", `150%`, `300,000 ₫`, `2099-12-31`, `3 lần`: Mã được tạo | Khác giả định (A01) | `S6_TC-CPN-37_1.png`, `S6_TC-CPN-37_2.png` | Mong đợi ERR17 theo A01 (tối đa 100); đặc tả chỉ yêu cầu dương |
| 42 | TC-CPN-38 | Phần trăm bằng 0 | `discount_value` `0` | OUT4, ERR6 | Ô "Giá trị" `0` với "Phần trăm (%)". Bảng có dòng `FR17TC38`, "Phần trăm", `0%`, `300,000 ₫`, `2099-12-31`, `3 lần`: Mã được tạo | Fail | `S6_TC-CPN-38_1.png`, `S6_TC-CPN-38_2.png` | Fail vì `discount_value` phải dương (FR-17) |
| 43 | TC-CPN-39 | Số tiền cố định bằng 0 | Cố định, `0` | OUT4, ERR6 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 44 | TC-CPN-40 | Giá trị giảm để trống | `discount_value` trống | OUT4, ERR5 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 45 | TC-CPN-41 | Đơn tối thiểu âm | `min_order_amount` `-1` | OUT4, ERR9 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-82 dòng E. Sinh viên không chạy do không đủ thời gian |
| 46 | TC-CPN-42 | Đơn tối thiểu để trống | Xóa `0`, để trống | OUT4, ERR8 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 47 | TC-CPN-43 | Ngày hết hạn để trống | `expired_at` trống | OUT4, ERR7 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 48 | TC-CPN-44 | Số lần dùng tối đa bằng 0 | `max_uses_per_user` `0` | OUT4, ERR11 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-82 dòng F. Sinh viên không chạy do không đủ thời gian |
| 49 | TC-CPN-45 | Số lần dùng tối đa là số thập phân | `max_uses_per_user` `1.5` | OUT4, ERR20 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-82 dòng D. Sinh viên không chạy do không đủ thời gian |
| 50 | TC-CPN-46 | Số lần dùng tối đa để trống | Xóa `1`, để trống | OUT4, ERR10 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |

### D. Giá trị biên qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 51 | TC-CPN-100 | Phần trăm là -1 | `discount_value` `-1` | OUT4, ERR6 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng A. Sinh viên không chạy do không đủ thời gian |
| 52 | TC-CPN-101 | Phần trăm là 0.01 | `discount_value` `0.01` | OUT1; `0.01%`. Bị từ chối vì là số thập phân: Khác giả định A02 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng B. Sinh viên không chạy do không đủ thời gian |
| 53 | TC-CPN-102 | Phần trăm là 1 | `discount_value` `1` | OUT1; `1%` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 54 | TC-CPN-103 | Phần trăm là 2 | `discount_value` `2` | OUT1; `2%` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 55 | TC-CPN-104 | Phần trăm là 99 | `discount_value` `99` | OUT1; `99%` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 56 | TC-CPN-105 | Phần trăm là 100.01 | `discount_value` `100.01` | OUT4, ERR17. Bị từ chối vì là số thập phân: Khác giả định A02 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng C. Sinh viên không chạy do không đủ thời gian |
| 57 | TC-CPN-106 | Phần trăm là 101 | `discount_value` `101` | OUT4, ERR17 | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 58 | TC-CPN-107 | Số tiền cố định là -1 | Cố định, `-1` | OUT4, ERR6 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng D. Sinh viên không chạy do không đủ thời gian |
| 59 | TC-CPN-108 | Số tiền cố định là 0.01 | Cố định, `0.01` | OUT1; K6 có `0.01`. Bị từ chối vì là số thập phân: Khác giả định A02 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng E. Sinh viên không chạy do không đủ thời gian |
| 60 | TC-CPN-109 | Số tiền cố định là 1 | Cố định, `1` | OUT1; `1 ₫` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 61 | TC-CPN-110 | Số tiền cố định là 2 | Cố định, `2` | OUT1; `2 ₫` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 62 | TC-CPN-111 | Số tiền cố định 2^53 + 1 | Cố định, `9007199254740993` | OUT1 hiện đúng `9,007,199,254,740,993 ₫`, K6 đúng; hoặc ERR22 rõ ràng. `...992` là Fail | Không chạy | Not run |  | Đọc cùng TC-CPN-131 dòng A (GH7). Sinh viên không chạy do không đủ thời gian |
| 63 | TC-CPN-112 | Đơn tối thiểu là -0.01 | `min_order_amount` `-0.01` | OUT4, ERR9. Bị từ chối vì là số thập phân: Khác giả định A03. Được chấp nhận: Fail | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng F. Sinh viên không chạy do không đủ thời gian |
| 64 | TC-CPN-113 | Đơn tối thiểu là 1 | `min_order_amount` `1` | OUT1; `1 ₫` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 65 | TC-CPN-114 | Đơn tối thiểu 2^53 + 1 | `min_order_amount` `9007199254740993` | Như TC-CPN-111 | Không chạy | Not run |  | Đọc cùng TC-CPN-131 dòng B. Sinh viên không chạy do không đủ thời gian |
| 66 | TC-CPN-115 | Số lần dùng tối đa là -1 | `max_uses_per_user` `-1` | OUT4, ERR11 | Không chạy | Not run |  | Bị chặn thì chạy TC-CPN-130 dòng G. Sinh viên không chạy do không đủ thời gian |
| 67 | TC-CPN-116 | Số lần dùng tối đa là 1 | `max_uses_per_user` `1` (gõ lại) | OUT1; `1 lần` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 68 | TC-CPN-117 | Số lần dùng tối đa là 2 | `max_uses_per_user` `2` | OUT1; `2 lần` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 69 | TC-CPN-119 | Số lần dùng tối đa 2^53 + 1 | `max_uses_per_user` `9007199254740993` | Như TC-CPN-111 | Không chạy | Not run |  | Đọc cùng TC-CPN-131 dòng C. Sinh viên không chạy do không đủ thời gian |
| 70 | TC-CPN-120 | Mã là 1 dấu cách | `␣` | OUT4, ERR1 | Không chạy | Not run |  | GH14. Sinh viên không chạy do không đủ thời gian |
| 71 | TC-CPN-121 | Mã dài 1 ký tự | `Q` | OUT1; `Q` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 72 | TC-CPN-122 | Mã 1 ký tự có dấu cách hai bên | `␣K␣` | OUT1; `K`. K5: Tạo lại `K`, mong đợi ERR2 | Không chạy | Not run |  | GH14. Sinh viên không chạy do không đủ thời gian |
| 73 | TC-CPN-123 | Mã là 1 chữ thường | `j` | OUT1; `j` hoặc `J` | Không chạy | Not run |  | GH9. Sinh viên không chạy do không đủ thời gian |
| 74 | TC-CPN-124 | Mã dài 2 ký tự | `QZ` | OUT1; `QZ` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 75 | TC-CPN-125 | Mã dài 1000 ký tự | `FR17TC125` + 991 chữ `X` | OUT1 đủ 1000 ký tự, hoặc ERR22 rõ ràng; cắt cụt là Fail | Không chạy | Not run |  | Ghi số ký tự ô nhận. Sinh viên không chạy do không đủ thời gian |
| 76 | TC-CPN-126 | Ngày hết hạn 01/01/0001 | `expired_at` `01/01/0001` | OUT1; hiện chữ "Hết hạn" | Không chạy | Not run |  | Ghi nếu ô không cho nhập năm này. Sinh viên không chạy do không đủ thời gian |
| 77 | TC-CPN-127 | Ngày hết hạn là hôm qua | `expired_at` ngày chạy trừ 1 | OUT1; hiện chữ "Hết hạn" | Không chạy | Not run |  | Cùng ngày với TC-CPN-22, 128. Sinh viên không chạy do không đủ thời gian |
| 78 | TC-CPN-128 | Ngày hết hạn là ngày mai | `expired_at` ngày chạy cộng 1 | OUT1; hiện đúng ngày | Không chạy | Not run |  | Cùng ngày với TC-CPN-22, 127. Sinh viên không chạy do không đủ thời gian |
| 79 | TC-CPN-129 | Ngày hết hạn 12/31/9999 | `expired_at` `12/31/9999` | OUT1; hiện `9999-12-31` | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |

### E. Xóa không phá dữ liệu mẫu

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 80 | TC-CPN-51 | Xóa mã vừa tạo | Tạo rồi xóa `FR17TC51` | OUT8; K7, K8 (tạo lại `FR17TC51` được) | Trước khi xóa, bảng có dòng `FR17TC51` ("Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần`). Sau khi bấm "Xóa", dòng `FR17TC51` không còn; `FR17TC37`, `FR17TC38` vẫn còn. Ảnh không có hộp thoại xác nhận | Pass | `S6_TC-CPN-51_1.png`, `S6_TC-CPN-51_2.png` | Ảnh không cho thấy bước tải lại (K7) và tạo lại `FR17TC51` (K8). Sinh viên xác nhận: Xóa ngay, không có thông báo hay hộp thoại xác nhận |
| 81 | TC-CPN-52 | Hủy ở hộp thoại xác nhận xóa | Tạo `FR17TC52`, bấm "Xóa", chọn hủy | OUT10. Không có hộp thoại: Không áp dụng | Không có hộp thoại xác nhận khi bấm "Xóa" (mục 1, TC-CPN-51) | Không áp dụng |  | Theo A07 (b), không có hộp thoại là đúng nên test case không áp dụng |
| 82 | TC-CPN-53 | Xóa mã đã bị xóa ở tab khác | `FR17TC53`, 2 tab | Báo lỗi hoặc tự cập nhật; mã khác không đổi | Không chạy | Not run |  | 4 bước. Sinh viên không chạy do không đủ thời gian |

### F. API (script `scripts/run_api_tests.py`)

Chạy nhóm F: `python scripts/run_api_tests.py` (từ thư mục feature). Dòng dự phòng: `python scripts/run_api_tests.py --only 82 --rows A,C` (thay số và dòng theo test case giao diện bị chặn); tương tự với `--only 130`. Bằng chứng là file log trong `logs/`; ảnh chỉ cần cho bước làm tay.

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 83 | TC-CPN-60 | API tạo mã thành công | Body cơ sở, `"FR17TC60"` | OUT2; đúng giá trị từng trường | HTTP 200 `{"message": "Coupon created", "id": 5}`. `GET` có `FR17TC60` với đúng giá trị đã gửi. Bảng trên giao diện có dòng `FR17TC60`, "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | Pass | Log `S6_api_20261021_003400.log`, `S6_TC-CPN-60.png` | Bằng chứng: log API |
| 84 | TC-CPN-62 | API xóa mã vừa tạo | `DELETE` với `id` của `FR17TC62` | OUT9 | Tạo `FR17TC62`: HTTP 200 (`id` 6). `DELETE /api/admin/coupons/6`: HTTP 200 `{"message": "Coupon deleted"}`. `GET` không còn `FR17TC62` | Pass | Log `S6_api_20261021_003400.log` | Blocked nếu `GET` không có `id` |
| 85 | TC-CPN-63 | API nhận Mã là số JSON | `"code": 2026` | OUT2; `GET` có `2026` | HTTP 200 (`id` 7). `GET` có mã `"2026"` (chuỗi) | Pass | Log `S6_api_20261021_003400.log` |  |
| 86 | TC-CPN-64 | API nhận chuỗi chứa số | 3 dòng | Mỗi dòng 2xx (mục 5) | 3 dòng đều HTTP 200; `GET` lưu dạng số (mục 5) | Pass | Log `S6_api_20261021_003400.log` | Dạng bảng |
| 87 | TC-CPN-65 | API từ chối `type` không hợp lệ | 3 dòng | Mỗi dòng 4xx (mục 5) | 3 dòng đều HTTP 200 `Coupon created`; mã được tạo với `type` lần lượt `null`, `"free"`, `"PERCENT"` (mục 5) | Fail | Log `S6_api_20261021_003400.log` | Fail vì dòng A, B: `type` bắt buộc và chỉ nhận `percent`, `fixed` (FR-17). Dòng C: Khác giả định A11 |
| 88 | TC-CPN-66 | API từ chối `null`, chuỗi rỗng | 6 dòng | Mỗi dòng 4xx (mục 5) | 6 dòng đều HTTP 200; mã được tạo với trường bắt buộc là `null` hoặc chuỗi rỗng; dòng F lưu `max_uses_per_user` là `1` (mục 5) | Fail | Log `S6_api_20261021_003400.log` | Fail vì thiếu giá trị ở trường bắt buộc vẫn tạo được mã (FR-17) |
| 89 | TC-CPN-67 | API từ chối trường số không phải số | 3 dòng | Mỗi dòng 4xx (mục 5) | 3 dòng đều HTTP 200; `GET` lưu nguyên `"abc"` ở trường số (mục 5) | Fail | Log `S6_api_20261021_003400.log` | Fail vì trường số nhận giá trị không phải số (FR-17: dương, >= 0, >= 1) |
| 90 | TC-CPN-68 | API từ chối ngày sai định dạng | 3 dòng | Mỗi dòng 4xx (mục 5) | 3 dòng đều HTTP 200; `GET` lưu nguyên `"12/31/2027"`, `"2027-02-30"`, `"2027-12-31T10:00:00Z"` (mục 5) | Khác giả định (A13) | Log `S6_api_20261021_003400.log` | Mong đợi ERR15 theo A13 (chỉ `yyyy-mm-dd`, ngày có thật) |
| 91 | TC-CPN-69 | API từ chối request không đọc được | 4 dòng | Mỗi dòng 4xx, không 5xx (mục 5) | Dòng A: HTTP 400, body là trang HTML lỗi có dòng `SyntaxError: Expected double-quoted property name in JSON at position 21` và đường dẫn tệp trên máy chủ. Dòng B, C, D: HTTP 500, body là trang HTML lỗi `TypeError: Cannot destructure property 'code' of 'req.body' as it is undefined.` kèm đường dẫn tệp. Không mã nào được tạo (mục 5) | Fail | Log `S6_api_20261021_003400.log` | Fail vì dòng B, C, D trả 5xx, theo quy ước "mọi 5xx là Sai" ở `05_final_tc.md` mục 1.2. Đặc tả không quy định mã HTTP; quy ước này dựa trên giả định A20, A23, nên xét theo giả định thì đây cũng là Khác giả định (A23). Body lỗi lộ đường dẫn tệp trên máy chủ |
| 92 | TC-CPN-70 | API từ chối body `{}` | Body `{}` | 4xx; số mã không đổi | HTTP 200 `Coupon created` (`id` 26); số mã từ 24 thành 25 | Fail | Log `S6_api_20261021_003400.log` | Fail vì body thiếu mọi trường bắt buộc vẫn tạo được mã (FR-17) |
| 93 | TC-CPN-71 | API xóa với `id` không hợp lệ | 3 dòng | Mỗi dòng 2xx hoặc 4xx, không 5xx (mục 5) | 3 dòng đều HTTP 200 `{"message": "Coupon deleted"}`; số mã không đổi (mục 5) | Pass | Log `S6_api_20261021_003400.log` | A15 (b) chấp nhận 2xx khi không có mã nào bị xóa |
| 94 | TC-CPN-72 | Tạo mã không có header Authorization | `"FR17TC72"`, không header | 4xx (ERR12); mã không được tạo | HTTP 401 `{"error": "Unauthorized"}`; không có `FR17TC72` | Pass | Log `S6_api_20261021_003400.log` |  |
| 95 | TC-CPN-73 | Tạo mã khi header thiếu `Bearer` | `Authorization: <token>` | 4xx (ERR12) | HTTP 401 `{"error": "Unauthorized"}`; không có `FR17TC73` | Pass | Log `S6_api_20261021_003400.log` |  |
| 96 | TC-CPN-74 | Tạo mã khi token không hợp lệ | `Bearer abc.def.ghi` | 4xx (ERR12) | HTTP 403 `{"error": "Forbidden"}`; không có `FR17TC74` | Pass | Log `S6_api_20261021_003400.log` | Mã 403 (không phải 401) cho token không hợp lệ; A20 chỉ yêu cầu 4xx |
| 97 | TC-CPN-75 | Tạo mã bằng token user thường | Token `test@eshop.com` | 4xx (ERR13) | HTTP 200 `Coupon created` (`id` 28); `GET` có `FR17TC75` | Fail | Log `S6_api_20261021_003400.log` | Fail vì token user thường tạo được mã (FR-12, SEC-03) |
| 98 | TC-CPN-76 | Xem danh sách không có header | `GET`, không header | 4xx (ERR12) | HTTP 401 `{"error": "Unauthorized"}` | Pass | Log `S6_api_20261021_003400.log` |  |
| 99 | TC-CPN-77 | Xem danh sách bằng token user thường | `GET`, token user thường | 4xx (ERR13). 2xx: Khác giả định A28 | HTTP 200, trả danh sách mã | Khác giả định (A28) | Log `S6_api_20261021_003400.log` | Mong đợi 4xx theo A28 (chỉ admin) |
| 100 | TC-CPN-78 | Xóa mã không có header | `DELETE`, không header | 4xx (ERR12); mã còn | Tạo `FR17TC78` (`id` 29). `DELETE` không có header: HTTP 401 `{"error": "Unauthorized"}`; `FR17TC78` vẫn còn | Pass | Log `S6_api_20261021_003400.log` | Blocked nếu không có `id` |
| 101 | TC-CPN-79 | Xóa mã bằng token user thường | `DELETE`, token user thường | 4xx (ERR13); mã còn | Tạo `FR17TC79` (`id` 30). `DELETE` bằng token user thường: HTTP 200 `{"message": "Coupon deleted"}`; `FR17TC79` không còn | Fail | Log `S6_api_20261021_003400.log` | Fail vì token user thường xóa được mã (FR-12, SEC-03) |
| 102 | TC-CPN-80 | `POST /api/coupons` (FR-12) không header | `"FR17TC80"`, không header | Mã không được tạo; không 5xx; 404 cũng Pass | HTTP 404, trang HTML `Cannot POST /api/coupons`; không có `FR17TC80` | Pass | Log `S6_api_20261021_003400.log` |  |
| 103 | TC-CPN-81 | `DELETE /api/coupons/:id` (FR-12) bằng user thường | `id` của `FR17TC81` | Mã còn; không 5xx; 404 cũng Pass | Tạo `FR17TC81` (`id` 31). `DELETE /api/coupons/31` bằng token user thường: HTTP 404 `Cannot DELETE /api/coupons/31`; `FR17TC81` vẫn còn | Pass | Log `S6_api_20261021_003400.log` | Blocked nếu không có `id` |
| 104 | TC-CPN-82 | Dự phòng số lẻ, số âm (S3) | 6 dòng | Theo dòng (mục 5) | Không chạy | Not run |  | Không chạy dòng dự phòng: Chỉ chạy khi test case giao diện tương ứng bị trình duyệt chặn; TC-CPN-15, 16, 20, 41, 44, 45 không chạy |
| 105 | TC-CPN-118 | Số lần dùng tối đa viết là 1.0 | `"max_uses_per_user": 1.0` | OUT2, lưu là 1 | HTTP 200 (`id` 32); `GET` lưu `max_uses_per_user` là `1` | Pass | Log `S6_api_20261021_003400.log` | GH12 |
| 106 | TC-CPN-130 | Dự phòng điểm biên số lẻ, số âm (S4) | 7 dòng | Theo dòng (mục 5) | Không chạy | Not run |  | Không chạy dòng dự phòng: Chỉ chạy khi test case giao diện tương ứng bị trình duyệt chặn; TC-CPN-100, 101, 105, 107, 108, 112, 115 không chạy |
| 107 | TC-CPN-131 | Server lưu chính xác 2^53 + 1 | 3 dòng | Theo dòng (mục 5) | 3 dòng đều HTTP 200; `GET` lưu `9007199254740992` thay cho `9007199254740993` ở cả 3 trường (mục 5) | Fail | Log `S6_api_20261021_003400.log` | Fail vì giá trị lưu khác giá trị gửi. TC-CPN-111, 114, 119 (giao diện) không chạy nên chưa đọc kết hợp được |
| 108 | TC-CPN-140 | API tạo mã có chữ thường | `"fr17tc140"`, rồi `"FR17TC140"` | Bước 1: OUT2. Bước 2: 4xx (ERR2) | Bước 1: HTTP 200 (`id` 36); `GET` có `fr17tc140` (giữ chữ thường). Bước 2 (K5): `FR17TC140` HTTP 200 (`id` 37), tạo được | Khác giả định (A04) | Log `S6_api_20261021_003400.log` | Mong đợi bước 2 là ERR2 theo A04 (so trùng không phân biệt hoa thường) |
| 109 | TC-CPN-141 | API từ chối mã khác mã mẫu ở hoa thường | `"save10"` | 4xx (ERR2); `SAVE10` giữ nguyên | HTTP 200 (`id` 38); `GET` có thêm mã `save10`; `SAVE10` giữ nguyên | Khác giả định (A04) | Log `S6_api_20261021_003400.log` | Mong đợi ERR2 theo A04 |
| 110 | TC-CPN-142 | API tạo mã là 1 chữ thường | `"m"` | OUT2; `m` hoặc `M` | HTTP 200 (`id` 39); `GET` có mã `m` | Pass | Log `S6_api_20261021_003400.log` |  |
| 111 | TC-CPN-143 | API cắt dấu cách đầu cuối của Mã | 4 dòng | Theo dòng (mục 5) | 4 dòng đều HTTP 200: Mã được lưu nguyên dấu cách (`␣FR17TC143A`, `FR17TC143B␣`); gửi lại dạng không dấu cách vẫn tạo được; `␣␣␣` và `␣SAVE10` được tạo (mục 5) | Khác giả định (A09) | Log `S6_api_20261021_003400.log` | Mong đợi theo A09: Cắt dấu cách đầu cuối; chỉ dấu cách tính như rỗng |

### G. Danh sách rất dài (sau nhóm API)

Tạo 100 mã: `python scripts/run_api_tests.py --only 144`, rồi kiểm trên giao diện và chụp ảnh.

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 112 | TC-CPN-144 | Danh sách hiển thị đủ khi có rất nhiều mã | 100 mã `FR17TC144N001` đến `FR17TC144N100` tạo bằng API | Xem được mọi mã (cuộn hoặc phân trang); số dòng bằng số mã trong `GET`; bố cục không vỡ; nút "Xóa" ở dòng cuối bấm được | Script tạo 100 mã, cả 100 lần HTTP 200; `GET` có 148 mã, trong đó 100 mã `FR17TC144N...`. Trang cuộn được tới cuối danh sách, không có phân trang; dòng cuối là `FR17TC144N100`, nút "Xóa" nhìn thấy; các cột thẳng hàng, không chồng lên nhau | Pass | Log `S6_api_20261021_005520.log`, `S6_TC-CPN-144.png` (00:56 21/10/2026) | Ảnh không cho thấy `FR17TC144N001` và không đếm số dòng trên trang |

### H. Phá dữ liệu mẫu, chạy cuối cùng

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 113 | TC-CPN-54 | Xóa mã mẫu còn hạn | `BIGBUY` | OUT8; 3 mã mẫu còn lại giữ nguyên | Không chạy | Not run |  | Sinh viên không chạy do không đủ thời gian |
| 114 | TC-CPN-55 | Xóa mã mẫu đã hết hạn | `EXPIRED` | OUT8 | Không chạy | Not run |  | Sau TC-CPN-36, TC-CPN-50. Sinh viên không chạy do không đủ thời gian |
| 115 | TC-CPN-56 | Trang trống khi không còn mã nào | Reset; xóa 4 mã mẫu | OUT6; `GET` trả danh sách rỗng | Không chạy | Not run |  | Reset riêng trước; reset ngay sau. Sinh viên không chạy do không đủ thời gian |

## 5. Kết quả theo dòng của test case dạng bảng

Chi tiết dữ liệu từng dòng ở `05_final_tc.md` mục 7.1. Dòng không chạy (dự phòng không cần) ghi "Không chạy".

| Mã | Dòng | Kết quả mong đợi | Mã HTTP | Body hoặc giá trị trong `GET` (tóm tắt) | Trạng thái |
|---|---|---|---|---|---|
| TC-CPN-64 | A | 2xx; `discount_value` 15 | HTTP 200 | `discount_value` lưu `15` (số) | Pass |
| TC-CPN-64 | B | 2xx; `min_order_amount` 300000 | HTTP 200 | `min_order_amount` lưu `300000` (số) | Pass |
| TC-CPN-64 | C | 2xx; `max_uses_per_user` 3 | HTTP 200 | `max_uses_per_user` lưu `3` (số) | Pass |
| TC-CPN-65 | A | 4xx (ERR3) | HTTP 200 | `Coupon created` (`id` 11); `type` lưu `null` | Fail |
| TC-CPN-65 | B | 4xx (ERR4) | HTTP 200 | `Coupon created` (`id` 12); `type` lưu `"free"` | Fail |
| TC-CPN-65 | C | 4xx (ERR4) | HTTP 200 | `Coupon created` (`id` 13); `type` lưu `"PERCENT"` | Khác giả định (A11) |
| TC-CPN-66 | A | 4xx (ERR1); số mã không đổi | HTTP 200 | `Coupon created` (`id` 14); số mã từ 12 thành 13 | Fail |
| TC-CPN-66 | B | 4xx (ERR3) | HTTP 200 | `Coupon created` (`id` 15); `type` lưu `""` | Fail |
| TC-CPN-66 | C | 4xx (ERR5) | HTTP 200 | `Coupon created` (`id` 16); `discount_value` lưu `null` | Fail |
| TC-CPN-66 | D | 4xx (ERR8) | HTTP 200 | `Coupon created` (`id` 17); `min_order_amount` lưu `null` | Fail |
| TC-CPN-66 | E | 4xx (ERR7) | HTTP 200 | `Coupon created` (`id` 18); `expired_at` lưu `""` | Fail |
| TC-CPN-66 | F | 4xx (ERR10) | HTTP 200 | `Coupon created` (`id` 19); `max_uses_per_user` lưu `1` | Fail |
| TC-CPN-67 | A | 4xx (ERR15) | HTTP 200 | `Coupon created` (`id` 20); `discount_value` lưu `"abc"` | Fail |
| TC-CPN-67 | B | 4xx (ERR15) | HTTP 200 | `Coupon created` (`id` 21); `min_order_amount` lưu `"abc"` | Fail |
| TC-CPN-67 | C | 4xx (ERR15) | HTTP 200 | `Coupon created` (`id` 22); `max_uses_per_user` lưu `"abc"` | Fail |
| TC-CPN-68 | A | 4xx (ERR15) | HTTP 200 | `Coupon created` (`id` 23); `expired_at` lưu `"12/31/2027"` | Khác giả định (A13) |
| TC-CPN-68 | B | 4xx (ERR15) | HTTP 200 | `Coupon created` (`id` 24); `expired_at` lưu `"2027-02-30"` | Khác giả định (A13) |
| TC-CPN-68 | C | 4xx (ERR15) | HTTP 200 | `Coupon created` (`id` 25); `expired_at` lưu `"2027-12-31T10:00:00Z"` | Khác giả định (A13) |
| TC-CPN-69 | A | 4xx (ERR16); không 5xx | HTTP 400 | Trang HTML lỗi `SyntaxError: Expected double-quoted property name in JSON at position 21`, có đường dẫn tệp trên máy chủ; không có `FR17TC69A` | Pass |
| TC-CPN-69 | B | 4xx (ERR16 hoặc thiếu mọi trường); không 5xx | HTTP 500 | Trang HTML lỗi `TypeError: Cannot destructure property 'code' of 'req.body' as it is undefined.`; không có `FR17TC69B` | Fail |
| TC-CPN-69 | C | Như dòng B | HTTP 500 | Như dòng B; không có `FR17TC69C` | Fail |
| TC-CPN-69 | D | Như dòng B; số mã không đổi | HTTP 500 | Như dòng B; số mã 24 không đổi | Fail |
| TC-CPN-71 | A | 2xx hoặc 4xx; không 5xx; số mã không đổi | HTTP 200 | `{"message": "Coupon deleted"}`; số mã 25 không đổi | Pass |
| TC-CPN-71 | B | Như dòng A | HTTP 200 | `{"message": "Coupon deleted"}`; số mã 25 không đổi | Pass |
| TC-CPN-71 | C | Như dòng A | HTTP 200 | Chuẩn bị: Tạo `FR17TC71C` (`id` 27), xóa lần 1 HTTP 200. Xóa lần 2: `{"message": "Coupon deleted"}`; số mã 25 không đổi | Pass |
| TC-CPN-82 | A | 2xx; `GET` có `12.5` |  |  | Không chạy |
| TC-CPN-82 | B | 2xx; `GET` có `1000.5` |  |  | Không chạy |
| TC-CPN-82 | C | 2xx; `GET` có `1000.5` |  |  | Không chạy |
| TC-CPN-82 | D | 4xx (ERR20) |  |  | Không chạy |
| TC-CPN-82 | E | 4xx (ERR9) |  |  | Không chạy |
| TC-CPN-82 | F | 4xx (ERR11) |  |  | Không chạy |
| TC-CPN-130 | A | 4xx (ERR6) |  |  | Không chạy |
| TC-CPN-130 | B | 2xx; `GET` có `0.01`. Bị từ chối vì là số thập phân: Khác giả định A02 |  |  | Không chạy |
| TC-CPN-130 | C | 4xx (ERR17). Bị từ chối vì là số thập phân: Khác giả định A02 |  |  | Không chạy |
| TC-CPN-130 | D | 4xx (ERR6) |  |  | Không chạy |
| TC-CPN-130 | E | 2xx; `GET` có `0.01`. Bị từ chối vì là số thập phân: Khác giả định A02 |  |  | Không chạy |
| TC-CPN-130 | F | 4xx (ERR9). Bị từ chối vì là số thập phân: Khác giả định A03; được chấp nhận là Fail |  |  | Không chạy |
| TC-CPN-130 | G | 4xx (ERR11) |  |  | Không chạy |
| TC-CPN-131 | A | 2xx và `GET` có đúng `9007199254740993`, hoặc 4xx rõ ràng (ERR22); `...992` hoặc 5xx là Fail | HTTP 200 | `discount_value` lưu `9007199254740992` | Fail |
| TC-CPN-131 | B | Như dòng A | HTTP 200 | `min_order_amount` lưu `9007199254740992` | Fail |
| TC-CPN-131 | C | Như dòng A | HTTP 200 | `max_uses_per_user` lưu `9007199254740992` | Fail |
| TC-CPN-143 | A | 2xx; `GET` có `FR17TC143A`. K5: Gửi lại `"FR17TC143A"`, 4xx (ERR2) | HTTP 200 | Lưu `␣FR17TC143A` (giữ dấu cách); K5 gửi `FR17TC143A`: HTTP 200, tạo được (`id` 41) | Khác giả định (A09) |
| TC-CPN-143 | B | 2xx; `GET` có `FR17TC143B`. K5: Gửi lại `"FR17TC143B"`, 4xx (ERR2) | HTTP 200 | Lưu `FR17TC143B␣` (giữ dấu cách); K5 gửi `FR17TC143B`: HTTP 200, tạo được (`id` 43) | Khác giả định (A09) |
| TC-CPN-143 | C | 4xx (ERR1); số mã không đổi | HTTP 200 | `Coupon created` (`id` 44); số mã từ 40 thành 41 | Khác giả định (A09) |
| TC-CPN-143 | D | 4xx (ERR2); `SAVE10` giữ nguyên | HTTP 200 | `Coupon created` (`id` 45); `GET` có mã `␣SAVE10`; `SAVE10` giữ nguyên | Khác giả định (A09) |

Cách đọc TC-CPN-131 cùng TC-CPN-111, 114, 119 và cách đọc TC-CPN-143 cùng TC-CPN-03, 04, 31, 35: Theo `05_final_tc.md` mục 7, 7.1.

## 6. Quan sát không có Pass hay Fail

| Mục | Quan sát | Ảnh |
|---|---|---|
| Placeholder ô "Giá trị" có đổi khi chọn "Số tiền cố định (₫)" không (S3, quyết định 2) | Có đổi: Với "Phần trăm (%)" là "Giá trị % (VD: 10)"; với "Số tiền cố định (₫)" là "Số tiền (VD: 50000)" | `S6_TC-CPN-91.png`, `S6_TC-CPN-02_1.png` |
| Tải lại trang (F5) và đường dẫn | Tải lại ở bất kỳ trang nào của Web Admin đều quay về Dashboard; URL luôn là `localhost:5174` dù đang ở trang nào (sinh viên quan sát ngày 21/10/2026) | URL ở `S6_TC-CPN-91.png`, `S6_TC-CPN-144.png` |
| Ngoài phạm vi FR-17: Trang đăng nhập Web Admin | Chữ tiếng Anh: Tiêu đề "Admin Login", placeholder "Email", "Password", nút "Login". Trang này thuộc đăng nhập admin, không thuộc FR-17; ghi lại để nhóm xét ở feature liên quan (FR-21) | `S0_01_dang_nhap_admin.png` (chụp 18/10/2026) |

## 7. Tổng hợp

Đếm bằng script từ bảng ở mục 4.

| Nhóm | Số TC | Pass | Fail | Khác giả định | Blocked | Không áp dụng | Not run |
|---|---|---|---|---|---|---|---|
| A. Dữ liệu mẫu nguyên vẹn, checklist | 8 | 5 | 3 | 0 | 0 | 0 | 0 |
| B. Thêm hợp lệ qua giao diện | 25 | 4 | 0 | 0 | 0 | 0 | 21 |
| C. Thêm không hợp lệ qua giao diện | 17 | 1 | 2 | 1 | 0 | 0 | 13 |
| D. Giá trị biên qua giao diện | 29 | 0 | 0 | 0 | 0 | 0 | 29 |
| E. Xóa không phá dữ liệu mẫu | 3 | 1 | 0 | 0 | 0 | 1 | 1 |
| F. API | 29 | 14 | 8 | 5 | 0 | 0 | 2 |
| G. Danh sách rất dài | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| H. Phá dữ liệu mẫu | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| **Tổng** | **115** | **26** | **13** | **6** | **0** | **1** | **69** |
