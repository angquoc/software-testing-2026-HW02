# S5: Bộ test case cuối cùng (FR-07 Giỏ hàng)

- Bước: S5 (Review lần cuối, bổ sung test case AI bỏ sót). Bản này do AI gộp `03_tc.md` và `04_bva.md`; sinh viên review và bổ sung ngay trong `05_final_tc.md`
- Thời gian tạo: 2026-10-21 06:55 (UTC+07:00)
- Bản này: Bản review của S5. Bản gốc của AI: `ai_raw/S5_final_test_cases.md`
- Cập nhật lần 1: 2026-10-21 06:57 (UTC+07:00). Sinh viên không bổ sung test case nào; chốt S5 (mục 13)
- Căn cứ: `03_tc.md` (bản review S3, 32 test case), `04_bva.md` (bản review S4, 6 test case mới), `ai_raw/S3_test_cases.md` và `ai_raw/S4_bva.md` (để xác định nguồn gốc), `01_io.md` (OUT15, FR07-R33), `02_ec.md` (lớp, giả định), `00_spec.md` (yêu cầu); cấu trúc theo `A_FR-01_DangKy/05_final_tc.md` và `C_FR-17_QuanLyCoupon/05_final_tc.md` (sinh viên cho phép tham khảo)

---

## 1. Cách gộp và quy ước

### 1.1 Nguồn gốc

| Giá trị | Nghĩa | Ứng với trường `origin` của skill `test-case-writing` |
|---|---|---|
| AI | Test case có trong bản AI (`ai_raw/S3_test_cases.md` hoặc `ai_raw/S4_bva.md`) và giữ nguyên nội dung. Chỉ đổi cách viết tiêu đề theo mẫu "Kiểm tra ..." vẫn tính là AI | `AI` |
| AI có SV sửa | Test case có trong bản AI nhưng đã đổi giá trị kiểm, kết quả mong đợi, bước, hoặc ghi chú giới hạn; hoặc test case mới do AI (phiên này hay phiên khác) đề xuất khi review | `Both` |
| SV thêm | Test case mới do sinh viên phát hiện thiếu khi review, hoặc sinh viên tự viết ở S5 | `Human` |

Cột **"Phát hiện"** ghi ai phát hiện điều gì dẫn tới test case đó, kể cả khi nguồn gốc vẫn là "AI":

| Ghi | Nghĩa |
|---|---|
| AI | Không có thay đổi hay bổ sung nào khi review; test case và lớp, Output nó phủ đều có trong bản AI |
| SV: ... | Sinh viên phát hiện, ghi bước và số câu hỏi hoặc quyết định |
| AI bổ sung ... | AI ở phiên thiết kế tự bổ sung khi viết bản review |
| Claude phiên điều phối `305c705a` | Một phiên AI khác phát hiện khi soát lại, sinh viên chuyển sang |

Một test case có thể có nhiều người phát hiện; các phần cách nhau bằng dấu chấm. Chi tiết ở mục 9.

### 1.2 Ký hiệu và kết quả mong đợi

- Mã test case giữ như `03_tc.md` và `04_bva.md`. Mã yêu cầu viết tắt `Rnn` thay cho `FR07-Rnn` trong các bảng test case.
- Kết quả mong đợi viết theo chữ của đặc tả: "Đơn giá", "Tổng cộng", "Tiếp tục mua sắm" (giao diện hiện là "Giá", "Tổng tạm tính", "← Mua tiếp", D01, D03, D04).

| Mã | Kết quả mong đợi |
|---|---|
| OUT15 | Sau khi bấm nút thêm vào giỏ: Có toast hoặc badge của link "Giỏ hàng" cập nhật (R33). Không ghi câu chữ vì đặc tả không nêu |
| K1 (kiểm chứng) | Tải lại trang Giỏ hàng và gọi `GET /api/cart` bằng token của `test@eshop.com`; cả hai cho cùng kết quả như cột "Kết quả mong đợi" |
| KQ-KH-API | Không trả về phản hồi thành công (ghi mã HTTP và body thực tế ở S6); `GET /api/cart` bằng token hợp lệ cho thấy giỏ không đổi (A25) |
| Giỏ trống (OUT9) | Có hình minh họa (ảnh hoặc biểu tượng, không chỉ có chữ) và thông báo nói rõ giỏ đang trống (A20); không còn bảng |
| Trang chủ (OUT10) | Đường dẫn `localhost:5173`, trang "Danh sách sản phẩm" |

Giả định đã chốt dùng trong kết quả mong đợi: `02_ec.md` mục 2 (A01 đến A31). Kết quả khác **giả định** (không phải khác đặc tả) ghi "Khác giả định" kèm mã giả định, xét ở S7 trước khi coi là bug.

### 1.3 Tiền điều kiện chung

- Dữ liệu EShop đã reset về dữ liệu mẫu.
- Giao diện: Chrome, đăng nhập `http://localhost:5173` bằng `test@eshop.com` / `Test1234!`; ghi phiên bản Chrome ở S6. Giỏ ban đầu trống.
- API: Base URL `http://localhost:3000`; token lấy bằng `POST /api/login`; header `Content-Type: application/json`, `Authorization: Bearer <token>`.

### 1.4 Giá trị cơ sở

| Input | Giá trị |
|---|---|
| Sản phẩm | iPhone 15 Pro Max (`id` = 1), Đơn giá 30,000,000 |
| Sản phẩm thứ hai | Samsung Galaxy S24 Ultra, Đơn giá 28,000,000 |
| Số lượng thêm | 1 |
| Token | Token của `test@eshop.com` |

Body API cơ sở:

```json
{"id": 1, "name": "iPhone 15 Pro Max", "price": 30000000, "quantity": 1}
```

---

## 2. Tổng hợp

| Nhóm | Mã | Số TC | AI | AI có SV sửa | SV thêm | Có phần do SV phát hiện | Có phần do phiên điều phối phát hiện |
|---|---|---|---|---|---|---|---|
| TS-01 Giỏ hàng hợp lệ qua giao diện (EP) | TC-CART-01 đến TC-CART-12 | 12 | 12 | 0 | 0 | 0 | 2 |
| TS-02 API không hợp lệ (EP) | TC-CART-30 đến TC-CART-36 | 7 | 7 | 0 | 0 | 0 | 0 |
| TS-03 API hợp lệ (EP) | TC-CART-50, TC-CART-51, TC-CART-54 | 3 | 3 | 0 | 0 | 0 | 0 |
| TS-04 Bảo mật (API và giao diện) | TC-CART-52, TC-CART-53 | 2 | 2 | 0 | 0 | 0 | 0 |
| TS-05 Giá trị biên (BVA) | TC-CART-100 đến TC-CART-105 | 6 | 6 | 0 | 0 | 0 | 2 |
| TS-06 Checklist giao diện | TC-CART-90 đến TC-CART-97 | 8 | 8 | 0 | 0 | 0 | 0 |
| **Tổng** | | **38** | **38** | **0** | **0** | **0** | **4** |

Cột cuối đếm test case mà cột "Phát hiện" có phần ghi phiên điều phối: TC-CART-01, TC-CART-02, TC-CART-100, TC-CART-101 kiểm OUT15 (FR07-R33, A31), Output bổ sung khi review S1 (mục 9.2). Các test case này vẫn mang nguồn gốc "AI" vì đã có trong bản AI của S3, S4.

Theo kỹ thuật: 32 test case Domain Testing (EP) và checklist từ S3, 6 test case BVA từ S4; S4 dùng lại thêm 7 test case của S3 làm điểm biên. Dự kiến Blocked: 3 (TC-CART-04 đến TC-CART-06, do D02).

---

## 3. TS-01: Giỏ hàng hợp lệ qua giao diện (EP)

| TC | Tiêu đề | Lớp | Yêu cầu | Tiền điều kiện | Bước và dữ liệu | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|---|
| TC-CART-01 | Kiểm tra thêm sản phẩm chưa có vào giỏ trống từ trang chi tiết | EC01, EC03, EC09, EC25, EC27, EC29 | R01 đến R03, R06, R07, R14, R33 | Giỏ trống | Mở trang chi tiết iPhone 15 Pro Max, giữ "Số lượng:" = 1, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | OUT15. 1 dòng "iPhone 15 Pro Max": Đơn giá 30,000,000 ₫, Số lượng 1, Thành tiền 30,000,000 ₫; "Tổng cộng" 30,000,000 ₫. K1 | AI | Claude phiên điều phối `305c705a`: OUT15 (review S1) |
| TC-CART-02 | Kiểm tra thêm sản phẩm chưa có từ trang chủ khi giỏ đã có 1 dòng | EC08, EC26, EC27 | R14, R24, R33 | Giỏ có iPhone 15 Pro Max × 1 | Ở trang chủ, bấm "Thêm vào giỏ" của Samsung Galaxy S24 Ultra; mở trang Giỏ hàng | OUT15. 2 dòng; Samsung: Số lượng 1, Thành tiền 28,000,000 ₫; "Tổng cộng" 58,000,000 ₫; badge 2 (A17). K1 | AI | Claude phiên điều phối `305c705a`: OUT15 (review S1) |
| TC-CART-03 | Kiểm tra thêm lại sản phẩm đã có trong giỏ từ trang chi tiết với số lượng 3 | EC03, EC09, EC28 | R08, R09, R24, R27 | Giỏ có iPhone 15 Pro Max × 1, Samsung Galaxy S24 Ultra × 1 | Mở trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 3, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | Vẫn 2 dòng. iPhone: Số lượng 4, Thành tiền 120,000,000 ₫; "Tổng cộng" 148,000,000 ₫; badge 5 (A08, A17). K1 | AI | AI |
| TC-CART-04 | Kiểm tra tăng số lượng bằng nút tăng | EC11 | R04, R06, R14 | Giỏ có iPhone 15 Pro Max × 1 | Bấm nút tăng ở dòng iPhone | Số lượng 2; Thành tiền 60,000,000 ₫; "Tổng cộng" 60,000,000 ₫ (A07). Dự kiến Blocked (GH2) | AI | AI |
| TC-CART-05 | Kiểm tra giảm số lượng bằng nút giảm khi số lượng là 2 | EC12 | R05, R06, R14 | Giỏ có iPhone 15 Pro Max × 2 (thêm từ trang chi tiết với "Số lượng:" = 2) | Bấm nút giảm ở dòng iPhone | Số lượng 1; Thành tiền 30,000,000 ₫; "Tổng cộng" 30,000,000 ₫. Dự kiến Blocked (GH2) | AI | AI |
| TC-CART-06 | Kiểm tra giảm số lượng khi số lượng là 1 | EC13 | R05, R11 | Giỏ có iPhone 15 Pro Max × 1 | Bấm nút giảm ở dòng iPhone | Số lượng không nhỏ hơn 1; nếu dòng bị xóa thì phải có dialog xác nhận trước (A04). Dự kiến Blocked (GH2) | AI | AI |
| TC-CART-07 | Kiểm tra hủy dialog xóa sản phẩm | EC15, EC26 | R10, R11 | Giỏ có iPhone 15 Pro Max × 1, Samsung Galaxy S24 Ultra × 1 | Bấm "Xóa" ở dòng Samsung; quan sát; bấm nút hủy (hoặc đóng) dialog | Dialog hiện ra; khi dialog mở, dòng Samsung vẫn còn. Sau khi hủy: Vẫn 2 dòng, "Tổng cộng" 58,000,000 ₫ (A10). K1 | AI | AI |
| TC-CART-08 | Kiểm tra xác nhận xóa một dòng trong giỏ 2 dòng | EC14, EC26 | R10, R11, R14 | Như TC-CART-07 | Bấm "Xóa" ở dòng Samsung, bấm nút xác nhận; sau đó ở trang chủ bấm "Thêm vào giỏ" của Samsung | Sau xác nhận: Còn 1 dòng iPhone, "Tổng cộng" 30,000,000 ₫. K1: Không còn Samsung. Thêm lại: Samsung là dòng mới, Số lượng 1 | AI | AI |
| TC-CART-09 | Kiểm tra xóa dòng cuối cùng | EC14, EC25 | R11, R15, R16 | Giỏ có iPhone 15 Pro Max × 1 | Bấm "Xóa", bấm nút xác nhận | Dialog hiện trước khi xóa. Sau xác nhận: Hiện ngay trạng thái giỏ trống (OUT9, A11) | AI | AI |
| TC-CART-10 | Kiểm tra giỏ trống và nút Tiếp tục mua sắm | EC24 | R12, R13, R15, R16, R24 | Giỏ trống | Mở trang Giỏ hàng; bấm "Tiếp tục mua sắm" | Trạng thái giỏ trống (OUT9); badge ẩn hoặc 0 (A18). Sau khi bấm: Trang chủ (OUT10) | AI | AI |
| TC-CART-11 | Kiểm tra nút Tiếp tục mua sắm khi giỏ có hàng | EC25 | R12, R13 | Giỏ có iPhone 15 Pro Max × 1 | Bấm "Tiếp tục mua sắm" (nếu không có thì ghi nhận, và bấm nút quay về đang có "← Mua tiếp" để kiểm R13); mở lại trang Giỏ hàng | Trang chủ (OUT10). Giỏ vẫn 1 dòng iPhone × 1 | AI | AI |
| TC-CART-12 | Kiểm tra Thành tiền và Tổng cộng từ 1 tỷ | EC09, EC30 | R14, R20 | Giỏ trống | Mở trang chi tiết MacBook Pro M3, nhập "Số lượng:" = 23, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | Số lượng 23; Thành tiền 1,035,000,000 ₫; "Tổng cộng" 1,035,000,000 ₫ (A01, A02) | AI | AI |

---

## 4. TS-02: API không hợp lệ (EP)

Tiền điều kiện chung của nhóm: Giỏ của `test@eshop.com` trống; token hợp lệ. Mỗi test case chỉ một lớp không hợp lệ; các trường khác lấy body cơ sở.

| TC | Tiêu đề | Lớp | Yêu cầu | Bước và dữ liệu | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|
| TC-CART-30 | Kiểm tra thêm vào giỏ bị từ chối khi sản phẩm không tồn tại | EC02 | R29 | Kiểm `GET /api/products/9999` không trả về sản phẩm; `POST /api/cart` với `id` = 9999 | ERR3: KQ-KH-API (A24) | AI | AI |
| TC-CART-31 | Kiểm tra thêm vào giỏ bị từ chối khi số lượng là 0 | EC04 | R27, R29 | `POST /api/cart` với `quantity` = 0 | ERR2: KQ-KH-API | AI | AI |
| TC-CART-32 | Kiểm tra thêm vào giỏ bị từ chối khi số lượng là số thập phân | EC05 | R27, R29 | `POST /api/cart` với `quantity` = 1.5 | ERR2: KQ-KH-API | AI | AI |
| TC-CART-33 | Kiểm tra thêm vào giỏ bị từ chối khi số lượng không phải số | EC06 | R29 | `POST /api/cart` với `quantity` = `"abc"` | ERR2: KQ-KH-API | AI | AI |
| TC-CART-34 | Kiểm tra thêm vào giỏ bị từ chối khi thiếu trường quantity | EC07 | R29 | `POST /api/cart`, bỏ trường `quantity` | ERR3: KQ-KH-API | AI | AI |
| TC-CART-35 | Kiểm tra thêm vào giỏ bị từ chối khi thiếu header Authorization | EC22 | R30 | `POST /api/cart` body cơ sở, không gửi header `Authorization` | ERR1: KQ-KH-API | AI | AI |
| TC-CART-36 | Kiểm tra xem giỏ bị từ chối khi token sai | EC23 | R28, R30 | 1. `POST /api/cart` body cơ sở với token hợp lệ. 2. `GET /api/cart` với token bị sửa một ký tự | ERR1: Bước 2 không trả về phản hồi thành công, không có dữ liệu giỏ (ngoại lệ của KQ-KH-API: Giỏ có 1 dòng do bước 1) | AI | AI |

---

## 5. TS-03: API hợp lệ (EP)

Tiền điều kiện chung của nhóm: Giỏ của `test@eshop.com` trống; token hợp lệ.

| TC | Tiêu đề | Lớp | Yêu cầu | Bước và dữ liệu | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|
| TC-CART-50 | Kiểm tra thêm và xem giỏ qua API với dữ liệu cơ sở | EC10, EC16, EC19, EC21, EC27, EC31 | R28, R29 | `POST /api/cart` body cơ sở; `GET /api/cart` | `POST` thành công. `GET` có 1 dòng `id` 1, số lượng 1. Trang Giỏ hàng hiển thị như TC-CART-01 | AI | AI |
| TC-CART-51 | Kiểm tra giỏ dùng giá trong CSDL khi client gửi price khác | EC20 | R29 | `POST /api/cart` với `price` = 1 | Không có dòng nào có Đơn giá 1 ₫. Nếu thêm thành công: Đơn giá 30,000,000 ₫, Thành tiền 30,000,000 ₫ (A24) | AI | AI |
| TC-CART-54 | Kiểm tra người dùng khác không thấy giỏ của test | EC32 | R28, R30 | 1. `POST /api/cart` body cơ sở với token của `test@eshop.com`. 2. Lấy token `admin@eshop.com`, gọi `GET /api/cart` | Bước 2 không có dòng `id` 1 mà bước 1 đã thêm (A16) | AI | AI |

---

## 6. TS-04: Bảo mật (API và giao diện)

**TC-CART-53 chạy cuối cùng trong đợt test và reset dữ liệu ngay sau đó** (mục 10).

| TC | Tiêu đề | Lớp | Yêu cầu | Bước và dữ liệu | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|
| TC-CART-52 | Kiểm tra tên sản phẩm có thẻ HTML không bị render trên trang Giỏ hàng | EC17 | R31 | `POST /api/cart` với `name` = `<b>X</b>`; mở trang Giỏ hàng | Tên hiển thị là chuỗi `<b>X</b>` nguyên văn hoặc tên trong CSDL; không có chữ "X" in đậm (A24) | AI | AI |
| TC-CART-53 | Kiểm tra tên sản phẩm có ký tự SQL không làm sai giỏ | EC18 | R32 | `POST /api/cart` với `name` = `X' OR '1'='1`; `GET /api/cart` | `POST` không trả về lỗi hệ thống; `GET` trả về đúng 1 dòng `id` 1, số lượng 1, không có dòng lạ. Giới hạn GH4 | AI | AI |

---

## 7. TS-05: Giá trị biên (BVA)

Phân vùng ở `04_bva.md` mục 2. Bảng dưới chỉ gồm test case mới của S4; điểm biên dùng lại test case của S3 ở cuối mục.

| TC | Tiêu đề | Phân vùng, điểm | Yêu cầu | Tiền điều kiện | Bước và dữ liệu | Kết quả mong đợi | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|---|
| TC-CART-100 | Kiểm tra thêm vào giỏ bị từ chối khi nhập số lượng 0 ở trang chi tiết | P1, LB-1 qua giao diện | R27, R33 | Giỏ trống | Trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 0, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | ERR2: Giỏ vẫn trống; không có toast thành công, badge không đổi (A31). Giới hạn GH3 | AI | Claude phiên điều phối `305c705a`: OUT15 (review S1). AI bổ sung A31 (S2) |
| TC-CART-101 | Kiểm tra thêm vào giỏ với số lượng 2 từ trang chi tiết | P1, LB+1 | R14, R27, R33 | Giỏ trống | Trang chi tiết iPhone 15 Pro Max, nhập "Số lượng:" = 2, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | OUT15. 1 dòng, Số lượng 2, Thành tiền 60,000,000 ₫, "Tổng cộng" 60,000,000 ₫. Giới hạn GH3 | AI | Claude phiên điều phối `305c705a`: OUT15 (review S1) |
| TC-CART-102 | Kiểm tra thêm vào giỏ qua API bị từ chối khi số lượng âm | P1, số âm qua API | R29 | Giỏ trống; token hợp lệ | `POST /api/cart` với `quantity` = -1 | ERR2: KQ-KH-API | AI | AI |
| TC-CART-103 | Kiểm tra thêm vào giỏ với số lượng lớn 1000 | P1, thăm dò giá trị lớn | R20, R27 | Giỏ trống | Trang chi tiết Bàn phím cơ Keychron Q1, nhập "Số lượng:" = 1000, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | Số lượng 1000, Thành tiền 4,000,000,000 ₫, "Tổng cộng" 4,000,000,000 ₫. Ghi số ô thực sự nhận (GH7) | AI | AI |
| TC-CART-104 | Kiểm tra định dạng tiền ngay dưới 1 tỷ | P4, LB-1 (gần nhất tạo được) | R14, R20 | Giỏ trống | Trang chi tiết Bàn phím cơ Keychron Q1, nhập "Số lượng:" = 249, bấm "Thêm vào giỏ hàng"; mở trang Giỏ hàng | Thành tiền, "Tổng cộng" 996,000,000 ₫ (2 dấu phân cách) | AI | AI |
| TC-CART-105 | Kiểm tra định dạng tiền đúng 1 tỷ | P4, LB | R14, R20 | Giỏ trống | Như TC-CART-104 với "Số lượng:" = 250 | Thành tiền, "Tổng cộng" 1,000,000,000 ₫ (3 dấu phân cách) | AI | AI |

Điểm biên dùng lại test case của S3: P1 LB = 1 (TC-CART-01), P1 LB-1 qua API = 0 (TC-CART-31); P2 LB = 1 (TC-CART-06), LB+1 = 2 (TC-CART-05); P3 0, 1, 2 dòng (TC-CART-10, TC-CART-01, TC-CART-02); P4 trên biên 1,035,000,000 (TC-CART-12).

---

## 8. TS-06: Checklist giao diện

| TC | Tiêu đề | Yêu cầu | Điểm kiểm tra | Kết quả mong đợi | Cách kiểm tra | Nguồn gốc | Phát hiện |
|---|---|---|---|---|---|---|---|
| TC-CART-90 | Kiểm tra bảng giỏ hàng có đủ cột, nút xóa và nhãn Tổng cộng | R01, R02, R03, R06, R07, R10, R14 | Bảng khi giỏ có 2 dòng | Cột "Sản phẩm", "Đơn giá", "Số lượng", "Thành tiền", "Thao tác"; mỗi dòng có nút xóa; nhãn tổng chính xác "Tổng cộng" | Quan sát (liên quan D01, D04) | AI | AI |
| TC-CART-91 | Kiểm tra giỏ trống có hình minh họa, thông báo và nút Tiếp tục mua sắm | R12, R15, R16 | Trang Giỏ hàng khi trống | Có hình minh họa, thông báo nói rõ giỏ trống (A20), có "Tiếp tục mua sắm" (liên kết cũng đạt, A30) | Quan sát (liên quan D05) | AI | AI |
| TC-CART-92 | Kiểm tra ngôn ngữ của trang Giỏ hàng và tiêu đề tab | R17 | Mọi chữ trên trang, khi có hàng và khi trống, gồm tiêu đề tab | Toàn bộ tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn | Quan sát (liên quan D10) | AI | AI |
| TC-CART-93 | Kiểm tra màu nút tích cực và nút nguy hiểm | R18, R19 | "Tiến hành thanh toán", "Xóa", nút xác nhận trong dialog xóa | "Tiến hành thanh toán" màu xanh dương; "Xóa" và nút xác nhận xóa màu đỏ (A22) | Quan sát; mở dialog xóa rồi hủy (liên quan D09) | AI | AI |
| TC-CART-94 | Kiểm tra định dạng tiền | R20 | Đơn giá, Thành tiền, Tổng cộng | Ký tự `₫` và phân cách hàng nghìn | Sao chép giá trị, dán vào trình soạn thảo để xác định ký tự `₫` (Q29) | AI | AI |
| TC-CART-95 | Kiểm tra navbar highlight mục Giỏ hàng và có breadcrumb | R23, R25 | Navbar và phần đầu trang khi đang ở trang Giỏ hàng | Mục "Giỏ hàng" được highlight; có breadcrumb | Quan sát (liên quan D06, D08) | AI | AI |
| TC-CART-96 | Kiểm tra trang Giỏ hàng có đúng 1 thẻ h1 và ảnh có alt | R21, R26 | Số thẻ `<h1>`; thuộc tính `alt` của ảnh sản phẩm | Đúng 1 thẻ `<h1>`; nếu có ảnh sản phẩm thì `alt` không rỗng | DevTools ở S6. Giới hạn GH8 | AI | AI |
| TC-CART-97 | Kiểm tra thứ tự focus khi nhấn Tab | R22 | Nhấn Tab từ đầu trang khi giỏ có hàng | Focus đi từ trên xuống dưới, trái sang phải | Nhấn Tab | AI | AI |

---

## 9. Nguồn gốc chi tiết

### 9.1 Test case không phải "AI"

Không có. Ở S3, S4, sinh viên chấp nhận toàn bộ các phương án AI đề xuất, không đổi nội dung test case nào (`03_tc.md` mục 15, `04_bva.md` mục 10).

### 9.2 Test case "AI" có Output do phiên khác bổ sung ở S1

Các test case dưới đây giữ nguyên bản AI (nên nguồn gốc là "AI"), nhưng Output mà chúng kiểm không có trong bản AI của S1; Output được thêm khi review S1 (`01_io.md` cập nhật lần 1). Ghi lại để phần gap analysis (S8) thấy đầy đủ.

| Output hoặc giả định | Thêm khi review S1 do | Test case phủ |
|---|---|---|
| OUT15, FR07-R33 (phản hồi trực quan sau khi bấm thêm vào giỏ) | Claude phiên điều phối `305c705a` phát hiện; sinh viên chuyển sang | TC-CART-01, TC-CART-02, TC-CART-101 |
| A31 (thêm bị từ chối thì không hiện phản hồi thành công), phát sinh từ OUT15 | AI bổ sung khi viết bản AI của S2 | TC-CART-100 |

### 9.3 Test case đã bỏ (không có trong bộ cuối)

Không có test case nào bị bỏ. Điểm 990,000,000 (MacBook Pro M3 × 22) hẹn ở `03_tc.md` mục 14 không thành test case; S4 thay bằng TC-CART-104, TC-CART-105 (`04_bva.md` quyết định 3).

---

## 10. Thứ tự chạy

1. Reset dữ liệu EShop về dữ liệu mẫu; đăng nhập `test@eshop.com`.
2. Giao diện, theo chuỗi trạng thái giỏ: TC-CART-10, 91 (giỏ trống); 01; 11; 02; 90, 92 đến 97; 07; 03; 08; 09; 04, 06 (thêm iPhone × 1 trước); 05 (giỏ iPhone × 2); 12; 100, 101, 103, 104, 105. Trước mỗi test case, đưa giỏ về đúng tiền điều kiện bằng "Xóa" hoặc reset.
3. Reset dữ liệu. API không hợp lệ: TC-CART-30 đến 35, 102 (giỏ trống trước mỗi test case), rồi 36.
4. Reset dữ liệu. API hợp lệ và bảo mật: TC-CART-50, 51, 54, 52; chạy TC-CART-53 cuối cùng.
5. Reset dữ liệu ngay sau TC-CART-53. Nếu kết quả bất thường, ghi kết quả rồi reset trước khi chạy lại bất kỳ test case nào.

---

## 11. Giới hạn quan sát

| Mã | Giới hạn | Test case |
|---|---|---|
| GH1 | Kiểm chứng bằng tải lại trang phụ thuộc việc giỏ có được giữ khi tải lại không (Q14); nếu giỏ mất thì ghi nhận và dựa vào `GET /api/cart` | TC-CART-01, 02, 03, 07, 08 |
| GH2 | Giao diện không có nút +/- (D02) và API spec không mô tả API đổi số lượng; dự kiến Blocked | TC-CART-04 đến TC-CART-06 |
| GH3 | Giá trị nhập ở ô "Số lượng:" đi qua trình duyệt trước khi tới hệ thống; kết quả phản ánh cả trình duyệt và EShop. Ghi trình duyệt ở S6 | TC-CART-03, 12, 100, 101, 103 đến 105 |
| GH4 | FR07-R32 (Parameterized Query) chỉ quan sát gián tiếp qua hành vi | TC-CART-53 |
| GH5 | Mã HTTP và câu chữ lỗi của API giỏ hàng không có trong đặc tả (A25); chỉ ghi lại ở S6 | TC-CART-30 đến 36, 102 |
| GH6 | Thêm trùng chỉ kiểm qua trang chi tiết; đường trang chủ và API không kiểm thêm trùng (`01_io.md` quyết định 10) | TC-CART-03 |
| GH7 | Giới hạn thật của ô "Số lượng:" chưa biết khi thiết kế; nếu ô chỉ nhận tối đa N, quay lại S5 bổ sung N-1, N, N+1 | TC-CART-103 |
| GH8 | Giỏ hiện không hiển thị ảnh sản phẩm (O16) nên chưa kiểm được `alt` | TC-CART-96 |

---

## 12. Ma trận truy vết yêu cầu

| Yêu cầu | Nội dung ngắn | Test case | Mức phủ |
|---|---|---|---|
| FR07-R01 | Cột "Sản phẩm" | TC-CART-01, TC-CART-90 | Đủ |
| FR07-R02 | Cột "Đơn giá" | TC-CART-01, TC-CART-90 | Đủ |
| FR07-R03 | Cột "Số lượng" | TC-CART-01, TC-CART-90 | Đủ |
| FR07-R04 | Nút tăng | TC-CART-04 | Đủ trên thiết kế; dự kiến Blocked (GH2) |
| FR07-R05 | Nút giảm | TC-CART-05, TC-CART-06 | Đủ trên thiết kế; dự kiến Blocked (GH2) |
| FR07-R06 | Cột "Thành tiền" | TC-CART-01, TC-CART-90 | Đủ |
| FR07-R07 | Cột "Thao tác" | TC-CART-01, TC-CART-90 | Đủ |
| FR07-R08 | Thêm trùng tăng số lượng | TC-CART-03 | Một phần (GH6) |
| FR07-R09 | Thêm trùng không tạo dòng mới | TC-CART-03 | Một phần (GH6) |
| FR07-R10 | Có nút xóa | TC-CART-07, TC-CART-08, TC-CART-90 | Đủ |
| FR07-R11 | Dialog xác nhận trước khi xóa | TC-CART-06 đến TC-CART-09 | Đủ |
| FR07-R12 | Có nút "Tiếp tục mua sắm" | TC-CART-10, TC-CART-11, TC-CART-91 | Đủ |
| FR07-R13 | Về trang chủ | TC-CART-10, TC-CART-11 | Đủ |
| FR07-R14 | Nhãn "Tổng cộng" | TC-CART-01 đến TC-CART-05, TC-CART-08, TC-CART-12, TC-CART-90, TC-CART-101, TC-CART-104, TC-CART-105 | Đủ |
| FR07-R15 | Giỏ trống có hình minh họa | TC-CART-09, TC-CART-10, TC-CART-91 | Đủ |
| FR07-R16 | Giỏ trống có thông báo | TC-CART-09, TC-CART-10, TC-CART-91 | Đủ |
| FR07-R17 | Tiếng Việt | TC-CART-92 | Đủ |
| FR07-R18 | Nút tích cực xanh dương | TC-CART-93 | Đủ |
| FR07-R19 | Nút nguy hiểm đỏ | TC-CART-93 | Đủ |
| FR07-R20 | Ký hiệu `₫`, phân cách hàng nghìn | TC-CART-12, TC-CART-94, TC-CART-103 đến TC-CART-105 | Đủ |
| FR07-R21 | Đúng 1 thẻ `<h1>` | TC-CART-96 | Đủ (DevTools ở S6) |
| FR07-R22 | Thứ tự Tab | TC-CART-97 | Đủ |
| FR07-R23 | Navbar highlight | TC-CART-95 | Đủ |
| FR07-R24 | Badge số lượng | TC-CART-02, TC-CART-03, TC-CART-10 | Đủ |
| FR07-R25 | Breadcrumb | TC-CART-95 | Đủ |
| FR07-R26 | `alt` của ảnh | TC-CART-96 | Một phần (GH8) |
| FR07-R27 | Số lượng nguyên dương, tối thiểu 1 | TC-CART-03, TC-CART-31, TC-CART-32, TC-CART-100, TC-CART-101, TC-CART-103 | Đủ |
| FR07-R28 | `GET /api/cart` | TC-CART-36, TC-CART-50, TC-CART-54 | Đủ |
| FR07-R29 | `POST /api/cart` | TC-CART-30 đến TC-CART-34, TC-CART-50, TC-CART-51, TC-CART-102 | Đủ |
| FR07-R30 | API yêu cầu token | TC-CART-35, TC-CART-36, TC-CART-54 | Đủ |
| FR07-R31 | Escape tên sản phẩm | TC-CART-52 | Đủ |
| FR07-R32 | Parameterized Query | TC-CART-53 | Một phần (GH4) |
| FR07-R33 | Phản hồi trực quan sau khi thêm vào giỏ | TC-CART-01, TC-CART-02, TC-CART-100, TC-CART-101 | Đủ |

---

## 13. Phần sinh viên bổ sung ở S5

Sinh viên không bổ sung test case nào ở S5.

Bộ test case cuối cùng của FR-07 gồm 38 test case như mục 2. Phần do người khác ngoài AI phiên thiết kế phát hiện đã được đưa vào trong quá trình review S1 (cột "Phát hiện", mục 9.2).

S5 đã chốt ngày 2026-10-21.

---

## 14. Thay đổi so với bản AI (`ai_raw/S5_final_test_cases.md`)

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 13 | Thay dòng chờ sinh viên bổ sung bằng ghi nhận: Sinh viên không bổ sung test case nào ở S5; chốt S5 | Quyết định của SV | Sinh viên review bộ test case cuối cùng |
