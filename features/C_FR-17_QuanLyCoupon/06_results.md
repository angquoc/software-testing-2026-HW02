# S6: Kết quả chạy test (FR-17 Quản lý mã giảm giá)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test, chụp ảnh và chạy script; AI chuẩn bị khung và điền kết quả theo ảnh, log và ghi chú của sinh viên; sinh viên review và sửa
- Bản này: AI điền theo ảnh, log của sinh viên, sinh viên review. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-20 22:35 (UTC+07:00)
- 2026-10-20 22:35 (UTC+07:00): AI điền sẵn TC-CPN-50, TC-CPN-90, TC-CPN-92, TC-CPN-93, TC-CPN-94 và phần quan sát của TC-CPN-91 bằng cách đối chiếu ảnh S0 (chụp 18/10/2026); trạng thái ghi "(đề xuất)", sinh viên xác nhận trên trang hiện tại. Điền dòng "Ô Mã coupon có tự chuyển chữ hoa" ở mục 1 theo thông tin sinh viên cung cấp ở S5; thêm một quan sát ngoài phạm vi ở mục 6. Mọi test case cần nhập dữ liệu hay gọi API do sinh viên chạy và điền
- 2026-10-20 22:50 (UTC+07:00): Theo yêu cầu của sinh viên, AI điền ngày chạy, người chạy, hệ điều hành, trình duyệt (giống `A_FR-01_DangKy/06_results.md`) và múi giờ ở mục 1; bỏ chữ "(đề xuất)" ở các trạng thái; điền trạng thái TC-CPN-91. Sinh viên review và tự sửa nếu sai
- 2026-10-21 00:01 (UTC+07:00): AI viết script `scripts/run_api_tests.py` cho nhóm F (và TC-CPN-61, 82, 130, 144 chạy bằng `--only`); sửa dòng "Bước", "Bản này" cho đúng cách làm thực tế; điền ngày chạy 21/10/2026, thời điểm reset 23:41 20/10/2026, đường dẫn log ở mục 1; ghi lệnh chạy ở nhóm A, F, G
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
| Ô Mã coupon có tự chuyển chữ hoa khi gõ không (GH9) | Có, theo quan sát của sinh viên khi nhập thử ở S0 (cung cấp ở S5); xác nhận lại khi chạy TC-CPN-06 |
| Ô số có chặn hoặc sửa số thập phân, số âm không (điền sau TC-CPN-15, TC-CPN-41; quyết định chạy dòng dự phòng của TC-CPN-82, TC-CPN-130) | |
| Ô `code` nhận tối đa bao nhiêu ký tự (điền sau TC-CPN-12, TC-CPN-125; GH10) | |
| Có hộp thoại xác nhận khi bấm "Xóa" không (điền sau TC-CPN-51; quyết định TC-CPN-52) | |
| `GET /api/coupons` có trả `id` và đủ 6 trường không (điền sau TC-CPN-61; quyết định Blocked cho TC-CPN-62, 71, 78, 79, 81 và cách kiểm GH11) | |
| File log API | `logs/S6_api_<thời gian>.log` (mỗi lần chạy script một file) |
| Reset dữ liệu trước TC-CPN-56 (thời điểm) | |
| Reset dữ liệu sau TC-CPN-56 (thời điểm) | |

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

### A. Cần dữ liệu mẫu nguyên vẹn, checklist giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1 | TC-CPN-50 | Danh sách hiển thị đúng 4 mã mẫu | Không nhập (ngay sau reset) | OUT5: 4 dòng `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`, đủ 7 cột, khớp bảng mã mẫu FR-09; `SAVE10` hiện `2099-12-31`; `EXPIRED` hiện chữ "Hết hạn" | 4 dòng, đủ 7 cột "Mã", "Loại", "Giá trị", "Đơn tối thiểu", "Hết hạn", "Giới hạn/người", "Hành động": `SAVE10` (Phần trăm, `10%`, `300,000 ₫`, `2099-12-31`, `1 lần`); `BIGBUY` (Cố định, `50,000 ₫`, `500,000 ₫`, `2099-12-31`, `1 lần`); `VIP100` (Cố định, `100,000 ₫`, `300,000 ₫`, `2099-12-31`, `2 lần`); `EXPIRED` (Phần trăm, `20%`, `100,000 ₫`, chữ "Hết hạn" màu đỏ, `1 lần`); mỗi dòng có nút "Xóa" | Pass | `S0_03_giao_dien_quan_ly_ma_giam_gia.png` (chụp 18/10/2026) | Khớp bảng mã mẫu của FR-09; `EXPIRED` hiện "Hết hạn" đúng A18. Ảnh S0 không chắc chụp ngay sau reset, sinh viên xác nhận sau khi reset ngày chạy. AI đối chiếu ảnh S0 (SUT commit `85af3ba` theo `00_spec.md`); sinh viên xác nhận trên trang hiện tại |
| 2 | TC-CPN-61 | API trả danh sách mã đủ trường | `GET /api/coupons`, token admin | OUT7 | | | | Chạy bằng `python scripts/run_api_tests.py --only 61`, trước nhóm B. Điền dòng "`GET` có trả `id`..." ở mục 1 |
| 3 | TC-CPN-90 | Dấu `*` cạnh trường bắt buộc | Không nhập | 6 ô có `*` cạnh nhãn | Không ô nào có dấu `*`; form không có nhãn, chỉ có placeholder | Fail | `S0_03_giao_dien_quan_ly_ma_giam_gia.png`, `S0_04_form_them_coupon_khong_noi_dung.png` (chụp 18/10/2026) | Ứng với điểm đối chiếu ở `00_spec.md` mục 4.4 (FR-22). AI đối chiếu ảnh S0 (SUT commit `85af3ba` theo `00_spec.md`); sinh viên xác nhận trên trang hiện tại |
| 4 | TC-CPN-91 | Ngôn ngữ của trang | Không nhập | Tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn | Chữ không phải tiếng Việt nhìn thấy trên trang: Mục menu "Dashboard"; lịch chọn ngày ("October 2026", "Su" đến "Sa", "Clear", "Today") và chữ gợi ý `mm/dd/yyyy` trong ô ngày. Các tiêu đề, cột, nút, placeholder còn lại bằng tiếng Việt | Fail | `S0_03_giao_dien_quan_ly_ma_giam_gia.png`, `S0_06_chon_ngay_expired.png` (chụp 18/10/2026) | Bổ sung ngôn ngữ thông báo lỗi khi chạy nhóm C. Fail vì mục menu "Dashboard" không phải tiếng Việt (FR-21); nếu sinh viên coi "Dashboard" là thuật ngữ kỹ thuật chuẩn thì đổi thành Pass. Lưu ý thêm: (1) lịch và `mm/dd/yyyy` là thành phần của trình duyệt, theo ngôn ngữ trình duyệt; (2) ảnh S0 không thấy thanh tab nên chưa xét tiêu đề tab. AI đối chiếu ảnh S0 (SUT commit `85af3ba` theo `00_spec.md`); sinh viên xác nhận trên trang hiện tại |
| 5 | TC-CPN-92 | Màu nút "Tạo mã" và "Xóa" | Không nhập | "Tạo mã" xanh dương; "Xóa" đỏ | Nút "Tạo mã" nền cam, chữ trắng; nút "Xóa" nền đỏ, chữ trắng | Fail | `S0_07_nut_thao_tac_tao_ma.png`, `S0_07_nut_thao_tac_xoa.png` (chụp 18/10/2026) | Fail vì nút "Tạo mã" (hành động tích cực) không phải màu xanh dương (FR-21); nút "Xóa" đạt. Ứng với điểm đối chiếu ở `00_spec.md` mục 4.4. AI đối chiếu ảnh S0 (SUT commit `85af3ba` theo `00_spec.md`); sinh viên xác nhận trên trang hiện tại |
| 6 | TC-CPN-93 | Định dạng tiền trong bảng | Không nhập | Cột "Giá trị" (loại cố định), "Đơn tối thiểu" có `₫` và phân cách hàng nghìn | Cột "Giá trị" của loại cố định: `50,000 ₫`, `100,000 ₫`; cột "Đơn tối thiểu": `300,000 ₫`, `500,000 ₫`, `300,000 ₫`, `100,000 ₫`. Đều có `₫` và dấu phẩy phân cách hàng nghìn | Pass | `S0_03_giao_dien_quan_ly_ma_giam_gia.png` (chụp 18/10/2026) | Chỉ xét dữ liệu mẫu; cách hiển thị số lẻ, số lớn xem thêm ở TC-CPN-16, TC-CPN-18, TC-CPN-20, TC-CPN-21. AI đối chiếu ảnh S0 (SUT commit `85af3ba` theo `00_spec.md`); sinh viên xác nhận trên trang hiện tại |
| 7 | TC-CPN-94 | Menu "Mã Giảm Giá" được highlight | Không nhập | Mục "Mã Giảm Giá" highlight khi đang ở trang này | Ở trang "Quản lý Mã Giảm Giá", mục "Mã Giảm Giá" chữ xanh, các mục khác chữ trắng; ở trang "Dashboard", mục "Dashboard" chữ xanh, "Mã Giảm Giá" chữ trắng | Pass | `S0_03_giao_dien_quan_ly_ma_giam_gia.png`, `S0_02_menu_admin.png` (chụp 18/10/2026) | So với khi ở trang khác. Highlight đổi theo trang đang mở (FR-23). AI đối chiếu ảnh S0 (SUT commit `85af3ba` theo `00_spec.md`); sinh viên xác nhận trên trang hiện tại |
| 8 | TC-CPN-95 | Trang có đúng 1 thẻ `<h1>` | Không nhập | Đúng 1 thẻ, mô tả nội dung trang | | | | DevTools |

### B. Thêm mã hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 9 | TC-CPN-01 | Dữ liệu hợp lệ cơ sở, loại phần trăm | Cơ sở | OUT1: `FR17TC01`, "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | | | | |
| 10 | TC-CPN-02 | Dữ liệu hợp lệ cơ sở, loại số tiền cố định | "Số tiền cố định (₫)", `50000` | OUT1; "Giá trị" `50,000 ₫` | | | | |
| 11 | TC-CPN-03 | Mã có dấu cách ở đầu | `␣FR17TC03` | OUT1; "Mã" hiện `FR17TC03`. K5: Tạo lại `FR17TC03`, mong đợi ERR2 | | | | GH14 |
| 12 | TC-CPN-04 | Mã có dấu cách ở cuối | `FR17TC04␣` | OUT1; "Mã" hiện `FR17TC04`. K5: Tạo lại `FR17TC04`, mong đợi ERR2 | | | | GH14 |
| 13 | TC-CPN-05 | Mã có dấu cách ở giữa | `FR17␣TC05` | OUT1; giữ dấu cách. K5: Tạo `FR17TC05`, mong đợi OUT1 | | | | |
| 14 | TC-CPN-06 | Mã gõ bằng chữ thường | `fr17tc06` | OUT1; hiện `fr17tc06` hoặc `FR17TC06`. K5: Tạo lại `FR17TC06`, mong đợi ERR2 | | | | GH9: Ghi giá trị thực tế trong ô trước khi bấm "Tạo mã" |
| 15 | TC-CPN-07 | Mã chỉ gồm chữ số có số 0 ở đầu | `0017007` | OUT1; hiện đúng `0017007` | | | | |
| 16 | TC-CPN-08 | Mã có gạch ngang và gạch dưới | `FR17-TC_08` | OUT1; hiện đúng | | | | |
| 17 | TC-CPN-09 | Mã có chữ tiếng Việt có dấu | `TẾTFR17TC09` | OUT1; hiện đúng ký tự | | | | |
| 18 | TC-CPN-10 | Mã có thẻ HTML hiển thị dạng chữ | `<b>FR17TC10</b>` | OUT1; hiện nguyên chuỗi (chữ thường hoặc hoa), không in đậm | | | | GH9 |
| 19 | TC-CPN-11 | Mã có ký tự SQL lưu nguyên văn | `FR17TC11'OR'1` | OUT1; 4 mã mẫu giữ nguyên. K2: Tạo lại đúng chuỗi, mong đợi ERR2 | | | | |
| 20 | TC-CPN-12 | Mã dài 255 ký tự | `FR17TC12` + 247 chữ `X` | OUT1 đủ 255 ký tự, hoặc ERR22 rõ ràng; cắt cụt là Fail | | | | Ghi số ký tự ô nhận ở mục 1 |
| 21 | TC-CPN-13 | Tạo lại mã trùng mã đã xóa | `FR17TC13`: Tạo, xóa, tạo lại | Bước 3: OUT1 | | | | 3 bước |
| 22 | TC-CPN-14 | Phần trăm bằng 100 | `discount_value` `100` | OUT1; `100%` | | | | |
| 23 | TC-CPN-15 | Phần trăm là số thập phân | `discount_value` `12.5` | OUT1; `12.5%` | | | | Bị trình duyệt chặn thì chạy TC-CPN-82 dòng A |
| 24 | TC-CPN-16 | Số tiền cố định là số thập phân | Cố định, `1000.5` | OUT1; K6 `GET` có `1000.5` | | | | Bị chặn thì chạy TC-CPN-82 dòng B |
| 25 | TC-CPN-17 | Số tiền cố định lớn hơn đơn tối thiểu | Cố định, `500000` | OUT1 | | | | |
| 26 | TC-CPN-18 | Số tiền cố định rất lớn | Cố định, `10000000000000000` | OUT1 hiện đúng, hoặc ERR22 rõ ràng | | | | GH8 |
| 27 | TC-CPN-19 | Đơn tối thiểu bằng 0 | `min_order_amount` `0` | OUT1; `0 ₫` | | | | |
| 28 | TC-CPN-20 | Đơn tối thiểu là số thập phân | `min_order_amount` `1000.5` | OUT1; K6 `GET` có `1000.5` | | | | Bị chặn thì chạy TC-CPN-82 dòng C |
| 29 | TC-CPN-21 | Đơn tối thiểu rất lớn | `min_order_amount` `10000000000000000` | Như TC-CPN-18 | | | | GH8 |
| 30 | TC-CPN-22 | Ngày hết hạn là hôm nay | `expired_at` ngày chạy | OUT1; cột "Hết hạn" hiện chữ "Hết hạn" | | | | Ghi ngày chạy |
| 31 | TC-CPN-23 | Ngày hết hạn trong quá khứ | `expired_at` `01/31/2025` | OUT1; hiện chữ "Hết hạn" | | | | |
| 32 | TC-CPN-24 | Ngày 29/02 năm nhuận | `expired_at` `02/29/2028` | OUT1; hiện `2028-02-29` | | | | |
| 33 | TC-CPN-25 | Số lần dùng tối đa rất lớn | `max_uses_per_user` `10000000000000000` | Như TC-CPN-18 | | | | GH8 |

### C. Thêm mã không hợp lệ qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 34 | TC-CPN-30 | Mã để trống | `code` trống | OUT4, ERR1 | | | | |
| 35 | TC-CPN-31 | Mã chỉ gồm 3 dấu cách | `␣␣␣` | OUT4, ERR1 | | | | GH14 |
| 36 | TC-CPN-32 | Mã trùng mã mẫu | `SAVE10` | OUT4, ERR2; `SAVE10` giữ nguyên | | | | |
| 37 | TC-CPN-33 | Mã trùng mã vừa tạo | `FR17TC33` tạo 2 lần | Lần 1: OUT1. Lần 2: OUT4, ERR2 | | | | 2 bước |
| 38 | TC-CPN-34 | Mã chỉ khác mã mẫu ở hoa thường | `save10` | OUT4, ERR2 | | | | GH9: Ghi giá trị thực tế trong ô |
| 39 | TC-CPN-35 | Mã trùng mã mẫu sau khi cắt dấu cách | `␣SAVE10` | OUT4, ERR2 | | | | GH14 |
| 40 | TC-CPN-36 | Mã trùng mã đã hết hạn | `EXPIRED` | OUT4, ERR2 | | | | |
| 41 | TC-CPN-37 | Phần trăm là 150 | `discount_value` `150` | OUT4, ERR17 | | | | |
| 42 | TC-CPN-38 | Phần trăm bằng 0 | `discount_value` `0` | OUT4, ERR6 | | | | |
| 43 | TC-CPN-39 | Số tiền cố định bằng 0 | Cố định, `0` | OUT4, ERR6 | | | | |
| 44 | TC-CPN-40 | Giá trị giảm để trống | `discount_value` trống | OUT4, ERR5 | | | | |
| 45 | TC-CPN-41 | Đơn tối thiểu âm | `min_order_amount` `-1` | OUT4, ERR9 | | | | Bị chặn thì chạy TC-CPN-82 dòng E |
| 46 | TC-CPN-42 | Đơn tối thiểu để trống | Xóa `0`, để trống | OUT4, ERR8 | | | | |
| 47 | TC-CPN-43 | Ngày hết hạn để trống | `expired_at` trống | OUT4, ERR7 | | | | |
| 48 | TC-CPN-44 | Số lần dùng tối đa bằng 0 | `max_uses_per_user` `0` | OUT4, ERR11 | | | | Bị chặn thì chạy TC-CPN-82 dòng F |
| 49 | TC-CPN-45 | Số lần dùng tối đa là số thập phân | `max_uses_per_user` `1.5` | OUT4, ERR20 | | | | Bị chặn thì chạy TC-CPN-82 dòng D |
| 50 | TC-CPN-46 | Số lần dùng tối đa để trống | Xóa `1`, để trống | OUT4, ERR10 | | | | |

### D. Giá trị biên qua giao diện

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 51 | TC-CPN-100 | Phần trăm là -1 | `discount_value` `-1` | OUT4, ERR6 | | | | Bị chặn thì chạy TC-CPN-130 dòng A |
| 52 | TC-CPN-101 | Phần trăm là 0.01 | `discount_value` `0.01` | OUT1; `0.01%`. Bị từ chối vì là số thập phân: Khác giả định A02 | | | | Bị chặn thì chạy TC-CPN-130 dòng B |
| 53 | TC-CPN-102 | Phần trăm là 1 | `discount_value` `1` | OUT1; `1%` | | | | |
| 54 | TC-CPN-103 | Phần trăm là 2 | `discount_value` `2` | OUT1; `2%` | | | | |
| 55 | TC-CPN-104 | Phần trăm là 99 | `discount_value` `99` | OUT1; `99%` | | | | |
| 56 | TC-CPN-105 | Phần trăm là 100.01 | `discount_value` `100.01` | OUT4, ERR17. Bị từ chối vì là số thập phân: Khác giả định A02 | | | | Bị chặn thì chạy TC-CPN-130 dòng C |
| 57 | TC-CPN-106 | Phần trăm là 101 | `discount_value` `101` | OUT4, ERR17 | | | | |
| 58 | TC-CPN-107 | Số tiền cố định là -1 | Cố định, `-1` | OUT4, ERR6 | | | | Bị chặn thì chạy TC-CPN-130 dòng D |
| 59 | TC-CPN-108 | Số tiền cố định là 0.01 | Cố định, `0.01` | OUT1; K6 có `0.01`. Bị từ chối vì là số thập phân: Khác giả định A02 | | | | Bị chặn thì chạy TC-CPN-130 dòng E |
| 60 | TC-CPN-109 | Số tiền cố định là 1 | Cố định, `1` | OUT1; `1 ₫` | | | | |
| 61 | TC-CPN-110 | Số tiền cố định là 2 | Cố định, `2` | OUT1; `2 ₫` | | | | |
| 62 | TC-CPN-111 | Số tiền cố định 2^53 + 1 | Cố định, `9007199254740993` | OUT1 hiện đúng `9,007,199,254,740,993 ₫`, K6 đúng; hoặc ERR22 rõ ràng. `...992` là Fail | | | | Đọc cùng TC-CPN-131 dòng A (GH7) |
| 63 | TC-CPN-112 | Đơn tối thiểu là -0.01 | `min_order_amount` `-0.01` | OUT4, ERR9. Bị từ chối vì là số thập phân: Khác giả định A03. Được chấp nhận: Fail | | | | Bị chặn thì chạy TC-CPN-130 dòng F |
| 64 | TC-CPN-113 | Đơn tối thiểu là 1 | `min_order_amount` `1` | OUT1; `1 ₫` | | | | |
| 65 | TC-CPN-114 | Đơn tối thiểu 2^53 + 1 | `min_order_amount` `9007199254740993` | Như TC-CPN-111 | | | | Đọc cùng TC-CPN-131 dòng B |
| 66 | TC-CPN-115 | Số lần dùng tối đa là -1 | `max_uses_per_user` `-1` | OUT4, ERR11 | | | | Bị chặn thì chạy TC-CPN-130 dòng G |
| 67 | TC-CPN-116 | Số lần dùng tối đa là 1 | `max_uses_per_user` `1` (gõ lại) | OUT1; `1 lần` | | | | |
| 68 | TC-CPN-117 | Số lần dùng tối đa là 2 | `max_uses_per_user` `2` | OUT1; `2 lần` | | | | |
| 69 | TC-CPN-119 | Số lần dùng tối đa 2^53 + 1 | `max_uses_per_user` `9007199254740993` | Như TC-CPN-111 | | | | Đọc cùng TC-CPN-131 dòng C |
| 70 | TC-CPN-120 | Mã là 1 dấu cách | `␣` | OUT4, ERR1 | | | | GH14 |
| 71 | TC-CPN-121 | Mã dài 1 ký tự | `Q` | OUT1; `Q` | | | | |
| 72 | TC-CPN-122 | Mã 1 ký tự có dấu cách hai bên | `␣K␣` | OUT1; `K`. K5: Tạo lại `K`, mong đợi ERR2 | | | | GH14 |
| 73 | TC-CPN-123 | Mã là 1 chữ thường | `j` | OUT1; `j` hoặc `J` | | | | GH9 |
| 74 | TC-CPN-124 | Mã dài 2 ký tự | `QZ` | OUT1; `QZ` | | | | |
| 75 | TC-CPN-125 | Mã dài 1000 ký tự | `FR17TC125` + 991 chữ `X` | OUT1 đủ 1000 ký tự, hoặc ERR22 rõ ràng; cắt cụt là Fail | | | | Ghi số ký tự ô nhận |
| 76 | TC-CPN-126 | Ngày hết hạn 01/01/0001 | `expired_at` `01/01/0001` | OUT1; hiện chữ "Hết hạn" | | | | Ghi nếu ô không cho nhập năm này |
| 77 | TC-CPN-127 | Ngày hết hạn là hôm qua | `expired_at` ngày chạy trừ 1 | OUT1; hiện chữ "Hết hạn" | | | | Cùng ngày với TC-CPN-22, 128 |
| 78 | TC-CPN-128 | Ngày hết hạn là ngày mai | `expired_at` ngày chạy cộng 1 | OUT1; hiện đúng ngày | | | | Cùng ngày với TC-CPN-22, 127 |
| 79 | TC-CPN-129 | Ngày hết hạn 12/31/9999 | `expired_at` `12/31/9999` | OUT1; hiện `9999-12-31` | | | | |

### E. Xóa không phá dữ liệu mẫu

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 80 | TC-CPN-51 | Xóa mã vừa tạo | Tạo rồi xóa `FR17TC51` | OUT8; K7, K8 (tạo lại `FR17TC51` được) | | | | Điền dòng "Có hộp thoại..." ở mục 1 |
| 81 | TC-CPN-52 | Hủy ở hộp thoại xác nhận xóa | Tạo `FR17TC52`, bấm "Xóa", chọn hủy | OUT10. Không có hộp thoại: Không áp dụng | | | | |
| 82 | TC-CPN-53 | Xóa mã đã bị xóa ở tab khác | `FR17TC53`, 2 tab | Báo lỗi hoặc tự cập nhật; mã khác không đổi | | | | 4 bước |

### F. API (script `scripts/run_api_tests.py`)

Chạy nhóm F: `python scripts/run_api_tests.py` (từ thư mục feature). Dòng dự phòng: `python scripts/run_api_tests.py --only 82 --rows A,C` (thay số và dòng theo test case giao diện bị chặn); tương tự với `--only 130`. Bằng chứng là file log trong `logs/`; ảnh chỉ cần cho bước làm tay.

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 83 | TC-CPN-60 | API tạo mã thành công | Body cơ sở, `"FR17TC60"` | OUT2; đúng giá trị từng trường | | | | Bằng chứng: log API |
| 84 | TC-CPN-62 | API xóa mã vừa tạo | `DELETE` với `id` của `FR17TC62` | OUT9 | | | | Blocked nếu `GET` không có `id` |
| 85 | TC-CPN-63 | API nhận Mã là số JSON | `"code": 2026` | OUT2; `GET` có `2026` | | | | |
| 86 | TC-CPN-64 | API nhận chuỗi chứa số | 3 dòng | Mỗi dòng 2xx (mục 5) | | | | Dạng bảng |
| 87 | TC-CPN-65 | API từ chối `type` không hợp lệ | 3 dòng | Mỗi dòng 4xx (mục 5) | | | | Dạng bảng |
| 88 | TC-CPN-66 | API từ chối `null`, chuỗi rỗng | 6 dòng | Mỗi dòng 4xx (mục 5) | | | | Dạng bảng |
| 89 | TC-CPN-67 | API từ chối trường số không phải số | 3 dòng | Mỗi dòng 4xx (mục 5) | | | | Dạng bảng |
| 90 | TC-CPN-68 | API từ chối ngày sai định dạng | 3 dòng | Mỗi dòng 4xx (mục 5) | | | | Dạng bảng |
| 91 | TC-CPN-69 | API từ chối request không đọc được | 4 dòng | Mỗi dòng 4xx, không 5xx (mục 5) | | | | Dạng bảng |
| 92 | TC-CPN-70 | API từ chối body `{}` | Body `{}` | 4xx; số mã không đổi | | | | Ghi thông báo liệt kê mấy trường |
| 93 | TC-CPN-71 | API xóa với `id` không hợp lệ | 3 dòng | Mỗi dòng 2xx hoặc 4xx, không 5xx (mục 5) | | | | Dạng bảng; Blocked dòng C nếu không có `id` |
| 94 | TC-CPN-72 | Tạo mã không có header Authorization | `"FR17TC72"`, không header | 4xx (ERR12); mã không được tạo | | | | |
| 95 | TC-CPN-73 | Tạo mã khi header thiếu `Bearer` | `Authorization: <token>` | 4xx (ERR12) | | | | |
| 96 | TC-CPN-74 | Tạo mã khi token không hợp lệ | `Bearer abc.def.ghi` | 4xx (ERR12) | | | | |
| 97 | TC-CPN-75 | Tạo mã bằng token user thường | Token `test@eshop.com` | 4xx (ERR13) | | | | |
| 98 | TC-CPN-76 | Xem danh sách không có header | `GET`, không header | 4xx (ERR12) | | | | |
| 99 | TC-CPN-77 | Xem danh sách bằng token user thường | `GET`, token user thường | 4xx (ERR13). 2xx: Khác giả định A28 | | | | |
| 100 | TC-CPN-78 | Xóa mã không có header | `DELETE`, không header | 4xx (ERR12); mã còn | | | | Blocked nếu không có `id` |
| 101 | TC-CPN-79 | Xóa mã bằng token user thường | `DELETE`, token user thường | 4xx (ERR13); mã còn | | | | Blocked nếu không có `id` |
| 102 | TC-CPN-80 | `POST /api/coupons` (FR-12) không header | `"FR17TC80"`, không header | Mã không được tạo; không 5xx; 404 cũng Pass | | | | |
| 103 | TC-CPN-81 | `DELETE /api/coupons/:id` (FR-12) bằng user thường | `id` của `FR17TC81` | Mã còn; không 5xx; 404 cũng Pass | | | | Blocked nếu không có `id` |
| 104 | TC-CPN-82 | Dự phòng số lẻ, số âm (S3) | 6 dòng | Theo dòng (mục 5) | | | | Chỉ chạy dòng có test case giao diện bị chặn |
| 105 | TC-CPN-118 | Số lần dùng tối đa viết là 1.0 | `"max_uses_per_user": 1.0` | OUT2, lưu là 1 | | | | GH12 |
| 106 | TC-CPN-130 | Dự phòng điểm biên số lẻ, số âm (S4) | 7 dòng | Theo dòng (mục 5) | | | | Chỉ chạy dòng có test case giao diện bị chặn |
| 107 | TC-CPN-131 | Server lưu chính xác 2^53 + 1 | 3 dòng | Theo dòng (mục 5) | | | | Luôn chạy, cùng TC-CPN-111, 114, 119 |
| 108 | TC-CPN-140 | API tạo mã có chữ thường | `"fr17tc140"`, rồi `"FR17TC140"` | Bước 1: OUT2. Bước 2: 4xx (ERR2) | | | | |
| 109 | TC-CPN-141 | API từ chối mã khác mã mẫu ở hoa thường | `"save10"` | 4xx (ERR2); `SAVE10` giữ nguyên | | | | |
| 110 | TC-CPN-142 | API tạo mã là 1 chữ thường | `"m"` | OUT2; `m` hoặc `M` | | | | |
| 111 | TC-CPN-143 | API cắt dấu cách đầu cuối của Mã | 4 dòng | Theo dòng (mục 5) | | | | Dạng bảng |

### G. Danh sách rất dài (sau nhóm API)

Tạo 100 mã: `python scripts/run_api_tests.py --only 144`, rồi kiểm trên giao diện và chụp ảnh.

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 112 | TC-CPN-144 | Danh sách hiển thị đủ khi có rất nhiều mã | 100 mã `FR17TC144N001` đến `FR17TC144N100` tạo bằng API | Xem được mọi mã (cuộn hoặc phân trang); số dòng bằng số mã trong `GET`; bố cục không vỡ; nút "Xóa" ở dòng cuối bấm được | | | | Ghi nếu trang tải chậm |

### H. Phá dữ liệu mẫu, chạy cuối cùng

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 113 | TC-CPN-54 | Xóa mã mẫu còn hạn | `BIGBUY` | OUT8; 3 mã mẫu còn lại giữ nguyên | | | | |
| 114 | TC-CPN-55 | Xóa mã mẫu đã hết hạn | `EXPIRED` | OUT8 | | | | Sau TC-CPN-36, TC-CPN-50 |
| 115 | TC-CPN-56 | Trang trống khi không còn mã nào | Reset; xóa 4 mã mẫu | OUT6; `GET` trả danh sách rỗng | | | | Reset riêng trước; reset ngay sau |

## 5. Kết quả theo dòng của test case dạng bảng

Chi tiết dữ liệu từng dòng ở `05_final_tc.md` mục 7.1. Dòng không chạy (dự phòng không cần) ghi "Không chạy".

| Mã | Dòng | Kết quả mong đợi | Mã HTTP | Body hoặc giá trị trong `GET` (tóm tắt) | Trạng thái |
|---|---|---|---|---|---|
| TC-CPN-64 | A | 2xx; `discount_value` 15 | | | |
| TC-CPN-64 | B | 2xx; `min_order_amount` 300000 | | | |
| TC-CPN-64 | C | 2xx; `max_uses_per_user` 3 | | | |
| TC-CPN-65 | A | 4xx (ERR3) | | | |
| TC-CPN-65 | B | 4xx (ERR4) | | | |
| TC-CPN-65 | C | 4xx (ERR4) | | | |
| TC-CPN-66 | A | 4xx (ERR1); số mã không đổi | | | |
| TC-CPN-66 | B | 4xx (ERR3) | | | |
| TC-CPN-66 | C | 4xx (ERR5) | | | |
| TC-CPN-66 | D | 4xx (ERR8) | | | |
| TC-CPN-66 | E | 4xx (ERR7) | | | |
| TC-CPN-66 | F | 4xx (ERR10) | | | |
| TC-CPN-67 | A | 4xx (ERR15) | | | |
| TC-CPN-67 | B | 4xx (ERR15) | | | |
| TC-CPN-67 | C | 4xx (ERR15) | | | |
| TC-CPN-68 | A | 4xx (ERR15) | | | |
| TC-CPN-68 | B | 4xx (ERR15) | | | |
| TC-CPN-68 | C | 4xx (ERR15) | | | |
| TC-CPN-69 | A | 4xx (ERR16); không 5xx | | | |
| TC-CPN-69 | B | 4xx (ERR16 hoặc thiếu mọi trường); không 5xx | | | |
| TC-CPN-69 | C | Như dòng B | | | |
| TC-CPN-69 | D | Như dòng B; số mã không đổi | | | |
| TC-CPN-71 | A | 2xx hoặc 4xx; không 5xx; số mã không đổi | | | |
| TC-CPN-71 | B | Như dòng A | | | |
| TC-CPN-71 | C | Như dòng A | | | |
| TC-CPN-82 | A | 2xx; `GET` có `12.5` | | | |
| TC-CPN-82 | B | 2xx; `GET` có `1000.5` | | | |
| TC-CPN-82 | C | 2xx; `GET` có `1000.5` | | | |
| TC-CPN-82 | D | 4xx (ERR20) | | | |
| TC-CPN-82 | E | 4xx (ERR9) | | | |
| TC-CPN-82 | F | 4xx (ERR11) | | | |
| TC-CPN-130 | A | 4xx (ERR6) | | | |
| TC-CPN-130 | B | 2xx; `GET` có `0.01`. Bị từ chối vì là số thập phân: Khác giả định A02 | | | |
| TC-CPN-130 | C | 4xx (ERR17). Bị từ chối vì là số thập phân: Khác giả định A02 | | | |
| TC-CPN-130 | D | 4xx (ERR6) | | | |
| TC-CPN-130 | E | 2xx; `GET` có `0.01`. Bị từ chối vì là số thập phân: Khác giả định A02 | | | |
| TC-CPN-130 | F | 4xx (ERR9). Bị từ chối vì là số thập phân: Khác giả định A03; được chấp nhận là Fail | | | |
| TC-CPN-130 | G | 4xx (ERR11) | | | |
| TC-CPN-131 | A | 2xx và `GET` có đúng `9007199254740993`, hoặc 4xx rõ ràng (ERR22); `...992` hoặc 5xx là Fail | | | |
| TC-CPN-131 | B | Như dòng A | | | |
| TC-CPN-131 | C | Như dòng A | | | |
| TC-CPN-143 | A | 2xx; `GET` có `FR17TC143A`. K5: Gửi lại `"FR17TC143A"`, 4xx (ERR2) | | | |
| TC-CPN-143 | B | 2xx; `GET` có `FR17TC143B`. K5: Gửi lại `"FR17TC143B"`, 4xx (ERR2) | | | |
| TC-CPN-143 | C | 4xx (ERR1); số mã không đổi | | | |
| TC-CPN-143 | D | 4xx (ERR2); `SAVE10` giữ nguyên | | | |

Cách đọc TC-CPN-131 cùng TC-CPN-111, 114, 119 và cách đọc TC-CPN-143 cùng TC-CPN-03, 04, 31, 35: Theo `05_final_tc.md` mục 7, 7.1.

## 6. Quan sát không có Pass hay Fail

| Mục | Quan sát | Ảnh |
|---|---|---|
| Placeholder ô "Giá trị" có đổi khi chọn "Số tiền cố định (₫)" không (S3, quyết định 2) | | |
| Ngoài phạm vi FR-17: Trang đăng nhập Web Admin | Chữ tiếng Anh: Tiêu đề "Admin Login", placeholder "Email", "Password", nút "Login". Trang này thuộc đăng nhập admin, không thuộc FR-17; ghi lại để nhóm xét ở feature liên quan (FR-21) | `S0_01_dang_nhap_admin.png` (chụp 18/10/2026) |

## 7. Tổng hợp

Điền sau khi chạy xong (có thể nhờ AI đếm lại từ bảng ở mục 4).

| Nhóm | Số TC | Pass | Fail | Khác giả định | Blocked | Không áp dụng | Not run |
|---|---|---|---|---|---|---|---|
| A. Dữ liệu mẫu nguyên vẹn, checklist | 8 | | | | | | |
| B. Thêm hợp lệ qua giao diện | 25 | | | | | | |
| C. Thêm không hợp lệ qua giao diện | 17 | | | | | | |
| D. Giá trị biên qua giao diện | 29 | | | | | | |
| E. Xóa không phá dữ liệu mẫu | 3 | | | | | | |
| F. API | 29 | | | | | | |
| G. Danh sách rất dài | 1 | | | | | | |
| H. Phá dữ liệu mẫu | 3 | | | | | | |
| **Tổng** | **115** | | | | | | |
