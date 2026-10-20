# S1: Xác định biến Input và Output (FR-07 Giỏ hàng, Web)

- Bước: S1 (Xác định biến Input và Output, theo Step 1 của slide S04)
- Thời gian tạo: 2026-10-21 03:15 (UTC+07:00)
- Căn cứ: `00_spec.md` (bản review S0, cập nhật lần 1: Mục 3 danh sách yêu cầu, mục 4 câu hỏi mở, mục 5 bảng quan sát, mục 7 khác biệt, mục 9 quyết định, mục 12 ghi chú cho bước sau)

---

## 1. Cách làm

- Theo Step 1 của slide S04: Liệt kê mọi thứ ảnh hưởng tới kết quả (Input, gồm cả Input không nhập trực tiếp) và mọi kết quả quan sát được (Output, gồm cả lỗi). Bước này chưa chia lớp.
- Tên trên giao diện lấy từ bảng quan sát (`Onn`) của `00_spec.md`. Chỗ giao diện không có thì ghi "Không có trên giao diện" kèm mã khác biệt (`Dnn`).
- Trường API lấy từ API spec mục 4. Chỗ API spec không mô tả thì ghi "Không có trong API spec"; điều đó không có nghĩa là hệ thống không có.
- Ràng buộc đặc tả không nêu thì trỏ về câu hỏi mở (`Qnn`) để S2 đặt giả định.
- Biến có dấu "(ứng viên)" là biến không có ràng buộc trong đặc tả; sinh viên quyết định giữ, bỏ, hay chuyển thành tiền điều kiện (mục 7).
- Đã xử lý mọi ý ở mục 12 "Ghi chú cho bước sau" của `00_spec.md`: Hai đường thêm vào giỏ (IN3), nút `+`, `-` không có trên giao diện (IN4, điểm quyết định 1), dấu hiệu kết quả lấy trên trang Giỏ hàng và `GET /api/cart` (mục 4), kết quả mong đợi viết theo chữ của đặc tả (mục 3), dữ liệu mẫu (IN12), Q28 đã chốt (OUT10).

## 2. Biến Input

### 2.1 Input nhập trực tiếp

| Mã | Biến | Tên trên giao diện | Trường API tương ứng | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|
| IN1 | Sản phẩm được thêm vào giỏ | Chọn qua thẻ sản phẩm ở trang chủ hoặc trang chi tiết (`localhost:5173/product/<id>`) (O31, O32) | `id` (`POST /api/cart`) | Thêm sản phẩm đã có trong giỏ thì tăng số lượng, không tạo dòng mới. "Cùng một sản phẩm" xác định theo gì: Q09. `id` không tồn tại: Q24 | FR07-R08, FR07-R09, FR07-R29 |
| IN2 | Số lượng thêm | Trang chi tiết: Ô "Số lượng:", mặc định "1" (O32). Trang chủ: Không có ô số lượng (O31) | `quantity` (`POST /api/cart`) | Trang chi tiết: Chỉ nhận số nguyên dương, tối thiểu 1 (FR-06, FR07-R27). Thêm trùng thì tăng 1 hay tăng đúng số này: Q08. Giới hạn trên: Q05. API nhận giá trị nào: Q25 | FR07-R08, FR07-R27, FR07-R29 |
| IN3 | Đường thêm vào giỏ | Nút "Thêm vào giỏ" ở trang chủ (O31); nút "Thêm vào giỏ hàng" ở trang chi tiết (O32) | `POST /api/cart` | Đặc tả không phân biệt các đường; trang chủ không có ô số lượng nên số lượng thêm từ trang chủ không được nêu (Q08) | FR07-R08, FR07-R09, FR07-R29 |
| IN4 | Thao tác chỉnh số lượng trong giỏ (tăng, giảm) | Không có trên giao diện (O19, D02) | Không có trong API spec (Q26) | Có nút `+`/`-` để chỉnh. Bước tăng giảm: Q07. Giảm ở số lượng 1: Q04. Giới hạn trên: Q05. Gõ trực tiếp được không: Q06 (O18 cho thấy chữ thường, không có viền ô nhập) | FR07-R03, FR07-R04, FR07-R05 |
| IN5 | Lựa chọn trong dialog xác nhận xóa | Nút "Xóa" ở cột "Thao tác" (O22); nút trong dialog chưa quan sát (O33, O34 để S6, Q10) | Không có trong API spec (Q26) | Phải có dialog xác nhận trước khi xóa. Hủy hoặc đóng dialog thì sao: Q10 | FR07-R10, FR07-R11 |
| IN6 | Tên sản phẩm gửi qua API | Không có trên giao diện | `name` (`POST /api/cart`) | Hiển thị phải được escape (SEC-04). Hệ thống dùng `name` client gửi hay tên trong CSDL: Q24 | FR07-R29, FR07-R31, FR07-R32 |
| IN7 | Đơn giá gửi qua API | Không có trên giao diện | `price` (`POST /api/cart`) | Hệ thống dùng `price` client gửi hay giá trong CSDL: Q24. FR-08 chỉ nói backend tính lại tổng khi thanh toán (ngoài phạm vi) | FR07-R29 |
| IN8 | Token xác thực | Không có trên giao diện | Header `Authorization: Bearer <token>` (API spec mục 4) | API giỏ hàng yêu cầu token (SEC-02). Phản hồi khi thiếu hoặc sai token: Q25 | FR07-R28, FR07-R29, FR07-R30 |

Ghi chú IN4: Đặc tả yêu cầu nút `+`/`-` nhưng giao diện không có (D02) và API spec không mô tả API đổi số lượng. Bản này giữ IN4 theo đặc tả; test case liên quan dự kiến không thực hiện được bước chỉnh số lượng khi chạy (điểm quyết định 1).

### 2.2 Input không nhập trực tiếp

| Mã | Biến | Giá trị hoặc nguồn | Ảnh hưởng tới | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|
| IN9 | Số dòng trong giỏ trước thao tác | 0 (giỏ trống), 1, nhiều dòng | Có hiện trạng thái giỏ trống không; Tổng cộng cộng mấy dòng; xóa dòng cuối thì sao (Q11) | Giỏ trống phải có hình minh họa và thông báo. Q28: Nút "Tiếp tục mua sắm" xét ở cả giỏ trống và giỏ có hàng | FR07-R12, FR07-R13, FR07-R14, FR07-R15, FR07-R16 |
| IN10 | Sản phẩm đích đã có trong giỏ hay chưa | Chưa có; đã có | Tạo dòng mới hay tăng số lượng dòng cũ | Đã có thì tăng số lượng, không tạo dòng mới | FR07-R08, FR07-R09 |
| IN11 | Số lượng hiện tại của dòng đích | Số nguyên từ 1 trở lên (giỏ khảo sát: 1, O18) | Số lượng sau khi thêm trùng, sau khi bấm `+`/`-`; Thành tiền | Giảm ở số lượng 1: Q04. Giới hạn trên: Q05 | FR07-R04, FR07-R05, FR07-R06, FR07-R08 |
| IN12 | Đơn giá của sản phẩm trong dữ liệu | Dữ liệu mẫu thấy được (`00_spec.md` mục 5.2): iPhone 15 Pro Max 30,000,000; Samsung Galaxy S24 Ultra 28,000,000; MacBook Pro M3 45,000,000; Tai nghe AirPods Pro 2 6,000,000; Bàn phím cơ Keychron Q1 4,000,000 | Đơn giá, Thành tiền, Tổng cộng | Cách tính Thành tiền: Q01. Cách tính Tổng cộng: Q02. Định dạng tiền: FR07-R20, Q29 | FR07-R02, FR07-R06, FR07-R14, FR07-R20 |
| IN13 | Trạng thái đăng nhập trên giao diện (ứng viên) | Đã đăng nhập `test@eshop.com`; chưa đăng nhập | Có xem, thêm được vào giỏ không | Đặc tả không nói người chưa đăng nhập dùng giỏ trên Web được không (Q15); chỉ FR-08 yêu cầu đăng nhập khi thanh toán | FR07-R30 (gián tiếp) |
| IN14 | Thời điểm xem lại giỏ (ứng viên) | Ngay sau thao tác; sau khi tải lại trang; sau khi đăng xuất rồi đăng nhập lại | Giỏ có được giữ lại không | Không có trong đặc tả (Q14) | FR07-R28 (gián tiếp) |
| IN15 | Giá sản phẩm thay đổi giữa hai lần thêm (ứng viên) | Không đổi; đổi (cần admin sửa giá, FR-15) | Đơn giá của dòng sau khi thêm trùng | Không có trong đặc tả (Q09) | FR07-R02, FR07-R08 |
| IN16 | Người sở hữu giỏ (ứng viên) | `test@eshop.com`; người dùng khác (chỉ có `admin@eshop.com` trong SRS, không dùng đăng ký) | Người dùng có thấy giỏ của người khác không | Không có trong đặc tả (Q16); SEC-02 chỉ yêu cầu token hợp lệ | FR07-R28, FR07-R30 |

### 2.3 Sự kiện kích hoạt

Không phải biến, không chia lớp.

| Mã | Sự kiện | Nơi thực hiện |
|---|---|---|
| E1 | Bấm "Thêm vào giỏ" (trang chủ) hoặc "Thêm vào giỏ hàng" (trang chi tiết) | Giao diện (O31, O32) |
| E2 | Bấm nút tăng, nút giảm số lượng | Giao diện; hiện không có nút (D02) |
| E3 | Bấm "Xóa" ở một dòng | Giao diện (O22) |
| E4 | Bấm nút xác nhận hoặc nút hủy, đóng dialog xóa | Giao diện; chưa quan sát (Q10) |
| E5 | Bấm "Tiếp tục mua sắm" (giỏ trống, O29) hoặc nút quay về ở giỏ có hàng ("← Mua tiếp", O25) | Giao diện |
| E6 | Mở trang Giỏ hàng (link "Giỏ hàng" trên navbar, O03; hoặc `localhost:5173/cart`, O04) | Giao diện |
| E7 | Gọi `GET /api/cart`, `POST /api/cart` | API |

## 3. Biến Output

### 3.1 Output khi thao tác được chấp nhận

Kết quả mong đợi dùng chữ của đặc tả ("Đơn giá", "Tổng cộng", "Tiếp tục mua sắm"), không dùng chữ đang hiển thị ("Giá", "Tổng tạm tính", "← Mua tiếp").

| Mã | Output | Khi nào xảy ra | Dấu hiệu quan sát được | Yêu cầu |
|---|---|---|---|---|
| OUT1 | Bảng giỏ hàng với 5 cột | Mở trang Giỏ hàng khi giỏ có sản phẩm (E6, IN9 lớn hơn 0) | Các cột "Sản phẩm", "Đơn giá", "Số lượng" (có nút `+`/`-`), "Thành tiền", "Thao tác"; mỗi sản phẩm một dòng | FR07-R01 đến FR07-R07 |
| OUT2 | Dòng mới cho sản phẩm chưa có trong giỏ | E1 hoặc `POST /api/cart` với IN10 = chưa có | Số dòng tăng 1; dòng mới có tên sản phẩm, Đơn giá, Số lượng bằng số lượng thêm (đường trang chủ: Q08) | FR07-R01, FR07-R29 |
| OUT3 | Tăng số lượng của dòng đã có | E1 hoặc `POST /api/cart` với IN10 = đã có | Số dòng không đổi; Số lượng của dòng đó tăng (tăng bao nhiêu: Q08) | FR07-R08, FR07-R09 |
| OUT4 | Số lượng sau khi chỉnh | E2 | Số lượng của dòng tăng hoặc giảm (bước: Q07; ở số lượng 1: Q04); các dòng khác không đổi | FR07-R04, FR07-R05 |
| OUT5 | Thành tiền của dòng | Sau mỗi thay đổi số lượng hoặc khi mở giỏ | Giá trị ở cột Thành tiền (cách tính: Q01) | FR07-R06 |
| OUT6 | Tổng tiền | Khi giỏ có sản phẩm | Nhãn chính xác "Tổng cộng"; giá trị (cách tính: Q02) cập nhật sau mỗi thay đổi | FR07-R14 |
| OUT7 | Dialog xác nhận xóa | E3 | Dialog hiện ra; khi dialog đang mở, dòng vẫn còn trong bảng | FR07-R11 |
| OUT8 | Kết quả sau dialog xóa | E4 | Xác nhận: Dòng đó biến mất, các dòng khác giữ nguyên, Tổng cộng cập nhật. Hủy hoặc đóng: Dòng và Số lượng giữ nguyên (Q10) | FR07-R11 |
| OUT9 | Trạng thái giỏ trống | Mở giỏ khi IN9 = 0; xóa dòng cuối cùng (Q11) | Có hình minh họa; có thông báo rõ ràng (tiêu chí: Q20); không còn bảng (O30) | FR07-R15, FR07-R16 |
| OUT10 | Về trang chủ | E5, ở cả giỏ có hàng và giỏ trống (Q28 đã chốt) | Đường dẫn `localhost:5173`, trang "Danh sách sản phẩm" (O06) | FR07-R12, FR07-R13 |
| OUT11 | Badge số lượng trên link "Giỏ hàng" | Khi giỏ có sản phẩm; sau mỗi lần thêm, xóa, chỉnh số lượng | Số bên cạnh link "Giỏ hàng" (đếm số dòng hay tổng số lượng: Q17; khi giỏ trống: Q18) | FR07-R24 |
| OUT12 | Tên sản phẩm hiển thị nguyên văn | Khi `name` chứa ký tự HTML (IN6) | Chữ hiển thị đúng như chuỗi đã gửi, không bị hiểu thành thẻ HTML | FR07-R31 |
| OUT13 | Phản hồi `GET /api/cart` | E7 với token hợp lệ | Phản hồi chứa các dòng của giỏ người gửi token (cấu trúc: Q27) | FR07-R28 |
| OUT14 | Phản hồi `POST /api/cart` thành công | E7 với token hợp lệ, body hợp lệ | API spec không mô tả phản hồi; dấu hiệu kiểm được: `GET /api/cart` hoặc trang Giỏ hàng có thay đổi tương ứng (OUT2, OUT3). Giá dùng là `price` client gửi hay giá trong CSDL: Q24 | FR07-R29 |

### 3.2 Output khi bị từ chối (theo nguyên nhân)

Đặc tả không nêu câu chữ thông báo hay mã lỗi nào cho giỏ hàng. Kết quả mong đợi chỉ ghi nguyên nhân và việc giỏ không đổi; không bịa câu chữ.

| Mã | Loại lỗi | Nguyên nhân | Dấu hiệu quan sát được | Yêu cầu |
|---|---|---|---|---|
| ERR1 | Từ chối do xác thực | Gọi API giỏ hàng thiếu token, token sai hoặc không hợp lệ | Không trả về dữ liệu giỏ, không thêm vào giỏ; mã lỗi và thông báo: Q25 | FR07-R30 |
| ERR2 | Từ chối do số lượng không hợp lệ | `quantity` (hoặc ô "Số lượng:" ở trang chi tiết) là 0, số âm, số thập phân, không phải số | Giỏ không đổi (kiểm bằng mục 4). Thông báo, mã lỗi: Q25. Căn cứ: FR-06 (FR07-R27); API spec không nêu ràng buộc cho `quantity` | FR07-R27, FR07-R29 |
| ERR3 | Từ chối do sản phẩm hoặc body không hợp lệ (ứng viên) | `id` không tồn tại, thiếu trường trong body | Giỏ không đổi. Đặc tả không nói đây là lỗi (Q24, Q25) | FR07-R29 |

Thuộc tính của thông báo lỗi (vị trí, nội dung, số lỗi khi nhiều lỗi): Đặc tả không nêu cho giỏ hàng. FR-22 ý 4 (lỗi nằm trên nút submit) đã ghi không áp dụng ở `00_spec.md` mục 3.6 vì trang Giỏ hàng không có form.

### 3.3 Phản hồi API

| API | Thành công theo API spec | Thất bại |
|---|---|---|
| `GET /api/cart` | API spec không mô tả phản hồi (Q27) | Không có trong API spec (Q25) |
| `POST /api/cart` | API spec không mô tả phản hồi | Không có trong API spec (Q25) |

## 4. Cách kiểm chứng tác động

Thay đổi hiển thị trên trang Giỏ hàng chưa chứng minh thay đổi đã được lưu.

| Tác động cần kiểm chứng | Cách đề xuất | Phụ thuộc feature khác |
|---|---|---|
| Thêm sản phẩm đã được lưu (OUT2, OUT3) | (a) Tải lại trang Giỏ hàng, xem lại số dòng và Số lượng; (b) `GET /api/cart` | Không. (a) phụ thuộc Q14 (giỏ có được giữ khi tải lại không) |
| Bị từ chối thì giỏ không đổi (ERR1 đến ERR3) | `GET /api/cart` với token hợp lệ trước và sau, so sánh | Không |
| Xóa đã được lưu (OUT8 xác nhận) | Tải lại trang, dòng không còn; thêm lại sản phẩm đó thì xuất hiện dòng mới với Số lượng bằng số lượng thêm (không cộng dồn số lượng cũ) | Không |
| Hủy dialog không xóa (OUT8 hủy) | Tải lại trang, dòng và Số lượng giữ nguyên | Không |
| Thành tiền, Tổng cộng đúng (OUT5, OUT6) | Tính tay từ Đơn giá trong dữ liệu mẫu (IN12) | Đơn giá tham chiếu lấy từ trang chủ, trang chi tiết (FR-05, FR-06) hoặc `GET /api/products/:id` (API spec 3.2) |
| Giỏ được giữ qua phiên đăng nhập (IN14) | Đăng xuất, đăng nhập lại, mở giỏ | Có: Đăng nhập, đăng xuất (FR-02) |
| Giỏ tách theo người dùng (IN16) | `GET /api/cart` bằng token của `admin@eshop.com` không thấy sản phẩm `test@eshop.com` đã thêm | Có: Đăng nhập lấy token (`POST /api/login`) |

## 5. Yêu cầu không mô hình hóa thành biến

Các yêu cầu là thuộc tính tĩnh của trang, không có miền giá trị để chia lớp. Đề xuất kiểm thành nhóm checklist riêng, ngoài Domain Testing.

| Yêu cầu | Nội dung | Ghi chú |
|---|---|---|
| FR07-R01, R02, R03, R06, R07 | Có đủ 5 cột với đúng tên | Cũng là một phần của OUT1; checklist kiểm tên cột (D01: cột "Giá") |
| FR07-R10 | Có nút xóa ở mỗi dòng | |
| FR07-R12 | Có nút "Tiếp tục mua sắm" ở cả hai trạng thái (Q28) | Hành vi bấm nút (FR07-R13) ở OUT10. Liên kết có tính là nút không: Q30 |
| FR07-R14 | Nhãn chính xác "Tổng cộng" | Giá trị tổng ở OUT6 |
| FR07-R15, R16 | Giỏ trống có hình minh họa, thông báo | Cũng là OUT9; tiêu chí "rõ ràng": Q20 |
| FR07-R17 | Toàn bộ chữ trên trang là tiếng Việt, gồm tiêu đề tab (D10 đã chốt) | |
| FR07-R18, R19 | Màu nút tích cực, nút nguy hiểm | Nút nào thuộc loại nào: Q22 |
| FR07-R20 | Ký hiệu `₫`, phân cách hàng nghìn | Q29. S2 có thể xét thêm theo độ lớn của giá trị (mục 8) |
| FR07-R21 | Đúng 1 thẻ `<h1>` | DevTools ở S6 |
| FR07-R22 | Thứ tự Tab | S6 |
| FR07-R23 | Navbar highlight mục Giỏ hàng | D06 |
| FR07-R25 | Có breadcrumb | D08; nội dung: Q19 |
| FR07-R26 | Ảnh sản phẩm có `alt` | Hiện giỏ không hiển thị ảnh (O16) nên chưa áp dụng được |

## 6. Truy vết yêu cầu sang biến

| Yêu cầu | Xử lý ở |
|---|---|
| FR07-R01 đến FR07-R07 | OUT1, OUT4, OUT5; checklist mục 5 |
| FR07-R08, FR07-R09 | IN1, IN2, IN3, IN10, IN11; OUT3 |
| FR07-R10, FR07-R11 | IN5; OUT7, OUT8 |
| FR07-R12, FR07-R13 | IN9; OUT10; checklist mục 5 |
| FR07-R14 | OUT6; checklist mục 5 |
| FR07-R15, FR07-R16 | IN9; OUT9; checklist mục 5 |
| FR07-R17 đến FR07-R23, FR07-R25, FR07-R26 | Checklist mục 5 |
| FR07-R24 | OUT11 |
| FR07-R27 | IN2; ERR2 |
| FR07-R28 | IN8; OUT13 |
| FR07-R29 | IN1, IN2, IN6, IN7; OUT14; ERR2, ERR3 |
| FR07-R30 | IN8; ERR1 |
| FR07-R31 | IN6; OUT12 |
| FR07-R32 | IN6 (giá trị có ký tự đặc biệt của SQL, S2 xét); không quan sát trực tiếp được |

## 7. Điểm cần sinh viên quyết định

| # | Vấn đề | Các lựa chọn |
|---|---|---|
| 1 | IN4 (nút `+`/`-`): Đặc tả yêu cầu nhưng giao diện không có (D02), API spec không mô tả API đổi số lượng | (a) Giữ IN4 theo đặc tả; test case dự kiến không thực hiện được khi chạy, ghi khác biệt; (b) Bỏ IN4, chỉ kiểm sự có mặt của nút bằng checklist |
| 2 | IN13 (đăng nhập trên giao diện): Đặc tả không nói người chưa đăng nhập dùng giỏ được không (Q15) | (a) Tiền điều kiện chung: Mọi test case giao diện chạy khi đã đăng nhập `test@eshop.com`; đăng nhập chỉ là biến ở nhóm API (IN8); (b) Biến Input: Thêm lớp "chưa đăng nhập" ở giao diện |
| 3 | IN3 (đường thêm vào giỏ): Trang chủ không có ô số lượng, trang chi tiết có | (a) Giữ IN3 làm biến với 3 giá trị (trang chủ, trang chi tiết, API); (b) Chỉ trang chi tiết và API; (c) Chỉ trang chi tiết |
| 4 | IN14 (thời điểm xem lại giỏ, Q14) | (a) Không là biến; dùng tải lại trang làm cách kiểm chứng (mục 4); (b) Biến Input với 3 giá trị (ngay sau thao tác, sau tải lại, sau đăng nhập lại) |
| 5 | IN15 (giá đổi giữa hai lần thêm, Q09): Cần admin sửa giá (FR-15) | (a) Bỏ; (b) Giữ, chạy cùng admin |
| 6 | IN16 (người sở hữu giỏ, Q16) | (a) Giữ ở nhóm API: Dùng token `admin@eshop.com` làm người dùng khác; (b) Bỏ |
| 7 | Output lỗi | (a) Tách 3 loại ERR1 đến ERR3 theo nguyên nhân; (b) Gộp thành một loại "API từ chối"; (c) Như (a) nhưng bỏ ERR3 vì đặc tả không nói |
| 8 | Cách kiểm chứng tác động (mục 4) | (a) Tải lại trang và `GET /api/cart`, không dùng đăng xuất, đăng nhập lại; (b) Như (a) và thêm đăng xuất, đăng nhập lại (phụ thuộc FR-02) |
| 9 | Nhóm checklist (mục 5) | (a) Kiểm các yêu cầu tĩnh thành nhóm checklist riêng, ngoài Domain Testing; (b) Viết thành test case thường cùng các test case khác |

## 8. Ghi chú cho bước sau

- Câu hỏi mở sẽ thành giả định ở S2: Q01, Q02 (cách tính), Q04, Q05, Q06, Q07 (số lượng trong giỏ), Q08 (tăng bao nhiêu khi thêm trùng), Q09 (cùng sản phẩm), Q10, Q11 (xóa), Q15 đến Q17 (truy cập, badge), Q20 (tiêu chí giỏ trống), Q22 (màu nút), Q24, Q25 (API), Q30 (liên kết có tính là nút). Q26, Q27 dùng để chốt cách thực thi.
- Biến có ràng buộc thứ tự để S2, S4 xét: IN2 (số lượng thêm, nguyên dương, tối thiểu 1, cận trên chưa biết), IN11 (số lượng hiện tại, giá trị 1 là biên khi giảm), IN9 (số dòng: 0, 1, nhiều).
- Biến tập giá trị: IN3 (3 đường), IN5 (xác nhận, hủy), IN10 (chưa có, đã có), IN8 (có token hợp lệ, thiếu, sai).
- IN6 (`name`): S2 xét chuỗi có thẻ HTML (FR07-R31) và ký tự đặc biệt của SQL (FR07-R32). IN7 (`price`): S2 xét giá khác giá trong CSDL, giá 0, giá âm (Q24).
- FR07-R20: S2 xét giá trị có số chữ số khác nhau (dưới 1,000, từ 1,000, từ 1,000,000), vì định dạng phân cách hàng nghìn có thể khác nhau theo độ lớn.
- Tiền điều kiện chung dự kiến: Reset dữ liệu mẫu, đăng nhập `test@eshop.com`, giỏ trống ban đầu (O01). Chờ chốt ở điểm quyết định 2.
- Mỗi test case làm thay đổi giỏ cần cách đưa giỏ về trạng thái đầu (S3 chốt thứ tự chạy).
