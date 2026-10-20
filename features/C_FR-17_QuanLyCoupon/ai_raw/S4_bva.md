# S4: Phân tích giá trị biên (FR-17 Quản lý mã giảm giá)

- Bước: S4 (Phân tích giá trị biên, theo Step 4 của slide S04)
- Thời gian tạo: 2026-10-20 20:52 (UTC+07:00)
- Căn cứ: `02_ec.md` (mục 2, 4, 10); `03_tc.md` (mục 2, 3, 4, 16); `01_io.md` (mục 3)
- Quyết định sinh viên chốt trước khi viết:
  1. Bước nhảy: Điểm biên chính dùng bước 1 (số nguyên); thêm điểm bước `0.01` chỉ ở các biên mà phép so sánh viết sai chỉ lộ ra khi có số lẻ.
  2. Thăm dò độ dài `code`: Giữ TC-CPN-12 (255 ký tự), thêm điểm 1000 ký tự; ở S6 ghi số ký tự ô nhận, nếu ô giới hạn N ký tự thì S5 bổ sung N-1, N, N+1.
  3. Biên qua API: Như A2 của S3. Biên chạy qua giao diện; biên thập phân và biên âm có bản API dự phòng (một test case dạng bảng), chỉ chạy khi trình duyệt chặn.

---

## 1. Cách làm

- Theo Step 4 của slide S04: Với mỗi phân vùng **có thứ tự**, xét LB-1, LB, LB+1, UB-1, UB, UB+1, giá trị nhỏ nhất và lớn nhất giao diện cho nhập, một giá trị ở giữa. Không áp máy móc: Điểm nào không áp dụng ghi lý do.
- Không áp BVA cho định dạng, tập ký tự, tính duy nhất, tập giá trị `type`, người gọi API, dạng request: Không có thứ tự, đã đủ ở S2, S3.
- Mỗi điểm chỉ vi phạm đúng một điều kiện; các input khác lấy giá trị cơ sở của `03_tc.md` mục 2.2. Quy trình và kết quả mong đợi chung theo `03_tc.md` mục 2.3 (QT-GD, KQ-H-GD, KQ-KH-GD, KQ-H-API, KQ-KH-API).
- Điểm trùng giá trị của test case đã có thì dùng lại mã đó, ghi "(đã có)". Mã mới từ TC-CPN-100.
- Kết quả mong đợi theo giả định đã chốt. Nếu hệ thống làm khác **giả định** (không phải khác đặc tả), ghi "khác giả định" để sinh viên xét ở S5 hoặc S7 trước khi coi là bug.
- Số lớn: `2^53 + 1` = `9007199254740993` là số nguyên nhỏ nhất không biểu diễn chính xác được bằng số thực 64 bit (kiểu số của JSON trong JavaScript); khi bị chuyển kiểu, nó thành `9007199254740992`. Đã kiểm bằng Python: `float(2**53 + 1) == 2**53` cho `True`.
- `␣` là một dấu cách. Mã yêu cầu viết tắt `Rnn`.

## 2. Phân vùng có thứ tự

| Mã | Phân vùng | Cận dưới (LB) | Cận trên (UB) | Căn cứ |
|---|---|---|---|---|
| P1 | `discount_value`, loại `percent` | Lớn hơn 0 (số nguyên nhỏ nhất 1; số lẻ nhỏ nhất theo bước 0.01 là `0.01`) | 100 | FR-17 "(dương)"; A01 (a); A02 (a) |
| P2 | `discount_value`, loại `fixed` | Lớn hơn 0 (như P1) | Không có | FR-17 "(dương)"; A25 (b) |
| P3 | `min_order_amount` | 0 | Không có | FR-17 "(>= 0)"; A03 (i)(a), (iii)(b) |
| P4 | `max_uses_per_user` | 1 (chỉ số nguyên) | Không có | FR-17 "(>= 1)"; A03 (ii)(a), (iii)(b) |
| P5 | Độ dài `code` sau khi cắt khoảng trắng đầu cuối | 1 ký tự | Không có | FR-17 bắt buộc; A04 độ dài (b); A09 |
| P6 | `expired_at` so với ngày chạy, theo cách hiển thị | Không có cận hợp lệ, không hợp lệ khi tạo (A05 (c)); ranh giới hiển thị: Không sau hôm nay thì hiện "Hết hạn", từ ngày mai hiện ngày | Không có | A05 (c); A18 (b) |

## 3. Bảng giá trị biên

### 3.1 P1: `discount_value`, loại `percent`

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case | Dự phòng API |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | | KH | ERR5 | TC-CPN-40 (đã có) | |
| Giá trị âm | `-1` | -1 | KH | ERR6 | TC-CPN-100 | TC-CPN-130 dòng A |
| LB-1 | `0` | 0 | KH | ERR6 | TC-CPN-38 (đã có) | |
| LB theo bước 0.01 | `0.01` | 0.01 | H | OUT1; cột "Giá trị" hiện `0.01%` | TC-CPN-101 | TC-CPN-130 dòng B |
| LB | `1` | 1 | H | OUT1; hiện `1%` | TC-CPN-102 | |
| LB+1 | `2` | 2 | H | OUT1; hiện `2%` | TC-CPN-103 | |
| Giữa | `15` | 15 | H | OUT1 | TC-CPN-01 (đã có) | |
| UB-1 | `99` | 99 | H | OUT1; hiện `99%` | TC-CPN-104 | |
| UB | `100` | 100 | H | OUT1 | TC-CPN-14 (đã có) | |
| UB theo bước 0.01 | `100.01` | 100.01 | KH | ERR17 | TC-CPN-105 | TC-CPN-130 dòng C |
| UB+1 | `101` | 101 | KH | ERR17 | TC-CPN-106 | |
| Lớn nhất giao diện cho nhập | Không áp dụng | | | | | Đã có UB; giá trị lớn hơn thuộc cùng lớp với `101`, `150` (TC-CPN-37) |

Ghi chú: `-1` không phải điểm biên theo slide (thấp hơn LB-1) nhưng là đại diện theo rủi ro: Bắt luật "dương" bị viết thành "khác 0". `100.01` bắt luật viết thành "nhỏ hơn 101" thay cho "không lớn hơn 100".

### 3.2 P2: `discount_value`, loại `fixed`

Mọi dòng dùng "Số tiền cố định (₫)".

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case | Dự phòng API |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | | KH | ERR5 | TC-CPN-40 (đã có, cùng lớp EC40 cho cả hai loại) | |
| Giá trị âm | `-1` | -1 | KH | ERR6 | TC-CPN-107 | TC-CPN-130 dòng D |
| LB-1 | `0` | 0 | KH | ERR6 | TC-CPN-39 (đã có) | |
| LB theo bước 0.01 | `0.01` | 0.01 | H | OUT1; ghi lại cách cột "Giá trị" hiển thị; K6 có `0.01` | TC-CPN-108 | TC-CPN-130 dòng E |
| LB | `1` | 1 | H | OUT1; hiện `1 ₫` | TC-CPN-109 | |
| LB+1 | `2` | 2 | H | OUT1; hiện `2 ₫` | TC-CPN-110 | |
| Giữa, UB-1, UB, UB+1 | Không áp dụng | | | | | Không có cận trên (A25 (b)) |
| Lớn nhất giao diện cho nhập (độ lớn) | `10000000000000000` | 10^16 | H | OUT1 hiện đúng, hoặc ERR22 có thông báo rõ | TC-CPN-18 (đã có) | |
| Lớn nhất giao diện cho nhập (độ chính xác) | `9007199254740993` | 2^53 + 1 | H | Đạt nếu: OUT1 và cột "Giá trị" hiện đúng `9,007,199,254,740,993 ₫`, K6 có đúng `9007199254740993`; hoặc bị từ chối có thông báo rõ (ERR22). Sai nếu: Hiển thị hoặc lưu `...992`, lỗi máy chủ | TC-CPN-111 | |

### 3.3 P3: `min_order_amount`

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case | Dự phòng API |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | | KH | ERR8 | TC-CPN-42 (đã có) | |
| LB-1 | `-1` | -1 | KH | ERR9 | TC-CPN-41 (đã có) | TC-CPN-82 dòng E (đã có) |
| LB-1 theo bước 0.01 | `-0.01` | -0.01 | KH | ERR9 | TC-CPN-112 | TC-CPN-130 dòng F |
| LB | `0` | 0 | H | OUT1 | TC-CPN-19 (đã có) | |
| LB+1 | `1` | 1 | H | OUT1; hiện `1 ₫` | TC-CPN-113 | |
| Giữa, UB-1, UB, UB+1 | Không áp dụng | | | | | Không có cận trên (A03 (iii)(b)) |
| Lớn nhất giao diện cho nhập (độ lớn) | `10000000000000000` | 10^16 | H | Như TC-CPN-18 | TC-CPN-21 (đã có) | |
| Lớn nhất giao diện cho nhập (độ chính xác) | `9007199254740993` | 2^53 + 1 | H | Như TC-CPN-111, với cột "Đơn tối thiểu" | TC-CPN-114 | |

Ghi chú: `-0.01` bắt trường hợp hệ thống cắt phần lẻ trước khi kiểm (cắt `-0.01` thành `0` rồi chấp nhận). Không cần `0.01` (LB+0.01): Mọi lỗi ở cận 0 đã lộ ra bằng `0` và `-0.01`.

### 3.4 P4: `max_uses_per_user`

| Điểm | Giá trị | Giá trị số | Loại | Kết quả mong đợi | Test case | Dự phòng API |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | | KH | ERR10 | TC-CPN-46 (đã có) | |
| Giá trị âm | `-1` | -1 | KH | ERR11 | TC-CPN-115 | TC-CPN-130 dòng G |
| LB-1 | `0` | 0 | KH | ERR11 | TC-CPN-44 (đã có) | TC-CPN-82 dòng F (đã có) |
| LB | `1` (gõ lại vào ô, không để giá trị mặc định) | 1 | H | OUT1; hiện `1 lần` | TC-CPN-116 | |
| LB+1 | `2` | 2 | H | OUT1; hiện `2 lần` | TC-CPN-117 | |
| LB, viết dạng thập phân | `1.0` | 1 | Theo A27 | (a) OUT2, lưu là 1; (b) ERR20 | TC-CPN-118 (qua API: `"max_uses_per_user": 1.0`) | |
| Giữa, UB-1, UB, UB+1 | Không áp dụng | | | | | Không có cận trên (A03 (iii)(b)) |
| Lớn nhất giao diện cho nhập (độ lớn) | `10000000000000000` | 10^16 | H | Như TC-CPN-18 | TC-CPN-25 (đã có) | |
| Lớn nhất giao diện cho nhập (độ chính xác) | `9007199254740993` | 2^53 + 1 | H | Như TC-CPN-111, với cột "Giới hạn/người" | TC-CPN-119 | |

Ghi chú: Không dùng `0.99` (ngay dưới LB theo bước 0.01): Vi phạm cùng lúc "nhỏ hơn 1" và "phải là số nguyên" (A03 (ii)(a)). Số lẻ đã có TC-CPN-45 (`1.5`).

### 3.5 P5: Độ dài `code` (sau khi cắt khoảng trắng đầu cuối)

Giá trị 1 và 2 ký tự không theo mẫu `FR17TCNN` vì chính độ dài là đối tượng test; các ký tự được chọn để không trùng mã mẫu và không trùng nhau.

| Điểm | Giá trị | Độ dài sau khi cắt | Loại | Kết quả mong đợi | Test case | Dự phòng API |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | 0 | KH | ERR1 | TC-CPN-30 (đã có) | |
| LB-1, biến thể khoảng trắng | `␣` (một dấu cách) | 0 | KH | ERR1 | TC-CPN-120 | |
| LB | `Q` | 1 | H | OUT1; cột "Mã" hiện `Q` | TC-CPN-121 | |
| LB, khoảng trắng hai bên | `␣K␣` | 1 | H | OUT1; cột "Mã" hiện `K`; K5: Tạo lại `K`, mong đợi ERR2 | TC-CPN-122 | |
| LB, chữ thường | `j` | 1 | H | OUT1; hiện `j` hoặc `J` đều đạt (A10) | TC-CPN-123 | |
| LB+1 | `QZ` | 2 | H | OUT1; hiện `QZ` | TC-CPN-124 | |
| Giữa, UB-1, UB, UB+1 | Không áp dụng | | | | | Không có cận trên (A04 độ dài (b)) |
| Thăm dò | `FR17TC12` + 247 chữ `X` | 255 | H | OUT1 đủ 255 ký tự, hoặc ERR22 | TC-CPN-12 (đã có) | |
| Lớn nhất giao diện cho nhập | `FR17TC125` + 991 chữ `X` | 1000 | H | Đạt nếu: OUT1 và cột "Mã" có đủ 1000 ký tự; hoặc bị từ chối có thông báo nói rõ `code` quá dài (ERR22). Sai nếu: Lưu bị cắt cụt, lỗi máy chủ. Ghi số ký tự ô nhận được | TC-CPN-125 | |

Ghi chú: `␣` (một dấu cách) khác TC-CPN-31 (`␣␣␣`) ở chỗ là đúng LB-1 sau khi cắt. Nếu ở S6 thấy ô giới hạn N ký tự, S5 bổ sung N-1, N, N+1.

### 3.6 P6: `expired_at` so với ngày chạy (ranh giới hiển thị)

Theo A05 (c), mọi ngày đều tạo được (OUT1); ranh giới chỉ ở cột "Hết hạn" (A18 (b)). Tạo và xem trong cùng ngày chạy; ghi ngày chạy.

| Điểm | Giá trị | Ngày so với ngày chạy | Loại | Kết quả mong đợi | Test case | Dự phòng API |
|---|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | `01/01/0001` | Rất xa trong quá khứ | H | OUT1; cột "Hết hạn" hiện chữ "Hết hạn". Ghi lại nếu ô chọn ngày không cho nhập năm này | TC-CPN-126 | |
| Hôm qua | Ngày chạy trừ 1 | -1 | H | OUT1; hiện chữ "Hết hạn" | TC-CPN-127 | |
| Hôm nay | Ngày chạy | 0 | H | OUT1; hiện chữ "Hết hạn" | TC-CPN-22 (đã có) | |
| Ngày mai | Ngày chạy cộng 1 | +1 | H | OUT1; cột "Hết hạn" hiện đúng ngày đó dạng `yyyy-mm-dd` | TC-CPN-128 | |
| Giữa | `12/31/2099` | Xa trong tương lai | H | OUT1; hiện `2099-12-31` | TC-CPN-01 (đã có) | |
| Lớn nhất giao diện cho nhập | `12/31/9999` | Lớn nhất ô cho chọn | H | OUT1; hiện `9999-12-31` | TC-CPN-129 | |

Ghi chú: Hôm qua, hôm nay, ngày mai là các điểm quanh ranh giới "không sau hôm nay"; nếu hệ thống hiện "Hết hạn" theo quy tắc khác (ví dụ chỉ khi trước hôm nay), ghi "khác giả định" (A18), không kết luận bug.

## 4. Test case API dự phòng (A2)

| Mã | Lớp phủ | Thao tác | Dữ liệu | Kết quả mong đợi | Yêu cầu |
|---|---|---|---|---|---|
| TC-CPN-130 | EC33, EC34, EC36, EC37, EC46, EC63 (điểm biên) | `POST /api/admin/coupons` | Dạng bảng, 7 dòng (bên dưới) | Theo từng dòng. **Chỉ chạy dòng nào** mà test case giao diện tương ứng bị trình duyệt chặn; dòng không chạy ghi "Không chạy, giao diện đã gửi được" | R07, R09, R10 |

| Dòng | Điểm | `code` | Thay đổi so với body cơ sở | Kết quả mong đợi | Chạy khi |
|---|---|---|---|---|---|
| A | P1 âm | `FR17TC130A` | `"discount_value": -1` | 4xx (ERR6) | TC-CPN-100 bị chặn |
| B | P1 LB bước 0.01 | `FR17TC130B` | `"discount_value": 0.01` | 2xx; `GET` có `0.01` | TC-CPN-101 bị chặn |
| C | P1 UB bước 0.01 | `FR17TC130C` | `"discount_value": 100.01` | 4xx (ERR17) | TC-CPN-105 bị chặn |
| D | P2 âm | `FR17TC130D` | `"type": "fixed"`, `"discount_value": -1` | 4xx (ERR6) | TC-CPN-107 bị chặn |
| E | P2 LB bước 0.01 | `FR17TC130E` | `"type": "fixed"`, `"discount_value": 0.01` | 2xx; `GET` có `0.01` | TC-CPN-108 bị chặn |
| F | P3 LB-1 bước 0.01 | `FR17TC130F` | `"min_order_amount": -0.01` | 4xx (ERR9) | TC-CPN-112 bị chặn |
| G | P4 âm | `FR17TC130G` | `"max_uses_per_user": -1` | 4xx (ERR11) | TC-CPN-115 bị chặn |

## 5. Tổng hợp

| Phân vùng | Test case mới | Dùng lại |
|---|---|---|
| P1 | TC-CPN-100 đến TC-CPN-106 (7) | TC-CPN-40, TC-CPN-38, TC-CPN-01, TC-CPN-14 |
| P2 | TC-CPN-107 đến TC-CPN-111 (5) | TC-CPN-40, TC-CPN-39, TC-CPN-18 |
| P3 | TC-CPN-112 đến TC-CPN-114 (3) | TC-CPN-42, TC-CPN-41, TC-CPN-19, TC-CPN-21 |
| P4 | TC-CPN-115 đến TC-CPN-119 (5) | TC-CPN-46, TC-CPN-44, TC-CPN-25 |
| P5 | TC-CPN-120 đến TC-CPN-125 (6) | TC-CPN-30, TC-CPN-12 |
| P6 | TC-CPN-126 đến TC-CPN-129 (4) | TC-CPN-22, TC-CPN-01 |
| API dự phòng | TC-CPN-130 (1, dạng bảng 7 dòng) | TC-CPN-82 dòng E, F |
| Tổng | 31 test case mới (29 qua giao diện, TC-CPN-118 qua API, TC-CPN-130 API dự phòng) | |

## 6. Truy vết

| Yêu cầu | Test case BVA | Ghi chú |
|---|---|---|
| FR17-R07 | TC-CPN-100 đến TC-CPN-111, TC-CPN-130 | P1, P2 |
| FR17-R09 | TC-CPN-112 đến TC-CPN-114, TC-CPN-130 | P3 |
| FR17-R10 | TC-CPN-115 đến TC-CPN-119, TC-CPN-130 | P4 |
| FR17-R04, FR17-R01 | TC-CPN-120 đến TC-CPN-125 | P5 |
| FR17-R08, FR17-R02 | TC-CPN-126 đến TC-CPN-129 | P6 |
| FR17-R03, R05, R06, R11 đến R19 | Không có | Không có phân vùng có thứ tự (xóa, tính duy nhất, tập giá trị, quyền, checklist) |

## 7. Điểm cần sinh viên quyết định

| # | Vấn đề | Các lựa chọn | Đề xuất của AI |
|---|---|---|---|
| 1 | Giả định mới A27: `max_uses_per_user` là `1.0` (số thập phân có giá trị nguyên) có hợp lệ không? A03 (ii)(a) chỉ nói "không nhận số thập phân" | (a) Hợp lệ, lưu là 1 (TC-CPN-118 thành H, OUT2); (b) Không hợp lệ (ERR20) | (a): Giá trị bằng đúng số nguyên 1; "số lần" chỉ cần là số đếm được |
| 2 | Ba điểm `2^53 + 1` (TC-CPN-111, TC-CPN-114, TC-CPN-119) | (a) Giữ cả ba; (b) Chỉ giữ cho `discount_value` loại `fixed` | (a): `10^16` ở TC-CPN-18, 21, 25 biểu diễn chính xác được nên không phát hiện lỗi mất độ chính xác; mỗi trường có thể được lưu theo kiểu khác nhau |
| 3 | Các điểm LB+1 (TC-CPN-103, TC-CPN-110, TC-CPN-113, TC-CPN-117, TC-CPN-124) | (a) Giữ theo slide; (b) Bỏ, chỉ giữ LB-1, LB | (a): Slide liệt kê LB+1; mỗi điểm chỉ một test case dữ liệu |
| 4 | Điểm âm của P1, P2, P4 (TC-CPN-100, TC-CPN-107, TC-CPN-115) không phải điểm biên theo slide | (a) Giữ làm đại diện theo rủi ro; (b) Bỏ, LB-1 là `0` đã đủ | (a): Bắt luật viết thành "khác 0" mà `0` không bắt được |
| 5 | Điểm `01/01/0001` (TC-CPN-126) | (a) Giữ; (b) Bỏ | (a): Là điểm "nhỏ nhất giao diện cho nhập" của slide; chi phí một test case |
| 6 | Điểm `␣` một dấu cách (TC-CPN-120) | (a) Giữ; (b) Bỏ, dùng TC-CPN-31 | (a): Là đúng LB-1 sau khi cắt, còn TC-CPN-31 là đại diện lớp |
| 7 | Kết quả khác giả định ở S6 | (a) Ghi trạng thái riêng "Khác giả định", xét ở S5 hoặc S7 trước khi mở bug; (b) Ghi là Fail | (a): Giả định do sinh viên chốt, không phải đặc tả |

## 8. Ghi chú cho bước sau

Cho S5:

- Nếu S6 thấy ô `code` giới hạn N ký tự, bổ sung N-1, N, N+1.
- TC-CPN-18, TC-CPN-21, TC-CPN-25 (`10^16`) chỉ kiểm độ lớn, không kiểm độ chính xác; độ chính xác do TC-CPN-111, TC-CPN-114, TC-CPN-119 kiểm. Cân nhắc ghi rõ điều này trong mục đích của các test case S3 đó.
- Xuất bằng `test-case-writing`: Các bảng giá trị biên dùng `format: "matrix"`, cột `covers` ghi phân vùng và điểm (ví dụ "P1 UB+1"); TC-CPN-130 giữ bảng dòng A đến G.

Cho S6:

- Thứ tự chạy: Các test case S4 tạo mã mới, không phá dữ liệu mẫu; chạy cùng nhóm "Thêm qua giao diện" (`03_tc.md` mục 9 bước 3). TC-CPN-127, TC-CPN-22, TC-CPN-128 phải tạo và xem trong cùng một ngày; ghi ngày chạy.
- TC-CPN-130 chỉ chạy các dòng có test case giao diện bị trình duyệt chặn.
