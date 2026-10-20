# Quy tắc chung

Đây là mặc định của skill. Nếu dự án có tài liệu quy trình riêng (ví dụ `WORKFLOW.md`), tài liệu đó ưu tiên hơn.

## Mục lục

1. Nguồn được đọc và không được đọc
2. Kiểm thử hộp đen
3. Khi thiếu thông tin
4. File và tên file
5. Bản AI trong `ai_raw/`
6. Bản review
7. Bảng "Thay đổi so với bản AI"
8. Giả định
9. Commit
10. Định dạng văn bản
11. Rà bước trước (khi bắt đầu từ giữa chừng)

---

## 1. Nguồn được đọc và không được đọc

| Được đọc | Không được đọc |
|---|---|
| Đề bài, tài liệu quy trình và README của dự án | Mã nguồn của hệ thống được test (backend, frontend, mobile) |
| Đặc tả của hệ thống (SRS, API spec) | Prompt log, ghi chú cá nhân của sinh viên (nếu dự án nêu tên) |
| Slide môn học về Domain Testing, BVA, viết test case | Lịch sử git (`git log`, `git show`, `git diff`). Ngoại lệ: `git checkout -- <file>` để khôi phục file trong `ai_raw/` của feature đang làm |
| Skill `test-case-writing` và chính skill này | Log phiên AI (ví dụ file `.jsonl`) |
| File trong thư mục **feature đang làm** và ảnh trong `screenshots/` | Thư mục của feature khác, trừ khi dự án cho phép |
| File do chính phiên này tạo ra | Kết quả nhập thử của sinh viên, nếu được cất ngoài thư mục làm bài |

Liệt kê thư mục để biết tên file không phải là đọc nội dung, nhưng không mở file bị cấm dù tên có vẻ hữu ích.

## 2. Kiểm thử hộp đen

- Căn cứ duy nhất để thiết kế: Đặc tả và những gì nhìn thấy trên giao diện qua **ảnh do sinh viên chụp**.
- Không tự mở giao diện, không tải HTML, JS hay gọi API để "xem thử" trong các bước thiết kế.
- Không dùng DevTools (Elements, Inspect) từ S0 đến S5, và không yêu cầu sinh viên dùng. Thuộc tính như `required`, `minlength`, `maxlength`, `pattern` là quy tắc do lập trình viên cài; biết trước sẽ khiến lớp tương đương bị chia theo code thay vì theo đặc tả. DevTools chỉ dùng ở S6 để kiểm những thuộc tính mà **đặc tả yêu cầu**.
- Hiểu biết chung về chuẩn và nền tảng (chuẩn HTML, chuẩn email, hành vi của trình duyệt hay hệ điều hành) được dùng để thiết kế, vì đó không phải mã nguồn của hệ thống. Khi dùng, ghi rõ nguồn ("theo chuẩn HTML...") để sinh viên kiểm chứng.

## 3. Khi thiếu thông tin

- Thiếu ảnh, ảnh bị cắt, không thấy được chi tiết cần đối chiếu: Liệt kê cụ thể cần chụp gì (trang nào, trạng thái nào, phần nào phải thấy), rồi dừng.
- Đặc tả không nói: Ghi thành câu hỏi mở (S0) hoặc giả định có phương án (S1 trở đi). Không tự chọn.
- Không rõ sinh viên muốn gì: Hỏi. Một câu hỏi đúng lúc rẻ hơn một file `_v2`.
- Không bao giờ bù chỗ thiếu bằng cách đọc mã nguồn, tự mở trang, hay đoán rồi viết như thể đã biết.

## 4. File và tên file

```
features/<Pool>_<FR>_<Tên>/
├── 00_spec.md        S0, bản sinh viên điền quan sát rồi AI viết lại
├── 01_io.md          S1, bản review
├── 02_ec.md          S2, bản review
├── 03_tc.md          S3, bản review
├── 04_bva.md         S4, bản review
├── ai_raw/
│   ├── S0_khao_sat.md
│   ├── S1_input_output.md
│   ├── S2_equivalence_classes.md
│   ├── S3_test_cases.md
│   └── S4_bva.md
└── screenshots/      S<bước>_<số thứ tự>_<nội dung>.png
```

Mã dùng trong tài liệu:

| Mã | Ý nghĩa | Ví dụ |
|---|---|---|
| `FRxx-Rnn` | Yêu cầu | `FR07-R03` |
| `Qnn` | Câu hỏi mở (S0) | `Q05` |
| `Onn` | Ô trong bảng quan sát (S0) | `O08` |
| `Dnn` | Khác biệt giữa giao diện và đặc tả (S0) | `D01` |
| `INn`, `OUTn`, `ERRn` | Biến Input, Output, loại lỗi (S1) | `IN2`, `ERR4` |
| `ECnn` | Lớp tương đương (S2) | `EC17` |
| `Ann` | Giả định, cùng số với câu hỏi mở gốc (S2) | `A05` ứng với `Q05` |
| `Pn` | Phân vùng có thứ tự (S4) | `P2` |
| `TC-<MÔĐUN>-NN` | Test case (S3, S4) | `TC-CART-12` |

Mã đã dùng thì không dùng lại cho thứ khác, kể cả khi mục đó bị bỏ. Mục bổ sung khi review được đánh số tiếp, không chèn giữa.

## 5. Bản AI trong `ai_raw/`

- Đầu file: Tên bước, thời gian tạo (có múi giờ), căn cứ (các file đã đọc). Sau đó là nguyên văn câu trả lời của AI. Không chép prompt.
- **Không bao giờ sửa hay ghi đè** sau khi đã giao cho sinh viên. Trong cùng lượt, trước khi giao, được sửa lỗi do chính mình phát hiện khi tự kiểm.
- Sinh viên yêu cầu AI làm lại cả bước: Lưu file mới `SN_<tên>_v2.md` (rồi `_v3`...). Đầu file ghi thêm: Lần sửa thứ mấy, thời gian, lý do (sinh viên yêu cầu gì, hoặc quy tắc nào bị vi phạm). File cũ giữ nguyên.
- Sinh viên chỉ hỏi hoặc quyết định từng điểm: Không cần `_v2`; ghi thay đổi vào bản review.
- S0: `ai_raw/S0_khao_sat.md` và `00_spec.md` ban đầu giống hệt nhau (kiểm bằng `cmp` hoặc so sánh tương đương).

## 6. Bản review

Bản review là bản đầy đủ của bước (không chỉ ghi phần sửa), gồm theo thứ tự:

1. Đầu file: Tên bước; "Bản này: Bản review của SN. Bản gốc của AI: `ai_raw/...`"; thời gian tạo bản AI; thời gian cập nhật và tóm tắt; căn cứ.
2. Nội dung chính đã áp các quyết định.
3. **Quyết định của sinh viên:** Bảng vấn đề và phương án đã chọn.
4. **Trả lời câu hỏi khi review:** Bảng câu hỏi, trả lời, thay đổi kéo theo.
5. **Kiểm tra mâu thuẫn:** Giữa các quyết định với nhau và với các bước trước; chỗ vướng ghi kèm cách đã xử lý.
6. **Ghi chú cho bước sau.**
7. **Thay đổi so với bản AI** (mục cuối cùng).

Mỗi lần cập nhật sau đó: Thêm dòng "Cập nhật lần N: <thời gian>. <tóm tắt>" ở đầu file và dòng tương ứng trong bảng thay đổi.

## 7. Bảng "Thay đổi so với bản AI"

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|

Cột "Loại" chỉ nhận một trong năm giá trị:

| Loại | Khi nào dùng | Ví dụ |
|---|---|---|
| Sai | Bản AI trái với đặc tả hoặc với giao diện quan sát được | Lập luận "ký tự này làm email sai định dạng" trong khi quy tắc đã chọn cho phép ký tự đó |
| Thiếu | Đặc tả có (hoặc bước trước đã dặn) mà bản AI không đưa vào: Biến, lớp, test case, giá trị biên, ma trận truy vết | Biến thể giá trị mà S2 đã ghi cho S4 xét nhưng S4 bỏ qua |
| Thừa | Bản AI tự đặt quy tắc hay khẳng định điều đặc tả không nói; mục trùng lặp; mục không cần thiết | Khẳng định "API không có trường X" khi đặc tả chỉ không mô tả trường đó |
| Mơ hồ | Bản AI ghi chung chung, không kiểm chứng được | "Hệ thống xử lý đúng" |
| Quyết định của SV | Bản AI không sai, nhưng sinh viên chọn một phương án AI đưa ra hoặc chốt một điểm đặc tả chưa rõ | Chọn phương án (a) cho giả định A07 |

Quy tắc ghi:

- Ghi **mọi** thay đổi về nội dung, kể cả nhỏ. Không ghi thay đổi thuần hình thức (dấu câu, định dạng).
- **Ghi rõ người phát hiện** trong cột "Lý do hoặc căn cứ", theo đúng thông tin sinh viên cung cấp:
  - "Sinh viên phát hiện".
  - "AI bổ sung khi viết bản review" (kèm định danh phiên nếu biết, ví dụ tên công cụ và session id).
  - Một phiên AI khác phát hiện rồi sinh viên chuyển sang: Ghi tên công cụ và định danh phiên mà sinh viên cung cấp.
  - Không rõ ai phát hiện thì **hỏi sinh viên**, không đoán, không mặc định là sinh viên.
- Một thay đổi vừa do câu hỏi của sinh viên vừa do quyết định: Ghi loại theo bản chất lỗi của bản AI (Sai, Thiếu, Thừa, Mơ hồ); ghi số câu hỏi và quyết định ở cột lý do.
- Bảng này là dữ liệu cho AI gap analysis và AI Audit Report, nên lý do phải đủ để người khác hiểu vì sao bản AI chưa đúng.

## 8. Giả định

Mỗi điểm đặc tả không nói mà ảnh hưởng tới kết quả mong đợi được ghi thành giả định:

| Mã | Câu hỏi gốc | Phương án | Lớp hoặc test case bị ảnh hưởng | Chữ đặc tả |
|---|---|---|---|---|

- Mỗi phương án nêu rõ hệ quả (lớp nào thành hợp lệ, không hợp lệ).
- Cột "Chữ đặc tả" chỉ trích đặc tả viết gì, nếu có liên quan; không phải đề xuất.
- AI không chọn phương án. Nếu sinh viên hỏi ý kiến, AI có thể nêu nhận xét, ghi rõ đó là nhận xét.
- Sau khi sinh viên chốt: Bản review ghi phương án chọn, lý do của sinh viên, hệ quả. Giả định mới phát sinh khi review được đánh số tiếp và cũng chờ sinh viên chốt.

## 9. Commit

- AI chỉ đưa commit message và lệnh; sinh viên tự commit (và làm các việc dự án yêu cầu trước khi commit, ví dụ xuất prompt log).
- Định dạng mặc định: `[<Pool>-<FR>][S<n>] <Verb> <nội dung>`, tiếng Anh, động từ mệnh lệnh, không dấu chấm cuối.
- Mỗi bước S1 đến S4: Một commit cho bản AI (`... (AI draft)`), một commit cho bản review. S0: Ba commit (bản AI, quan sát và ảnh của sinh viên, bản AI viết lại). Bản `_vN`: `... (AI revision N)`.
- Không biết sinh viên đã commit bản trước chưa (vì không được xem lịch sử git): Đưa cả hai phương án lệnh.

## 10. Định dạng văn bản

- Tiếng Việt; giữ nguyên tên trường, nút, thông báo như trên giao diện.
- Không dùng dấu "—" và dấu "·" làm dấu ngăn cách. Trong phần trích **nguyên văn** đặc tả thì giữ nguyên ký tự gốc và ghi chú điều đó.
- Chữ cái đầu tiên sau dấu ":" viết hoa (trừ code, tên label, đường dẫn, giờ).
- Giá trị test có dấu cách ở đầu, cuối hoặc nhiều dấu cách liền nhau: Viết bằng ký hiệu `␣` và ghi chú "`␣` là một dấu cách". Markdown tự xóa một dấu cách ở mỗi đầu đoạn code khi cả hai đầu đều có dấu cách, nên viết dấu cách thật sẽ bị mất khi hiển thị.
- Chuỗi dài viết dạng "`tc12@` + 64 chữ `a` + `.com`", ghi rõ độ dài.

## 11. Rà bước trước (khi bắt đầu từ giữa chừng)

Đọc các bản review đã có và báo cho sinh viên những điểm thiếu theo danh sách dưới đây. Không tự sửa; sinh viên quyết định bổ sung trước hay đi tiếp.

| Bước | Kiểm tra |
|---|---|
| S0 | Có trích nguyên văn đặc tả (FR chính, yêu cầu chung áp cho màn hình, API, bảo mật tham khảo); có danh sách yêu cầu mã `FRxx-Rnn`; có câu hỏi mở; bảng quan sát đã điền và đối chiếu với ảnh; ảnh trong `screenshots/` đúng tên; không có mục nào dựa trên DevTools hay phải nhập dữ liệu; có mục khác biệt giữa giao diện và đặc tả; có bảng thay đổi |
| S1 | Có Input gián tiếp; Output có loại lỗi theo nguyên nhân; có cách kiểm chứng tác động; có bảng thay đổi |
| S2 | Mỗi lớp ghi rõ H, KH; lý do tách lớp; giả định đã chốt hết; có lớp Output; có ghi chú cho S4 |
| S3 | Mỗi lớp có test case; test case không hợp lệ chỉ phủ 1 lớp không hợp lệ; có ma trận truy vết; có thứ tự chạy |
| Mọi bước | `ai_raw/` có bản AI tương ứng; tên file đúng; định dạng văn bản đúng |

Mỗi điểm thiếu ghi kèm hệ quả cho bước sắp làm (ví dụ "S0 chưa có mã yêu cầu nên S1 không truy vết được").
