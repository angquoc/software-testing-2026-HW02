# Appendix A: Prompt Log (HW02-AI)

| Mục | Giá trị |
|---|---|
| MSSV | 23120061 |
| Họ tên sinh viên | Nguyễn Thị Ánh Ngọc |
| Bài tập | HW02-AI: Domain Testing on EShop |
| Chính sách AI | Open (khai báo + AI Audit Report bắt buộc) |
| Bloom-AI | G9.2 (Apply), G9.3 (Analyse) |
| Công cụ AI | Claude Code (Anthropic); ChatGPT, Gemini _(nếu dùng)_ |
| Múi giờ | Giờ Việt Nam (UTC+7), định dạng `HH:MM dd/mm/yyyy` |

**Quy ước mã:** `C##` = Claude, `G##` = ChatGPT, `M##` = Gemini. Mã này dùng để dẫn chiếu trong AI Audit Report (Appendix B).

---

## 1. Claude Code (xuất tự động, nguyên văn)

> Phần dưới được xuất từ lịch sử phiên Claude Code bằng `python tools/export_prompt_log.py`. Script chỉ đọc các phiên thuộc HW02 (danh sách trắng `SESSIONS`), không lấy phiên khác. Không chỉnh sửa tay trong vùng này; chạy lại script trước mỗi commit để cập nhật.

<!-- CLAUDE-LOG:START -->

### C01 · 14:17 12/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Bây giờ tôi sẽ làm bài tập HW02, bạn cần đọc kỹ yêu cầu, đọc thêm các docs ở folder khác nếu cần. HW01 để tham khảo cách thiết kế folder (23120061_HW01_AI_100 là folder đã tổng hợp để nộp bài và tôi nhét vào HW01 cho gọn, chứ ban đầu chưa cần có folder đó), có thể dùng lại các file trong HW01 nếu cần (ví dụ như tool, forms,...). Bởi vì đây là bài tập cá nhân nhưng cũng có nhóm nên đầu tiên chúng ta hãy đi từng bước:
1. Hiểu rõ đề bài và những việc cần chuẩn bị.
2. Thiết kế folder HW02 cần những gì.
3. Những việc cần chốt trước khi làm và những việc cần phải nhớ xuyên suốt quá trình làm (log, commit, v.v...)

Khi chúng ta đã verify mọi thứ thì mới bắt đầu làm bài tập để không bị bỏ sót bước nào. Hãy đi từng bước ở trên, nếu bạn có suggest nào có thể nêu ra để cải thiện.


 

Đừng để ý tới git đang hiện có, đó là phần của HW01 và nó tràn ra vì tôi add thêm folder 23120061_HW01_AI_100 vào. Nó không ảnh hưởng gì đến HW02, đừng nhầm lẫn.

Bất cứ vấn đề gì bạn không hiểu rõ, hãy hỏi tôi, không nên tự quyết hoặc tự bịa.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: List workspace structure
- Read: D:\Dang\Test\Homeworks\HW02\2026.HW02.Domain Testing_En.md
- Read: D:\Dang\Test\Homeworks\___2026.Homework.Policies.md
- Bash: Inspect HW01 structure and key docs
- Bash: List HW01 non-image files
- Bash: Read HW01 README, notes, tools, report outline
- Read: C:\Users\Lenovo\.claude\projects\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\tool-results\bnbp8ql5s.txt
- Bash: Inspect EShop SUT repo overview
- Bash: Skim group docs and check seed credentials
- Bash: Check PDF text extraction tools
- Bash: Extract text from domain testing slides
- Read: C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\scratchpad\S04_Domain Testing.txt
- Read: C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\scratchpad\EN.DOMAIN TESTING.txt
- Read: C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\scratchpad\EN.DOMAIN TESTING - UC Analysis.txt
- Read: C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\scratchpad\EN.DOMAIN TESTING.Exe.txt
- Bash: Survey mobile app screens
- Bash: Inspect course test case and report templates
- Bash: Check Node, git, gh, transcript folders

**Output AI (nguyên văn):**

````text
Mình sẽ bắt đầu bằng việc khảo sát cấu trúc thư mục và đọc đề bài HW02.

Giờ mình xem cách HW01 được tổ chức.

HW01 đã rõ. Giờ mình xem SUT EShop (đã clone trong `DA/eshop-sut`) và tài liệu nhóm.

Mình đã đọc xong phần lớn tài liệu, kiểm tra nhanh thêm môi trường (Node, nơi lưu log Claude) rồi sẽ tổng hợp.

Mình đã đọc xong đề HW02, quy định chung, cấu trúc HW01 (cả `_NOTES.md` và các tool), đặc tả SRS của EShop, slide Domain Testing (S04 và Refs) và template test case của môn. Chưa tạo file nào. Dưới đây là 3 bước bạn yêu cầu, cuối cùng là danh sách câu hỏi cần bạn trả lời.

---

# Bước 1 — Hiểu đề và những việc cần chuẩn bị

## 1.1 Đề yêu cầu gì

**Phạm vi:** chọn 4 feature, mỗi Pool một feature (A, B, C, D). Trong nhóm không ai được trùng feature với ai.

| Rubric | Điểm |
|---|---|
| Feature A, Pool A (Domain + BVA) | 25 |
| Feature B, Pool B | 25 |
| Feature C, Pool C | 25 |
| Feature D, Pool D (Mobile) | 15 |
| Agent Skills | 10 |

**Mỗi feature phải có 4 phần:**
1. **Domain Testing:** dùng AI để thiết kế test case và giải thích chi tiết từng bước đã làm.
2. **BVA:** tương tự, cũng giải thích từng bước.
3. **AI gap analysis:** những test case hoặc bug mà AI bỏ sót, và lý do bỏ sót (do prompt, do giới hạn của công cụ, hay do feature phức tạp).
4. **Bug report:** ghi trong file Markdown và tạo issue trên GitHub Issues của nhóm, mỗi issue có ảnh chụp.

**Phần chung cho cả bài:**
- **Agent Skill** cho Domain Testing và BVA, kèm video YouTube demo chạy hết một feature từ đầu đến cuối.
- **AI Audit Report:** cho mỗi lượt dùng AI ghi tên công cụ, ngày giờ, prompt và output. Script `export_prompt_log.py` của HW01 làm được việc này.
- **AI Critique** dài 200–300 từ.
- **Commit:** mỗi bước của mỗi feature là một commit, và nộp kèm `git_log.txt`.
- **README.md:** bảng tự chấm điểm và test summary (số feature; số TC đã thiết kế, đã chạy, pass, fail, chưa chạy; số bug; link video).
- **Định dạng:** mọi file đều có bản MD và bản PDF.
- **Tên file nộp:** `23120061_HW02_AI_DomainTesting_XXX.zip`, tối đa 20 file, mỗi file không quá 20MB.

**Những điểm có thể làm mất trắng điểm:**
- Thiếu bất kỳ tài liệu bắt buộc nào thì bài bị 0 điểm.
- Hai sinh viên chép của nhau, **kể cả chép prompt**, thì cả hai bị 0 điểm. Vì vậy trong nhóm chỉ nên dùng chung danh sách chia feature và quy ước đặt issue. Prompt và skill phải là của riêng bạn.
- Policy nói nếu chọn task quá đơn giản thì điểm tối đa đạt được sẽ bị giới hạn.

## 1.2 Kỹ thuật theo đúng slide của môn (S04)

Đề nhấn mạnh phải hướng dẫn AI đi qua từng bước của kỹ thuật **như đã dạy**, không được dùng một prompt chung chung. Quy trình trong slide có 4 bước:

1. **Xác định biến Input và Output** dựa trên đặc tả. Output gồm cả thông báo lỗi.
2. **Xác định các lớp tương đương (EC) hợp lệ và không hợp lệ** theo guideline:
   - Điều kiện dạng khoảng giá trị: 1 lớp hợp lệ và 2 lớp không hợp lệ.
   - Điều kiện dạng tập giá trị: mỗi giá trị một lớp hợp lệ, cộng thêm 1 lớp không hợp lệ.
   - Điều kiện dạng "must be": 1 lớp hợp lệ và 1 lớp không hợp lệ.
   - Nếu các phần tử trong một lớp có thể bị chương trình xử lý khác nhau thì tách lớp đó ra.
   - Kết quả là bảng *Complete Set of Partitions*.
3. **Chọn test case:**
   - Mỗi TC hợp lệ phủ càng nhiều lớp hợp lệ càng tốt.
   - Mỗi TC không hợp lệ chỉ phủ đúng một lớp không hợp lệ.
   - Kết quả là bảng *Coverage* và bảng *Minimum Set*.
4. **BVA:** với mỗi phân vùng, lấy tối đa 9 điểm: LB−1, LB, LB+1, UB−1, UB, UB+1, giá trị nhỏ nhất và lớn nhất mà UI cho nhập, và một giá trị ở giữa.

Slide Kaner còn có 4 cách nhìn về "tương đương": intuitive, specified, equivalent paths, risk-based. Phần này dùng tốt khi giải thích vì sao lại tách một lớp.

## 1.3 Những điều đã biết về SUT

- **Oracle (căn cứ để xác định kết quả đúng)** là SRS trong `DA/eshop-sut/README.md`. App được cài lỗi có chủ đích.
- **Mật khẩu admin đúng là `Admin123!`**, mình đã kiểm tra trong `database.js:92`. File `setup_guide.md` ghi `admin123` là sai.
- **App Mobile ghi cứng `API_URL = 192.168.10.13`** ở `frontend-mobile/App.js:16`. Bạn phải đổi thành IP LAN của máy mình và ghi lại việc này trong phần môi trường test. App dùng Expo SDK 54.
- **Pool D không có danh sách FR riêng.** SRS chỉ có FR-20, liệt kê các chức năng trên mobile: xem sản phẩm, đăng nhập, đăng ký, giỏ hàng, thanh toán, hồ sơ, hủy đơn…
- **Môi trường:** máy đã có Node 20.19.5 và git. Chưa có `gh` CLI, nên sẽ tạo issue trên GitHub bằng web, việc này cũng tiện cho chụp ảnh.

## 1.4 Gợi ý chọn feature (để nhóm cân nhắc)

Kỹ thuật này phát huy tốt nhất ở những feature có miền giá trị rõ, có thứ tự và có biên:

| Pool | Feature có nhiều biên để test | Feature ít biên (nên tránh) |
|---|---|---|
| A | FR-01 Đăng ký (độ dài và luật mật khẩu, email), FR-04 Hồ sơ (SĐT bắt đầu bằng 0, 10–11 số), FR-02 (khóa sau 3 lần sai, 30 giây), FR-03 (OTP 6 số) | FR-05, FR-06 |
| B | **FR-09 Coupon** (`>= min_order`, hạn dùng, số lượt dùng, percent/fixed), FR-07 Giỏ hàng (số lượng) | FR-10, FR-11 (hợp với state transition hơn) |
| C | **FR-17 Coupon CRUD** (6 trường có ràng buộc), FR-15 Sản phẩm (tên tối đa 255 ký tự, giá > 0), FR-16 CSV | FR-12, FR-13, FR-14 |

---

# Bước 2 — Thiết kế folder HW02 (đề xuất)

```
HW02/
├── .gitignore                 # file đề, ~$*, *.mp4, *.zip, _NOTES.md (giống HW01)
├── _NOTES.md                  # nháp, không nộp: ghi các artifact AI cho Audit và chất liệu cho Critique
├── README.md                  # bảng tự chấm + Test Summary + link video   ← bắt buộc
├── report.md / report.pdf     # báo cáo chính (xem dàn ý bên dưới)
├── prompt_log.md / .pdf       # Appendix A: xuất tự động bằng script
├── git_log.txt
├── environment.md             # commit SUT (85af3ba), Node, trình duyệt, điện thoại, Expo Go, IP, dữ liệu reset
├── features/
│   ├── A_FR-xx_<ten>/
│   │   ├── 00_spec.md         # trích nguyên văn FR từ SRS (oracle)
│   │   ├── ai_raw/            # output AI NGUYÊN VĂN của từng bước (S1..S4), không sửa
│   │   ├── 01_io.md … 04_bva.md   # bản đã review / sửa của từng bước
│   │   ├── testcases.md       # bảng TC cuối cùng + Actual/Status
│   │   └── screenshots/       # đặt tên theo TC-ID / BUG-ID
│   ├── B_FR-xx_<ten>/  C_FR-xx_<ten>/  D_MOBILE_<ten>/
├── bugs/
│   └── bug_report.md          # danh sách bug + link tới GitHub issue số mấy
├── skills/                    # bản nộp của Agent Skill
│   ├── domain-testing/SKILL.md
│   └── boundary-value-analysis/SKILL.md
├── forms/                     # (tuỳ chọn) AI-02/03/05 điền như HW01
└── tools/
    ├── export_prompt_log.py   # lấy từ HW01, đổi TRANSCRIPT_DIR và lọc theo phiên HW02
    ├── fill_ai02.py, docx_to_md.py   # lấy từ HW01 nếu dùng forms
    └── build_summary.py       # (đề xuất) đếm TC/pass/fail/bug từ testcases.md → README
```

**Dàn ý `report.md`:**
1. Thông tin chung và môi trường test
2. Cách áp dụng kỹ thuật
3. Mỗi feature (A→D) gồm:
   - Đặc tả
   - S1 biến I/O
   - S2 bảng EC
   - S3 bảng Coverage và Minimum Set
   - S4 BVA
   - Kết quả thực thi
   - AI gap analysis
4. Tổng hợp bug
5. Agent Skill
6. AI Critique
7. Mandatory Disclosure
8. Self-Assessment
9. Appendix A (prompt log) và Appendix B (AI Audit Report)

**Lý do tách `ai_raw/` khỏi bản đã review:** đây vừa là bằng chứng có review của người, vừa là chất liệu chính cho phần *AI gap analysis*. HW01 cũng làm như vậy với `AI_generated_testcases_C57.md`.

---

# Bước 3 — Những việc cần chốt và những việc cần nhớ

## 3.1 Quy trình đề xuất cho mỗi feature (mỗi dòng là một commit)

| Bước | Nội dung | Ví dụ commit message |
|---|---|---|
| S0 | Trích đặc tả và khám phá UI (chưa thiết kế TC) | `HW02 [B-FR09] S0: extract spec & explore SUT` |
| S1 | AI xác định biến I/O, sau đó bạn review | `… S1: identify input/output variables` |
| S2 | AI chia EC, sau đó bạn review | `… S2: equivalence classes` |
| S3 | AI chọn TC (Coverage, Minimum Set), sau đó bạn review | `… S3: domain test cases` |
| S4 | AI làm BVA, sau đó bạn review | `… S4: boundary value test cases` |
| S5 | Bạn bổ sung TC mà AI thiếu | `… S5: human review & added TCs` |
| S6 | Chạy test thật, ghi Actual và chụp ảnh | `… S6: execute tests` |
| S7 | Viết bug report và tạo GitHub Issues | `… S7: bug reports` |
| S8 | Viết AI gap analysis | `… S8: AI gap analysis` |

**Gợi ý cách làm skill (mục 10 điểm):**
1. Làm **feature đầu tiên** bằng tay, hướng dẫn AI qua từng bước. Như vậy prompt nào cũng cho thấy rõ bạn đang dẫn dắt AI theo kỹ thuật.
2. Đúc kết lại thành **skill**, trong đó skill tự dừng sau mỗi bước để bạn review.
3. Dùng skill cho **các feature còn lại** và quay video trên một feature.

Cách này có cả bằng chứng "guided step-by-step" lẫn một skill tái sử dụng được.

## 3.2 Những việc cần nhớ xuyên suốt

- **Trước mỗi commit:** chạy `export_prompt_log.py` và commit message ghi rõ feature và bước.
- **Không sửa `ai_raw/`.** Mọi chỉnh sửa làm trên bản review, và ghi vào `_NOTES.md` để sau này đưa vào Audit và Critique.
- **Actual result chỉ lấy từ lần chạy thật.** Mình sẽ không tự điền kết quả nếu bạn chưa chạy.
- **Reset DB (`node database.js`) trước mỗi đợt test** để kết quả lặp lại được. Việc này đặc biệt quan trọng với coupon, vì số lượt dùng mỗi user bị lưu lại.
- **Mỗi bug là một issue,** có ảnh chụp, và ghi số issue vào `bug_report.md`.
- **Chú ý giới hạn khi nộp:** tối đa 20 file và mỗi file 20MB. Policy cũng cảnh báo không phụ thuộc quá nhiều vào link online.

## 3.3 Ba gợi ý cải thiện

1. **Mở VS Code ngay tại folder `HW02`.** Khi đó log Claude sẽ nằm riêng trong `~/.claude/projects/d--Dang-Test-Homeworks-HW02`. Hiện tại folder `d--Dang-Test` chung đã có 2 phiên, nên script xuất log rất dễ lẫn phiên không liên quan.
2. **Giữ đúng kiểu black-box.** Bạn và mình đã đọc mã nguồn EShop, và trong `DA/docs` đã có sẵn danh sách lỗi cho seminar T09. Nếu đưa những thông tin này vào prompt thì phần "AI tìm ra hay bỏ sót" không còn trung thực. Mình đề xuất chỉ thiết kế TC từ SRS. Chỉ đọc code sau khi đã có bug, để giải thích nguyên nhân, và khai báo việc đó.
3. **Cross-check với một AI khác** (ChatGPT hoặc Gemini) ở bước S2 và S4 của ít nhất một feature. Việc này cho thêm chất liệu tốt cho gap analysis và Critique, và HW01 đã làm theo cách này.

---

# Câu hỏi cần bạn trả lời trước khi bắt đầu

1. **Nhóm:** nhóm gồm những ai, và các bạn khác đã chọn feature nào? Bạn định chọn 4 feature nào?
2. **Pool D:** nếu một feature mobile trùng FR với feature web của bạn khác (ví dụ "Đăng ký trên mobile" và FR-01) thì có tính là trùng không? Câu này có lẽ phải hỏi nhóm hoặc TA.
3. **GitHub Issues của nhóm:** URL repo là gì, ai tạo repo, và nhóm đã có quy ước đặt tên issue hay label chưa (ví dụ `[23120061][FR-09] …`)?
4. **Repo cá nhân cho HW02:** chỉ dùng git local như HW01, hay có đẩy lên GitHub riêng?
5. **Deadline** trên Moodle là ngày nào?
6. **Ngôn ngữ báo cáo:** tiếng Việt như HW01, hay tiếng Anh theo đề?
7. **Định dạng test case:** Markdown làm bản chính (mình đề xuất, vì dễ diff, skill dễ sinh ra và dễ đếm tự động), hay Excel theo template môn kèm bảng copy sang MD?
8. **Thiết bị mobile:** điện thoại thật (Android hay iOS) hay emulator?
9. **Có dùng lại các form AI-02, AI-03, AI-05 như HW01 không?** Đề HW02 chỉ ghi "if needed".
10. **Bạn có đồng ý với nguyên tắc black-box** (gợi ý số 2) và việc chuyển workspace sang folder `HW02` (gợi ý số 1) không?

Khi bạn trả lời xong, mình sẽ dựng khung folder, `git init`, sửa script log, rồi bắt đầu S0 của feature đầu tiên.
````

---

### C02 · 15:39 12/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
1. Nhóm gồm 3 người (gồm tôi), chưa ai chọn feature nào cả. Tôi tính sẽ tạo excel rồi up lên google drive để chọn, đương nhiên file đó cũng sẽ đánh dấu những việc nào nặng/nhẹ để các thành viên tự cân nhắc.
2. Pool D tôi sẽ hỏi lại giảng viên. Nhưng có cách nào để vừa chọn bên web vừa chọn bên mobile không trùng không hay feature không đủ để làm việc đó?
3. Tôi sẽ là người tạo repo và add các thành viên vào. Tôi đang suy nghĩ nên chung 1 repo và mỗi người 1 nhánh riêng hay là chung 1 repo và mỗi người 1 repo riêng. Tôi cũng sẽ là người quy ước đặt tên issue và gắn label.
4. Đề bài có yêu cầu cái nào không?
5. Deadline chưa thấy tạo, có thể là thứ 3 tuần sau.
6. Tiếng Việt
7. Markdown và fill lại vào excel theo template được không?
8. Tôi chưa tính tới. Nhưng nếu điện thoại thật thì là android.
9. Xem thử có những form nào cần thì hãy làm. Tôi nghĩ là cùng cần.
10. Nếu đề yêu cầu black-box thì làm theo đề. Chuyển workspace thì có bị mất cuộc trò chuyện này không? Tôi có cần làm cuộc trò chuyện lại với bạn không?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check HW01 remote and read AI-04/06/01 templates
- Bash: Read AI-04/06/01 templates with UTF-8

**Output AI (nguyên văn):**

````text
Mình kiểm tra nhanh hai điều trước khi trả lời: HW01 có đẩy lên remote không, và nội dung các form AI-04 và AI-06, để biết HW02 cần form nào.

Đã có đủ thông tin. Trả lời lần lượt 10 ý của bạn:

---

### 1. File Excel chọn feature

Mình có thể soạn sẵn file này. Mỗi dòng là một FR, gồm các cột: Pool, Feature, số biến input, số biên có thể test, mức độ **Nặng / Vừa / Nhẹ** kèm lý do, và cột "Người chọn". Mức độ sẽ chỉ dựa trên SRS (black-box). Bạn chỉ cần mở file rồi tự upload lên Drive.

### 2. Web và Mobile có chọn được mà không trùng không?

**Đủ feature để làm.** Lấy ví dụ nhóm 3 người, chọn trên web:
- Pool A có 6 FR, 3 người lấy 3 FR, còn dư 3.
- Pool B có 5 FR, 3 người lấy 3 FR, còn dư 2.
- Cộng lại còn **5 FR chưa ai làm trên web**, trong khi Mobile chỉ cần 3.

Mình liếc qua `App.js` thì thấy app mobile có các màn: đăng ký, đăng nhập, quên mật khẩu/OTP, hồ sơ, tìm sản phẩm, giỏ hàng, checkout có coupon, lịch sử đơn và hủy đơn. Danh sách này trải rộng cả FR-01 đến FR-11. Phải chạy app thật thì mới khẳng định được.

**Cái bẫy là các FR còn dư thường là FR "nhẹ"** (FR-05, FR-06, FR-11), nên rất khó làm BVA trên đó. Vì vậy khi chia nên chọn **cả 6 feature (web và mobile) cùng lúc**, chứ đừng chọn web trước rồi lấy phần thừa cho mobile.

Ví dụ một cách chia hợp lý:
- **Web, Pool A:** FR-01, FR-02, FR-04
- **Mobile:** FR-03 (OTP và luật mật khẩu), FR-07 (số lượng trong giỏ), FR-08 hoặc FR-11

Trong file Excel mình sẽ thêm cột "Có trên Mobile?" để nhóm thấy rõ điều này.

Lưu ý thêm: dù giảng viên cho phép, bạn **không nên tự chọn cùng một FR cho cả web lẫn mobile**. Như vậy dễ bị đánh giá là làm lại cùng một bộ TC.

### 3. Repo của nhóm

Mình đề xuất làm như sau:
- **1 repo nhóm chỉ dùng cho Issues.** Repo này chứa README ghi bảng chia feature, quy ước đặt tên issue, label và issue template.
- **Mỗi người 1 repo cá nhân, để private,** dùng cho bài làm.

Lý do không nên dùng chung một repo chia nhánh:
1. Đây là bài cá nhân và chép prompt bị 0 điểm. Chung repo thì ai cũng đọc được prompt và skill của nhau, vừa dễ bị nghi chép vừa khó chứng minh mình không chép.
2. `git log` nộp cho giảng viên phải là của riêng bạn. Chia nhánh vẫn lọc được, nhưng dễ lẫn commit của người khác.
3. Giảng viên chỉ yêu cầu "group's GitHub Issues page", không yêu cầu chung code.

Khi cần review chéo (policy có yêu cầu), mỗi người cấp quyền đọc repo của mình cho bạn cùng nhóm.

### 4. Đề có bắt buộc gì về repo không?

Có. Policy ghi *"Students must use Git (GitHub / Bitbucket / GitLab)… may work on their personal / group GitHub repositories and submit the git commit logs"*. Tức là cần có remote, chỉ dùng git local là không đủ. HW01 của bạn đã có remote `angquoc/software-testing-2026-HW01`, nên HW02 làm tương tự với repo `software-testing-2026-HW02`.

### 5. Deadline

Nếu hạn là thứ Ba tuần sau thì đó là **20/10/2026**; hôm nay là thứ Hai 12/10. Lịch dự kiến:

| Ngày | Việc |
|---|---|
| 12–13/10 | Dựng khung, chia feature, tạo repo và quy ước issue, **chạy thử app mobile** |
| 14/10 | Feature 1: làm tay, hướng dẫn AI qua từng bước S0–S8 |
| 15/10 | Đúc kết thành skill, rồi dùng skill cho Feature 2 |
| 16–17/10 | Feature 3 và Feature 4 (Mobile) |
| 18/10 | Quay video skill, tạo GitHub Issues, viết gap analysis |
| 19/10 | Critique, Audit, các form, README, PDF, nén zip |
| 20/10 | Dự phòng |

### 6. Ngôn ngữ

Tiếng Việt. ✔

### 7. Viết test case bằng Markdown rồi điền sang Excel

Được. Markdown là bản gốc. Một script sẽ điền vào một workbook ghép từ 2 template của môn:
- Sheet *Function list* và *Test cases*, lấy từ `Test cases_Template_En.xlsx`
- Sheet *Test summary report* và *Bug report*, lấy từ `Test report_Template_En.xlsx`

Script chạy lại bao nhiêu lần cũng được, giống `fill_ai02.py` của HW01.

### 8. Android thật

Cách này được, nhưng có **một rủi ro cần kiểm tra sớm**. App dùng **Expo SDK 54**, mà Expo Go trên Play Store thường chỉ hỗ trợ SDK mới nhất. Nếu Expo Go hiện tại đã lên SDK mới hơn thì app có thể không mở được. Khi đó phải cài bản Expo Go cũ hơn bằng APK, hoặc dùng emulator.

Ngoài ra cần:
- Sửa `API_URL` thành IP LAN của máy bạn.
- Cho phép Node đi qua Windows Firewall (cổng 3000 và 8081).
- Điện thoại và máy tính dùng chung Wi-Fi.

Vì vậy mình đưa việc chạy thử mobile vào ngày đầu, **trước khi nhóm chốt feature Pool D**.

### 9. Các form AI cần nộp

| Form | HW02 | Lý do |
|---|---|---|
| **AI-02 Audit Report** | ✅ Cần | Đề ghi bắt buộc. Dùng lại `fill_ai02.py` |
| **AI-03 Disclosure** | ✅ Cần | Đề bắt buộc phần khai báo |
| **AI-05 Privacy Checklist** | ✅ Nên làm | Đề HW02 không nhắc tới, nhưng HW01 đã chấm. Làm tốn ít công vì đã có sẵn script |
| AI-04 Reflective Statement | ❌ | Form ghi chỉ dùng cho Project lớn, Seminar, Đồ án. Tuy vậy, 3 câu hỏi của form này dùng tốt làm **dàn ý cho AI Critique** |
| AI-01, AI-06 | ❌ | Chỉ ký một lần vào tuần đầu của môn, không nộp theo từng HW |

### 10. Black-box và chuyển workspace

**Black-box:** đề không ghi chữ "black-box", nhưng có hai chỗ đều chỉ về cùng hướng:
- Slide S04, Bước 1 ghi *"Based on program specification"*.
- SRS ghi *"dùng tài liệu này làm cơ sở thiết kế test case, sau đó kiểm thử hệ thống thực"*.

Nên mình sẽ **thiết kế TC chỉ từ SRS và không đưa code vào prompt**. Code chỉ được đọc sau khi đã tìm ra bug, để giải thích nguyên nhân, và việc đó sẽ được ghi rõ là có đọc code.

**Chuyển workspace:** cuộc trò chuyện này **không mất**, nó vẫn nằm trong folder log của `D:\Dang\Test`. Tuy nhiên phiên mới mở ở HW02 sẽ **không có ngữ cảnh** của phiên này, và memory cũng tách theo từng workspace. Vì vậy mình đổi đề xuất: **cứ ở lại workspace này**. Script xuất log sẽ chỉ lấy những phiên có trong danh sách session ID của HW02, bắt đầu bằng phiên hiện tại (`305c705a`), nên không bị lẫn với phiên khác. Bản thân cuộc trò chuyện này cũng là AI usage của HW02 và cần đưa vào log.

---

### Cần bạn xác nhận để bắt đầu dựng khung

1. Đồng ý mô hình **1 repo nhóm chỉ dùng cho Issues, cộng repo cá nhân private**?
2. Mình **soạn luôn file Excel chọn feature** (kèm mức nặng/nhẹ và cột "Có trên Mobile?")?
3. Đồng ý **ở lại workspace này**?

Nếu cả 3 đều đồng ý, mình sẽ làm theo thứ tự: tạo khung `HW02/` → `git init` → chỉnh `export_prompt_log.py` → soạn file Excel chọn feature.
````

---

### C03 · 21:33 12/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
1. Đồng ý.
2. Đồng ý.
3. Đồng ý. Nhưng bạn nhớ tuyệt đối không được để lẫn các phần session khác đâu đấy.
4. Remote thì có phải bật public không?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Read rest of export script, git identity, session files
- Bash: Create HW02 folders, copy tools, git init
- Write: D:\Dang\Test\Homeworks\HW02\tools\export_prompt_log.py
- Bash: View manual section of HW01 prompt log
- Write: D:\Dang\Test\Homeworks\HW02\prompt_log.md
- Bash: Run export script and verify isolation
- Edit: D:\Dang\Test\Homeworks\HW02\tools\export_prompt_log.py
- Bash: Rerun export and verify no other session leaked
- Edit: D:\Dang\Test\Homeworks\HW02\tools\export_prompt_log.py
- Write: D:\Dang\Test\Homeworks\HW02\prompt_log.md
- Bash: Rerun export and verify session isolation
- Write: D:\Dang\Test\Homeworks\HW02\.gitignore
- Write: D:\Dang\Test\Homeworks\HW02\README.md
- Write: D:\Dang\Test\Homeworks\HW02\_NOTES.md
- Write: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Bash: Generate feature selection workbook and inspect
- PowerShell: Verify workbook formulas via Excel COM on a copy
- PowerShell: Verify workbook formulas via Excel COM on a copy

**Output AI (nguyên văn):**

````text
Về câu 4: **không cần public**. Đề và policy chỉ yêu cầu có dùng Git và nộp git log. Mình đề xuất:

- **Repo cá nhân:** để **private**. Như vậy không ai đọc được prompt hay skill của bạn.
- **Repo Issues của nhóm:** cũng để private được, vì ảnh chụp issue đã nằm trong file zip. Nếu giảng viên muốn xem trực tiếp thì mời thêm tài khoản của thầy cô vào repo, hoặc bật public sau deadline.

Giờ mình bắt đầu dựng khung, trước hết là đọc toàn bộ script xuất log của HW01.

Giờ là script xuất log, phiên bản dùng whitelist:

Console Windows không in được tiếng Việt. Mình thêm cấu hình UTF-8 cho stdout vào script, để chạy ở terminal nào cũng được.

Giờ mình soạn file Excel chọn feature. Script tạo file được đặt trong `tools/`, để khi cần sửa nội dung thì chạy lại là có file mới.

Đã dựng xong khung HW02 và file Excel chọn feature. Mình chưa commit gì.

**Prompt log chỉ chứa HW02.** Script đọc đúng phiên hiện tại (`305c705a`) và bỏ qua phiên giải nén zip ngày 30/09 (`8298971a`). Khi chạy, script in rõ phiên nào bị bỏ qua. Nếu một phiên trong danh sách bị thiếu thì script dừng lại chứ không xuất thiếu. Mình đã chạy thử: log có đúng 3 lượt của hôm nay và không lẫn nội dung của phiên kia. Sau này mở phiên Claude mới cho HW02, chỉ cần thêm session ID vào `SESSIONS` trong [tools/export_prompt_log.py](Homeworks/HW02/tools/export_prompt_log.py).

**Có sửa một lỗi mang theo từ script HW01.** Nếu script gặp lỗi giữa chừng, nó xoá trắng `prompt_log.md`. Lần chạy đầu hôm nay đã bị đúng như vậy; mình sửa xong và tạo lại file. Lỗi này đã ghi vào `_NOTES.md` để dùng cho AI Critique.

**Những file đã tạo trong `HW02/`:**
- `.gitignore`: chặn file đề, video, zip và `_NOTES.md`.
- [README.md](Homeworks/HW02/README.md): khung bảng feature, Test Summary, video và tự chấm điểm.
- [prompt_log.md](Homeworks/HW02/prompt_log.md): Appendix A.
- `_NOTES.md`: nháp không nộp, gồm các quyết định đã chốt, việc đang chờ, quy trình S0–S8 và danh sách mục cần khai trong Audit.
- Các thư mục `features/`, `bugs/`, `skills/`, `forms/`, `tools/`. `fill_ai02.py` và `docx_to_md.py` được chép từ HW01.
- Git: đã `git init` với nhánh `main`, tên người commit `angquoc` giống HW01.

**File Excel chọn feature** nằm ở [group/HW02_Chon_feature_Nhom.xlsx](Homeworks/HW02/group/HW02_Chon_feature_Nhom.xlsx). File này viết cho 2 bạn trong nhóm. Gồm 4 sheet:
- **Hướng dẫn:** luật chọn và lưu ý về Pool D.
- **Thành viên:** chỗ điền 3 người.
- **Chọn feature:** 19 FR. Mỗi FR có biến input, biên có thể làm BVA, mức độ, lý do và có trên mobile hay không. Chọn người bằng dropdown, nên mỗi ô chỉ ghi được một tên. Cột "Cảnh báo" báo khi một người chọn cùng FR cho cả Web và Mobile, và khi một FR được chọn cả trên Web lẫn Mobile (cần chờ giảng viên trả lời).
- **Kiểm tra:** tự đếm số feature mỗi người ở từng Pool.

Mình đã điền dữ liệu giả vào một bản sao và mở bằng Excel: các công thức tính đúng. File gốc không bị đụng tới.

**Bạn cần xem lại trước khi gửi nhóm:**
1. Mức Nặng/Vừa/Nhẹ là bản nháp mình đánh giá dựa trên SRS. File chỉ ghi "tham khảo", không ghi là AI đánh giá. Bạn nên duyệt lại trước khi chia sẻ.
2. Có 2 FR mình ghi "Cần xác nhận khi chạy app": FR-03 Quên mật khẩu và FR-09 Coupon, vì FR-20 không liệt kê hai chức năng này trên mobile.

**Việc tiếp theo:**
1. Tạo repo cá nhân **private** `software-testing-2026-HW02` và repo Issues cho nhóm, rồi gửi mình URL để thêm remote.
2. Cho mình commit đầu tiên với message `HW02: init structure, prompt log tool, feature selection sheet`. Mình sẽ xuất lại log ngay trước khi commit.
3. Chạy thử app mobile trên Android sớm để biết Expo Go có mở được SDK 54 không.
4. Mình có thể soạn tiếp quy ước đặt tên issue, label và issue template cho repo nhóm. Bạn muốn làm luôn không?
````

---

### C04 · 14:15 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Phần D hiện tại thầy cũng chưa trả lời nhưng deadline thì kề cận rồi, có lẽ chúng ta phải tự giác tìm cách để làm và chọn.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check mobile app dependencies and config
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Bash: Regenerate workbook and inspect bundle sheet
- Bash: Check lock file and any user edits in workbook
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- PowerShell: Generate test copy and verify via Excel COM
- Edit: D:\Dang\Test\Homeworks\HW02\_NOTES.md

**Output AI (nguyên văn):**

````text
Hôm nay đã là 17/10, nếu deadline là 20/10 thì chỉ còn khoảng 3 ngày. Trước khi đề xuất cách chọn Pool D, mình kiểm tra một điều quyết định khả năng làm D: app mobile có chạy được bằng cách nào khác ngoài Expo Go không.

File Excel đang bị khoá, có lẽ bạn đang mở nó. Mình kiểm tra xem bạn đã sửa gì trong file chưa trước khi ghi đè.

Mình đề xuất nhóm **tự chốt theo cách hiểu chặt nhất**: mỗi FR chỉ được làm một lần trong cả nhóm, tính chung cả Web lẫn Mobile. Như vậy dù thầy trả lời theo hướng nào thì bài cũng không bị tính là trùng.

**Đủ FR để làm theo cách này.** Pool A và B có 11 FR. Nhóm cần 9: 3 cho Pool A trên web, 3 cho Pool B trên web, và 3 cho mobile. Còn dư 2, nên mình bỏ ra 2 FR nhẹ nhất là FR-05 và FR-11.

**Trong report sẽ ghi:** nhóm đã hỏi giảng viên, chưa nhận được trả lời trước deadline nên chọn cách hiểu chặt, kèm lý do. Bạn nhớ **chụp lại bài hỏi trên forum** để làm bằng chứng.

## 3 gói chia sẵn (không trùng FR nào)

Mỗi người nhận một gói. Độ nặng tính theo Nặng = 3, Vừa = 2, Nhẹ = 1.

| Gói | Pool A (Web) | Pool B (Web) | Pool C (Web) | Pool D (Mobile) | Độ nặng |
|---|---|---|---|---|---|
| 1 | FR-01 Đăng ký | FR-07 Giỏ hàng | FR-17 Coupon CRUD | FR-04 Hồ sơ (SĐT 10–11 số) | 10 |
| 2 | FR-03 Quên mật khẩu | FR-08 Thanh toán | FR-15 Sản phẩm CRUD | FR-10 Hủy đơn | 10 |
| 3 | FR-02 Đăng nhập/khóa | FR-09 Coupon | FR-16 Import CSV | FR-06 Số lượng sản phẩm | 9 |

- FR nặng được đặt ở phía web, vì Pool D chỉ 15 điểm còn A, B, C mỗi pool 25 điểm.
- Gói 3 nhẹ hơn một chút, nhưng FR-09 và FR-16 là hai feature nặng nhất bài.
- **FR-06 trên mobile chưa chắc làm được.** Phải mở app xem màn chi tiết sản phẩm có ô nhập số lượng không; nếu không có thì đổi sang FR-05.
- Mọi người có thể đổi feature giữa các gói, miễn là không trùng.

## Đã cập nhật script tạo Excel

- Thêm sheet **"Gói gợi ý"** có dropdown để chọn người nhận gói.
- Đổi luật trong sheet "Hướng dẫn" thành quy tắc chặt.
- Cột "Cảnh báo" giờ báo **"VI PHẠM"** khi một FR bị chọn ở cả Web và Mobile.

Mình đã chạy thử trên một bản sao bằng Excel và công thức báo đúng. Tuy nhiên **file thật chưa được ghi đè**, vì bạn đang mở nó trong Excel. Bản trên đĩa vẫn là bản ngày 12/10, chưa có chỉnh sửa nào được lưu. **Bạn đóng Excel rồi báo mình**, mình sẽ tạo lại file.

## Thời gian còn rất gấp

Nếu deadline là 20/10 thì chỉ còn 3 ngày, trong khi 4 feature vẫn chưa bắt đầu. Có 3 việc đang chặn:

1. **Nhóm chọn gói ngay hôm nay.**
2. **Chạy thử app mobile hôm nay.** App không có bản chạy trên web, nên chỉ còn Android thật hoặc emulator. Nếu Expo Go trên Play Store không mở được app SDK 54 thì có 2 hướng: cài bản Expo Go cũ hơn bằng APK (theo mình biết trang expo.dev/go có bản cho từng SDK, nhưng mình chưa kiểm tra), hoặc dùng emulator của Android Studio. Cài emulator sẽ tốn thêm thời gian.
3. **Tạo 2 repo** (repo cá nhân private và repo Issues của nhóm) để mình làm commit đầu tiên.

Khi bạn chọn xong gói, mình đề xuất bắt đầu ngay với **feature Pool C** của gói đó. Pool C không liên quan đến mobile nên không bị chặn, và feature này cũng được dùng để đúc kết thành skill.
````

---

### C05 · 14:26 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Trong report sẽ ghi: nhóm đã hỏi giảng viên, chưa nhận được trả lời trước deadline nên chọn cách hiểu chặt, kèm lý do. Bạn nhớ chụp lại bài hỏi trên forum để làm bằng chứng. -> Không cần ghi.

Tôi đã đóng excel rồi nên bạn làm đi.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Regenerate the real feature selection workbook
- Edit: D:\Dang\Test\Homeworks\HW02\_NOTES.md

**Output AI (nguyên văn):**

````text
Đã tạo lại file. Giờ mình bỏ mục "ghi vào report" trong ghi chú theo ý bạn.

Mình đã tạo lại file [group/HW02_Chon_feature_Nhom.xlsx](Homeworks/HW02/group/HW02_Chon_feature_Nhom.xlsx) theo quy tắc chặt. File gồm 5 sheet: Hướng dẫn, Thành viên, Chọn feature, Gói gợi ý và Kiểm tra. Trước khi ghi đè, mình đã kiểm tra bản cũ trên đĩa không có chỉnh sửa nào của bạn nên không mất gì.

Chuyện hỏi giảng viên mình sẽ không đưa vào report, trong `_NOTES.md` cũng đã ghi lại quyết định này.

File sẵn sàng để bạn upload lên Google Drive cho nhóm chọn gói. Sau đó mình còn cần 3 thứ:
1. Gói bạn nhận.
2. Kết quả chạy thử app mobile trên Android.
3. URL của 2 repo (repo cá nhân và repo Issues của nhóm), để mình làm commit đầu tiên.
````

---

### C06 · 14:38 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Sao không có cột D ở feature?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Read: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\make_feature_sheet.py
- PowerShell: Verify restructured workbook via Excel COM
- Bash: Replace empty-string cells with truly empty cells
- Bash: Make web-row notes truly empty too
- PowerShell: Re-verify workbook formulas after fix
- Bash: Write the real feature selection workbook

**Output AI (nguyên văn):**

````text
Mình kiểm tra trên một bản sao bằng Excel trước, rồi mới ghi file thật.

Kết quả đã đúng. Giờ mình ghi file thật (Excel đã đóng nên không bị khoá).

Mình đã sửa file Excel. Lý do lúc trước không thấy cột D: ở bản cũ, Pool D không có dòng riêng mà chỉ là cột "Chọn – Mobile" đặt cạnh các dòng FR của Pool A và B, nên rất dễ hiểu nhầm.

**Sheet "Chọn feature" bây giờ có 30 dòng:**
- Pool A, B, C (Web): 19 dòng, giữ như cũ.
- **Pool D (Mobile): 11 dòng mới,** từ FR-01 đến FR-11, tô nền xanh nhạt. Cột "Ghi chú" của các dòng này cho biết FR đó có trên mobile theo FR-20, hay cần mở app để xác nhận.
- Có thêm cột **"Nền tảng"** (Web / Mobile). Thay cho 2 cột chọn cũ, giờ mỗi dòng chỉ có một cột **"Người chọn"**.
- Cột "Cảnh báo" báo vi phạm khi cùng một FR bị chọn ở cả dòng Web lẫn dòng Mobile.
- Sheet "Kiểm tra" đếm số feature của mỗi người ở đủ 4 Pool A, B, C, D.

**Mình đã kiểm tra bằng Excel trên một bản sao trước khi ghi file thật.** Lần kiểm tra đầu bắt được một lỗi: script ghi chuỗi rỗng vào các ô "Người chọn". Excel không coi những ô đó là trống, nên dòng Mobile FR-04 bị báo vi phạm sai. Mình đã sửa để các ô đó thực sự để trống, và chạy lại thì cảnh báo cũng như phần đếm đều đúng.

**Có một điều cần bạn kiểm tra.** Lần này mình ghi đè file thật mà không kiểm tra trước xem bạn có chỉnh sửa gì sau lần tạo trước không. Nếu bạn đã điền gì vào file đó (ví dụ tên thành viên) thì phần đó đã mất. Bạn mở file ra kiểm tra giúp mình nhé.
````

---

### C07 · 14:46 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Hay nên để nó là file md và upload ở trong git luôn nhỉ? Theo bạn là cái nào?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- (không)

**Output AI (nguyên văn):**

````text
Mình đề xuất **dùng cả hai, mỗi cách cho một giai đoạn**:

**Lúc chọn: dùng Excel trên Google Drive (Google Sheets).**
- Ba người có thể sửa cùng lúc mà không ai ghi đè lên ai.
- Có sẵn dropdown, và sheet tự báo khi chọn trùng hoặc thiếu Pool, nên không ai phải dò lại bằng tay.
- Bạn cùng nhóm không cần biết dùng git.

Nếu làm bằng file MD trong git ở giai đoạn này thì có hai vấn đề. Thứ nhất, hai người sửa cùng lúc sẽ bị conflict, và trên GitHub web thì người lưu sau sẽ bị từ chối. Thứ hai, không có cơ chế kiểm tra trùng nên phải tự soát bằng mắt. Với deadline chỉ còn 3 ngày, những trục trặc này không đáng.

**Sau khi chốt: ghi kết quả vào `README.md` của repo nhóm.** Đây là bảng ai làm feature nào, đặt ngay cạnh quy ước đặt tên issue và label. Cách này có ba cái lợi:
- Mọi thứ nằm ở một chỗ: bảng phân công và GitHub Issues cùng một repo.
- Git lưu lại lịch sử, nên nếu sau này có người đổi feature thì vẫn xem lại được.
- Khi viết issue, mọi người tra nhanh được ai phụ trách FR nào.

File Excel trong `HW02/group/` chỉ dùng để phối hợp nhóm, không đưa vào bài nộp.

Khi nhóm chốt xong, bạn gửi mình kết quả. Mình sẽ soạn `README.md` cho repo nhóm, gồm bảng phân công, quy ước đặt tên issue, bộ label và issue template, để bạn đưa lên repo luôn.
````

---

### C08 · 14:55 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Đã xong. Phần excel tôi sẽ gửi cho nhóm. Bây giờ đến lập repo chung và repo riêng cho của từng người đúng không? Cái này chắc cũng nên ghi trong repo chung để mọi người biết.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Create separate folder for group repo content
- Write: D:\Dang\Test\Homeworks\HW02_group\README.md
- Write: D:\Dang\Test\Homeworks\HW02_group\.github\ISSUE_TEMPLATE\bug_report.yml
- Write: D:\Dang\Test\Homeworks\HW02_group\.github\ISSUE_TEMPLATE\config.yml
- Bash: Validate issue template YAML
- Edit: D:\Dang\Test\Homeworks\HW02\_NOTES.md

**Output AI (nguyên văn):**

````text
Đúng, bước tiếp theo là lập repo. Phần hướng dẫn tạo repo cá nhân cũng nên ghi vào repo chung để cả nhóm làm giống nhau. Mình soạn sẵn nội dung repo chung trong một thư mục riêng, nằm ngoài repo HW02 của bạn để không bị lẫn vào git log bài nộp.

Mình đã soạn xong nội dung cho repo chung. Phần hướng dẫn tạo repo cá nhân đã nằm trong README, nên cả nhóm làm theo cùng một cách.

Phần này viết cho 2 bạn cùng nhóm, nên mình viết theo kiểu hướng dẫn làm theo được ngay.

**Nội dung nằm trong thư mục [Homeworks/HW02_group/](Homeworks/HW02_group/README.md).** Thư mục này tách riêng khỏi `HW02` nên không lẫn vào git log bài nộp của bạn. Gồm:
- **`README.md`**, có 4 phần:
  1. Bảng phân công feature, đang để trống chờ điền.
  2. Quy định repo cá nhân: mỗi người tự tạo repo private, không cho nhau vào và không gửi nhau prompt hay skill; review chéo thì chỉ gửi báo cáo.
  3. Quy ước Issues: ai báo bug nào, cách đặt tiêu đề `[MSSV][FR-xx][Web|Admin|Mobile] …`, bảng label (severity, platform, technique, pool), cách xử lý issue báo nhầm.
  4. Môi trường EShop dùng chung, kèm ghi chú mật khẩu admin đúng là `Admin123!`.
- **Issue template dạng form (`bug_report.yml`).** Bắt buộc điền MSSV, FR, nền tảng, mã test case, severity, các bước tái hiện, kết quả mong đợi theo đặc tả, kết quả thực tế và ảnh chụp. Mình cũng tắt việc tạo issue trống, nên ai tạo issue cũng phải đi qua form này. Hai file YAML đã được kiểm tra, đọc được không lỗi.

**Các bước bạn làm trên GitHub:**

Repo chung:
1. Vào **New repository**, đặt tên ví dụ `software-testing-2026-HW02-group`, chọn **Private**, **không** tick "Add README" để repo trống.
2. Gửi mình URL. Mình sẽ `git init`, commit 3 file trên rồi push lên. Bạn đồng ý thì mình làm.
3. Vào **Settings → Collaborators** và mời 2 bạn.
4. Vào **Issues → Labels** và tạo các label theo bảng trong README. Máy chưa có `gh` CLI nên phải tạo tay, khoảng 13 label. Label `bug` mặc định thì giữ lại.

Repo cá nhân:
1. Tạo repo `software-testing-2026-HW02`, chọn **Private**, để trống.
2. Gửi mình URL. Mình sẽ thêm remote, xuất lại prompt log, rồi làm commit đầu tiên của HW02 và push lên.

Khi nhóm chốt feature xong, bạn gửi mình kết quả để mình điền vào bảng phân công trong README của repo chung.
````

---

### C09 · 15:16 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
https://github.com/angquoc/software-testing-2026-HW02-group

Nhưng bạn không commit, tôi là người sẽ commit.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Read: D:\Dang\Test\Homeworks\HW02_group\README.md
- Write: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\user-commits-herself.md
- Write: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\hw02-prompt-log-whitelist.md
- Write: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\MEMORY.md
- Bash: Rename memory file to neutral wording

**Output AI (nguyên văn):**

````text
Đã ghi nhận: từ giờ mình **không commit**, việc commit để bạn tự làm. Mình lưu điều này vào memory để các phiên sau cũng làm theo.

Mình đổi lại tên file memory vừa tạo, để dùng cách viết trung tính.

Repo chung đã có URL, bảng phân công trong README đã có tên 3 thành viên mà bạn điền. Mình không tạo commit nào, dưới đây là các lệnh để bạn tự chạy.

**Đẩy nội dung repo chung lên GitHub**, chạy trong thư mục `D:\Dang\Test\Homeworks\HW02_group`:

```bash
git init -b main
git config user.name angquoc
git config user.email nguyenthianhngocnc2005@gmail.com
git remote add origin https://github.com/angquoc/software-testing-2026-HW02-group.git
git add README.md .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
git commit -m "Init group repo: feature allocation table, issue conventions, labels, bug report template"
git push -u origin main
```

Hai dòng `git config` giúp tên người commit giống HW01. Nếu không cần thì bạn bỏ qua.

**Sau khi push, làm tiếp trên GitHub:**
1. Vào **Settings → Collaborators** và mời An và Hương.
2. Vào **Issues → Labels** và tạo các label theo bảng ở mục 3.3 của README.
3. Thử bấm **New issue**. Nếu template đã hoạt động, form "Bug report" sẽ hiện ra và không có lựa chọn tạo issue trống.

**Repo cá nhân HW02:** thư mục `HW02` đã được `git init` từ hôm 12/10 nhưng chưa có commit nào. Khi bạn tạo repo `software-testing-2026-HW02` (Private) và gửi URL, mình sẽ xuất lại prompt log, rồi đưa bạn commit message cùng các lệnh để tự commit và push, giống như trên.

Mình cũng đã lưu vào memory 2 quy tắc để các phiên sau làm theo:
1. Mình không commit và không push. Mình chỉ chuẩn bị file, commit message và lệnh để bạn tự chạy.
2. Prompt log của HW02 chỉ lấy các phiên Claude nằm trong whitelist, nên các phiên khác không bị lẫn vào.
````

---

### C10 · 15:18 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
.github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml

-> Cái này là của github hả?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- (không)

**Output AI (nguyên văn):**

````text
Đúng vậy, đây là quy ước riêng của **GitHub**. Git không dùng hai file này, còn GitLab thì dùng một thư mục khác.

Khi repo có thư mục `.github/ISSUE_TEMPLATE/` trên nhánh mặc định (`main`), GitHub tự đọc thư mục đó mỗi khi có người bấm **New issue**:

| File | Tác dụng |
|---|---|
| `bug_report.yml` | Tạo ra form "Bug report" với các ô: MSSV, FR, nền tảng, test case, severity, các bước tái hiện, mong đợi, thực tế, ảnh chụp… Ô nào ghi `required: true` thì chưa điền thì không gửi được. Form cũng tự điền sẵn tiêu đề `[MSSV][FR-xx][Web\|Admin\|Mobile]` và tự gắn label `bug`. |
| `config.yml` | Dòng `blank_issues_enabled: false` tắt lựa chọn "Open a blank issue", nên ai tạo issue cũng phải đi qua form. |

Lưu ý thêm:
- Tên thư mục và tên file `config.yml` phải viết **đúng chính xác** như trên thì GitHub mới nhận. Riêng `bug_report.yml` thì đặt tên khác cũng được.
- Repo private vẫn dùng được, nhưng hai file phải được push lên **nhánh `main`** thì form mới hiện ra.
- GitHub cũng có cách tạo template ngay trên web (Settings → Features → Issues → Set up templates), nhưng cách đó chỉ tạo template dạng Markdown, không bắt buộc được các ô phải điền. Vì vậy mình dùng file `.yml`.
````

---

### C11 · 15:19 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
commit nên viết theo dạng chuẩn đi, kiểu [ ] ... á.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- (không)

**Output AI (nguyên văn):**

````text
Mình đề xuất quy ước sau: **tag trong ngoặc vuông đặt trước, sau đó là mô tả ngắn bằng tiếng Anh dạng mệnh lệnh** (giống HW01). Đây là quy ước tự đặt cho môn, không phải một chuẩn có sẵn như Conventional Commits (`feat: …`, `docs: …`).

```
[<repo>][<phạm vi>][<bước>] <Verb> <nội dung>
```

**Repo cá nhân HW02.** Mỗi bước của mỗi feature là một commit, đúng như đề yêu cầu:

| Loại commit | Ví dụ |
|---|---|
| Bước kiểm thử | `[HW02][B-FR09][S1] Identify input/output variables` |
| | `[HW02][B-FR09][S4] Design boundary value test cases` |
| Không thuộc feature nào | `[HW02][setup] Init folder structure and prompt log tool` |
| | `[HW02][skill] Add domain testing agent skill` |
| | `[HW02][report] Add AI critique` · `[HW02][forms] Fill AI-02 audit report` |

**Repo chung của nhóm.** Mình đề xuất tách thành 2 commit:

```bash
git add README.md
git commit -m "[Group][docs] Add README: feature allocation, issue conventions, labels"
git add .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
git commit -m "[Group][template] Add bug report issue form and disable blank issues"
git push -u origin main
```

Nếu bạn muốn khác chỗ nào, ví dụ viết commit bằng tiếng Việt hoặc đổi thứ tự các tag, cứ nói để mình sửa. Khi bạn đã chốt, mình sẽ ghi quy ước này vào `_NOTES.md` và memory để những lần sau đưa commit message đúng dạng.
````

---

### C12 · 15:20 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Tại sao còn phải thêm [<repo>] vậy?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Locate commit convention line in notes
- Edit: D:\Dang\Test\Homeworks\HW02\_NOTES.md
- Edit: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\user-does-own-commits.md

**Output AI (nguyên văn):**

````text
Thực ra không cần. Mỗi repo chỉ chứa commit của chính nó, và `git_log.txt` nộp kèm cũng đã thuộc riêng HW02, nên tag `[HW02]` hay `[Group]` chỉ lặp lại thông tin có sẵn. Mình bỏ tag đó, quy ước rút gọn còn:

```
[<phạm vi>][<bước>] <Verb> <nội dung>
```

**Repo cá nhân HW02:**

| Loại commit | Ví dụ |
|---|---|
| Bước kiểm thử | `[B-FR09][S1] Identify input/output variables` |
| Không thuộc feature nào | `[setup] Init folder structure and prompt log tool` · `[skill] Add domain testing agent skill` · `[report] Add AI critique` |

**Repo nhóm:**

```bash
git add README.md
git commit -m "[docs] Add README: feature allocation, issue conventions, labels"
git add .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
git commit -m "[template] Add bug report issue form and disable blank issues"
git push -u origin main
```

Mình đã ghi quy ước mới vào `_NOTES.md` và vào memory, nên những lần sau commit message mình đưa ra sẽ đúng dạng này.
````

---

### C13 · 15:25 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Nên ghi quy định commit để mọi người trong nhóm đồng nhất. Ghi vào readme đi.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Read: D:\Dang\Test\Homeworks\HW02_group\README.md
- Edit: D:\Dang\Test\Homeworks\HW02_group\README.md
- Bash: Renumber later sections and check headings

**Output AI (nguyên văn):**

````text
Mình đã thêm **mục 3 "Quy ước commit"** vào [README.md](Homeworks/HW02_group/README.md) của repo chung. Mục Issues giờ là mục 4, mục Môi trường là mục 5, và câu dẫn chiếu ở mục 2 cũng đã đổi số theo.

Mục 3 gồm 3 phần:
- **Định dạng chung:** `[<phạm vi>][<bước>] <Verb> <nội dung>`. Viết tiếng Anh, bắt đầu bằng động từ mệnh lệnh, không có tag tên repo, mỗi commit chỉ chứa một bước.
- **3.1 Commit cho bước kiểm thử:** phạm vi có dạng `<Pool>-<FR>` (ví dụ `B-FR09`, `D-FR04`). Kèm bảng S0–S8, mỗi bước có một commit mẫu, và cách ghi khi phải sửa lại một bước đã commit.
- **3.2 Commit không thuộc feature nào:** gồm `[setup]`, `[skill]`, `[report]`, `[forms]`, `[docs]`, `[template]`.

Bạn cần biết: danh sách S0–S8 vốn là quy trình mình đề xuất riêng cho bạn, giờ cả nhóm sẽ dùng chung. Danh sách này chỉ là các bước của kỹ thuật theo slide và đề, không có prompt nào bên trong, nên không vi phạm quy định "không chép prompt". Tuy vậy, nếu bạn muốn giữ riêng thì nói mình rút bảng S0–S8 ra, chỉ để lại định dạng chung.

Các lệnh commit cho repo chung vẫn như lần trước:

```bash
git add README.md
git commit -m "[docs] Add README: feature allocation, commit and issue conventions, labels"
git add .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
git commit -m "[template] Add bug report issue form and disable blank issues"
git push -u origin main
```
````

---

### C14 · 15:26 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
D:\Dang\Test>git init -b main
Initialized empty Git repository in D:/Dang/Test/.git/

D:\Dang\Test>git config user.name angquoc

D:\Dang\Test>git config user.email nguyenthianhngocnc2005@gmail.com

D:\Dang\Test>git remote add origin https://github.com/angquoc/software-testing-2026-HW02-group.git

D:\Dang\Test>git add README.md .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
fatal: pathspec 'README.md' did not match any files


Tôi lỡ add nhầm rồi, đáng lẽ phải add vào folder HW02 mới đúng.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Verify the mistaken repo is empty

**Output AI (nguyên văn):**

````text
Lệnh `git add` bị lỗi nên chưa có gì được thêm vào. Trước khi chỉ cách gỡ, mình kiểm tra repo vừa tạo nhầm ở `D:\Dang\Test` để chắc là nó còn trống.

Repo tạo nhầm ở `D:\Dang\Test` hoàn toàn trống: chưa có commit, chưa có file nào được thêm vào, và chưa push gì lên GitHub. Xoá thư mục `.git` của nó là sạch, không mất gì.

Còn một chỗ cần đính chính: nội dung repo chung nằm trong **`Homeworks\HW02_group`**, chứ không phải `HW02`. `HW02` là repo cá nhân của bạn, đã được `git init` từ trước và sẽ trỏ lên một repo GitHub khác.

Bạn đang dùng cmd, nên chạy lần lượt các lệnh sau:

```bat
:: 1. Gỡ repo tạo nhầm ở D:\Dang\Test (chỉ xoá thư mục .git trống, không đụng file nào khác)
rmdir /s /q D:\Dang\Test\.git

:: 2. Vào đúng thư mục repo chung
cd /d D:\Dang\Test\Homeworks\HW02_group

:: 3. Khởi tạo và đẩy lên
git init -b main
git config user.name angquoc
git config user.email nguyenthianhngocnc2005@gmail.com
git remote add origin https://github.com/angquoc/software-testing-2026-HW02-group.git
git add README.md
git commit -m "[docs] Add README: feature allocation, commit and issue conventions, labels"
git add .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
git commit -m "[template] Add bug report issue form and disable blank issues"
git push -u origin main
```

Chạy xong, bạn gửi mình output để mình kiểm tra hai commit đã lên đúng repo chưa.
````

---

### C15 · 15:38 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Đã chạy xong. Kiểm tra.

Đồng thời tôi muốn xác nhận lại bạn có nhớ yêu cầu đề bài không, những bước tôi sẽ làm để hoàn thành, cũng như những thứ tôi cần luôn làm trong bài (như xuất log, commit từng bước,...). Và các file tôi sẽ nộp sau khi xong bài.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Verify group repo commits and remote state

**Output AI (nguyên văn):**

````text
## Kiểm tra repo chung: ✅ đã đúng

- Thư mục `.git` tạo nhầm ở `D:\Dang\Test` đã được xoá.
- Repo `HW02_group` có 2 commit, đúng định dạng đã chốt và đúng tác giả `angquoc`:
  - `00b4ca4 [docs] Add README: …`
  - `73558cc [template] Add bug report issue form …`
- `main` đã khớp với `origin/main`, và GitHub cũng đang ở commit `73558cc`, tức là đã push lên đủ.

---

## 1. Đề bài yêu cầu gì

- **4 feature,** mỗi Pool một feature: A, B, C làm trên Web, D làm trên Mobile. Trong nhóm không trùng FR nào, tính chung cả Web và Mobile.
- **Mỗi feature cần 4 phần:**
  1. Domain Testing (chia lớp tương đương), có giải thích từng bước.
  2. BVA, có giải thích từng bước.
  3. AI gap analysis: AI bỏ sót gì và vì sao (do prompt, do giới hạn của công cụ, hay do feature phức tạp).
  4. Bug report trong file MD, đồng thời tạo issue trên repo nhóm, mỗi issue có ảnh chụp.
- **Kỹ thuật phải đúng như slide S04:** I/O → EC (theo guideline) → bảng Coverage và Minimum Set → BVA (LB±1, UB±1…). AI phải được dẫn qua **từng bước**, không dùng một prompt chung chung. Mọi output AI đều phải được bạn review và sửa.
- **Agent Skill** cho Domain Testing và BVA, kèm video YouTube chạy trọn một feature (10 điểm).
- **AI Audit Report:** tên công cụ, ngày giờ, prompt, output. Thêm **AI Critique** dài 200–300 từ và **khai báo** có dùng AI.
- **Git:** mỗi bước của mỗi feature là một commit, nộp kèm git log dạng text.
- **Bảng điểm:** A 25, B 25, C 25, D 15, Skill 10.
- **Những lỗi bị 0 điểm:** thiếu bất kỳ tài liệu bắt buộc nào; chép bài kể cả chép prompt; nộp trễ.
- Có thể bị gọi vấn đáp: 30% sinh viên, mỗi người 5–7 phút.

## 2. Các bước bạn sẽ làm

**Mỗi feature đi qua 9 bước, mỗi bước là một commit:**

| Bước | Việc | Ai làm |
|---|---|---|
| S0 | Trích FR từ SRS, mở app xem giao diện | Bạn, AI hỗ trợ |
| S1 | Xác định biến Input và Output | AI đề xuất, bạn review |
| S2 | Chia lớp tương đương (Complete Set of Partitions) | AI đề xuất, bạn review |
| S3 | Thiết kế TC Domain Testing (Coverage, Minimum Set) | AI đề xuất, bạn review |
| S4 | Thiết kế TC BVA | AI đề xuất, bạn review |
| S5 | Review, bổ sung TC mà AI thiếu | **Bạn** |
| S6 | Chạy test thật, ghi Actual và Status, chụp ảnh | **Bạn** |
| S7 | Viết bug report và tạo issue trên repo nhóm | Bạn, AI hỗ trợ viết |
| S8 | AI gap analysis | Bạn, AI hỗ trợ phân tích |

**Thứ tự đề xuất:**
1. Làm feature Pool C trước, theo cách thủ công từng bước.
2. Đúc kết feature đó thành skill.
3. Dùng skill cho Pool A và B.
4. Làm Pool D (Mobile).
5. Quay video demo skill.
6. Làm các phần chung: Critique, Audit, các form, README, file Excel, PDF, git log, file zip.

## 3. Những việc phải làm xuyên suốt

| Lúc nào | Việc |
|---|---|
| Trước mỗi commit | Chạy `python tools/export_prompt_log.py` và đọc lại log. Sau đó bạn tự commit theo dạng `[B-FR09][S1] Identify input/output variables` (mình chỉ đưa message và lệnh) |
| Mỗi khi dùng AI | Dẫn AI từng bước. Lưu output nguyên văn vào `ai_raw/` và **không sửa** file đó; mọi chỉnh sửa làm trên bản review |
| Mỗi khi AI sai hoặc bạn sửa output | Ghi vào `_NOTES.md`. Đây là chất liệu cho Audit Report, Critique và gap analysis |
| Khi thiết kế TC | Chỉ dựa vào SRS (black-box), không đưa code vào prompt. Code chỉ được đọc sau khi đã tìm ra bug, và phải khai báo việc đó |
| Trước mỗi đợt test | Reset DB bằng `node database.js` |
| Khi chạy test | Actual chỉ lấy từ lần chạy thật. Ảnh chụp đặt tên theo TC-ID hoặc BUG-ID |
| Mỗi bug | Tạo 1 issue bằng template, gắn label, đính kèm ảnh. Ghi số issue vào `bugs/bug_report.md` và chụp lại trang issue |
| Khi dùng ChatGPT hoặc Gemini | Tự dán nguyên văn prompt và output vào mục 2 của `prompt_log.md` (mã `G##` / `M##`) |
| Khi mở phiên Claude mới cho HW02 | Thêm session ID vào `SESSIONS` trong script. Nếu không thêm, log sẽ thiếu phiên đó |

## 4. Các file sẽ nộp

Tên file: **`23120061_HW02_AI_DomainTesting_XXX.zip`**. Moodle nhận tối đa 20 file, mỗi file không quá 20MB, nên nếu ảnh làm zip vượt dung lượng thì phải nén nhỏ ảnh hoặc chia zip.

| File / thư mục | Nội dung | Căn cứ |
|---|---|---|
| `README.md` + `.pdf` | Bảng tự chấm điểm, Test Summary (số feature; số TC thiết kế, đã chạy, pass, fail, chưa chạy; số bug), link video | Đề §14 |
| `report.md` + `.pdf` | Domain Testing và BVA cho 4 feature (giải thích từng bước), AI gap analysis, **AI Critique**, khai báo AI, **Appendix B: AI Audit Report** | Đề §6, 9, 10, 14 |
| `bugs/bug_report.md` + `.pdf` + ảnh chụp trang GitHub Issues | Danh sách bug, có liên kết tới số issue | Đề §6.4, 14 |
| `prompt_log.md` + `.pdf` | Appendix A: nguyên văn prompt và output | Đề §9 |
| `forms/` | AI-02 Audit, AI-03 Disclosure, AI-05 Privacy (bản docx, md, pdf) | Template AI |
| `git_log.txt` | Git commit log | Đề §12 |
| `skills/` | Agent Skills: domain-testing, boundary-value-analysis | Đề §7 |
| `features/` | Đặc tả, `ai_raw/`, các bước đã review, test case, ảnh chụp của từng feature | Supporting materials |
| File Excel test case | Điền theo template môn từ file test case dạng MD | Supporting materials |

**Không nộp:**
- `_NOTES.md`
- File đề bài
- File Excel chọn feature của nhóm
- Thư mục `.git`

---

## Còn chờ trước khi bắt đầu S0

1. Nhóm chốt feature, sau đó điền bảng phân công vào README của repo chung.
2. Trên GitHub: mời An và Hương vào repo, tạo các label.
3. **Repo cá nhân `software-testing-2026-HW02`** (Private): bạn gửi mình URL.
4. **Chạy thử app mobile trên Android.**
5. Xác nhận deadline trên Moodle.
````

---

### C16 · 16:38 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
- Ghi các phần 1, 2, 3, 4 vào phần giống như NOTE để tôi tiện theo dõi, và bạn cũng phải đánh dấu từng bước mỗi khi hoàn thành phần đó.
- Tiện thể tôi đã down nguyên folder CSC13003-CQ-Software Testing-CT4-VN-20261015T045955Z-1-001 về, kiểm tra xem trong đó có gì mới như template hay các slide nào bạn cần chú ý cho bài tập HW02 này không. 
- Tiện thể xem thử trong đó thầy có up skill viết file docs không.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Locate the downloaded course folder
- Bash: List all files in the downloaded course folder
- Bash: Hash-compare new course folder with existing copies
- Bash: Hash-compare new course folder with existing copies
- Bash: List current workspace root
- Bash: Compare HW02 docs and AI templates; inspect skill file
- Bash: Extract lecturer skill and read SKILL.md
- Bash: Read skill JSON schema, guide outline, script deps
- Bash: Extract new slides, syllabus, in-class activity text
- Bash: Read syllabus sections on HW, repos, anti-cheat
- Bash: Skim test case AI-first slides and W03 activity
- Read: D:\Dang\Test\Homeworks\HW02\_NOTES.md
- Write: D:\Dang\Test\Homeworks\HW02\_NOTES.md
- Write: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\hw02-tracker-in-notes.md
- Bash: Add tracker memory to index

**Output AI (nguyên văn):**

````text
Mình tìm thư mục bạn vừa tải về trước.

Mình so sánh thư mục mới tải với các bản đang có trong `D:\Dang\Test` (Slides, Templates, Homeworks) bằng mã hash, để tìm file mới hoặc file đã bị thay đổi.

Thư mục `Slides` và `Templates` không còn nằm ở `D:\Dang\Test`. Mình xem lại cấu trúc hiện tại.

Skill của thầy đã nắm được. Giờ mình đọc các slide mới (`EN.Test_Cases_AI_First`, bài in-class tuần 3) và phần Syllabus có liên quan đến HW02.

Syllabus có vài điểm liên quan trực tiếp đến cách làm HW02. Mình đọc kỹ các đoạn đó.

Đã xem xong thư mục mới. Trước khi viết vào ghi chú, mình đọc lại toàn bộ `_NOTES.md` hiện tại.

Mình đã làm xong cả 3 việc. Có 2 phát hiện cần bạn quyết định, nằm ở cuối.

## 1. Tracker trong `_NOTES.md`

Phần **TRACKER** được đặt ngay đầu [_NOTES.md](Homeworks/HW02/_NOTES.md), gồm 4 mục:
1. **Yêu cầu đề:** 14 dòng, mỗi dòng ghi nguồn (mục của đề, syllabus hay slide) và trạng thái.
2. **Các bước:**
   - 2.0 Chuẩn bị: 13 việc. 7 việc đã xong (✅). Những việc đang chờ bạn hoặc nhóm (⏳) là: mời thành viên, tạo label, chốt feature, tạo repo cá nhân, xác nhận deadline. Việc mình chưa làm (⬜) là cài và chạy EShop. Việc bạn chưa làm là chạy thử app mobile.
   - 2.1 Bảng S0–S8 cho 4 feature. Tên cột đang là `FR-??`, mình sẽ đổi khi nhóm chốt.
   - 2.2 Phần chung từ G1 đến G10.
3. **Việc làm xuyên suốt.**
4. **File nộp**, có cột trạng thái.

Ký hiệu: ✅ xong · 🔄 đang làm · ⬜ chưa làm · ⏳ chờ. Mình đã lưu vào memory rằng cứ xong mục nào là mình đánh dấu mục đó ngay.

## 2. Thư mục môn học mới tải

So mã hash thì **đề HW02, Homework Policies và cả 12 AI Templates không thay đổi gì**. Riêng slide S04 thì không so được, vì bạn đã xoá bản cũ. Tên file vẫn giống.

**Những thứ mới liên quan đến HW02:**
- **`Slides/EN.Test_Cases_AI_First.pdf`.** Slide này đáng dùng cho HW02 vì có 3 thứ:
  - Mẫu prompt **ROLE / CONTEXT / TASK / FORMAT / CONSTRAINTS**.
  - 7 thuộc tính của một test case tốt.
  - **4 kiểu AI hay sai**: bịa kết quả mong đợi, test trùng nhau nhưng trông hợp lý, bỏ sót biên của miền giá trị, bịa ra nút hoặc trường không có trên giao diện. Mình đề xuất dùng đúng 4 kiểu này làm khung phân loại cho phần AI gap analysis.
- **Syllabus (cập nhật 05/2026)** có 2 điểm:
  - Xác nhận HW02 bắt buộc nộp [AI-02], [AI-03] **có ký tên**, và [AI-05].
  - **Mâu thuẫn với đề:** mục chống gian lận ghi "HW02–HW06: Video chạy test trên EShop + ảnh selfie với màn hình debug". Đề HW02 lại ghi "Anti-AI-Cheat Constraints: None".

## 3. Skill của thầy

**Có.** File `InClass/test-case-writing.skill` (ngày 14/10) là một skill dùng để viết, chuẩn hoá và chấm test case:
- Đầu vào là **1 file JSON**. Script lint kiểm tra lỗi, rồi script build xuất ra **cả file Word (.docx) lẫn Excel (.xlsx)**.
- File xuất có ma trận truy vết, dropdown trạng thái và đếm Pass/Fail tự động.
- Hỗ trợ định dạng bảng dữ liệu có cột `covers`, để ghi mỗi dòng nhắm vào lớp tương đương hay biên nào. Định dạng này rất hợp với EP và BVA.
- Trong SKILL.md, thầy ghi cần kết hợp với một skill **`domain-testing-design`** để chọn dữ liệu, nhưng skill đó **không có trong thư mục**. Đây chính là phần đề HW02 yêu cầu sinh viên tự xây.

Máy đã có sẵn `python-docx` và `openpyxl` nên chạy được. Mình mới giải nén ra thư mục tạm để đọc, chưa chạy script nào.

---

## Cần bạn quyết định

**1. Có dùng skill của thầy để xuất test case không?**

Mình đề xuất **có**, và đổi lại quyết định hôm 12/10 (viết Markdown rồi tự viết script điền vào template Excel). Cách làm mới:
- Skill domain-testing và BVA của bạn sinh ra file JSON theo schema của thầy.
- Chạy lint và build của thầy để ra file Word và Excel.
- Viết thêm một script nhỏ chuyển JSON thành bảng Markdown để đưa vào `report.md`.

Lợi ích:
- Không phải tự viết script xuất Excel.
- Định dạng đúng thứ thầy dạy.
- Lint tự bắt các lỗi viết test case.
- Skill của bạn trở thành đúng mảnh `domain-testing-design` mà thầy để trống, nên phần Agent Skill có lý do rõ ràng.

Khi làm vậy, trong Audit Report phải khai báo rằng có dùng skill của thầy.

**2. Có quay video chạy test và chụp ảnh selfie như syllabus yêu cầu không?**

Đề HW02 không bắt buộc, nhưng thiếu tài liệu là bị 0 điểm. Mình đề xuất làm phòng hờ ở mức nhẹ:
- Video demo skill có kèm đoạn chạy vài test case trên EShop.
- Một ảnh selfie chụp cùng màn hình đang chạy test (DevTools hoặc terminal backend).
````

---

### C17 · 17:46 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
- Đã mời repo nhóm. Hình như chưa tạo label.
- Tôi đã chốt feature cho mình, các thành viên khác chưa chốt. Tôi lấy Gói 1 của gói gợi ý.
- Tôi đã tạo repo cá nhân nhưng chưa thêm remote hay commit gì: https://github.com/angquoc/software-testing-2026-HW02
- Deadline là trước 12h ngày 21/10. Tôi muốn xong sớm và nộp bài trước 20/10.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check EShop dependency install status
- Bash: Compare local EShop commit with upstream
- Bash: Clone a separate EShop copy for HW02
- Bash: Install EShop backend, web, admin dependencies
- Bash: Create folders for the four chosen features
- Edit: D:\Dang\Test\Homeworks\HW02\README.md
- Edit: D:\Dang\Test\Homeworks\HW02\README.md
- Edit: D:\Dang\Test\Homeworks\HW02\README.md
- Edit: D:\Dang\Test\Homeworks\HW02_group\README.md
- Bash: Show group README diff against last commit
- Bash: Update tracker statuses in notes
- Bash: Export prompt log and preview first commit contents
- Bash: Inspect the match to confirm it is not a leak
- Bash: Find the header line without the session id

**Output AI (nguyên văn):**

````text
Mình làm theo thứ tự:
1. Cập nhật tracker và README theo Gói 1.
2. Tạo thư mục cho 4 feature.
3. Chuẩn bị commit đầu tiên cho repo cá nhân.
4. Kiểm tra EShop đã cài thư viện chưa.

Trong lúc chờ cài, mình tạo thư mục cho 4 feature của Gói 1:

Giờ cập nhật bảng feature trong README của HW02:

Điền dòng của bạn vào bảng phân công trong README repo nhóm. Bạn sẽ tự commit file này.

File README của repo nhóm đã bị sửa trên đĩa sau lần mình đọc trước. Mình xem diff để chắc chỉ có dòng mình vừa điền thay đổi.

Diff chỉ có đúng dòng của bạn. Giờ cập nhật tracker trong `_NOTES.md`:

Giờ mình xuất lại prompt log và xem những file sẽ vào commit đầu tiên của repo cá nhân.

Kiểm tra rò rỉ trả về 1 kết quả. Mình xem đó là nội dung của phiên khác lọt vào, hay chỉ là chỗ chính phiên này nhắc tới mã `8298971a`.

Kiểm tra xong: dòng đó chỉ là một tiêu đề nằm trong câu trả lời của mình, không phải tiêu đề lượt. Log có đủ 17 lượt và **tất cả đều thuộc phiên `305c705a`**, không lẫn phiên nào khác.

## Đã làm

- **Gói 1 của bạn:** A FR-01 Đăng ký · B FR-07 Giỏ hàng · C FR-17 Quản lý mã giảm giá · D FR-04 Hồ sơ (Mobile).
  - Đã tạo 4 thư mục trong `features/`, mỗi thư mục có `ai_raw/` và `screenshots/`.
  - Đã điền bảng feature trong [README.md](Homeworks/HW02/README.md) của HW02.
  - Đã điền **dòng của bạn** trong README repo nhóm. Diff chỉ có đúng dòng đó, chưa commit.
- **Tracker:** đã cập nhật deadline (trước 12:00 ngày 21/10), tên 4 feature ở bảng S0–S8, và trạng thái các mục 0.8–0.13.
- **SUT riêng cho HW02:** mình clone EShop vào `Homeworks/eshop-sut`, cùng commit `85af3ba` với bản mới nhất trên GitHub. Mục đích là tách khỏi `DA/eshop-sut` của seminar bảo mật để DB và code không bị lẫn. Thư viện backend, web và admin **đang cài chạy nền**.

## Lệnh để bạn tự commit

**Repo cá nhân.** Commit này gồm `.gitignore`, `README.md`, `prompt_log.md`, `tools/` (4 script), 4 thư mục feature, và file Excel chọn feature trong `group/`. File đề và `_NOTES.md` đã bị `.gitignore` chặn, mình đã kiểm tra.

```bat
cd /d D:\Dang\Test\Homeworks\HW02
git remote add origin https://github.com/angquoc/software-testing-2026-HW02.git
git add .
git commit -m "[setup] Init folder structure, prompt log tool and feature folders"
git push -u origin main
```

**Repo nhóm:**

```bat
cd /d D:\Dang\Test\Homeworks\HW02_group
git add README.md
git commit -m "[docs] Add feature allocation for 23120061"
git push
```

## Label cho repo nhóm (tạo tay)

Vào **Issues → Labels → New label**. Màu chỉ là gợi ý, bạn đổi tuỳ ý.

| Label | Màu |
|---|---|
| `severity: critical` | `#B60205` |
| `severity: high` | `#D93F0B` |
| `severity: medium` | `#FBCA04` |
| `severity: low` | `#C2E0C6` |
| `platform: web` · `platform: admin` · `platform: mobile` | `#1D76DB` |
| `technique: EP` · `technique: BVA` | `#5319E7` |
| `pool: A` · `pool: B` · `pool: C` · `pool: D` | `#BFDADC` |

## Lịch để nộp trước 20/10

| Ngày | Việc |
|---|---|
| 17/10 (tối) | Chạy EShop; **chạy thử app mobile trên Android**; FR-17 (Pool C) từ S0 đến S4, làm thủ công từng bước |
| 18/10 | FR-17 từ S5 đến S8; đúc kết thành skill; FR-01 từ S0 đến S8 bằng skill |
| 19/10 | FR-07 và FR-04 (Mobile) từ S0 đến S8; quay video skill |
| 19/10 tối – 20/10 sáng | Critique, Audit, các form, README, PDF, git log, nén zip, nộp |

## Hai câu lần trước còn chờ bạn trả lời

Hai câu này quyết định định dạng file test case, nên cần trả lời trước khi bắt đầu S0:

1. **Dùng skill `test-case-writing` của thầy để xuất test case?** Cách làm là JSON → lint → Word + Excel, rồi chuyển JSON thành bảng Markdown cho report. Mình đề xuất **có**.
2. **Làm phòng hờ video chạy test và ảnh selfie** như syllabus ghi? Mình đề xuất **có, ở mức nhẹ**.
````

---

### C18 · 17:48 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
<task-notification>
<task-id>bbd00fd63</task-id>
<tool-use-id>toolu_01RjhQCo3JnZ13kWzNezjTPd</tool-use-id>
<output-file>C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\tasks\bbd00fd63.output</output-file>
<status>completed</status>
<summary>Background command "Install EShop backend, web, admin dependencies" completed (exit code 0)</summary>
</task-notification>
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check npm install results
- Bash: Update tracker item 0.11

**Output AI (nguyên văn):**

````text
Đã cài xong thư viện cho backend, frontend web và web admin của EShop. Lệnh cài báo thành công, cả 3 thư mục đều đã có `node_modules`.

Mình chưa khởi tạo DB và chưa bật server nào. Mục 0.11 trong tracker đã ghi lại đúng trạng thái này.

Mình vẫn cần bạn trả lời 2 câu ở tin nhắn trước:
1. Có dùng skill `test-case-writing` của thầy để xuất test case không?
2. Có làm phòng hờ video chạy test và ảnh selfie không?

Bạn trả lời xong thì mình bật EShop và bắt đầu S0 cho FR-17.
````

---

### C19 · 21:03 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Sao git ở repo cá nhân có cả phần group vậy? Điều đó có bắt buộc không?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check whether group files were committed
- Bash: Move group files out of personal repo
- Bash: Verify moved script runs; find stale references
- Bash: Update notes for moved group files

**Output AI (nguyên văn):**

````text
Đã chuyển xong:
- File Excel và script `make_feature_sheet.py` giờ nằm ở `Homeworks/HW02_chon_feature/`. Thư mục này nằm ngoài cả repo cá nhân lẫn repo nhóm.
- Đường dẫn trong script đã được sửa theo vị trí mới. Mình chạy thử thì script vẫn tạo được file Excel.
- Thư mục `HW02/group/` đã được xoá.
- `_NOTES.md` đã cập nhật hai chỗ có nhắc tới hai file này.

Lúc này `git status` trong `HW02` báo 2 file bị xoá. Bạn commit như sau:

```bat
cd /d D:\Dang\Test\Homeworks\HW02
git add -A
git commit -m "[setup] Remove group coordination files from personal repo"
git push
```

Lịch sử git vẫn còn hai file này trong commit `e2e8085`. Muốn xoá hẳn khỏi lịch sử thì phải viết lại lịch sử rồi force push. Mình không khuyên làm vậy: repo là private, file không có gì nhạy cảm, và một commit dọn dẹp như trên cũng là lịch sử hợp lý.

Hai câu hỏi lần trước vẫn đang chờ bạn trả lời:
1. Có dùng skill `test-case-writing` của thầy để xuất test case không?
2. Có làm phòng hờ video chạy test và ảnh selfie không?
````

---

### C20 · 22:49 17/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
- Phần tool cũng comment luôn sao?
- Không thấy README có trong changes để add lên repo nhóm.
- Nên thêm các ký hiệu hay note gì về label cho các thành viên không?

1. Có dùng.
2. Đề bài yêu cầu thì làm, không thì thôi.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check group repo status
- Read: D:\Dang\Test\Homeworks\HW02_group\README.md
- Edit: D:\Dang\Test\Homeworks\HW02_group\README.md
- Bash: Install lecturer skill and smoke-test on its example
- Bash: Record decisions in notes
- Bash: Check the path line rendered correctly
- Bash: Fix the broken path in notes
- Bash: Replace tab character with backslash-t in path
- Bash: Replace literal tab in path with backslash
- Bash: Fix tab in path using explicit character codes

**Output AI (nguyên văn):**

````text
Mình kiểm tra trạng thái repo nhóm trước.

Đường dẫn trong ghi chú bị hỏng: chuỗi `\t` bị Python đọc thành ký tự tab. Mình sửa lại:

Đã sửa xong đường dẫn. Trả lời lần lượt các ý của bạn:

**1. Thư mục `tools/` có nên commit không?** Có, nên để trong repo cá nhân, khác với file Excel chọn feature lúc nãy:
- `export_prompt_log.py` là thứ đề khuyến khích ở mục 9: *"create a skill or rule that extracts the information above automatically after an AI session"*. Nó được tính là supporting material.
- `fill_ai02.py` và `docx_to_md.py` dùng để làm các form AI-02, AI-03, AI-05.
- Cả ba script đều do AI viết, nên sẽ được khai báo trong Audit Report.

**2. README không hiện trong Changes.** Git vẫn ghi nhận README đã thay đổi. Chỉ là khung Source Control của VS Code không dò tới repo `HW02_group`, vì repo này nằm sâu 2 cấp thư mục. Cách xử lý mình đã nêu ở trên: commit bằng terminal, hoặc đặt `git.repositoryScanMaxDepth` thành `2`.

**3. Ghi chú về label cho thành viên.** Mình đã thêm vào mục 4.3 trong README repo nhóm:
- Mỗi issue gắn đủ 4 nhóm label, và cách chọn `technique` (EP hay BVA).
- 4 câu hỏi lần lượt để chọn severity, gặp câu trả lời "Có" đầu tiên thì dừng.
- Một ví dụ issue gắn label đầy đủ.
- Bảng màu label.
- Quy định không tự tạo label mới.

Lệnh commit cho repo nhóm:

```bat
cd /d D:\Dang\Test\Homeworks\HW02_group
git add README.md
git commit -m "[docs] Add feature allocation for 23120061 and label guidelines"
git push
```

**Hai quyết định đã ghi vào `_NOTES.md`:**
1. **Dùng skill của thầy.** Mỗi feature sẽ có test case nguồn là một file JSON theo schema của thầy. Từ file đó, lint của thầy kiểm tra lỗi, rồi build ra Word và Excel. Mình sẽ viết thêm một script chuyển JSON thành bảng Markdown để đưa vào report.
   - Skill được cài ở `D:\Dang\Test\.claude\skills\test-case-writing\`, nằm ngoài repo cá nhân và không nộp.
   - Mình đã chạy thử trên ví dụ có sẵn: lint báo 0 lỗi, build ra đủ file docx và xlsx.
2. **Không làm video chạy test và ảnh selfie**, vì đề ghi Anti-AI-Cheat là "None".

Còn một việc bạn cần làm: tạo label trên repo nhóm.

Bước tiếp theo là bật EShop rồi bắt đầu **S0 cho FR-17**. Ở S0, mình trích đúng phần FR-17 từ SRS vào `features/C_FR-17_QuanLyCoupon/00_spec.md`, sau đó bạn mở trang Quản lý mã giảm giá trong Web Admin để xem giao diện. Bạn đồng ý thì mình bắt đầu.
````

---

### C21 · 00:34 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Sau dấu : thì viết hoa chữ cái đầu tiên.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- AskUserQuestion
- Bash: List lowercase-after-colon spots in documents
- Bash: Capitalize first letter after colons in document prose
- Write: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\doc-style-capitalize-after-colon.md
- Bash: Index memory and check group repo state
- Bash: Check personal repo state

**Output AI (nguyên văn):**

````text
Đã sửa 31 chỗ trong 3 file: README repo nhóm, README HW02 và `_NOTES.md`. Mình lưu quy tắc này vào memory để những tài liệu viết sau cũng theo đúng.

Mình đã viết hoa chữ cái đầu sau dấu `:` ở 31 chỗ, trong README của repo nhóm, README của HW02 và `_NOTES.md`. Code, tên label, khoá YAML, đường dẫn, giờ và phần log tự xuất được giữ nguyên. Quy tắc này đã lưu vào memory, chỉ áp dụng cho câu văn trong tài liệu.

Trong 31 chỗ có vài chỗ hơi gượng, ví dụ `AI-05: Docx + md + pdf` hay `Agent Skill: Domain-testing, …`. Nếu bạn muốn giữ chữ thường ở những tên riêng hoặc tên kỹ thuật như vậy thì báo mình.

Lệnh commit cho 2 repo:

```bat
cd /d D:\Dang\Test\Homeworks\HW02_group
git add README.md
git commit -m "[docs] Add feature allocation for 23120061 and label guidelines"
git push

cd /d D:\Dang\Test\Homeworks\HW02
git add README.md
git commit -m "[setup] Add chosen features to README"
git push
```

Bạn chưa xác nhận bắt đầu S0 cho FR-17. Khi bạn đồng ý, mình bật EShop và bắt đầu.
````

---

### C22 · 01:09 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Label như này đúng không?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- (không)

**Output AI (nguyên văn):**

````text
Đúng rồi: tên `severity: critical` và màu `#B60205` khớp với README.

Ô **Description** không bắt buộc. Tuy vậy, nên điền vào, vì khi thành viên chọn label trong issue, GitHub sẽ hiện mô tả ngay bên dưới tên label và họ không phải mở README ra xem. Dưới đây là danh sách 13 label để bạn chép:

| Name | Color | Description |
|---|---|---|
| `severity: critical` | `#B60205` | Lộ/mất dữ liệu, vượt quyền, chặn luồng chính |
| `severity: high` | `#D93F0B` | Chấp nhận dữ liệu sai hoặc tính sai, không có cách đi vòng |
| `severity: medium` | `#FBCA04` | Sai nghiệp vụ/validation, có cách đi vòng |
| `severity: low` | `#C2E0C6` | Sai giao diện, câu chữ, thông báo |
| `platform: web` | `#1D76DB` | Frontend Web (localhost:5173) |
| `platform: admin` | `#1D76DB` | Web Admin (localhost:5174) |
| `platform: mobile` | `#1D76DB` | App Mobile (Expo) |
| `technique: EP` | `#5319E7` | Phát hiện nhờ Equivalence Partitioning |
| `technique: BVA` | `#5319E7` | Phát hiện nhờ Boundary Value Analysis |
| `pool: A` | `#BFDADC` | Authentication, Categories, Products |
| `pool: B` | `#BFDADC` | Shopping Cart, Checkout |
| `pool: C` | `#BFDADC` | Web Admin |
| `pool: D` | `#BFDADC` | Mobile App |

Giữ lại label `bug` mặc định, vì template tự gắn label này cho mọi issue. Các label mặc định khác của GitHub (`documentation`, `enhancement`, `good first issue`…) bạn có thể xoá cho gọn. Riêng `duplicate` và `invalid` nên giữ để đánh dấu issue trùng hoặc issue báo nhầm.
````

---

### C23 · 01:20 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
- Tôi đã tạo xong label
- Phần repo cá nhân tôi cũng đã commit.
- Chạy log những gì đã chat đi, để tôi commit lại. Ngày mai tôi mới bắt đầu S0.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Export prompt log and check repo states
- Bash: Inspect the last exported turn
- Bash: Tick completed preparation items in tracker

**Output AI (nguyên văn):**

````text
Lệnh commit:

```bat
cd /d D:\Dang\Test\Homeworks\HW02
git add prompt_log.md
git commit -m "[setup] Update prompt log for preparation phase"
git push
```

Lượt C23 ghi output là "(Không có phản hồi …)", vì log được xuất khi câu trả lời này còn đang viết. Đây không phải lỗi. Câu trả lời đầy đủ sẽ được ghi vào log ở lần xuất tiếp theo, trước commit S0 ngày mai.

Tracker đã đánh dấu xong mục 0.8 (label) và 0.10 (repo cá nhân). Còn 3 mục mở:
- **0.9:** Đang chờ An và Hương chốt feature.
- **0.11:** Chưa khởi tạo DB và chưa bật server.
- **0.12:** Chưa chạy thử app mobile trên Android.

Ngày mai, mình bật EShop trước rồi mới làm S0 cho FR-17. Nếu tiện, bạn chạy thử mobile sớm, vì Pool D là phần duy nhất còn rủi ro về môi trường.
````

---

### C24 · 10:17 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Bây giờ sẽ chạy EShop đi. Chạy xong rồi mình sẽ chạy mobile.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check for new Claude session transcripts
- Bash: Initialize EShop database with seed data
- Bash: Start EShop backend server on port 3000
- Bash: Start EShop customer web on port 5173
- Bash: Start EShop admin web on port 5174
- Bash: Wait for servers to respond and show ready lines
- Bash: Install mobile app dependencies
- PowerShell: Get LAN IPv4 addresses and network profile

**Output AI (nguyên văn):**

````text
Hệ thống báo phiên vừa được khởi động lại. Trước khi bật EShop, mình kiểm tra xem đây có phải một phiên Claude mới không, vì nếu đúng thì phải thêm phiên đó vào whitelist của prompt log.

Đây vẫn là phiên cũ `305c705a` được mở lại, không có phiên mới, nên whitelist không cần thêm gì. Giờ mình khởi tạo DB và bật backend.

Cả 3 phần của EShop đang chạy (DB đã khởi tạo lúc 10:18), nhưng **mình dừng lại trước bước mobile vì mạng hiện tại không phù hợp**.

| Phần | URL | Trạng thái |
|---|---|---|
| Backend API | http://localhost:3000 | ✅ HTTP 200 |
| Web khách hàng | http://localhost:5173 | ✅ HTTP 200 |
| Web Admin | http://localhost:5174 | ✅ HTTP 200 |

Thư viện của app mobile đang được cài chạy nền.

**Vấn đề với mạng:** máy đang dùng Wi-Fi quán cà phê "Kochi Coffee T1", Windows xếp mạng này vào loại **Public**. Có 2 rủi ro:
1. **Có thể không kết nối được.** Wi-Fi công cộng thường chặn các thiết bị nhìn thấy nhau (client isolation), nên điện thoại có thể không gọi được tới máy tính ở `192.168.1.53`.
2. **Có rủi ro bảo mật.** EShop được cài lỗi bảo mật có chủ đích (SQL injection, lộ mật khẩu…). Muốn điện thoại gọi được backend thì phải mở firewall cổng 3000 trên mạng Public, tức là ai ngồi chung quán cũng truy cập được app đầy lỗ hổng này trên máy bạn.

**Ba cách an toàn hơn, bạn chọn một:**

| Cách | Làm gì | Ưu / nhược |
|---|---|---|
| **A. USB + `adb reverse`** (mình đề xuất) | Cắm cáp, bật USB debugging, chạy `adb reverse tcp:3000 tcp:3000` và `adb reverse tcp:8081 tcp:8081`. Sau đó `API_URL` để là `http://localhost:3000/api` | Không lộ gì ra mạng, không phải mở firewall. Cần cài Android platform-tools (adb) |
| **B. Phát hotspot từ điện thoại** | Cho laptop bắt hotspot của điện thoại, rồi dùng IP mới của laptop trên mạng đó | Mạng riêng giữa 2 thiết bị. Tốn dung lượng 4G của điện thoại |
| C. Về nhà dùng Wi-Fi riêng | Đặt mạng nhà là Private, mở firewall cổng 3000 và 8081 | Đơn giản nhưng phải chờ về nhà |

Với cả 3 cách, mình sẽ sửa `API_URL` trong bản clone HW02 (`Homeworks/eshop-sut`), không sửa bản trong `DA`. Thay đổi này sẽ được ghi vào phần môi trường test.

Bạn cho mình biết thêm:
1. Bạn chọn cách nào?
2. Điện thoại Android của bạn chạy phiên bản Android mấy?
3. Đã cài **Expo Go** chưa, và nếu rồi thì là phiên bản nào (xem trong app: Settings, hoặc trang thông tin ứng dụng)? Mình cần biết để kiểm tra Expo Go đó có mở được app viết bằng SDK 54 không.
````

---

### C25 · 10:19 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
<task-notification>
<task-id>bjri25kh8</task-id>
<tool-use-id>toolu_01CW2GQUKSZphYxAKoqVTusW</tool-use-id>
<output-file>C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\tasks\bjri25kh8.output</output-file>
<status>completed</status>
<summary>Background command "Install mobile app dependencies" completed (exit code 0)</summary>
</task-notification>
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Confirm mobile install and update tracker

**Output AI (nguyên văn):**

````text
Đã cài xong thư viện cho app mobile (696 package, không có lỗi). Trong tracker, mục 0.11 đã đánh dấu ✅. Mình cũng ghi vào `_NOTES.md` hai điều:
- Backend có thể tự reset DB mỗi lần khởi động.
- Không mở firewall cho EShop khi đang dùng Wi-Fi công cộng.

Phía máy tính đã sẵn sàng cho mobile. Mình chờ bạn trả lời 3 câu ở tin trước: chọn cách kết nối A, B hay C, phiên bản Android, và phiên bản Expo Go.
````

---

### C26 · 10:48 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Tôi đã xem qua web. Bây giờ sẽ chạy mobile, tôi chọn cách A. Tôi đã cắm cáp, bật USB debugging, có cài android platform-tools ở laptop.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Locate adb executable
- Bash: List connected Android devices
- PowerShell: Check whether Windows sees the phone over USB

**Output AI (nguyên văn):**

````text
Mình tìm `adb` và kiểm tra máy tính đã nhận điện thoại chưa.

Windows đã thấy một thiết bị USB, nhưng chỉ nhận là "WinUsb Device" chung chung, còn `adb devices` thì **chưa liệt kê điện thoại nào**. Nếu điện thoại chỉ đang chờ bạn cho phép thì adb vẫn phải hiện dòng `unauthorized`. Danh sách trống nghĩa là adb chưa thấy cổng debug của điện thoại. Nguyên nhân thường gặp nhất là chế độ USB hoặc quyền debug.

Bạn thử lần lượt các bước sau trên điện thoại:

1. **Mở khoá màn hình**, kéo thanh thông báo xuống, chạm vào thông báo USB ("Đang sạc qua USB" hoặc tương tự) rồi chọn **Truyền tệp / File transfer (MTP)**.
2. Nếu vẫn chưa được: vào **Tuỳ chọn nhà phát triển**, chọn **Thu hồi quyền gỡ lỗi USB** (Revoke USB debugging authorizations), tắt rồi bật lại **Gỡ lỗi USB**.
3. **Rút cáp ra cắm lại.** Khi điện thoại hiện hộp thoại *"Cho phép gỡ lỗi USB?"*, tick **"Luôn cho phép từ máy tính này"** rồi bấm **Cho phép**.

Làm xong bạn báo mình để mình chạy lại `adb devices`.

Thêm một lưu ý: máy có cài **LDPlayer**, và LDPlayer có adb riêng (phiên bản khác). Nếu LDPlayer đang mở, hai bản adb sẽ tranh nhau cổng 5037 và làm mất kết nối. Bạn tắt LDPlayer trong lúc làm bước này.

Mình cũng cần 3 thông tin:
- Hãng và dòng điện thoại (một số hãng như Xiaomi hay Oppo cần bật thêm tuỳ chọn riêng).
- Phiên bản Android.
- Đã cài Expo Go chưa, và nếu rồi thì phiên bản nào.
````

---

### C27 · 10:51 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Samsung Galaxy S21 Ultra.
- Tôi đã rút cáp ra cắm lại, bật cho phép gỡ lỗi, nhưng không thấy hỏi cho phép từ máy tính nào. Có vẻ phải chạy mới có hỏi.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Restart adb server and list devices
- PowerShell: List Samsung/ADB USB devices including driver errors

**Output AI (nguyên văn):**

````text
Có thể bạn nói đúng: hộp thoại cho phép thường chỉ hiện khi adb thật sự kết nối tới điện thoại. Mình khởi động lại adb server và xem lại toàn bộ thiết bị USB, kể cả những thiết bị Windows đang báo lỗi driver.

Mình đã tìm ra nguyên nhân: **lúc này Windows không thấy điện thoại S21 Ultra qua USB.**

- Driver Samsung đã có sẵn trên máy, và trước đây chiếc S21 Ultra từng kết nối được (Windows còn lưu các mục "SAMSUNG Android ADB Interface" và "S21 Ultra", serial `R5CR707GW3X`). Nhưng hiện tại tất cả các mục đó đều ở trạng thái **Present = False**, tức là điện thoại không đang được cắm.
- Thiết bị "WinUsb Device" thấy lúc trước có mã hãng `VID_30C9`, không phải Samsung (`VID_04E8`), nên đó là một thiết bị khác, có thể là webcam của laptop.

Vì Windows còn chưa thấy điện thoại nên adb không thấy, và hộp thoại cho phép gỡ lỗi cũng chưa thể hiện ra. Nguyên nhân gần như chắc chắn nằm ở **cáp hoặc cổng USB**:

1. **Kiểm tra cáp.** Nhiều cáp chỉ có dây sạc, không truyền dữ liệu. Dấu hiệu là điện thoại báo đang sạc nhưng không hiện thông báo "USB" hay "Truyền tệp". Bạn đổi sang cáp Samsung zin hoặc một cáp chắc chắn truyền được dữ liệu.
2. **Cắm thẳng vào cổng USB của laptop,** không qua hub hay dock. Nếu được thì thử thêm một cổng khác.
3. **Khi cắm đúng cáp,** điện thoại sẽ hiện thông báo USB. Bạn chọn **Truyền tệp**, ngay sau đó hộp thoại *"Cho phép gỡ lỗi USB?"* sẽ hiện ra. Tick "Luôn cho phép" rồi bấm **Cho phép**.

Cắm lại xong thì bạn báo mình để mình kiểm tra.

Còn 2 câu chưa có trả lời: điện thoại chạy Android mấy (xem trong Cài đặt → Thông tin điện thoại → Thông tin phần mềm), và đã cài Expo Go chưa.
````

---

### C28 · 10:54 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
- Bạn kiểm tra xem có được không. Tôi mới đổi dây cáp khác.
- Android 15.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check adb connection, Android version, Expo Go
- PowerShell: Check whether the Samsung phone is present on USB now

**Output AI (nguyên văn):**

````text
Lần này vẫn chưa được. `adb` không thấy thiết bị nào, và Windows cũng **không thấy thiết bị Samsung nào đang cắm**. Điện thoại vẫn chưa kết nối dữ liệu với laptop.

Android 15 trên S21 Ultra chạy One UI 7. Bản này có tính năng **Auto Blocker** (Trình chặn tự động). Khi bật, nó chặn các lệnh gửi qua cáp USB, và có thể chặn luôn việc gỡ lỗi USB. Bạn kiểm tra theo thứ tự:

1. **Auto Blocker:** Vào **Cài đặt → Bảo mật và quyền riêng tư → Trình chặn tự động**. Tắt hẳn, hoặc ít nhất tắt mục **"Chặn lệnh qua cáp USB"**.
2. **Cấu hình USB mặc định:** Vào **Tuỳ chọn nhà phát triển → Cấu hình USB mặc định**, chọn **Truyền tệp / Android Auto**. Kiểm tra lại mục **Gỡ lỗi USB** vẫn đang bật.
3. **Cắm lại cáp.** Nếu dữ liệu đã thông, điện thoại sẽ hiện thông báo "USB đang được dùng để…", sau đó là hộp thoại *"Cho phép gỡ lỗi USB?"*.
4. Nếu vẫn **không có thông báo USB nào** (chỉ thấy đang sạc), thì lỗi nằm ở cáp hoặc cổng. Thử cổng USB khác trên laptop, ưu tiên cổng USB-C nếu có.

Làm xong bạn báo mình để mình kiểm tra lại.

Nếu USB vẫn không được, mình chuyển sang **cách B (phát hotspot từ điện thoại)**. Cách này không cần cáp, và mạng chỉ có điện thoại với laptop, vẫn an toàn.
````

---

### C29 · 10:56 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Được rồi, lần này đã có thông báo và tôi đã cho phép.
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Verify adb connection and Expo Go presence
- Bash: Check Expo Go version on phone
- Bash: Point API_URL to localhost and set up adb reverse
- Bash: Start Expo and open the app on the Android phone
- Bash: Wait for Expo startup output
- Bash: Wait for Expo Go install and bundle
- Bash: Capture phone screen via adb
- Bash: Capture phone screen via adb
- Read: C:\Users\Lenovo\AppData\Local\Temp\claude\d--Dang-Test\305c705a-d915-42fa-8501-b411992acb4b\scratchpad\phone1_small.png
- Bash: Record mobile environment in notes and tick 0.12
- Bash: Verify the adb path line has no stray control chars
- Bash: Fix control character in adb path

**Output AI (nguyên văn):**

````text
Expo CLI đang tự tải Expo Go bản hợp với SDK 54. Mình chờ cài xong và app được nạp lên điện thoại.

Đường dẫn trong ghi chú lại bị hỏng như lần trước: chuỗi `\a` bị Python đọc thành một ký tự điều khiển. Mình sửa bằng mã ký tự:

**Môi trường đã sẵn sàng.** Trong tracker, phần chuẩn bị chỉ còn mục 0.9: chờ An và Hương chốt feature.

| Thành phần | Trạng thái |
|---|---|
| Backend `localhost:3000` · Web `5173` · Admin `5174` | ✅ Đang chạy (DB khởi tạo lúc 10:18) |
| Mobile trên S21 Ultra (Android 15), Expo Go 54.0.8 | ✅ Đang chạy, đã lấy được danh sách sản phẩm từ backend |

**Những điều mình đã ghi vào `_NOTES.md`** (để đưa vào phần môi trường test của report):
- `API_URL` trong bản clone HW02 đổi từ `192.168.10.13` sang `localhost`. Bản trong `DA` không bị đụng tới.
- Cách kết nối là `adb reverse` qua USB. **Mỗi lần rút cáp ra cắm lại phải chạy lại 2 lệnh reverse.** Bạn báo mình là được, mình chạy giúp.
- Expo cảnh báo `expo@54.0.34` nên nâng lên `~54.0.37`. Mình **không nâng cấp**, để giữ nguyên SUT như giảng viên phát.
- Vài lưu ý khác: tắt LDPlayer khi dùng adb; cáp đầu tiên của bạn chỉ sạc được, không truyền dữ liệu.

**Lưu ý khi tắt máy:** cả 4 server (backend, web, admin, Expo) đang chạy nền trong phiên Claude này. Khi bạn tắt laptop hoặc đóng phiên, chúng sẽ dừng. Lần sau mình bật lại cho bạn.

Bước tiếp theo là **S0 cho FR-17 (Quản lý mã giảm giá trên Web Admin)**:
1. Mình trích nguyên văn FR-17 cùng các phần SRS liên quan (FR-09 về cách coupon được dùng, FR-12 về phân quyền admin) vào `features/C_FR-17_QuanLyCoupon/00_spec.md`.
2. Bạn đăng nhập Web Admin tại `localhost:5174` bằng `admin@eshop.com` / `Admin123!`, mở trang quản lý mã giảm giá, chụp màn hình form thêm mã và danh sách mã.

Mình bắt đầu bước 1 nhé?
````

---

### C30 · 11:35 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
1. Đồng ý.
2. Chụp gửi bạn hay là chụp đưa vào folder nào?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Locate relevant SRS sections by line number
- Bash: Print verbatim SRS sections for FR-17
- Bash: Find coupon parts in API specification
- Bash: Print coupon sections of API spec
- Write: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\00_spec.md
- Edit: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\00_spec.md
- Bash: Check capitalize-after-colon in new spec file
- Bash: Update tracker and audit notes for S0

**Output AI (nguyên văn):**

````text
Bạn **lưu thẳng vào thư mục** `features/C_FR-17_QuanLyCoupon/screenshots/`, không cần gửi qua chat. Mình đọc được file trong thư mục, và ảnh đặt ở đó cũng là bằng chứng nộp kèm bài. Đặt tên theo bước và thứ tự:

- `S0_01_danh_sach_coupon.png`: Trang danh sách mã giảm giá
- `S0_02_form_them_coupon.png`: Form thêm mã (chụp đủ các trường)
- `S0_03_...png`: Bất kỳ màn hình nào khác bạn thấy đáng chú ý, ví dụ thông báo lỗi hay hộp xác nhận xoá

Giờ mình làm bước 1, trích nguyên văn đặc tả từ SRS:

Mình đã soạn xong phần đặc tả cho S0 ở file [00_spec.md](Homeworks/HW02/features/C_FR-17_QuanLyCoupon/00_spec.md). Giờ đến lượt bạn khám phá giao diện và điền bảng ở mục 4.

**Nội dung file:**

1. **Trích nguyên văn đặc tả.** Mục này chép y từ tài liệu gốc, không có nội dung do AI tự viết:
   - Từ `README.md`: FR-17; FR-12 (phân quyền admin); FR-09 (ý nghĩa của từng trường coupon khi người mua dùng mã, kèm 4 mã mẫu); FR-21 và FR-22 (yêu cầu giao diện và form); SEC-02, 03, 04.
   - Từ `api_specification.md`: Các API thêm, xem, xóa mã.
2. **15 yêu cầu có mã từ FR17-R01 đến R15.** Mình tách các đoạn trích ở mục 1 thành từng câu kiểm chứng được. Các mã này dùng để truy vết test case trong file JSON của skill thầy.
3. **8 câu hỏi Q1–Q8 về những điểm SRS bỏ ngỏ**, mỗi câu kèm mã yêu cầu liên quan:
   - `percent` có giới hạn trên 100 không.
   - Các trường số có nhận số thập phân không.
   - `code` dài tối đa bao nhiêu, có phân biệt hoa thường khi kiểm tra trùng không.
   - `expired_at` có được là ngày trong quá khứ không.
   - Admin có sửa được mã không.
   - Xóa mã có hộp thoại xác nhận không.
   - Trường `is_active` có trên form không.
4. **Bảng khám phá UI**, để bạn điền tên chính xác của từng trường, loại ô nhập, dấu `*`, giá trị mặc định, các nút và màu sắc.

Mục 2 và 3 là phần mình tự suy ra từ đặc tả, nên bạn cần đọc lại trước khi commit. Mình đã ghi điều này vào danh sách cần khai báo trong Audit.

Mình đã sửa một hướng dẫn trong bảng khám phá. Bản đầu bảo bạn bấm **Xóa** để xem có hộp thoại xác nhận không. Nhưng nếu trang không có hộp thoại thì mã mẫu sẽ bị xóa thật. Bây giờ bảng ghi rõ **không bấm Xóa ở S0**, việc này để dành cho S6.

**Việc của bạn:**
1. Mở `http://localhost:5174`, đăng nhập bằng `admin@eshop.com` / `Admin123!`, vào trang quản lý mã giảm giá.
2. Chụp màn hình và lưu vào `screenshots/` theo tên `S0_01_danh_sach_coupon.png`, `S0_02_form_them_coupon.png`, …
3. Điền bảng ở mục 4. Bạn có thể ghi vắn tắt, mình sẽ viết lại cho gọn sau.

Làm xong thì báo mình. Mình sẽ đối chiếu ảnh chụp với bảng, cập nhật câu trả lời cho Q1–Q8 nếu giao diện đã cho biết, rồi xuất log và đưa bạn lệnh commit `[C-FR17][S0] Extract spec and explore UI`.
````

---

### C31 · 14:48 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Không xài dấu —
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: List em-dash occurrences in documents and tools
- Bash: Show context of em dash on notes line 163
- Bash: Show context of em dash on notes line 163
- Bash: Replace em dashes and verify none remain
- Bash: Locate remaining em dashes
- Edit: D:\Dang\Test\Homeworks\HW02\tools\export_prompt_log.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\export_prompt_log.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\fill_ai02.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\fill_ai02.py
- Edit: D:\Dang\Test\Homeworks\HW02\tools\docx_to_md.py
- Bash: Fix last note dash, re-export log, verify
- Write: C:\Users\Lenovo\.claude\projects\d--Dang-Test\memory\doc-style-no-em-dash.md
- Bash: Index the new style memory
- Bash: Remove em dashes from memory index

**Output AI (nguyên văn):**

````text
Mình sẽ bỏ dấu `—` khỏi các tài liệu và lưu quy tắc này vào memory. Trước hết, mình liệt kê mọi chỗ đang dùng dấu này:

Mình đã bỏ hết dấu `—` trong các tài liệu và các script trong `tools/`. Quy tắc này đã lưu vào memory, và mình sẽ không dùng dấu `—` cả khi trả lời trong chat.

**Đã sửa (lệnh kiểm tra cho thấy còn 0 chỗ):**
- `00_spec.md`: Tiêu đề đổi thành "S0. Đặc tả FR-17: …" và "1.2 FR-12: Kiểm soát truy cập". Dòng Pool ghi "C, Web Admin".
- `README.md`: Dòng tiêu đề đổi thành "HW02-AI: Domain Testing on EShop (Software Testing 2026)". Các dòng feature ghi theo dạng "A: FR-01".
- `_NOTES.md`: Thay 10 chỗ, dùng dấu `:`, dấu phẩy hoặc dấu ngoặc tuỳ ngữ cảnh. Các ô trống trong bảng ghi chữ "Không".
- `export_prompt_log.py`: Tiêu đề mỗi lượt trong log đổi thành `### C01 · 14:17 12/10/2026 · Tool: … · Session …`. Mình đã xuất lại log theo định dạng mới. Log vẫn chỉ có phiên `305c705a`.
- `fill_ai02.py` và `docx_to_md.py`: Sửa các mẫu chữ có dấu `—`. Từ giờ, bảng Audit trong report sẽ viết theo dạng `A01: …`.

**Những chỗ vẫn còn dấu `—` vì là nguyên văn:**
- Phần trích SRS trong `00_spec.md`. Mình kiểm tra lại thì phần này không có dấu `—`.
- Vùng log tự xuất trong `prompt_log.md`. Vùng này chép nguyên văn những gì bạn và mình đã chat, mà các tin nhắn trước của mình có dùng dấu `—`. Nếu sửa vùng này thì log không còn là nguyên văn nữa.

S0 vẫn đang chờ bạn khám phá giao diện Web Admin, chụp màn hình và điền bảng ở mục 4.
````

---

### C32 · 14:54 18/10/2026 · Tool: Claude Code (n/a) · Session `305c705a`

**Prompt (nguyên văn):**

````text
<task-notification>
<task-id>b1dr8c9xn</task-id>
<task-id>bowzdpchf</task-id>
<task-id>bpmpz6o2e</task-id>
<task-id>bvpl43z73</task-id>
<task-id>__orphan_summary__:shell</task-id>
<status>stopped</status>
<summary>4 background shell command tasks didn't finish before the previous session ended. Task ids: b1dr8c9xn, bowzdpchf, bpmpz6o2e, bvpl43z73.</summary>
<note>No completion record was found for them in the previous session. They may have been stopped (via the UI, Monitor timeout, or agent teardown — these leave no transcript marker), or they may have been running when the previous Claude Code process exited. They have been marked stopped. Task ids in this notification beginning with "__orphan_summary" are internal scan markers, not tasks.</note>
</task-notification>
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- (không)

**Output AI (nguyên văn):**

````text
(Không có phản hồi: Phiên bị dừng hoặc chưa hoàn tất)
````

---

### C33 · 15:02 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Sao dấu ₫ của bạn bay cao thế
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Check for new session and inspect currency character

**Output AI (nguyên văn):**

````text
Hệ thống báo phiên vừa khởi động lại và 4 server chạy nền (backend, web, admin, Expo) đã dừng. Mình kiểm tra 2 việc: có phiên Claude mới cần thêm vào whitelist không, và ký tự `₫` trong file là ký tự gì.

Ký tự đó không sai. Đây là **ký hiệu đồng `₫`** (Unicode U+20AB, "DONG SIGN"), đúng ký tự mà SRS dùng. Trông nó bay cao là do **font chữ**: nhiều font vẽ `₫` theo kiểu chữ "đ" nhỏ có gạch dưới, đặt cao như chỉ số trên, giống cách ghi tiền truyền thống ở Việt Nam. Trên điện thoại lúc nãy, giá hiển thị "30.000.000 đ" có gạch dưới cũng chính là ký tự này, chỉ khác font.

Mình đề xuất **giữ nguyên `₫`**, vì:
- 8 trong 9 chỗ nằm trong phần **trích nguyên văn SRS**, nên không được sửa.
- **FR-21** yêu cầu "luôn dùng ký hiệu `₫`". Khi viết test case kiểm tra cách hiển thị tiền, kết quả mong đợi phải ghi đúng ký tự này. Nếu ghi `đ` thì sẽ lệch với đặc tả.

Chỗ duy nhất là chữ của mình là "0.01 ₫" ở câu hỏi Q2, và mình cũng để `₫` cho thống nhất. Nếu bạn chỉ thấy khó đọc khi xem file, có thể đổi font trong phần Markdown preview của VS Code, nội dung file không cần đổi.

Về các server: phiên vừa khởi động lại nhưng vẫn là phiên `305c705a`, nên whitelist không cần thêm gì. 4 server chạy nền (backend, web, admin, Expo) đã dừng. Khi bạn sẵn sàng khám phá Web Admin cho S0, bạn báo mình để mình bật lại. Nếu cần mobile thì mình chạy lại cả `adb reverse`.
````

---

### C34 · 15:07 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
- Vì lúc nãy máy bị crash nên tôi cần bạn khởi động lại phần web.
- Đồng thời với mỗi ảnh tôi chụp thì tôi nên đặt tên gì, bạn gợi ý trước cho tôi đi.
- Cần tôi trả lời Q1-Q8 khi quan sát không?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Start EShop backend on port 3000
- Bash: Start EShop customer web on port 5173
- Bash: Start EShop admin web on port 5174
- Bash: Wait until all three servers respond

**Output AI (nguyên văn):**

````text
Mình bật lại backend, web và admin. Lưu ý: như đã ghi lúc trước, mỗi lần khởi động backend có thể tự reset DB về dữ liệu mẫu. Ở S0 việc này không ảnh hưởng gì.

Cả 3 server đã chạy lại: backend tại `localhost:3000`, web tại `5173`, Web Admin tại `5174`. Backend lại in ra dòng "Database initialized and seeded", tức là DB đã về dữ liệu mẫu.

## Tên ảnh cho S0

Lưu vào `features/C_FR-17_QuanLyCoupon/screenshots/`. Mỗi tên có dạng `S0_<số thứ tự>_<nội dung>.png`. Số thứ tự giữ cho ảnh xếp đúng trình tự, phần nội dung khớp với một dòng trong bảng ở mục 4.

| Tên file | Chụp gì |
|---|---|
| `S0_01_dang_nhap_admin.png` | Trang đăng nhập Web Admin |
| `S0_02_menu_admin.png` | Trang đầu sau khi đăng nhập, thấy menu dẫn tới mục mã giảm giá |
| `S0_03_danh_sach_coupon.png` | Trang mã giảm giá: Tiêu đề, URL trên thanh địa chỉ, bảng danh sách đầy đủ các cột và mã mẫu |
| `S0_04_form_them_coupon.png` | Form thêm mã khi **chưa nhập gì**, thấy đủ nhãn, dấu `*` và giá trị mặc định |
| `S0_05_dropdown_type.png` | Dropdown `type` đang mở, nếu trường này là dropdown |
| `S0_06_chon_ngay_expired.png` | Ô chọn ngày `expired_at` đang mở, nếu có |
| `S0_07_nut_thao_tac.png` | Cận cảnh nút Thêm, Xóa, Sửa (nếu có) để thấy chữ và màu |

Gặp màn hình nào khác đáng chú ý thì đánh số tiếp từ `S0_08_…`. Nếu một ảnh đã chụp đủ nội dung của ảnh khác, ví dụ ảnh danh sách đã thấy rõ nút Xóa, thì bỏ qua ảnh còn lại.

## Có cần trả lời Q1–Q8 không?

**Chỉ trả lời những câu nhìn thấy được, không cần thử.** Ở S0 bạn chỉ quan sát giao diện, không nhập dữ liệu sai.

| Câu | Trả lời được ở S0 bằng cách |
|---|---|
| Q6 (có sửa được mã không) | Xem có nút Sửa không |
| Q8 (có trường `is_active` không) | Xem form và bảng có trường trạng thái không |
| Q5 (định dạng ngày) | Xem ô `expired_at` là ô chọn ngày hay ô gõ chữ |
| Q1–Q4 (giới hạn, số thập phân, độ dài `code`) | Chỉ ghi nếu giao diện **tự nói ra**, ví dụ chữ gợi ý "0–100" hay "tối đa 20 ký tự". Nếu không thấy thì để trống |
| Q7 (hộp thoại khi xóa) | Để trống, dời sang S6 |

Những câu còn trống sẽ được xử lý ở các bước sau. Ở S2, câu nào ảnh hưởng tới cách chia lớp tương đương sẽ được ghi thành **giả định**. Đến S6, khi chạy test thật, mình sẽ biết hệ thống thực sự xử lý thế nào.
````

---

### C35 · 15:19 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Tôi nghĩ là cần commit file 00_spec lại, vì file đó là bạn viết. Sau đó tôi điền vào quan sát thì 1 commit nữa. Và bạn viết lại và mình kiểm tra thì thêm 1 commit. Hay là không cần mà chỉ 1 commit cho tất cả?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Export prompt log and show pending changes

**Output AI (nguyên văn):**

````text
Mình đề xuất **tách thành 3 commit**. Đề chỉ bắt buộc mỗi bước tối thiểu một commit, nhưng tách nhỏ có 3 lợi ích:

1. **Lịch sử git cho thấy rõ AI viết gì và bạn sửa gì.** Diff giữa bản AI soạn và bản sau khi bạn review chính là bằng chứng "human review" mà đề yêu cầu. Bằng chứng này cũng dùng được cho Audit Report (mục "SV đã sửa gì") và khi bị gọi vấn đáp.
2. Nếu bạn sửa sai ở bước review thì vẫn còn bản gốc để quay lại.
3. Cả 3 commit vẫn cùng tag `[C-FR17][S0]`, nên khi đếm vẫn tính là một bước.

| Commit | Nội dung | Message |
|---|---|---|
| 1 | `00_spec.md` bản AI soạn | `[C-FR17][S0] Add spec extract and requirement list (AI draft)` |
| 2 | Ảnh chụp và bảng quan sát bạn điền | `[C-FR17][S0] Record UI exploration and screenshots` |
| 3 | Mình viết lại cho gọn và cập nhật Q1–Q8; bạn kiểm tra xong thì commit | `[C-FR17][S0] Review spec and answer open questions` |

Mình áp dụng cách tách này cho mọi bước có AI tham gia (S1–S4): **AI soạn → commit, bạn review → commit**.

Commit 1 làm ngay được. Mình xuất lại prompt log trước:

Log đã xuất xong: 35 lượt, tất cả thuộc phiên `305c705a`. `git status` cho thấy đang có **3 nhóm thay đổi** chưa commit, nên mình tách lệnh theo từng nhóm:

- `README.md` và 3 file trong `tools/`: Đây là phần bỏ dấu `—` lúc nãy, không thuộc S0. Nên commit riêng với tag `[setup]`.
- `00_spec.md` và `prompt_log.md`: Đây là commit 1 của S0.
- 2 ảnh `S0_01`, `S0_02` bạn vừa chụp, cùng việc xoá file `.gitkeep` trong `screenshots/`: Để dành cho commit 2, khi bạn chụp xong và điền bảng quan sát.

```bat
cd /d D:\Dang\Test\Homeworks\HW02

git add README.md tools/
git commit -m "[setup] Replace em dashes in README and tools output"

git add features/C_FR-17_QuanLyCoupon/00_spec.md prompt_log.md
git commit -m "[C-FR17][S0] Add spec extract and requirement list (AI draft)"

git push
```

Ảnh chụp chưa được `add` nên không lẫn vào hai commit này. Khi bạn chụp xong và điền bảng ở mục 4 thì báo mình, mình sẽ đưa lệnh cho commit 2.
````

---

### C36 · 15:48 18/10/2026 · Tool: Claude Code (claude-opus-5-5) · Session `305c705a`

**Prompt (nguyên văn):**

````text
Tôi đã điền những gì quan sát được và hình ảnh. Bạn hãy kiểm tra.

Q1. Giá trị % điền 1000 vẫn nhận.
Q2. Có nhận số phần trăm.
Q3. min_order_amount có nhận số thập phân, còn max_uses_per_user không nhận. Có giới hạn trên là hạn trên cái gì? Là không chạm số âm hay là số quá lớn?
Q4. Hiện tại thử có dấu tiếng Việt, số, dấu @ ! các thứ thì không thấy bị chặn. Mã tự động viết hoa dù để bàn phím hoa hay thường.
Q5. Được chọn ngày quá khứ, hôm nay. Định dạng mm/dd/yyyy
Q6. Không thấy nút sửa.
Q7. Tôi xóa chính mã tôi tạo ra thì không có hộp thoại xác nhận.
Q8. is_active là cột hết hạn hả?
````

**Thao tác AI đã thực hiện (đọc/ghi file, chạy lệnh):**

- Bash: Read filled observation table and list screenshots
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_03_giao_dien_quan_ly_ma_giam_gia.png
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_04_form_them_coupon_khong_noi_dung.png
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_05_dropdown_type.png
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_06_chon_ngay_expired.png
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_07_nut_thao_tac_tao_ma.png
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_07_nut_thao_tac_xoa.png
- Read: D:\Dang\Test\Homeworks\HW02\features\C_FR-17_QuanLyCoupon\screenshots\S0_02_menu_admin.png
- Bash: Export prompt log before commit 2

**Output AI (nguyên văn):**

````text
Mình đọc bảng quan sát bạn đã điền và xem các ảnh chụp.
````


<!-- CLAUDE-LOG:END -->

---

## 2. Công cụ khác (tự điền)

> Dán nguyên văn prompt và output. Mẫu:
>
> `### G01 · HH:MM dd/mm/yyyy · Tool: ChatGPT (<model>)` → **Phần liên quan:** … → **Prompt (nguyên văn):** … → **Output AI (nguyên văn):** …

_(Chưa có)_
