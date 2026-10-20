# S4: Phân tích giá trị biên

Theo Step 4 của slide S04: Chương trình dễ sai ở biên (bất đẳng thức viết nhầm, giá trị biên gõ nhầm). Với mỗi phân vùng **có thứ tự**, xét tối đa 9 điểm. Giá trị biên thường là "đại diện tốt nhất" của lớp.

**Đầu ra:** `ai_raw/S4_bva.md`, `04_bva.md`.

## Hỏi trước khi viết

- Độ dài dùng để thăm dò "giá trị lớn nhất giao diện cho nhập" khi chưa biết giới hạn thật (ví dụ khoảng 1000 ký tự).
- Biên nào cần chạy thêm qua API.

## 1. Chuẩn bị

1. Đọc mục **"Ghi chú cho bước sau"** của `02_ec.md` và `03_tc.md`. Mọi biến thể giá trị, cận đã hẹn cho S4 phải có trong bảng hoặc được ghi lý do không xét.
2. Liệt kê các phân vùng có thứ tự:

| Mã | Phân vùng | Cận dưới (LB) | Cận trên (UB) | Căn cứ |
|---|---|---|---|---|

Phân vùng có thứ tự: Độ dài, số lượng, giá trị số, ngày giờ, số lần. **Không** áp BVA cho định dạng, tập ký tự, tính duy nhất, so khớp bằng nhau: Những thứ đó không có thứ tự, đã đủ ở S2, S3. Giá trị "gần khớp" của phép so sánh bằng là đại diện theo rủi ro của một lớp không hợp lệ, không phải điểm biên.

## 2. Các điểm cần xét

| Điểm | Ý nghĩa |
|---|---|
| LB-1, LB, LB+1 | Quanh cận dưới |
| UB-1, UB, UB+1 | Quanh cận trên |
| Nhỏ nhất giao diện cho nhập | Thường là rỗng hoặc 1 ký tự |
| Lớn nhất giao diện cho nhập | Chưa biết khi thiết kế (không dùng DevTools); dùng chuỗi dài để thăm dò |
| Giữa | Một giá trị bên trong phân vùng hợp lệ |

**Không áp máy móc đủ 9 điểm.** Ghi rõ điểm nào không áp dụng và vì sao:

| Tình huống | Xử lý |
|---|---|
| Phân vùng không có cận trên | Không có UB-1, UB, UB+1 và **không có điểm "giữa"**; thay bằng điểm thăm dò "lớn nhất giao diện cho nhập". Không chọn một số tùy ý cho "giữa" |
| Điểm biên trùng giá trị của test case đã có | Dùng lại mã test case đó, không tạo mới |
| Giá trị tại biên buộc phải vi phạm thêm điều kiện khác (ví dụ mật khẩu 1 ký tự không thể đủ 4 loại ký tự) | Không dùng điểm đó; chọn **giá trị nhỏ nhất chỉ vi phạm đúng điều kiện đang xét**, ghi lý do |
| Giới hạn thật của ô chỉ biết khi chạy | Ở S6 ghi số ký tự ô thực sự nhận; nếu ô giới hạn N ký tự, bổ sung N-1, N, N+1 ở S5 |

## 3. Mỗi điểm chỉ vi phạm đúng một điều kiện

Giống S3: Giá trị tại mỗi điểm phải thỏa mọi điều kiện khác (ví dụ mật khẩu ở biên độ dài vẫn đủ các loại ký tự). Nếu không thể, xử lý như bảng trên.

## 4. Biên có liên quan tới chuẩn hóa và môi trường

- **Biến thể khoảng trắng tại biên:** Giá trị ở LB có khoảng trắng hai bên (sau khi cắt còn đúng LB ký tự); với trường không cắt khoảng trắng, giá trị chỉ đủ LB ký tự khi tính cả khoảng trắng, xét riêng khoảng trắng ở đầu và ở cuối.
- **Giá trị bị môi trường biến đổi trước khi tới hệ thống** (`platforms.md`): Tính biên trên **dạng sau biến đổi**. Ví dụ tên miền có dấu được chuyển sang punycode, nên giới hạn 63 ký tự mỗi nhãn tính trên dạng punycode; dùng công cụ chuẩn (ví dụ bộ mã hóa IDNA của Python) để tính, ghi rõ cách tính.
- **Biên mà trình duyệt hoặc nền tảng đã chuẩn hóa sẵn** (ví dụ ô `type="email"` tự cắt khoảng trắng): Qua giao diện, test case có thể trùng test case khác (một dấu cách thành chuỗi rỗng). Kiểm qua API, hoặc bỏ nếu nhóm API đã có test case tương đương.

## 5. Bảng giá trị biên

Mỗi phân vùng một bảng:

| Điểm | Giá trị | Độ dài hoặc giá trị số | Loại | Kết quả mong đợi | Test case |
|---|---|---|---|---|---|

- Cột "Test case": Mã mới, hoặc "mã cũ (đã có)".
- Giá trị dài ghi dạng "`x` + N chữ `a`", ghi độ dài.
- Kết quả mong đợi theo giả định đã chốt. Nếu hệ thống làm khác **giả định** (không phải khác đặc tả), ghi là "khác giả định", để sinh viên xét ở S5 hoặc S7 trước khi coi là bug.

## 6. Biên qua API

Biên quan trọng nhất mà giao diện có thể chặn trước (ví dụ ngay dưới cận dưới, ngay trên cận trên của luật định dạng): Thêm test case API, mỗi biên một test case.

## 7. Tổng hợp và truy vết

Bảng phân vùng, test case mới, test case dùng lại; tổng số mới theo đường thực thi; truy vết test case BVA về yêu cầu. Yêu cầu không có test case BVA: Ghi lý do. Kiểm bằng `check_step.py coverage` (truyền cả `03_tc.md` và `04_bva.md`).

## 8. Điểm cần sinh viên quyết định (gợi ý)

Độ dài thăm dò; giữ hay bỏ điểm vi phạm nhiều điều kiện; giữ hay bỏ phân vùng chỉ có LB, LB+1 (số lượng "ít nhất 1"); thêm biên qua API; cách xử lý khi kết quả khác giả định.
