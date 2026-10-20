# S1: Xác định biến Input và Output (FR-17 Quản lý mã giảm giá)

- Bước: S1 (Xác định biến Input và Output, theo Step 1 của slide S04)
- Thời gian tạo: 2026-10-20 16:03 (UTC+07:00)
- Căn cứ: `00_spec.md` (mục 1 đến 4); ảnh `screenshots/S0_01` đến `S0_07`; `Homeworks/eshop-sut/README.md` (FR-09, FR-12, FR-17, FR-21 đến FR-24, mục 9); `Homeworks/eshop-sut/api_specification.md` (mục 5, 6.4)
- Quyết định sinh viên chốt trước khi viết:
  1. Các điểm S0 còn thiếu được nêu ngay trong bản này: Câu hỏi mới đánh số tiếp từ Q9, yêu cầu chưa có trong `00_spec.md` ghi là "đề xuất bổ sung".
  2. Quyền truy cập: Ở giao diện là tiền điều kiện chung (đăng nhập admin); ở nhóm API là biến Input "người gọi".
  3. Phạm vi: Thêm là miền chính; Xóa có biến riêng (mã cần xóa); Xem là Output, cộng biến gián tiếp "các mã đang có".

---

## 1. Cách làm

- Theo Step 1 của slide S04: Input là mọi thứ ảnh hưởng tới kết quả, gồm cả yếu tố không nhập trực tiếp (dữ liệu có sẵn, thời điểm, người thao tác). Output là mọi kết quả quan sát được, gồm cả thông báo lỗi.
- Bước này chỉ xác định **biến** và **ràng buộc đặc tả đặt lên biến**; chưa chia lớp. Ràng buộc nào đặc tả không nêu thì trỏ về câu hỏi mở `Qnn` để S2 đặt giả định.
- Mã dùng trong file: `INn` (Input), `OUTn` (Output), `ERRn` (loại lỗi theo nguyên nhân), `PCn` (tiền điều kiện chung), `Kn` (cách kiểm chứng tác động). Câu hỏi của `00_spec.md` giữ nguyên mã `Q1` đến `Q8`; câu hỏi mới đánh số `Q9` trở đi.
- Form "Tạo mã giảm giá mới" **không có nhãn** (`00_spec.md` mục 4.3), nên cột "Tên trên giao diện" ghi placeholder hoặc nội dung hiển thị, kèm dòng tương ứng ở mục 4.3.
- Kết quả sinh viên nhập thử ở S0 không được cung cấp. Với Q1 đến Q4 và Q7, bản này chỉ dùng phần giao diện mà `00_spec.md` cho phép và coi hành vi là chưa biết.

## 2. Tiền điều kiện chung và đường thực thi

| Mã | Tiền điều kiện | Căn cứ |
|---|---|---|
| PC1 | Thao tác qua giao diện: Đã đăng nhập Web Admin `http://localhost:5174` bằng tài khoản admin mặc định `admin@eshop.com` / `Admin123!`, mở trang bằng menu "Mã Giảm Giá" | README mục 1; `00_spec.md` mục 4.1; quyết định 2 |
| PC2 | Dữ liệu ở trạng thái mẫu (4 mã `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`) trước mỗi đợt test | `00_spec.md` mục 4.2; `WORKFLOW.md` mục 3.3 |

Hai đường thực thi, chọn cho từng test case ở S3:

| Đường | Thêm | Xem | Xóa |
|---|---|---|---|
| Giao diện | Form "Tạo mã giảm giá mới", nút "Tạo mã" | Bảng danh sách trên trang "Quản lý Mã Giảm Giá" | Nút "Xóa" ở cột "Hành động" |
| API | `POST /api/admin/coupons` | `GET /api/coupons` | `DELETE /api/admin/coupons/:id` |

Đường dẫn API lấy theo API spec. FR-12 lại ghi `POST/PUT/DELETE /api/coupons`, không khớp với API spec (Q22).

## 3. Biến Input

### 3.1 Thao tác Thêm: Input nhập trực tiếp

| Mã | Biến | Tên trên giao diện | Trường API tương ứng | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|
| IN1 | Mã giảm giá | Ô chữ, placeholder "Mã coupon (VD: SAVE10)", mặc định trống (mục 4.3 dòng 1) | `code` | Bắt buộc; duy nhất so với các mã đang có (IN9). Độ dài, ký tự cho phép, phân biệt hoa thường khi so trùng: Không nêu (Q4). Khoảng trắng đầu, cuối, giữa, chỉ khoảng trắng: Không nêu (Q9). Có tự chuyển chữ hoa khi lưu không: Không nêu (Q10). Hiển thị lại phải được escape (SEC-04); truy vấn không được nối chuỗi (SEC-05) | FR17-R01, R04, R05, R15, R16 (đề xuất) |
| IN2 | Loại mã | Dropdown, 2 lựa chọn "Phần trăm (%)" và "Số tiền cố định (₫)", mặc định "Phần trăm (%)" (mục 4.3 dòng 2, ảnh `S0_05`) | `type` | Bắt buộc; chỉ nhận `percent` hoặc `fixed`. Trên giao diện chỉ chọn được 2 giá trị trong tập và không thấy lựa chọn rỗng; giá trị ngoài tập, rỗng, khác hoa thường (ví dụ `PERCENT`) chỉ gửi được qua API, cách xử lý không nêu (Q11) | FR17-R01, R06 |
| IN3 | Giá trị giảm | Ô số, placeholder "Giá trị % (VD: 10)", mặc định trống (mục 4.3 dòng 3) | `discount_value` | Bắt buộc; dương (> 0). Ý nghĩa phụ thuộc IN2 theo FR-09: `percent` là phần trăm của tổng đơn, `fixed` là số tiền. Giới hạn trên của loại `percent`: Không nêu (Q1). Số thập phân: Không nêu (Q2). Loại `fixed` có được lớn hơn IN4 không: Không nêu (Q12) | FR17-R01, R07 |
| IN4 | Đơn tối thiểu | Ô số, placeholder "Đơn tối thiểu (₫)", mặc định `0` (mục 4.3 dòng 4) | `min_order_amount` | Bắt buộc; >= 0. Số thập phân, giới hạn trên: Không nêu (Q3) | FR17-R01, R09 |
| IN5 | Ngày hết hạn | Ô chọn ngày, hiển thị `mm/dd/yyyy`, mặc định trống; lịch không làm mờ các ngày trước hôm nay (mục 4.3 dòng 5, ảnh `S0_06`) | `expired_at` | Bắt buộc. Được là ngày quá khứ hoặc hôm nay không: Không nêu (Q5). Qua API: Ví dụ trong API spec có dạng `"2025-01-31"`; định dạng khác, ngày không tồn tại, có kèm giờ: Không nêu (Q13) | FR17-R01, R08 |
| IN6 | Số lần dùng tối đa mỗi người | Ô số, placeholder "Số lần dùng tối đa/người", mặc định `1` (mục 4.3 dòng 6) | `max_uses_per_user` | Bắt buộc; >= 1. Số thập phân, giới hạn trên: Không nêu (Q3) | FR17-R01, R10 |

Ghi chú:

- IN4 và IN6 có giá trị mặc định, nên muốn để trống thì phải tự xóa giá trị đó (ảnh `S0_04` cho thấy xóa được).
- Ngoài giá trị của từng trường, qua API còn có thể gửi body thiếu hẳn một trường, giá trị `null`, chuỗi rỗng, sai kiểu (chuỗi `"15"` thay cho số `15`, chữ ở trường số), hoặc thêm trường lạ như `is_active`. Đặc tả không nêu cách xử lý (Q14).
- `00_spec.md` ghi IN3, IN4, IN6 là "ô số" và IN5 là ô chọn ngày. Theo hiểu biết chung về trình duyệt (`platforms.md`), ô số có thể chặn chữ hoặc cho gõ `e`, `-`, và ô ngày chỉ cho chọn ngày có thật. Khi đó một số giá trị chỉ gửi được qua API; việc này sẽ xét ở S2.

### 3.2 Thao tác Xóa: Input nhập trực tiếp

| Mã | Biến | Tên trên giao diện | Trường API tương ứng | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|
| IN7 | Mã cần xóa | Nút "Xóa" trên dòng của mã, cột "Hành động" (mục 4.4, ảnh `S0_07_nut_thao_tac_xoa`) | `:id` trong `DELETE /api/admin/coupons/:id` | Đặc tả chỉ nêu "Admin có thể ... Xóa". Trên giao diện chỉ xóa được mã đang hiển thị. Qua API có thể gửi `id` không tồn tại, đã bị xóa, không phải số: Không nêu (Q15). `id` lấy từ đâu: API spec không mô tả phản hồi của `GET /api/coupons` (Q17). Xóa mã đã được dùng trong đơn hàng: Không nêu (Q16) | FR17-R03 |
| IN8 | Lựa chọn ở hộp thoại xác nhận xóa (ứng viên) | Chưa biết có hộp thoại hay không | Không có trong API spec | Chỉ tồn tại nếu giao diện có hộp thoại xác nhận (Q7). FR-24 chỉ yêu cầu hộp thoại khi xóa sản phẩm khỏi giỏ hàng, không nói về mã giảm giá | FR17-R03 |

### 3.3 Input không nhập trực tiếp

| Mã | Biến | Ảnh hưởng tới | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|
| IN9 | Các mã đang có trong hệ thống: 4 mã mẫu, mã do test case trước tạo ra, mã đã bị xóa | Tính duy nhất của IN1; IN7 có tồn tại không; nội dung danh sách (OUT5); khi không còn mã nào thì hiện trang trống (OUT6) | `code` duy nhất (FR-17). Mã đã xóa có còn tính là "đã có" khi so trùng không: Không nêu (Q16) | FR17-R02, R03, R05, R18 (đề xuất) |
| IN10 | Ngày hiện tại lúc chạy test | IN5 là quá khứ, hôm nay hay tương lai (Q5); mã có hiện chữ "Hết hạn" trong danh sách không (Q18) | FR-17 không có ràng buộc. FR-09 C2 ("Ngày hiện tại phải trước `expired_at`") là điều kiện **dùng** mã, không phải điều kiện **tạo** mã | FR17-R02, R08 |
| IN11 | Người gọi API (chỉ dùng ở nhóm API, quyết định 2): Không gửi token; token không hợp lệ; token của user thường (`test@eshop.com`); token của admin | Có được thêm, xem, xóa mã không | FR-12: Phải có JWT hợp lệ **và** `role = 'admin'`. SEC-02: Phải có JWT hợp lệ. SEC-03: Phải kiểm tra `role`, không chỉ kiểm sự tồn tại của token. API spec mục 5.2 ghi `GET /api/coupons` "Dành cho Admin" và cần header `Authorization` | FR17-R11 |
| IN12 | Múi giờ, ngôn ngữ của máy chạy test (ứng viên) | Cách ô ngày hiển thị và nhận ngày (`mm/dd/yyyy` theo ngôn ngữ máy); ngày lưu có thể lệch một ngày nếu có chuyển múi giờ | Không có trong đặc tả (Q13) | FR17-R08 |

### 3.4 Sự kiện kích hoạt

Không phải biến, không chia lớp.

| Thao tác | Giao diện | API |
|---|---|---|
| Thêm | Bấm nút "Tạo mã" | Gửi `POST /api/admin/coupons` |
| Xem | Mở trang qua menu "Mã Giảm Giá"; tải lại trang | Gửi `GET /api/coupons` |
| Xóa | Bấm nút "Xóa" trên dòng của mã (và chọn ở hộp thoại nếu có) | Gửi `DELETE /api/admin/coupons/:id` |

## 4. Biến Output

### 4.1 Thành công

| Mã | Output | Khi nào xảy ra | Dấu hiệu quan sát được | Yêu cầu |
|---|---|---|---|---|
| OUT1 | Thêm thành công qua giao diện | IN1 đến IN6 đều hợp lệ, IN1 chưa có trong IN9 | Bảng danh sách của chính trang này có thêm một dòng với `code` vừa nhập; các cột khớp với giá trị đã nhập. Dòng vẫn còn sau khi tải lại trang (K1). Thông báo thành công, form có được xóa trắng không, vị trí dòng mới trong bảng: Đặc tả không nêu (Q19) | FR17-R01, R02 |
| OUT2 | Thêm thành công qua API | Như OUT1, gửi qua API với token admin | API spec không nêu mã trạng thái và thân phản hồi (Q20). Tối thiểu: Phản hồi không phải lỗi, và mã mới có trong `GET /api/coupons` hoặc trong bảng trên giao diện | FR17-R01 |
| OUT3 | Cách mã vừa tạo được hiển thị lại | Sau OUT1 hoặc OUT2 | `code` hiện đúng nguyên văn dưới dạng chữ, không bị trình duyệt hiểu thành HTML (SEC-04). Có tự chuyển chữ hoa không, có cắt khoảng trắng không: Không nêu (Q9, Q10). Số thập phân có bị làm tròn khi hiển thị không: Không nêu (Q2, Q3) | FR17-R15 |
| OUT5 | Danh sách mã (Xem) qua giao diện | Mở trang hoặc tải lại trang khi có ít nhất 1 mã | Mỗi mã một dòng, gồm các cột "Mã", "Loại", "Giá trị", "Đơn tối thiểu", "Hết hạn", "Giới hạn/người", "Hành động" (mục 4.1). Đặc tả chỉ yêu cầu tiền có `₫` và phân cách hàng nghìn (FR-21); cách hiển thị khác quan sát ở S0 (ngày `yyyy-mm-dd`, chữ "Hết hạn", "n lần") chỉ dùng làm mẫu đối chiếu. Quy tắc hiện chữ "Hết hạn": Không nêu (Q18) | FR17-R02, R14 |
| OUT6 | Trang trống | IN9 không còn mã nào | Có icon hoặc hình minh họa và message thân thiện (FR-24) | FR17-R18 (đề xuất) |
| OUT7 | Danh sách mã qua API | `GET /api/coupons` với token admin | API spec không mô tả phản hồi (Q17, Q20) | FR17-R02 |
| OUT8 | Xóa thành công qua giao diện | Bấm "Xóa" trên một mã đang có (và xác nhận nếu có hộp thoại) | Dòng của mã biến mất khỏi bảng và vẫn không có sau khi tải lại trang (K7) | FR17-R03 |
| OUT9 | Xóa thành công qua API | `DELETE` với `id` của một mã đang có, token admin | API spec không nêu mã trạng thái (Q20). Tối thiểu: Phản hồi không phải lỗi, mã không còn trong danh sách | FR17-R03 |
| OUT10 | Hộp thoại xác nhận xóa (ứng viên) | Bấm "Xóa", nếu giao diện có hộp thoại (Q7) | Hộp thoại hiện ra; chọn hủy thì mã còn nguyên trong bảng | FR17-R03 |

Mã `OUT4` dùng cho thuộc tính của thông báo lỗi (mục 4.3).

### 4.2 Bị từ chối: Loại lỗi theo nguyên nhân

Đặc tả không nêu câu chữ thông báo nào, nên kết quả mong đợi của mọi loại lỗi chỉ ghi nguyên nhân, không ghi câu chữ: **Không tạo (hoặc không xóa) mã** (kiểm chứng theo mục 5), và có thông báo cho biết nguyên nhân (thuộc tính ở OUT4).

| Mã | Nguyên nhân | Biến | Căn cứ đặc tả | Yêu cầu |
|---|---|---|---|---|
| ERR1 | Thiếu `code` | IN1 | FR-17: Trường bắt buộc | FR17-R04 |
| ERR2 | `code` trùng với mã đang có | IN1, IN9 | FR-17: `code` (duy nhất) | FR17-R05 |
| ERR3 | Thiếu `type` (chỉ gửi được qua API) | IN2 | FR-17: Trường bắt buộc | FR17-R06 |
| ERR4 | `type` không phải `percent` hoặc `fixed` (chỉ gửi được qua API) | IN2 | FR-17: `type` (percent/fixed) | FR17-R06 |
| ERR5 | Thiếu `discount_value` | IN3 | FR-17: Trường bắt buộc | FR17-R07 |
| ERR6 | `discount_value` không dương (0 hoặc âm) | IN3 | FR-17: `discount_value` (dương) | FR17-R07 |
| ERR7 | Thiếu `expired_at` | IN5 | FR-17: Trường bắt buộc | FR17-R08 |
| ERR8 | Thiếu `min_order_amount` | IN4 | FR-17: Trường bắt buộc | FR17-R09 |
| ERR9 | `min_order_amount` âm | IN4 | FR-17: `min_order_amount` (>= 0) | FR17-R09 |
| ERR10 | Thiếu `max_uses_per_user` | IN6 | FR-17: Trường bắt buộc | FR17-R10 |
| ERR11 | `max_uses_per_user` nhỏ hơn 1 | IN6 | FR-17: `max_uses_per_user` (>= 1) | FR17-R10 |
| ERR12 | Chưa xác thực: Không có token hoặc token không hợp lệ | IN11 | FR-12 điều 1; SEC-02 | FR17-R11 |
| ERR13 | Không đủ quyền: Token hợp lệ nhưng không phải `role = 'admin'` | IN11 | FR-12 điều 2; SEC-03 | FR17-R11 |
| ERR14 | Xóa mã không tồn tại (chỉ gửi được qua API) | IN7, IN9 | Không có trong đặc tả (Q15) | FR17-R03 |
| ERR15 | Giá trị sai kiểu hoặc sai định dạng (chữ ở trường số, ngày không tồn tại, sai định dạng ngày) (ứng viên) | IN3 đến IN6 | Không có trong đặc tả (Q13, Q14) | FR17-R07 đến R10 |

Các loại lỗi chỉ phát sinh khi sinh viên chọn giả định ở S2 (ví dụ `percent` lớn hơn 100 bị từ chối theo Q1, ngày quá khứ bị từ chối theo Q5, số thập phân bị từ chối theo Q2, Q3) sẽ được thêm mã `ERR16` trở đi ở S2, không tạo trước ở đây.

### 4.3 Thuộc tính của thông báo lỗi

| Mã | Thuộc tính | Đặc tả nói gì | Yêu cầu |
|---|---|---|---|
| OUT4 | Vị trí | Phải ở **trên** nút submit, tức nút "Tạo mã" (FR-22). Nếu thông báo là bong bóng kiểm tra ô của chính trình duyệt thì có tính là thông báo lỗi theo FR-22 không: Không nêu (Q21) | FR17-R13 |
| OUT4 | Ngôn ngữ | Tiếng Việt (FR-21) | FR17-R14 |
| OUT4 | Nội dung | Không nêu câu chữ; mong đợi tối thiểu là chỉ ra được trường hoặc nguyên nhân | Không có |
| OUT4 | Nhiều lỗi cùng lúc | Không nêu: Hiện tất cả hay chỉ lỗi đầu tiên (Q19) | Không có |
| OUT4 | Dữ liệu đã nhập có được giữ lại khi bị từ chối | Không nêu (Q19) | Không có |
| OUT4 | Phản hồi API khi thất bại | Không nêu mã trạng thái, thân phản hồi; không nêu có phân biệt ERR12 và ERR13 bằng mã trạng thái khác nhau không (Q20) | FR17-R11 |

## 5. Cách kiểm chứng tác động

Kết quả "thành công" chỉ chứng minh hệ thống chấp nhận. Các cách dưới đây kiểm chứng dữ liệu thật sự được tạo, lưu hoặc xóa, và chỉ dùng chính màn hình, API của FR-17, trừ K9.

| Mã | Tác động cần kiểm chứng | Cách | Phụ thuộc, giới hạn |
|---|---|---|---|
| K1 | Mã đã được tạo, lưu đúng giá trị | Tải lại trang, dòng mới vẫn có và các cột khớp giá trị đã nhập | Chỉ thấy dạng hiển thị (ví dụ tiền đã định dạng), không thấy giá trị lưu thật |
| K2 | Mã đã được tạo (khóa duy nhất) | Tạo lại với cùng `code`, mong đợi ERR2 | Cần ERR2 hoạt động đúng; nếu ERR2 lỗi thì K2 không kết luận được |
| K3 | Mã chưa được tạo khi bị từ chối | Tải lại trang, không có dòng mới | |
| K4 | Mã chưa được tạo khi bị từ chối (khóa duy nhất) | Tạo lại cùng `code` với dữ liệu hợp lệ, mong đợi OUT1 | Không dùng được cho ERR2 (mã vốn đã có) |
| K5 | Dạng lưu của `code` (đã cắt khoảng trắng, đã chuyển chữ hoa) | Xem cột "Mã"; tạo lại với dạng đã chuẩn hóa, mong đợi ERR2 | Phụ thuộc giả định về so trùng hoa thường và khoảng trắng (Q4, Q9, Q10) |
| K6 | Giá trị số lưu đúng (thập phân, làm tròn) | Xem cột tương ứng trong bảng; hoặc xem phản hồi `GET /api/coupons` | Bảng có thể làm tròn khi hiển thị; phản hồi API chưa được mô tả (Q17) |
| K7 | Mã đã bị xóa | Tải lại trang, dòng không còn; `GET /api/coupons` không còn mã | |
| K8 | Mã đã bị xóa (khóa duy nhất) | Tạo lại cùng `code`, mong đợi OUT1 | Phụ thuộc Q16 (mã đã xóa có còn tính khi so trùng không) |
| K9 | Mã mới đang hoạt động (`is_active = 1`) và dùng được | Gọi `POST /api/apply-coupon` với `code` vừa tạo | Phụ thuộc FR-09 (feature khác): Nếu lỗi thì không rõ lỗi thuộc FR-17 hay FR-09. Liên quan Q8 |

Dữ liệu: Mỗi test case tạo mã dùng một `code` riêng theo một mẫu thống nhất (chốt ở S3), để K2, K4, K8 không bị ảnh hưởng bởi test case khác.

## 6. Yêu cầu không mô hình hóa thành biến

Các yêu cầu dưới đây là thuộc tính tĩnh của màn hình, không có miền giá trị để chia lớp. Đề xuất kiểm tra thành nhóm checklist riêng, ngoài Domain Testing.

| Yêu cầu | Nội dung kiểm | Quan sát S0 (`00_spec.md`) |
|---|---|---|
| FR17-R12 | Trường bắt buộc có dấu `*` | Không trường nào có dấu `*`, form không có nhãn |
| FR17-R14 | Giao diện tiếng Việt; nút tích cực màu xanh dương, nút nguy hiểm màu đỏ; tiền có `₫` và phân cách hàng nghìn | Nút "Tạo mã" màu cam, nút "Xóa" màu đỏ; tiền dạng `300,000 ₫`; lịch chọn ngày có chữ tiếng Anh ("October", "Clear", "Today") |
| FR17-R17 (đề xuất) | Menu "Mã Giảm Giá" được highlight khi đang ở trang này (FR-23) | Ảnh `S0_03`: Mục "Mã Giảm Giá" có màu chữ khác các mục còn lại |
| FR17-R19 (đề xuất) | Trang có đúng 1 thẻ `<h1>` (FR-21); kiểm ở S6 bằng DevTools vì đặc tả yêu cầu | Chưa quan sát (không dùng DevTools ở S0 đến S5) |
| Không có mã | Placeholder ô "Giá trị" có đổi theo loại không | `00_spec.md` mục 4.4 đã ghi là điểm đối chiếu ở S6 |

Ghi chú: FR17-R13 (vị trí thông báo lỗi) không đưa vào checklist mà kiểm kèm các test case không hợp lệ qua giao diện, vì chỉ thấy được khi có lỗi (OUT4).

## 7. Yêu cầu đề xuất bổ sung và câu hỏi mới

### 7.1 Yêu cầu đề xuất bổ sung

Các đoạn đặc tả dưới đây áp cho màn hình này nhưng chưa có trong danh sách yêu cầu của `00_spec.md` mục 2. Mã đánh tiếp từ R16, chờ sinh viên nhận hay bỏ.

| Mã | Yêu cầu | Nguồn (trích nguyên văn) |
|---|---|---|
| FR17-R16 (đề xuất) | Dữ liệu nhập (ví dụ `code`) không làm thay đổi truy vấn CSDL: Chuỗi có ký tự đặc biệt kiểu SQL được xử lý như dữ liệu bình thường | SEC-05: "Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp." |
| FR17-R17 (đề xuất) | Menu "Mã Giảm Giá" được highlight khi đang ở trang này | FR-23: "Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn." |
| FR17-R18 (đề xuất) | Khi không còn mã nào, danh sách hiện trang trống có icon hoặc hình minh họa và message thân thiện | FR-24: "Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện." |
| FR17-R19 (đề xuất) | Trang có đúng 1 thẻ `<h1>` | FR-21: "**Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang." (đã trích ở `00_spec.md` mục 1.4 nhưng chưa có trong danh sách yêu cầu) |

Lưu ý về R16: Kiểm thử hộp đen chỉ quan sát được gián tiếp (mã được lưu, hiển thị nguyên văn, các mã khác không bị ảnh hưởng); không chứng minh được hệ thống thật sự dùng Parameterized Query.

### 7.2 Câu hỏi mới

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q9 | `code` có khoảng trắng ở đầu, cuối, giữa, hoặc chỉ gồm khoảng trắng thì hệ thống cắt, từ chối hay giữ nguyên? | IN1, FR17-R04, R05 | Chạy thử S6 |
| Q10 | `code` có tự chuyển thành chữ hoa khi lưu không, hay chữ hoa trong bảng chỉ là cách hiển thị? (4 mã mẫu vốn đã viết hoa nên ảnh S0 không cho biết) | IN1, OUT3 | Chạy thử S6 |
| Q11 | Qua API, `type` rỗng, ngoài tập, hoặc khác hoa thường (`PERCENT`) thì xử lý thế nào? | IN2, ERR3, ERR4 | Chạy thử S6 |
| Q12 | Loại `fixed` có được có `discount_value` lớn hơn `min_order_amount` không? Theo công thức FR-09, khi đó `final_amount` có thể âm | IN3, IN4 | Không có trong đặc tả |
| Q13 | Qua API, `expired_at` nhận những định dạng nào? Ngày không tồn tại (ví dụ `2026-02-30`), có kèm giờ thì sao? Ngày có bị lệch do múi giờ khi lưu và hiển thị không? | IN5, IN12, ERR15 | Chạy thử S6 |
| Q14 | Qua API, body thiếu hẳn một trường, có giá trị `null`, chuỗi rỗng, sai kiểu (chuỗi `"15"`, chữ ở trường số), hoặc có trường lạ (ví dụ `is_active`) thì xử lý thế nào? | IN1 đến IN6, ERR15 | Chạy thử S6 |
| Q15 | Xóa qua API với `id` không tồn tại, đã bị xóa, hoặc không phải số thì phản hồi thế nào? | IN7, ERR14 | Chạy thử S6 |
| Q16 | Xóa mã đã được dùng trong đơn hàng thì sao? Sau khi xóa, có tạo lại được mã cùng `code` không? | IN7, IN9, K8 | Không có trong đặc tả |
| Q17 | `GET /api/coupons` trả về những trường nào (cần `id` để xóa qua API và để kiểm chứng giá trị lưu)? | IN7, OUT7, K6 | Chạy thử S6 |
| Q18 | Danh sách hiện chữ "Hết hạn" thay cho ngày theo quy tắc nào? Mã có `expired_at` đúng bằng hôm nay hiện ngày hay "Hết hạn"? (FR-09 C2 ghi "Ngày hiện tại phải **trước** `expired_at`") | IN5, IN10, OUT5 | Chạy thử S6 |
| Q19 | Sau khi tạo thành công: Có thông báo không, form có được xóa trắng không, dòng mới nằm ở đâu trong bảng? Khi bị từ chối: Dữ liệu đã nhập có được giữ lại không, nhiều lỗi cùng lúc thì hiện tất cả hay chỉ lỗi đầu tiên? | OUT1, OUT4 | Chạy thử S6 |
| Q20 | Phản hồi API (mã trạng thái, thân phản hồi) khi thành công và thất bại của `POST`, `DELETE`, `GET` là gì? ERR12 và ERR13 có trả về mã trạng thái khác nhau không? | OUT2, OUT7, OUT9, OUT4, ERR12, ERR13 | Không có trong đặc tả |
| Q21 | Nếu trình duyệt chặn gửi form và hiện bong bóng thông báo của chính nó, thì có tính là "thông báo lỗi" theo FR-22 (phải ở trên nút submit) không? | OUT4, FR17-R13 | Không có trong đặc tả |
| Q22 | FR-12 ghi `POST/PUT/DELETE /api/coupons`, API spec ghi `POST /api/admin/coupons` và `DELETE /api/admin/coupons/:id`. Test theo đường dẫn nào, hay cả hai? | Mục 2, IN11 | Không có trong đặc tả |

## 8. Đối chiếu yêu cầu với biến

| Yêu cầu | Input | Output |
|---|---|---|
| FR17-R01 | IN1 đến IN6 | OUT1, OUT2 |
| FR17-R02 | IN9, IN10 | OUT5, OUT7 |
| FR17-R03 | IN7, IN8, IN9 | OUT8, OUT9, OUT10, ERR14 |
| FR17-R04 | IN1 | ERR1 |
| FR17-R05 | IN1, IN9 | ERR2 |
| FR17-R06 | IN2 | ERR3, ERR4 |
| FR17-R07 | IN3 | ERR5, ERR6 |
| FR17-R08 | IN5, IN10, IN12 | ERR7 |
| FR17-R09 | IN4 | ERR8, ERR9 |
| FR17-R10 | IN6 | ERR10, ERR11 |
| FR17-R11 | IN11 (nhóm API); PC1 (giao diện) | ERR12, ERR13 |
| FR17-R12 | Không (checklist) | Không |
| FR17-R13 | IN1 đến IN6 khi bị từ chối qua giao diện | OUT4 |
| FR17-R14 | Không (checklist) | OUT4, OUT5 |
| FR17-R15 | IN1 | OUT3 |
| FR17-R16 (đề xuất) | IN1 | OUT1, OUT3 |
| FR17-R17 (đề xuất) | Không (checklist) | Không |
| FR17-R18 (đề xuất) | IN9 | OUT6 |
| FR17-R19 (đề xuất) | Không (checklist) | Không |

Không có biến nào cho Q6 (sửa mã): FR-17 chỉ ghi Thêm, Xem, Xóa và giao diện không có nút sửa (`00_spec.md` mục 4.4).

## 9. Điểm cần sinh viên quyết định

Cột "Đề xuất của AI" chỉ là nhận xét để tham khảo; sinh viên quyết định.

| # | Vấn đề | Các lựa chọn | Đề xuất của AI |
|---|---|---|---|
| 1 | Mức chia loại lỗi ở mục 4.2 | (a) Giữ 11 loại lỗi về dữ liệu (ERR1 đến ERR11), mỗi trường tách "thiếu" và "vi phạm ràng buộc"; (b) Gộp các lỗi "thiếu trường" thành một loại, ghi kèm tên trường; (c) Mỗi trường một loại lỗi, không tách "thiếu" và "vi phạm" | (a): Đặc tả nêu riêng từng điều kiện, tách thì mỗi test case không hợp lệ ở S3 biết đúng nguyên nhân mong đợi |
| 2 | Nhận các yêu cầu đề xuất bổ sung FR17-R16 đến R19 (mục 7.1) | (a) Nhận cả bốn; (b) Chỉ nhận R16 và R18 (có miền giá trị để chia lớp), R17 và R19 bỏ; (c) Không nhận | (a): Cả bốn đều là đặc tả áp trực tiếp cho màn hình này; R17, R19 chỉ thêm 2 dòng checklist |
| 3 | Nhận các câu hỏi mới Q9 đến Q22 (mục 7.2) để S2 chuyển thành giả định | (a) Nhận hết; (b) Chọn bớt (ghi rõ câu nào bỏ) | (a): Mỗi câu ứng với một ràng buộc đặc tả không nói mà ảnh hưởng tới kết quả mong đợi |
| 4 | Trường `is_active` (Q8): Mã mới tạo có đang hoạt động không | (a) Không mô hình hóa ở FR-17, ghi thành rủi ro "không kiểm chứng được trong phạm vi FR-17"; (b) Thêm Output "mã mới dùng được", kiểm bằng K9 (`POST /api/apply-coupon`), ghi rõ phụ thuộc FR-09 | (a): Màn hình FR-17 không hiện `is_active`; dùng K9 thì khi lỗi không biết lỗi thuộc FR-17 hay FR-09 |
| 5 | IN8 (lựa chọn ở hộp thoại xác nhận xóa) và OUT10 | (a) Giữ làm ứng viên, S2 đặt giả định cho Q7; (b) Bỏ, coi xóa là một bước | (a): Chưa biết có hộp thoại hay không; giữ thì không mất gì, nếu không có hộp thoại thì test case tương ứng ghi Blocked ở S6 |
| 6 | IN12 (múi giờ, ngôn ngữ máy) | (a) Không phải biến, ghi thành điều kiện môi trường cần ghi lại ở S6; (b) Giữ làm biến, chia lớp ở S2 | (a): Đặc tả không có ràng buộc nào, và khó thay đổi múi giờ một cách có kiểm soát trong khi test |
| 7 | ERR15 (sai kiểu, sai định dạng qua API) | (a) Giữ làm ứng viên, S2 quyết định theo giả định Q13, Q14; (b) Bỏ, chỉ test giá trị đúng kiểu | (a): Ô số và ô ngày trên giao diện có thể chặn các giá trị này, nên API là đường duy nhất kiểm được hệ thống |
| 8 | Cách kiểm chứng tác động (mục 5) | (a) Dùng K1 đến K8, không dùng K9; (b) Dùng K1 đến K9 | (a): Giữ lỗi khoanh được trong FR-17; K9 chỉ cần nếu chọn 4(b) |
| 9 | Nhóm checklist (mục 6) | (a) Lập nhóm checklist riêng ngoài Domain Testing như mục 6; (b) Không kiểm các yêu cầu tĩnh trong bài này | (a): R12, R14 nằm trong danh sách yêu cầu của `00_spec.md`; không kiểm thì ma trận truy vết ở S3 có yêu cầu chưa phủ |

## 10. Ghi chú cho bước sau

Cho S2:

- Các câu hỏi Q1 đến Q5, Q7, Q8 và Q9 đến Q22 (nếu được nhận) thành giả định cùng số (`A01` ứng với `Q1`, `A09` ứng với `Q9`), mỗi giả định có phương án và hệ quả. Q6 đã đóng (không có thao tác sửa).
- Biến có ràng buộc thứ tự, cần lớp và cận cho S4: IN3 (> 0; giới hạn trên của `percent` theo Q1), IN4 (>= 0), IN6 (>= 1), IN5 (ngày tương đối theo IN10: hôm qua, hôm nay, ngày mai, theo Q5).
- IN3 phụ thuộc IN2: Tách lớp theo từng loại `percent`, `fixed` khi có lý do tin hai loại xử lý khác nhau (giới hạn trên Q1, quan hệ với IN4 Q12).
- IN2 là tập giá trị: Hai giá trị hợp lệ chọn được trên giao diện; giá trị ngoài tập, rỗng, khác hoa thường chỉ gửi được qua API (Q11).
- IN1 là chuỗi: Xét độ dài, tập ký tự (Q4), khoảng trắng đầu, cuối, giữa, chỉ khoảng trắng (Q9), hoa thường khi so trùng và khi lưu (Q4, Q10), chuỗi có thẻ HTML (R15), chuỗi kiểu SQL (R16 nếu được nhận).
- Lớp "để trống" của IN4, IN6 phải tự xóa giá trị mặc định (`0`, `1`).
- Môi trường (`platforms.md`): Ô số có thể chặn chữ, cho gõ `e`, `-`, xử lý số thập phân theo bước nhảy; ô ngày chỉ cho chọn ngày có thật. Lớp nào bị môi trường chặn hoặc biến đổi thì ghi chú và cân nhắc đường API.
- Ví dụ trong API spec dùng `"expired_at": "2025-01-31"`, là ngày đã qua so với thời điểm làm bài. Đây chỉ là ví dụ, không phải quy tắc; có thể ghi vào cột "Chữ đặc tả" của giả định A05.
- Xóa: Lớp của IN7 (mã mẫu, mã vừa tạo, mã đã xóa, `id` không tồn tại) theo Q15, Q16; IN8 theo quyết định 5.
- IN11 (chỉ nhóm API): Không token, token không hợp lệ, token user thường, token admin; xét cho cả ba thao tác Thêm, Xem, Xóa; đường dẫn theo Q22.
- Lớp Output: OUT1 đến OUT10, ERR1 đến ERR15 theo quyết định 1 và 7; lỗi mới từ giả định đánh số từ ERR16.
- Thông tin S0 dùng được: Chỉ phần giao diện trong `00_spec.md`; không dùng kết quả nhập thử.
