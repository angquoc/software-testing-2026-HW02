# S8: AI gap analysis (FR-17 Quản lý mã giảm giá)

- Bước: S8 (Phân tích những gì AI bỏ sót và vì sao, đề mục 6.3)
- Thời gian tạo: 2026-10-21 03:26 (UTC+07:00)
- Bản gốc của AI: `ai_raw/S8_gap_analysis.md`. `08_gap_analysis.md` lúc tạo giống hệt bản này; sinh viên review trực tiếp trên `08_gap_analysis.md`
- Căn cứ: Bảng "Thay đổi so với bản AI" của `01_io.md` (S1), `02_ec.md` (S2), `03_tc.md` (S3), `04_bva.md` (S4), `05_final_tc.md` (S5); `05_final_tc.md` mục 2, 9.1, 9.2, 13; `06_results.md` (S6); `bugs/bug_report.md` mục FR-17 (S7); `ai_raw/S3_test_cases.md`, `ai_raw/S4_bva.md` (để biết test case nào có trong bản AI gốc)
- Ba nguyên nhân dùng để phân loại (theo đề mục 6.3): **Chất lượng input/prompt** (AI không có hoặc không được đưa thông tin cần thiết), **Giới hạn của công cụ AI** (thông tin có sẵn nhưng AI suy luận thiếu hoặc sai), **Độ phức tạp của feature** (nhiều giả định, đường thực thi, tham chiếu chéo chồng lên nhau)

---

## 1. Thống kê các bảng "Thay đổi so với bản AI" (S1 đến S5)

S0 làm theo quy trình cũ, không có bản AI (`ai_raw/S0_khao_sat.md`), nên không có bảng thay đổi để đếm.

### 1.1 Theo Loại

| Bước | File | Sai | Thiếu | Thừa | Mơ hồ | Quyết định của SV | Tổng |
|---|---|---|---|---|---|---|---|
| S1 | `01_io.md` mục 13 | 0 | 9 | 0 | 1 | 10 | 20 |
| S2 | `02_ec.md` mục 11 | 0 | 4 | 0 | 1 | 24 | 29 |
| S3 | `03_tc.md` mục 17 | 0 | 5 | 0 | 2 | 5 | 12 |
| S4 | `04_bva.md` mục 13 | 0 | 3 | 0 | 0 | 4 | 7 |
| S5 | `05_final_tc.md` mục 14 | 1 | 2 | 0 | 1 | 0 | 4 |
| **Tổng** | | **1** | **23** | **0** | **5** | **43** | **72** |

43 trên 72 dòng (60%) là quyết định của sinh viên khi chọn giữa các phương án AI đưa ra, chủ yếu ở S2 (24 giả định). 29 dòng còn lại (Sai, Thiếu, Mơ hồ) là chỗ bản AI chưa đúng hoặc chưa đủ.

### 1.2 Theo người phát hiện (29 dòng Sai, Thiếu, Mơ hồ)

Người phát hiện lấy từ cột "Lý do hoặc căn cứ" của từng dòng.

| Bước | Sinh viên | AI tự phát hiện khi review | Phiên điều phối (`305c705a`) | Tổng |
|---|---|---|---|---|
| S1 | 8 | 2 | 0 | 10 |
| S2 | 0 | 5 | 0 | 5 |
| S3 | 0 | 7 | 0 | 7 |
| S4 | 0 | 1 | 2 | 3 |
| S5 | 4 | 0 | 0 | 4 |
| **Tổng** | **12** | **15** | **2** | **29** |

Ghi chú về cách đếm:

- S4, dòng "Mục 6" (giới hạn quan sát) có hai người phát hiện: Phần số lớn do phiên điều phối, các dòng còn lại do AI bổ sung. Dòng này được đếm vào phiên điều phối vì phần chính (số lớn) dẫn tới thay đổi.
- Trong 15 dòng "AI tự phát hiện", 7 dòng là **cập nhật hệ quả** của một quyết định hay câu hỏi khác (S1: 2 dòng ghi chú cho S2; S2: Ghi chú cho S4, hệ quả của A07; S3: Ghi chú cho S4, S5; S4: Trạng thái "Khác giả định" áp chung). 8 dòng là lỗi thật AI tự bắt được khi kiểm tra mâu thuẫn hoặc viết lại: A26 (khoảng trắng gồm ký tự nào), A15 vướng A20, thứ tự EC84 và EC72, `GET` thiếu trường, dòng F của TC-CPN-82, trỏ dòng dự phòng, reset trước TC-CPN-56, yêu cầu tiếng Việt cho thông báo lỗi.
- Một dòng "Quyết định của SV" ở S1 (mã trạng thái HTTP, mục 4.1) bắt nguồn từ câu hỏi 3 của sinh viên; ban đầu ghi là Thiếu, sinh viên yêu cầu đổi vì bản AI không sai.

### 1.3 Phần bổ sung lúc gộp S5 (ngoài bảng thay đổi)

Khi yêu cầu gộp S5, sinh viên đưa thông tin "ô Mã coupon tự chuyển chữ hoa khi gõ" (quan sát lúc nhập thử ở S0, trước đó không cung cấp cho AI). Phần này đã nằm trong bản AI `ai_raw/S5_final_test_cases.md`, nên không có dòng trong bảng thay đổi của `05_final_tc.md`. Đếm theo `05_final_tc.md` mục 9.1, 13:

| Thay đổi | Số test case | Phát hiện |
|---|---|---|
| Thêm test case API cho lớp chữ thường (TC-CPN-140, 141, 142) | 3 (SV thêm) | Sinh viên |
| Thêm giới hạn GH9 cho test case giao diện nhập chữ thường (TC-CPN-06, 34, 123) | 3 (AI có SV sửa) | Sinh viên |
| Sửa kết quả mong đợi của TC-CPN-10 (`<b>` thành `<B>`) | 1 (AI có SV sửa) | Sinh viên đưa thông tin; AI nhận ra hệ quả |

### 1.4 Nguồn gốc của bộ test case cuối

Theo `05_final_tc.md` mục 2 (sau cập nhật lần 1): 115 test case, gồm 80 "AI", 30 "AI có SV sửa", 5 "SV thêm"; 28 test case có phần do sinh viên phát hiện.

## 2. Test case AI bỏ sót hoặc thiết kế sai

Mỗi dòng xếp vào một nguyên nhân chính. Căn cứ lấy từ cột "Vì sao AI bỏ sót" và "Phát hiện" của `05_final_tc.md`, hoặc từ bảng thay đổi của bước tương ứng.

### 2.1 Bỏ sót hoặc sai ở bước thiết kế (S1 đến S4)

| Test case | AI bỏ sót hoặc sai gì | Phát hiện | Nguyên nhân | Căn cứ |
|---|---|---|---|---|
| TC-CPN-53, 55, 71 (dòng C) | Bản AI S1 không có Input gián tiếp cho thao tác Xóa (trạng thái mã cần xóa: Hết hạn, đã bị xóa ở nơi khác) | Sinh viên (S1, câu 1) | Giới hạn của công cụ AI | `01_io.md` mục 13: "Bản AI chỉ ghi Q16 như ràng buộc chưa rõ của IN7, không lập trạng thái của mã cần xóa thành Input gián tiếp, trong khi step S1 yêu cầu xét trạng thái dữ liệu có sẵn". Hướng dẫn S1 có yêu cầu; AI tập trung vào các ô của form Thêm |
| TC-CPN-69, 70 | Bản AI S1 không xét dạng của cả request API (JSON sai cú pháp, thiếu `Content-Type`, body rỗng) | Sinh viên (S1, câu 2) | Giới hạn của công cụ AI | `01_io.md` mục 13: "Bản AI đã đưa đường API vào phạm vi nhưng chỉ xét giá trị trong body đọc được, bỏ sót dạng của cả request" |
| TC-CPN-73 | Bản AI S1 không có lớp header `Authorization` sai dạng | Sinh viên (S1, câu 2) | Giới hạn của công cụ AI | `01_io.md` mục 13: "API spec mục 5.2, 6 quy định dạng header...; bản AI chỉ ghi 'không gửi token', 'token không hợp lệ'" |
| TC-CPN-61 | Không có cách kiểm thay thế khi `GET` thiếu trường giá trị | AI tự phát hiện (review S3) | Độ phức tạp của feature | `03_tc.md` mục 17; giá trị lưu chỉ thấy được qua API, phụ thuộc giả định A17 |
| TC-CPN-15, 16, 20, 41, 44, 45, 82 | Trỏ "dòng tương ứng" mơ hồ; dòng F của TC-CPN-82 không khớp TC-CPN-44 | AI tự phát hiện (review S3) | Độ phức tạp của feature | `03_tc.md` mục 17; bộ test có nhiều tham chiếu chéo giữa test case giao diện và dòng dự phòng API |
| TC-CPN-56 | Không có bước reset riêng, phải xóa tay hàng chục mã | AI tự phát hiện (review S3) | Giới hạn của công cụ AI | `03_tc.md` mục 17: Bản AI xếp thứ tự chạy mà không tính số mã tích lũy |
| TC-CPN-30 đến 46 (quy ước KQ-KH-GD) | Kết quả mong đợi thiếu yêu cầu thông báo bằng tiếng Việt | AI tự phát hiện (review S3) | Giới hạn của công cụ AI | `03_tc.md` mục 17: Thuộc tính đã có ở `01_io.md` mục 4.3 nhưng không được mang sang S3 |
| TC-CPN-111, 114, 119, 131 | Chỉ chạy điểm `2^53 + 1` qua giao diện; không xét giá trị bị làm tròn trước khi gửi | Phiên điều phối `305c705a` (S4) | Giới hạn của công cụ AI | `05_final_tc.md` cột "Vì sao AI bỏ sót": "Bản AI coi kết quả qua giao diện là kết quả của hệ thống, chưa xét việc làm tròn ở trình duyệt hoặc mã của trang". AI áp quy tắc dự phòng A2 (chỉ khi bị chặn) một cách máy móc |

### 2.2 Do thông tin bị giữ lại từ S0 (ô Mã coupon tự viết hoa)

Kết quả nhập thử ở S0 được sinh viên cất riêng, không đưa cho AI khi thiết kế (yêu cầu ngay từ đầu S1). Một phần kết quả đó (ô tự chuyển chữ hoa khi gõ) chỉ được đưa ra ở S5.

| Test case | Thay đổi | Phát hiện | Nguyên nhân | Căn cứ |
|---|---|---|---|---|
| TC-CPN-140, 141, 142 | Thêm bản API cho lớp chữ thường (EC07, EC18, điểm P5 "1 chữ thường") | Sinh viên (S5) | Chất lượng input/prompt | Cột "Vì sao AI bỏ sót": "Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế" |
| TC-CPN-06, 34, 123 | Thêm GH9: Chỉ kiểm hành vi giao diện | Sinh viên (S5) | Chất lượng input/prompt | Như trên |
| TC-CPN-10 | Kết quả mong đợi chấp nhận `<B>FR17TC10</B>` | Sinh viên đưa thông tin; AI nhận ra hệ quả (S5) | Chất lượng input/prompt | Như trên |
| TC-CPN-143 và GH14 cho TC-CPN-03, 04, 31, 35, 120, 122 | Thêm bản API cho khoảng trắng đầu cuối của `code` | Sinh viên (S5, ý 3) | Chất lượng input/prompt | Cột "Vì sao AI bỏ sót": "...dấu hiệu trang có xử lý giá trị (tự chuyển chữ hoa) chỉ có từ lần nhập thử ở S0". Ý này được xếp vào đây vì dấu hiệu mã của trang tự sửa giá trị là thông tin bị giữ lại; nếu biết sớm, AI có căn cứ để không dựa vào lưu ý chung "ô chữ không tự cắt khoảng trắng" |

Việc giữ lại thông tin là có chủ đích, để phần phân tích này trung thực. Hệ quả: 10 test case (3 thêm, 7 sửa) chỉ được điều chỉnh ở S5.

### 2.3 Các ý sinh viên hỏi khi review S5

| Ý | Test case | AI bỏ sót hoặc sai gì | Nguyên nhân | Căn cứ |
|---|---|---|---|---|
| 1 | TC-CPN-77 | Gán quyền admin của `GET /api/coupons` cho FR-12, trong khi FR-12 chỉ nói `/api/admin/*` và các method thay đổi dữ liệu (loại Sai) | Giới hạn của công cụ AI | `05_final_tc.md` mục 14: "Bản AI (từ S1) truy vết sai căn cứ". Đặc tả có hai nguồn không khớp (FR-12 và API spec), nhưng AI có đủ cả hai và vẫn khẳng định quá căn cứ |
| 2 | TC-CPN-101, 105, 108, 112, 130 | Kết quả mong đợi không nói cách đọc khi hệ thống từ chối vì số thập phân thay vì vì giá trị (loại Mơ hồ) | Độ phức tạp của feature | `05_final_tc.md` mục 14; điểm biên bước 0.01 chịu cùng lúc giả định A02, A03 và ràng buộc giá trị |
| 3 | TC-CPN-143 | Không có bản API cho khoảng trắng đầu cuối (loại Thiếu) | Chất lượng input/prompt | Xem mục 2.2 |
| 4 | TC-CPN-144 | Không tách lớp "rất nhiều mã" để kiểm hiển thị danh sách (loại Thiếu) | Giới hạn của công cụ AI | Cột "Vì sao AI bỏ sót": "AI chỉ chia số mã đang có theo đặc tả (có mã, không còn mã) và chưa tách lớp 'rất nhiều mã' theo rủi ro hiển thị, vì đặc tả không nêu phân trang" |

### 2.4 Tổng hợp theo nguyên nhân

| Nguyên nhân | Nhóm ở mục 2.1 đến 2.3 | Ví dụ |
|---|---|---|
| Chất lượng input/prompt | 4 | Ô tự viết hoa, khoảng trắng qua API |
| Giới hạn của công cụ AI | 8 | Input gián tiếp của Xóa, dạng request, số lớn, truy vết FR-12, danh sách dài |
| Độ phức tạp của feature | 3 | Tham chiếu chéo dự phòng API, `GET` thiếu trường, điểm biên số thập phân |

(TC-CPN-143 được đếm một lần, ở mục 2.2.)

## 3. Bug AI bỏ sót

Đối chiếu 12 bug ở `bugs/bug_report.md` (issue #55 đến #66) với nguồn gốc của test case phát hiện ra chúng (`05_final_tc.md`, `ai_raw/S3_test_cases.md`, `ai_raw/S4_bva.md`).

| Bug | Issue | Test case phát hiện | Nguồn gốc test case | Bản AI gốc bắt được không |
|---|---|---|---|---|
| BUG-FR17-01 | #60 | TC-CPN-75, 79 | AI | Có |
| BUG-FR17-02 | #61 | TC-CPN-66, 65 (dòng A); TC-CPN-70; TC-CPN-143 (dòng C) | AI; AI (lớp EC95 từ câu hỏi S1 của sinh viên); SV thêm | Có, với phần chính (TC-CPN-66, 65). Body `{}` và mã chỉ có dấu cách nhờ sinh viên |
| BUG-FR17-03 | #62 | TC-CPN-65 (dòng B) | AI | Có |
| BUG-FR17-04 | #55 | TC-CPN-38 | AI | Có |
| BUG-FR17-05 | #63 | TC-CPN-67 | AI | Có |
| BUG-FR17-06 | #64 | TC-CPN-131 | AI có SV sửa (thêm khi review S4, phiên điều phối phát hiện) | Không trực tiếp: Bản AI có TC-CPN-111, 114, 119 qua giao diện nhưng các test case này không chạy ở S6; bug chỉ tìm được nhờ TC-CPN-131 |
| BUG-FR17-07 | #65 | TC-CPN-69 | AI (lớp EC91 đến EC94 từ câu hỏi 2 của sinh viên ở S1) | Không: Bản AI S1 không có biến dạng request; lớp chỉ có sau câu hỏi của sinh viên |
| BUG-FR17-08 | #56 | TC-CPN-37 | AI | Có (Khác giả định A01, sinh viên quyết định thành bug) |
| BUG-FR17-09 | #66 | TC-CPN-68 | AI | Có (Khác giả định A13, sinh viên quyết định thành bug) |
| BUG-FR17-10 | #57 | TC-CPN-91, 32 | AI | Có. Lý do Fail về tiếng Việt của thông báo dựa trên yêu cầu AI tự bổ sung khi review S3 |
| BUG-FR17-11 | #58 | TC-CPN-92 | AI | Có |
| BUG-FR17-12 | #59 | TC-CPN-90 | AI | Có |

Tóm lại:

- **Bản AI gốc bắt được 10 trên 12 bug** (01, 02 phần chính, 03, 04, 05, 08, 09, 10, 11, 12).
- **2 bug chỉ tìm được nhờ test case do người hoặc phiên khác bổ sung:** BUG-FR17-07 (câu hỏi của sinh viên ở S1 về request API) và BUG-FR17-06 (phiên điều phối ở S4 về làm tròn số lớn).
- **Bổ sung của sinh viên ở S5 không tìm ra bug mới riêng:** TC-CPN-140, 141 cho kết quả "Khác giả định A04" (sinh viên quyết định không thành bug), TC-CPN-142, 144 Pass, TC-CPN-143 dòng C được gộp vào BUG-FR17-02.
- **Một sửa đổi của sinh viên tránh được bug có căn cứ sai:** Nếu giữ kết quả mong đợi của bản AI cho TC-CPN-77 (ERR13 theo FR-12), lần chạy trả 2xx sẽ thành bug dẫn sai FR-12. Sau ý 1 ở S5, hành vi này được ghi là "Khác giả định A28" và chỉ nêu trong ghi chú của BUG-FR17-01.

## 4. Giới hạn của kết quả

- **S6 rút gọn:** 69 trên 115 test case Not run (`06_results.md` mục 7). Toàn bộ 29 test case BVA qua giao diện (nhóm D), 21 trên 25 test case hợp lệ qua giao diện, 13 trên 17 test case không hợp lệ qua giao diện và nhóm H không chạy. Các dòng dự phòng của TC-CPN-82, 130 không chạy. Vì vậy chưa biết bản AI có bỏ sót bug nào nằm trong các test case này hay không, và chưa đánh giá được hiệu quả của phần BVA (S4) qua giao diện.
- **Đọc kết hợp chưa làm được:** TC-CPN-131 (API) cần đọc cùng TC-CPN-111, 114, 119 (giao diện) để biết làm tròn xảy ra ở đâu; ba test case giao diện không chạy.
- **Thứ tự chạy khác kế hoạch:** Nhóm API chạy lúc 00:34, trước test giao diện; TC-CPN-61 chạy lúc 00:54 sau test giao diện, không phải ngay sau reset. Khi test giao diện, danh sách đã có thêm khoảng 40 mã do API tạo ra; không ảnh hưởng kết quả của các test case đã chạy, nhưng khác điều kiện "dữ liệu mẫu nguyên vẹn" của kế hoạch.
- **Bằng chứng chưa đầy đủ:** Ảnh của nhiều test case giao diện không cho thấy bước tải lại trang (K1, K3, K7); 4 ảnh log (`S6_TC-CPN-66_log_2.png`, `67_log`, `68_log`, `69_log`) bị cắt chữ ở mép phải nên không thấy đủ giá trị làm bằng chứng.
- **Phân loại nguyên nhân là đánh giá:** Mỗi dòng ở mục 2 chỉ xếp một nguyên nhân chính; nhiều dòng có cả yếu tố khác (ví dụ TC-CPN-77 vừa do AI khẳng định quá căn cứ, vừa do đặc tả có hai nguồn không khớp).
- **"Khác giả định" phụ thuộc giả định của sinh viên:** 6 test case Khác giả định không được tính là bug của AI hay của hệ thống; 2 trong số đó được sinh viên quyết định thành bug.

## 5. Bài học

1. **Câu hỏi sớm ở S1 có giá trị lớn nhất.** Hai câu hỏi của sinh viên ở S1 (Input gián tiếp của Xóa, dạng request API) tạo ra các lớp dẫn tới BUG-FR17-07 và một phần BUG-FR17-02. AI thiên về các ô nhìn thấy trên form; cần nhắc riêng các biến về trạng thái dữ liệu và giao thức.
2. **Thông tin quan sát giao diện quyết định đường thực thi.** Việc mã của trang tự sửa giá trị (viết hoa) làm 10 test case phải chỉnh ở S5. Lưu ý chung về nền tảng (ô chữ không tự cắt khoảng trắng) không thay được quan sát thật của chính trang.
3. **Quy tắc dự phòng không nên áp máy móc.** Quy tắc "API chỉ chạy khi giao diện chặn" bỏ sót trường hợp giao diện không chặn mà vẫn biến đổi giá trị (`2^53 + 1`). Một phiên soát độc lập (phiên điều phối) đã bắt được, và nhờ đó tìm ra BUG-FR17-06.
4. **AI tự kiểm tra mâu thuẫn có ích nhưng chủ yếu sửa lỗi nhỏ.** 15 trên 29 thay đổi do AI tự phát hiện, phần lớn là tham chiếu chéo, thứ tự chạy, cập nhật hệ quả. Các thiếu sót về phạm vi (biến, lớp mới) đều do người hoặc phiên khác phát hiện.
5. **Mỗi kết quả mong đợi cần trích đúng câu đặc tả bao phủ nó.** AI gán quyền admin của `GET` cho FR-12 dù FR-12 không nói về `GET`; lỗi này chỉ lộ ra khi sinh viên đọc lại căn cứ ở S5.
