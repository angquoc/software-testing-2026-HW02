# S8: AI gap analysis (FR-01 Đăng ký tài khoản)

- Bước: S8 (đề mục 6.3: AI bỏ sót test case hay bug nào, vì sao). AI viết bản nháp từ các file của feature và `bugs/bug_report.md`; sinh viên review
- Thời gian tạo: 2026-10-21 02:44 (+07:00)
- Bản này: Bản review của S8. Bản gốc của AI: `ai_raw/S8_gap_analysis.md`
- Cập nhật lần 1: 2026-10-21 03:14 (+07:00). Sinh viên chấp nhận cách lấy căn cứ ở đầu file; đổi nguyên nhân của dòng 4, 5 (thành Độ phức tạp) và dòng 15 (thành Input); ghi rõ người phát hiện dòng 24; cập nhật số đếm theo nguyên nhân (mục 6)
- Căn cứ: Bảng "Thay đổi so với bản AI" của `00_spec.md` đến `05_final_tc.md`; các mục trả lời câu hỏi khi review (`02_ec.md` mục 11, `03_tc.md` mục 10, `04_bva.md` mục 9); `05_final_tc.md` mục 2, 9 (nguồn gốc, người phát hiện); `06_results.md` mục 4 đến 6 (kết quả, quan sát ngoài test case); `bugs/bug_report.md` phần FR-01; `ai_raw/S3_test_cases.md` mục 5.3 (cách chọn test case API)

Ghi chú về căn cứ: Cột "Vì sao AI bỏ sót" chỉ có trong bảng trống ở `ai_raw/S5_final_test_cases.md` mục 13. Sinh viên không bổ sung test case nào ở S5, nên bảng đó đã được thay bằng ghi nhận ở `05_final_tc.md` mục 13 và cột này không có dữ liệu. Lý do AI bỏ sót ở mục 2 lấy từ cột "Lý do hoặc căn cứ" của các bảng thay đổi và từ các mục trả lời câu hỏi khi review.

---

## 1. Thống kê các bảng "Thay đổi so với bản AI"

### 1.1 Nguồn số liệu

| Bước | File | Mục | Bản AI được so |
|---|---|---|---|
| S0 | `00_spec.md` | Mục 6 | `ai_raw/S0_khao_sat.md`, `ai_raw/S0_khao_sat_v2.md` |
| S1 | `01_io.md` | Mục 6 | `ai_raw/S1_input_output.md` |
| S2 | `02_ec.md` | Mục 12 | `ai_raw/S2_equivalence_classes.md` |
| S3 | `03_tc.md` | Mục 12 | `ai_raw/S3_test_cases.md` |
| S4 | `04_bva.md` | Mục 10 | `ai_raw/S4_bva.md` |
| S5 | `05_final_tc.md` | Mục 14 | `ai_raw/S5_final_test_cases.md` |

Mỗi dòng của bảng thay đổi đếm là 1, kể cả khi dòng đó gộp nhiều lớp hay nhiều test case. Không đếm `00_spec.md` mục 4.6 (chỗ AI sửa trên bảng quan sát do sinh viên điền), vì đó không phải thay đổi so với bản AI.

### 1.2 Theo Loại

| Bước | Sai | Thiếu | Thừa | Mơ hồ | Quyết định của SV | Tổng |
|---|---|---|---|---|---|---|
| S0 | 0 | 0 | 1 | 0 | 6 | 7 |
| S1 | 0 | 2 | 0 | 0 | 6 | 8 |
| S2 | 1 | 13 | 0 | 0 | 27 | 41 |
| S3 | 0 | 6 | 1 | 0 | 11 | 18 |
| S4 | 0 | 4 | 4 | 0 | 7 | 15 |
| S5 | 0 | 2 | 0 | 0 | 1 | 3 |
| **Tổng** | **1** | **27** | **6** | **0** | **58** | **92** |

Dòng "Quyết định của SV" gồm cả các dòng hệ quả và thay bảng phương án bằng bảng quyết định (ví dụ "Cập nhật tổng hợp", "Thay bảng phương án"), nên không phản ánh lỗi của bản AI. Phần còn lại, 34 dòng Sai, Thiếu, Thừa, là chỗ bản AI chưa đúng.

### 1.3 Theo người phát hiện (34 dòng Sai, Thiếu, Thừa)

Cách xếp, theo cột "Lý do hoặc căn cứ":

- **Sinh viên:** Lý do ghi "Sinh viên phát hiện", hoặc dẫn tới một câu hỏi của sinh viên khi review (ví dụ "câu hỏi Email 1"). Dòng `02_ec.md` mục 7.3 (giả định A15) không ghi người phát hiện; xếp theo câu hỏi gắn với nó (`02_ec.md` mục 11.2 câu 3).
- **AI tự phát hiện khi review:** Lý do ghi "AI bổ sung khi viết bản review", "AI bổ sung khi review" hoặc "AI bổ sung khi trả lời câu hỏi" (AI ở phiên thiết kế).
- **Phiên điều phối:** Lý do ghi "Claude ở phiên điều phối (session `305c705a`)", gồm cả dòng ghi "Như dòng trên" ngay sau dòng đó.

| Bước | Sinh viên | AI tự phát hiện khi review | Phiên điều phối | Tổng |
|---|---|---|---|---|
| S0 | 1 | 0 | 0 | 1 |
| S1 | 0 | 2 | 0 | 2 |
| S2 | 11 | 3 | 0 | 14 |
| S3 | 4 | 0 | 3 | 7 |
| S4 | 4 | 2 | 2 | 8 |
| S5 | 2 | 0 | 0 | 2 |
| **Tổng** | **22** | **7** | **5** | **34** |

| Loại | Sinh viên | AI tự phát hiện khi review | Phiên điều phối | Tổng |
|---|---|---|---|---|
| Sai | 1 | 0 | 0 | 1 |
| Thiếu | 16 | 7 | 4 | 27 |
| Thừa | 5 | 0 | 1 | 6 |
| **Tổng** | **22** | **7** | **5** | **34** |

Nhận xét:

- S2 (chia lớp) có nhiều chỗ chưa đúng nhất: 14 trong 34 dòng, gần hết là lớp bị thiếu.
- Cả 7 dòng AI tự phát hiện đều là "Thiếu" và đều xuất hiện ở bản review, sau khi sinh viên đã chốt quyết định hoặc đặt câu hỏi (ví dụ EC67 sau A07 (a), EC62 và EC63 sau A04 (b), nguyên tắc ở `04_bva.md` mục 1 sau câu hỏi 2).
- Cả 5 dòng của phiên điều phối liên quan tới hành vi nằm ngoài đặc tả: Trình duyệt tự cắt khoảng trắng của ô `type="email"`, và tác dụng phụ của TC-REG-79 lên dữ liệu dùng chung.

---

## 2. Test case AI bỏ sót hoặc thiết kế sai

### 2.1 Cách xếp nguyên nhân

| Nguyên nhân (theo đề) | Tiêu chí dùng trong bảng |
|---|---|
| Input (chất lượng input hoặc prompt) | Thông tin cần để thiết kế đúng chưa có trong input khi AI làm bản gốc: Giả định, nguyên tắc do sinh viên chốt sau đó, hoặc quy tắc chọn được giao cho AI chưa nêu tiêu chí cần thiết |
| Giới hạn công cụ AI | Thông tin đã có trong input hoặc trong chính bản AI, nhưng AI không dùng hoặc dùng sai: Gộp lớp không có căn cứ, áp quy tắc của slide một cách máy móc, bỏ qua ghi chú đã có, suy luận sai |
| Độ phức tạp của feature | Lỗi đến từ sự tương tác giữa nhiều quy tắc hoặc nhiều tầng (đặc tả, chuẩn HTML, trình duyệt, giao diện, API), khó thấy khi xét từng quy tắc riêng lẻ; hoặc đặc tả không định nghĩa một quy tắc nên phải dựa vào chuẩn bên ngoài có nhiều luật con (ví dụ định dạng email theo HTML5) |

Mỗi dòng chỉ xếp vào một nguyên nhân chính. Cột "Kết quả S6" lấy từ `06_results.md` mục 4.

### 2.2 Danh sách

| # | Test case | Bước | Bản AI bỏ sót hoặc sai gì | Người phát hiện | Nguyên nhân | Căn cứ | Kết quả S6 |
|---|---|---|---|---|---|---|---|
| 1 | TC-REG-04, TC-REG-05 (EC56, EC55) | S2 | Gộp chữ số và dấu câu vào EC06; không có lớp Họ Tên không có chữ cái nào | Sinh viên | Giới hạn công cụ | `02_ec.md` mục 11.1 câu 2: Bản AI gộp chung "vì cùng là ký tự không phải chữ cái", không có lý do để tin hai loại được xử lý giống nhau | Not run |
| 2 | TC-REG-06 (EC54) | S2 | Thiếu lớp Họ Tên có khoảng trắng đầu cuối | Sinh viên | Input | `02_ec.md` mục 12: "Câu hỏi Họ Tên 5; nguyên tắc khoảng trắng". Nguyên tắc khoảng trắng do sinh viên chốt khi review S2 (mục 1.1), bản AI gốc chưa có | Not run |
| 3 | TC-REG-131 (`␣A␣`) | S2, S4 | S2: Chỉ ngầm thể hiện cận dưới 1 ký tự của Họ Tên. S4: Bỏ qua biến thể `␣A␣` dù `02_ec.md` đã ghi cho S4 | Sinh viên | Giới hạn công cụ | `04_bva.md` mục 10: "`02_ec.md` cuối mục 2 đã ghi biến thể này cho S4, bản AI bỏ qua"; mục 9 câu 1 | Not run |
| 4 | TC-REG-12, TC-REG-39, TC-REG-13, TC-REG-40, TC-REG-41 (EC57 đến EC61) | S2 | Thiếu lớp dấu chấm và ký tự đặc biệt ở hai phía của `@` | Sinh viên | Độ phức tạp | `02_ec.md` mục 12: "Câu hỏi Email 1, 2; quy tắc HTML5 theo A04 (b)". Đặc tả chỉ nêu ví dụ `user@domain.com`, không định nghĩa định dạng email; các lớp này đến từ quy tắc HTML5 (A04 (b)) có nhiều luật con cho hai phía của `@` | TC-REG-39 Blocked; còn lại Not run |
| 5 | TC-REG-42, TC-REG-43 (EC62, EC63) | S2 | Thiếu 2 luật của HTML5: Nhãn tên miền bắt đầu hoặc kết thúc bằng `-`, nhãn dài hơn 63 ký tự | AI tự phát hiện | Độ phức tạp | `02_ec.md` mục 12: "Quy tắc HTML5 theo A04 (b) có 2 luật này. AI bổ sung khi trả lời câu hỏi Email 2". Như dòng 4: Đặc tả không định nghĩa định dạng email | Not run |
| 6 | TC-REG-44, TC-REG-14 (EC64, EC65); giả định A15 | S2 | Thiếu lớp email có chữ Unicode; chưa thấy A04 (b) không đủ để kết luận cho tên miền quốc tế | Sinh viên | Độ phức tạp | `02_ec.md` mục 11.2 câu 3: Chuẩn HTML cho phép trình duyệt chuyển tên miền quốc tế sang punycode; mục 7.3 nêu 3 hệ quả (phụ thuộc trình duyệt, khác biệt khi qua API, cách tính biên 63 ký tự) | Not run |
| 7 | TC-REG-15 (EC66) | S2 | Kết luận sai rằng ký tự SQL, HTML "đã làm email sai định dạng" nên không lập lớp riêng (dòng "Sai" duy nhất) | Sinh viên | Giới hạn công cụ | `02_ec.md` mục 11.2 câu 4: Theo chính A04 (b) mà bản AI mô tả, `'` được phép ở phần trước `@` | Not run |
| 8 | TC-REG-48 (EC67) | S2 | Thiếu lớp email trùng sau khi cắt khoảng trắng | AI tự phát hiện | Input | `02_ec.md` mục 12: "Hệ quả của A07 (a) ... AI bổ sung khi review"; A07 (a) chốt khi review | Not run (cùng lớp qua API: TC-REG-82 Fail) |
| 9 | TC-REG-18 (EC68) | S2 | Thiếu lớp mật khẩu chỉ đủ 8 ký tự khi tính cả khoảng trắng đầu hoặc cuối | AI tự phát hiện | Input | `02_ec.md` mục 12: "Hệ quả của nguyên tắc khoảng trắng và A10 (a). AI bổ sung khi review" | Not run |
| 10 | TC-REG-58 (EC69) | S2 | Thiếu lớp mật khẩu chỉ gồm khoảng trắng | Sinh viên | Giới hạn công cụ | `02_ec.md` mục 12: "Hệ quả của nguyên tắc khoảng trắng mà bản AI và lần review trước chưa xét". Nguyên tắc đã có trong input của lần review nhưng AI không suy ra lớp này | Not run |
| 11 | TC-REG-07 (EC70) | S2 | Thiếu lớp Họ Tên có từ 2 khoảng trắng liền nhau ở giữa | Sinh viên | Giới hạn công cụ | `02_ec.md` mục 11.3 câu 2: Nhiều hệ thống kiểm tên theo mẫu "các từ cách nhau đúng 1 dấu cách"; AI không xét biến thể này dù đã có nguyên tắc khoảng trắng | Not run |
| 12 | TC-REG-02 đến TC-REG-07, TC-REG-09 đến TC-REG-14, TC-REG-16 đến TC-REG-18 (15 test case tách từ 6 test case gộp) | S3 | Gộp nhiều lớp hợp lệ bất thường vào một test case (ví dụ TC-REG-07 cũ có 3 lớp), khi lỗi không biết lớp nào gây ra | Sinh viên | Input | `03_tc.md` mục 10 câu 3: "Quy tắc của slide cho phép gộp để có số test case tối thiểu". Bản AI làm đúng quy tắc Minimum Set được giao; tiêu chí "không quá phức tạp" của Kaner không có trong quy tắc đó. Dòng này ghi là "Quyết định của SV" ở `03_tc.md` mục 12 nhưng lý do nêu rõ bản AI vi phạm tiêu chí này | Not run (cả 15) |
| 13 | TC-REG-11 (bước 2); giới hạn GH1, GH3 cho TC-REG-06, 07, 16, 18 | S3 | Cho kết quả OUT1 nhưng không nêu OUT1 chỉ chứng minh hệ thống chấp nhận; không kiểm chứng email được lưu ở dạng nào | Sinh viên | Giới hạn công cụ | `03_tc.md` mục 12 (dòng TC-REG-11 và dòng mục 5.1), mục 10 câu 2 | Not run |
| 14 | TC-REG-59 đến TC-REG-62 (phạm vi qua API) | S3 | Khẳng định "API không có trường Xác nhận mật khẩu", quá căn cứ của đặc tả | Sinh viên | Giới hạn công cụ | `03_tc.md` mục 12 (dòng "Thừa"), mục 10 câu 1: Đặc tả API chỉ không mô tả trường này | Blocked (BUG-FR01-02) |
| 15 | TC-REG-70 (kiểm tra body không chứa mật khẩu) | S3 | Không có ma trận truy vết, nên không thấy FR01-R23 chưa được phủ | Sinh viên | Input | `03_tc.md` mục 10 câu 5: Thiếu ma trận truy vết nên không thấy R23 chưa được phủ. Theo sinh viên, prompt S3 không yêu cầu ma trận truy vết và không giao skill `test-case-writing` (skill có yêu cầu này, theo `03_tc.md` mục 12) | Pass |
| 16 | TC-REG-79 (chạy cuối, reset ngay sau đó) | S3 | Không xét rủi ro test case bảo mật phá dữ liệu dùng chung, làm sai kết quả các test case chạy sau | Phiên điều phối | Giới hạn công cụ | `03_tc.md` mục 12, mục 10.2 câu 1 | Blocked (BUG-FR01-01) |
| 17 | TC-REG-80, TC-REG-81, TC-REG-82; ghi chú GH2 cho TC-REG-11, 33, 48 | S3 | Không xét việc ô `type="email"` tự cắt khoảng trắng trước khi gửi, nên test case qua giao diện có thể chỉ kiểm tra trình duyệt | Phiên điều phối | Độ phức tạp | `03_tc.md` mục 10.2 câu 2: Hành vi của trình duyệt theo chuẩn HTML chồng lên hành vi của EShop | TC-REG-80 Fail, TC-REG-82 Fail, TC-REG-81 Blocked; TC-REG-33 Blocked; TC-REG-11, 48 Not run |
| 18 | TC-REG-105 (đã bỏ) | S4 | Chọn mật khẩu 1 ký tự, vi phạm cùng lúc độ dài và 3 điều kiện loại ký tự; không có nguyên tắc "mỗi điểm chỉ vi phạm một điều kiện" | Sinh viên | Giới hạn công cụ | `04_bva.md` mục 9 câu 2: Chọn chỉ vì là "LB" và "nhỏ nhất giao diện cho nhập" theo slide | Đã bỏ |
| 19 | TC-REG-109 (đã bỏ) | S4 | Thêm điểm "giữa" (mật khẩu 20 ký tự) cho phân vùng không có cận trên | Sinh viên | Giới hạn công cụ | `04_bva.md` mục 9 câu 3: Cùng lớp với TC-REG-108, 20 là con số tùy chọn | Đã bỏ |
| 20 | TC-REG-125 đến TC-REG-128 (đã bỏ) | S4 | Áp BVA cho phép so khớp Xác nhận mật khẩu, vốn không có thứ tự | Sinh viên | Giới hạn công cụ | `04_bva.md` mục 9 câu 4: Trái với nguyên tắc ở mục 1 của chính bản AI | Đã bỏ |
| 21 | TC-REG-124 (đã bỏ); quy ước biên khoảng trắng của Email phải kiểm qua API | S4 | Chọn Email là 1 dấu cách qua giao diện, trùng TC-REG-32 nếu trình duyệt cắt khoảng trắng | Phiên điều phối | Giới hạn công cụ | `04_bva.md` mục 10: "bản AI không áp ghi chú về `type="email"` đã có ở `03_tc.md` mục 10.2" | Đã bỏ |
| 22 | Mọi test case (tiền điều kiện reset dữ liệu mẫu) | S1 | Thiếu tiền điều kiện reset dữ liệu trước mỗi đợt test | AI tự phát hiện | Giới hạn công cụ | `01_io.md` mục 6: Theo WORKFLOW mục 3.3; IN5 thay đổi sau mỗi lần đăng ký thành công | Đã áp ở S6 (`06_results.md` mục 1) |
| 23 | Bước kiểm chứng "không tạo tài khoản" của TC-REG-71, 72, 75, 76, 77, 129 | S1 | Đưa phương án đăng ký lại cùng email mà không nêu điều kiện để kết quả đáng tin | AI tự phát hiện | Giới hạn công cụ | `01_io.md` mục 6: Cách này dựa vào chính FR01-R05 | Điều kiện đó không đạt ở S6, xem mục 4.4 |
| 24 | Không có test case API cho Email trùng chính xác | S3 | Bản AI chỉ chọn qua API các lớp "mà phía giao diện có thể chặn trước khi gửi"; luật Email duy nhất (FR01-R05) chỉ kiểm qua giao diện (TC-REG-45 đến 47) | AI tự phát hiện ở S8 (thấy qua kết quả S6, không có trong bảng thay đổi nào) | Độ phức tạp | `ai_raw/S3_test_cases.md` mục 5.3. Kiểm FR01-R05 qua giao diện cần một lần đăng ký thành công trước, nên lỗi ở luật mật khẩu (BUG-FR01-01) chặn luôn luật này: TC-REG-45 Blocked, TC-REG-46, 47 Not run | BUG-FR01-07 chỉ lộ ra nhờ TC-REG-82 và QS03 (mục 3) |

Quan hệ với mục 1: Các dòng 1 đến 11 và 13 đến 23 ứng với 30 trong 34 dòng Sai, Thiếu, Thừa (các dòng cùng nói về một test case được gộp lại). 4 dòng không thuộc test case nên không đưa vào: `00_spec.md` (bỏ phần DevTools), `04_bva.md` mục 4.3 (ghi chú ô Mật khẩu không bị cắt khoảng trắng), `05_final_tc.md` (2 dòng về cột "Phát hiện"). Dòng 12 lấy từ một dòng "Quyết định của SV"; dòng 24 thấy ở S6.

### 2.3 Tổng hợp theo nguyên nhân

| Nguyên nhân | Số dòng | Dòng | Người phát hiện |
|---|---|---|---|
| Input | 5 | 2, 8, 9, 12, 15 | Sinh viên 3, AI tự phát hiện 2 |
| Giới hạn công cụ | 14 | 1, 3, 7, 10, 11, 13, 14, 16, 18, 19, 20, 21, 22, 23 | Sinh viên 10, AI tự phát hiện 2, phiên điều phối 2 |
| Độ phức tạp | 5 | 4, 5, 6, 17, 24 | Sinh viên 2, AI tự phát hiện 1, phiên điều phối 1, AI tự phát hiện ở S8 1 |
| **Tổng** | **24** | | |

Nhận xét:

- **Input:** Có hai nguồn. (1) Giả định chưa chốt khi AI làm bản gốc (dòng 2, 8, 9): Khi đã có thông tin, AI tự sửa được, 2 trong 3 dòng này do AI tự bổ sung ngay sau khi sinh viên chốt A07 (a), A10 (a). (2) Prompt S3 chỉ giao quy tắc Minimum Set, không nêu tiêu chí tách lớp bất thường và không yêu cầu ma trận truy vết (dòng 12, 15).
- **Giới hạn công cụ** chiếm đa số và không tự hết khi input đã đủ. Các kiểu lặp lại: Gộp lớp không có căn cứ (dòng 1); áp quy tắc của slide máy móc (dòng 18, 19, 20); bỏ qua ghi chú đã có ở bước trước (dòng 3, 21); không xét giới hạn của kết quả mong đợi (dòng 13, 23); suy luận sai trên chính quy tắc mình mô tả (dòng 7).
- **Độ phức tạp:** Đặc tả không định nghĩa định dạng email nên phải dựa vào quy tắc HTML5 có nhiều luật con (dòng 4, 5); các dòng còn lại nằm ở chỗ giao nhau giữa các tầng: Chuẩn HTML và trình duyệt (dòng 6, 17), giao diện và API (dòng 24).

### 2.4 Không tính là AI bỏ sót

- TC-REG-78, TC-REG-79 (test bảo mật qua API): Bản AI của S3 đã phủ FR01-R25 qua giao diện bằng TC-REG-08 (EC07) và TC-REG-15 (EC66); việc thêm test qua API là phương án (b) của quyết định 4 ở `03_tc.md` mục 9, sinh viên chọn.
- Các dòng "Quyết định của SV" về giả định (GĐ thành H hoặc KH) và chọn phương án: Bản AI đã nêu đủ phương án để sinh viên chọn.

---

## 3. Bug AI bỏ sót

### 3.1 Từng bug

"Bản AI gốc" là test case có trong `ai_raw/S3_test_cases.md` hoặc `ai_raw/S4_bva.md` (nguồn gốc "AI" ở `05_final_tc.md`).

| Bug | Issue | Test case phát hiện | Nguồn gốc (S5) | Bản AI gốc bắt được | Phần ngoài bản AI gốc |
|---|---|---|---|---|---|
| BUG-FR01-01 | #42 | TC-REG-01, TC-REG-108 | AI, AI | Có | QS02: Sinh viên thử thêm `Test1234!` (mật khẩu của tài khoản mẫu); là dữ liệu bổ sung cho cùng bug |
| BUG-FR01-02 | #43 | TC-REG-90 | AI | Có | Khác biệt D01 đã ghi từ S0 (`00_spec.md` mục 5.1) |
| BUG-FR01-03 | #44 | TC-REG-71, TC-REG-72 | AI, AI | Có | |
| BUG-FR01-04 | #45 | TC-REG-73, TC-REG-80 | AI, AI có SV sửa | Có (TC-REG-73) | Biến thể Email chỉ gồm dấu cách chỉ có ở TC-REG-80 (phiên điều phối đề xuất) |
| BUG-FR01-05 | #46 | TC-REG-75 | AI | Có | |
| BUG-FR01-06 | #47 | TC-REG-74, TC-REG-130 | AI, AI | Có | |
| BUG-FR01-07 | #48 | TC-REG-82; bước kiểm chứng của TC-REG-71, 72, 75, 76, 77, 129 (QS03) | AI có SV sửa; AI | Không trực tiếp | Bản AI gốc không có test case API nào nhắm vào luật Email duy nhất (mục 2.2 dòng 24). Bug lộ ra nhờ TC-REG-82 (phiên điều phối đề xuất) và QS03: AI ghi khi điền nhóm E từ log (`06_results.md`, nhật ký 23:35). Bước kiểm chứng có trong bản AI gốc nhưng được thiết kế để kiểm "không tạo tài khoản", không phải để kiểm trùng email |
| BUG-FR01-08 | #49 | TC-REG-76, TC-REG-77, TC-REG-129 | AI, AI, AI | Có | |
| BUG-FR01-09 | #50 | TC-REG-96 | AI | Có | |
| BUG-FR01-10 | #51 | TC-REG-95 | AI | Có | |
| BUG-FR01-11 | #52 | TC-REG-92 | AI | Có | |
| BUG-FR01-12 | #53 | TC-REG-93 | AI | Có | |
| BUG-FR01-13 | #54 | TC-REG-91 | AI | Có | Phần bong bóng "Please fill out this field." thấy khi chạy TC-REG-30; sinh viên quyết định tính vào FR01-R14 (`06_results.md`, nhật ký 23:02) |

QS01 (bong bóng đè lên nút "Đăng Ký") không thành bug (`bugs/bug_report.md`, mục "Quan sát ngoài test case").

### 3.2 Kết luận

- Bản AI gốc bắt được 12 trong 13 bug. Bug duy nhất bản AI gốc bỏ sót là **BUG-FR01-07** (API cho tạo nhiều tài khoản cùng một Email), do cách chọn test case API (mục 2.2 dòng 24).
- Không bug nào tìm được nhờ test case sinh viên tự thêm: TC-REG-131 (nguồn gốc "SV thêm" duy nhất) chưa chạy.
- Phần ngoài bản AI gốc đóng góp: 1 bug (BUG-FR01-07, nhờ TC-REG-82 và QS03), 1 biến thể của bug (BUG-FR01-04, nhờ TC-REG-80), dữ liệu bổ sung cho BUG-FR01-01 (QS02), và một phần của BUG-FR01-13 (bong bóng tiếng Anh).

### 3.3 Kết quả theo nguồn gốc test case

| Nguồn gốc | Số TC | Pass | Fail | Blocked | Not run |
|---|---|---|---|---|---|
| AI | 70 | 8 | 17 | 14 | 31 |
| AI có SV sửa | 25 | 1 | 2 | 4 | 18 |
| SV thêm | 1 | 0 | 0 | 0 | 1 |
| **Tổng** | **96** | **9** | **19** | **18** | **50** |

Đếm bằng cách ghép cột nguồn gốc của `05_final_tc.md` với cột trạng thái của `06_results.md` mục 4; tổng khớp `06_results.md` mục 5. 19 trong 26 test case không phải "AI" chưa chạy, nên con số "12 trong 13 bug" không cho biết phần review bổ sung có tìm thêm được bug hay không (mục 4.2).

---

## 4. Giới hạn của kết quả

### 4.1 Pass không chứng minh luật được cài đúng

| Test case | Vì sao Pass chưa đủ |
|---|---|
| TC-REG-50, TC-REG-56, TC-REG-107 | Mật khẩu yếu bị giao diện từ chối đúng như mong đợi, nhưng mật khẩu hợp lệ `Abcdef1!` cũng nhận cùng thông báo (TC-REG-01, BUG-FR01-01). Pass không cho biết giao diện có kiểm đúng từng điều kiện FR01-R06 đến FR01-R10 hay từ chối mọi mật khẩu |
| TC-REG-30, TC-REG-32, TC-REG-49 | Pass nhờ bong bóng bắt buộc nhập của trình duyệt, không phải kiểm tra của EShop. Qua API, các giá trị rỗng này đều được nhận (BUG-FR01-03, 04, 05) |
| TC-REG-70 | Chỉ kiểm được body phản hồi không chứa mật khẩu; việc mật khẩu có lưu dạng plaintext hay không (FR01-R23) không quan sát được (GH5) |
| TC-REG-94 | Thứ tự Tab trong form đúng, nhưng ảnh không cho thấy các mục trên navbar có được focus hay không (`06_results.md` mục 4, ghi chú TC-REG-94) |

### 4.2 Test case Not run

50 trong 96 test case không chạy, lý do: Sinh viên không đủ thời gian (`06_results.md` mục 4, 5):

| Nhóm | Số TC | Test case |
|---|---|---|
| B. Không hợp lệ qua giao diện | 15 | TC-REG-40 đến 44, 46, 47, 48, 51 đến 55, 57, 58 (ghi mức ưu tiên 2) |
| C. Hợp lệ qua giao diện | 17 | TC-REG-02 đến TC-REG-18 |
| D. Giá trị biên qua giao diện | 18 | TC-REG-102, 103, 106, 110 đến 123, 131 |

Hệ quả cho gap analysis:

- Gần hết các lớp do review bổ sung (EC54 đến EC70) chưa được kiểm: Các test case giao diện phủ chúng đều Not run, trừ TC-REG-39 (Blocked). Riêng EC67 có kết quả qua API (TC-REG-82 Fail).
- Các test case hợp lệ qua giao diện (nhóm C) đều cần một mật khẩu hợp lệ được giao diện chấp nhận, nên khi chạy có thể cũng bị BUG-FR01-01 chặn; kết quả thật của chúng chưa biết.

### 4.3 Test case Blocked

18 test case Blocked (`bugs/bug_report.md`, bảng "Test case Blocked và bug gây chặn"): Có 14 test case do BUG-FR01-01 (TC-REG-31, 33 đến 39, 45, 78, 79, 81, 101, 104), 4 do BUG-FR01-02 (TC-REG-59 đến 62). Vì vậy các luật định dạng Email (FR01-R04) và Email duy nhất (FR01-R05) chưa được kiểm qua giao diện, và FR01-R11, FR01-R12 (Xác nhận mật khẩu) không kiểm được.

### 4.4 Tiền đề thiết kế không còn đúng khi chạy

- Ô Email là `type="text"` (TC-REG-96). Giới hạn GH2 (trình duyệt tự cắt khoảng trắng) không áp dụng, nên TC-REG-11, 33, 48 kiểm hành vi của chính EShop. Tiền đề của giả định A15 (b) (trình duyệt chuyển tên miền có dấu sang punycode) cũng không còn, nên TC-REG-14, 121, 122 cần xem lại trước khi chạy (`06_results.md` mục 4, ghi chú các dòng này).
- Bước kiểm chứng "đăng ký lại cùng email" dựa vào FR01-R05 (`01_io.md` mục 3.4). Vì API cho tạo trùng email (BUG-FR01-07), bước này không còn phân biệt được request trước có tạo tài khoản hay không. Ở S6, kết luận "đã tạo tài khoản" dựa vào `id` trong phản hồi của chính request đó.

### 4.5 Phạm vi chạy

Một lần chạy ngày 20/10/2026, Windows 11, Google Chrome 155.0.8059.85, EShop commit `85af3ba` (`06_results.md` mục 1). Kết quả qua giao diện có thể khác trên trình duyệt khác.

---

## 5. Bài học khi làm việc với AI trong feature này

1. **Chốt giả định và nêu đủ yêu cầu trong prompt trước khi giao bước tiếp theo.** Lỗi do input tự hết khi AI có thông tin: AI tự bổ sung EC67, EC68 ngay sau khi có A07 (a), A10 (a) (và EC62, EC63 sau khi có A04 (b)). Nên đưa các nguyên tắc chung (như nguyên tắc khoảng trắng) vào prompt ngay từ đầu bước chia lớp; ở bước chọn test case, nêu rõ yêu cầu ma trận truy vết và tiêu chí tách lớp bất thường (dòng 12, 15).
2. **Hỏi "vì sao" cho từng lớp và từng điểm biên.** Lỗi do giới hạn công cụ chiếm đa số (14 trong 24 dòng) và vẫn còn khi input đã đủ. Phần lớn (10 dòng) bị phát hiện qua câu hỏi cụ thể của sinh viên, như "Vì sao EC06 gộp chữ số và dấu câu", "TC-REG-105 vi phạm mấy điều kiện".
3. **Cho một phiên AI khác soát lại.** Phiên điều phối thấy những chỗ phiên thiết kế bỏ qua (hành vi trình duyệt, tác dụng phụ của test case). Test case nó đề xuất là test case duy nhất nhắm thẳng vào bug mà bản AI gốc bỏ sót (TC-REG-82, BUG-FR01-07).
4. **Chạy trước test case hợp lệ cơ sở và các kiểm tra rẻ.** Thiết kế dùng chung một mật khẩu cơ sở và bước kiểm chứng qua giao diện, nên một bug (BUG-FR01-01) chặn 14 test case. Chạy TC-REG-01 và TC-REG-96 trước như một bước kiểm tra nhanh sẽ cho biết sớm cần đường kiểm chứng thay thế (ví dụ qua API) và tiền đề nào (`type="email"`) đã sai.
5. **Đối chứng mỗi Pass với một trường hợp hợp lệ.** TC-REG-50, 56, 107 Pass trong khi giao diện từ chối cả mật khẩu hợp lệ; TC-REG-30, 32, 49 Pass nhờ trình duyệt trong khi API nhận giá trị rỗng. Khi đọc kết quả do AI điền, không coi Pass là bằng chứng luật được cài đúng nếu chưa có trường hợp hợp lệ tương ứng.

---

## 6. Thay đổi so với bản AI (`ai_raw/S8_gap_analysis.md`)

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 2.2 dòng 4, 5 | Nguyên nhân từ Input thành Độ phức tạp; viết lại cột Căn cứ | Quyết định của SV | Đặc tả không định nghĩa định dạng email; các lớp EC57 đến EC63 đến từ quy tắc HTML5 có nhiều luật con |
| Mục 2.2 dòng 15 | Nguyên nhân từ Giới hạn công cụ thành Input; viết lại cột Căn cứ | Sai | Prompt S3 không yêu cầu ma trận truy vết và không giao skill `test-case-writing`. Bản AI suy ra "Giới hạn công cụ" từ câu "skill `test-case-writing` yêu cầu ma trận này" mà không biết skill đó có được giao hay không. Sinh viên phát hiện |
| Mục 2.2 dòng 24; mục 2.3 | Người phát hiện "AI khi viết S8" thành "AI tự phát hiện ở S8" | Mơ hồ | Sinh viên yêu cầu ghi rõ |
| Mục 2.1 | Tiêu chí của Độ phức tạp thêm trường hợp đặc tả không định nghĩa quy tắc, phải dựa vào chuẩn bên ngoài có nhiều luật con | Quyết định của SV | Hệ quả của dòng 4, 5 |
| Mục 2.3 | Số đếm theo nguyên nhân: Input từ 6 thành 5, Giới hạn công cụ từ 15 thành 14, Độ phức tạp từ 3 thành 5; cập nhật người phát hiện và nhận xét | Quyết định của SV | Hệ quả của các dòng trên |
| Mục 5, ý 1, 2 | Ý 1 thêm bài học về prompt S3 (dòng 12, 15); ý 2 đổi số đếm (14 trong 24 dòng, 10 dòng do sinh viên phát hiện) | Quyết định của SV | Hệ quả của các dòng trên |
