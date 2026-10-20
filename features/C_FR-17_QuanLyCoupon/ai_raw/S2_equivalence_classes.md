# S2: Chia lớp tương đương (FR-17 Quản lý mã giảm giá)

- Bước: S2 (Chia lớp tương đương, Complete Set of Partitions, theo Step 2 của slide S04)
- Thời gian tạo: 2026-10-20 17:02 (UTC+07:00)
- Căn cứ: `00_spec.md` (mục 1 đến 4); `01_io.md` (toàn bộ, đặc biệt mục 9 đến 12); ảnh `screenshots/S0_03` đến `S0_06`; `Homeworks/eshop-sut/README.md` (FR-09, FR-12, FR-17, FR-22, FR-24); `Homeworks/eshop-sut/api_specification.md` (mục 1, 5, 6)
- Nguyên tắc sinh viên chốt trước khi viết:
  1. Khoảng trắng của `code` (A09): Cắt khoảng trắng đầu và cuối; chỉ gồm khoảng trắng tính như rỗng (ERR1); khoảng trắng ở giữa là ký tự bình thường, giữ nguyên.
  2. Hoa thường của `code` (A04 phần so trùng, A10): Không phân biệt hoa thường khi so trùng; hệ thống lưu, hiển thị chữ hoa hay giữ nguyên đều chấp nhận.
  3. Định dạng `expired_at` qua API (A13 phần định dạng): Chỉ dạng `yyyy-mm-dd` và phải là ngày có thật; định dạng khác, có kèm giờ, ngày không có thật bị từ chối (ERR15).

---

## 1. Cách làm

- Theo Step 2 của slide S04: Hai giá trị cùng lớp nếu kết quả mong đợi giống nhau. Áp các guideline: Khoảng giá trị có một cận thì 1 lớp hợp lệ và 1 lớp không hợp lệ; tập giá trị mà mỗi phần tử xử lý khác nhau thì mỗi phần tử một lớp cộng 1 lớp ngoài tập; điều kiện "must be" thì 1 lớp hợp lệ và 1 lớp không hợp lệ; tách lớp khi có lý do tin các phần tử được xử lý khác nhau (ghi ở cột cuối).
- Cột "Loại": `H` (hợp lệ), `KH` (không hợp lệ), `GĐ Ann` (phụ thuộc giả định chưa chốt). Loại xét theo điều kiện của chính dòng đó.
- Cột "Kết quả mong đợi" dùng mã Output, mã lỗi của `01_io.md`; lớp hợp lệ cho OUT1 (giao diện) hoặc OUT2 (API) khi mọi input khác cũng hợp lệ. Mã lỗi mới phát sinh từ giả định đánh số từ ERR17 (mục 4).
- Cột "Đường": `GD` (gửi được qua giao diện), `API` (chỉ gửi được qua API), `GD, API` (cả hai). Đường thực thi cụ thể chọn ở S3.
- Đại diện chỉ để minh họa; giá trị cụ thể chọn ở S3, S4. `␣` là một dấu cách.
- Mã yêu cầu viết tắt `Rnn` thay cho `FR17-Rnn`.
- Mã giả định trùng số câu hỏi mở gốc (`A01` ứng với `Q1`). Giả định mới phát sinh ở bước này: A25.

## 2. Lớp tương đương của Input

### 2.1 IN1: Mã giảm giá (`code`)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC01 | Bắt buộc | Có ít nhất 1 ký tự khác khoảng trắng | H | GD, API | `SUMMER26` | OUT1, OUT2 | R04 | Lớp cơ sở |
| EC02 | Bắt buộc | Rỗng (để trống; API không có trường `code`) | KH | GD, API | (trống) | ERR1 | R04 | |
| EC03 | Bắt buộc | Chỉ gồm khoảng trắng | KH | GD, API | `␣␣␣` | ERR1 (A09 đã chốt) | R04 | Bước chuẩn hóa là nhánh xử lý riêng: Sau khi cắt mới thành rỗng |
| EC04 | Khoảng trắng | Có khoảng trắng ở đầu | H | GD, API | `␣SUMMER26` | OUT1; lưu là `SUMMER26` (kiểm bằng K5) | R04, R05 | Bước cắt là nhánh riêng; có thể chỉ cắt một phía, nên tách đầu và cuối |
| EC05 | Khoảng trắng | Có khoảng trắng ở cuối | H | GD, API | `SUMMER26␣` | OUT1; lưu là `SUMMER26` (K5) | R04, R05 | Như EC04 |
| EC06 | Khoảng trắng | Có khoảng trắng ở giữa | H | GD, API | `SUM␣26` | OUT1; giữ nguyên khoảng trắng ở giữa (A09) | R01 | Hệ thống có thể có luật cấm hoặc chuẩn hóa khoảng trắng ở giữa mà đặc tả không nêu |
| EC07 | Hoa thường | Có chữ thường | H | GD, API | `summer26` | OUT1; hiển thị chữ hoa hay giữ nguyên đều chấp nhận (A10 đã chốt) | R01 | Có thể có bước chuyển chữ hoa (Q10) |
| EC08 | Tập ký tự | Chỉ chữ cái in hoa ASCII và chữ số, như mã mẫu | H | GD, API | `SUMMER26` | OUT1, OUT2 | R01 | Lớp cơ sở |
| EC09 | Tập ký tự | Chỉ gồm chữ số | H | GD, API | `007` | OUT1; hiển thị đúng `007` (OUT3) | R01, R15 | Chuỗi toàn chữ số có thể bị hiểu thành số và mất số 0 ở đầu |
| EC10 | Tập ký tự | Có dấu gạch ngang hoặc gạch dưới | GĐ A04 | GD, API | `TET-2027` | (a) OUT1; (b) ERR21; (c) OUT1 | R01 | Hệ thống có thể có luật ký tự mà đặc tả không nêu; `-`, `_` là dấu thường gặp trong mã |
| EC11 | Tập ký tự | Có chữ tiếng Việt có dấu hoặc ký tự Unicode khác | GĐ A04 | GD, API | `TẾT2027` | (a) OUT1, hiển thị đúng ký tự (OUT3); (b) ERR21; (c) ERR21 | R01, R15 | Ký tự ngoài ASCII có thể bị mã hóa, lưu, chuyển hoa khác |
| EC12 | Tập ký tự | Có ký tự đặc biệt của HTML | GĐ A04 | GD, API | `<b>X</b>` | (a) OUT1, bảng hiện đúng chuỗi `<b>X</b>` dạng chữ, không in đậm (OUT3); (b), (c) ERR21 | R15 | Rủi ro bảo mật: `code` được lưu và hiển thị lại trong bảng (SEC-04) |
| EC13 | Tập ký tự | Có ký tự đặc biệt của SQL | GĐ A04 | GD, API | `X'OR'1` | (a) OUT1, hiển thị nguyên văn, các mã khác không thay đổi; (b), (c) ERR21 | R16 | Rủi ro bảo mật (SEC-05); tách khỏi EC12 vì là một rủi ro khác, ở bước lưu chứ không ở bước hiển thị |
| EC14 | Độ dài | Rất dài | GĐ A04 | GD, API | `X` lặp 255 lần (255 ký tự) | (a) OUT1, lưu và hiển thị đủ 255 ký tự; (b) OUT1 như (a), hoặc ERR22 có thông báo rõ | R01 | Đặc tả không nêu độ dài tối đa; hệ thống lưu thường có giới hạn |
| EC15 | Duy nhất | Chưa có trong các mã đang có | H | GD, API | `SUMMER26` | OUT1, OUT2 | R05 | Lớp cơ sở |
| EC16 | Duy nhất | Trùng nguyên văn một mã mẫu | KH | GD, API | `SAVE10` | ERR2 | R05 | |
| EC17 | Duy nhất | Trùng nguyên văn một mã vừa tạo bằng chính chức năng | KH | GD, API | Tạo `SUMMER26` hai lần | ERR2 | R05 | Dữ liệu tạo theo hai đường khác nhau (dữ liệu mẫu, chức năng thêm) |
| EC18 | Duy nhất | Chỉ khác mã đang có ở hoa thường | KH | GD, API | `save10` | ERR2 (A10 đã chốt) | R05 | Phép so trùng có thể phân biệt hoa thường |
| EC19 | Duy nhất | Trùng mã đang có sau khi cắt khoảng trắng đầu cuối | KH | GD, API | `␣SAVE10` | ERR2 (A09 đã chốt) | R05 | Phép so trùng có thể chạy trước bước cắt |
| EC20 | Duy nhất | Trùng mã đã hết hạn | KH | GD, API | `EXPIRED` | ERR2 | R05 | Phép so trùng có thể chỉ xét mã còn hạn |
| EC21 | Duy nhất | Trùng mã đã bị xóa | GĐ A16 | GD, API | Xóa `SUMMER26` rồi tạo lại | (a) OUT1; (b) ERR2 | R05 | Xóa có thể chỉ là ẩn (xóa mềm), mã vẫn còn khi so trùng |
| EC22 | Kiểu dữ liệu | `null` hoặc chuỗi rỗng `""` | KH | API | `"code": null` | ERR1 (A14, cả hai phương án) | R04 | Giá trị rỗng của JSON có thể đi nhánh khác với trường vắng mặt |
| EC23 | Kiểu dữ liệu | Số JSON thay vì chuỗi | GĐ A14 | API | `"code": 2026` | (a) ERR15; (b) OUT2, lưu là `2026` | R04 | Kiểu dữ liệu khác chuỗi có thể làm lỗi bước cắt, so trùng |

### 2.2 IN2: Loại mã (`type`)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC24 | Tập giá trị | `percent` ("Phần trăm (%)") | H | GD, API | `percent` | OUT1, OUT2; cột "Loại" hiện là phần trăm, "Giá trị" có `%` | R06 | Tập giá trị mà mỗi phần tử xử lý khác nhau (công thức FR-09, cách hiển thị) |
| EC25 | Tập giá trị | `fixed` ("Số tiền cố định (₫)") | H | GD, API | `fixed` | OUT1, OUT2; cột "Giá trị" có `₫` | R06 | Như EC24 |
| EC26 | Bắt buộc | Thiếu trường `type` | KH | API | (không có trường) | ERR3 | R06 | Dropdown luôn có giá trị mặc định nên chỉ gửi được qua API |
| EC27 | Tập giá trị | Ngoài tập | KH | API | `free` | ERR4 | R06 | |
| EC28 | Tập giá trị | Khác hoa thường so với giá trị trong tập | GĐ A11 | API | `PERCENT` | (a) ERR4; (b) OUT2 | R06 | Phép so khớp có thể không phân biệt hoa thường |
| EC29 | Kiểu dữ liệu | `null` hoặc chuỗi rỗng `""` | KH | API | `"type": ""` | ERR3 (A14, cả hai phương án) | R06 | Như EC22 |

### 2.3 IN3: Giá trị giảm (`discount_value`)

Tách theo IN2 vì IN3 phụ thuộc IN2: Ý nghĩa khác (FR-09), có giới hạn trên riêng của `percent` (A01), có quan hệ riêng với IN4 khi là `fixed` (A12), và luật "dương" có thể được cài riêng trong từng nhánh loại.

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC30 | `percent`, khoảng giá trị | Số nguyên từ 1 đến 99 | H | GD, API | `15` | OUT1, OUT2 | R07 | Lớp cơ sở của `percent` |
| EC31 | `percent`, khoảng giá trị | Bằng 100 | GĐ A01 | GD, API | `100` | (a), (b) OUT1; (c) ERR17 | R07 | Giảm toàn bộ giá trị đơn: Có thể bị luật giới hạn trên xử lý riêng |
| EC32 | `percent`, khoảng giá trị | Lớn hơn 100 | GĐ A01 | GD, API | `150` | (a), (c) ERR17; (b) OUT1 | R07 | Theo công thức FR-09, `final_amount` sẽ âm |
| EC33 | `percent`, dương | Không dương (0 hoặc âm) | KH | GD, API | `0` | ERR6 | R07 | Luật "dương" có thể chỉ cài cho một nhánh loại, nên tách theo loại |
| EC34 | `percent`, số thập phân | Số thập phân dương | GĐ A02 | GD, API | `12.5` | (a), (b) OUT1, hiển thị đúng `12.5%`; (c) ERR18 | R07 | Số thập phân có thể bị làm tròn, cắt, từ chối |
| EC35 | `fixed`, khoảng giá trị | Số nguyên dương, không lớn hơn `min_order_amount` | H | GD, API | `50000` với `min_order_amount` là `300000` | OUT1, OUT2 | R07 | Lớp cơ sở của `fixed` |
| EC36 | `fixed`, dương | Không dương (0 hoặc âm) | KH | GD, API | `0` | ERR6 | R07 | Như EC33 |
| EC37 | `fixed`, số thập phân | Số thập phân dương | GĐ A02 | GD, API | `1000.5` | (a) OUT1, hiển thị đúng giá trị; (b), (c) ERR18 | R07 | Như EC34; đơn vị `₫` không có phần lẻ |
| EC38 | `fixed`, quan hệ với IN4 | Lớn hơn `min_order_amount` | GĐ A12 | GD, API | `500000` với `min_order_amount` là `300000` | (a) OUT1; (b) ERR24 | R07, R09 | Hệ thống có thể kiểm quan hệ giữa hai trường mà đặc tả không nêu |
| EC39 | `fixed`, giới hạn trên | Rất lớn | GĐ A25 | GD, API | `1` và 16 chữ số `0` (17 chữ số, lớn hơn 2^53) | (a) OUT1, lưu và hiển thị đúng giá trị; (b) OUT1 như (a), hoặc ERR22 có thông báo rõ | R07 | Số lớn có thể vượt khả năng biểu diễn chính xác của kiểu số (ví dụ số thực 64 bit của JSON trong JavaScript) |
| EC40 | Bắt buộc | Thiếu (để trống; API không có trường) | KH | GD, API | (trống) | ERR5 | R07 | |
| EC41 | Kiểu dữ liệu | Không phải số | KH | API | `abc` | ERR15 | R07 | Ô số của trình duyệt có thể chặn chữ, nên qua giao diện chỉ kiểm được trình duyệt |
| EC42 | Kiểu dữ liệu | Chuỗi chứa số | GĐ A14 | API | `"15"` | (a) ERR15; (b) OUT2 | R07 | Kiểu dữ liệu khác số có thể đi nhánh khác |
| EC43 | Kiểu dữ liệu | `null` hoặc chuỗi rỗng `""` | KH | API | `null` | ERR5 (A14, cả hai phương án) | R07 | Như EC22 |

### 2.4 IN4: Đơn tối thiểu (`min_order_amount`)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC44 | Khoảng giá trị (>= 0) | Số nguyên dương | H | GD, API | `300000` | OUT1, OUT2; hiển thị `300,000 ₫` | R09, R14 | Lớp cơ sở |
| EC45 | Khoảng giá trị (>= 0) | Bằng 0 | H | GD, API | `0` | OUT1, OUT2 | R09 | Giá trị 0 có thể bị hiểu nhầm là "không có giá trị" và báo thiếu (ERR8); 0 cũng là giá trị mặc định của ô |
| EC46 | Khoảng giá trị (>= 0) | Âm | KH | GD, API | `-1` | ERR9 | R09 | |
| EC47 | Số thập phân | Số thập phân dương | GĐ A03 | GD, API | `1000.5` | (a) OUT1, hiển thị đúng giá trị; (b) ERR19 | R09 | Như EC34 |
| EC48 | Giới hạn trên | Rất lớn | GĐ A03 | GD, API | `1` và 16 chữ số `0` | (a) OUT1, lưu và hiển thị đúng; (b) OUT1 như (a), hoặc ERR22 có thông báo rõ | R09 | Như EC39 |
| EC49 | Bắt buộc | Thiếu (tự xóa giá trị mặc định `0`; API không có trường) | KH | GD, API | (trống) | ERR8 | R09 | |
| EC50 | Kiểu dữ liệu | Không phải số | KH | API | `abc` | ERR15 | R09 | Như EC41 |
| EC51 | Kiểu dữ liệu | Chuỗi chứa số | GĐ A14 | API | `"300000"` | (a) ERR15; (b) OUT2 | R09 | Như EC42 |
| EC52 | Kiểu dữ liệu | `null` hoặc chuỗi rỗng `""` | KH | API | `null` | ERR8 (A14, cả hai phương án) | R09 | Như EC22 |

### 2.5 IN5: Ngày hết hạn (`expired_at`)

Điều kiện "thời điểm" xét theo IN10 (ngày chạy test).

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC53 | Thời điểm | Sau hôm nay | H | GD, API | `2099-12-31` | OUT1, OUT2; cột "Hết hạn" hiện đúng ngày đã nhập | R08 | Lớp cơ sở. Ngày hiển thị phải đúng ngày đã nhập (OUT1), kể cả khi máy chạy ở múi giờ khác (A13) |
| EC54 | Thời điểm | Đúng hôm nay | GĐ A05 | GD, API | Ngày chạy test | (a), (c) OUT1; (b) ERR23 | R08 | Theo FR-09 C2, mã hết hạn hôm nay đã không dùng được ngay khi tạo |
| EC55 | Thời điểm | Trước hôm nay | GĐ A05 | GD, API | `2025-01-31` | (a), (b) ERR23; (c) OUT1 | R08 | Lịch chọn ngày không làm mờ ngày quá khứ (ảnh `S0_06`), nên chọn được qua giao diện |
| EC56 | Bắt buộc | Thiếu (để trống; API không có trường) | KH | GD, API | (trống) | ERR7 | R08 | |
| EC57 | Lịch | Ngày 29 tháng 2 của năm nhuận | H | GD, API | `2028-02-29` | OUT1, OUT2 | R08 | Phép kiểm ngày có thật có thể sai với năm nhuận |
| EC58 | Định dạng | Khác dạng `yyyy-mm-dd` | KH | API | `12/31/2027` | ERR15 (A13 đã chốt) | R08 | Ô chọn ngày của trình duyệt chỉ gửi một định dạng, nên chỉ kiểm được qua API |
| EC59 | Định dạng | Đúng dạng nhưng không phải ngày có thật | KH | API | `2027-02-30` | ERR15 (A13 đã chốt) | R08 | Kiểm định dạng chuỗi có thể không kiểm lịch |
| EC60 | Định dạng | Có kèm giờ | KH | API | `2027-12-31T10:00:00Z` | ERR15 (A13 đã chốt) | R08 | Nhiều bộ phân tích ngày nhận được dạng này |
| EC61 | Kiểu dữ liệu | `null` hoặc chuỗi rỗng `""` | KH | API | `""` | ERR7 (A14, cả hai phương án) | R08 | Như EC22 |

### 2.6 IN6: Số lần dùng tối đa mỗi người (`max_uses_per_user`)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC62 | Khoảng giá trị (>= 1) | Số nguyên từ 1 trở lên | H | GD, API | `3` | OUT1, OUT2; hiển thị `3 lần` | R10 | Lớp cơ sở |
| EC63 | Khoảng giá trị (>= 1) | Nhỏ hơn 1 (0 hoặc âm) | KH | GD, API | `0` | ERR11 | R10 | Một cận nên một lớp không hợp lệ; S4 xét cả 0 và -1 (0 có thể bị hiểu nhầm là thiếu) |
| EC64 | Số thập phân | Số thập phân | GĐ A03 | GD, API | `1.5` | (a) ERR20; (b) OUT1 | R10 | Như EC34 |
| EC65 | Giới hạn trên | Rất lớn | GĐ A03 | GD, API | `1` và 16 chữ số `0` | (a) OUT1, lưu và hiển thị đúng; (b) OUT1 như (a), hoặc ERR22 có thông báo rõ | R10 | Như EC39 |
| EC66 | Bắt buộc | Thiếu (tự xóa giá trị mặc định `1`; API không có trường) | KH | GD, API | (trống) | ERR10 | R10 | |
| EC67 | Kiểu dữ liệu | Không phải số | KH | API | `abc` | ERR15 | R10 | Như EC41 |
| EC68 | Kiểu dữ liệu | Chuỗi chứa số | GĐ A14 | API | `"3"` | (a) ERR15; (b) OUT2 | R10 | Như EC42 |
| EC69 | Kiểu dữ liệu | `null` hoặc chuỗi rỗng `""` | KH | API | `null` | ERR10 (A14, cả hai phương án) | R10 | Như EC22 |

### 2.7 Thao tác Xóa: IN7 (mã cần xóa), IN13 (trạng thái của mã cần xóa), IN8 (hộp thoại)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC70 | Mã cần xóa | Mã mẫu còn hạn | H | GD, API | `BIGBUY` | OUT8, OUT9 | R03 | Lớp cơ sở |
| EC71 | Mã cần xóa | Mã vừa tạo bằng chính chức năng | H | GD, API | `SUMMER26` vừa tạo | OUT8, OUT9 | R03 | Dữ liệu tạo theo hai đường khác nhau |
| EC72 | Trạng thái (IN13 (ii)) | Mã đã hết hạn | H | GD, API | `EXPIRED` | OUT8, OUT9 | R03 | Dòng của mã hết hạn hiển thị khác (chữ "Hết hạn") nên có thể được dựng khác |
| EC73 | Mã cần xóa | `id` không tồn tại | GĐ A15 | API | `999999` | (a) ERR14; (b) ERR14 hoặc phản hồi thành công; cả hai phương án: Không mã nào bị xóa | R03 | |
| EC74 | Mã cần xóa | `id` không phải số | GĐ A15 | API | `abc` | Như EC73 | R03 | Bước đọc tham số đường dẫn có thể lỗi với chuỗi không phải số |
| EC75 | Trạng thái (IN13 (iii)) | `id` của mã đã bị xóa | GĐ A15 | API | `id` của `SUMMER26` sau khi xóa | Như EC73 | R03 | Xóa có thể chỉ là ẩn (xóa mềm) |
| EC76 | Trạng thái (IN13 (iii)) | Mã đã bị xóa ở tab khác, danh sách đang hiển thị chưa cập nhật | GĐ A24 | GD | Mở 2 tab, xóa ở tab 1, xóa lại ở tab 2 | (a) ERR14 hoặc danh sách tự cập nhật; không mã nào khác bị xóa | R03 | Cách duy nhất gặp ERR14 qua giao diện |
| EC77 | Trạng thái (IN13 (i)) | Mã đã được dùng trong đơn hàng | GĐ A16 | GD, API | Mã đã áp vào một đơn hàng | (a) OUT8; (b) ERR25; (c) Không lập lớp | R03 | Dữ liệu liên quan đơn hàng có thể ràng buộc việc xóa |
| EC78 | Hộp thoại (IN8) | Đồng ý | H | GD | Bấm nút đồng ý của hộp thoại | OUT8 | R03 | Chỉ có nếu giao diện có hộp thoại (A07) |
| EC79 | Hộp thoại (IN8) | Hủy | H | GD | Bấm nút hủy của hộp thoại | OUT10: Mã còn nguyên sau khi tải lại trang | R03 | Như EC78 |

### 2.8 Thao tác Xem: IN9 (các mã đang có), IN10 (ngày hiện tại)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC80 | Số mã đang có | Ít nhất 1 mã | H | GD, API | 4 mã mẫu | OUT5, OUT7 | R02 | Lớp cơ sở |
| EC81 | Số mã đang có | Không còn mã nào | H | GD, API | Xóa hết 4 mã mẫu | OUT6 (giao diện); OUT7 trả về danh sách rỗng (API) | R02, R18 | Trạng thái trống là nhánh hiển thị riêng (FR-24) |
| EC82 | Hạn của mã so với IN10 | `expired_at` sau hôm nay | H | GD | `2099-12-31` | OUT5, cột "Hết hạn" hiện ngày | R02 | Lớp cơ sở |
| EC83 | Hạn của mã so với IN10 | `expired_at` đúng hôm nay | GĐ A18 | GD | Mã tạo với ngày chạy test | (a) Hiện ngày; (b) Hiện "Hết hạn" | R02 | Ranh giới của quy tắc hiển thị; tạo được hay không phụ thuộc A05 |
| EC84 | Hạn của mã so với IN10 | `expired_at` trước hôm nay | GĐ A18 | GD | `EXPIRED` | (a), (b) Hiện "Hết hạn" | R02 | Chữ "Hết hạn" là hành vi quan sát ở S0, đặc tả không quy định |

### 2.9 IN11: Người gọi API (Thêm, Xem, Xóa)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC85 | Xác thực, quyền | Token của admin | H | API | Token từ `POST /api/login` với `admin@eshop.com` | OUT2, OUT7, OUT9 | R11 | Lớp cơ sở |
| EC86 | Xác thực | Không có header `Authorization` | KH | API | (không có header) | ERR12 | R11 | |
| EC87 | Xác thực | Header sai dạng | KH | API | `Authorization: <token admin>` (thiếu `Bearer`) | ERR12 | R11 | Bước tách header là nhánh riêng, có thể lấy nhầm token |
| EC88 | Xác thực | Token không hợp lệ | KH | API | `Authorization: Bearer abc.def.ghi` | ERR12 | R11 | |
| EC89 | Quyền | Token hợp lệ của user thường | KH | API | Token từ `POST /api/login` với `test@eshop.com` | ERR13 | R11 | SEC-03 là yêu cầu riêng: Kiểm `role`, không chỉ kiểm token tồn tại |

### 2.10 IN14: Dạng request API (Thêm)

| Mã | Điều kiện | Lớp | Loại | Đường | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC90 | Dạng request | Body JSON hợp lệ, `Content-Type: application/json` | H | API | Body như ví dụ mục 6.4 | OUT2 | R01 | Dạng chuẩn, dùng cho mọi test case API khác |
| EC91 | Dạng request | JSON sai cú pháp | GĐ A23 | API | `{"code": "X",` | (a) ERR16; (b) Không lập lớp | R01 | Bước đọc JSON là nhánh riêng, trước mọi bước kiểm trường |
| EC92 | Dạng request | Thiếu header `Content-Type` | GĐ A23 | API | Body đúng, không có header | (a) ERR16, hoặc bị từ chối như thiếu mọi trường; (b) Không lập lớp | R01 | Body có thể không được đọc |
| EC93 | Dạng request | `Content-Type` khác JSON | GĐ A23 | API | `Content-Type: text/plain`, body JSON đúng | Như EC92 | R01 | Như EC92 |
| EC94 | Dạng request | Không có body | GĐ A23 | API | (không có body) | Như EC92 | R01 | |
| EC95 | Dạng request | Body `{}` | KH | API | `{}` | ERR1, ERR3, ERR5, ERR7, ERR8, ERR10 cùng lúc | R04, R06 đến R10 | Ngoại lệ: Thiếu mọi trường bắt buộc nên vi phạm 6 lớp không hợp lệ cùng lúc |

## 3. Lớp tương đương của Output

Theo slide, mỗi Output và mỗi loại lỗi là một lớp. Các lớp ERR17 trở đi chỉ tồn tại nếu giả định tương ứng chọn phương án có lỗi đó.

| Mã | Output | Lớp Input dẫn tới | Ghi chú |
|---|---|---|---|
| EC96 | OUT1: Thêm thành công qua giao diện | Mọi lớp H của IN1 đến IN6 qua giao diện | Kiểm chứng bằng K1, K2 |
| EC97 | OUT2: Thêm thành công qua API | EC85, EC90 và lớp H của IN1 đến IN6 | Mã trạng thái theo A20 |
| EC98 | OUT3: Mã vừa tạo được hiển thị lại đúng | EC04 đến EC07, EC09, EC11 đến EC13 | Kiểm escape (R15) và dạng lưu (K5) |
| EC99 | OUT4: Thuộc tính của thông báo lỗi | Mọi lớp KH qua giao diện | Vị trí theo A21; nhiều lỗi, giữ dữ liệu theo A19 |
| EC100 | OUT5: Danh sách mã qua giao diện | EC80, EC82 đến EC84 | |
| EC101 | OUT6: Trang trống | EC81 | |
| EC102 | OUT7: Danh sách mã qua API | EC80, EC81 với EC85 | Trường trả về theo A17 |
| EC103 | OUT8: Xóa thành công qua giao diện | EC70 đến EC72, EC78 | Kiểm chứng bằng K7, K8 |
| EC104 | OUT9: Xóa thành công qua API | EC70 đến EC72 với EC85 | Cần `id` (A17) |
| EC105 | OUT10: Hủy ở hộp thoại, mã còn nguyên | EC79 | Chỉ có nếu có hộp thoại |
| EC106 | ERR1: Thiếu `code` | EC02, EC03, EC22, EC95 | |
| EC107 | ERR2: `code` trùng | EC16 đến EC20, EC21 (A16 (b)) | |
| EC108 | ERR3: Thiếu `type` | EC26, EC29, EC95 | |
| EC109 | ERR4: `type` ngoài tập | EC27, EC28 (A11 (a)) | |
| EC110 | ERR5: Thiếu `discount_value` | EC40, EC43, EC95 | |
| EC111 | ERR6: `discount_value` không dương | EC33, EC36 | |
| EC112 | ERR7: Thiếu `expired_at` | EC56, EC61, EC95 | |
| EC113 | ERR8: Thiếu `min_order_amount` | EC49, EC52, EC95 | |
| EC114 | ERR9: `min_order_amount` âm | EC46 | |
| EC115 | ERR10: Thiếu `max_uses_per_user` | EC66, EC69, EC95 | |
| EC116 | ERR11: `max_uses_per_user` nhỏ hơn 1 | EC63 | |
| EC117 | ERR12: Chưa xác thực | EC86 đến EC88 | |
| EC118 | ERR13: Không đủ quyền | EC89 | |
| EC119 | ERR14: Xóa mã không tồn tại | EC73 đến EC76 | Theo A15, A24 |
| EC120 | ERR15: Sai kiểu hoặc sai định dạng | EC23 (A14 (a)), EC41, EC42 (A14 (a)), EC50, EC51 (A14 (a)), EC58 đến EC60, EC67, EC68 (A14 (a)) | |
| EC121 | ERR16: Request không đọc được | EC91 đến EC94 (A23 (a)) | |
| EC122 | ERR17: `percent` vượt giới hạn trên | EC31 (A01 (c)), EC32 (A01 (a), (c)) | Mã lỗi mới, phụ thuộc A01 |
| EC123 | ERR18: `discount_value` không phải số nguyên | EC34 (A02 (c)), EC37 (A02 (b), (c)) | Mã lỗi mới, phụ thuộc A02 |
| EC124 | ERR19: `min_order_amount` không phải số nguyên | EC47 (A03 (i)(b)) | Mã lỗi mới, phụ thuộc A03 |
| EC125 | ERR20: `max_uses_per_user` không phải số nguyên | EC64 (A03 (ii)(a)) | Mã lỗi mới, phụ thuộc A03 |
| EC126 | ERR21: `code` có ký tự không được phép | EC10 đến EC13 (A04 (b), (c)) | Mã lỗi mới, phụ thuộc A04 |
| EC127 | ERR22: Vượt giới hạn mà đặc tả không nêu (độ dài `code`, độ lớn trường số) | EC14, EC39, EC48, EC65 (phương án (b) của A04, A25, A03) | Mã lỗi mới; thông báo phải chỉ ra trường bị vượt |
| EC128 | ERR23: `expired_at` không còn hiệu lực khi tạo | EC54 (A05 (b)), EC55 (A05 (a), (b)) | Mã lỗi mới, phụ thuộc A05 |
| EC129 | ERR24: `fixed` lớn hơn `min_order_amount` | EC38 (A12 (b)) | Mã lỗi mới, phụ thuộc A12 |
| EC130 | ERR25: Không xóa được mã đã dùng trong đơn hàng | EC77 (A16 (i)(b)) | Mã lỗi mới, phụ thuộc A16 |

## 4. Giả định

### 4.1 Đã chốt hoặc đã đóng

| Mã | Câu hỏi gốc | Trạng thái |
|---|---|---|
| A04 (phần so trùng) | Q4: Có phân biệt hoa thường khi kiểm tra trùng không? | Chốt trước khi viết: Không phân biệt (EC18) |
| A06 | Q6: Admin có sửa được mã không? | Đã đóng ở S1: Không có thao tác sửa |
| A08 | Q8: Trường `is_active` | Đã đóng ở S1 (quyết định 4): Không mô hình hóa, ghi giới hạn quan sát |
| A09 | Q9: Khoảng trắng của `code` | Chốt trước khi viết: Cắt đầu cuối; chỉ khoảng trắng như rỗng; giữa giữ nguyên (EC03 đến EC06, EC19) |
| A10 | Q10: `code` có tự chuyển chữ hoa không | Chốt trước khi viết: Lưu, hiển thị chữ hoa hay giữ nguyên đều chấp nhận (EC07) |
| A13 | Q13: Định dạng `expired_at` qua API; múi giờ | Chốt trước khi viết: Chỉ `yyyy-mm-dd`, ngày có thật (EC57 đến EC60). Phần múi giờ không cần giả định riêng: Ngày hiển thị phải đúng ngày đã nhập, theo OUT1 ("các cột khớp với giá trị đã nhập") |

### 4.2 Chờ sinh viên chốt

Cột "Nhận xét của AI" là đề xuất theo yêu cầu của sinh viên, không phải quyết định. Mỗi phương án nêu lớp nào thành H hoặc KH.

| Mã | Câu hỏi gốc | Phương án | Lớp bị ảnh hưởng | Chữ đặc tả | Nhận xét của AI |
|---|---|---|---|---|---|
| A01 | Q1: `percent` có giới hạn trên không? | (a) Tối đa 100: EC31 H, EC32 KH (ERR17); (b) Không có giới hạn trên: EC31, EC32 H; (c) Phải nhỏ hơn 100: EC31, EC32 KH (ERR17) | EC31, EC32 | FR-17: "`discount_value` (dương)"; FR-09: "`discount_amount = total × discount_value / 100`" | Đề xuất (a): Trên 100% thì `final_amount` âm theo chính công thức FR-09; 100% vẫn có nghĩa (miễn phí) |
| A02 | Q2: `discount_value` có nhận số thập phân không? | (a) Nhận cho cả hai loại: EC34, EC37 H; (b) Chỉ `percent` nhận: EC34 H, EC37 KH (ERR18); (c) Không nhận: EC34, EC37 KH (ERR18) | EC34, EC37 | FR-17: "(dương)" | Đề xuất (a): Đặc tả chỉ yêu cầu dương; cấm số thập phân là tự đặt thêm luật |
| A03 | Q3: `min_order_amount`, `max_uses_per_user` có nhận số thập phân, có giới hạn trên không? | (i) `min_order_amount` thập phân: (a) Nhận, EC47 H; (b) Không nhận, EC47 KH (ERR19). (ii) `max_uses_per_user` thập phân: (a) Không nhận, EC64 KH (ERR20); (b) Nhận, EC64 H. (iii) Giới hạn trên: (a) Không có, EC48, EC65 phải được nhận và lưu đúng; (b) Hệ thống được có giới hạn, EC48, EC65 bị từ chối có thông báo rõ (ERR22) cũng đúng; chỉ sai khi lưu sai giá trị hoặc lỗi máy chủ | EC47, EC48, EC64, EC65 | FR-17: "`min_order_amount` (>= 0), `max_uses_per_user` (>= 1)"; FR-09 C5: "Số lần đã dùng mã này của user < `max_uses_per_user`" | Đề xuất (i)(a): Đặc tả không cấm. (ii)(a): "Số lần" là đại lượng đếm, C5 so với số lần đã dùng là số nguyên. (iii)(b): Đặc tả không nêu giới hạn nhưng mọi hệ thống có giới hạn lưu; lỗi thật là lưu sai hoặc lỗi máy chủ |
| A04 | Q4 (phần còn lại): Độ dài, ký tự cho phép của `code` | Ký tự: (a) Mọi ký tự in được đều hợp lệ: EC10 đến EC13 H; (b) Chỉ chữ cái ASCII và chữ số: EC10 đến EC13 KH (ERR21); (c) Chữ cái ASCII, chữ số, `-`, `_`: EC10 H, EC11 đến EC13 KH (ERR21). Độ dài: (a) Không giới hạn: EC14 phải được nhận đủ; (b) Hệ thống được có giới hạn: EC14 bị từ chối có thông báo rõ (ERR22) cũng đúng; sai khi lưu bị cắt cụt hoặc lỗi máy chủ | EC10 đến EC14 | FR-17: "`code` (duy nhất)"; ví dụ API "`TET2025`", mã mẫu đều là chữ hoa và số | Đề xuất ký tự (a): Ví dụ không phải luật; độ dài (b): Như A03 (iii). Hệ quả của ký tự (b), (c): R15, R16 chỉ còn kiểm được việc từ chối, không kiểm được escape khi hiển thị |
| A05 | Q5: `expired_at` được là ngày quá khứ, hôm nay không? | (a) Quá khứ bị từ chối, hôm nay hợp lệ: EC54 H, EC55 KH (ERR23); (b) Quá khứ và hôm nay bị từ chối: EC54, EC55 KH (ERR23); (c) Mọi ngày đều hợp lệ: EC54, EC55 H | EC54, EC55; EC83, EC84 (tạo dữ liệu) | FR-17: "`expired_at`" (chỉ bắt buộc); FR-09 C2: "Ngày hiện tại phải trước `expired_at`"; ví dụ API mục 6.4: `"2025-01-31"`; dữ liệu mẫu có `EXPIRED` hạn 2020-01-01 | Đề xuất (c): Đặc tả không cấm; FR-09 C2 đã chặn mã hết hạn lúc dùng. Nếu chọn (a) hoặc (b), EC84 chỉ còn dùng được mã mẫu `EXPIRED`, còn EC83 không tạo được dữ liệu ở (b) |
| A07 | Q7: Xóa mã có hộp thoại xác nhận không? | (a) Bắt buộc có hộp thoại: Không có hộp thoại là khác biệt so với giả định; (b) Không bắt buộc: Xóa ngay là đúng; nếu có hộp thoại thì xét EC78, EC79 | EC78, EC79 | FR-24: "Khi xóa item khỏi giỏ phải có dialog xác nhận" (chỉ nói giỏ hàng) | Đề xuất (b): FR-24 chỉ áp cho giỏ hàng, không mở rộng sang màn hình khác |
| A11 | Q11: `type` khác hoa thường (`PERCENT`) | (a) Không hợp lệ: EC28 KH (ERR4); (b) Hợp lệ: EC28 H | EC28 | FR-17: "`type` (percent/fixed)" | Đề xuất (a): Đặc tả ghi đúng hai giá trị kỹ thuật viết thường |
| A12 | Q12: `fixed` được lớn hơn `min_order_amount` không? | (a) Được: EC38 H; (b) Không được: EC38 KH (ERR24). Hệ quả của (b): Mã `fixed` với `min_order_amount` là 0 (giá trị mặc định) luôn bị từ chối | EC38; EC35 (chọn đại diện) | FR-17 không có ràng buộc giữa hai trường; mã mẫu `BIGBUY` 50,000 ₫ với ngưỡng 500,000 ₫, `VIP100` 100,000 ₫ với ngưỡng 300,000 ₫ | Đề xuất (a): Đặc tả không có ràng buộc; trường hợp `final_amount` âm là việc của FR-09 khi áp mã |
| A14 | Q14: Kiểu dữ liệu qua API | (a) Chặt: `null`, `""` tính như thiếu; chuỗi chứa số ở trường số và số JSON ở `code` là sai kiểu (ERR15): EC23, EC42, EC51, EC68 KH; (b) Dễ: `null`, `""` tính như thiếu; chuỗi chứa số được hiểu là số, số JSON ở `code` được hiểu là chuỗi: EC23, EC42, EC51, EC68 H. Cả hai: EC22, EC29, EC43, EC52, EC61, EC69 KH (lỗi thiếu); trường lạ (ví dụ `is_active`) không lập lớp vì không quan sát được tác động (quyết định 4 của S1) | EC22, EC23, EC29, EC42, EC43, EC51, EC52, EC61, EC68, EC69 | API spec mục 6.4: Ví dụ dùng số cho trường số, chuỗi cho `code`, không quy định kiểu | Đề xuất (b): Đặc tả chỉ cho ví dụ, không quy định kiểu; chuỗi chứa số mang đúng giá trị nên từ chối không có căn cứ |
| A15 | Q15: Xóa `id` không tồn tại, không phải số, đã bị xóa | (a) Bị từ chối, báo mã không tồn tại (ERR14); (b) Từ chối hoặc phản hồi thành công đều chấp nhận. Cả hai: Không mã nào bị xóa, không lỗi máy chủ | EC73 đến EC75 | Không có | Đề xuất (b): Cả hai cách đều phổ biến với thao tác xóa; điều cần kiểm là không xóa nhầm |
| A16 | Q16: Xóa mã đã dùng trong đơn hàng; tạo lại mã đã xóa | (i) Mã đã dùng: (a) Xóa được (OUT8); (b) Không xóa được (ERR25); (c) Không lập lớp, ghi rủi ro. (ii) Tạo lại mã đã xóa: (a) Được (EC21 H, OUT1); (b) Không được (EC21 KH, ERR2) | EC21, EC77; K8 | FR-17: "`code` (duy nhất)" | Đề xuất (i)(c): Tạo dữ liệu phải đặt hàng (FR-09) và đặc tả không nói kết quả. (ii)(a): "Duy nhất" xét với các mã đang có; mã đã xóa không còn |
| A17 | Q17: `GET /api/coupons` trả về những trường nào? | (a) Mong đợi mỗi mã có đủ 6 trường đã nhập và `id`; thiếu `id` thì test case xóa qua API ghi Blocked; (b) Không đặt mong đợi; dùng `id` nếu có | EC80 đến EC81 (OUT7); EC70 đến EC75 (đường API) | API spec mục 5.2: Chỉ có endpoint và header; mục 6.4: Xóa dùng `:id` | Đề xuất (a): Xóa qua API cần `:id`, và chỉ API dành cho admin này có thể cung cấp `id` |
| A18 | Q18: Quy tắc hiện chữ "Hết hạn" | (a) "Hết hạn" khi `expired_at` trước hôm nay: EC83 hiện ngày; (b) "Hết hạn" khi `expired_at` không sau hôm nay: EC83 hiện "Hết hạn". Cả hai: EC84 hiện "Hết hạn", EC82 hiện ngày | EC82 đến EC84 | FR-09 C2: "Ngày hiện tại phải trước `expired_at`" | Đề xuất (b): Khớp với C2, mã có `expired_at` là hôm nay đã không dùng được |
| A19 | Q19: Phản hồi giao diện sau khi tạo, khi bị từ chối | (a) Mong đợi tối thiểu: Thành công là có dòng mới; thông báo thành công, xóa form, vị trí dòng mới không bắt buộc; bị từ chối là có thông báo chỉ ra nguyên nhân; hiện tất cả lỗi hay lỗi đầu tiên, giữ dữ liệu hay không đều chấp nhận, ghi lại hành vi ở S6; (b) Mong đợi chặt: Có thông báo thành công, form được xóa, dữ liệu được giữ khi lỗi, hiện tất cả lỗi | EC96, EC99 | FR-22: "Thông báo lỗi phải xuất hiện **trên** nút submit" | Đề xuất (a): Đặc tả không yêu cầu các hành vi ở (b) |
| A20 | Q20: Mã trạng thái HTTP | (a) Chỉ kiểm theo nhóm: Thành công là 2xx, bị từ chối là 4xx, không phải 5xx (RFC 9110 mục 15), ghi mã thực tế ở S6; (b) Kiểm mã cụ thể theo thông lệ REST (201, 400, 401, 403, 404, 409); (c) Không kiểm mã, chỉ kiểm tác động bằng K1 đến K8 | Mọi lớp đường API | API spec mục 1.1, 1.2, 1.3: "200 OK"; mục 5, 6.4 không ghi | Đề xuất (a): Có chuẩn làm căn cứ mà không đặt thêm luật; (b) còn khác "200 OK" mà mục 1.1 dùng cho thao tác tạo |
| A21 | Q21: Bong bóng thông báo của trình duyệt có tính là thông báo lỗi theo FR-22 không | (a) Không tính: Phải có thông báo của chính trang ở trên nút "Tạo mã"; (b) Tính, không xét vị trí; (c) Tính, và vẫn xét vị trí phải ở trên nút "Tạo mã" | EC99 | FR-22: "Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới." | Đề xuất (c): Đặc tả không phân biệt nguồn của thông báo, chỉ quy định vị trí |
| A22 | Q22: Đường dẫn API theo FR-12 hay API spec | (a) Chỉ theo API spec; ghi khác biệt tài liệu; (b) Theo API spec cho mọi lớp, cộng thêm test case gọi `POST /api/coupons` và `DELETE /api/coupons/:id` theo FR-12 với EC86, EC89: Mong đợi không tạo, không xóa được mã | EC85 đến EC89 (đường thực thi) | FR-12: "`POST/PUT/DELETE /api/products`, `/api/categories`, `/api/coupons`"; API spec mục 6.4: `/api/admin/coupons` | Đề xuất (b): FR-12 nêu đích danh đường này trong yêu cầu bảo mật; chỉ tốn vài test case |
| A23 | Q23: Request không đọc được thành JSON | (a) Bị từ chối (ERR16), không tạo mã, không lỗi máy chủ; với EC92 đến EC94, bị từ chối như thiếu mọi trường cũng chấp nhận: EC91 đến EC94 KH; (b) Không lập lớp IN14 ngoài EC90, EC95 | EC91 đến EC94 | API spec mục 6.4: "**Body (JSON):**" | Đề xuất (a): Mong đợi "không tạo mã, không lỗi máy chủ" kiểm chứng được mà không cần biết hệ thống phân loại lỗi thế nào |
| A24 | Q24: Xóa qua giao diện một mã đã bị xóa ở tab khác | (a) Giao diện báo lỗi hoặc tự cập nhật danh sách (cả hai chấp nhận); không mã nào khác bị xóa: EC76 KH; (b) Không lập lớp | EC76 | Không có | Đề xuất (a): Đây là cách duy nhất kiểm ERR14 qua giao diện |
| A25 | Mới: `discount_value` loại `fixed` có giới hạn trên không? (Q1 chỉ hỏi cho `percent`) | (a) Không có: EC39 phải được nhận và lưu đúng; (b) Hệ thống được có giới hạn: EC39 bị từ chối có thông báo rõ (ERR22) cũng đúng; chỉ sai khi lưu sai giá trị hoặc lỗi máy chủ | EC39 | FR-17: "(dương)" | Đề xuất (b): Như A03 (iii) |

## 5. Dữ liệu có rủi ro bảo mật

| Trường | Ký tự HTML, SQL có đi tới bước lưu không | Kiểm được trong FR-17 không |
|---|---|---|
| `code` | Có, nếu A04 ký tự chọn (a): EC12, EC13 được lưu | Có: Bảng danh sách hiển thị lại `code` (EC12, R15). R16 chỉ quan sát gián tiếp: Mã được lưu nguyên văn và các mã khác không thay đổi |
| `code` | Không, nếu A04 ký tự chọn (b) hoặc (c): Bị từ chối (ERR21) | Chỉ kiểm được việc từ chối; escape khi hiển thị không còn kiểm được qua `code` |
| `discount_value`, `min_order_amount`, `max_uses_per_user` | Không: Chuỗi chứa ký tự HTML, SQL không phải số nên bị từ chối (ERR15, EC41, EC50, EC67) | Ô số của giao diện có thể chặn trước; chỉ kiểm qua API |
| `expired_at` | Không: Sai định dạng `yyyy-mm-dd` nên bị từ chối (ERR15, EC58, A13 đã chốt) | Chỉ qua API |
| `type` | Không: Ngoài tập nên bị từ chối (ERR4, EC27) | Chỉ qua API |

Giới hạn quan sát: `code` còn được hiển thị ở các màn hình của feature khác (ví dụ thanh toán); việc escape ở đó không thuộc FR-17.

## 6. Tổng hợp

Đếm bằng `check_step.py classes`.

| Biến | H | KH | GĐ |
|---|---|---|---|
| IN1 `code` (EC01 đến EC23) | 8 | 8 | 7 |
| IN2 `type` (EC24 đến EC29) | 2 | 3 | 1 |
| IN3 `discount_value` (EC30 đến EC43) | 2 | 5 | 7 |
| IN4 `min_order_amount` (EC44 đến EC52) | 2 | 4 | 3 |
| IN5 `expired_at` (EC53 đến EC61) | 2 | 5 | 2 |
| IN6 `max_uses_per_user` (EC62 đến EC69) | 1 | 4 | 3 |
| Xóa: IN7, IN8, IN13 (EC70 đến EC79) | 5 | 0 | 5 |
| Xem: IN9, IN10 (EC80 đến EC84) | 3 | 0 | 2 |
| IN11 người gọi (EC85 đến EC89) | 1 | 4 | 0 |
| IN14 dạng request (EC90 đến EC95) | 1 | 1 | 4 |
| Tổng lớp Input (EC01 đến EC95) | 27 | 34 | 34 |
| Output (EC96 đến EC130) | | | 35 lớp Output |
| Tổng cộng | | | 130 lớp |

## 7. Điểm cần sinh viên quyết định

| # | Vấn đề | Các lựa chọn | Đề xuất của AI |
|---|---|---|---|
| 1 | Chốt các giả định ở mục 4.2 | Mỗi giả định chọn một phương án | Theo cột "Nhận xét của AI" |
| 2 | Tách lớp "không dương" của IN3 theo loại (EC33, EC36) | (a) Tách theo loại; (b) Gộp thành một lớp | (a): Luật "dương" có thể chỉ cài trong một nhánh loại; tách chỉ thêm một test case |
| 3 | Lớp "bằng 0" của IN4 (EC45) | (a) Giữ lớp riêng; (b) Gộp vào EC44, để S4 xét 0 là cận dưới | (a): 0 là giá trị mặc định của ô và dễ bị hiểu nhầm là thiếu, khác các số dương |
| 4 | ERR22 dùng chung cho mọi giới hạn không có trong đặc tả | (a) Một loại lỗi chung, thông báo phải chỉ ra trường; (b) Mỗi trường một loại lỗi | (a): Quyết định 1 của S1 tách theo nguyên nhân đặc tả nêu; giới hạn này đặc tả không nêu nên không cần tách |
| 5 | Lớp body `{}` (EC95) vi phạm 6 lớp cùng lúc | (a) Giữ làm ngoại lệ, ghi rõ ở S3; (b) Bỏ | (a): Là trường hợp hay gặp khi gọi API sai, và kiểm được hệ thống báo đủ hay chỉ một lỗi |
| 6 | Lớp kiểu dữ liệu của `code` (EC22, EC23) | (a) Giữ; (b) Bỏ, chỉ xét `code` là chuỗi | (a): Bước cắt khoảng trắng và so trùng có thể lỗi khi nhận kiểu khác chuỗi |

## 8. Ghi chú cho bước sau

Cho S3:

- Lớp cơ sở để gộp vào test case hợp lệ: EC01, EC08, EC15, EC24 hoặc EC25, EC30 hoặc EC35, EC44, EC53, EC62 (thêm EC85, EC90 với đường API). Các lớp hợp lệ bất thường (EC04 đến EC07, EC09, EC45, EC57 và lớp GĐ nào thành H) mỗi lớp một test case riêng.
- Mỗi test case không hợp lệ chỉ vi phạm một lớp KH. Ngoại lệ đã biết: EC95 (body `{}`).
- Lớp chỉ gửi được qua API (cột "Đường" là `API`): EC22, EC23, EC26 đến EC29, EC41 đến EC43, EC50 đến EC52, EC58 đến EC61, EC67 đến EC69, EC73 đến EC75, EC85 đến EC95. Với IN11 (EC85 đến EC89), xét cho cả ba thao tác Thêm, Xem, Xóa; nếu A22 chọn (b) thì thêm test case theo đường của FR-12.
- Môi trường (`platforms.md`): Ô số có thể chặn chữ, cho gõ `e`, `-`, và với số thập phân có thể hiện bong bóng của trình duyệt theo bước nhảy; nếu vậy lớp thập phân (EC34, EC37, EC47, EC64) và lớp âm (EC46, EC63) qua giao diện chỉ kiểm trình duyệt, nên thêm test case qua API. Ô chọn ngày cho chọn ngày quá khứ (ảnh `S0_06`).
- Thứ tự chạy: EC81 (xóa hết mã) và các test case xóa mã mẫu (EC70, EC72) chạy cuối, reset dữ liệu ngay sau đó; EC17, EC21, EC71, EC75 cần tạo dữ liệu trước trong cùng test case.
- Kiểm chứng: K1, K2 cho lớp H; K3, K4 cho lớp KH; K5 cho EC04, EC05, EC07, EC19; K7, K8 cho xóa (K8 theo A16 (ii)).
- Mã trạng thái API theo A20; trường của `GET /api/coupons` theo A17.
- Dữ liệu test cần một mẫu `code` thống nhất theo test case (chốt ở S3).

Cho S4 (phân vùng có thứ tự):

- IN3 `percent`: Cận dưới "> 0" (điểm nhỏ nhất hợp lệ là 1 nếu chỉ số nguyên, hoặc số thập phân nhỏ như `0.01` nếu A02 cho phép); cận trên 100 theo A01.
- IN3 `fixed`: Cận dưới "> 0" như trên; không có cận trên trong đặc tả (A25), chỉ thăm dò giá trị lớn nhất cho nhập; nếu A12 (b) thì có cận trên tương đối là `min_order_amount` (xét bằng, lớn hơn 1).
- IN4: Cận dưới 0 (0 hợp lệ, -1 không hợp lệ); không có cận trên (A03 (iii)).
- IN6: Cận dưới 1 (1 hợp lệ, 0 và -1 không hợp lệ); không có cận trên (A03 (iii)).
- IN5: Cận tương đối theo ngày chạy: Hôm qua, hôm nay, ngày mai (A05); ngày lớn nhất ô chọn ngày cho chọn (ví dụ `9999-12-31`); ghi ngày chạy ở S6.
- IN1 độ dài: Cận dưới 1 ký tự sau khi cắt; không có cận trên (A04 độ dài). Biến thể tại biên: 1 ký tự có khoảng trắng hai bên (`␣A␣`), 1 ký tự là chữ thường.
- Số lớn: Xét quanh 2^53 (`9007199254740992`) cho các trường số, vì có thể mất độ chính xác khi lưu hoặc hiển thị.
- Không có điểm "giữa" cho phân vùng không có cận trên.
