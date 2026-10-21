# S8: AI gap analysis (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S8 (Phân tích những gì AI bỏ sót và vì sao, đề mục 6.3)
- Thời gian tạo: 2026-10-21 09:43 (UTC+07:00), lấy từ giờ máy
- Bản gốc của AI: `ai_raw/S8_gap_analysis.md`. `08_gap_analysis.md` lúc tạo giống hệt bản này; sinh viên review trực tiếp trên `08_gap_analysis.md`
- Căn cứ: Bảng "Thay đổi so với bản AI" của `00_spec.md` (S0), `01_io.md` (S1), `02_ec.md` (S2), `03_tc.md` (S3), `04_bva.md` (S4), `05_final_tc.md` (S5); `05_final_tc.md` mục 2, 8; `06_results.md` (S6); `bugs/bug_report.md` mục FR-04 (S7); `ai_raw/S3_test_cases.md`, `ai_raw/S4_bva.md` (để biết test case nào có trong bản AI gốc). Cấu trúc theo `features/C_FR-17_QuanLyCoupon/08_gap_analysis.md` (sinh viên cho phép đọc để lấy cấu trúc)
- Ba nguyên nhân dùng để phân loại (theo đề mục 6.3): **Chất lượng input/prompt** (AI không có hoặc không được đưa thông tin cần thiết), **Giới hạn của công cụ AI** (thông tin có sẵn nhưng AI suy luận thiếu hoặc sai), **Độ phức tạp của feature** (nhiều giả định, đường thực thi, nền tảng chồng lên nhau)

---

## 1. Thống kê các bảng "Thay đổi so với bản AI" (S0 đến S5)

### 1.1 Theo Loại

Đếm bằng `check_step.py changes`.

| Bước | File | Sai | Thiếu | Thừa | Mơ hồ | Quyết định của SV | Tổng |
|---|---|---|---|---|---|---|---|
| S0 | `00_spec.md` mục 13 | 0 | 0 | 0 | 0 | 6 | 6 |
| S1 | `01_io.md` mục 12 | 0 | 0 | 0 | 0 | 10 | 10 |
| S2 | `02_ec.md` mục 11 | 1 | 0 | 0 | 0 | 6 | 7 |
| S3 | `03_tc.md` mục 14 | 1 | 1 | 0 | 0 | 7 | 9 |
| S4 | `04_bva.md` mục 10 | 0 | 0 | 0 | 0 | 5 | 5 |
| S5 | `05_final_tc.md` mục 15 | 0 | 0 | 0 | 0 | 1 | 1 |
| **Tổng** | | **2** | **1** | **0** | **0** | **35** | **38** |

35 trên 38 dòng (92%) là quyết định của sinh viên. Ở mọi bước, sinh viên chọn đúng phương án AI đã áp tạm (theo yêu cầu "mỗi bước review một lượt, điểm nhỏ thì áp phương án đề xuất"). Các quyết định không theo đề xuất: Bỏ xuất Word, Excel (`03_tc.md` điểm 6), không chụp `S0_05`, `S0_08` (`00_spec.md` quyết định 6, 7).

### 1.2 Theo người phát hiện (3 dòng Sai, Thiếu)

| Bước | Dòng | Sinh viên | AI tự phát hiện | Phiên điều phối |
|---|---|---|---|---|
| S2 | Mục 1 trỏ tới cột "Hệ quả" không có trong bảng giả định (Sai) | 0 | 1 (khi viết bản review) | 0 |
| S3 | Giờ tạo bản AI ghi ước lượng 07:45, trễ hơn giờ máy (Sai) | 0 | 1 (khi viết bản review) | 0 |
| S3 | Ma trận truy vết thiếu TC-PROF-71 cho FR04-R02, FR04-R05 (Thiếu) | 0 | 1 (khi gộp S5) | 0 |
| **Tổng** | | **0** | **3** | **0** |

Cả 3 lỗi đều là lỗi hình thức hoặc truy vết, không đổi test case nào. Vì sinh viên không sửa nội dung ở S0 đến S5, bảng thay đổi **không cho thấy** chỗ thiết kế của AI chưa đúng; các chỗ đó chỉ lộ ra khi chạy test ở S6 (mục 2).

### 1.3 Nguồn gốc của bộ test case cuối

Theo `05_final_tc.md` mục 2: 34 test case, cả 34 là "AI"; 0 "AI có SV sửa"; 0 "SV thêm"; sinh viên không bổ sung ở S5 (mục 13).

## 2. Test case AI bỏ sót hoặc thiết kế sai

Không có test case nào được sửa hay thêm khi review, nên mục này lấy từ kết quả S6, S7: Những chỗ thiết kế không lường trước, làm test case bị chặn, hoặc làm bug chỉ được tìm thấy ngoài test case.

### 2.1 Ở bước thiết kế (S1 đến S4)

| Test case | AI bỏ sót hoặc sai gì | Phát hiện | Nguyên nhân | Căn cứ |
|---|---|---|---|---|
| TC-PROF-04, TC-PROF-30 (và TC-PROF-02, 03, 05, 31 nếu chạy) | Test case kiểm Họ Tên nhập kèm Số điện thoại cơ sở `0912345678` để "đổi thêm một trường" (A19). Khi chính giá trị cơ sở bị ứng dụng từ chối, cả hai test case thành Blocked; không có phương án dự phòng (ví dụ giữ nguyên ô Số điện thoại, hoặc chạy TC-PROF-01 trước để xác nhận giá trị cơ sở) | AI khi điền S6 | Giới hạn của công cụ AI | `06_results.md` dòng 5, 12; `bugs/bug_report.md` mục FR-04, "Test case Blocked". Thứ tự chạy ở `05_final_tc.md` mục 9 có TC-PROF-01 đầu nhóm giao diện, nhưng không ghi "nếu TC-PROF-01 Fail thì đổi giá trị cơ sở" |
| Không có test case (BUG-FR04-04) | Không có lớp hay test case kiểm màn Hồ sơ **hiển thị giá trị đang lưu**. Thiết kế dùng EV4 ("mở lại màn Hồ sơ thấy giá trị mới") như cách kiểm chứng, mặc định là màn hình hiển thị đúng dữ liệu | AI khi đọc ảnh S6 (QS03), sinh viên xác nhận | Chất lượng input/prompt | Ở S0, hồ sơ mẫu có Số điện thoại, Địa chỉ trống (`00_spec.md` Q23), nên ảnh khảo sát không thể cho thấy ô có hiển thị giá trị đã lưu không. AI có ghi rủi ro "EV4 có thể hiển thị giá trị trong bộ nhớ" (`05_final_tc.md` mục 10) nhưng không biến nó thành test case |
| TC-PROF-72 | Giả định A16 (d) ghi "trường không gửi bị xóa là sai", không xét ngữ nghĩa của `PUT` (thay toàn bộ tài nguyên, RFC 9110). Ở S7 chính AI đề xuất "không thành bug" với lý do này | AI khi viết S7 | Giới hạn của công cụ AI | `02_ec.md` A16; `bugs/bug_report.md` mục FR-04, KG01 |
| TC-PROF-77 | Bước kiểm chỉ xem `role` trong `GET /api/users/me`; không có bước đăng nhập lại để xem token mới có quyền admin không, nên chưa đo được mức ảnh hưởng thật của BUG-FR04-01 | AI khi viết S7 | Độ phức tạp của feature | `bugs/bug_report.md` BUG-FR04-01, Ghi chú. Quyền admin thuộc FR-12; S1 đã chốt không dùng API admin để kiểm chứng (`01_io.md` mục 8 điểm 7) |

### 2.2 Ở hướng dẫn chạy (S6)

| Phần | AI sai gì | Phát hiện | Nguyên nhân | Căn cứ |
|---|---|---|---|---|
| Hướng dẫn từng bước S6, bước 0.4 (`adb reverse`, hàm `shot`) | Giả định lệnh `adb` có trong PATH của PowerShell; trên máy sinh viên không có, phiên điều phối sửa bằng đường dẫn đầy đủ tới `adb` | Phiên điều phối | Giới hạn của công cụ AI | Sinh viên báo khi giao S8. AI viết lệnh mà không kiểm môi trường (có thể hỏi hoặc thêm bước `Get-Command adb`) |

### 2.3 Tổng hợp theo nguyên nhân

| Nguyên nhân | Số dòng ở mục 2.1, 2.2 | Ví dụ |
|---|---|---|
| Chất lượng input/prompt | 1 | Hồ sơ mẫu trống nên S0 không quan sát được việc hiển thị giá trị đã lưu |
| Giới hạn của công cụ AI | 3 | Không có dự phòng khi giá trị cơ sở bị từ chối; giả định A16 bỏ qua ngữ nghĩa `PUT`; lệnh `adb` không có trong PATH |
| Độ phức tạp của feature | 1 | Mức ảnh hưởng của việc tự đổi `role` nằm ở feature khác (FR-12) |

## 3. Bug AI bỏ sót

Đối chiếu 5 bug ở `bugs/bug_report.md` (issue #85 đến #89) với nguồn gốc test case phát hiện ra chúng.

| Bug | Issue | Test case phát hiện | Nguồn gốc test case | Bản AI gốc bắt được không |
|---|---|---|---|---|
| BUG-FR04-01 | #85 | TC-PROF-77 | AI (`ai_raw/S3_test_cases.md`) | Có |
| BUG-FR04-02 | #86 | TC-PROF-01, TC-PROF-101 | AI (S3, S4) | Có |
| BUG-FR04-03 | #87 | TC-PROF-74, 75, 71 | AI (S3; TC-PROF-74, 75 là hai test case "kiểm phía hệ thống" AI thêm ở S3) | Có |
| BUG-FR04-04 | #88 | TC-PROF-04 (quan sát QS03) | AI, nhưng không phải mục đích của test case | Không trực tiếp: Không có test case kiểm việc hiển thị giá trị đã lưu (mục 2.1); bug tìm được nhờ đọc ảnh khi điền S6 |
| BUG-FR04-05 | #89 | TC-PROF-90 (điểm 5) | AI | Có (điền từ ảnh S0, theo quyết định Q27 của sinh viên ở S1) |

Tóm lại:

- **Bản AI gốc bắt được 4 trên 5 bug** (01, 02, 03, 05). BUG-FR04-04 là quan sát ngoài test case.
- **Hai test case API "kiểm phía hệ thống" (TC-PROF-74, 75) có giá trị lớn:** Chúng cho thấy hệ thống không kiểm Số điện thoại, trong khi ứng dụng kiểm sai; nếu chỉ chạy qua giao diện thì chỉ thấy BUG-FR04-02.
- **Hai "Khác giả định" (TC-PROF-72, 73) không thành bug** theo quyết định của sinh viên ở S7 (KG01, KG02).

## 4. Giới hạn của kết quả

- **S6 rút gọn:** 13 trên 34 test case Not run (`06_results.md` mục 5): Mọi test case giao diện ngoài danh sách tối thiểu (TC-PROF-02, 03, 05 đến 10, 31, 35, 100, 103, 104). Vì vậy chưa biết có bug ở chữ tiếng Việt có dấu, khoảng trắng, thẻ HTML ở Địa chỉ, xuống dòng, và các biên Họ Tên (`A`, `␣B␣`) qua ứng dụng hay không; phần BVA qua giao diện chỉ chạy 1 trên 4 test case mới (TC-PROF-101).
- **TC-PROF-06 Not run:** Chưa biết ứng dụng có lưu được hồ sơ khi để trống Số điện thoại không; trong lần chạy này chưa có lần cập nhật nào thành công qua ứng dụng.
- **TC-PROF-90 điểm (6), (7) Not run:** Chức năng nút "Thoát" (Q26) chưa rõ; FR04-R12, FR04-R16 và khác biệt D01 chưa kiểm.
- **Blocked:** TC-PROF-04, 30 bị chặn bởi BUG-FR04-02, nên việc ứng dụng có từ chối Họ Tên rỗng (A01) và hiển thị thẻ HTML đã lưu (FR04-R22) chưa kiểm được.
- **Lỗi chạy của sinh viên:** TC-PROF-01, 04, 33 thiếu lệnh `get`; EV3 lấy gián tiếp từ phản hồi đăng nhập trong log `chuan` của test case kế tiếp (thời điểm muộn hơn vài chục giây, nhưng trước khi đặt lại `S_CHUAN`). Log `chuan` lúc 08:53:21 mang nhãn TC-PROF-33 nhưng là của TC-PROF-101; log `get` lúc 08:53:29 chạy trước thao tác và bị bỏ qua. TC-PROF-101 gõ `09123453789` thay vì `09123456789` (vẫn 11 chữ số, cùng điểm biên).
- **Bằng chứng từ S0:** TC-PROF-90 điểm (1) đến (5) lấy từ ảnh S0 cùng ngày, cùng commit, không chụp lại ở S6.
- **QS02 chưa đánh giá:** Phản hồi API có trường `password`, nhưng script che giá trị nên không biết là văn bản rõ hay đã băm. Sinh viên quyết định không báo trong FR-04; nếu nhóm muốn xét SEC-01 thì cần kiểm ở feature khác (FR-02, FR-19).
- **Phân loại nguyên nhân là đánh giá:** Mỗi dòng ở mục 2 chỉ xếp một nguyên nhân chính.

## 5. Bài học

1. **Kiểm giá trị cơ sở trước, và có phương án dự phòng.** Một giá trị cơ sở bị từ chối (`0912345678`) làm 2 test case Blocked và không có lần lưu thành công nào qua ứng dụng. Thiết kế nên ghi rõ: Chạy test case cơ sở đầu tiên; nếu Fail thì đổi sang biến thể không đụng trường đó.
2. **Đường API tách được lỗi của ứng dụng và lỗi của hệ thống.** Cùng giá trị, ứng dụng từ chối (TC-PROF-01, 101) còn hệ thống nhận cả giá trị sai (TC-PROF-74, 75). Hai lớp kiểm tra cùng sai, theo hai hướng ngược nhau; nếu chỉ chạy giao diện sẽ bỏ sót BUG-FR04-03.
3. **Khảo sát S0 với dữ liệu trống che mất một nhóm lỗi.** Hồ sơ mẫu không có Số điện thoại, Địa chỉ, nên S0 không thấy được màn hình có hiển thị giá trị đã lưu không (BUG-FR04-04). Khi dữ liệu mẫu trống, nên thêm một test case "mở màn hình khi trường đang có giá trị".
4. **Giả định về API cần xét ngữ nghĩa của giao thức.** A16 coi việc xóa trường không gửi là sai, trái với ngữ nghĩa chuẩn của `PUT`; AI tự mâu thuẫn ở S7.
5. **Hướng dẫn chạy cần kiểm môi trường và gộp thao tác.** Lệnh `adb` không có trong PATH; ba lần quên `get` và một nhãn `--tag` sai cho thấy chuỗi lệnh `chuan`, thao tác tay, `get` dễ lỗi. Nên kiểm công cụ trước (`Get-Command adb`) và để script tự chạy `get` sau mỗi bước tay.
