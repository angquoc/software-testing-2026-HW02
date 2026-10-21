# S4: Phân tích giá trị biên (FR-07 Giỏ hàng, Web)

- Bước: S4 (Phân tích giá trị biên, theo Step 4 của slide S04)
- Bản này: Bản review của S4. Bản gốc của AI: `ai_raw/S4_bva.md`
- Thời gian tạo bản AI: 2026-10-21 06:47 (UTC+07:00)
- Cập nhật theo quyết định của sinh viên: 2026-10-21 06:54 (UTC+07:00). Sinh viên chấp nhận cả 4 điểm đã áp; nội dung không đổi. Các thay đổi so với bản AI liệt kê ở mục cuối
- Căn cứ: `ai_raw/S4_bva.md`, `02_ec.md`, `03_tc.md`

---

## 1. Cách làm

- Chỉ áp BVA cho phân vùng có thứ tự thật sự: Số lượng thêm, số lượng hiện tại khi giảm, số dòng trong giỏ, độ lớn giá trị tiền. Không áp cho tập giá trị (đường thêm, token, dialog).
- Không áp máy móc 9 điểm: Phân vùng không có cận trên (A05) thì không có UB và điểm giữa; thay bằng một điểm thăm dò giá trị lớn. Điểm trùng test case đã có thì dùng lại.
- Tiền điều kiện chung, cách đọc kết quả, giá trị cơ sở: Như `03_tc.md` mục 1. Mã mới từ TC-CART-100.
- Đã xét mọi điểm hẹn ở `02_ec.md` mục 9 và `03_tc.md` mục 14.

## 2. Phân vùng có thứ tự

| Mã | Phân vùng | Cận dưới (LB) | Cận trên (UB) | Căn cứ |
|---|---|---|---|---|
| P1 | IN2 số lượng thêm (EC03, EC04) | 1 | Không có (A05) | FR-06: Số nguyên dương, tối thiểu 1 |
| P2 | IN11 số lượng hiện tại khi bấm giảm (EC12, EC13) | 1 | Không có | A04 |
| P3 | IN9 số dòng trong giỏ (EC24 đến EC26) | 0 | Không có | FR-07: Giỏ trống và giỏ có hàng |
| P4 | Độ lớn giá trị tiền, biên thêm nhóm phân cách (EC29, EC30) | 1,000,000,000 | Không xét | FR-21: Phân cách hàng nghìn |

## 3. Bảng giá trị biên

### 3.1 P1: Số lượng thêm

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB-1, qua giao diện | Ô "Số lượng:" = 0, trang chi tiết iPhone 15 Pro Max | 0 | KH | ERR2: Giỏ vẫn trống; không có toast thành công, badge không đổi (A31) | TC-CART-100 |
| LB-1, qua API | `quantity` = 0 | 0 | KH | ERR2 | TC-CART-31 (đã có) |
| Số âm, qua API | `quantity` = -1 | -1 | KH | ERR2: Không trả về phản hồi thành công; giỏ vẫn trống | TC-CART-102 |
| LB | Ô "Số lượng:" = 1 | 1 | H | OUT2 | TC-CART-01 (đã có) |
| LB+1 | Ô "Số lượng:" = 2, trang chi tiết iPhone 15 Pro Max | 2 | H | OUT2, OUT15: 1 dòng, Số lượng 2, Thành tiền 60,000,000 ₫, "Tổng cộng" 60,000,000 ₫ | TC-CART-101 |
| Thăm dò giá trị lớn | Ô "Số lượng:" = 1000, trang chi tiết Bàn phím cơ Keychron Q1 | 1000 | H | OUT2: Số lượng 1000, Thành tiền 4,000,000,000 ₫, "Tổng cộng" 4,000,000,000 ₫. Ghi số ô thực sự nhận ở S6 | TC-CART-103 |
| UB-1, UB, UB+1, giữa | Không áp dụng | | | Không có cận trên (A05) | |

Lý do tách số âm khỏi 0: Luật "khác 0" và luật "lớn hơn 0" cho kết quả khác nhau ở số âm; chỉ chạy qua API để không phụ thuộc ô nhập của trình duyệt. Giá trị qua giao diện (TC-CART-100, 101, 103) phản ánh cả trình duyệt và hệ thống (`platforms.md`); ghi trình duyệt ở S6.

### 3.2 P2: Số lượng hiện tại khi bấm giảm

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB | Dòng có Số lượng 1 | 1 | H | Theo A04 | TC-CART-06 (đã có) |
| LB+1 | Dòng có Số lượng 2 | 2 | H | Số lượng 1 | TC-CART-05 (đã có) |
| LB-1 | Không áp dụng | 0 | | Giỏ không thể có dòng số lượng 0 | |

Cả hai test case dự kiến Blocked (D02).

### 3.3 P3: Số dòng trong giỏ

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB | Giỏ trống | 0 | H | OUT9 | TC-CART-10 (đã có) |
| LB+1 | 1 dòng | 1 | H | OUT1, OUT6 | TC-CART-01 (đã có) |
| LB+2 | 2 dòng | 2 | H | OUT6 cộng 2 dòng | TC-CART-02 (đã có) |

Không thăm dò số dòng lớn: Dữ liệu mẫu chỉ thấy 5 sản phẩm, không có lý do tin giỏ nhiều dòng hơn được xử lý khác.

### 3.4 P4: Độ lớn giá trị tiền

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB-1 (giá trị gần nhất tạo được) | Bàn phím cơ Keychron Q1 (4,000,000), "Số lượng:" = 249 | 996,000,000 | H | Thành tiền, "Tổng cộng" 996,000,000 ₫ (2 dấu phân cách) | TC-CART-104 |
| LB | Bàn phím cơ Keychron Q1, "Số lượng:" = 250 | 1,000,000,000 | H | Thành tiền, "Tổng cộng" 1,000,000,000 ₫ (3 dấu phân cách) | TC-CART-105 |
| LB+ (trên biên) | MacBook Pro M3, "Số lượng:" = 23 | 1,035,000,000 | H | 1,035,000,000 ₫ | TC-CART-12 (đã có) |

Không có điểm đúng 999,999,999: Giá trong dữ liệu mẫu đều là bội của 1,000,000, nên tích gần nhất dưới biên với Keychron là 996,000,000. Phân vùng không có lớp KH (mọi độ lớn đều hợp lệ); biên này kiểm định dạng và giá trị khi số tiền thêm một nhóm phân cách.

## 4. Chi tiết test case mới

| # | Test case | Tiền điều kiện | Bước | Yêu cầu |
|---|---|---|---|---|
| 1 | TC-CART-100 | Giỏ trống | Trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 0, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | FR07-R27, FR07-R33 |
| 2 | TC-CART-101 | Giỏ trống | Trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 2, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | FR07-R27, FR07-R14, FR07-R33 |
| 3 | TC-CART-102 | Giỏ trống; token hợp lệ | `POST /api/cart`, body cơ sở với `quantity` = -1; `GET /api/cart` | FR07-R29 |
| 4 | TC-CART-103 | Giỏ trống | Trang chi tiết Bàn phím cơ Keychron Q1, nhập "Số lượng:" = 1000, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | FR07-R20, FR07-R27 |
| 5 | TC-CART-104 | Giỏ trống | Trang chi tiết Bàn phím cơ Keychron Q1, nhập "Số lượng:" = 249, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | FR07-R14, FR07-R20 |
| 6 | TC-CART-105 | Giỏ trống | Như TC-CART-104 với "Số lượng:" = 250 | FR07-R14, FR07-R20 |

Thứ tự chạy: TC-CART-100, 101, 103, 104, 105 chạy cuối nhóm giao diện của `03_tc.md` (bước 2), giỏ trống trước mỗi test case. TC-CART-102 chạy trong nhóm API không hợp lệ (bước 3).

## 5. Tổng hợp

| Phân vùng | Test case mới | Dùng lại |
|---|---|---|
| P1 | TC-CART-100, TC-CART-101, TC-CART-102, TC-CART-103 | TC-CART-01, TC-CART-31 |
| P2 | | TC-CART-05, TC-CART-06 |
| P3 | | TC-CART-01, TC-CART-02, TC-CART-10 |
| P4 | TC-CART-104, TC-CART-105 | TC-CART-12 |

Mới: 6 (5 giao diện, 1 API). Cả bộ: 32 + 6 = 38 test case.

Truy vết: FR07-R27 thành Đủ (TC-CART-100 kiểm giá trị không hợp lệ qua giao diện). Yêu cầu không có test case BVA mới: Các yêu cầu không có phân vùng có thứ tự (tên cột, dialog, đường dẫn, token).

## 6. Quyết định của sinh viên

| # | Vấn đề | Quyết định |
|---|---|---|
| 1 | Số âm cho P1 | (a) Thêm -1 qua API (TC-CART-102) |
| 2 | Thăm dò giá trị lớn cho P1 | (a) 1000 qua giao diện (TC-CART-103) |
| 3 | Biên 1 tỷ của P4 | (a) Đúng biên bằng Bàn phím cơ Keychron Q1 × 249 và × 250 (TC-CART-104, 105), thay cho điểm 990,000,000 đã hẹn ở `03_tc.md` mục 14 |
| 4 | Số dòng lớn cho P3 | (a) Không thăm dò |

## 7. Trả lời câu hỏi khi review

Không có câu hỏi của sinh viên ở lượt này.

## 8. Kiểm tra mâu thuẫn

| Quyết định hoặc câu hỏi | Kết quả kiểm tra |
|---|---|
| 3 và `03_tc.md` mục 14 | Đã xử lý: Điểm 990,000,000 (MacBook Pro M3 × 22) được thay bằng 996,000,000 và 1,000,000,000; `03_tc.md` giữ nguyên, thay đổi ghi tại đây |
| 2 và A05 | Thống nhất: Không có cận trên nên dùng điểm thăm dò, không có điểm giữa |
| TC-CART-100 và `02_ec.md` quyết định 2 | Thống nhất: Giá trị 0 chạy qua giao diện ở S4 như đã hẹn |

## 9. Ghi chú cho bước sau

- S5: Gộp `03_tc.md` và bản này; cả bộ 38 test case. FR07-R27 thành Đủ nhờ TC-CART-100.
- S6: Ghi số ô "Số lượng:" thực sự nhận ở TC-CART-103; nếu ô có giới hạn N, xét bổ sung N-1, N, N+1. Ghi trình duyệt cho TC-CART-100, 101, 103 đến 105.

## 10. Thay đổi so với bản AI (`ai_raw/S4_bva.md`)

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 6 bản AI, điểm 1 đến 4 | Chốt phương án (a) đã áp ở bản AI | Quyết định của SV | Sinh viên chấp nhận cả 4 điểm |
