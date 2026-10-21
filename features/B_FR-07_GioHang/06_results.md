# S6: Kết quả chạy test (FR-07 Giỏ hàng)

- Bước: S6 (Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh). Sinh viên chạy test và điền file này; AI chuẩn bị khung và điền sẵn các mục checklist quan sát được từ ảnh S0
- Bản này: Sinh viên điền. Bản gốc của AI: `ai_raw/S6_results_template.md`
- Thời gian tạo khung: 2026-10-21 07:01 (UTC+07:00)
- Căn cứ: `05_final_tc.md` (38 test case, thứ tự chạy ở mục 10, giới hạn quan sát ở mục 11), ảnh `screenshots/S0_*.png`

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
| Reset dữ liệu sau TC-CART-53 (thời điểm) | |

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

| Thứ tự | Mã | Làm gì | Ảnh |
|---|---|---|---|
| 1 | TC-CART-10 | Mở trang Giỏ hàng khi giỏ trống; chụp; bấm "Tiếp tục mua sắm"; chụp trang đích | `S6_TC-CART-10_1.png`, `S6_TC-CART-10_2.png` |
| 2 | TC-CART-01 | Trang chi tiết iPhone 15 Pro Max, giữ "Số lượng:" = 1, bấm "Thêm vào giỏ hàng", chụp **ngay** (bắt toast, badge); mở Giỏ hàng, chụp; F5, chụp; chạy `--show-cart` | `S6_TC-CART-01_1.png` đến `_3.png` |
| 3 | TC-CART-11 | Ở Giỏ hàng (iPhone × 1), bấm nút quay về ("Tiếp tục mua sắm" hoặc "← Mua tiếp"); chụp trang đích; mở lại Giỏ hàng | `S6_TC-CART-11.png` |
| 4 | TC-CART-02 | Trang chủ, bấm "Thêm vào giỏ" của Samsung Galaxy S24 Ultra, chụp ngay; mở Giỏ hàng, chụp (tổng 58,000,000, badge); F5; `--show-cart` | `S6_TC-CART-02_1.png`, `_2.png` |
| 5 | TC-CART-07 | Bấm "Xóa" ở dòng Samsung; chụp (dialog có hiện không, dòng còn không); bấm nút hủy hoặc đóng; chụp; F5. Ghi luôn màu nút trong dialog cho TC-CART-93 | `S6_TC-CART-07_1.png`, `_2.png` |
| 6 | TC-CART-08 | Bấm "Xóa" ở dòng Samsung, xác nhận; chụp; F5, `--show-cart`; trang chủ bấm "Thêm vào giỏ" của Samsung; mở Giỏ hàng, chụp (Samsung Số lượng 1) | `S6_TC-CART-08_1.png`, `_2.png` |
| 7 | TC-CART-03 | Giỏ: iPhone × 1, Samsung × 1. Trang chi tiết iPhone, nhập "Số lượng:" = 3, bấm thêm; mở Giỏ hàng, chụp (vẫn 2 dòng, iPhone 4, tổng 148,000,000, badge 5); F5, `--show-cart` | `S6_TC-CART-03_1.png`, `_2.png` |
| 8 | TC-CART-09 | Xóa Samsung (xác nhận) cho giỏ còn 1 dòng; bấm "Xóa" ở dòng iPhone, chụp dialog; xác nhận; chụp trạng thái giỏ trống | `S6_TC-CART-09_1.png`, `_2.png` |
| 9 | TC-CART-100 | Giỏ trống. Trang chi tiết iPhone, nhập "Số lượng:" = 0, bấm thêm, chụp ngay (toast?, thông báo của trình duyệt?); mở Giỏ hàng, chụp | `S6_TC-CART-100_1.png`, `_2.png` |
| 10 | TC-CART-105 | Giỏ trống. Trang chi tiết Bàn phím cơ Keychron Q1, nhập "Số lượng:" = 250, bấm thêm; mở Giỏ hàng, chụp (1,000,000,000 ₫) | `S6_TC-CART-105.png` |

Ghi chú: Ở bước 8, Số lượng iPhone là 4 (sau TC-CART-03), khác tiền điều kiện "iPhone × 1" của TC-CART-09; không ảnh hưởng kết quả mong đợi (xóa dòng cuối). TC-CART-04 đến TC-CART-06 không cần thao tác: Giao diện không có nút +/- (`S0_03`), đề xuất Blocked. Nếu còn thời gian: TC-CART-94 (sao chép giá trị, dán vào trình soạn thảo), TC-CART-97 (Tab), TC-CART-96 (DevTools), TC-CART-103 (1000).

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
| 4 | TC-CART-93 | Màu nút tích cực, nút nguy hiểm | "Tiến hành thanh toán" xanh dương; "Xóa" và nút xác nhận xóa đỏ | "Tiến hành thanh toán" nền xanh lá; "Xóa" chữ đỏ, không nền. Nút xác nhận trong dialog: Chưa quan sát | Fail | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). Fail vì nút thanh toán (D09); bổ sung màu nút dialog khi chạy TC-CART-07 |
| 5 | TC-CART-94 | Định dạng tiền | Ký tự `₫`, phân cách hàng nghìn | Phân cách hàng nghìn bằng dấu phẩy ("30,000,000 ₫"); ký hiệu đứng sau số, ảnh không phân biệt được `₫` với chữ `đ` gạch dưới |  | `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền một phần). Cần sao chép giá trị, dán vào trình soạn thảo (Q29) rồi chốt trạng thái |
| 6 | TC-CART-95 | Navbar highlight và breadcrumb | Mục "Giỏ hàng" được highlight; có breadcrumb | "Giỏ hàng" chữ trắng giống hệt ở trang chủ, không highlight; không có breadcrumb | Fail | `S0_01_trang_chu.png`, `S0_03_gio_hang_co_hang.png` | Từ ảnh S0 (AI điền, SV kiểm). D06, D08 |
| 7 | TC-CART-96 | Đúng 1 thẻ h1, ảnh có alt | Đúng 1 `<h1>`; ảnh sản phẩm (nếu có) có `alt` |  |  |  | DevTools. Giỏ không hiển thị ảnh (GH8) |
| 8 | TC-CART-97 | Thứ tự Tab | Trên xuống dưới, trái sang phải |  |  |  |  |

### B. Giỏ hàng qua giao diện (EP)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 9 | TC-CART-10 | Giỏ trống và Tiếp tục mua sắm | Không nhập | OUT9; badge ẩn hoặc 0; bấm "Tiếp tục mua sắm" thì OUT10 |  |  |  |  |
| 10 | TC-CART-01 | Thêm sản phẩm chưa có từ trang chi tiết | iPhone 15 Pro Max, "Số lượng:" 1 | OUT15; 1 dòng, Đơn giá 30,000,000 ₫, Số lượng 1, Thành tiền 30,000,000 ₫, "Tổng cộng" 30,000,000 ₫; K1 |  |  |  |  |
| 11 | TC-CART-11 | Tiếp tục mua sắm khi giỏ có hàng | Không nhập | OUT10; giỏ vẫn iPhone × 1 |  |  |  | Nếu chỉ có "← Mua tiếp" thì ghi nhận và bấm nút đó |
| 12 | TC-CART-02 | Thêm từ trang chủ khi giỏ có 1 dòng | Samsung Galaxy S24 Ultra, nút "Thêm vào giỏ" | OUT15; 2 dòng; "Tổng cộng" 58,000,000 ₫; badge 2; K1 |  |  |  |  |
| 13 | TC-CART-07 | Hủy dialog xóa | "Xóa" dòng Samsung, rồi hủy | Dialog hiện, dòng còn khi dialog mở; sau hủy vẫn 2 dòng, 58,000,000 ₫; K1 |  |  |  | Ghi màu nút trong dialog vào TC-CART-93 |
| 14 | TC-CART-08 | Xác nhận xóa 1 trong 2 dòng | "Xóa" dòng Samsung, xác nhận; thêm lại Samsung | Còn iPhone, 30,000,000 ₫; K1; thêm lại: Samsung dòng mới, Số lượng 1 |  |  |  |  |
| 15 | TC-CART-03 | Thêm lại sản phẩm đã có với số lượng 3 | iPhone, "Số lượng:" 3 | Vẫn 2 dòng; iPhone 4, 120,000,000 ₫; "Tổng cộng" 148,000,000 ₫; badge 5; K1 |  |  |  |  |
| 16 | TC-CART-09 | Xóa dòng cuối cùng | "Xóa" dòng iPhone, xác nhận | Dialog hiện trước; sau xác nhận hiện ngay OUT9 |  |  |  | Số lượng iPhone là 4 (mục 2.1), không ảnh hưởng |
| 17 | TC-CART-04 | Tăng bằng nút tăng | Nút tăng | Số lượng 2; 60,000,000 ₫ |  |  |  | Dự kiến Blocked: Không có nút (`S0_03`) |
| 18 | TC-CART-05 | Giảm khi số lượng 2 | Nút giảm | Số lượng 1; 30,000,000 ₫ |  |  |  | Dự kiến Blocked |
| 19 | TC-CART-06 | Giảm khi số lượng 1 | Nút giảm | Số lượng không nhỏ hơn 1; nếu xóa thì qua dialog (A04) |  |  |  | Dự kiến Blocked |
| 20 | TC-CART-12 | Thành tiền, Tổng cộng từ 1 tỷ | MacBook Pro M3, "Số lượng:" 23 | 1,035,000,000 ₫ |  |  |  |  |

### C. Giá trị biên qua giao diện (BVA)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 21 | TC-CART-100 | Số lượng 0 ở trang chi tiết | iPhone, "Số lượng:" 0 | Giỏ vẫn trống; không có toast thành công, badge không đổi (A31) |  |  |  | Ghi thông báo của trang hay của trình duyệt (GH3) |
| 22 | TC-CART-101 | Số lượng 2 | iPhone, "Số lượng:" 2 | OUT15; Số lượng 2, 60,000,000 ₫ |  |  |  |  |
| 23 | TC-CART-103 | Số lượng 1000 | Keychron Q1, "Số lượng:" 1000 | Số lượng 1000; 4,000,000,000 ₫ |  |  |  | Ghi số ô thực sự nhận vào mục 1 (GH7) |
| 24 | TC-CART-104 | Ngay dưới 1 tỷ | Keychron Q1, "Số lượng:" 249 | 996,000,000 ₫ |  |  |  |  |
| 25 | TC-CART-105 | Đúng 1 tỷ | Keychron Q1, "Số lượng:" 250 | 1,000,000,000 ₫ |  |  |  |  |

### D. API (script `scripts/run_api_tests.py`)

Không hợp lệ: Chạy `python scripts/run_api_tests.py` (TC-CART-30 đến 35, 102, 36). Hợp lệ: Mỗi test case một lệnh `--only`, xóa hết giỏ qua giao diện trước mỗi lệnh (script báo nếu giỏ chưa trống).

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 26 | TC-CART-30 | `id` không tồn tại | `id`: 9999 | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 27 | TC-CART-31 | Số lượng 0 | `quantity`: 0 | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 28 | TC-CART-32 | Số lượng thập phân | `quantity`: 1.5 | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 29 | TC-CART-33 | Số lượng không phải số | `quantity`: `"abc"` | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 30 | TC-CART-34 | Thiếu `quantity` | Bỏ trường `quantity` | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 31 | TC-CART-35 | Thiếu header Authorization | Không gửi header | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 32 | TC-CART-102 | Số lượng âm | `quantity`: -1 | KQ-KH-API |  |  |  | Bằng chứng: log API |
| 33 | TC-CART-36 | Token sai | `GET` với token sửa 1 ký tự | Bước 2 không thành công, không có dữ liệu giỏ |  |  |  | Bằng chứng: log API; bước 1 thêm 1 dòng |
| 34 | TC-CART-50 | Thêm và xem giỏ qua API | Body cơ sở | `POST` thành công; `GET` có `id` 1, số lượng 1; trang Giỏ hàng như TC-CART-01 |  |  |  | `--only 50`; chụp trang Giỏ hàng |
| 35 | TC-CART-51 | `price` khác giá CSDL | `price`: 1 | Không có dòng Đơn giá 1 ₫; nếu thêm được thì 30,000,000 ₫ |  |  |  | `--only 51` |
| 36 | TC-CART-54 | Người dùng khác không thấy giỏ | Token `admin@eshop.com` | `GET` của admin không có dòng `id` 1 vừa thêm |  |  |  | `--only 54` |
| 37 | TC-CART-52 | `name` có thẻ HTML | `name`: `<b>X</b>` | Tên hiển thị nguyên văn hoặc tên CSDL; không có "X" in đậm |  |  |  | `--only 52`; mở trang Giỏ hàng, chụp |

### E. Bảo mật, chạy cuối cùng (`--only 53`)

| # | Mã | Tiêu đề ngắn | Giá trị nhập chính | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ảnh | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 38 | TC-CART-53 | `name` có ký tự SQL | `name`: `X' OR '1'='1` | `POST` không lỗi hệ thống; `GET` đúng 1 dòng `id` 1, số lượng 1 |  |  |  | Chạy cuối; reset ngay sau, ghi thời điểm vào mục 1 |

## 5. Tổng hợp

Điền sau khi chạy xong (có thể nhờ AI đếm lại từ bảng ở mục 4).

| Nhóm | Số TC | Pass | Fail | Blocked | Not run |
|---|---|---|---|---|---|
| A. Checklist giao diện | 8 | | | | |
| B. Giỏ hàng qua giao diện | 12 | | | | |
| C. Giá trị biên qua giao diện | 5 | | | | |
| D. API | 12 | | | | |
| E. Bảo mật, chạy cuối cùng | 1 | | | | |
| **Tổng** | **38** | | | | |
