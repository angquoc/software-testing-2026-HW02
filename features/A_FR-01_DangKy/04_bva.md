# S4: Phân tích giá trị biên (FR-01 Đăng ký tài khoản)

- Bước: S4 (Boundary Value Analysis, theo Step 4 của slide S04)
- Bản này: Bản review của S4. Bản gốc của AI: `ai_raw/S4_bva.md`
- Thời gian tạo bản AI: 2026-10-20 13:14 (+07:00)
- Cập nhật theo câu hỏi và quyết định của sinh viên: 2026-10-20 13:58 (+07:00). Các thay đổi so với bản AI liệt kê ở mục 10
- Cập nhật lần 2: 2026-10-20 14:30 (+07:00). Bỏ TC-REG-124 theo quyết định của sinh viên ở mục 7
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
| Giữa | Một giá trị nằm bên trong phân vùng hợp lệ |

Chỉ áp BVA cho phân vùng có thứ tự (độ dài, số lượng). Các lớp về định dạng, tập ký tự, tính duy nhất, so khớp chuỗi không có thứ tự nên đã đủ ở S2, S3.

Điểm nào trùng với test case đã có ở `03_tc.md` thì ghi lại mã đó, không tạo test case mới. Một điểm chỉ được tạo test case khi giá trị đó **chỉ vi phạm đúng một điều kiện** (hoặc không vi phạm điều kiện nào); nếu không thể, ghi lý do ở mục 5.

## 2. Quy ước

- Mã test case mới: `TC-REG-1NN` (dải 100 đến 199). Email theo mẫu `tc1NN@domain.com`, trừ khi chính email là đối tượng test. Mã của các test case bị bỏ khi review (TC-REG-105, TC-REG-109, TC-REG-124, TC-REG-125 đến TC-REG-128) không dùng lại.
- `␣` là một dấu cách. Chuỗi dài ghi dạng "`tc118@` + 62 chữ `a` + `.com`".
- Giá trị cơ sở, tiền điều kiện, quy trình chạy và cách đọc OUT1, OUT2, OUT3, OUT4 như `03_tc.md` mục 3.
- Các test case S4 chạy ở bước 2 của thứ tự chạy (`03_tc.md` mục 8), tức là trước TC-REG-79.
- Ô Email có thể dùng `type="email"` (kiểm ở TC-REG-96). Khi đó trình duyệt tự cắt khoảng trắng đầu cuối trước khi gửi (`03_tc.md` mục 10.2), nên biên về khoảng trắng của Email phải kiểm qua API.

## 3. Các phân vùng có thứ tự

| Mã | Phân vùng | Cận dưới (LB) | Cận trên (UB) | Căn cứ |
|---|---|---|---|---|
| P1 | Độ dài Họ Tên sau khi cắt khoảng trắng | 1 | Không có | FR01-R01; `02_ec.md` mục 2 (cận dưới và biến thể có khoảng trắng); A01 |
| P2 | Độ dài Mật khẩu (không cắt khoảng trắng) | 8 (lớp hợp lệ); lớp không hợp lệ là 1 đến 7 | Không có | FR01-R06; A08; nguyên tắc khoảng trắng |
| P3 | Số ký tự mỗi loại trong Mật khẩu (chữ hoa, chữ thường, chữ số, ký tự đặc biệt) | 1 | Không có | FR01-R07 đến FR01-R10 ("có ít nhất 1") |
| P4 | Độ dài phần trước `@` của Email | 1 | Không có (HTML5 không giới hạn) | A04 (b) |
| P5 | Độ dài một nhãn tên miền | 1 | 63 (tính trên dạng punycode nếu có chữ có dấu) | A04 (b); A15 (b), hệ quả 3 |
| P6 | Tổng độ dài Email | 3 (dạng ngắn nhất `a@b`) | Không có | A05 |
| P7 | Số dấu cách trong giá trị chỉ gồm khoảng trắng (Họ Tên, Email) | 1 | Không có | Nguyên tắc khoảng trắng; A03, A07 |

Không xét BVA cho việc so khớp Xác nhận mật khẩu với Mật khẩu: Đây là phép so sánh bằng, không có thứ tự (mục 9, câu 4).

---

## 4. Bảng giá trị biên

### 4.1 P1: Độ dài Họ Tên (sau khi cắt khoảng trắng)

| Điểm | Giá trị | Độ dài trước khi cắt | Độ dài sau khi cắt | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập, LB-1 | (để trống) | 0 | 0 | KH | OUT2, ERR1 | TC-REG-30 (đã có) |
| LB | `A` | 1 | 1 | H | OUT1 | TC-REG-101 |
| LB, có khoảng trắng hai bên | `␣A␣` | 3 | 1 | H | OUT1 | TC-REG-131 (thêm khi review) |
| LB+1 | `An` | 2 | 2 | H | OUT1 | TC-REG-102 |
| Giữa | `Nguyen Van A` | 12 | 12 | H | OUT1 | TC-REG-01 (đã có) |
| UB-1, UB, UB+1 | Không áp dụng | | | | | A01: Không giới hạn |
| Lớn nhất giao diện cho nhập | 1000 chữ `a` (dán vào ô) | 1000 | 1000 | H | OUT1. Ghi lại ở S6 số ký tự ô thực sự nhận | TC-REG-103 |

TC-REG-131 nhắm vào thứ tự giữa bước cắt khoảng trắng và bước kiểm tra độ dài: Nếu bước cắt bị cài sai (ví dụ cắt mất cả ký tự duy nhất) thì giá trị còn lại rỗng và hệ thống báo ERR1 sai.

### 4.2 P7: Số dấu cách trong giá trị chỉ gồm khoảng trắng

| Điểm | Trường | Giá trị | Cách gửi | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|---|
| LB (nhỏ nhất) | Họ Tên | `␣` (1 dấu cách) | Giao diện | KH | OUT2, ERR1 | TC-REG-104 |
| Giữa | Họ Tên | `␣␣␣` (3 dấu cách) | Giao diện | KH | OUT2, ERR1 | TC-REG-31 (đã có) |
| Giá trị chỉ gồm khoảng trắng | Email | 3 dấu cách | API | KH | OUT4 | TC-REG-80 (đã có) |

LB-1 (0 dấu cách) chính là giá trị rỗng: TC-REG-30 (Họ Tên), TC-REG-32 (Email). Không tạo test case Email là 1 dấu cách: Qua giao diện, nếu ô dùng `type="email"` thì trình duyệt cắt thành chuỗi rỗng trước khi gửi, nên trùng TC-REG-32 (mục 9, câu 5); qua API thì TC-REG-80 (3 dấu cách) đã kiểm việc EShop xử lý email chỉ gồm khoảng trắng (mục 7).

### 4.3 P2: Độ dài Mật khẩu

Mật khẩu và Xác nhận mật khẩu nhập giống nhau. Mọi giá trị dưới đây đều đủ 4 loại ký tự, để lỗi duy nhất (nếu có) là độ dài.

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | 0 | KH | OUT2, ERR5 | TC-REG-49 (đã có) |
| Giá trị nhỏ nhất chỉ vi phạm độ dài (thay cho LB của lớp 1 đến 7) | `Aa1!` | 4 | KH | OUT2, ERR6 | TC-REG-106 |
| LB-1 (UB của lớp 1 đến 7) | `Abcde1!` | 7 | KH | OUT2, ERR6 | TC-REG-107 |
| LB | `Abcdef1!` | 8 | H | OUT1 | TC-REG-01 (đã có) |
| LB+1 | `Abcdefg1!` | 9 | H | OUT1 | TC-REG-108 |
| Giữa | Không xác định | | | | Phân vùng hợp lệ không có cận trên nên không có "giữa"; xem mục 5 |
| UB-1, UB, UB+1 | Không áp dụng | | | | A08: Không giới hạn |
| Lớn nhất giao diện cho nhập | `Abcdef1!` + 992 chữ `a` | 1000 | H | OUT1. Ghi lại ở S6 số ký tự ô thực sự nhận | TC-REG-110 |

Biên liên quan tới khoảng trắng (không cắt khoảng trắng, khoảng trắng tính vào độ dài):

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB, khoảng trắng ở cuối | `Abcde1!␣` | 8 | H | OUT1 | TC-REG-18 (đã có) |
| LB, khoảng trắng ở đầu | `␣Abcde1!` | 8 | H | OUT1 | TC-REG-111. Hệ thống có thể chỉ cắt một phía, nên xét riêng đầu và cuối |

Ô Mật khẩu không bị trình duyệt cắt khoảng trắng, nên TC-REG-111 và TC-REG-18 kiểm đúng hành vi của EShop.

### 4.4 P3: Số ký tự mỗi loại trong Mật khẩu

| Điểm | Giá trị | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|
| LB-1 (0 ký tự của loại đó) | `abcdef1!`, `ABCDEF1!`, `Abcdefg!`, `Abcdefg1` | KH | OUT2, ERR6 | TC-REG-51, TC-REG-53, TC-REG-55, TC-REG-56 (đã có) |
| LB (đúng 1): Chữ hoa, chữ số, ký tự đặc biệt | `Abcdef1!` | H | OUT1 | TC-REG-01 (đã có) |
| LB (đúng 1): Chữ thường | `ABCDEf1!` | H | OUT1 | TC-REG-112 |
| LB+1 (đúng 2 mỗi loại) | `AAbb11!!` | H | OUT1 | TC-REG-113 |
| UB | Không áp dụng | | | Đặc tả chỉ có "ít nhất" |

### 4.5 P4: Độ dài phần trước `@`

| Điểm | Giá trị | Độ dài phần trước `@` | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB-1 | `@domain.com` | 0 | KH | OUT2, ERR3 | TC-REG-35 (đã có) |
| LB | `t@domain.com` | 1 | H | OUT1 | TC-REG-114. Không theo mẫu `tcNN` vì độ dài là đối tượng test |
| LB+1 | `tc@domain.com` | 2 | H | OUT1 | TC-REG-115 |
| Giữa | `tc01@domain.com` | 4 | H | OUT1 | TC-REG-01 (đã có) |
| UB và lớn nhất giao diện cho nhập | Xem P6 | | | | |

### 4.6 P5: Độ dài một nhãn tên miền

| Điểm | Giá trị | Độ dài nhãn | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| LB-1 | `tc39@.domain.com` | 0 | KH | OUT2, ERR3 | TC-REG-39 (đã có) |
| LB | `tc116@a.com` | 1 | H | OUT1 | TC-REG-116 |
| LB+1 | `tc117@ab.com` | 2 | H | OUT1 | TC-REG-117 |
| Giữa | `tc01@domain.com` | 6 | H | OUT1 | TC-REG-01 (đã có) |
| UB-1 | `tc118@` + 62 chữ `a` + `.com` | 62 | H | OUT1 | TC-REG-118 |
| UB | `tc119@` + 63 chữ `a` + `.com` | 63 | H | OUT1 | TC-REG-119 |
| UB+1 | `tc120@` + 64 chữ `a` + `.com` | 64 | KH | OUT2, ERR3 | TC-REG-120 |

Nhãn có chữ có dấu (A15 (b), hệ quả 3: Độ dài tính trên dạng punycode). Độ dài punycode được tính bằng bộ mã hóa IDNA chuẩn của Python:

| Điểm | Giá trị | Độ dài dạng có dấu | Độ dài dạng punycode | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|---|
| UB | `tc121@tên` + 53 chữ `a` + `.vn` | 56 | 63 | H | OUT1 | TC-REG-121 |
| UB+1 | `tc122@tên` + 54 chữ `a` + `.vn` | 57 | 64 | KH | OUT2, ERR3 | TC-REG-122. Nếu hệ thống đếm theo dạng có dấu (57 ký tự) thì sẽ chấp nhận nhầm |

TC-REG-121, TC-REG-122 phụ thuộc trình duyệt chuyển punycode (A15 (b)); chỉ chạy qua giao diện, ghi phiên bản trình duyệt.

### 4.7 P6: Tổng độ dài Email

| Điểm | Giá trị | Độ dài | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất hợp lệ | `t@a` | 3 | H | OUT1 | Không tạo riêng; xem ghi chú |
| Lớn nhất giao diện cho nhập | Phần trước `@` là `tc123` + 995 chữ `a`, phần sau là `@domain.com` | 1011 | H | OUT1. Ghi lại ở S6 số ký tự ô thực sự nhận | TC-REG-123 |

Ghi chú:

- Không tạo test case riêng cho `t@a`: Giá trị này gộp LB của P4 (TC-REG-114), LB của P5 (TC-REG-116) và dạng không có dấu chấm (EC16, TC-REG-10). Ba test case đó đã phủ từng thành phần.
- TC-REG-123: Theo A04 (b) và A05, email này hợp lệ. Chuẩn email RFC giới hạn phần trước `@` 64 ký tự, nhưng giả định đã chọn là HTML5, không có giới hạn này. Nếu hệ thống từ chối, ghi là **khác với giả định A05**; sinh viên xét ở S5 hoặc S7 trước khi coi là bug (quyết định 5).

### 4.8 Biên qua API

| TC | Biên | Body JSON | Kết quả mong đợi |
|---|---|---|---|
| TC-REG-129 | P2, LB-1 (mật khẩu 7 ký tự) | `{"name": "Nguyen Van A", "email": "tc129@domain.com", "password": "Abcde1!"}` | OUT4; kiểm chứng không tạo tài khoản |
| TC-REG-130 | P5, UB+1 (nhãn 64 ký tự) | `{"name": "Nguyen Van A", "email": "tc130@` + 64 chữ `a` + `.com", "password": "Abcdef1!"}` | OUT4 |

LB của P2 qua API (8 ký tự) đã có ở TC-REG-70.

---

## 5. Điểm không áp dụng hoặc không tạo test case, và lý do

| Phân vùng | Điểm | Lý do |
|---|---|---|
| P1, P2, P4, P6 | UB-1, UB, UB+1 | Đặc tả không nêu giới hạn trên (A01, A08, A05; HTML5 không giới hạn phần trước `@`). Thay bằng điểm "lớn nhất giao diện cho nhập" |
| P2 | LB của lớp không hợp lệ 1 đến 7 (mật khẩu 1 ký tự) | Mật khẩu từ 1 đến 3 ký tự không thể đủ 4 loại ký tự, nên luôn vi phạm cùng lúc độ dài và ít nhất một điều kiện loại ký tự; khi bị từ chối không biết vì điều kiện nào. Thay bằng `Aa1!` (4 ký tự), giá trị nhỏ nhất chỉ vi phạm độ dài (quyết định 2) |
| P2 | Giữa | Phân vùng hợp lệ (từ 8 ký tự trở lên) không có cận trên nên không có điểm "giữa". Mọi giá trị từ 9 ký tự trở lên đều cùng lớp với TC-REG-108, không thêm rủi ro mới; đầu lớn của phân vùng đã có TC-REG-110 |
| P3 | UB-1, UB, UB+1 | Đặc tả chỉ nói "có ít nhất 1" |
| P5 | Nhỏ nhất, lớn nhất giao diện cho nhập | Nhãn tên miền không phải ô nhập riêng; độ dài tổng xét ở P6 |
| P7 | Email là 1 dấu cách | Qua giao diện: Trình duyệt có thể cắt thành rỗng, trùng TC-REG-32. Qua API: TC-REG-80 (3 dấu cách) đã kiểm cùng hành vi (quyết định ở mục 7) |
| Mọi phân vùng | Giá trị lớn nhất giao diện cho nhập (thật) | Chưa biết ở bước thiết kế, vì không được dùng DevTools (WORKFLOW mục 1.1). TC-REG-103, TC-REG-110, TC-REG-123 dùng chuỗi khoảng 1000 ký tự để thăm dò (quyết định 1). Nếu ở S6 thấy ô chỉ nhận tối đa N ký tự, bổ sung các điểm N-1, N, N+1 ở S5 |
| So khớp Xác nhận mật khẩu | Mọi điểm | Phép so sánh bằng không có thứ tự, không thuộc BVA (mục 9, câu 4) |

---

## 6. Tổng hợp

| Phân vùng | Test case mới | Test case đã có được dùng lại |
|---|---|---|
| P1 | TC-REG-101, TC-REG-102, TC-REG-103, TC-REG-131 | TC-REG-30, TC-REG-01 |
| P7 | TC-REG-104 | TC-REG-31, TC-REG-80, TC-REG-30, TC-REG-32 |
| P2 | TC-REG-106, TC-REG-107, TC-REG-108, TC-REG-110, TC-REG-111 | TC-REG-49, TC-REG-01, TC-REG-18 |
| P3 | TC-REG-112, TC-REG-113 | TC-REG-51, TC-REG-53, TC-REG-55, TC-REG-56, TC-REG-01 |
| P4 | TC-REG-114, TC-REG-115 | TC-REG-35, TC-REG-01 |
| P5 | TC-REG-116 đến TC-REG-122 | TC-REG-39, TC-REG-01 |
| P6 | TC-REG-123 | TC-REG-114, TC-REG-116, TC-REG-10 |
| API | TC-REG-129, TC-REG-130 | TC-REG-70, TC-REG-80 |

Tổng: 24 test case mới, gồm 22 qua giao diện và 2 qua API (TC-REG-129, TC-REG-130). Không còn test case BVA nào dự kiến Blocked.

### 6.1 Truy vết bổ sung

| Yêu cầu | Test case BVA |
|---|---|
| FR01-R01 | TC-REG-101 đến TC-REG-104, TC-REG-131 |
| FR01-R04 | TC-REG-114 đến TC-REG-123, TC-REG-130 |
| FR01-R06 | TC-REG-106, TC-REG-107, TC-REG-108, TC-REG-110, TC-REG-111, TC-REG-129 |
| FR01-R07 đến FR01-R10 | TC-REG-112, TC-REG-113 |

FR01-R02 và FR01-R12 không có test case BVA mới. FR01-R02: Các điểm biên dùng lại TC-REG-32 và TC-REG-80. FR01-R12: So khớp chuỗi không thuộc BVA (mục 5, dòng cuối); vẫn được phủ bởi TC-REG-59 đến TC-REG-62 ở `03_tc.md`.

---

## 7. Kiểm tra mâu thuẫn giữa các quyết định

| Quyết định hoặc câu hỏi | Kết quả kiểm tra |
|---|---|
| Quyết định 2 (b) và câu hỏi 2 | Thống nhất: Cùng bỏ TC-REG-105 |
| Quyết định 3 (a) (giữ P3) và câu hỏi 3 (bỏ TC-REG-109) | Không mâu thuẫn: TC-REG-113 là điểm LB+1, một điểm biên chuẩn của slide; còn TC-REG-109 là điểm "giữa" của phân vùng không có cận trên, không xác định được |
| Quyết định 6 (a) (giữ TC-REG-111) và câu hỏi 1 (thêm TC-REG-131) | Thống nhất: Cả hai cùng nhắm vào cách hệ thống xử lý khoảng trắng ở từng phía |
| Quyết định 4 (a) (giữ 2 test case biên qua API) và câu hỏi 5 (TC-REG-124) | **Có vướng, đã xử lý:** Câu hỏi 5 dẫn tới việc chuyển TC-REG-124 sang API, làm nhóm biên qua API thành 3 test case. Bản cập nhật đầu chọn chuyển sang API. Sinh viên quyết định bỏ hẳn TC-REG-124, vì TC-REG-80 (3 dấu cách qua API) đã kiểm việc EShop xử lý email chỉ gồm khoảng trắng; nhóm biên qua API giữ đúng 2 test case như quyết định 4 (a) |
| Quyết định 1, 5 | Không liên quan tới các thay đổi khác |

---

## 8. Quyết định của sinh viên

| # | Vấn đề | Quyết định |
|---|---|---|
| 1 | Độ dài thăm dò "lớn nhất giao diện cho nhập" | (a) Khoảng 1000 ký tự |
| 2 | TC-REG-105 (mật khẩu 1 ký tự) | (b) Bỏ, dùng TC-REG-106 (4 ký tự) làm giá trị nhỏ nhất chỉ vi phạm độ dài |
| 3 | P3 (số ký tự mỗi loại) | (a) Giữ TC-REG-112, TC-REG-113 |
| 4 | Biên qua API | (a) Giữ TC-REG-129, TC-REG-130. Bỏ TC-REG-124 vì đã có TC-REG-80 (xem mục 7) |
| 5 | Nếu TC-REG-123 bị từ chối | (a) Ghi là khác giả định A05, sinh viên xét ở S5 hoặc S7 trước khi coi là bug |
| 6 | TC-REG-111 (khoảng trắng ở đầu mật khẩu) | (a) Giữ |

---

## 9. Trả lời câu hỏi khi review

| # | Câu hỏi | Trả lời | Thay đổi |
|---|---|---|---|
| 1 | Sao không có test case Họ Tên một ký tự có khoảng trắng hai bên (`␣A␣`)? | Đúng là thiếu. Cuối mục 2 của `02_ec.md` đã ghi biến thể này để S4 xét, nhưng bản AI bỏ qua vì cho rằng kết quả không phân biệt được hệ thống cắt khoảng trắng trước hay sau khi kiểm tra độ dài. Lập luận đó bỏ sót một lỗi khác: Bước cắt khoảng trắng bị cài sai, làm mất cả ký tự duy nhất, khiến hệ thống báo ERR1 sai | Thêm TC-REG-131 |
| 2 | TC-REG-105 vi phạm cùng lúc độ dài và 3 điều kiện loại ký tự, khi bị từ chối sao biết vì điều kiện nào? Có nhắm tới lỗi nào khác không? | Không biết được. Bản AI chọn giá trị này chỉ vì nó là "LB của lớp 1 đến 7" và "nhỏ nhất giao diện cho nhập" theo slide, không nhắm tới lỗi cụ thể nào khác. Vì ERR6 gộp mọi vi phạm độ mạnh, test case này không cho thêm thông tin so với TC-REG-106 | Bỏ TC-REG-105 (quyết định 2) |
| 3 | Vì sao cần mật khẩu 20 ký tự (TC-REG-109) khi đã có 9 ký tự? | Đúng, hai giá trị cùng một lớp. Bản AI thêm để điền điểm "giữa" theo slide, nhưng phân vùng hợp lệ không có cận trên nên "giữa" không xác định; 20 là con số tùy chọn, không thêm rủi ro mới | Bỏ TC-REG-109; ghi lý do ở mục 5 |
| 4 | Các trường hợp lệch 1 ký tự của Xác nhận mật khẩu (P8) có phải BVA không? | Không. So khớp là phép so sánh bằng, không có thứ tự; bản AI tự mâu thuẫn với nguyên tắc ở mục 1 của chính nó. Các giá trị "gần khớp" là đại diện theo rủi ro của lớp không hợp lệ EC42 (đã có TC-REG-59), không phải điểm biên. Thêm nữa, cả 4 đều dự kiến Blocked do D01 | Bỏ P8 và TC-REG-125 đến TC-REG-128 |
| 5 | TC-REG-124 (Email là 1 dấu cách) qua giao diện có bị ảnh hưởng bởi việc ô `type="email"` tự cắt khoảng trắng không? | Có. Nếu ô dùng `type="email"`, trình duyệt cắt 1 dấu cách thành chuỗi rỗng trước khi gửi, nên với EShop test case này giống hệt TC-REG-32 (Email rỗng). Bản AI đã bỏ qua ghi chú về điểm này ở `03_tc.md`. Điểm này do Claude ở phiên điều phối phát hiện khi soát lại | Bỏ TC-REG-124 (qua API đã có TC-REG-80); thêm quy ước ở mục 2 |

---

## 10. Thay đổi so với bản AI (`ai_raw/S4_bva.md`)

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 4.1, TC-REG-131 | Thêm điểm LB có khoảng trắng hai bên (`␣A␣`) cho Họ Tên | Thiếu | `02_ec.md` cuối mục 2 đã ghi biến thể này cho S4, bản AI bỏ qua. Sinh viên phát hiện (câu hỏi 1) |
| Mục 4.3, mục 5, TC-REG-105 | Bỏ mật khẩu 1 ký tự; ghi lý do và dùng `Aa1!` (4 ký tự) làm giá trị nhỏ nhất chỉ vi phạm độ dài | Thừa | Giá trị vi phạm nhiều điều kiện cùng lúc, không xác định được nguyên nhân. Sinh viên phát hiện (câu hỏi 2); quyết định 2 (b) |
| Mục 4.3, mục 5, TC-REG-109 | Bỏ mật khẩu 20 ký tự; điểm "giữa" của P2 ghi là không xác định | Thừa | Cùng lớp với TC-REG-108, phân vùng không có cận trên nên không có điểm giữa. Sinh viên phát hiện (câu hỏi 3) |
| Mục 3, mục 4.8 cũ, mục 5, TC-REG-125 đến TC-REG-128 | Bỏ phân vùng P8 (Xác nhận mật khẩu gần khớp) và 4 test case | Thừa | So khớp chuỗi không có thứ tự, trái với nguyên tắc ở mục 1 của chính bản AI; cả 4 đều dự kiến Blocked. Sinh viên phát hiện (câu hỏi 4) |
| Mục 4.2, mục 4.8, TC-REG-124 | Bỏ test case Email là 1 dấu cách | Thừa | Qua giao diện, trình duyệt có thể cắt thành rỗng nên trùng TC-REG-32 (Claude ở phiên điều phối phát hiện khi soát lại, câu hỏi 5). Qua API, TC-REG-80 (3 dấu cách) đã kiểm cùng hành vi (sinh viên quyết định, mục 7) |
| Mục 2 | Thêm quy ước: Biên về khoảng trắng của Email phải kiểm qua API | Thiếu | Như dòng trên; bản AI không áp ghi chú về `type="email"` đã có ở `03_tc.md` mục 10.2 |
| Mục 1 | Thêm nguyên tắc: Chỉ tạo test case cho điểm chỉ vi phạm đúng một điều kiện; nếu không thể, ghi lý do | Thiếu | Bản AI không có nguyên tắc này nên mới chọn TC-REG-105. AI bổ sung khi viết bản review, rút ra từ câu hỏi 2 |
| Mục 4.3 | Ghi chú ô Mật khẩu không bị trình duyệt cắt khoảng trắng, nên TC-REG-18, TC-REG-111 kiểm đúng hành vi của EShop | Thiếu | Làm rõ khác biệt với Email sau câu hỏi 5. AI bổ sung khi viết bản review |
| Mục 7 | Thêm phần kiểm tra mâu thuẫn giữa các quyết định; ghi điểm vướng giữa quyết định 4 (a) và câu hỏi 5 | Quyết định của SV | Sinh viên yêu cầu kiểm tra mâu thuẫn |
| Mục 4.7 | Ghi rõ cách xử lý nếu TC-REG-123 bị từ chối | Quyết định của SV | Quyết định 5 (a) |
| Mục 5 | Ghi độ dài thăm dò khoảng 1000 ký tự là lựa chọn đã chốt | Quyết định của SV | Quyết định 1 (a) |
| Mục 4.4 | Giữ P3 | Quyết định của SV | Quyết định 3 (a) |
| Mục 6 | Cập nhật tổng hợp: 24 test case mới (22 giao diện, 2 API), không còn test case dự kiến Blocked; cập nhật truy vết (FR01-R02, FR01-R12 không có test case BVA mới) | Quyết định của SV | Hệ quả của các thay đổi trên |
| Mục 8 | Thay bảng phương án bằng bảng quyết định | Quyết định của SV | Quyết định 1 đến 6 |
| Mục 9 | Thêm phần trả lời câu hỏi | Quyết định của SV | 5 câu hỏi khi review |
