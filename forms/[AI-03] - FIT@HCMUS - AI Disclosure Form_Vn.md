> Bản text-based của `[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.docx` (bản binary: .docx / .pdf cùng tên).

Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)

CS423 / CSC15003 – Kiểm chứng Phần mềm (AI-augmented · 2026)

CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0

# Biểu mẫu Khai báo Sử dụng AI

Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.

Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.

## 1. Thông tin Môn học & Sinh viên

| Mục | Giá trị |
|---|---|
| Môn học: | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| Mã bài tập: | HW02-AI |
| Tên bài tập: | Domain Testing on EShop (Domain Testing và Boundary Value Analysis cho FR-01, FR-07, FR-17, FR-04) |
| Cấp độ AI (1–5): | Cấp 4 – AI hỗ trợ sản xuất |
| Ngày: | 21/10/2026 |
| Họ tên sinh viên: | Nguyễn Thị Ánh Ngọc |
|  |  |
| MSSV: | 23120061 |

## 2. Câu hỏi Khai báo

### 1. Công cụ AI đã dùng:

Liệt kê mọi công cụ AI dùng cho bài tập này (ví dụ AI Tool (e.g., ChatGPT, Claude, Gemini), ChatGPT, GitHub Copilot, Cursor, Gemini).

Claude Code (Anthropic, claude-opus-5-5), chạy trong VS Code: 1 phiên điều phối (305c705a) và 4 phiên thiết kế (FR-01: 38378bef; FR-17: 1648c211; FR-07: 709e0d24; FR-04: 633ed316). Không dùng công cụ AI nào khác.

### 2. Giai đoạn nào của bài tập có dùng AI:

Tick: [x] brainstorm  [x] outline  [x] viết nháp  [x] phản hồi  [x] sửa chữa  [x] code  [x] phân tích dữ liệu  [ ] thiết kế đồ hoạ  [x] khác (ghi rõ).

Khác: Thiết kế test case Domain Testing và BVA theo từng bước của slide S04 (bản gốc của AI lưu trong ai_raw/ của từng feature); điền bảng kết quả S6 theo ảnh và log do sinh viên chạy; viết nháp bug report và trang link tạo issue; điều phối nhiều phiên và soát thao tác bị cấm. Code: Script chạy test API, script xuất prompt log, xuất PDF, điền form, Agent Skill domain-testing-design. Phân tích dữ liệu: Đếm bảng "Thay đổi so với bản AI" cho AI gap analysis (S8).

### 3. Prompt / nhiệm vụ chính cho AI:

Dán nguyên văn 2–3 prompt quan trọng nhất. Để xem đầy đủ, đính kèm Phụ lục A (prompt_log.md).

(1) C255 – Claude Code – 06:47 21/10/2026 (gọi Agent Skill cho FR-04, có quay video): "/domain-testing-design Feature D, FR-04 Quản lý hồ sơ cá nhân trên Mobile (app EShop chạy bằng Expo Go trên Android, Samsung Galaxy S21 Ultra), thư mục Homeworks/HW02/features/D_FR-04_HoSo_Mobile/. Lưu ý: Bắt đầu từ S0. [...] Tuân thủ WORKFLOW.md: Hộp đen, không đọc mã nguồn EShop, không đọc file của feature khác trừ khi tôi cho phép."

(2) C121 – Claude Code – 15:55 20/10/2026 (gọi Agent Skill cho FR-17): "/domain-testing-design Feature C, FR-17 Quản lý mã giảm giá trên Web Admin (http://localhost:5174) [...] Ở S0 tôi có nhập thử vài trường hợp; kết quả được cất riêng, không cung cấp. Không hỏi về kết quả này, thiết kế như thể chưa biết."

(3) C160 – Claude Code – 22:09 20/10/2026 (review S5 của FR-17): "Bạn hãy kiểm tra lại các ý sau. Tôi đang thắc mắc, cảm thấy sai sai khi đọc bài của bạn chứ cũng chưa chắc đúng 100%, hãy kiểm chứng: Xem lại giúp tôi logic endpoint [...] Chưa có API kiểm tra cắt khoảng trắng đầu/cuối [...]"

Toàn bộ prompt có timestamp, nguyên văn: Phụ lục A (prompt_log.md).

### 4. Phần cụ thể AI đóng góp:

Càng cụ thể càng tốt. Ví dụ: 'AI sinh TC01–TC15 ở Mục 3.2; tôi viết lại TC04 và TC11; AI KHÔNG đóng góp vào Mục 1, 2, 4, hoặc AI Critique.'

Với cả 4 feature: AI viết bản gốc của S0 đến S5 (trích đặc tả, biến Input/Output, lớp tương đương, test case Domain Testing, BVA, bộ test cuối; lưu nguyên văn trong ai_raw/), script chạy test API, điền bảng kết quả S6 từ ảnh và log của sinh viên, nháp bug report, nháp AI gap analysis (S8). Khác: WORKFLOW.md, Agent Skill domain-testing-design, các script trong tools/, khung report.md và README, nháp AI Critique, Mandatory Disclosure, Phụ lục B. AI KHÔNG đóng góp vào: Ảnh khảo sát và ảnh chạy test (sinh viên chụp), việc chạy test và script, 48 issue trên GitHub (sinh viên tự tạo), các quyết định chọn phương án ở từng bước, phần Kết luận của Phụ lục B, điểm tự chấm. Chi tiết từng artifact: AI Audit Report (Phụ lục B của report.md, B01 đến B19).

### 5. Cách tôi rà soát / chỉnh sửa / xác minh đầu ra AI:

Mô tả phương pháp xác minh (chạy test, kiểm tra spec, hỏi TA, tra RFC, đối chiếu ISTQB syllabus, v.v.).

Mỗi bước review bản AI và ghi mọi chỗ sửa vào bảng "Thay đổi so với bản AI" (Loại: Sai, Thiếu, Thừa, Mơ hồ, Quyết định của SV; kèm người phát hiện); đối chiếu với đặc tả EShop (README, API spec) và slide S04; chạy script check_step.py để kiểm mọi lớp có test case phủ và định dạng; chạy test thật trên Web, Web Admin và điện thoại để kiểm kết quả mong đợi; một phiên Claude riêng làm điều phối, đọc transcript để soát thao tác bị cấm (đọc mã nguồn, đọc ghi chú điều phối) và đếm lại số liệu S8; giữ toàn bộ prompt trong prompt log. Kết quả rà soát: Phụ lục B (VALID, INCOMPLETE, INVALID).

### 6. Trích dẫn (nếu môn yêu cầu):

Môn Kiểm chứng Phần mềm dùng phong cách IEEE. Ví dụ: Anthropic. (2026). AI Tool (e.g., ChatGPT, Claude, Gemini) [Large language model]. https://claude.ai

[1] Anthropic, "Claude Code (claude-opus-5-5)," [Large language model], 2026. [Online]. Available: https://claude.ai

## 3. Cam đoan Trung thực

Bằng việc ký tên dưới đây, tôi cam đoan thông tin khai báo ở trên là chính xác và đầy đủ. Tôi hiểu rằng việc không khai báo hoặc khai báo sai lệch về việc dùng AI sẽ bị coi là vi phạm liêm chính học thuật và có thể dẫn đến điểm 0 cho bài tập cùng việc bị chuyển lên hội đồng kỷ luật.

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

Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.

ISTQB Foundation Level Syllabus (latest version).

Hardman, P. (2025). A Post-AI Learning Taxonomy.

Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.

Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.

Anthropic (2025). Building reliable AI test agents — engineering blog.

DeepEval & Promptfoo documentation — testing frameworks for LLM systems.
