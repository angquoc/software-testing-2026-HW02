# S4: Phân tích giá trị biên (FR-01 Đăng ký tài khoản)

- Bước: S4 (Boundary Value Analysis, theo Step 4 của slide S04)
- Thời gian tạo: 2026-10-20 13:14 (+07:00)
- Căn cứ: `02_ec.md` (lớp tương đương, giả định A01 đến A15, nguyên tắc khoảng trắng), `03_tc.md` (bộ test case EP, quy ước, giá trị cơ sở, thứ tự chạy)

---

## 1. Cách làm

Theo slide S04 và WORKFLOW mục 3.2: Với mỗi phân vùng **có thứ tự**, xét tối đa 9 điểm:

| Điểm | Ý nghĩa |
|---|---|
| LB-1, LB, LB+1 | Ngay dưới, tại, ngay trên cận dưới |
| UB-1, UB, UB+1 | Ngay dưới, tại, ngay trên cận trên |
| Nhỏ nhất giao diện cho nhập | Giá trị nhỏ nhất có thể đưa vào qua giao diện |
| Lớn nhất giao diện cho nhập | Giá trị lớn nhất có thể đưa vào qua giao diện |
| Giữa | Một giá trị nằm giữa phân vùng hợp lệ |

Chỉ áp BVA cho phân vùng có thứ tự (độ dài, số lượng). Các lớp về định dạng, tập ký tự, tính duy nhất không có thứ tự nên đã đủ ở S2, S3.

Điểm nào trùng với test case đã có ở `03_tc.md` thì ghi lại mã đó, không tạo test case mới.

## 2. Quy ước

- Mã test case mới: `TC-REG-1NN` (dải 100 đến 199). Email theo mẫu `tc1NN@domain.com`, trừ khi chính email là đối tượng test.
- `␣` là một dấu cách. Chuỗi dài ghi dạng "`tc118@` + 62 chữ `a` + `.com`".
- Giá trị cơ sở, tiền điều kiện, quy trình chạy và cách đọc OUT1, OUT2, OUT3, OUT4 như `03_tc.md` mục 3.
- Các test case S4 chạy ở bước 2 của thứ tự chạy (`03_tc.md` mục 8), tức là trước TC-REG-79.

## 3. Các phân vùng có thứ tự

| Mã | Phân vùng | Cận dưới (LB) | Cận trên (UB) | Căn cứ |
|---|---|---|---|---|
| P1 | Độ dài Họ Tên sau khi cắt khoảng trắng | 1 | Không có | FR01-R01; `02_ec.md` mục 2 (cận dưới); A01 |
| P2 | Độ dài Mật khẩu (không cắt khoảng trắng) | 8 (lớp hợp lệ); lớp không hợp lệ là 1 đến 7 | Không có | FR01-R06; A08; nguyên tắc khoảng trắng |
| P3 | Số ký tự mỗi loại trong Mật khẩu (chữ hoa, chữ thường, chữ số, ký tự đặc biệt) | 1 | Không có | FR01-R07 đến FR01-R10 ("có ít nhất 1") |
| P4 | Độ dài phần trước `@` của Email | 1 | Không có (HTML5 không giới hạn) | A04 (b) |
| P5 | Độ dài một nhãn tên miền | 1 | 63 (tính trên dạng punycode nếu có chữ có dấu) | A04 (b); A15 (b), hệ quả 3 |
| P6 | Tổng độ dài Email | 3 (dạng ngắn nhất `a@b`) | Không có | A05 |
| P7 | Số dấu cách trong giá trị chỉ gồm khoảng trắng (Họ Tên, Email) | 1 | Không có | Nguyên tắc khoảng trắng; A03, A07 |
| P8 | Mức khác biệt giữa Xác nhận mật khẩu và Mật khẩu | 0 (khớp) | Không áp dụng | FR01-R12; A14 |

---

## 4. Bảng giá trị biên

### 4.1 P1: Độ dài Họ Tên (sau khi cắt khoảng trắng)

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập, LB-1 | (để trống) | 0 | KH | OUT2, ERR1 | TC-REG-30 (đã có) |
| LB | `A` | 1 | H | OUT1 | TC-REG-101 (mới) |
| LB+1 | `An` | 2 | H | OUT1 | TC-REG-102 (mới) |
| Giữa | `Nguyen Van A` | 12 | H | OUT1 | TC-REG-01 (đã có) |
| UB-1, UB, UB+1 | Không áp dụng | | | | A01: Không giới hạn |
| Lớn nhất giao diện cho nhập | 1000 chữ `a` (dán vào ô) | 1000 | H | OUT1. Ghi lại ở S6 số ký tự ô thực sự nhận | TC-REG-103 (mới) |

### 4.2 P7: Số dấu cách trong giá trị chỉ gồm khoảng trắng

| Điểm | Trường | Giá trị | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB (nhỏ nhất) | Họ Tên | `␣` (1 dấu cách) | KH | OUT2, ERR1 | TC-REG-104 (mới) |
| Giữa | Họ Tên | `␣␣␣` (3 dấu cách) | KH | OUT2, ERR1 | TC-REG-31 (đã có) |
| LB (nhỏ nhất) | Email | `␣` (1 dấu cách) | KH | OUT2, ERR2 | TC-REG-124 (mới) |
| Giữa | Email | `␣␣␣` (3 dấu cách) | KH | OUT2, ERR2 | TC-REG-33 (đã có) |

LB-1 (0 dấu cách) chính là giá trị rỗng: TC-REG-30 (Họ Tên), TC-REG-32 (Email).

### 4.3 P2: Độ dài Mật khẩu

Mật khẩu và Xác nhận mật khẩu nhập giống nhau. Mọi giá trị dưới đây đều đủ 4 loại ký tự, trừ những giá trị ghi chú khác, để lỗi duy nhất (nếu có) là độ dài.

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | 0 | KH | OUT2, ERR5 | TC-REG-49 (đã có) |
| LB của lớp không hợp lệ 1 đến 7 | `A` | 1 | KH | OUT2, ERR6 | TC-REG-105 (mới). **Ngoại lệ:** Mật khẩu 1 ký tự không thể đủ 4 loại, nên vi phạm thêm FR01-R08 đến FR01-R10 |
| Giữa lớp không hợp lệ 1 đến 7 | `Aa1!` | 4 | KH | OUT2, ERR6 | TC-REG-106 (mới). Độ dài nhỏ nhất mà chỉ vi phạm điều kiện độ dài |
| LB-1 (UB của lớp 1 đến 7) | `Abcde1!` | 7 | KH | OUT2, ERR6 | TC-REG-107 (mới) |
| LB | `Abcdef1!` | 8 | H | OUT1 | TC-REG-01 (đã có) |
| LB+1 | `Abcdefg1!` | 9 | H | OUT1 | TC-REG-108 (mới) |
| Giữa lớp hợp lệ | `Abcdefghijklmnopqr1!` | 20 | H | OUT1 | TC-REG-109 (mới) |
| UB-1, UB, UB+1 | Không áp dụng | | | | A08: Không giới hạn |
| Lớn nhất giao diện cho nhập | `Abcdef1!` + 992 chữ `a` | 1000 | H | OUT1. Ghi lại ở S6 số ký tự ô thực sự nhận | TC-REG-110 (mới) |

Biên liên quan tới khoảng trắng (không cắt khoảng trắng, khoảng trắng tính vào độ dài):

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB, khoảng trắng ở cuối | `Abcde1!␣` | 8 | H | OUT1 | TC-REG-18 (đã có) |
| LB, khoảng trắng ở đầu | `␣Abcde1!` | 8 | H | OUT1 | TC-REG-111 (mới). Hệ thống có thể chỉ cắt một phía, nên xét riêng đầu và cuối |

### 4.4 P3: Số ký tự mỗi loại trong Mật khẩu

| Điểm | Giá trị | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|
| LB-1 (0 ký tự của loại đó) | `abcdef1!`, `ABCDEF1!`, `Abcdefg!`, `Abcdefg1` | KH | OUT2, ERR6 | TC-REG-51, TC-REG-53, TC-REG-55, TC-REG-56 (đã có) |
| LB (đúng 1): Chữ hoa, chữ số, ký tự đặc biệt | `Abcdef1!` | H | OUT1 | TC-REG-01 (đã có) |
| LB (đúng 1): Chữ thường | `ABCDEf1!` | H | OUT1 | TC-REG-112 (mới) |
| LB+1 (đúng 2 mỗi loại) | `AAbb11!!` | H | OUT1 | TC-REG-113 (mới) |
| UB | Không áp dụng | | | Đặc tả chỉ có "ít nhất" |

### 4.5 P4: Độ dài phần trước `@`

| Điểm | Giá trị | Độ dài phần trước `@` | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB-1 | `@domain.com` | 0 | KH | OUT2, ERR3 | TC-REG-35 (đã có) |
| LB | `t@domain.com` | 1 | H | OUT1 | TC-REG-114 (mới). Không theo mẫu `tcNN` vì độ dài là đối tượng test |
| LB+1 | `tc@domain.com` | 2 | H | OUT1 | TC-REG-115 (mới) |
| Giữa | `tc01@domain.com` | 4 | H | OUT1 | TC-REG-01 (đã có) |
| UB và lớn nhất giao diện cho nhập | Xem P6 | | | | |

### 4.6 P5: Độ dài một nhãn tên miền

| Điểm | Giá trị | Độ dài nhãn | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB-1 | `tc39@.domain.com` | 0 | KH | OUT2, ERR3 | TC-REG-39 (đã có) |
| LB | `tc116@a.com` | 1 | H | OUT1 | TC-REG-116 (mới) |
| LB+1 | `tc117@ab.com` | 2 | H | OUT1 | TC-REG-117 (mới) |
| Giữa | `tc01@domain.com` | 6 | H | OUT1 | TC-REG-01 (đã có) |
| UB-1 | `tc118@` + 62 chữ `a` + `.com` | 62 | H | OUT1 | TC-REG-118 (mới) |
| UB | `tc119@` + 63 chữ `a` + `.com` | 63 | H | OUT1 | TC-REG-119 (mới) |
| UB+1 | `tc120@` + 64 chữ `a` + `.com` | 64 | KH | OUT2, ERR3 | TC-REG-120 (mới) |

Nhãn có chữ có dấu (A15 (b), hệ quả 3: Độ dài tính trên dạng punycode). Độ dài punycode được tính bằng bộ mã hóa IDNA chuẩn của Python:

| Điểm | Giá trị | Độ dài dạng có dấu | Độ dài dạng punycode | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|---|
| UB | `tc121@tên` + 53 chữ `a` + `.vn` | 56 | 63 | H | OUT1 | TC-REG-121 (mới) |
| UB+1 | `tc122@tên` + 54 chữ `a` + `.vn` | 57 | 64 | KH | OUT2, ERR3 | TC-REG-122 (mới). Nếu hệ thống đếm theo dạng có dấu (57 ký tự) thì sẽ chấp nhận nhầm |

TC-REG-121, TC-REG-122 phụ thuộc trình duyệt chuyển punycode (A15 (b)); chỉ chạy qua giao diện, ghi phiên bản trình duyệt.

### 4.7 P6: Tổng độ dài Email

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất hợp lệ | `t@a` | 3 | H | OUT1 | TC-REG-114, TC-REG-116 đã phủ từng phần; xem ghi chú |
| Lớn nhất giao diện cho nhập | Phần trước `@` là `tc123` + 995 chữ `a`, phần sau là `@domain.com` | 1011 | H | OUT1. Ghi lại ở S6 số ký tự ô thực sự nhận | TC-REG-123 (mới) |

Ghi chú:

- Không tạo test case riêng cho `t@a`: Giá trị này gộp LB của P4 (TC-REG-114), LB của P5 (TC-REG-116) và dạng không có dấu chấm (EC16, TC-REG-10). Ba test case đó đã phủ từng thành phần.
- TC-REG-123: Theo A04 (b) và A05, email này hợp lệ. Chuẩn email RFC giới hạn phần trước `@` 64 ký tự, nhưng giả định đã chọn là HTML5, không có giới hạn này. Nếu hệ thống từ chối, đó là **khác với giả định A05**, chưa chắc là lỗi so với đặc tả; cần sinh viên xét lại ở S5 hoặc S7.

### 4.8 P8: Mức khác biệt giữa Xác nhận mật khẩu và Mật khẩu

Mật khẩu là `Abcdef1!`. Các giá trị dưới đây là những giá trị "gần khớp nhất" mà vẫn không khớp, nhắm vào lỗi so sánh sai (chỉ so phần đầu, chỉ so độ dài). Tất cả dự kiến Blocked do D01.

| Điểm | Xác nhận mật khẩu | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|
| Khớp (0 khác biệt) | `Abcdef1!` | H | OUT1 | TC-REG-01 (đã có, chỉ phủ trên thiết kế) |
| Thiếu ký tự cuối | `Abcdef1` | KH | OUT2, ERR7 | TC-REG-125 (mới) |
| Thừa 1 ký tự ở cuối | `Abcdef1!a` | KH | OUT2, ERR7 | TC-REG-126 (mới) |
| Khác ký tự đầu | `Bbcdef1!` | KH | OUT2, ERR7 | TC-REG-127 (mới) |
| Khác ký tự cuối | `Abcdef1@` | KH | OUT2, ERR7 | TC-REG-128 (mới) |
| Chỉ khác hoa thường, khác khoảng trắng | | KH | OUT2, ERR7 | TC-REG-61, TC-REG-62 (đã có) |

### 4.9 Biên qua API

Theo `03_tc.md` mục 1: Nhóm API dùng cho các giá trị mà giao diện hoặc trình duyệt có thể chặn trước khi gửi. Đề xuất hai biên quan trọng nhất:

| TC | Biên | Body JSON | Kết quả mong đợi |
|---|---|---|---|
| TC-REG-129 | P2, LB-1 (mật khẩu 7 ký tự) | `{"name": "Nguyen Van A", "email": "tc129@domain.com", "password": "Abcde1!"}` | OUT4; kiểm chứng không tạo tài khoản |
| TC-REG-130 | P5, UB+1 (nhãn 64 ký tự) | `{"name": "Nguyen Van A", "email": "tc130@` + 64 chữ `a` + `.com", "password": "Abcdef1!"}` | OUT4 |

LB của P2 qua API (8 ký tự) đã có ở TC-REG-70.

---

## 5. Điểm không áp dụng và lý do

| Phân vùng | Điểm không áp dụng | Lý do |
|---|---|---|
| P1, P2, P4, P6 | UB-1, UB, UB+1 | Đặc tả không nêu giới hạn trên (A01, A08, A05; HTML5 không giới hạn phần trước `@`). Thay bằng điểm "lớn nhất giao diện cho nhập" |
| P3 | UB-1, UB, UB+1 | Đặc tả chỉ nói "có ít nhất 1" |
| P5 | Nhỏ nhất, lớn nhất giao diện cho nhập | Nhãn tên miền không phải ô nhập riêng; độ dài tổng xét ở P6 |
| Mọi phân vùng | Giá trị lớn nhất giao diện cho nhập (thật) | Chưa biết ở bước thiết kế, vì không được dùng DevTools (WORKFLOW mục 1.1). TC-REG-103, TC-REG-110, TC-REG-123 dùng chuỗi 1000 ký tự để thăm dò. Nếu ở S6 thấy ô chỉ nhận tối đa N ký tự, bổ sung các điểm N-1, N, N+1 ở S5 |

---

## 6. Tổng hợp

| Phân vùng | Test case mới | Test case đã có được dùng lại |
|---|---|---|
| P1 | TC-REG-101, TC-REG-102, TC-REG-103 | TC-REG-30, TC-REG-01 |
| P7 | TC-REG-104, TC-REG-124 | TC-REG-31, TC-REG-33, TC-REG-30, TC-REG-32 |
| P2 | TC-REG-105 đến TC-REG-111 | TC-REG-49, TC-REG-01, TC-REG-18 |
| P3 | TC-REG-112, TC-REG-113 | TC-REG-51, TC-REG-53, TC-REG-55, TC-REG-56, TC-REG-01 |
| P4 | TC-REG-114, TC-REG-115 | TC-REG-35, TC-REG-01 |
| P5 | TC-REG-116 đến TC-REG-122 | TC-REG-39, TC-REG-01 |
| P6 | TC-REG-123 | TC-REG-114, TC-REG-116, TC-REG-10 |
| P8 | TC-REG-125 đến TC-REG-128 | TC-REG-01, TC-REG-61, TC-REG-62 |
| API | TC-REG-129, TC-REG-130 | TC-REG-70 |

Tổng: 30 test case mới (TC-REG-101 đến TC-REG-130), gồm 28 qua giao diện (4 dự kiến Blocked do D01) và 2 qua API.

### 6.1 Truy vết bổ sung

| Yêu cầu | Test case BVA |
|---|---|
| FR01-R01 | TC-REG-101 đến TC-REG-104 |
| FR01-R02 | TC-REG-124 |
| FR01-R04 | TC-REG-114 đến TC-REG-123, TC-REG-130 |
| FR01-R06 | TC-REG-105 đến TC-REG-111, TC-REG-129 |
| FR01-R07 đến FR01-R10 | TC-REG-112, TC-REG-113 |
| FR01-R12 | TC-REG-125 đến TC-REG-128 |

---

## 7. Điểm cần sinh viên quyết định khi review

| # | Vấn đề | Các lựa chọn |
|---|---|---|
| 1 | Độ dài thăm dò "lớn nhất giao diện cho nhập" (TC-REG-103, TC-REG-110, TC-REG-123) | (a) 1000 ký tự; (b) Độ dài khác (sinh viên chỉ rõ) |
| 2 | TC-REG-105 (mật khẩu 1 ký tự) vi phạm nhiều điều kiện cùng lúc | (a) Giữ, ghi là ngoại lệ như TC-REG-58; (b) Bỏ, dùng TC-REG-106 (4 ký tự) làm giá trị nhỏ nhất chỉ vi phạm độ dài |
| 3 | P3 (số ký tự mỗi loại): LB đã gần như phủ bởi TC-REG-01 | (a) Giữ TC-REG-112, TC-REG-113; (b) Bỏ P3 |
| 4 | Biên qua API | (a) Giữ 2 test case như mục 4.9; (b) Thêm biên khác qua API (sinh viên chỉ rõ) |
| 5 | Nếu TC-REG-123 bị từ chối | (a) Ghi là khác giả định A05, sinh viên xét ở S5 hoặc S7 trước khi coi là bug; (b) Coi là bug ngay |
| 6 | TC-REG-111 (khoảng trắng ở đầu mật khẩu) | (a) Giữ; (b) Bỏ, chỉ giữ TC-REG-18 |
