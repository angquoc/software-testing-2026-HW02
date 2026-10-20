# S0: Trích đặc tả và khảo sát giao diện (FR-07 Giỏ hàng, Web)

- Bước: S0 (Trích đặc tả, khảo sát giao diện), pha 1
- Thời gian tạo: 2026-10-21 02:16 (UTC+07:00)
- Căn cứ: `Homeworks/eshop-sut/README.md` (SRS, mục 1, 3, 4, 8, 9), `Homeworks/eshop-sut/api_specification.md` (mục 4), `Homeworks/HW02/WORKFLOW.md`, `Homeworks/HW02/README.md`
- Nền tảng: Web, `http://localhost:5173`. Tài khoản khảo sát: `test@eshop.com`. Không dùng chức năng đăng ký.

---

## 1. Cách làm

- Mục 2 chép **nguyên văn** các đoạn đặc tả liên quan (dòng bắt đầu bằng `>`), giữ nguyên ký tự gốc, kể cả dấu "—" mà quy tắc định dạng không cho dùng ngoài phần trích.
- Mục 3 tách đặc tả thành yêu cầu có mã `FR07-Rnn`, mỗi mã một điều kiện kiểm được, chia 5 nhóm: Chính (FR-07), phụ (yêu cầu giao diện chung áp cho trang Giỏ hàng), liên quan (feature khác dùng làm đường vào), API, tham khảo (bảo mật).
- Mục 4 là câu hỏi mở `Qnn`. AI không trả lời bằng cách đoán.
- Mục 5 là bảng quan sát `Onn` để trống cho sinh viên điền. Bảng chỉ hỏi những gì nhìn thấy được mà không cần nhập dữ liệu, không cần thao tác chức năng của giỏ hàng và không cần DevTools.

## 2. Trích nguyên văn đặc tả

### 2.1 FR-07 (SRS, mục 4)

> ### FR-07: Giỏ hàng (Shopping Cart)
>
> - Hiển thị danh sách sản phẩm với các cột: **Sản phẩm**, **Đơn giá**, **Số lượng** (có nút +/- để chỉnh), **Thành tiền**, **Thao tác**.
> - Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.
> - Nút **Xóa sản phẩm** phải có dialog xác nhận trước khi thực hiện.
> - Có nút **Tiếp tục mua sắm** để quay về trang chủ.
> - Tổng tiền hiển thị nhãn chính xác: **"Tổng cộng"** (không phải "Tổng tạm tính").
> - Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng.

### 2.2 Tài khoản và môi trường (SRS, mục 1)

> | Frontend Web | React + Vite + Tailwind CSS | `http://localhost:5173` |
>
> **Tài khoản mặc định:**
>
> - Admin: `admin@eshop.com` / `Admin123!`
> - User test: `test@eshop.com` / `Test1234!`

Ghi chú: SRS không mô tả dữ liệu mẫu của sản phẩm và không nói giỏ hàng của `test@eshop.com` ban đầu có gì.

### 2.3 Feature khác có liên quan tới giỏ hàng (SRS, mục 3 và 4)

FR-06 (đường vào: Thêm sản phẩm vào giỏ):

> - Có ô nhập **Số lượng** (chỉ nhận số nguyên dương, tối thiểu là 1).
> - Nút **Thêm vào giỏ hàng** — sau khi bấm hiển thị phản hồi trực quan (toast notification hoặc badge cập nhật).

FR-08 (dùng giỏ hàng làm đầu vào):

> - Chỉ người dùng **đã đăng nhập** mới tiến hành thanh toán được.
> - **Tổng tiền thanh toán** được tính tự động từ giỏ hàng và không cho phép người dùng chỉnh sửa trực tiếp.
> - Sau thanh toán thành công, giỏ hàng được xóa.

### 2.4 Yêu cầu giao diện chung (SRS, mục 8)

FR-21:

> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
> - **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
> - **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
> - **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.

FR-22:

> - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
> - Trường Email phải dùng `type="email"`.
> - Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
> - Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
> - Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.

FR-23:

> - Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.
> - Link "Giỏ hàng" phải hiển thị **badge số lượng** sản phẩm trong giỏ.
> - Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").
> - Breadcrumb bắt buộc có ở các trang con (Giỏ hàng, Thanh toán, Chi tiết sản phẩm).

FR-24:

> - Sau khi bấm "Thêm vào giỏ", phải có phản hồi trực quan (toast/badge).
> - Khi xóa item khỏi giỏ phải có dialog xác nhận.
> - Trang trống (Empty State) phải có icon/hình minh họa và message thân thiện.
> - Tất cả ảnh sản phẩm phải có thuộc tính `alt` mô tả nội dung ảnh (không để rỗng).

### 2.5 API giỏ hàng (API spec, mục 4)

> ## 4. Giỏ hàng & Đơn hàng (Cart & Orders)
>
> *Yêu cầu Header: `Authorization: Bearer <token>`*
>
> ### 4.1 Lấy giỏ hàng
> - **Endpoint:** `GET /api/cart`
>
> ### 4.2 Thêm vào giỏ hàng
> - **Endpoint:** `POST /api/cart`
> - **Body (JSON):**
>   ```json
>   {
>     "id": 1,
>     "name": "Sản phẩm A",
>     "price": 100000,
>     "quantity": 2
>   }
>   ```

Ghi chú: API spec không mô tả phản hồi của hai API này (thành công hay thất bại), và không mô tả API nào để đổi số lượng hay xóa một sản phẩm khỏi giỏ.

API đăng nhập (để lấy token khi test API giỏ hàng, API spec mục 1.2):

> - **Endpoint:** `POST /api/login`
> - **Phản hồi thành công (200 OK):** Trả về chuỗi JWT `token` và thông tin `user`.

### 2.6 Bảo mật tham khảo (SRS, mục 9)

> ## 9. Yêu cầu Bảo mật (Security Requirements — Tham khảo)
>
> | SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ. |
> | SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
> | SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp. |

## 3. Danh sách yêu cầu có mã

### 3.1 Nhóm chính (FR-07)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR07-R01 | Trang giỏ hàng hiển thị danh sách sản phẩm có cột "Sản phẩm" | FR-07 ý 1 | |
| FR07-R02 | Danh sách có cột "Đơn giá" | FR-07 ý 1 | |
| FR07-R03 | Danh sách có cột "Số lượng" | FR-07 ý 1 | |
| FR07-R04 | Cột Số lượng có nút `+` để tăng số lượng | FR-07 ý 1 | Bước tăng không được nêu (Q07) |
| FR07-R05 | Cột Số lượng có nút `-` để giảm số lượng | FR-07 ý 1 | Hành vi ở số lượng 1 không được nêu (Q04) |
| FR07-R06 | Danh sách có cột "Thành tiền" | FR-07 ý 1 | Cách tính không được nêu (Q01) |
| FR07-R07 | Danh sách có cột "Thao tác" | FR-07 ý 1 | |
| FR07-R08 | Thêm một sản phẩm đã có trong giỏ làm tăng số lượng của dòng sản phẩm đó | FR-07 ý 2 | Tăng thêm bao nhiêu không được nêu (Q08) |
| FR07-R09 | Thêm một sản phẩm đã có trong giỏ không tạo dòng mới | FR-07 ý 2 | |
| FR07-R10 | Mỗi sản phẩm trong giỏ có nút Xóa sản phẩm | FR-07 ý 3 | Nhãn nút không được nêu nguyên văn |
| FR07-R11 | Bấm Xóa sản phẩm hiện dialog xác nhận; sản phẩm chưa bị xóa trước khi người dùng xác nhận | FR-07 ý 3, FR-24 ý 2 | Hành vi khi hủy dialog không được nêu (Q10) |
| FR07-R12 | Có nút "Tiếp tục mua sắm" | FR-07 ý 4 | |
| FR07-R13 | Bấm "Tiếp tục mua sắm" quay về trang chủ | FR-07 ý 4 | |
| FR07-R14 | Tổng tiền có nhãn chính xác "Tổng cộng" (không phải "Tổng tạm tính") | FR-07 ý 5 | Cách tính tổng không được nêu (Q02) |
| FR07-R15 | Giỏ hàng trống có hình minh họa | FR-07 ý 6, FR-24 ý 3 | |
| FR07-R16 | Giỏ hàng trống có thông báo rõ ràng | FR-07 ý 6, FR-24 ý 3 | "Rõ ràng", "thân thiện" là tiêu chí chủ quan (Q20) |

### 3.2 Nhóm phụ (yêu cầu giao diện chung áp cho trang Giỏ hàng)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR07-R17 | Toàn bộ chữ trên trang Giỏ hàng là tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn) | FR-21 ý 1 | |
| FR07-R18 | Nút hành động tích cực trên trang Giỏ hàng có màu xanh dương | FR-21 ý 2 | Nút nào là "tích cực" không được nêu (Q22) |
| FR07-R19 | Nút nguy hiểm, hủy bỏ trên trang Giỏ hàng (và trong dialog xóa) có màu đỏ | FR-21 ý 2 | Q22 |
| FR07-R20 | Đơn giá, Thành tiền, Tổng cộng dùng ký hiệu `₫` và phân cách hàng nghìn | FR-21 ý 3 | Ký tự phân cách và vị trí `₫` không được nêu (Q03) |
| FR07-R21 | Trang Giỏ hàng có đúng 1 thẻ `<h1>` mô tả nội dung trang | FR-21 ý 4 | Chỉ kiểm được bằng DevTools ở S6 |
| FR07-R22 | Thứ tự focus theo Tab trên trang Giỏ hàng đi từ trên xuống dưới, trái sang phải | FR-21 ý 5 | Chỉ kiểm được khi chạy ở S6 |
| FR07-R23 | Navbar highlight mục Giỏ hàng khi đang ở trang Giỏ hàng | FR-23 ý 1 | |
| FR07-R24 | Link "Giỏ hàng" trên navbar có badge số lượng sản phẩm trong giỏ | FR-23 ý 2 | Đếm số dòng hay tổng số lượng không được nêu (Q17) |
| FR07-R25 | Trang Giỏ hàng có breadcrumb | FR-23 ý 4 | Nội dung breadcrumb không được nêu (Q19) |
| FR07-R26 | Ảnh sản phẩm trong giỏ (nếu có) có thuộc tính `alt` mô tả nội dung, không rỗng | FR-24 ý 4 | Chỉ kiểm được bằng DevTools ở S6; chỉ áp dụng nếu giỏ hiển thị ảnh (O14) |

### 3.3 Nhóm liên quan (feature khác, dùng làm đường vào hoặc điều kiện)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR07-R27 | Ô Số lượng ở trang chi tiết sản phẩm chỉ nhận số nguyên dương, tối thiểu 1; giá trị này là số lượng được thêm vào giỏ | FR-06 ý 2, 3 | Thuộc FR-06; ghi lại vì là nguồn của số lượng trong giỏ (Q08). Phần "giá trị này là số lượng được thêm vào giỏ" là cách hiểu, chờ sinh viên xác nhận ở điểm quyết định 1 |

### 3.4 Nhóm API

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR07-R28 | `GET /api/cart` trả về giỏ hàng của người dùng gửi token | API spec 4.1 | Định dạng phản hồi không được mô tả (Q27). "Của người dùng gửi token" là cách hiểu (Q16) |
| FR07-R29 | `POST /api/cart` với body `id`, `name`, `price`, `quantity` thêm sản phẩm vào giỏ | API spec 4.2 | Phản hồi không được mô tả; vai trò của `name`, `price` do client gửi không được nêu (Q24) |
| FR07-R30 | API giỏ hàng yêu cầu header `Authorization: Bearer <token>`; không có token hợp lệ thì bị từ chối | API spec mục 4, SEC-02 | Mã lỗi và thông báo không được mô tả (Q25) |

### 3.5 Nhóm tham khảo (bảo mật)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR07-R31 | Tên sản phẩm hiển thị trong giỏ được escape, không render HTML | SEC-04 | Liên quan vì `POST /api/cart` nhận `name` từ client (Q24) |
| FR07-R32 | Truy vấn giỏ hàng dùng Parameterized Query | SEC-05 | Không quan sát trực tiếp được bằng hộp đen; chỉ suy ra qua hành vi khi gửi chuỗi đặc biệt |

### 3.6 Yêu cầu không áp dụng hoặc ngoài phạm vi

| Nguồn | Yêu cầu | Lý do |
|---|---|---|
| FR-22 ý 1 đến 5 | Dấu `*`, `type="email"`, `type="password"`, vị trí thông báo lỗi, Step Indicator | Trang Giỏ hàng không có form nhập liệu theo đặc tả. Nếu O16 cho thấy Số lượng là ô nhập, sinh viên xem lại ý 4 (vị trí thông báo lỗi) |
| FR-23 ý 3 | Nút "Đăng xuất" | Thuộc điều hướng chung của mọi trang, không riêng giỏ hàng |
| FR-24 ý 1, FR-06 ý 3 | Phản hồi trực quan sau khi bấm "Thêm vào giỏ" | Xảy ra ở trang chi tiết sản phẩm (FR-06). Phần badge đã có ở FR07-R24 |
| FR-08 | Thanh toán, giỏ được xóa sau thanh toán thành công | Thuộc FR-08 |
| FR-20 | Giỏ hàng trên Mobile | Feature này làm trên Web |

## 4. Câu hỏi mở

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| | **Tính toán và hiển thị tiền** | | |
| Q01 | Thành tiền có phải bằng Đơn giá nhân Số lượng không? | FR07-R06 | Không có trong đặc tả |
| Q02 | Tổng cộng có phải bằng tổng Thành tiền của mọi dòng không, có cộng phí hay trừ giảm giá nào không? | FR07-R14 | Không có trong đặc tả |
| Q03 | Ký tự phân cách hàng nghìn là dấu chấm hay dấu phẩy; `₫` đứng trước hay sau số; có khoảng cách giữa số và `₫` không? | FR07-R20 | Quan sát S0 (cách đang hiển thị); đặc tả không chọn |
| | **Số lượng** | | |
| Q04 | Số lượng nhỏ nhất trong giỏ là bao nhiêu? Bấm `-` khi số lượng là 1 thì nút bị vô hiệu, số lượng giữ nguyên, hay sản phẩm bị xóa (có qua dialog không)? | FR07-R05, FR07-R11 | Quan sát S0 (nút `-` có trông bị mờ không); Chạy thử S6 |
| Q05 | Số lượng có giới hạn trên không (tồn kho, số tối đa)? | FR07-R04 | Không có trong đặc tả |
| Q06 | Số lượng chỉ chỉnh bằng `+`/`-` hay gõ trực tiếp được? Nếu gõ được thì nhận giá trị nào? | FR07-R03 | Quan sát S0 (hình dạng ô); Chạy thử S6 |
| Q07 | Mỗi lần bấm `+` hoặc `-` thay đổi bao nhiêu đơn vị? | FR07-R04, FR07-R05 | Chạy thử S6 |
| Q08 | Thêm lại một sản phẩm đã có trong giỏ thì số lượng tăng 1 hay tăng đúng bằng số lượng chọn ở trang chi tiết (hoặc `quantity` gửi qua API)? | FR07-R08, FR07-R27, FR07-R29 | Không có trong đặc tả |
| Q09 | "Cùng một sản phẩm" được xác định theo gì (mã sản phẩm, tên)? Nếu giá sản phẩm thay đổi giữa hai lần thêm thì Đơn giá trong giỏ là giá nào? | FR07-R02, FR07-R08 | Không có trong đặc tả |
| | **Xóa sản phẩm** | | |
| Q10 | Dialog xác nhận có nội dung, nút gì? Bấm hủy hoặc đóng dialog thì sản phẩm và số lượng giữ nguyên? | FR07-R11 | Chạy thử S6 (hoặc Quan sát S0 nếu chọn phương án 3(b)) |
| Q11 | Xóa sản phẩm cuối cùng thì trang chuyển ngay sang trạng thái giỏ trống không? | FR07-R11, FR07-R15, FR07-R16 | Chạy thử S6 |
| Q12 | Có nút xóa toàn bộ giỏ không? Nếu có thì có dialog xác nhận không? | FR07-R11 | Quan sát S0 |
| | **Điều hướng và lưu giỏ** | | |
| Q13 | "Trang chủ" là trang nào (đường dẫn nào)? | FR07-R13 | Quan sát S0 |
| Q14 | Giỏ hàng có được giữ lại khi tải lại trang, đăng xuất rồi đăng nhập lại, mở trình duyệt khác không? | FR07-R28 | Không có trong đặc tả; Chạy thử S6 |
| Q15 | Người chưa đăng nhập có xem được trang Giỏ hàng, thêm được sản phẩm vào giỏ trên Web không? | FR07-R30 | Không có trong đặc tả |
| Q16 | Mỗi người dùng có giỏ riêng, không xem được giỏ của người khác? | FR07-R28, FR07-R30 | Không có trong đặc tả |
| | **Badge và breadcrumb** | | |
| Q17 | Badge đếm số dòng sản phẩm hay tổng số lượng? | FR07-R24 | Không có trong đặc tả |
| Q18 | Khi giỏ trống, badge hiện số 0 hay ẩn? | FR07-R24 | Quan sát S0 |
| Q19 | Breadcrumb của trang Giỏ hàng gồm những mục nào? | FR07-R25 | Quan sát S0; đặc tả không nêu nội dung |
| | **Giỏ trống** | | |
| Q20 | Tiêu chí nào để coi thông báo là "rõ ràng", "thân thiện" và hình là "minh họa"? | FR07-R15, FR07-R16 | Không có trong đặc tả; sinh viên chốt tiêu chí |
| Q21 | Khi giỏ trống, bảng, nhãn "Tổng cộng" và nút "Tiếp tục mua sắm" có còn hiển thị không? | FR07-R12, FR07-R14, FR07-R16 | Quan sát S0 |
| | **Màu và cột Thao tác** | | |
| Q22 | Trên trang Giỏ hàng, nút nào là "hành động tích cực" (ví dụ nút thanh toán, "Tiếp tục mua sắm"), nút nào là "nguy hiểm, hủy bỏ" (nút xóa, nút hủy trong dialog)? | FR07-R18, FR07-R19 | Không có trong đặc tả |
| Q23 | Cột Thao tác chứa những gì ngoài nút xóa? | FR07-R07, FR07-R10 | Quan sát S0 |
| | **API** | | |
| Q24 | `POST /api/cart` nhận `name`, `price` từ client: Hệ thống dùng giá client gửi hay giá của sản phẩm trong CSDL? `id` không tồn tại thì sao? | FR07-R29, FR07-R31 | Không có trong đặc tả |
| Q25 | API giỏ hàng trả về gì khi thất bại (thiếu token, token sai, `quantity` là 0, số âm, số thập phân, không phải số, thiếu trường)? | FR07-R29, FR07-R30 | Không có trong đặc tả; Chạy thử S6 |
| Q26 | Đổi số lượng và xóa sản phẩm trên giao diện có gọi API nào được mô tả không? Nếu không, các thao tác này chỉ kiểm được qua giao diện | FR07-R04, FR07-R05, FR07-R11 | Không có trong đặc tả |
| Q27 | `GET /api/cart` trả về cấu trúc gì (danh sách dòng, tổng tiền)? | FR07-R28 | Không có trong đặc tả; Chạy thử S6 |

## 5. Bảng quan sát giao diện (sinh viên điền)

### 5.1 Chuẩn bị trước khi chụp

1. Đăng nhập Web bằng `test@eshop.com` / `Test1234!` (SRS mục 1).
2. Mở trang Giỏ hàng **trước khi thêm gì**, ghi trạng thái ban đầu vào O01. Nếu giỏ đang trống thì chụp ngay ảnh giỏ trống (`S0_05`).
3. Thêm sản phẩm vào giỏ theo phương án sinh viên chọn ở điểm quyết định 2 (mặc định trong bảng: Hai sản phẩm khác nhau, mỗi sản phẩm một lần, giữ số lượng mặc định). Ghi lại đã thêm gì vào O02 để S6 dựng lại được.
4. Không bấm `+`, `-`, nút xóa, nút "Tiếp tục mua sắm" (đó là hành vi cần test ở S6), trừ khi chọn phương án 3(b).
5. Ảnh chụp **cả cửa sổ trình duyệt** để thấy tiêu đề tab và thanh địa chỉ. Có thể che thanh bookmark, ảnh đại diện nếu không muốn lộ thông tin cá nhân.

### 5.2 Bảng quan sát

| Mã | Mục quan sát | Sinh viên ghi | Ảnh |
|---|---|---|---|
| | **Chuẩn bị** | | |
| O01 | Trạng thái giỏ hàng ngay sau khi đăng nhập (trống, hay có sản phẩm nào, số lượng bao nhiêu) | | |
| O02 | Đã thêm những sản phẩm nào vào giỏ, từ trang nào (trang chủ hay trang chi tiết), số lượng chọn | | |
| | **Đường vào** | | |
| O03 | Mở trang Giỏ hàng bằng cách nào (link, nút, biểu tượng nào, ở vị trí nào trên trang) | | |
| O04 | Đường dẫn trên thanh địa chỉ của trang Giỏ hàng | | |
| O05 | Tiêu đề tab của trang Giỏ hàng (khi có sản phẩm và khi trống) | | |
| O06 | Đường dẫn trên thanh địa chỉ và tiêu đề tab của trang chủ | | |
| | **Navbar và breadcrumb** | | |
| O07 | Nhãn nguyên văn của link Giỏ hàng trên navbar | | |
| O08 | Badge cạnh link Giỏ hàng khi giỏ có sản phẩm: Có không, số hiển thị | | |
| O09 | Badge khi giỏ trống: Có không, số hiển thị | | |
| O10 | Khi đang ở trang Giỏ hàng, mục nào trên navbar trông khác các mục còn lại, khác ở điểm nào (màu, gạch chân, in đậm) | | |
| O11 | Breadcrumb: Có không, nội dung nguyên văn, vị trí | | |
| | **Tiêu đề và chữ (giỏ có sản phẩm)** | | |
| O12 | Các tiêu đề nhìn thấy trên trang, nguyên văn | | |
| O13 | Dòng hướng dẫn hoặc chữ hiển thị sẵn khác (ngoài bảng) | | |
| O14 | Chữ không phải tiếng Việt trên trang (nếu có) | | |
| | **Bảng sản phẩm** | | |
| O15 | Tên các cột, nguyên văn, theo thứ tự từ trái sang phải | | |
| O16 | Cột Sản phẩm hiển thị gì (ảnh, tên, thông tin khác) | | |
| O17 | Cột Đơn giá: Chép nguyên văn giá của từng dòng (giữ dấu phân cách, ký hiệu tiền) | | |
| O18 | Cột Số lượng: Số hiển thị ở từng dòng; số nằm trong ô có viền (giống ô nhập) hay là chữ thường | | |
| O19 | Nút giảm và nút tăng trong cột Số lượng: Nhãn hoặc biểu tượng, thứ tự, màu | | |
| O20 | Ở dòng có số lượng 1, nút giảm trông có khác nút tăng không (mờ, xám) | | |
| O21 | Cột Thành tiền: Chép nguyên văn giá trị của từng dòng | | |
| O22 | Cột Thao tác: Các nút, biểu tượng; nhãn nguyên văn hoặc mô tả biểu tượng; màu nền, màu chữ | | |
| | **Tổng tiền và nút** | | |
| O23 | Nhãn tổng tiền nguyên văn và giá trị hiển thị nguyên văn | | |
| O24 | Các khoản khác hiển thị gần tổng tiền (tạm tính, phí vận chuyển, giảm giá), nếu có | | |
| O25 | Nút "Tiếp tục mua sắm": Nhãn nguyên văn; là nút hay liên kết; màu nền, màu chữ; vị trí | | |
| O26 | Các nút khác trên trang (ví dụ thanh toán, xóa toàn bộ): Nhãn nguyên văn; màu nền, màu chữ; vị trí | | |
| | **Giỏ hàng trống** | | |
| O27 | Hình minh họa: Có không, mô tả ngắn | | |
| O28 | Thông báo nguyên văn | | |
| O29 | Nút hoặc liên kết hiển thị khi giỏ trống: Nhãn nguyên văn, màu, vị trí | | |
| O30 | Bảng, tên cột, nhãn tổng tiền còn hiển thị khi giỏ trống không | | |
| | **Trang có nút thêm vào giỏ (đường vào, FR-06)** | | |
| O31 | Trang chủ: Mỗi sản phẩm có nút thêm vào giỏ không; nhãn nguyên văn | | |
| O32 | Trang chi tiết sản phẩm: Nhãn ô Số lượng, giá trị mặc định, loại ô nhìn thấy được; nhãn nút thêm vào giỏ | | |
| | **Dialog xác nhận xóa (chỉ điền nếu chọn phương án 3(b))** | | |
| O33 | Tiêu đề và nội dung dialog, nguyên văn | | |
| O34 | Các nút trong dialog: Nhãn nguyên văn, màu nền, màu chữ, vị trí | | |

### 5.3 Ảnh cần chụp

| Tên file | Trạng thái | Phải thấy |
|---|---|---|
| `S0_01_trang_chu.png` | Đã đăng nhập, trang chủ | Cả cửa sổ: Tiêu đề tab, thanh địa chỉ, navbar có link Giỏ hàng và badge, ít nhất một sản phẩm |
| `S0_02_chi_tiet_san_pham.png` | Trang chi tiết của một sản phẩm sẽ thêm vào giỏ | Ô Số lượng, nút thêm vào giỏ, tiêu đề tab, thanh địa chỉ |
| `S0_03_gio_hang_co_hang.png` | Giỏ có sản phẩm (sau bước chuẩn bị) | Cả cửa sổ: Tab, thanh địa chỉ, navbar (badge, mục được highlight), breadcrumb, tiêu đề, toàn bộ bảng với tên cột |
| `S0_04_gio_hang_phan_tong.png` | Như `S0_03`, cuộn xuống nếu `S0_03` không thấy hết | Nhãn tổng tiền, giá trị, nút "Tiếp tục mua sắm" và các nút khác. Bỏ ảnh này nếu `S0_03` đã thấy đủ |
| `S0_05_gio_hang_trong.png` | Giỏ trống | Cả cửa sổ: Tab, thanh địa chỉ, badge, hình minh họa, thông báo, các nút |
| `S0_06_dialog_xoa.png` | Chỉ khi chọn phương án 3(b): Dialog đang mở | Toàn bộ dialog và các nút |

## 6. Điểm cần sinh viên quyết định

| # | Vấn đề | Các lựa chọn |
|---|---|---|
| 1 | Phạm vi yêu cầu đưa vào thiết kế. Bản này lấy rộng để bước sau chỉ cần bỏ bớt | (a) Giữ như mục 3: Chính, phụ, liên quan (FR07-R27), API, tham khảo; (b) Như (a) nhưng bỏ nhóm liên quan FR07-R27 (để Số lượng ở trang chi tiết cho FR-06); (c) Chỉ nhóm chính và API |
| 2 | Cách đưa sản phẩm vào giỏ ở S0. Thêm lại cùng sản phẩm, bấm `+`, `-` là chạy thử FR07-R04, R05, R08, R09 trước S6 | (a) Thêm hai sản phẩm khác nhau, mỗi sản phẩm một lần với số lượng mặc định; (b) Như (a) và thêm lại một sản phẩm lần nữa để có dòng số lượng lớn hơn 1; (c) Như (a) nhưng chọn số lượng 2 ở trang chi tiết cho sản phẩm thứ hai |
| 3 | Dialog xác nhận xóa: Bấm nút xóa là chạy thử FR07-R11 (nếu không có dialog, sản phẩm bị xóa ngay) | (a) Không chụp ở S0, để S6; nội dung dialog thành câu hỏi mở Q10; (b) Bấm nút xóa, chụp dialog, rồi bấm nút hủy hoặc đóng |
| 4 | Cách có ảnh giỏ trống nếu giỏ của `test@eshop.com` không trống ngay sau đăng nhập | (a) Nhờ phiên điều phối reset dữ liệu mẫu rồi xem lại; nếu dữ liệu mẫu vẫn có sản phẩm thì báo lại để chọn tiếp; (b) Xóa từng sản phẩm bằng nút xóa (đồng thời là chạy thử FR07-R11) |

## 7. Ghi chú cho bước sau

- S1 cần Input gián tiếp: Trạng thái đăng nhập, giỏ hiện có (trống, đã có sản phẩm đó hay chưa, số lượng hiện tại), dữ liệu sản phẩm (giá), người dùng sở hữu giỏ.
- Dấu hiệu nhận biết kết quả của thao tác giỏ hàng nên lấy ngay trên trang Giỏ hàng (số dòng, Số lượng, Thành tiền, Tổng cộng, trạng thái giỏ trống) và `GET /api/cart`, không dựa vào toast của FR-06.
- Q01, Q02, Q04 đến Q09, Q15 đến Q17, Q20, Q22, Q24, Q25 không có trong đặc tả, dự kiến thành giả định ở S2.
- Nếu Q26 xác nhận không có API đổi số lượng, xóa, thì các lớp của `+`, `-`, xóa chỉ kiểm qua giao diện; nhóm API chỉ gồm `GET` và `POST /api/cart`.
- Tài khoản được dùng: `test@eshop.com`, `admin@eshop.com` (SRS). Không dùng đăng ký. Nếu S2 cần lớp "người dùng khác" (Q16), phải chốt dùng tài khoản nào.
- Các test case làm thay đổi giỏ cần thứ tự chạy và cách đưa giỏ về trạng thái ban đầu (S3).
