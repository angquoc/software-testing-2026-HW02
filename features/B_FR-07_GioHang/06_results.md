# S6: Kết quả chạy test (FR-07 Giỏ hàng)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test và điền file này; AI chuẩn bị khung và điền sẵn các mục checklist quan sát được từ ảnh S0
- Bản này: Sinh viên điền. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-21 07:01 (UTC+07:00)
- Căn cứ: `05_final_tc.md` (38 test case, thứ tự chạy ở mục 10, giới hạn quan sát ở mục 11), ảnh `screenshots/S0_*.png`
- Cập nhật lần 10: 2026-10-21 08:12 (UTC+07:00). Ghi thời điểm reset sau TC-CART-53 (08:11); ghi "Không chạy" ở cột Kết quả thực tế của 8 dòng Not run
- Cập nhật lần 9: 2026-10-21 08:03 (UTC+07:00). Điền TC-CART-53 theo log `S6_tc53_20261021_080248.log`; điền bảng tổng hợp (mục 5). Chờ thời điểm reset sau TC-CART-53
- Cập nhật lần 8: 2026-10-21 08:01 (UTC+07:00). Điền TC-CART-51, 54, 52 theo log `S6_api_20261021_080006.log`
- Cập nhật lần 7: 2026-10-21 08:00 (UTC+07:00). TC-CART-50 và ghi nhận 8: Ghi ảnh dùng lại `S0_05` (SV không chụp lại)
- Cập nhật lần 6: 2026-10-21 07:57 (UTC+07:00). Điền TC-CART-50 theo log `S6_api_20261021_075653.log`
- Cập nhật lần 5: 2026-10-21 07:49 (UTC+07:00). Thêm ghi nhận 8 (giỏ Web và giỏ API tách nhau, giỏ Web mất sau F5); đổi cách chạy nhóm API hợp lệ (mục 4.D)
- Cập nhật lần 4: 2026-10-21 07:45 (UTC+07:00). Điền nhóm API không hợp lệ theo log `S6_api_20261021_074419.log`; thêm ghi nhận 6, 7 ở mục 4.F
- Cập nhật lần 3: 2026-10-21 07:40 (UTC+07:00). TC-CART-03 chạy lại (ảnh `S6_TC-CART-03_3.png`): Fail; ghi quyết định của sinh viên về nhãn "Đã thêm" (mục 4.F)
- Cập nhật lần 2: 2026-10-21 07:36 (UTC+07:00). Điền kết quả giao diện theo ảnh S6 và mô tả của sinh viên; thêm mục 4.F (ghi nhận thêm khi chạy). Nhóm API chưa chạy
- Cập nhật lần 1: 2026-10-21 07:11 (UTC+07:00). Theo yêu cầu của sinh viên, soát lại mục 2.1: Dùng lại ảnh S0 khi ảnh đã chứng minh được trạng thái cần kiểm (TC-CART-10 phần 1, TC-CART-02 phần giỏ 2 dòng, TC-CART-04 đến 06); gộp ảnh trước và sau F5; bỏ ảnh dialog của TC-CART-09. Giảm từ 19 xuống 14 ảnh mới

---

## 1. Môi trường

| Mục | Giá trị |
|---|---|
| Ngày chạy | 21/10/2026 |
| Người chạy | Nguyễn Thị Ánh Ngọc |
| Hệ điều hành | Windows 11 |
| Trình duyệt và phiên bản | Chrome 155.0.8059.85 |
| SUT | EShop, commit `85af3ba` |
| Backend | `http://localhost:3000` |
| Web | `http://localhost:5173` |
| Reset dữ liệu mẫu trước đợt test (thời điểm) | 06:37 21/10/2026 |
| Ô "Số lượng:" nhận tối đa bao nhiêu (điền sau TC-CART-103) | |
| File log API | `logs/S6_api_<thời gian>.log`, `logs/S6_cart_<thời gian>.log` (kiểm chứng K1), `logs/S6_tc53_<thời gian>.log` |
| Reset dữ liệu sau TC-CART-53 (thời điểm) | 08:11 21/10/2026 (phiên điều phối khởi động lại backend) |

## 2. Cách điền

- **Kết quả thực tế:** Ghi đúng những gì quan sát được: Số dòng, Số lượng, Thành tiền, nhãn và giá trị tổng tiền (nguyên văn), có toast hay badge không, dialog có hiện không. Test case API: Mã HTTP và body, lấy từ log.
- **Trạng thái:** Pass, Fail, Blocked hoặc Not run.
  - Pass: Kết quả thực tế khớp kết quả mong đợi.
  - Fail: Không khớp. Mô tả khác ở đâu trong cột Ghi chú; đây là ứng viên bug cho S7. Khác **giả định** (không phải khác đặc tả) ghi "Khác giả định Ann".
  - Blocked: Không chạy được vì điều kiện bên ngoài test case (ví dụ giao diện không có nút). Ghi lý do.
  - Not run: Chưa chạy.
- **Ảnh:** Tên file `S6_<mã>.png` trong `screenshots/`, ví dụ `S6_TC-CART-01.png`. Test case nhiều bước: `S6_TC-CART-01_1.png`, `S6_TC-CART-01_2.png`.
- **Kiểm chứng K1:** Tải lại trang Giỏ hàng (F5), chụp ảnh; chạy `python scripts/run_api_tests.py --show-cart` để ghi `GET /api/cart` vào log.
- **Điền sẵn từ ảnh S0:** Các dòng checklist có ghi "Từ ảnh S0" do AI điền từ ảnh chụp ở S0 (cùng ngày, cùng phiên bản EShop). Sinh viên kiểm lại; nếu muốn có ảnh S6 riêng thì chụp lại và thay cột Ảnh.
- **DevTools:** Chỉ dùng cho TC-CART-96 (thuộc tính mà đặc tả yêu cầu).
- **Phạm vi chạy:** Do thời gian, sinh viên chạy danh sách tối thiểu ở mục 2.1; test case giao diện không có trong danh sách và không có ảnh thì ghi Not run.

### 2.1 Danh sách chạy tối thiểu qua giao diện

Thứ tự liền mạch theo trạng thái giỏ, bắt đầu từ giỏ trống sau reset.

Nguyên tắc: Ảnh S0 dùng lại được khi chỉ cần chứng minh **trạng thái hiển thị** (giỏ trống, giỏ 2 dòng, không có nút, không có badge); ảnh S0 cùng ngày, cùng phiên bản EShop, trạng thái dữ liệu giống (sau reset). Ảnh mới chỉ cần khi phải chứng minh **kết quả của một thao tác** (bấm nút, xóa, thêm), vì ảnh S0 không có thao tác đó. Mỗi lần chụp trang Giỏ hàng: Bấm F5 trước rồi mới chụp (một ảnh thay cho hai ảnh trước và sau F5); nếu thấy trước và sau F5 khác nhau thì chụp thêm.

| Thứ tự | Mã | Làm gì | Ảnh mới | Dùng lại ảnh S0 |
|---|---|---|---|---|
| 1 | TC-CART-10 | Giỏ đang trống: Bấm "Tiếp tục mua sắm", chụp trang đích | `S6_TC-CART-10.png` | `S0_05` cho trạng thái giỏ trống (không hình minh họa, thông báo, không badge) |
| 2 | TC-CART-01 | Trang chi tiết iPhone 15 Pro Max, giữ "Số lượng:" = 1, bấm "Thêm vào giỏ hàng", chụp **ngay** (bắt toast, badge); mở Giỏ hàng, F5, chụp; chạy `--show-cart` | `S6_TC-CART-01_1.png`, `_2.png` | Không: `S0_02` chụp trước khi bấm, không có toast |
| 3 | TC-CART-11 | Ở Giỏ hàng, bấm "← Mua tiếp" (không có nút "Tiếp tục mua sắm", O25), chụp trang đích | `S6_TC-CART-11.png` | Không |
| 4 | TC-CART-02 | Trang chủ, bấm "Thêm vào giỏ" của Samsung Galaxy S24 Ultra, chụp **ngay**; mở Giỏ hàng, xem có giống `S0_03` không; chạy `--show-cart` | `S6_TC-CART-02.png` (toast lúc bấm) | `S0_03` cho giỏ 2 dòng, tổng 58,000,000, không badge. Chỉ chụp lại nếu giỏ khác `S0_03` |
| 5 | TC-CART-07 | Bấm "Xóa" ở dòng Samsung, chụp (dialog, dòng còn không, màu nút trong dialog cho TC-CART-93); bấm hủy hoặc đóng, F5, chụp | `S6_TC-CART-07_1.png`, `_2.png` | Không |
| 6 | TC-CART-08 | Bấm "Xóa" ở dòng Samsung, xác nhận, F5, chụp; trang chủ bấm "Thêm vào giỏ" của Samsung; mở Giỏ hàng, chụp (Samsung Số lượng 1) | `S6_TC-CART-08_1.png`, `_2.png` | Không |
| 7 | TC-CART-03 | Giỏ: iPhone × 1, Samsung × 1. Trang chi tiết iPhone, nhập "Số lượng:" = 3, bấm thêm; mở Giỏ hàng, F5, chụp (vẫn 2 dòng, iPhone 4, tổng 148,000,000); `--show-cart` | `S6_TC-CART-03.png` | Không |
| 8 | TC-CART-09 | Xóa Samsung (xác nhận), không cần chụp; bấm "Xóa" ở dòng iPhone, xác nhận; chụp ngay (chưa F5) trạng thái giỏ | `S6_TC-CART-09.png` | Không: Phải thấy trạng thái giỏ trống hiện ngay sau thao tác xóa (A11), `S0_05` là lúc mở trang. Ảnh dialog không cần, đã có ở `S6_TC-CART-07_1`; chỉ chụp nếu dialog lần này khác |
| 9 | TC-CART-100 | Giỏ trống. Trang chi tiết iPhone, nhập "Số lượng:" = 0, bấm thêm, chụp **ngay** (toast, thông báo của trang hay trình duyệt); mở Giỏ hàng, chụp | `S6_TC-CART-100_1.png`, `_2.png` | Không |
| 10 | TC-CART-105 | Giỏ trống. Trang chi tiết Bàn phím cơ Keychron Q1, nhập "Số lượng:" = 250, bấm thêm; mở Giỏ hàng, chụp (1,000,000,000 ₫) | `S6_TC-CART-105.png` | Không |

Tổng: 14 ảnh mới (trước khi soát lại: 19). Không cần thao tác hay chụp: TC-CART-04 đến TC-CART-06 (đề xuất Blocked, ảnh `S0_03`: Không có nút +/-) và checklist TC-CART-90 đến 93, 95 (đã điền từ ảnh S0).

Ghi chú: Ở bước 8, Số lượng iPhone là 4 (sau TC-CART-03), khác tiền điều kiện "iPhone × 1" của TC-CART-09; không ảnh hưởng kết quả mong đợi (xóa dòng cuối). Nếu còn thời gian: TC-CART-94 (sao chép giá trị, dán vào trình soạn thảo; không cần ảnh mới), TC-CART-97 (Tab), TC-CART-96 (DevTools), TC-CART-103 (1000).

## 3. Mã kết quả mong đợi

| Mã | Kết quả mong đợi |
|---|---|
| OUT15 | Sau khi bấm nút thêm vào giỏ: Có toast hoặc badge của link "Giỏ hàng" cập nhật |
| K1 | Sau F5 và trong `GET /api/cart`: Giỏ giống kết quả mong đợi |
| OUT9 | Giỏ trống: Có hình minh họa (ảnh hoặc biểu tượng), thông báo nói rõ giỏ trống; không còn bảng |
| OUT10 | Trang chủ: `localhost:5173`, "Danh sách sản phẩm" |
| KQ-KH-API | Không trả về phản hồi thành công; giỏ không đổi (log ghi số dòng trước và sau) |

Kết quả mong đợi viết theo chữ đặc tả ("Đơn giá", "Tổng cộng", "Tiếp tục mua sắm"). Giá trị đầy đủ ở `05_final_tc.md`.

## 4. Kết quả theo thứ tự chạy

### A. Checklist giao diện

| # | Mã | Tiêu đề ngắn | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | TC-CART-90 | Bảng có đủ cột, nút xóa, nhãn Tổng cộng | Cột "Sản phẩm", "Đơn giá", "Số lượng", "Thành tiền", "Thao tác"; mỗi dòng có nút xóa; nhãn "Tổng cộng" | Cột "Sản phẩm", "Giá", "Số lượng", "Thành tiền", "Thao tác" (cột Đơn giá có nhãn "Giá"); mỗi dòng có "Xóa"; nhãn tổng "Tổng tạm tính:" | Fail | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). D01, D04 |
| 2 | TC-CART-91 | Giỏ trống có hình minh họa, thông báo, nút Tiếp tục mua sắm | Có hình minh họa; thông báo nói rõ giỏ trống; có "Tiếp tục mua sắm" | Không có hình minh họa; thông báo "Giỏ hàng của bạn đang trống"; có liên kết "Tiếp tục mua sắm" | Fail | `S0_05_gio_hang_trong.png` | Từ ảnh S0 (AI điền, SV kiểm). Thiếu hình minh họa (FR07-R15), D05 |
| 3 | TC-CART-92 | Ngôn ngữ trang và tiêu đề tab | Toàn bộ tiếng Việt, gồm tiêu đề tab | Tiêu đề tab "frontend-web" (cả khi có hàng và khi trống); chữ trên trang tiếng Việt, trừ tên riêng "EShop", "SUT" | Fail | `S0_03_gio_hang_co_hang.png`, `S0_05_gio_hang_trong.png` | Từ ảnh S0 (AI điền, SV kiểm). D10 |
| 4 | TC-CART-93 | Màu nút tích cực, nút nguy hiểm | "Tiến hành thanh toán" xanh dương; "Xóa" và nút xác nhận xóa đỏ | "Tiến hành thanh toán" nền xanh lá; "Xóa" chữ đỏ, không nền. Không có dialog xóa nên không có nút xác nhận (TC-CART-07) | Fail | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). Fail vì nút thanh toán (D09) |
| 5 | TC-CART-94 | Định dạng tiền | Ký tự `₫`, phân cách hàng nghìn | Không chạy | Not run |  | Không chạy (thiếu thời gian) |
| 6 | TC-CART-95 | Navbar highlight và breadcrumb | Mục "Giỏ hàng" được highlight; có breadcrumb | "Giỏ hàng" chữ trắng giống hệt ở trang chủ, không highlight; không có breadcrumb | Fail | `S0_01_trang_chu.png`, `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). D06, D08 |
| 7 | TC-CART-96 | Đúng 1 thẻ h1, ảnh có alt | Đúng 1 `<h1>`; ảnh sản phẩm (nếu có) có `alt` | Không chạy | Not run |  | Không chạy (thiếu thời gian) |
| 8 | TC-CART-97 | Thứ tự Tab | Trên xuống dưới, trái sang phải | Không chạy | Not run |  | Không chạy (thiếu thời gian) |

### B. Giỏ hàng qua giao diện (EP)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 9 | TC-CART-10 | Giỏ trống và Tiếp tục mua sắm | Không nhập | OUT9; badge ẩn hoặc 0; bấm "Tiếp tục mua sắm" thì OUT10 | Giỏ trống: Không có hình minh họa; thông báo "Giỏ hàng của bạn đang trống"; không có badge. Sau khi bấm "Tiếp tục mua sắm": `localhost:5173`, trang "Danh sách sản phẩm" | Fail | `S0_05_gio_hang_trong.png`, `S6_TC-CART-10.png` | Phần điều hướng đạt (OUT10); Fail vì thiếu hình minh họa (FR07-R15) |
| 10 | TC-CART-01 | Thêm sản phẩm chưa có từ trang chi tiết | iPhone 15 Pro Max, "Số lượng:" 1 | OUT15; 1 dòng, Đơn giá 30,000,000 ₫, Số lượng 1, Thành tiền 30,000,000 ₫, "Tổng cộng" 30,000,000 ₫; K1 | Giữ "Số lượng:" = 1, bấm "Thêm vào giỏ hàng": Không có gì thay đổi; nút vẫn là "Thêm vào giỏ hàng", không có toast, không có badge. Giỏ vẫn trống | Fail | `S6_TC-CART-01_1.png`, `S0_05_gio_hang_trong.png` | Sản phẩm không được thêm khi giữ số lượng mặc định; chỉ khi đổi số lượng rồi bấm thì nút mới chuyển thành "Đã thêm" và sản phẩm vào giỏ (SV quan sát). Ảnh giỏ trống dùng lại `S0_05` (SV). Ứng viên bug |
| 11 | TC-CART-11 | Tiếp tục mua sắm khi giỏ có hàng | Không nhập | OUT10; giỏ vẫn iPhone × 1 | Bấm "← Mua tiếp" (không có nút nhãn "Tiếp tục mua sắm"): Về `localhost:5173`, trang "Danh sách sản phẩm" | Pass | `S6_TC-CART-10.png` (trang đích giống, SV không chụp lại) | Đạt FR07-R13. Nhãn nút sai đã ghi ở TC-CART-90 (FR07-R12). Giỏ lúc chạy là các dòng Samsung, không phải iPhone × 1 (TC-CART-01 Fail) |
| 12 | TC-CART-02 | Thêm từ trang chủ khi giỏ có 1 dòng | Samsung Galaxy S24 Ultra, nút "Thêm vào giỏ" | OUT15; 2 dòng; "Tổng cộng" 58,000,000 ₫; badge 2; K1 | Bấm "Thêm vào giỏ" của Samsung ở trang chủ: Không có toast, không có badge, trang chủ đứng nguyên. Bấm 1 lần thì giỏ có 1 dòng Samsung; bấm 2 lần thì giỏ có 2 dòng Samsung riêng (mỗi dòng Số lượng 1, Thành tiền 28,000,000 ₫); "Tổng tạm tính:" 56,000,000 ₫ | Fail | `S6_TC-CART-02.png` | Fail OUT15 (không phản hồi, FR07-R33) và badge (FR07-R24). Tiền điều kiện khác (giỏ không có iPhone vì TC-CART-01 Fail) nên mong đợi 58,000,000 không áp dụng; tổng 56,000,000 = 2 × 28,000,000 đúng A02. Thêm trùng qua trang chủ tạo dòng mới: Trái FR07-R08, R09 (xem mục 6) |
| 13 | TC-CART-07 | Hủy dialog xóa | "Xóa" dòng Samsung, rồi hủy | Dialog hiện, dòng còn khi dialog mở; sau hủy vẫn 2 dòng, 58,000,000 ₫; K1 | Bấm "Xóa" ở 1 trong 2 dòng Samsung: Không có dialog; dòng bị xóa ngay | Fail | `S6_TC-CART-02.png` (trước), `S6_TC-CART-08.png` (sau) | Fail FR07-R11. Không thực hiện được bước hủy dialog |
| 14 | TC-CART-08 | Xác nhận xóa 1 trong 2 dòng | "Xóa" dòng Samsung, xác nhận; thêm lại Samsung | Còn iPhone, 30,000,000 ₫; K1; thêm lại: Samsung dòng mới, Số lượng 1 | Xóa 1 trong 2 dòng Samsung: Không có dialog; còn 1 dòng Samsung, "Tổng tạm tính:" 28,000,000 ₫. Thêm lại Samsung từ trang chủ: Giỏ lại có 2 dòng Samsung riêng, giống `S6_TC-CART-02` | Fail | `S6_TC-CART-08.png` | Phần xóa dòng và cập nhật tổng đạt; Fail vì không có dialog (FR07-R11). Thêm lại khi giỏ còn 1 dòng Samsung tạo dòng mới thay vì tăng số lượng (FR07-R09). SV không chụp ảnh sau khi thêm lại. Chưa kiểm K1 |
| 15 | TC-CART-03 | Thêm lại sản phẩm đã có với số lượng 3 | iPhone, "Số lượng:" 3 | Vẫn 2 dòng; iPhone 4, 120,000,000 ₫; "Tổng cộng" 148,000,000 ₫; badge 5; K1 | Lần 1: Giỏ có 2 dòng Samsung, chưa có iPhone; trang chi tiết iPhone, "Số lượng:" = 3, bấm "Thêm vào giỏ hàng" (bấm lần 2 nút mới thành "Đã thêm"): Thêm dòng iPhone, Số lượng 3, Thành tiền 90,000,000 ₫. Lần 2 (chạy lại khi giỏ đã có iPhone × 3): Thêm iPhone với "Số lượng:" = 2 tạo dòng iPhone mới (Số lượng 2, Thành tiền 60,000,000 ₫), dòng iPhone × 3 giữ nguyên; giỏ có 2 dòng iPhone; "Tổng tạm tính:" 1,150,000,000 ₫ (cùng dòng Keychron × 250) | Fail | `S6_TC-CART-03_1.png`, `S6_TC-CART-03_2.png`, `S6_TC-CART-03_3.png` | Fail FR07-R08, FR07-R09: Thêm sản phẩm đã có tạo dòng mới thay vì tăng số lượng (SV: mỗi lần thêm là 1 dòng mới). Tổng 1,150,000,000 = 1,000,000,000 + 60,000,000 + 90,000,000 đúng A02 |
| 16 | TC-CART-09 | Xóa dòng cuối cùng | "Xóa" dòng iPhone, xác nhận | Dialog hiện trước; sau xác nhận hiện ngay OUT9 | Xóa lần lượt đến dòng cuối: Không có dialog; sau khi xóa dòng cuối hiện trạng thái giỏ trống (như `S0_05`) | Fail | `S0_05_gio_hang_trong.png` (SV không chụp lại) | Fail FR07-R11 (không có dialog) và FR07-R15 (không có hình minh họa). Trạng thái giỏ trống hiện sau khi xóa theo SV quan sát |
| 17 | TC-CART-04 | Tăng bằng nút tăng | Nút tăng | Số lượng 2; 60,000,000 ₫ | Cột Số lượng chỉ có số, không có nút tăng | Blocked | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). D02 |
| 18 | TC-CART-05 | Giảm khi số lượng 2 | Nút giảm | Số lượng 1; 30,000,000 ₫ | Không có nút giảm | Blocked | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). D02 |
| 19 | TC-CART-06 | Giảm khi số lượng 1 | Nút giảm | Số lượng không nhỏ hơn 1; nếu xóa thì qua dialog (A04) | Không có nút giảm | Blocked | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). D02 |
| 20 | TC-CART-12 | Thành tiền, Tổng cộng từ 1 tỷ | MacBook Pro M3, "Số lượng:" 23 | 1,035,000,000 ₫ | Không chạy | Not run |  | Không chạy; định dạng từ 1 tỷ đã kiểm ở TC-CART-105 |

### C. Giá trị biên qua giao diện (BVA)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 21 | TC-CART-100 | Số lượng 0 ở trang chi tiết | iPhone, "Số lượng:" 0 | Giỏ vẫn trống; không có toast thành công, badge không đổi (A31) | Không chạy | Not run |  | Không chạy (thiếu thời gian) |
| 22 | TC-CART-101 | Số lượng 2 | iPhone, "Số lượng:" 2 | OUT15; Số lượng 2, 60,000,000 ₫ | Không chạy | Not run |  | Không chạy (thiếu thời gian) |
| 23 | TC-CART-103 | Số lượng 1000 | Keychron Q1, "Số lượng:" 1000 | Số lượng 1000; 4,000,000,000 ₫ | Không chạy | Not run |  | Không chạy (thiếu thời gian) |
| 24 | TC-CART-104 | Ngay dưới 1 tỷ | Keychron Q1, "Số lượng:" 249 | 996,000,000 ₫ | Không chạy | Not run |  | Không chạy (thiếu thời gian) |
| 25 | TC-CART-105 | Đúng 1 tỷ | Keychron Q1, "Số lượng:" 250 | 1,000,000,000 ₫ | Trang chi tiết Bàn phím cơ Keychron Q1 (`/product/5`), "Số lượng:" = 250: Nút thành "Đã thêm". Giỏ: 1 dòng, Đơn giá 4,000,000 ₫, Số lượng 250, Thành tiền 1,000,000,000 ₫; "Tổng tạm tính:" 1,000,000,000 ₫ | Pass | `S6_TC-CART-105_1.png`, `S6_TC-CART-105_2.png` | Giá trị và định dạng (3 dấu phân cách) đúng. Nhãn "Tổng tạm tính" đã ghi Fail ở TC-CART-90 |

### D. API (script `scripts/run_api_tests.py`)

Không hợp lệ: Chạy `python scripts/run_api_tests.py` (TC-CART-30 đến 35, 102, 36). Hợp lệ: Mỗi test case một lệnh `--only`. Vì giỏ của API tách khỏi giỏ trên Web (mục 4.F, ghi nhận 8), xóa trên giao diện không làm trống giỏ API; không xóa giỏ, bỏ qua cảnh báo "Giỏ chưa trống" của script, đánh giá theo dòng mới xuất hiện giữa "Giỏ trước" và "Giỏ sau" trong log.

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 26 | TC-CART-30 | `id` không tồn tại | `id`: 9999 | KQ-KH-API | `GET /api/products/9999`: HTTP 200, body `{}`. `POST`: HTTP 200 `{"message": "Added to cart"}`; giỏ thêm dòng `id` 9999 với `name`, `price` do client gửi | Fail | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. Hệ thống nhận sản phẩm không tồn tại (khác A24) |
| 27 | TC-CART-31 | Số lượng 0 | `quantity`: 0 | KQ-KH-API | HTTP 200 `Added to cart`; giỏ thêm dòng `id` 1, `quantity` 0 | Fail | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. Nhận số lượng 0 (FR07-R27) |
| 28 | TC-CART-32 | Số lượng thập phân | `quantity`: 1.5 | KQ-KH-API | HTTP 200 `Added to cart`; giỏ thêm dòng `quantity` 1.5 | Fail | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. Nhận số lượng thập phân (FR07-R27) |
| 29 | TC-CART-33 | Số lượng không phải số | `quantity`: `"abc"` | KQ-KH-API | HTTP 200 `Added to cart`; giỏ thêm dòng `quantity` `"abc"` | Fail | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. Nhận số lượng không phải số |
| 30 | TC-CART-34 | Thiếu `quantity` | Bỏ trường `quantity` | KQ-KH-API | HTTP 200 `Added to cart`; giỏ thêm dòng không có `quantity` (null) | Fail | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. Nhận body thiếu trường (khác A25) |
| 31 | TC-CART-35 | Thiếu header Authorization | Không gửi header | KQ-KH-API | HTTP 401 `{"error": "Unauthorized"}`; giỏ không đổi | Pass | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. |
| 32 | TC-CART-102 | Số lượng âm | `quantity`: -1 | KQ-KH-API | HTTP 200 `Added to cart`; giỏ thêm dòng `quantity` -1 | Fail | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. Nhận số lượng âm (FR07-R27) |
| 33 | TC-CART-36 | Token sai | `GET` với token sửa 1 ký tự | Bước 2 không thành công, không có dữ liệu giỏ | Bước 1: HTTP 200. Bước 2: HTTP 403 `{"error": "Forbidden"}`, không có dữ liệu giỏ | Pass | Log `logs/S6_api_20261021_074419.log` | Bằng chứng: log API. |
| 34 | TC-CART-50 | Thêm và xem giỏ qua API | Body cơ sở | `POST` thành công; `GET` có `id` 1, số lượng 1; trang Giỏ hàng như TC-CART-01 | `POST`: HTTP 200 `Added to cart`. `GET`: Giỏ API từ 7 lên 8 dòng, dòng mới `id` 1, số lượng 1. Trang Giỏ hàng sau F5: Trống (SV quan sát) | Fail | Log `logs/S6_api_20261021_075653.log`; `S0_05_gio_hang_trong.png` (trang Giỏ hàng trống giống ảnh này nên SV không chụp lại) | Phần API đạt; Fail vì dòng thêm qua API không hiện trên trang Giỏ hàng (ghi nhận 8). Tiền điều kiện khác (giỏ API đã có 7 dòng từ nhóm không hợp lệ). Dòng "Gợi ý: Số lượng của id 1 = 0" trong log lấy nhầm dòng `id` 1 đầu tiên, không dùng |
| 35 | TC-CART-51 | `price` khác giá CSDL | `price`: 1 | Không có dòng Đơn giá 1 ₫; nếu thêm được thì 30,000,000 ₫ | HTTP 200 `Added to cart`; giỏ API thêm dòng `id` 1, `price` 1, số lượng 1 | Fail | Log `logs/S6_api_20261021_080006.log` | Bằng chứng: log API. Tiền điều kiện khác (giỏ API chưa trống). Hệ thống lưu giá do client gửi (khác A24; FR-08: Backend không tin số tiền client gửi). Không xem được trên trang Giỏ hàng (ghi nhận 8) |
| 36 | TC-CART-54 | Người dùng khác không thấy giỏ | Token `admin@eshop.com` | `GET` của admin không có dòng `id` 1 vừa thêm | Bước 1: HTTP 200, giỏ của `test@eshop.com` từ 9 lên 10 dòng. Bước 2: `GET /api/cart` bằng token `admin@eshop.com` trả giỏ trống, không có dòng `id` 1 | Pass | Log `logs/S6_api_20261021_080006.log` | Bằng chứng: log API. Tiền điều kiện khác (giỏ API chưa trống). |
| 37 | TC-CART-52 | `name` có thẻ HTML | `name`: `<b>X</b>` | Tên hiển thị nguyên văn hoặc tên CSDL; không có "X" in đậm | HTTP 200 `Added to cart`; giỏ API lưu nguyên văn `name` = `<b>X</b>`. Trang Giỏ hàng không hiển thị giỏ API nên không xem được tên có bị render HTML không | Blocked | Log `logs/S6_api_20261021_080006.log` | Bằng chứng: log API. Tiền điều kiện khác (giỏ API chưa trống). Điều cần kiểm (hiển thị trên giao diện) không quan sát được vì giỏ Web và giỏ API tách nhau (ghi nhận 8) |

### E. Bảo mật, chạy cuối cùng (`--only 53`)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 38 | TC-CART-53 | `name` có ký tự SQL | `name`: `X' OR '1'='1` | `POST` không lỗi hệ thống; `GET` đúng 1 dòng `id` 1, số lượng 1 | `POST`: HTTP 200 `Added to cart`, không lỗi hệ thống. `GET`: HTTP 200, giỏ API từ 11 lên 12 dòng; đúng 1 dòng mới `id` 1, số lượng 1, `name` lưu nguyên văn `X' OR '1'='1`; không có dòng lạ, các dòng cũ giữ nguyên | Pass | Log `logs/S6_tc53_20261021_080248.log` | Tiền điều kiện khác (giỏ API chưa trống), đánh giá theo dòng mới. FR07-R32 chỉ quan sát gián tiếp (GH4). Reset dữ liệu sau test case: Xem mục 1 |

### F. Ghi nhận thêm khi chạy (ứng viên cho S7, S8)

Do sinh viên quan sát khi chạy các test case trên; không có test case riêng trong `05_final_tc.md`.

| # | Ghi nhận | Liên quan | Bằng chứng |
|---|---|---|---|
| 1 | Trang chi tiết: Giữ "Số lượng:" mặc định 1 rồi bấm "Thêm vào giỏ hàng" thì không thêm gì; chỉ khi đổi số lượng rồi bấm mới thêm | TC-CART-01; FR07-R27 (mặc định 1 là hợp lệ), FR07-R33 | `S6_TC-CART-01_1.png`, `S0_05_gio_hang_trong.png` |
| 2 | Trang chi tiết: Bấm "Thêm vào giỏ hàng" lần đầu không có phản hồi; bấm lần 2 nút mới thành "Đã thêm"; giỏ chỉ thêm một lần (Số lượng 3, không phải 6) | TC-CART-03, TC-CART-105; FR07-R33 | `S6_TC-CART-03_1.png`, `S6_TC-CART-03_2.png` |
| 3 | Thêm sản phẩm đã có trong giỏ tạo dòng mới thay vì tăng số lượng, ở cả trang chủ và trang chi tiết | TC-CART-02, TC-CART-03, TC-CART-08; FR07-R08, FR07-R09 | `S6_TC-CART-02.png`, `S6_TC-CART-03_3.png` |
| 4 | Phản hồi sau khi thêm: Trang chủ không có gì; trang chi tiết chỉ đổi nhãn nút thành "Đã thêm". Không có toast, không có badge | TC-CART-01, TC-CART-02; FR07-R24, FR07-R33 | `S6_TC-CART-02.png`, `S6_TC-CART-03_1.png` |
| 5 | Bấm "Xóa" xóa ngay, không có dialog xác nhận | TC-CART-07 đến 09; FR07-R11 | `S6_TC-CART-02.png`, `S6_TC-CART-08.png` |
| 6 | `POST /api/cart` nhận mọi dữ liệu không hợp lệ (sản phẩm không tồn tại, số lượng 0, âm, thập phân, chữ, thiếu trường), luôn trả HTTP 200 và thêm dòng vào giỏ | TC-CART-30 đến 34, 102; FR07-R27, FR07-R29 | `logs/S6_api_20261021_074419.log` |
| 7 | Qua API, mỗi lần `POST` cùng `id` 1 cũng tạo dòng mới, không cộng số lượng | TC-CART-31 đến 34, 102, 36; FR07-R08, FR07-R09 | `logs/S6_api_20261021_074419.log` |
| 8 | Giỏ trên trang Web và giỏ của API tách nhau: Lúc 07:38 trang Giỏ hàng có 3 dòng (`S6_TC-CART-03_3.png`) nhưng lúc 07:44 `GET /api/cart` trả giỏ trống; sau khi API thêm 7 dòng, F5 trang Giỏ hàng lại trống. Giỏ trên Web cũng không được giữ sau F5 (SV không xóa gì) | FR07-R28, Q14 (đặc tả không nói rõ, ghi chờ xét ở S7); giới hạn GH1: Kiểm chứng K1 không dùng được | `S6_TC-CART-03_3.png`, `S0_05_gio_hang_trong.png` (trang trống sau F5 giống ảnh này nên SV không chụp lại), `logs/S6_api_20261021_074419.log`, `logs/S6_api_20261021_075653.log` |

Ghi chú cho S8: Ghi nhận 3 ở đường trang chủ nằm ngoài phạm vi thiết kế (thêm trùng chỉ kiểm qua trang chi tiết, `01_io.md` quyết định 10, giới hạn GH6); ở đường trang chi tiết đã được TC-CART-03 bắt.

Quyết định của sinh viên khi chạy: Nhãn nút đổi thành "Đã thêm" không tính là phản hồi trực quan theo FR07-R33 (đặc tả nêu dạng "toast notification hoặc badge cập nhật"), nên TC-CART-01, 02 giữ Fail ở FR07-R33.

## 5. Tổng hợp

AI đếm từ bảng ở mục 4 (cập nhật lần 9).

| Nhóm | Số TC | Pass | Fail | Blocked | Not run |
|---|---|---|---|---|---|
| A. Checklist giao diện | 8 | 0 | 5 | 0 | 3 |
| B. Giỏ hàng qua giao diện | 12 | 1 | 7 | 3 | 1 |
| C. Giá trị biên qua giao diện | 5 | 1 | 0 | 0 | 4 |
| D. API | 12 | 3 | 8 | 1 | 0 |
| E. Bảo mật, chạy cuối cùng | 1 | 1 | 0 | 0 | 0 |
| **Tổng** | **38** | **6** | **20** | **4** | **8** |
