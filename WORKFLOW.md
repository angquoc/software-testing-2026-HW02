# Quy trình làm bài HW02: Domain Testing trên EShop

Tài liệu này mô tả cách làm bài HW02 cho từng feature: Các bước, file đầu ra, cách commit và các quy tắc phải giữ. Mọi phiên AI tham gia làm bài phải đọc file này trước khi bắt đầu.

---

## 1. Nguyên tắc chung

### 1.1 Kiểm thử hộp đen

- Căn cứ duy nhất để thiết kế test case là đặc tả của EShop: `Homeworks/eshop-sut/README.md` (SRS) và `Homeworks/eshop-sut/api_specification.md`, cùng với những gì nhìn thấy trên giao diện (ảnh chụp trong thư mục feature).
- **Không** đọc mã nguồn EShop (`backend/`, `frontend-web/`, `frontend-admin/`, `frontend-mobile/`).
- **Không** tự mở trang, **không** tải HTML/JS của trang bằng curl hay cách khác. Thông tin giao diện chỉ lấy từ ảnh do sinh viên chụp.
- **Không** dùng DevTools (thẻ Elements, Inspect) để xem HTML ở các bước thiết kế S0 đến S5. Thuộc tính HTML như `required`, `minlength`, `maxlength`, `pattern` là quy tắc do lập trình viên cài vào; biết trước sẽ khiến lớp tương đương được chia theo code thay vì theo đặc tả. DevTools chỉ dùng ở S6 (xem mục 3.3).
- Chỗ nào đặc tả không nói rõ thì ghi thành **giả định**, không tự đặt ra quy tắc.

### 1.2 AI-First, có người kiểm soát

- AI được dẫn qua **từng bước** của kỹ thuật Domain Testing theo slide S04, mỗi lượt chỉ làm **một bước**, sau đó dừng lại chờ sinh viên review.
- Sinh viên review và quyết định sửa gì ở mọi output của AI.
- Output của AI ở mỗi bước được lưu **nguyên văn** trong `ai_raw/`. **Không bao giờ sửa hay ghi đè file trong `ai_raw/`.** Mọi chỉnh sửa nằm ở bản review.
- Khi AI viết lại output của một bước (theo yêu cầu của sinh viên), bản viết lại cũng là output của AI: Lưu thành **file mới** có đuôi `_v2`, `_v3`... (ví dụ `ai_raw/S0_khao_sat_v2.md`), file cũ giữ nguyên.

### 1.3 Phiên điều phối và phiên thiết kế

| Phiên | Làm gì |
|---|---|
| Phiên thiết kế | Làm các bước S0 đến S8 cho feature theo tài liệu này |
| Phiên điều phối | Theo dõi tiến độ, xuất prompt log, chạy server EShop, kiểm tra phiên thiết kế không đọc file bị cấm. Phiên thiết kế **không** chạy script xuất prompt log |

### 1.4 Phiên thiết kế được đọc và không được đọc

| Được đọc | Không được đọc |
|---|---|
| Đề bài `Homeworks/HW02/2026.HW02.Domain Testing_En.md` | `Homeworks/HW02/prompt_log.md` |
| `Homeworks/HW02/README.md`, `Homeworks/HW02/WORKFLOW.md` | `Homeworks/HW02/_NOTES.md` |
| SRS và API spec của EShop (mục 1.1) | Lịch sử git (`git log`, `git show`, `git diff`). Ngoại lệ: Được dùng `git checkout -- <file>` để khôi phục một file trong `ai_raw/` **của feature đang làm** nếu lỡ sửa |
| Slide môn học (S04 Domain Testing, tài liệu tham khảo Domain Testing, Test Cases AI First) | Thư mục `DA/` |
| Skill `test-case-writing` của giảng viên (`.claude/skills/test-case-writing/`) | Mã nguồn EShop (mục 1.1) |
| File trong thư mục feature đang làm và ảnh trong `screenshots/` | File `.jsonl` trong `~/.claude/projects/` |
| File do chính phiên đó tạo ra | File kết quả nhập thử của sinh viên (nếu có), được cất ngoài thư mục làm bài |

---

## 2. Cấu trúc thư mục một feature

```
features/<Pool>_<FR>_<Tên>/        ví dụ: features/A_FR-01_DangKy/
├── 00_spec.md        S0, bản SV điền quan sát rồi review
├── 01_io.md          S1, bản đã review
├── 02_ec.md          S2, bản đã review
├── 03_tc.md          S3, bản đã review
├── 04_bva.md         S4, bản đã review
├── ai_raw/           Output nguyên văn của AI từng bước
│   ├── S0_khao_sat.md
│   ├── S1_input_output.md
│   ├── S2_equivalence_classes.md
│   ├── S3_test_cases.md
│   └── S4_bva.md
└── screenshots/      Ảnh chụp giao diện và bằng chứng chạy test
```

- Đầu mỗi file trong `ai_raw/` ghi tên bước và thời gian tạo, sau đó là nguyên văn câu trả lời của AI. Không chép prompt vào file (prompt đã có trong prompt log).
- File bản viết lại (`_v2`, `_v3`...) ghi thêm ở đầu: Lần sửa thứ mấy, thời gian, lý do sửa (sinh viên yêu cầu gì, hoặc quy tắc nào trong tài liệu này bị vi phạm).
- Bản review có thể nhờ AI viết lại, nhưng sinh viên quyết định nội dung sửa.
- Cuối mỗi bản review có mục **"Thay đổi so với bản AI"**, dạng bảng với các cột:

  | Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
  |---|---|---|---|

  Cột "Loại" chỉ nhận một trong các giá trị:

  | Loại | Khi nào dùng |
  |---|---|
  | Sai | Bản AI trái với đặc tả hoặc với giao diện quan sát được |
  | Thiếu | Đặc tả có mà bản AI không đưa vào (biến, lớp, test case, giá trị biên...) |
  | Thừa | Bản AI tự đặt quy tắc mà đặc tả không có, hoặc có mục trùng lặp, không cần thiết |
  | Mơ hồ | Bản AI ghi chung chung, không kiểm chứng được (ví dụ "hệ thống xử lý đúng") |
  | Quyết định của SV | Bản AI không sai, nhưng sinh viên chọn một trong các phương án AI đưa ra hoặc chốt một điểm đặc tả chưa rõ |

  Bảng này là dữ liệu cho bước S8 (AI gap analysis) và cho AI Audit Report, nên ghi đủ mọi thay đổi, kể cả thay đổi nhỏ về nội dung. Không cần ghi thay đổi thuần hình thức (dấu câu, định dạng).
- Các file của S5 đến S8 (test case cuối cùng, kết quả chạy, bug, gap analysis) sẽ được bổ sung vào cấu trúc này khi làm tới.

---

## 3. Các bước

| Bước | Nội dung | Ai làm | Đầu ra |
|---|---|---|---|
| S0 | Trích đặc tả, khảo sát giao diện | AI trích, SV chụp ảnh và quan sát | `ai_raw/S0_khao_sat.md`, `screenshots/S0_*.png`, `00_spec.md` |
| S1 | Xác định biến Input và Output | AI đề xuất, SV review | `ai_raw/S1_input_output.md`, `01_io.md` |
| S2 | Chia lớp tương đương (Complete Set of Partitions) | AI đề xuất, SV review | `ai_raw/S2_equivalence_classes.md`, `02_ec.md` |
| S3 | Chọn test case: Bảng phủ lớp tương đương và Minimum Set | AI đề xuất, SV review | `ai_raw/S3_test_cases.md`, `03_tc.md` |
| S4 | Phân tích giá trị biên (BVA) | AI đề xuất, SV review | `ai_raw/S4_bva.md`, `04_bva.md` |
| S5 | Review lần cuối, bổ sung test case AI bỏ sót | **SV** | Bộ test case cuối cùng, ghi rõ test case nào do người thêm |
| S6 | Chạy test thật, ghi kết quả thực tế và trạng thái, chụp ảnh | **SV** | Kết quả chạy, `screenshots/S6_*.png` |
| S7 | Viết bug report, tạo issue trên GitHub của nhóm | SV, AI hỗ trợ viết | `bugs/bug_report.md`, issue trên repo nhóm |
| S8 | Phân tích những gì AI bỏ sót và vì sao | SV, AI hỗ trợ | Phần AI gap analysis của feature |

### 3.1 S0: Trích đặc tả và khảo sát giao diện

- Trích **nguyên văn** các yêu cầu liên quan từ SRS và API spec.
- Tách thành danh sách yêu cầu có mã để truy vết, dạng `<FR>-R01, <FR>-R02, ...` (ví dụ `FR01-R01`).
- Liệt kê những điểm đặc tả chưa nói rõ (câu hỏi mở). **Không** trả lời bằng cách đoán.
- Lập bảng quan sát giao diện cho sinh viên điền.
- **S0 chỉ quan sát.** Bảng quan sát và các câu hỏi chỉ được hỏi những gì **nhìn thấy được** trên giao diện mà không cần nhập dữ liệu và **không cần DevTools**: Tiêu đề, nhãn, placeholder, loại ô nhập nhìn thấy được (ô chữ, dropdown, ô chọn ngày...), dấu `*`, giá trị mặc định, nút, chữ và màu hiển thị sẵn. Không yêu cầu sinh viên nhập thử. Hành vi chỉ thấy được khi nhập dữ liệu (thông báo lỗi, giới hạn, tự định dạng...) là việc của S6.
- Thứ tự và file:
  1. AI viết `ai_raw/S0_khao_sat.md` (trích đặc tả, danh sách yêu cầu, câu hỏi mở, bảng quan sát còn trống), đồng thời tạo `00_spec.md` có **nội dung giống hệt** để sinh viên điền.
  2. Sinh viên chụp ảnh vào `screenshots/` và điền bảng quan sát **ngay trong `00_spec.md`**.
  3. AI đọc ảnh và bảng sinh viên đã điền rồi viết lại `00_spec.md` (sửa chỗ ghi nhầm, đối chiếu với ảnh, cập nhật câu hỏi mở). `ai_raw/S0_khao_sat.md` giữ nguyên làm bản gốc.

### 3.2 S1 đến S4: Theo đúng slide S04

- S1: Input gồm cả yếu tố không nhập trực tiếp nhưng ảnh hưởng tới kết quả (dữ liệu đã có, trạng thái hệ thống, người thao tác). Output gồm cả thông báo lỗi.
- S2: Theo các guideline của slide (khoảng giá trị, tập giá trị, điều kiện "must be", tách lớp khi có lý do tin rằng các phần tử được xử lý khác nhau). Ghi rõ lớp hợp lệ và không hợp lệ.
- S3: Test case hợp lệ phủ càng nhiều lớp hợp lệ càng tốt; mỗi test case không hợp lệ chỉ phủ đúng một lớp không hợp lệ.
- S4: Mỗi phân vùng có thứ tự xét các điểm biên theo slide (LB-1, LB, LB+1, UB-1, UB, UB+1, giá trị nhỏ nhất và lớn nhất giao diện cho nhập, một giá trị ở giữa).
- Cách trình bày test case và việc dùng skill `test-case-writing` để xuất Word/Excel sẽ chốt khi tới S3.

### 3.3 S6: Chạy test

- DevTools được dùng ở S6 để kiểm tra những thuộc tính mà **đặc tả yêu cầu**, ví dụ `type="email"`, `type="password"` (FR-22), số thẻ `<h1>` (FR-21). Đây là bước chạy test, không dùng để tìm thêm quy tắc mới cho việc thiết kế.
- Reset dữ liệu EShop về dữ liệu mẫu trước mỗi đợt test.
- Kết quả thực tế chỉ lấy từ lần chạy thật.

---

## 4. Commit

### 4.1 Định dạng

```
[<Pool>-<FR>][S<n>] <Verb> <nội dung>
```

- Tiếng Anh, bắt đầu bằng động từ dạng mệnh lệnh, không có dấu chấm cuối. Ví dụ: `[A-FR01][S1] Identify input/output variables`.
- Commit không thuộc feature nào: `[setup] ...`, `[skill] ...`, `[report] ...`, `[forms] ...`.
- **Sinh viên tự commit.** AI chỉ đưa commit message và lệnh. Trước mỗi commit, sinh viên nhờ phiên điều phối xuất prompt log.

### 4.2 Tách commit trong mỗi bước

Tách để lịch sử git cho thấy rõ phần AI viết và phần sinh viên sửa.

| Bước | Các commit | Ví dụ message |
|---|---|---|
| S0 | (1) `ai_raw/S0_khao_sat.md` và `00_spec.md` giống hệt (bản AI) | `[A-FR01][S0] Add spec extract and requirement list (AI draft)` |
| | (2) Ảnh chụp và bảng quan sát sinh viên điền trong `00_spec.md` | `[A-FR01][S0] Record UI exploration and screenshots` |
| | (3) `00_spec.md` do AI viết lại sau khi đọc ảnh và bảng | `[A-FR01][S0] Review spec and answer open questions` |
| S1 đến S4 | (1) Output AI trong `ai_raw/` | `[A-FR01][S2] Add equivalence classes (AI draft)` |
| Bất kỳ bước nào | AI viết lại theo yêu cầu: Thêm `ai_raw/..._v2.md` và cập nhật bản review | `[A-FR01][S0] Remove DevTools observations from spec (AI revision 1)` |
| | (2) Bản review | `[A-FR01][S2] Review equivalence classes` |
| S5 đến S8 | Mỗi bước một commit; thêm commit nếu phải sửa | `[A-FR01][S6] Execute tests and record results` |

Sửa lại một bước đã commit thì giữ nguyên tag của bước đó, ví dụ `[A-FR01][S2] Fix missing invalid class for empty email`.

---

## 5. Ảnh chụp

Lưu trong `screenshots/` của feature, đặt tên `S<bước>_<số thứ tự>_<nội dung>.png`:

- S0: `S0_01_form_dang_ky.png`, `S0_02_...png`
- S6: Theo mã test case, ví dụ `S6_TC-REG-05.png`
- S7: Ảnh trang issue đã tạo, ví dụ `S7_issue_12.png`

---

## 6. Bug report và GitHub Issues

Repo của nhóm: https://github.com/angquoc/software-testing-2026-HW02-group. Quy ước đầy đủ nằm ở mục 4 README của repo này. Tóm tắt:

- Tiêu đề: `[MSSV][FR-xx][Web|Admin|Mobile] Mô tả ngắn: Hành vi sai so với đặc tả`
- Dùng template "Bug report", bắt buộc có ảnh chụp.
- Gắn đủ 4 nhóm label: Một `severity`, một `platform`, ít nhất một `technique` (`EP` hoặc `BVA`), một `pool`.
- Mỗi bug một issue. Ghi số issue vào `bugs/bug_report.md`.

---

## 7. Định dạng văn bản

- Viết tiếng Việt; giữ nguyên tên trường, nút, thông báo như trên giao diện.
- Không dùng dấu "—" và dấu "·".
- Chữ cái đầu tiên sau dấu ":" viết hoa (trừ code, tên label, đường dẫn, giờ).
