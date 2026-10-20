# HW02-AI: Domain Testing trên EShop

| | |
|---|---|
| MSSV | 23120061 |
| Họ tên | Nguyễn Thị Ánh Ngọc |
| Lớp | Kiểm thử phần mềm - CQ2023/3 |
| Môn học | CS423 / CSC15003 - Software Testing |
| Bloom-AI | G9.2 (Apply), G9.3 (Analyse) |
| Công cụ AI | Claude Code (Anthropic, claude-opus-5-5) |
| SUT | [EShop](https://github.com/ttbhanh/eshop-sut), commit `85af3ba` |
| Repo nhóm (GitHub Issues) | https://github.com/angquoc/software-testing-2026-HW02-group |
| Ngày nộp | 21/10/2026 |

> Báo cáo này là bản tổng hợp. Chi tiết từng bước của mỗi feature nằm trong thư mục `features/<feature>/`, mỗi bước một file và có bản gốc của AI trong `ai_raw/`. Các đường dẫn bên dưới tính từ thư mục gốc của bài.

## Mục lục

1. [Cách làm](#1-cách-làm)
2. [Feature A: FR-01 Đăng ký tài khoản (Web)](#2-feature-a-fr-01-đăng-ký-tài-khoản-web)
3. [Feature B: FR-07 Giỏ hàng (Web)](#3-feature-b-fr-07-giỏ-hàng-web)
4. [Feature C: FR-17 Quản lý mã giảm giá (Web Admin)](#4-feature-c-fr-17-quản-lý-mã-giảm-giá-web-admin)
5. [Feature D: FR-04 Hồ sơ cá nhân (Mobile)](#5-feature-d-fr-04-hồ-sơ-cá-nhân-mobile)
6. [Agent Skill](#6-agent-skill)
7. [Test Summary](#7-test-summary)
8. [AI Critique](#ai-critique)
9. [Mandatory Disclosure](#mandatory-disclosure)
10. [Self-Assessment](#self-assessment)
11. [Appendix A: Prompt log](#appendix-a-prompt-log)
12. [Appendix B: AI Audit Report](#appendix-b-ai-audit-report)

---

## 1. Cách làm

### 1.1 Quy trình cho mỗi feature

Quy trình đầy đủ ở [`WORKFLOW.md`](WORKFLOW.md). Mỗi bước có một commit cho bản AI và một commit cho bản sinh viên review.

| Bước | Nội dung | Ai làm | File |
|---|---|---|---|
| S0 | Trích đặc tả, khảo sát giao diện qua ảnh chụp | AI trích, sinh viên chụp ảnh | `00_spec.md` |
| S1 | Bước 1 của slide S04: Xác định biến Input, Output | AI đề xuất, sinh viên review | `01_io.md` |
| S2 | Bước 2: Lớp tương đương hợp lệ và không hợp lệ theo guideline | AI đề xuất, sinh viên review | `02_ec.md` |
| S3 | Bước 3: Bảng phủ lớp, Minimum Set (mỗi test case không hợp lệ chỉ vi phạm 1 lớp) | AI đề xuất, sinh viên review | `03_tc.md` |
| S4 | Bước 4: Boundary Value Analysis (LB-1, LB, LB+1, UB-1, UB, UB+1, nhỏ nhất và lớn nhất giao diện cho nhập), chỉ cho phân vùng có thứ tự | AI đề xuất, sinh viên review | `04_bva.md` |
| S5 | Gộp bộ test case cuối, sinh viên bổ sung test case AI bỏ sót | Sinh viên | `05_final_tc.md` |
| S6 | Chạy test thật, ghi kết quả, chụp ảnh, chạy script API | Sinh viên (AI điền theo ảnh và log) | `06_results.md`, `screenshots/`, `logs/` |
| S7 | Bug report và GitHub Issues | Sinh viên, AI hỗ trợ viết | [`bugs/bug_report.md`](bugs/bug_report.md) |
| S8 | AI gap analysis | Sinh viên, AI hỗ trợ | `08_gap_analysis.md` |

### 1.2 Nguyên tắc

- **Kiểm thử hộp đen.** AI chỉ được dùng đặc tả (README, API spec của EShop) và ảnh sinh viên chụp. Không đọc mã nguồn, không tự mở giao diện, không dùng DevTools từ S0 đến S5. DevTools chỉ dùng ở S6 cho thuộc tính mà đặc tả yêu cầu (thẻ `<h1>`, `type` của ô nhập).
- **Giữ nguyên bản AI.** Mỗi bước, output của AI được lưu nguyên văn trong `ai_raw/` và không sửa. Bản review là file riêng, có bảng **"Thay đổi so với bản AI"** với cột Loại (Sai, Thiếu, Thừa, Mơ hồ, Quyết định của SV) và người phát hiện. Bảng này là dữ liệu cho AI gap analysis (S8).
- **Tách phiên.** Một phiên Claude Code làm điều phối (đọc các phiên khác, soạn tin nhắn, soát thao tác bị cấm, xuất log). Mỗi feature được thiết kế trong một phiên riêng, không thấy ghi chú điều phối, để phần gap analysis phản ánh đúng năng lực của AI. Sinh viên là người gửi mọi tin nhắn và tự commit.
- **Thông tin giữ lại.** Ở FR-17, kết quả nhập thử ở S0 (ô mã tự viết hoa) được cố ý giữ lại, không đưa cho AI, để đo xem AI có tự nghĩ tới không. Sinh viên bổ sung ở S5.

### 1.3 Hai cách tạo test case

- **FR-01 (làm mẫu):** Thiết kế thủ công từng bước trong một phiên Claude Code mới, sinh viên review sâu. Bài học từ FR-01 được đúc thành Agent Skill `domain-testing-design`.
- **FR-17, FR-07, FR-04:** Dùng Agent Skill (mục 6). FR-07 và FR-04 làm gọn hơn vì thời gian: Mỗi bước sinh viên review một lượt.

---

## 2. Feature A: FR-01 Đăng ký tài khoản (Web)

Thư mục: [`features/A_FR-01_DangKy/`](features/A_FR-01_DangKy/)

### 2.1 Domain Testing từng bước

| Bước | Kết quả | File |
|---|---|---|
| S0 Đặc tả | Trích nguyên văn FR-01 và các yêu cầu chung (FR-21 đến FR-24), danh sách yêu cầu có mã `FR01-Rnn`, câu hỏi mở; đối chiếu giao diện: Form không có trường Xác nhận mật khẩu (D01), không có dấu `*`, nút màu đỏ | [`00_spec.md`](features/A_FR-01_DangKy/00_spec.md) |
| S1 Input, Output | 4 biến Input trực tiếp (Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu), 1 biến gián tiếp (danh sách email đã có); Output: Chuyển trang `/login` hoặc thông báo lỗi ERR1 đến ERR7, phản hồi API | [`01_io.md`](features/A_FR-01_DangKy/01_io.md) |
| S2 Lớp tương đương | 70 lớp: 30 lớp Input hợp lệ, 32 lớp Input không hợp lệ, 8 lớp Output. Áp guideline "must be", khoảng giá trị, tập giá trị; giả định A01 đến A15 cho chỗ đặc tả không nói (khoảng trắng, định dạng email theo HTML5, tên miền có dấu) | [`02_ec.md`](features/A_FR-01_DangKy/02_ec.md) |
| S3 Coverage, Minimum Set | Bảng phủ lớp, 72 test case; mỗi test case không hợp lệ chỉ vi phạm 1 lớp; ma trận truy vết yêu cầu | [`03_tc.md`](features/A_FR-01_DangKy/03_tc.md) |

### 2.2 Boundary Value Analysis

7 phân vùng có thứ tự (độ dài Họ Tên, độ dài Mật khẩu, số ký tự mỗi loại trong Mật khẩu, độ dài phần trước `@`, độ dài nhãn tên miền với cận trên 63, tổng độ dài Email, số dấu cách). 24 test case BVA. Không thêm điểm "giữa" cho phân vùng không có cận trên, không xét BVA cho phép so khớp Xác nhận mật khẩu (so sánh bằng, không có thứ tự). Chi tiết: [`04_bva.md`](features/A_FR-01_DangKy/04_bva.md).

### 2.3 Bộ test case cuối và kết quả

- [`05_final_tc.md`](features/A_FR-01_DangKy/05_final_tc.md): **96 test case** (72 Domain Testing, 24 BVA). Nguồn gốc: AI 70, AI có SV sửa 25, SV thêm 1.
- [`06_results.md`](features/A_FR-01_DangKy/06_results.md): Chạy ngày 20/10/2026. Pass 9, Fail 19, Blocked 18, Not run 50. Nhóm API chạy bằng [`scripts/run_api_tests.py`](features/A_FR-01_DangKy/scripts/run_api_tests.py), log trong `logs/`.
- Phát hiện chính: Giao diện từ chối mọi mật khẩu hợp lệ (`Abcdef1!`, `Test1234!`), nên không đăng ký được qua giao diện; ngược lại API nhận mọi dữ liệu sai và cho tạo nhiều tài khoản cùng một email. 18 test case Blocked vì lỗi mật khẩu và vì thiếu trường Xác nhận mật khẩu.

### 2.4 Bug

13 bug, issue **#42 đến #54** (1 Critical, 7 High, 1 Medium, 4 Low). Chi tiết: [`bugs/bug_report.md`](bugs/bug_report.md), mục FR-01.

### 2.5 AI gap analysis

Chi tiết: [`08_gap_analysis.md`](features/A_FR-01_DangKy/08_gap_analysis.md).

- 92 dòng thay đổi so với bản AI từ S0 đến S5: 58 Quyết định của SV, 27 Thiếu, 6 Thừa, 1 Sai. Người phát hiện 34 chỗ AI chưa đúng: Sinh viên 22, AI tự phát hiện khi review 7, phiên điều phối 5.
- 24 test case AI bỏ sót hoặc thiết kế sai, theo nguyên nhân: Giới hạn của công cụ AI 14, chất lượng input 5, độ phức tạp của feature 5.
- Bản AI gốc bắt được 12 trên 13 bug. Bug bị bỏ sót (email trùng qua API) chỉ lộ ra nhờ test case do phiên điều phối đề xuất và một quan sát ngoài test case.

---

## 3. Feature B: FR-07 Giỏ hàng (Web)

Thư mục: [`features/B_FR-07_GioHang/`](features/B_FR-07_GioHang/)

> _(Đang thực hiện. Điền khi xong S8.)_

### 3.1 Domain Testing từng bước

| Bước | Kết quả | File |
|---|---|---|
| S0 Đặc tả | Trích FR-07 và các yêu cầu chung áp cho trang Giỏ hàng (FR-06, FR-21 đến FR-24, API giỏ hàng, SEC); 32 yêu cầu, 30 câu hỏi mở; 10 khác biệt giữa giao diện và đặc tả (không có nút `+`/`-`, không có badge, không có breadcrumb, cột "Giá" thay cho "Đơn giá", nút "← Mua tiếp", nút thanh toán màu xanh lá...) | [`00_spec.md`](features/B_FR-07_GioHang/00_spec.md) |
| S1 Input, Output | 8 biến Input trực tiếp, 5 biến gián tiếp; 3 đường thêm vào giỏ (trang chủ, trang chi tiết, API); 3 loại lỗi theo nguyên nhân | [`01_io.md`](features/B_FR-07_GioHang/01_io.md) |
| S2 Lớp tương đương | _(điền)_ | `02_ec.md` |
| S3 Coverage, Minimum Set | _(điền)_ | `03_tc.md` |

### 3.2 Boundary Value Analysis

_(điền)_

### 3.3 Bộ test case cuối và kết quả

_(điền)_

### 3.4 Bug

_(điền)_

### 3.5 AI gap analysis

_(điền)_

---

## 4. Feature C: FR-17 Quản lý mã giảm giá (Web Admin)

Thư mục: [`features/C_FR-17_QuanLyCoupon/`](features/C_FR-17_QuanLyCoupon/). Thiết kế bằng Agent Skill `domain-testing-design`.

### 4.1 Domain Testing từng bước

| Bước | Kết quả | File |
|---|---|---|
| S0 Đặc tả | Trích FR-17, FR-12 (quyền admin), API admin coupons; khảo sát trang Quản lý Mã Giảm Giá qua ảnh. Kết quả nhập thử được giữ lại, không đưa cho AI | [`00_spec.md`](features/C_FR-17_QuanLyCoupon/00_spec.md) |
| S1 Input, Output | 6 biến của form tạo mã (`code`, `type`, `discount_value`, `min_order_amount`, `expired_at`, `max_uses_per_user`), biến của thao tác Xóa, các biến gián tiếp (mã đang có, ngày chạy, người gọi API) | [`01_io.md`](features/C_FR-17_QuanLyCoupon/01_io.md) |
| S2 Lớp tương đương | 123 lớp (49 hợp lệ, 45 không hợp lệ, 29 Output); giả định A01 đến A28 | [`02_ec.md`](features/C_FR-17_QuanLyCoupon/02_ec.md) |
| S3 Coverage, Minimum Set | 78 test case, cả 123 lớp đều có test case | [`03_tc.md`](features/C_FR-17_QuanLyCoupon/03_tc.md) |

### 4.2 Boundary Value Analysis

6 phân vùng có thứ tự: `discount_value` loại phần trăm (cận trên 100), loại cố định, `min_order_amount` (cận dưới 0), `max_uses_per_user` (cận dưới 1), độ dài `code`, `expired_at` so với ngày chạy. 32 test case BVA, gồm điểm `2^53 + 1` để kiểm độ chính xác số lớn qua API. Chi tiết: [`04_bva.md`](features/C_FR-17_QuanLyCoupon/04_bva.md).

### 4.3 Bộ test case cuối và kết quả

- [`05_final_tc.md`](features/C_FR-17_QuanLyCoupon/05_final_tc.md): **115 test case**. Nguồn gốc: AI 80, AI có SV sửa 30, SV thêm 5 (bản API cho các lớp mà giao diện không gửi được, vì ô mã tự viết hoa).
- [`06_results.md`](features/C_FR-17_QuanLyCoupon/06_results.md): Chạy ngày 21/10/2026, bản rút gọn vì thời gian. Pass 26, Fail 13, Khác giả định 6, Không áp dụng 1, Not run 69. Nhóm API chạy bằng [`scripts/run_api_tests.py`](features/C_FR-17_QuanLyCoupon/scripts/run_api_tests.py).
- Phát hiện chính: Token của user thường tạo và xóa được mã giảm giá (vượt quyền); API nhận `type` sai, trường bắt buộc rỗng, chữ ở trường số, body `{}`; request không phải JSON gây lỗi 500 lộ stack trace; số `2^53 + 1` bị lưu thành `2^53`; giao diện nhận giảm 0% và 150%.

### 4.4 Bug

12 bug, issue **#55 đến #66** (1 Critical, 5 High, 3 Medium, 3 Low). Chi tiết: [`bugs/bug_report.md`](bugs/bug_report.md), mục FR-17.

### 4.5 AI gap analysis

Chi tiết: [`08_gap_analysis.md`](features/C_FR-17_QuanLyCoupon/08_gap_analysis.md).

- 72 dòng thay đổi so với bản AI từ S1 đến S5: 43 Quyết định của SV, 23 Thiếu, 5 Mơ hồ, 1 Sai.
- Test case bỏ sót theo nguyên nhân: Giới hạn của công cụ AI 8 nhóm, chất lượng input 4 nhóm (đều do thông tin ô tự viết hoa bị giữ lại), độ phức tạp 3 nhóm.
- Bản AI gốc bắt được 10 trên 12 bug. Hai bug bị bỏ sót chỉ tìm được nhờ câu hỏi của sinh viên ở S1 (request không phải JSON) và nhờ phiên điều phối ở S4 (số lớn bị làm tròn).

---

## 5. Feature D: FR-04 Hồ sơ cá nhân (Mobile)

Thư mục: `features/D_FR-04_HoSo_Mobile/`

> _(Đang thực hiện. Điền khi xong.)_

---

## 6. Agent Skill

Skill **`domain-testing-design`** ([`skills/domain-testing-design/`](skills/domain-testing-design/)) dẫn AI đi qua Domain Testing và BVA của slide S04 **từng bước một**, mỗi lượt một bước, dừng chờ sinh viên review.

| Thành phần | Nội dung |
|---|---|
| `SKILL.md` | Quy trình S0 đến S4, nguyên tắc hộp đen, cách lưu `ai_raw/` và bảng "Thay đổi so với bản AI" |
| `references/` | Hướng dẫn từng bước (`step-s0.md` đến `step-s4.md`), quy tắc chung, bài học rút ra từ FR-01 (`lessons.md`), lưu ý theo nền tảng Web, Web Admin, Mobile (`platforms.md`), ví dụ FR-01 |
| `assets/templates/` | Khung file `ai_raw` và bản review |
| `scripts/check_step.py` | Kiểm tự động: Định dạng, bảng thay đổi, mọi lớp có test case phủ, mã test case không trùng |

- Skill được đúc kết từ cách làm FR-01, sau đó dùng cho FR-17, FR-07 và FR-04.
- Đến S5, bộ test case cuối có thể trình bày bằng skill `test-case-writing` của giảng viên.

**Video demo** (chạy trọn một feature bằng skill): _(link YouTube, điền sau)_

---

## 7. Test Summary

Bảng đầy đủ ở [`README.md`](README.md).

| Feature | TC thiết kế | Đã chạy | Pass | Fail | Chưa chạy | Bug |
|---|---|---|---|---|---|---|
| A: FR-01 | 96 | 46 | 9 | 19 | 50 | 13 |
| B: FR-07 | | | | | | |
| C: FR-17 | 115 | 46 | 26 | 13 | 69 | 12 |
| D: FR-04 (Mobile) | | | | | | |

"Đã chạy" gồm cả test case Blocked (A: 18), Khác giả định (C: 6) và Không áp dụng (C: 1).

---

## AI Critique

> _(Bản nháp do Claude soạn từ ghi chú trong quá trình làm; sinh viên đọc, sửa và viết lại theo ý mình trước khi nộp.)_

AI làm tốt phần áp dụng máy móc các guideline của slide S04, nhưng sai ở những chỗ cần biết về hệ thống thật hoặc cần tự hỏi lại giả định của chính mình. Ở FR-01, bản AI áp đủ 9 điểm BVA cho cả phân vùng không có cận trên, và chọn đại diện vi phạm hai điều kiện cùng lúc. Ở FR-17, AI gán quyền admin của `GET /api/coupons` cho FR-12 trong khi FR-12 không nói vậy; lỗi truy vết này đi qua bốn bước review mà không ai thấy, cho tới khi tôi hỏi lại ở S5. AI cũng không nghĩ tới việc trang tự sửa giá trị trước khi gửi (ô mã tự viết hoa), nên các lớp chữ thường và khoảng trắng qua giao diện thực chất chỉ kiểm được trang web, không kiểm được server. Hai bug của FR-17 (lỗi 500 khi request không phải JSON, số lớn bị làm tròn) chỉ lộ ra nhờ câu hỏi của tôi và của phiên điều phối. AI còn quy sai nguyên nhân cho người dùng: Khi công cụ báo file bị sửa từ bên ngoài, AI nói tôi sửa tay, trong khi chính nó vừa sửa bằng lệnh khác. AI bỏ sót vì nó chỉ thấy đặc tả và ảnh, không thấy hành vi thật, và vì nó có xu hướng khẳng định thay vì ghi "đây là giả định". Nguyên tắc tôi rút ra: Giữ nguyên bản AI và ghi mọi thay đổi kèm người phát hiện thì mới đo được AI sai ở đâu; con người phải là người quyết định ở mỗi bước, và mọi kết quả Pass cần được đọc cùng giới hạn của nó, vì một test case Pass không chứng minh luật được cài đúng.

---

## Mandatory Disclosure

"Tôi dùng AI (Claude Code, Anthropic, claude-opus-5-5) cho các việc sau: Trích đặc tả, đề xuất biến Input và Output, lớp tương đương, test case Domain Testing và BVA cho 4 feature (bản gốc của AI lưu nguyên văn trong `ai_raw/` của từng feature); viết script chạy test API; điền bảng kết quả S6 theo ảnh và log do tôi chạy và chụp; viết nháp bug report, nội dung issue và trang link tạo issue; viết nháp AI gap analysis; viết Agent Skill `domain-testing-design`; viết `WORKFLOW.md`, các script trong `tools/`, khung báo cáo, README, bản nháp AI Critique và Appendix B. Một phiên Claude Code làm điều phối: Đọc các phiên khác, soát thao tác bị cấm, soạn tin nhắn để tôi gửi cho các phiên thiết kế, xuất prompt log. Tôi review và quyết định ở mọi bước (các bảng "Thay đổi so với bản AI" ghi đủ chỗ tôi sửa và người phát hiện); tôi tự chụp ảnh khảo sát và kết quả chạy test, tự chạy script, tự tạo 25 issue trên GitHub, tự commit; các quyết định chọn phương án là của tôi, một số có tham khảo đề xuất của AI. AI Audit Report chi tiết ở Appendix B."

---

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---|---|
| 1 | Feature A: FR-01 (Domain + Boundary) | 25 | |
| 2 | Feature B: FR-07 (Domain + Boundary) | 25 | |
| 3 | Feature C: FR-17 (Domain + Boundary) | 25 | |
| 4 | Feature D: FR-04 Mobile (Domain + Boundary) | 15 | |
| 5 | Agent Skills | 10 | |
| | **Total** | **100** | |

---

## Appendix A: Prompt log

Xem [`prompt_log.md`](prompt_log.md) (và `prompt_log.pdf`). Log xuất tự động từ transcript Claude Code bằng [`tools/export_prompt_log.py`](tools/export_prompt_log.py), chỉ gồm các phiên của HW02 (danh sách trắng): Phiên điều phối `305c705a`, phiên thiết kế FR-01 `38378bef`, phiên skill FR-17 `1648c211`, phiên skill FR-07 `709e0d24`, phiên skill FR-04 _(điền)_. Mỗi lượt có mã `Cnn`, thời gian, công cụ, prompt và output nguyên văn.

---

## Appendix B: AI Audit Report

> Theo mẫu [AI-02] (5 mục cho mỗi artifact). Nguyên văn prompt và output ở `prompt_log.md` (Appendix A); bản gốc của AI ở `ai_raw/` của từng feature. Cột (4) dựa trên bảng "Thay đổi so với bản AI" của từng bước. Phần in đậm ở cột (5) là phần sinh viên thay đổi.

| Artifact | (1) Prompt + công cụ + thời gian | (2) Output AI | (3) Verdict | (4) Lý do | (5) Bản SV sửa |
|---|---|---|---|---|---|
| B01: Kế hoạch làm bài, cấu trúc thư mục, `WORKFLOW.md` | Claude Code, phiên điều phối `305c705a`, 12/10/2026 đến 19/10/2026 | Phân tích đề, quy trình S0 đến S8, quy tắc hộp đen, quy tắc `ai_raw/` và bảng thay đổi | **INCOMPLETE** | Hướng dẫn S0 ban đầu mâu thuẫn ("chỉ quan sát" nhưng có câu hỏi buộc nhập thử); chưa có quy tắc cấm DevTools ở S0 đến S5 và quy tắc không sửa `ai_raw/` | Thêm **quy tắc không DevTools ở S0 đến S5**, **bản AI viết lại lưu `_v2`**, **cột Loại và người phát hiện** trong bảng thay đổi |
| B02: Script `tools/export_prompt_log.py` | Phiên điều phối, 17/10/2026; sửa 20/10/2026 | Xuất transcript các phiên trong danh sách trắng ra `prompt_log.md` | **INCOMPLETE** | Kiểm khi chạy thật: Bản tóm tắt ngữ cảnh do hệ thống tự tạo khi nén phiên bị xuất thành một prompt như thể sinh viên gõ | Phiên điều phối tự phát hiện khi soát log; **bỏ dòng `isCompactSummary`** |
| B03: FR-01, S0 đến S4 (bản AI) | Phiên `38378bef`, 19/10/2026 đến 20/10/2026 | `ai_raw/S0_khao_sat.md` đến `ai_raw/S4_bva.md` | **INCOMPLETE** | 34 chỗ chưa đúng: 27 Thiếu, 6 Thừa, 1 Sai (ví dụ: Áp đủ 9 điểm BVA cho phân vùng không có cận trên; đại diện vi phạm 2 điều kiện; thiếu test case API cho khoảng trắng của Email); AI đề xuất dùng DevTools ở S0 dù đã được dặn hộp đen; AI sửa luôn file `ai_raw` khi được yêu cầu sửa bản review | Bản review `00_spec.md` đến `04_bva.md`, mỗi file có **bảng thay đổi**; khôi phục `ai_raw/S0` và lưu bản sửa thành `_v2` |
| B04: FR-01, S5 bộ test case cuối | Phiên `38378bef`, 20/10/2026 | `ai_raw/S5_final_test_cases.md` (96 test case) | **INCOMPLETE** | Thiếu cột người phát hiện trong bảng chính dù sinh viên đã chọn phương án có cột này | Thêm **cột "Phát hiện"** |
| B05: FR-01, S6 khung kết quả, script API, điền kết quả | Phiên `38378bef`, 20/10/2026 | `06_results.md`, `scripts/run_api_tests.py`, `scripts/run_tc79.py`; điền kết quả từ ảnh và log | **INCOMPLETE** | Script chạy đúng. Khi điền kết quả, AI ghi câu hỏi và đề xuất vào ô kết quả, thêm chữ "(đề xuất)" ở trạng thái; ghi sai giờ một dòng nhật ký | Sinh viên yêu cầu **ô kết quả chỉ ghi sự kiện**; phiên điều phối **sửa giờ nhật ký**, điền mục tổng hợp, sửa mô tả vai trò ở đầu file cho đúng thực tế |
| B06: FR-01, S7 bug report, trang link tạo issue | Phiên `38378bef`, 21/10/2026 | 13 bug trong `bugs/bug_report.md`, nội dung theo template issue của nhóm | **INCOMPLETE** | Gom 19 Fail thành 13 bug đúng; bug API chỉ có log, chưa có ảnh; chú thích ảnh ở #42 đặt sai chỗ | Sinh viên **chụp 11 ảnh log**, quyết định mức độ và gắn label, **tự tạo 13 issue** |
| B07: FR-01, S8 gap analysis | Phiên `38378bef`, 21/10/2026 | `ai_raw/S8_gap_analysis.md` | **INCOMPLETE** | Số liệu đúng (phiên điều phối đếm lại); xếp nhầm nguyên nhân 3 dòng | Dòng 15 đổi thành **Input**; dòng 4, 5 đổi thành **Độ phức tạp** |
| B08: Agent Skill `domain-testing-design` | Phiên `38378bef`, 20/10/2026 | `SKILL.md`, `references/`, `assets/`, `scripts/check_step.py` | **VALID** | Chạy được trên FR-17, FR-07, FR-04; script kiểm bắt được lỗi định dạng và lớp không có test case. Một lần phiên dùng skill vẫn chạy lệnh đọc file ghi chú bị cấm (kết quả bị cắt, AI không thấy nội dung) | Giữ nguyên |
| B09: FR-17, S1 đến S4 (bản AI, qua skill) | Phiên `1648c211`, 20/10/2026 | `ai_raw/S1_input_output.md` đến `ai_raw/S4_bva.md` | **INCOMPLETE** | 21 Thiếu, 4 Mơ hồ (ví dụ: Thiếu biến gián tiếp của thao tác Xóa, thiếu lớp request không phải JSON, thiếu điểm `2^53 + 1` qua API) | Bản review có **bảng thay đổi**; thêm các lớp và test case theo câu hỏi của sinh viên |
| B10: FR-17, S5 bộ test case cuối | Phiên `1648c211`, 20/10/2026 | `ai_raw/S5_final_test_cases.md` (113 test case) | **INCOMPLETE** | Gán quyền admin của `GET` cho FR-12 (sai căn cứ); thiếu API cho khoảng trắng của `code`; thiếu kiểm danh sách dài | Thêm **giả định A28**, **TC-CPN-143, 144**; sinh viên thêm **TC-CPN-140 đến 142** (ô tự viết hoa) |
| B11: FR-17, S6 script API, điền kết quả | Phiên `1648c211`, 21/10/2026 | `scripts/run_api_tests.py`; `06_results.md` điền từ 21 ảnh và 3 log | **INCOMPLETE** | Script chạy đúng, che token trong log, không xóa dữ liệu mẫu. Bảng điền đúng nhưng để trống ô ở mục 1 và cột kết quả của dòng Not run, ghi giờ nhật ký không cụ thể | Phiên điều phối **điền ô trống, ghi giờ cụ thể** theo yêu cầu của sinh viên |
| B12: FR-17, S7 bug report | Phiên `1648c211`, 21/10/2026 | 9 bug, 6 dòng Khác giả định chờ quyết định | **INCOMPLETE** | Gộp hai lỗi khác giao diện vào một bug; đề xuất gộp hành vi dựa trên giả định vào bug Critical | Sinh viên **tách BUG-04**, **KG01, KG02 thành bug**, KG03 chỉ ghi chú; **tự tạo 12 issue** |
| B13: FR-17, S8 gap analysis | Phiên `1648c211`, 21/10/2026 | `ai_raw/S8_gap_analysis.md` | **VALID** | Số liệu đúng (phiên điều phối đếm lại: 72 dòng); cách xếp nguyên nhân có căn cứ | Giữ nguyên |
| B14: FR-07, S0 đến S4 (bản AI, qua skill) | Phiên `709e0d24`, 21/10/2026 | `ai_raw/S0_khao_sat.md`, `ai_raw/S1_input_output.md`, _(điền)_ | **INCOMPLETE** | Thiếu output "phản hồi trực quan sau khi bấm Thêm vào giỏ" (FR-24), do phiên điều phối phát hiện; AI điền bảng quan sát S0 từ ảnh thay cho sinh viên (đã tự ghi chú việc này) _(bổ sung)_ | _(điền)_ |
| B15: FR-04 | _(điền)_ | | | | |
| B16: Phiên điều phối: Soạn tin nhắn, soát phiên, đếm lại số liệu | Phiên `305c705a`, 17/10/2026 đến 21/10/2026 | Tin nhắn cho các phiên thiết kế, bảng tình trạng, đề xuất phương án | **INCOMPLETE** | Có lần ghi nhầm người phát hiện; có lần ghi đè file Excel thật mà chưa kiểm; có lần phân loại sai một quan sát | Sinh viên phát hiện và yêu cầu sửa; từ đó **gắn sẵn người phát hiện vào tin nhắn**, **kiểm thời gian sửa trước khi ghi đè** |
| B17: `tools/md_to_pdf.py`, khung `report.md`, README | Phiên điều phối, 21/10/2026 | Script xuất PDF cho mọi file MD; khung báo cáo, Test Summary, bản nháp AI Critique, Appendix B | _(điền sau khi SV review)_ | | |

### Tổng kết độ chính xác AI

| Chỉ số | Số lượng | Tỉ lệ |
|---|---|---|
| Tổng artifact AI sinh đã audit | _(điền)_ | |
| VALID | | |
| INVALID | | |
| INCOMPLETE | | |

### Kết luận: Khi nào nên, không nên dùng AI?

_(Sinh viên viết.)_
