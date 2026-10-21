# S4: Phân tích giá trị biên (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S4 (Phân tích giá trị biên, theo Step 4 của slide S04)
- Thời gian tạo: 2026-10-21 07:44 (UTC+07:00), lấy từ giờ máy
- Căn cứ: `02_ec.md` (giả định A01, A02, A04, A05, A07, A10; ghi chú mục 10), `03_tc.md` (giá trị cơ sở, `S_CHUAN`, QT-GD, QT-API, cách đọc kết quả mục 2.4; ghi chú mục 13)

---

## 1. Cách làm

- Theo Step 4 của slide S04: Với mỗi phân vùng **có thứ tự**, xét LB-1, LB, LB+1, UB-1, UB, UB+1, giá trị nhỏ nhất và lớn nhất giao diện cho nhập, một giá trị ở giữa. Không áp máy móc: Điểm không áp dụng ghi lý do; điểm trùng test case đã có thì dùng lại mã cũ.
- Mỗi điểm chỉ vi phạm đúng một điều kiện: Giá trị Số điện thoại tại biên vẫn bắt đầu bằng `0` và chỉ gồm chữ số; trường còn lại lấy giá trị cơ sở.
- Phạm vi theo yêu cầu của sinh viên: Các biên đã liệt kê ở `03_tc.md` mục 13 (11 chữ số qua giao diện, Số điện thoại `0`, 11 chữ số qua API, Họ Tên `A` và `␣A␣`). Điểm khác chỉ ghi lý do không thêm.
- Quy trình và cách đọc kết quả theo `03_tc.md` mục 2 (QT-GD, QT-API, `S_CHUAN`, mục 2.4). Mã test case mới từ TC-PROF-100.
- `␣` là một dấu cách.
- Theo yêu cầu của sinh viên, các điểm nhỏ ở mục 6 đã **áp tạm phương án đề xuất**; sinh viên duyệt ở lượt review.

## 2. Phân vùng có thứ tự

| Mã | Phân vùng | Cận dưới (LB) | Cận trên (UB) | Căn cứ |
|---|---|---|---|---|
| P1 | Số chữ số của Số điện thoại (tính cả `0` đầu) | 10 | 11 | FR04-R05; A07 (a). Lớp: EC11 (KH, dưới), EC08 (H), EC12 (KH, trên) |
| P2 | Độ dài Họ Tên sau khi cắt khoảng trắng đầu cuối | 1 | Không có | FR04-R01; A01 (a) (bắt buộc), A04 (a) (cắt), A02 (a) (không có cận trên). Lớp: EC06, EC07 (KH), EC01 (H) |

Không lập phân vùng có thứ tự cho:

- Địa chỉ: Không có cận nào (A10 (a)).
- Chữ số đầu, tập ký tự của Số điện thoại; ký tự của Họ Tên; `email`, `role`, token, `id`: Là điều kiện "must be" hoặc tập giá trị, không có thứ tự; đã đủ ở S2, S3.

## 3. Bảng giá trị biên

### 3.1 P1 Số chữ số của Số điện thoại

Test case mới: Họ Tên lấy giá trị cơ sở `Nguyen Van An NN` (NN là số test case, ví dụ `Nguyen Van An 100`); Địa chỉ giữ `S_CHUAN`. Giao diện chạy theo QT-GD, API theo QT-API với body `B(NN)` đổi `phone`. Kết quả ERR2 nghĩa là EV3 trả `S_CHUAN` cho cả Họ Tên và Số điện thoại (`03_tc.md` mục 2.4).

| Điểm | Giá trị | Độ dài hoặc giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | 0 | H (EC09, A05 (a)) | OUT1, lưu trống | TC-PROF-06 (đã có) |
| Nhỏ nhất chỉ vi phạm số chữ số | `0` | 1 chữ số | KH | ERR2 | TC-PROF-100 (giao diện) |
| LB-1 | `091234567` | 9 chữ số | KH | ERR2 | TC-PROF-33 (đã có, giao diện), TC-PROF-75 (đã có, API) |
| LB | `0912345678` | 10 chữ số | H | OUT1 | TC-PROF-01 (đã có) |
| LB+1, trùng UB | `09123456789` | 11 chữ số | H | OUT1; EV3 trả `09123456789` | TC-PROF-101 (giao diện) |
| UB qua API | `09123456789` | 11 chữ số | H | OUT2; EV3 trả `09123456789` | TC-PROF-102 (API) |
| UB-1, trùng LB | `0912345678` | 10 chữ số | H | OUT1 | TC-PROF-01 (đã có) |
| UB+1 | `091234567890` | 12 chữ số | KH | ERR2 | TC-PROF-34 (đã có) |
| Giữa | Không áp dụng | | | | Giữa 10 và 11 không có số nguyên nào |
| Lớn nhất giao diện cho nhập | Không thêm | | | | TC-PROF-34 (đã có), dùng làm điểm thăm dò: Ở bước 3 của QT-GD ghi số chữ số ô thực sự nhận; nếu ô chỉ nhận tới 11 chữ số thì kết quả phản ánh ứng dụng chặn, không phải hệ thống (mục 6 điểm 2) |


### 3.2 P2 Độ dài Họ Tên sau khi cắt

Test case mới chạy theo QT-GD: Số điện thoại lấy giá trị cơ sở `0912345678`; Địa chỉ giữ `S_CHUAN`.

| Điểm | Giá trị | Độ dài hoặc giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | 0 | KH | ERR1 | TC-PROF-30 (đã có) |
| LB-1, dạng chỉ khoảng trắng | `␣␣␣` | 0 sau khi cắt (3 trước khi cắt) | KH | ERR1 | TC-PROF-31 (đã có) |
| LB | `A` | 1 | H | OUT1; EV3 trả `A` | TC-PROF-103 (giao diện) |
| LB, khoảng trắng hai bên | `␣B␣` | 1 sau khi cắt (3 trước khi cắt) | H | OUT1; EV3 trả `B` (A04 (a)) | TC-PROF-104 (giao diện) |
| LB+1 | Không thêm | | | | Cùng lớp EC01 với giá trị cơ sở; lỗi lệch cận (đặt cận là 2) đã bị điểm LB phát hiện (mục 6 điểm 3) |
| UB-1, UB, UB+1, giữa | Không áp dụng | | | | Không có cận trên (A02 (a)) nên không có điểm giữa |
| Lớn nhất giao diện cho nhập | Không thêm | | | | Thăm dò chuỗi dài (ví dụ 1000 ký tự) để ngoài ngân sách (mục 6 điểm 4) |

Ghi chú:

- TC-PROF-104 dùng chữ `B` (khác `A` của TC-PROF-103) để kết quả không trùng nếu hai test case chạy liền nhau mà quên đặt lại `S_CHUAN`.
- Một dấu cách `␣` (LB-1 dạng 1 ký tự trước khi cắt) cùng lớp EC07 với TC-PROF-31; không thêm.
- Nếu hệ thống lưu `␣B␣` nguyên văn thay vì `B`: Đó là **khác giả định** A04 (a), không phải khác đặc tả; sinh viên xét ở S5 hoặc S7 trước khi coi là bug.


Họ Tên của TC-PROF-103, TC-PROF-104 không theo mẫu `Nguyen Van An NN` vì chính độ dài Họ Tên là đối tượng test; Số điện thoại cơ sở đổi khác `S_CHUAN` nên vẫn thấy được lần lưu.

## 4. Tổng hợp và truy vết

| Phân vùng | Test case mới | Test case dùng lại |
|---|---|---|
| P1 | TC-PROF-100, TC-PROF-101 (giao diện), TC-PROF-102 (API) | TC-PROF-01, TC-PROF-06, TC-PROF-33, TC-PROF-34, TC-PROF-75 |
| P2 | TC-PROF-103, TC-PROF-104 (giao diện) | TC-PROF-30, TC-PROF-31 |

- Mới: 5 test case (4 giao diện, 1 API). Cả bộ: 29 (S3) + 5 = **34 test case**, trong mục tiêu 25 đến 35.
- Truy vết: FR04-R05 (TC-PROF-100, TC-PROF-101, TC-PROF-102); FR04-R01 (TC-PROF-103, TC-PROF-104). Yêu cầu khác không có test case BVA vì không có phân vùng có thứ tự (mục 2).
- Thứ tự chạy: TC-PROF-100, TC-PROF-101, TC-PROF-103, TC-PROF-104 chạy cùng nhóm giao diện (`03_tc.md` mục 9.1 bước 3); TC-PROF-102 chạy cùng nhóm API (bước 4).

## 5. Biên qua API

- Đã thêm: UB = 11 chữ số (TC-PROF-102), vì nếu ứng dụng tự giới hạn ô ở 10 chữ số thì TC-PROF-101 chỉ kiểm ứng dụng.
- Đã có từ S3: LB-1 = 9 chữ số (TC-PROF-75).
- Không thêm: UB+1 = 12 chữ số qua API (mục 6 điểm 1); biên Họ Tên qua API (bàn phím chữ gõ được dấu cách và chữ cái, ứng dụng không có lý do biến đổi giá trị trước khi gửi).

## 6. Điểm cần sinh viên quyết định

Các điểm dưới đây đã áp tạm phương án (a); sinh viên duyệt ở lượt review.

| # | Vấn đề | Các lựa chọn | Đã áp tạm |
|---|---|---|---|
| 1 | UB+1 (12 chữ số) qua API | (a) Không thêm, giữ tổng 34 test case; (b) thêm một test case API (tổng 35), để kiểm phía hệ thống cả cận trên | (a) |
| 2 | Lớn nhất giao diện cho nhập của Số điện thoại | (a) Dùng TC-PROF-34 làm điểm thăm dò, ghi số chữ số ô nhận; (b) thêm test case chuỗi dài riêng | (a) |
| 3 | LB+1 của Họ Tên (2 ký tự) | (a) Không thêm; (b) thêm `An` | (a) |
| 4 | Lớn nhất giao diện cho nhập của Họ Tên (chuỗi dài) | (a) Không thêm; (b) thêm một chuỗi khoảng 1000 ký tự, ghi số ký tự ô nhận và giá trị lưu | (a) |
| 5 | Kết quả khác giả định (ví dụ `␣B␣` lưu nguyên văn) | (a) Ghi "khác giả định", xét ở S5 hoặc S7; (b) coi là không đạt | (a) |

## 7. Ghi chú cho bước sau

- **S5:** Bộ test case cuối gồm `03_tc.md` và `04_bva.md`, trình bày bằng Markdown (không xuất Word, Excel). Nếu S6 thấy ô Số điện thoại hoặc Họ Tên giới hạn N ký tự, bổ sung N-1, N, N+1 ở S5.
- **S6:** Ghi tên thiết bị, phiên bản Android, phiên bản Expo Go, ngày chạy. Với TC-PROF-34, ghi số chữ số ô nhận. Với TC-PROF-101, nếu ô không cho gõ chữ số thứ 11 thì ghi lại; TC-PROF-102 cho biết hệ thống có nhận 11 chữ số không.
