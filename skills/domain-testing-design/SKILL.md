---
name: domain-testing-design
description: Thiết kế test case bằng Domain Testing (phân hoạch tương đương) và Boundary Value Analysis theo slide S04, đi từng bước S0 (trích đặc tả, khảo sát giao diện qua ảnh chụp), S1 (biến Input và Output), S2 (lớp tương đương), S3 (chọn test case, Minimum Set, ma trận truy vết), S4 (giá trị biên). Mỗi lượt chỉ làm một bước, lưu nguyên văn bản AI vào ai_raw/, dừng chờ sinh viên review, rồi viết bản review có bảng "Thay đổi so với bản AI". Kiểm thử hộp đen: không đọc mã nguồn, không tự mở giao diện, không dùng DevTools khi thiết kế. Dùng cho Web, Web Admin và Mobile. Dùng khi người dùng nói "domain testing", "phân hoạch tương đương", "lớp tương đương", "equivalence partitioning", "giá trị biên", "boundary value analysis", "BVA", "làm S0 (S1, S2, S3, S4) cho feature", "thiết kế test case cho FR-xx theo slide S04", kể cả khi chỉ đưa thư mục feature và bảo "làm bước tiếp theo". Đến S5, bộ test case cuối được trình bày bằng skill test-case-writing. Không dùng để chạy test, ghi kết quả thực tế hay viết bug report.
---

# Thiết kế test case bằng Domain Testing và BVA

Skill này dẫn AI đi qua kỹ thuật Domain Testing của slide S04 **từng bước một**, như một trợ lý có kỷ luật chứ không phải hộp đen sinh test case. Sinh viên review và quyết định ở mọi bước; mọi output của AI được giữ nguyên văn để làm bằng chứng cho AI Audit Report và AI gap analysis.

Các quy tắc trong skill được đúc kết từ lần làm đầu tiên (feature FR-01 Đăng ký của EShop). Những lỗi AI đã mắc ở lần đó được ghi thành checklist trong `references/lessons.md`; đọc nó trước khi giao bất kỳ bước nào.

## Phạm vi

| Bước | Nội dung | Ai làm | Skill này |
|---|---|---|---|
| S0 | Trích đặc tả, khảo sát giao diện | AI trích; sinh viên chụp ảnh và điền bảng quan sát | Có |
| S1 | Xác định biến Input và Output | AI đề xuất, sinh viên review | Có |
| S2 | Chia lớp tương đương (Complete Set of Partitions) | AI đề xuất, sinh viên review | Có |
| S3 | Chọn test case: Bảng phủ lớp, Minimum Set, ma trận truy vết | AI đề xuất, sinh viên review | Có |
| S4 | Phân tích giá trị biên | AI đề xuất, sinh viên review | Có |
| S5 | Review lần cuối, trình bày bộ test case | Sinh viên | Chỉ phần nối sang skill `test-case-writing` (mục cuối) |
| S6 đến S8 | Chạy test, bug report, gap analysis | Sinh viên | Không |

## Bước 0: Xác định ngữ cảnh (đầu mỗi phiên)

1. **Đọc quy trình của dự án.** Nếu dự án có `WORKFLOW.md` (hoặc tài liệu quy trình tương tự), đọc trước tiên. Quy tắc của dự án **ưu tiên hơn** mặc định của skill; chỗ nào dự án không nói thì dùng mặc định trong `references/rules.md`.
2. **Xác định**, hỏi người dùng nếu chưa rõ:
   - Thư mục feature và mã yêu cầu (ví dụ `features/B_FR-07_GioHang/`, FR-07).
   - Nền tảng: Web, Web Admin hay Mobile.
   - Vị trí đặc tả (SRS, API spec) và danh sách file được, không được đọc.
3. **Xác định bước hiện tại** từ các file đã có trong thư mục feature:

   | Đã có | Bước tiếp theo |
   |---|---|
   | Chưa có gì | S0 pha 1 |
   | `ai_raw/S0_khao_sat.md`, `00_spec.md` giống hệt, chưa có ảnh | Chờ sinh viên (S0 pha 2) |
   | Có ảnh và bảng quan sát đã điền, `00_spec.md` chưa có bảng thay đổi | S0 pha 3 |
   | `00_spec.md` đã review | S1 |
   | `ai_raw/SN_...md` có, bản review tương ứng chưa có | Chờ sinh viên review bước N |
   | Bản review bước N đã có | Bước N+1 |

4. **Bắt đầu từ giữa chừng** (các bước trước làm theo quy trình cũ hoặc làm tay): Rà các bản review đã có theo mục "Rà bước trước" ở `references/rules.md`, báo cho sinh viên những gì thiếu. **Không tự viết lại**; chờ sinh viên quyết định bổ sung hay đi tiếp.
5. **Nạp tài liệu:** Luôn đọc `references/rules.md` và `references/lessons.md`; đọc `references/step-sN.md` của bước sắp làm; đọc `references/platforms.md` khi thiết kế S2 đến S4.

## Quy tắc cứng

Chi tiết ở `references/rules.md`. Tóm tắt:

- **Hộp đen.** Căn cứ duy nhất là đặc tả và ảnh chụp giao diện do sinh viên cung cấp. Không đọc mã nguồn hệ thống, không tự mở giao diện, không tải HTML hay JS, không dùng DevTools từ S0 đến S5.
- **Thiếu thông tin thì hỏi người dùng.** Khi cần ảnh, cần quan sát thêm, hay đặc tả không nói, dừng lại và nói rõ cần gì. Không tìm cách tự lấy bằng các đường bị cấm, không tự đoán rồi viết tiếp.
- **Mỗi lượt một bước**, xong thì dừng chờ sinh viên.
- **Không bao giờ sửa hay ghi đè file trong `ai_raw/`.** Bản AI làm lại thì lưu thành file mới `_v2`, `_v3`, đầu file ghi lần sửa, thời gian, lý do. Lỡ sửa thì khôi phục bằng `git checkout -- <file>` nếu dự án cho phép.
- **Chỗ đặc tả không nói:** Ghi thành giả định kèm các phương án để sinh viên chọn. Không tự chọn, không khẳng định quá căn cứ.
- **Bản review** có đủ các mục bắt buộc và bảng "Thay đổi so với bản AI" với cột Loại chỉ nhận 5 giá trị (`references/rules.md`). Ghi rõ người phát hiện mỗi thay đổi; không đoán.
- **AI không tự commit.** Chỉ đưa commit message và lệnh.
- **Văn bản** tiếng Việt, giữ nguyên tên trường, nút, thông báo như trên giao diện; định dạng theo `references/rules.md`.

## Vòng lặp cho mỗi bước S1 đến S4

**Pha A: Chuẩn bị**

1. Đọc bản review của **tất cả** các bước trước, đặc biệt mục **"Ghi chú cho bước sau"**, các quyết định và giả định đã chốt. Mọi điểm mà bước trước dặn "để bước này xét" phải được xử lý hoặc ghi rõ lý do không xử lý.
2. Xác định các **quyết định ảnh hưởng tới cấu trúc cả bản** (danh sách gợi ý ở mục "Hỏi trước khi viết" của `references/step-sN.md`). Nếu có, **hỏi sinh viên trước khi viết** bản AI, vì `ai_raw/` không được sửa sau khi viết.

**Pha B: Viết bản AI**

3. Viết `ai_raw/SN_<tên>.md` theo `assets/templates/ai_raw.md`. Ngoài nội dung chính, file luôn có:
   - Mục **"Điểm cần sinh viên quyết định"**: Mỗi điểm có các phương án đánh chữ cái; không chọn thay sinh viên.
   - Mục **"Ghi chú cho bước sau"**: Những gì bước sau phải xét (biến thể giá trị, biên cần tính, cách thực thi cần chốt).
4. **Tự kiểm** trước khi giao:
   - Chạy `scripts/check_step.py` (cách dùng ở mục Tài nguyên); sửa hết lỗi.
   - Đi qua checklist của bước đó trong `references/lessons.md`.
   - Chỉ sửa file `ai_raw/` khi **chưa giao** cho sinh viên trong lượt này.

**Pha C: Dừng**

5. Báo cho sinh viên: Tóm tắt ngắn, các điểm cần quyết định, commit message cho bản AI. Dừng.

**Pha D: Viết bản review**

6. Nhận câu hỏi và quyết định của sinh viên:
   - Trả lời từng câu hỏi: Nếu sinh viên đúng thì nhận và sửa; nếu không thì giải thích, dựa trên đặc tả.
   - **Kiểm tra mâu thuẫn** giữa các quyết định với nhau và với các bước trước; báo chỗ vướng kèm phương án.
   - Nếu quyết định của sinh viên làm thay đổi lớn cấu trúc, trình bày phương án và chờ duyệt trước khi viết.
7. Viết bản review (`0N_<tên>.md`) theo `assets/templates/review.md`: Nội dung đã sửa, quyết định của sinh viên, trả lời câu hỏi, kiểm tra mâu thuẫn, ghi chú cho bước sau, bảng "Thay đổi so với bản AI".
8. Chạy lại `scripts/check_step.py`, rồi đưa commit message cho bản review. Dừng.

Sửa bản review sau khi sinh viên hỏi thêm: Sửa trực tiếp bản review (không phải `ai_raw/`), thêm dòng "Cập nhật lần N" ở đầu file, thêm dòng tương ứng vào bảng thay đổi.

## S0 có quy trình riêng (3 pha)

Chi tiết ở `references/step-s0.md`.

1. **Pha 1 (AI):** Trích nguyên văn đặc tả, lập danh sách yêu cầu có mã, câu hỏi mở, bảng quan sát còn trống và danh sách ảnh cần chụp. Ghi vào `ai_raw/S0_khao_sat.md` và tạo `00_spec.md` **giống hệt**. Dừng.
2. **Pha 2 (sinh viên):** Chụp ảnh vào `screenshots/`, điền bảng quan sát ngay trong `00_spec.md`.
3. **Pha 3 (AI):** **Trước tiên kiểm tra ảnh đã đủ chưa.** Ảnh thiếu, bị cắt, không thấy được ô nào cần đối chiếu: Liệt kê cụ thể ảnh cần chụp thêm hoặc chụp lại, rồi dừng. Đủ rồi mới đối chiếu từng ô, sửa chỗ ghi nhầm, cập nhật câu hỏi mở, ghi khác biệt giữa giao diện và đặc tả, viết bảng thay đổi.

AI **không bao giờ** tự điền bảng quan sát thay sinh viên, kể cả khi có thể đoán.

## Tóm tắt các bước

| Bước | Việc chính | Đầu ra | Hướng dẫn |
|---|---|---|---|
| S0 | Trích nguyên văn yêu cầu; mã `FRxx-Rnn`; câu hỏi mở `Qnn`; bảng quan sát `Onn` chỉ hỏi những gì nhìn thấy được | `ai_raw/S0_khao_sat.md`, `00_spec.md` | `references/step-s0.md` |
| S1 | Biến Input trực tiếp và gián tiếp; sự kiện kích hoạt; Output thành công, từ chối theo nguyên nhân, phản hồi API; cách kiểm chứng tác động | `ai_raw/S1_input_output.md`, `01_io.md` | `references/step-s1.md` |
| S2 | Lớp hợp lệ, không hợp lệ theo guideline của slide; lý do tách lớp; giả định có phương án; lớp Output | `ai_raw/S2_equivalence_classes.md`, `02_ec.md` | `references/step-s2.md` |
| S3 | Bảng phủ lớp; test case hợp lệ và không hợp lệ; nhóm API; checklist; ma trận truy vết; thứ tự chạy | `ai_raw/S3_test_cases.md`, `03_tc.md` | `references/step-s3.md` |
| S4 | Phân vùng có thứ tự; các điểm biên áp dụng được; dùng lại test case đã có | `ai_raw/S4_bva.md`, `04_bva.md` | `references/step-s4.md` |

## Điểm dừng chờ sinh viên

- Trước khi viết bản AI của một bước, nếu có quyết định ảnh hưởng tới cấu trúc cả bản.
- Sau khi viết bản AI của mỗi bước.
- Sau khi viết bản review của mỗi bước.
- S0: Sau pha 1 (chờ ảnh và bảng quan sát); trong pha 3 nếu ảnh chưa đủ.
- Bất cứ lúc nào thiếu thông tin mà chỉ người dùng cung cấp được.

## Nối sang S5: Trình bày bằng skill test-case-writing

S5 do sinh viên làm: Review lần cuối và bổ sung test case AI bỏ sót. Khi sinh viên yêu cầu xuất Word và Excel, dùng skill `test-case-writing` của giảng viên (chế độ Thiết kế, xuất qua một file JSON, chạy linter rồi build). Ghép như sau:

| Nguồn | Trường JSON của `test-case-writing` |
|---|---|
| Danh sách yêu cầu ở `00_spec.md`, ma trận truy vết ở `03_tc.md` | `requirements`; trường `requirements` của từng case |
| Các nhóm test case (hợp lệ, không hợp lệ, API, checklist, BVA) | `suites`. Nhóm chỉ khác dữ liệu dùng `format: "matrix"`, cột `covers` ghi lớp hoặc biên; nhóm nhiều bước (API, test case 2 bước) dùng `format: "steps"` |
| Giả định đã chốt (A01...) và nguyên tắc chung | `meta.assumptions` |
| Bảng "Thay đổi so với bản AI" và phần sinh viên thêm ở S5 | `origin`: `AI` (giữ nguyên bản AI), `Both` (AI tạo, sinh viên sửa), `Human` (sinh viên thêm) |
| Test case dự kiến Blocked, giới hạn quan sát | `notes` |
| Nền tảng, trình duyệt hoặc thiết bị | `meta.environment` |

Không tự viết lại nội dung test case khi chuyển sang JSON; chỉ đổi hình thức. Chỗ nào linter báo lỗi về nội dung (ví dụ kết quả mong đợi mơ hồ) thì báo sinh viên, không tự sửa.

## Tài nguyên

- `references/rules.md`: Nguồn được đọc và không được đọc, hộp đen, file và tên file, bản review, bảng thay đổi, giả định, commit, định dạng, rà bước trước.
- `references/lessons.md`: Checklist tự kiểm theo từng bước, rút từ lỗi đã gặp.
- `references/step-s0.md` đến `references/step-s4.md`: Hướng dẫn chi tiết từng bước, kèm "Hỏi trước khi viết".
- `references/platforms.md`: Lưu ý theo nền tảng Web, Web Admin, Mobile; cách xử lý khi môi trường làm thay đổi giá trị.
- `references/example-fr01.md`: Ví dụ rút gọn từ feature FR-01.
- `assets/templates/ai_raw.md`, `assets/templates/review.md`: Khung file.
- `scripts/check_step.py`: Kiểm tra máy móc. Cách dùng:

  ```bash
  python -I <skill>/scripts/check_step.py format <file>...                 # dấu "—", "·" ngoài phần trích nguyên văn
  python -I <skill>/scripts/check_step.py changes <file>...                # cột Loại của bảng thay đổi
  python -I <skill>/scripts/check_step.py classes <02_ec.md>               # mã lớp trùng, đếm theo Loại
  python -I <skill>/scripts/check_step.py coverage <02_ec.md> <03_tc.md> [<04_bva.md>]
                                                                           # lớp chưa có test case, mã test case trùng hoặc không tồn tại
  python -I <skill>/scripts/check_step.py all --ec 02_ec.md --tc 03_tc.md 04_bva.md --files <mọi file của bước>
  ```

  Script không đánh giá nội dung; kết quả mong đợi đúng hay sai là việc của AI và sinh viên.
