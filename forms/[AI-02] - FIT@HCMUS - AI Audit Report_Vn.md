> Bản text-based của `[AI-02] - FIT@HCMUS - AI Audit Report_Vn.docx` (bản binary: .docx / .pdf cùng tên).

Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)

CS423 / CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)

CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0

# AI Audit Report — Mẫu 5 mục cho mỗi Artifact

Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).

Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.

## 1. Thông tin Sinh viên

| Mục | Giá trị |
|---|---|
| Họ tên sinh viên (in hoa): | NGUYỄN THỊ ÁNH NGỌC |
| MSSV: | 23120061 |
| Lớp / Khoá: | Kiểm thử phần mềm - CQ2023/3 |
| Mã bài tập (ví dụ HW#00, HW#02): | HW02-AI |
| Ngày làm bài: | 12/10/2026 đến 21/10/2026 |
| Công cụ AI đã dùng: | Claude Code (Anthropic, claude-opus-5-5) |
| Công cụ AI đã dùng: | [x] Có  [ ] Không |

## 2. Hướng dẫn (đọc trước khi điền)

- Thêm 1 hàng cho mỗi artifact AI sinh (test case, script, checklist, OpenAPI spec, JMeter plan…).

- Dán nguyên văn prompt — KHÔNG paraphrase.

- Dán nguyên văn output AI (hoặc kèm screenshot có chú thích trong báo cáo).

- Gắn nhãn: VALID / INVALID / INCOMPLETE.

- Lý do phải dẫn chiếu slide, mục ISTQB, hoặc RFC kỹ thuật.

- Hiển thị bản sửa với phần thay đổi được tô sáng.

- Hàng mẫu in nghiêng — thay trước khi nộp.

## 3. Bảng Audit — 1 hàng / artifact

| (1) Prompt + Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |
|---|---|---|---|---|
| B01: Kế hoạch làm bài, cấu trúc thư mục, WORKFLOW.md <br> Claude Code, phiên điều phối 305c705a, 12/10/2026 đến 19/10/2026 | Phân tích đề, quy trình S0 đến S8, quy tắc hộp đen, quy tắc ai_raw/ và bảng thay đổi | INCOMPLETE | Hướng dẫn S0 ban đầu mâu thuẫn ("chỉ quan sát" nhưng có câu hỏi buộc nhập thử); chưa có quy tắc cấm DevTools ở S0 đến S5 và quy tắc không sửa ai_raw/ | Thêm quy tắc không DevTools ở S0 đến S5, bản AI viết lại lưu _v2, cột Loại và người phát hiện trong bảng thay đổi |
| B02: Script tools/export_prompt_log.py <br> Phiên điều phối, 17/10/2026; sửa 20/10/2026 | Xuất transcript các phiên trong danh sách trắng ra prompt_log.md | INCOMPLETE | Kiểm khi chạy thật: Bản tóm tắt ngữ cảnh do hệ thống tự tạo khi nén phiên bị xuất thành một prompt như thể sinh viên gõ | Phiên điều phối tự phát hiện khi soát log; bỏ dòng isCompactSummary |
| B03: FR-01, S0 đến S4 (bản AI) <br> Phiên 38378bef, 19/10/2026 đến 20/10/2026 | ai_raw/S0_khao_sat.md đến ai_raw/S4_bva.md | INCOMPLETE | 34 chỗ chưa đúng: 27 Thiếu, 6 Thừa, 1 Sai (ví dụ: Áp đủ 9 điểm BVA cho phân vùng không có cận trên; đại diện vi phạm 2 điều kiện; thiếu test case API cho khoảng trắng của Email); AI đề xuất dùng DevTools ở S0 dù đã được dặn hộp đen; AI sửa luôn file ai_raw khi được yêu cầu sửa bản review | Bản review 00_spec.md đến 04_bva.md, mỗi file có bảng thay đổi; khôi phục ai_raw/S0 và lưu bản sửa thành _v2 |
| B04: FR-01, S5 bộ test case cuối <br> Phiên 38378bef, 20/10/2026 | ai_raw/S5_final_test_cases.md (96 test case) | INCOMPLETE | Thiếu cột người phát hiện trong bảng chính dù sinh viên đã chọn phương án có cột này | Thêm cột "Phát hiện" |
| B05: FR-01, S6 khung kết quả, script API, điền kết quả <br> Phiên 38378bef, 20/10/2026 | 06_results.md, scripts/run_api_tests.py, scripts/run_tc79.py; điền kết quả từ ảnh và log | INCOMPLETE | Script chạy đúng. Khi điền kết quả, AI ghi câu hỏi và đề xuất vào ô kết quả, thêm chữ "(đề xuất)" ở trạng thái; ghi sai giờ một dòng nhật ký | Sinh viên yêu cầu ô kết quả chỉ ghi sự kiện; phiên điều phối sửa giờ nhật ký, điền mục tổng hợp, sửa mô tả vai trò ở đầu file cho đúng thực tế |
| B06: FR-01, S7 bug report, trang link tạo issue <br> Phiên 38378bef, 21/10/2026 | 13 bug trong bugs/bug_report.md, nội dung theo template issue của nhóm | INCOMPLETE | Gom 19 Fail thành 13 bug đúng; bug API chỉ có log, chưa có ảnh; chú thích ảnh ở #42 đặt sai chỗ | Sinh viên chụp 11 ảnh log, quyết định mức độ và gắn label, tự tạo 13 issue |
| B07: FR-01, S8 gap analysis <br> Phiên 38378bef, 21/10/2026 | ai_raw/S8_gap_analysis.md | INCOMPLETE | Số liệu đúng (phiên điều phối đếm lại); xếp nhầm nguyên nhân 3 dòng | Dòng 15 đổi thành Input; dòng 4, 5 đổi thành Độ phức tạp |
| B08: Agent Skill domain-testing-design <br> Phiên 38378bef, 20/10/2026 | SKILL.md, references/, assets/, scripts/check_step.py | VALID | Chạy được trên FR-17, FR-07, FR-04; script kiểm bắt được lỗi định dạng và lớp không có test case. Một lần phiên dùng skill vẫn chạy lệnh đọc file ghi chú bị cấm (kết quả bị cắt, AI không thấy nội dung) | Giữ nguyên |
| B09: FR-17, S1 đến S4 (bản AI, qua skill) <br> Phiên 1648c211, 20/10/2026 | ai_raw/S1_input_output.md đến ai_raw/S4_bva.md | INCOMPLETE | 21 Thiếu, 4 Mơ hồ (ví dụ: Thiếu biến gián tiếp của thao tác Xóa, thiếu lớp request không phải JSON, thiếu điểm 2^53 + 1 qua API) | Bản review có bảng thay đổi; thêm các lớp và test case theo câu hỏi của sinh viên |
| B10: FR-17, S5 bộ test case cuối <br> Phiên 1648c211, 20/10/2026 | ai_raw/S5_final_test_cases.md (113 test case) | INCOMPLETE | Gán quyền admin của GET cho FR-12 (sai căn cứ); thiếu API cho khoảng trắng của code; thiếu kiểm danh sách dài | Thêm giả định A28, TC-CPN-143, 144; sinh viên thêm TC-CPN-140 đến 142 (ô tự viết hoa) |
| B11: FR-17, S6 script API, điền kết quả <br> Phiên 1648c211, 21/10/2026 | scripts/run_api_tests.py; 06_results.md điền từ 21 ảnh và 3 log | INCOMPLETE | Script chạy đúng, che token trong log, không xóa dữ liệu mẫu. Bảng điền đúng nhưng để trống ô ở mục 1 và cột kết quả của dòng Not run, ghi giờ nhật ký không cụ thể | Phiên điều phối điền ô trống, ghi giờ cụ thể theo yêu cầu của sinh viên |
| B12: FR-17, S7 bug report <br> Phiên 1648c211, 21/10/2026 | 9 bug, 6 dòng Khác giả định chờ quyết định | INCOMPLETE | Gộp hai lỗi khác giao diện vào một bug; đề xuất gộp hành vi dựa trên giả định vào bug Critical | Sinh viên tách BUG-04, KG01, KG02 thành bug, KG03 chỉ ghi chú; tự tạo 12 issue |
| B13: FR-17, S8 gap analysis <br> Phiên 1648c211, 21/10/2026 | ai_raw/S8_gap_analysis.md | VALID | Số liệu đúng (phiên điều phối đếm lại: 72 dòng); cách xếp nguyên nhân có căn cứ | Giữ nguyên |
| B14: FR-07, S0 đến S5 (bản AI, qua skill) <br> Phiên 709e0d24, 21/10/2026 | ai_raw/S0_khao_sat.md đến ai_raw/S5_final_test_cases.md (32 lớp, 38 test case) | INCOMPLETE | Thiếu output "phản hồi trực quan sau khi bấm Thêm vào giỏ" (FR-24), do phiên điều phối phát hiện; AI điền bảng quan sát S0 từ ảnh thay cho sinh viên (đã tự ghi chú việc này); AI tự sửa 3 lỗi trước khi giao (ví dụ mốc "không tạo được đúng 1 tỷ" ở S4); một lần tự suy rộng quyền đọc file S5 của FR-01, FR-17 để lấy định dạng | Thêm FR07-R33 và OUT15; các phương án nhỏ sinh viên chấp nhận theo đề xuất để kịp giờ |
| B15: FR-07, S6 đến S8 (script API, điền kết quả, bug report, gap analysis) <br> Phiên 709e0d24, 21/10/2026 | scripts/run_api_tests.py, 06_results.md, mục FR-07 của bugs/bug_report.md (18 bug), 08_gap_analysis.md | VALID | Script không xóa giỏ, không reset, che token; phiên không tự reset dữ liệu mà chờ phiên điều phối (đúng WORKFLOW); bug gom theo yêu cầu, số liệu S8 đúng (phiên điều phối đếm lại: 25 dòng) | Sinh viên chọn giữ riêng 18 bug, tự tạo 18 issue; điền "Không chạy" và giờ reset theo yêu cầu |
| B16: FR-04, S0 đến S5 (bản AI, qua skill, có quay video) <br> Phiên 633ed316, 21/10/2026 | ai_raw/S0_khao_sat.md đến ai_raw/S5_final_test_cases.md (38 lớp, 34 test case) | INCOMPLETE | 3 lỗi, đều do AI tự phát hiện: Tham chiếu sai cột ở S2, giờ tạo ghi ước lượng ở S3, ma trận truy vết S3 thiếu TC-PROF-71; giả định A16 bỏ qua ngữ nghĩa của PUT (lộ ra ở S7); không có phương án dự phòng khi giá trị cơ sở bị từ chối. AI hỏi xin phép trước khi đọc file của FR-01 | Sửa ở bản review từng bước; các phương án nhỏ sinh viên chấp nhận theo đề xuất để kịp giờ |
| B17: FR-04, S6 đến S8 (script API, hướng dẫn chạy trên điện thoại, điền kết quả, bug report, gap analysis) <br> Phiên 633ed316, 21/10/2026 | scripts/run_api_tests.py (lệnh chuan, get, run, last), 06_results.md, mục FR-04 của bugs/bug_report.md (5 bug), 08_gap_analysis.md | INCOMPLETE | Script đúng, che token và mật khẩu; nhưng hướng dẫn S6 dùng lệnh adb không có trong PATH của PowerShell, hàm shot lưu ảnh JPG với đuôi .png, và bảo sinh viên tự khởi động lại backend; S7 ghép issue theo tiêu đề trong ảnh, S8 số liệu đúng (phiên điều phối đếm lại: 38 dòng) | Phiên điều phối sửa hướng dẫn S6 (đường dẫn adb đầy đủ, kéo ảnh và đặt tên giúp, tự reset); sinh viên tự tạo 5 issue |
| B18: Phiên điều phối: Soạn tin nhắn, soát phiên, đếm lại số liệu <br> Phiên 305c705a, 17/10/2026 đến 21/10/2026 | Tin nhắn cho các phiên thiết kế, bảng tình trạng, đề xuất phương án | INCOMPLETE | Có lần ghi nhầm người phát hiện; có lần đưa danh sách commit không kiểm git log trước; một lần grep API_URL trong mã nguồn app mobile để xác nhận cấu hình chạy (không dùng cho thiết kế); có lần ghi đè file Excel thật mà chưa kiểm; có lần phân loại sai một quan sát | Sinh viên phát hiện và yêu cầu sửa; từ đó gắn sẵn người phát hiện vào tin nhắn, kiểm thời gian sửa trước khi ghi đè |
| B19: tools/md_to_pdf.py, tools/fill_ai02.py, tools/fill_ai03_05.py, khung report.md, README <br> Phiên điều phối, 21/10/2026 | Script xuất PDF cho mọi file MD; khung báo cáo, Test Summary, bản nháp AI Critique, Mandatory Disclosure, Appendix B | INCOMPLETE | Khung và số liệu dùng được (số liệu đếm lại từ file của từng feature); bản nháp AI Critique chưa có ý về việc AI dựa vào trí nhớ thay vì kiểm tra lại; phần Kết luận và điểm tự chấm để trống cho sinh viên | Sinh viên bổ sung AI Critique (AI áp dụng máy móc, AI dựa vào trí nhớ thay vì kiểm tra), tự viết Kết luận, điền tự chấm, thay mục lục |

## 4. Tổng kết Độ chính xác AI

Tổng hợp verdict từ Mục 3 và điền vào bảng dưới.

| Chỉ số | Số lượng | Tỉ lệ |
|---|---|---|
| Tổng artifact AI sinh đã audit | 19 | 100% |
| VALID (đúng, dùng nguyên) | 3 | 15.8% |
| INVALID (sai; loại bỏ) | 0 | 0.0% |
| INCOMPLETE (chấp nhận sau khi sửa) | 16 | 84.2% |

## 5. Kết luận — Khi nào nên / không nên dùng AI?

Viết 80–150 chữ mô tả pattern quan sát được. AI mạnh ở đâu? AI sai ở đâu? Khuyến nghị của bạn cho việc dùng AI trong loại công việc này?

AI mạnh trong việc lên kế hoạch, điều phối, đồng thời vì nắm rõ ngữ cảnh nên các đề xuất cũng phù hợp. Tuy nhiên AI cũng không thể bao phủ hết các test case, cũng chưa nghĩ tới trường hợp ngoại lệ khác vì không thể thao tác trực tiếp và cũng không nắm rõ quy trình hành vi người dùng.

## 6. Mandatory Disclosure (dán nguyên văn)

"Tôi dùng AI (Claude Code, Anthropic, claude-opus-5-5) cho các việc sau: Trích đặc tả, đề xuất biến Input và Output, lớp tương đương, test case Domain Testing và BVA cho 4 feature (bản gốc của AI lưu nguyên văn trong `ai_raw/` của từng feature); viết script chạy test API; điền bảng kết quả S6 theo ảnh và log do tôi chạy và chụp; viết nháp bug report, nội dung issue và trang link tạo issue; viết nháp AI gap analysis; viết Agent Skill `domain-testing-design`; viết `WORKFLOW.md`, các script trong `tools/`, khung báo cáo, README, bản nháp AI Critique và Appendix B. Một phiên Claude Code làm điều phối: Đọc các phiên khác, soát thao tác bị cấm, soạn tin nhắn để tôi gửi cho các phiên thiết kế, xuất prompt log. Tôi review và quyết định ở mọi bước (các bảng "Thay đổi so với bản AI" ghi đủ chỗ tôi sửa và người phát hiện); tôi tự chụp ảnh khảo sát và kết quả chạy test, tự chạy script, tự tạo toàn bộ issue trên GitHub, tự commit; các quyết định chọn phương án là của tôi, một số có tham khảo đề xuất của AI. AI Audit Report chi tiết ở Appendix B."

## Chữ ký

| Họ tên sinh viên (in hoa): | NGUYỄN THỊ ÁNH NGỌC |
|---|---|
| MSSV: | 23120061 |
| Lớp / Khoá: | Kiểm thử phần mềm - CQ2023/3 |
| Môn học: | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| Giảng viên: | Lâm Quang Vũ <br> Hồ Tuấn Thanh <br> Trương Phước Lộc |
| Ngày: | 21/10/2026 |
| Chữ ký: | *(Ảnh chữ ký: Xem bản PDF)* |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.

- ISTQB Foundation Level Syllabus (latest version).

- Hardman, P. (2025). A Post-AI Learning Taxonomy.

- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.

- Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.

- Anthropic (2025). Building reliable AI test agents — engineering blog.

- DeepEval & Promptfoo documentation — testing frameworks for LLM systems.
