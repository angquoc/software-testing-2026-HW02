# S8: AI gap analysis (FR-07 Giỏ hàng)

- Bước: S8 (Phân tích những gì AI bỏ sót và vì sao, đề mục 6.3)
- Thời gian tạo: 2026-10-21 09:07 (UTC+07:00)
- Bản gốc của AI: `ai_raw/S8_gap_analysis.md`. `08_gap_analysis.md` lúc tạo giống hệt bản này; sinh viên review trực tiếp trên `08_gap_analysis.md`
- Căn cứ: Bảng "Thay đổi so với bản AI" của `00_spec.md` (S0), `01_io.md` (S1), `02_ec.md` (S2), `03_tc.md` (S3), `04_bva.md` (S4), `05_final_tc.md` (S5); `05_final_tc.md` mục 2, 9; `06_results.md` (S6, mục 4.F); `bugs/bug_report.md` mục FR-07 (S7); `ai_raw/S3_test_cases.md`, `ai_raw/S4_bva.md`
- Ba nguyên nhân dùng để phân loại (theo đề mục 6.3): **Chất lượng input/prompt**, **Giới hạn của công cụ AI**, **Độ phức tạp của feature**

---

## 1. Thống kê các bảng "Thay đổi so với bản AI" (S0 đến S5)

### 1.1 Theo Loại

| Bước | File | Sai | Thiếu | Thừa | Mơ hồ | Quyết định của SV | Tổng |
|---|---|---|---|---|---|---|---|
| S0 | `00_spec.md` mục 13 | 0 | 0 | 0 | 0 | 8 | 8 |
| S1 | `01_io.md` mục 12 | 0 | 2 | 0 | 0 | 10 | 12 |
| S2 | `02_ec.md` mục 10 | 0 | 0 | 0 | 0 | 2 | 2 |
| S3 | `03_tc.md` mục 15 | 0 | 0 | 0 | 0 | 1 | 1 |
| S4 | `04_bva.md` mục 10 | 0 | 0 | 0 | 0 | 1 | 1 |
| S5 | `05_final_tc.md` mục 14 | 0 | 0 | 0 | 0 | 1 | 1 |
| **Tổng** | | **0** | **2** | **0** | **0** | **23** | **25** |

23 trên 25 dòng là quyết định của sinh viên. Từ S2, do thời gian gấp, sinh viên yêu cầu AI áp luôn phương án đề xuất rồi duyệt một lượt, và chấp nhận toàn bộ. Vì vậy bảng thay đổi ít cho thấy sai sót của AI; phần lớn thông tin về chỗ AI bỏ sót đến từ kết quả chạy (mục 2, 3).

### 1.2 Theo người phát hiện (2 dòng Thiếu)

| Bước | Sinh viên | AI tự phát hiện khi review | Phiên điều phối (`305c705a`) | Tổng |
|---|---|---|---|---|
| S1 | 0 | 0 | 2 | 2 |

Cả 2 dòng cùng một thiếu sót: Yêu cầu FR07-R33 và Output OUT15 (phản hồi trực quan sau khi bấm "Thêm vào giỏ", FR-24 ý 1).

### 1.3 Lỗi AI tự sửa trước khi giao (không có trong bảng thay đổi)

| Bước | Lỗi | Cách phát hiện |
|---|---|---|
| S0 | Mã câu hỏi mở không liên tục theo thứ tự trong bảng | Tự kiểm trước khi giao |
| S1 | Hai câu khẳng định quá căn cứ (tên lấy từ sản phẩm được chọn; trang hiển thị lại thay đổi ngay) | Tự kiểm theo checklist S1 |
| S4 | Ghi "không tạo được đúng 1,000,000,000 từ dữ liệu mẫu", trong khi Bàn phím cơ Keychron Q1 × 250 cho đúng giá trị này | Tự kiểm phép tính trước khi giao; P4 đổi sang Keychron (TC-CART-104, 105). Điểm 990,000,000 đã hẹn ở `03_tc.md` mục 14 là hệ quả của lỗi tính này |

### 1.4 Nguồn gốc của bộ test case cuối

Theo `05_final_tc.md` mục 2: 38 test case, cả 38 là "AI"; 4 test case (TC-CART-01, 02, 100, 101) kiểm Output do phiên điều phối bổ sung ở S1.

## 2. Test case AI bỏ sót hoặc thiết kế chưa đủ

| Nội dung | AI bỏ sót hoặc chưa đủ gì | Phát hiện | Nguyên nhân | Căn cứ |
|---|---|---|---|---|
| FR07-R33, OUT15 (TC-CART-01, 02, 100, 101) | Bản AI S0 xếp FR-24 ý 1 ra ngoài phạm vi vì "xảy ra ở trang chi tiết"; S1 thêm đường trang chủ (IN3) nhưng không xét lại | Phiên điều phối `305c705a` (S1) | Giới hạn của công cụ AI | `01_io.md` mục 7.1, 9: AI có đủ chữ của FR-24 nhưng chia phạm vi theo trang thay vì theo nút |
| Giỏ có được giữ sau khi tải lại trang (Q14) | Không có lớp nào; AI đề xuất "IN14 không là biến, dùng tải lại trang làm cách kiểm chứng", sinh viên chọn | Lộ ra ở S6 khi script so giỏ API trước và sau (ghi nhận 8) | Độ phức tạp của feature | `01_io.md` quyết định 4; đặc tả không nói về lưu giỏ, và AI dùng chính hành vi chưa kiểm (tải lại trang) làm cách kiểm chứng |
| Cách kiểm chứng K1 (F5 và `GET /api/cart`) | Giả định giỏ trên Web và giỏ API là một; khi chạy thì không phải, K1 không dùng được | S6 | Độ phức tạp của feature | `06_results.md` mục 4.F, ghi nhận 8; `05_final_tc.md` GH1 chỉ tính trường hợp giỏ mất khi tải lại |
| Nút "Tiếp tục mua sắm" khi giỏ có hàng (FR07-R12) | Checklist TC-CART-91 chỉ xét giỏ trống; ở giỏ có hàng chỉ có ghi chú trong bước của TC-CART-11 | AI đề xuất thành bug ở S7 (KG04) | Giới hạn của công cụ AI | Q28 đã chốt xét cả hai trạng thái nhưng S3 không đưa vào checklist |
| Tiền điều kiện nối tiếp (TC-CART-02, 03, 08, 11; nhóm API hợp lệ) | Kết quả mong đợi phụ thuộc test case trước (ví dụ tổng 58,000,000 cần TC-CART-01 Pass; giỏ API trống cần xóa qua giao diện) | Sinh viên (S6, câu hỏi về 58,000,000; TC-CART-03 phải chạy lại) | Giới hạn của công cụ AI | `06_results.md` cột Ghi chú; AI xếp thứ tự chạy liền mạch để tiết kiệm thời gian mà không tính trường hợp test case đầu Fail |
| Thêm trùng qua trang chủ và API | Không thiết kế (chỉ một đại diện mỗi đường) | Lộ ra ở TC-CART-02 (bấm 2 lần) và log API | Chất lượng input/prompt | `01_io.md` quyết định 10 của sinh viên do thiếu thời gian; không phải AI bỏ sót, ghi lại vì bug thật nằm ở đó |

Tổng hợp: Giới hạn của công cụ AI 3; Độ phức tạp của feature 2; Chất lượng input/prompt 1.

## 3. Bug AI bỏ sót

Đối chiếu 18 bug ở `bugs/bug_report.md` (issue #67 đến #84) với test case phát hiện.

| Bug | Issue | Test case phát hiện | Bản AI gốc bắt được không |
|---|---|---|---|
| BUG-FR07-01 | #67 | TC-CART-31 đến 34, 102 | Có |
| BUG-FR07-02 | #68 | TC-CART-51 | Có (Khác giả định A24, sinh viên quyết định thành bug) |
| BUG-FR07-03 | #69 | TC-CART-30 | Có (giả định A24) |
| BUG-FR07-04 | #70 | TC-CART-03, 02, 08 | Có (TC-CART-03); phần trang chủ thấy được nhờ sinh viên bấm 2 lần ở TC-CART-02 |
| BUG-FR07-05 | #71 | TC-CART-04 đến 06 (Blocked) | Có |
| BUG-FR07-06 | #72 | TC-CART-07 đến 09 | Có |
| BUG-FR07-07 | #73 | TC-CART-01 | Có; hiện tượng "phải bấm 2 lần" do sinh viên quan sát |
| BUG-FR07-08 | #74 | TC-CART-50 | Một phần: TC-CART-50 Fail vì trang không hiện dòng thêm qua API, nhưng việc giỏ mất khi tải lại không có test case (mục 2) |
| BUG-FR07-09, 10 | #75, #76 | TC-CART-90 | Có |
| BUG-FR07-11 | #77 | TC-CART-11 (Pass) | Không trực tiếp: Thành bug từ đề xuất KG04 ở S7 |
| BUG-FR07-12 | #78 | TC-CART-01, 02 | Không với bản AI S1 gốc: OUT15 do phiên điều phối bổ sung; các test case S3 đã có OUT15 |
| BUG-FR07-13 đến 18 | #79 đến #84 | TC-CART-02, 91, 10, 09, 92, 93, 95 | Có |

Tóm lại: Bộ test case AI thiết kế (S3, S4) bắt được 15 trên 18 bug một cách trực tiếp. BUG-FR07-12 cần Output do phiên điều phối bổ sung; BUG-FR07-08 và 11 chỉ thành bug nhờ quan sát và đề xuất thêm ở S6, S7.

## 4. Giới hạn của kết quả

- **S6 rút gọn:** 8 trên 38 test case Not run (TC-CART-12, 94, 96, 97, 100, 101, 103, 104). 4 trên 5 test case BVA qua giao diện không chạy, nên chưa đánh giá được phần BVA qua giao diện (chỉ có TC-CART-105 Pass).
- **Tiền điều kiện khác kế hoạch:** TC-CART-02, 03, 08, 11 chạy với giỏ khác tiền điều kiện vì TC-CART-01 Fail; nhóm API hợp lệ chạy khi giỏ API đã có 7 đến 11 dòng rác. Kết quả được đánh giá theo dòng mới thêm, không theo giá trị mong đợi gốc.
- **Bằng chứng:** Một số trạng thái dùng lại ảnh S0 (`S0_05`, `S0_03`) thay vì chụp lúc chạy; hiện tượng "phải bấm 2 lần" chỉ có lời mô tả. Bảng quan sát S0 do AI điền từ ảnh theo yêu cầu sinh viên (lệch WORKFLOW mục 3.1).
- **Bảng thay đổi ít dữ liệu:** Vì sinh viên chấp nhận toàn bộ đề xuất từ S2, không đo được chất lượng các đề xuất đó qua review; chỉ đo được qua kết quả chạy.
- **Phân loại nguyên nhân là đánh giá:** Mỗi dòng ở mục 2 chỉ xếp một nguyên nhân chính.

## 5. Bài học

1. **Chia phạm vi theo nút, không theo trang.** AI loại FR-24 ý 1 vì gắn nó với trang chi tiết, bỏ qua nút cùng tên ở trang chủ. Một phiên soát độc lập bắt được, và yêu cầu này dẫn tới BUG-FR07-12.
2. **Không dùng hành vi chưa kiểm làm cách kiểm chứng.** AI chọn "tải lại trang" để chứng minh dữ liệu đã lưu, trong khi chính việc giỏ có được giữ hay không chưa có test case. Bug lớn nhất về dữ liệu (BUG-FR07-08) lộ ra nhờ script so giỏ trước và sau, không nhờ thiết kế.
3. **Chuỗi tiền điều kiện tiết kiệm thời gian nhưng dễ gãy.** Khi test case đầu tiên Fail, các test case nối tiếp mang giá trị mong đợi sai. Nên ghi kết quả mong đợi theo trạng thái tương đối (ví dụ "tổng tăng đúng bằng Thành tiền dòng mới") hoặc dựng tiền điều kiện độc lập.
4. **Áp đề xuất hàng loạt giúp kịp giờ nhưng làm mất dấu vết review.** Từ S2, 100% thay đổi là "Quyết định của SV"; các chỗ AI chưa tốt chỉ hiện ra ở S6. Khi gấp, vẫn nên đọc kỹ các đề xuất loại bỏ biến (như IN14) vì đó là chỗ dễ mất lớp nhất.
