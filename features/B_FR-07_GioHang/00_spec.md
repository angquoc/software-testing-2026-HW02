# S0: Trích đặc tả và khảo sát giao diện (FR-07 Giỏ hàng, Web)

- Bước: S0 (Trích đặc tả, khảo sát giao diện), pha 3
- Bản này: Bản review của S0. Bản gốc của AI: `ai_raw/S0_khao_sat.md`
- Thời gian tạo bản AI: 2026-10-21 02:16 (UTC+07:00)
- Cập nhật theo ảnh và quyết định của sinh viên: 2026-10-21 02:36 (UTC+07:00). Điền bảng quan sát từ ảnh, cập nhật câu hỏi mở, ghi 10 khác biệt chờ S6. Các thay đổi so với bản AI liệt kê ở mục cuối
- Căn cứ: `ai_raw/S0_khao_sat.md`, `screenshots/S0_01_trang_chu.png`, `S0_02_chi_tiet_san_pham.png`, `S0_03_gio_hang_co_hang.png` (bản chụp lại lúc 2:54), `S0_05_gio_hang_trong.png`, O01 đến O03 và quyết định do sinh viên cung cấp
- Nền tảng: Web, `http://localhost:5173`. Tài khoản khảo sát: `test@eshop.com`. Không dùng chức năng đăng ký.
- Cập nhật lần 1: 2026-10-21 02:55 (UTC+07:00). Sinh viên bổ sung O02 và chụp lại `S0_03` (2:54, giỏ có 2 dòng); cập nhật O02, O08, O16 đến O18, O21 đến O23; chốt Q28 (cả hai trạng thái) và D10 (tiêu đề tab tính là giao diện); thêm Q30

---

## 1. Cách làm

- Mục 2 chép **nguyên văn** các đoạn đặc tả liên quan (dòng bắt đầu bằng `>`), giữ nguyên ký tự gốc, kể cả dấu "—" mà quy tắc định dạng không cho dùng ngoài phần trích.
- Mục 3 tách đặc tả thành yêu cầu có mã `FR07-Rnn`, mỗi mã một điều kiện kiểm được, chia 5 nhóm: Chính (FR-07), phụ (yêu cầu giao diện chung áp cho trang Giỏ hàng), liên quan (feature khác dùng làm đường vào), API, tham khảo (bảo mật).
- Mục 4 là câu hỏi mở `Qnn`. AI không trả lời bằng cách đoán.
- Mục 5 là bảng quan sát `Onn`. Bảng chỉ hỏi những gì nhìn thấy được mà không cần nhập dữ liệu, không cần thao tác chức năng của giỏ hàng và không cần DevTools. Theo yêu cầu của sinh viên, O01 đến O03 do sinh viên ghi, các ô còn lại do AI điền từ ảnh và chờ sinh viên kiểm lại.
- Pha 3: Đối chiếu ảnh, cập nhật câu hỏi mở (mục 4), ghi khác biệt giữa giao diện và đặc tả (mục 7, chờ xác nhận ở S6).

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

### 4.1 Câu hỏi của bản AI (giữ nguyên)

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

### 4.2 Trạng thái sau quan sát

| Mã | Trạng thái | Căn cứ |
|---|---|---|
| Q01, Q02 | Vẫn mở. Giỏ có 2 dòng, cùng số lượng 1: Thành tiền bằng giá của dòng, "Tổng tạm tính" 58,000,000 bằng tổng hai Thành tiền (30,000,000 + 28,000,000). Chỉ một trường hợp, số lượng đều là 1, nên chưa đủ để trả lời quy tắc tính; đặc tả vẫn không nêu | `S0_03` (O17, O21, O23) |
| Q03 | Đã trả lời bằng quan sát (một phần): Trên trang Giỏ hàng, phân cách hàng nghìn là dấu phẩy, ký hiệu tiền đứng sau số, có một khoảng cách (`30,000,000 ₫`). Còn mở: Ký hiệu là ký tự `₫` hay chữ `đ` gạch dưới (Q29) | `S0_03` |
| Q04 | Chưa áp dụng được: Cột Số lượng không có nút giảm | `S0_03` (O19) |
| Q05 | Vẫn mở | |
| Q06 | Một phần: Số lượng hiển thị dạng chữ thường, không có viền ô nhập. Có gõ được hay không vẫn chờ S6 | `S0_03` (O18) |
| Q07 | Chưa áp dụng được: Không có nút `+`, `-` | `S0_03` (O19) |
| Q08, Q09 | Vẫn mở | |
| Q10 | Vẫn mở, làm rõ ở S6 (quyết định 3(a)) | |
| Q11 | Vẫn mở | |
| Q12 | Đã trả lời bằng quan sát: Không thấy nút xóa toàn bộ giỏ | `S0_03` (O26) |
| Q13 | Đã trả lời bằng quan sát: Trang ở `localhost:5173`, tiêu đề "Danh sách sản phẩm" | `S0_01` (O06) |
| Q14, Q15, Q16, Q17 | Vẫn mở. Q17 hiện chưa áp dụng được vì không thấy badge khi giỏ có 2 dòng (O08) | |
| Q18 | Đã trả lời bằng quan sát: Khi giỏ trống không có badge (khi giỏ có hàng cũng không có, xem D07) | `S0_05` (O09) |
| Q19 | Chưa áp dụng được: Không thấy breadcrumb | `S0_03`, `S0_05` (O11) |
| Q20 | Vẫn mở (sinh viên chốt tiêu chí) | |
| Q21 | Đã trả lời bằng quan sát: Khi giỏ trống không còn bảng, tên cột, nhãn tổng tiền; chỉ có thông báo và liên kết "Tiếp tục mua sắm" | `S0_05` (O28 đến O30) |
| Q22 | Vẫn mở. Các nút cụ thể trên trang: "← Mua tiếp" (nền trắng, viền xám), "Tiến hành thanh toán" (nền xanh lá), "Xóa" (chữ đỏ, không nền) | `S0_03` |
| Q23 | Đã trả lời bằng quan sát: Cột Thao tác chỉ có "Xóa" | `S0_03` (O22) |
| Q24 đến Q27 | Vẫn mở | |

### 4.3 Câu hỏi mới sau quan sát

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q28 | Giỏ có hàng có nút "← Mua tiếp", giỏ trống có liên kết "Tiếp tục mua sắm". FR07-R12, FR07-R13 được xét ở trạng thái nào: Cả hai, chỉ giỏ có hàng, hay chỉ giỏ trống? | FR07-R12, FR07-R13 | Không có trong đặc tả |
| Q29 | Ký hiệu tiền trên trang Giỏ hàng là ký tự `₫` hay chữ `đ` có gạch dưới? Ảnh không phân biệt được hai dạng này | FR07-R20 | Chạy thử S6 (bôi đen giá trị, sao chép, dán vào trình soạn thảo văn bản) |
| Q30 | Ở giỏ trống, "Tiếp tục mua sắm" có dạng liên kết (không nền, không viền). Liên kết có được coi là "nút" theo FR07-R12 không? (Thêm ở cập nhật lần 1, phát sinh từ Q28) | FR07-R12 | Không có trong đặc tả |

Trạng thái: Q28 đã chốt, xét FR07-R12, FR07-R13 ở cả giỏ có hàng và giỏ trống (quyết định 6). Q29 vẫn mở, chờ S6. Q30 vẫn mở, dự kiến thành giả định ở S2.

## 5. Bảng quan sát giao diện

### 5.1 Chuẩn bị đã làm

- Dữ liệu EShop reset lúc 02:25 ngày 21/10/2026 (quyết định 4(a)).
- Đăng nhập Web bằng `test@eshop.com`.
- Thêm sản phẩm theo quyết định 2(a), chi tiết ở O02. Không bấm nút xóa (quyết định 3(a)).
- Thời gian trên ảnh (đồng hồ Windows): `S0_05` lúc 2:30, `S0_01` và `S0_02` lúc 2:33, `S0_03` lúc 2:54 (chụp lại sau khi thêm sản phẩm thứ hai; theo sinh viên, bản chụp lúc 2:34 chỉ có 1 dòng vì chụp trước khi thêm).

### 5.2 Bảng quan sát

Cột "Người ghi": "SV" là sinh viên ghi; "AI từ ảnh" là AI điền theo yêu cầu của sinh viên, chỉ chép những gì thấy trong ảnh, chờ sinh viên kiểm lại.

| Mã | Mục quan sát | Giá trị quan sát | Người ghi | Ảnh |
|---|---|---|---|---|
| | **Chuẩn bị** | | | |
| O01 | Trạng thái giỏ hàng ngay sau khi đăng nhập | Giỏ trống ngay sau khi đăng nhập (dữ liệu vừa reset lúc 02:25 21/10/2026) | SV | `S0_05` |
| O02 | Đã thêm những sản phẩm nào, từ trang nào, số lượng chọn | Thêm iPhone 15 Pro Max từ trang chi tiết; sau đó thêm Samsung Galaxy S24 Ultra từ trang chủ (nút "Thêm vào giỏ"); số lượng mặc định. Đã chụp lại `S0_03` sau khi thêm sản phẩm thứ hai | SV | `S0_02`, `S0_01`, `S0_03` |
| | **Đường vào** | | | |
| O03 | Mở trang Giỏ hàng bằng cách nào | Bấm link "Giỏ hàng" trên navbar | SV | `S0_03` |
| O04 | Đường dẫn trên thanh địa chỉ của trang Giỏ hàng | `localhost:5173/cart` (cả khi có sản phẩm và khi trống) | AI từ ảnh | `S0_03`, `S0_05` |
| O05 | Tiêu đề tab của trang Giỏ hàng | "frontend-web" (cả khi có sản phẩm và khi trống) | AI từ ảnh | `S0_03`, `S0_05` |
| O06 | Đường dẫn và tiêu đề tab của trang chủ | `localhost:5173`; tab "frontend-web"; tiêu đề trang "Danh sách sản phẩm" | AI từ ảnh | `S0_01` |
| | **Navbar và breadcrumb** | | | |
| O07 | Nhãn nguyên văn của link Giỏ hàng trên navbar | "Giỏ hàng", chữ trắng, góc phải navbar, bên trái "Chào, Test User" (chữ vàng) và nút "Thoát" (nền đỏ, chữ trắng) | AI từ ảnh | `S0_01`, `S0_03` |
| O08 | Badge cạnh link Giỏ hàng khi giỏ có sản phẩm | Không có badge (giỏ đang có 2 dòng) | AI từ ảnh | `S0_03` |
| O09 | Badge khi giỏ trống | Không có badge | AI từ ảnh | `S0_05` |
| O10 | Mục navbar trông khác khi đang ở trang Giỏ hàng | Không thấy khác biệt: "Giỏ hàng" chữ trắng giống hệt ở trang chủ, trang chi tiết và trang Giỏ hàng; không gạch chân, không đổi nền | AI từ ảnh | `S0_01`, `S0_02`, `S0_03` |
| O11 | Breadcrumb | Không có, cả khi có sản phẩm và khi trống | AI từ ảnh | `S0_03`, `S0_05` |
| | **Tiêu đề và chữ (giỏ có sản phẩm)** | | | |
| O12 | Các tiêu đề nhìn thấy trên trang | "Giỏ Hàng" (chữ H viết hoa), góc trên bên trái khung nội dung; logo "EShop" trên navbar | AI từ ảnh | `S0_03` |
| O13 | Dòng hướng dẫn hoặc chữ hiển thị sẵn khác | Không có dòng hướng dẫn. Chân trang: "© 2026 EShop SUT. Dành cho mục đích kiểm thử." | AI từ ảnh | `S0_03` |
| O14 | Chữ không phải tiếng Việt | Tiêu đề tab "frontend-web"; "EShop", "SUT" (tên riêng) | AI từ ảnh | `S0_03` |
| | **Bảng sản phẩm** | | | |
| O15 | Tên các cột, từ trái sang phải | "Sản phẩm", "Giá", "Số lượng", "Thành tiền", "Thao tác" | AI từ ảnh | `S0_03` |
| O16 | Cột Sản phẩm hiển thị gì | Chỉ có tên ("iPhone 15 Pro Max", "Samsung Galaxy S24 Ultra"), không có ảnh | AI từ ảnh | `S0_03` |
| O17 | Cột Đơn giá (trên giao diện là cột "Giá"), từng dòng | Dòng 1: "30,000,000 ₫"; dòng 2: "28,000,000 ₫" | AI từ ảnh | `S0_03` |
| O18 | Cột Số lượng: Số hiển thị, dạng hiển thị | "1" ở cả hai dòng; chữ thường, không có viền ô nhập | AI từ ảnh | `S0_03` |
| O19 | Nút giảm và nút tăng trong cột Số lượng | Không có nút giảm, nút tăng | AI từ ảnh | `S0_03` |
| O20 | Ở dòng số lượng 1, nút giảm trông có khác nút tăng không | Không áp dụng: Không có nút (O19) | AI từ ảnh | `S0_03` |
| O21 | Cột Thành tiền, từng dòng | Dòng 1: "30,000,000 ₫"; dòng 2: "28,000,000 ₫" | AI từ ảnh | `S0_03` |
| O22 | Cột Thao tác | Mỗi dòng chỉ có chữ "Xóa", màu đỏ, không nền, không viền | AI từ ảnh | `S0_03` |
| | **Tổng tiền và nút** | | | |
| O23 | Nhãn tổng tiền và giá trị | "Tổng tạm tính:" (chữ đen, đậm) "58,000,000 ₫" (chữ đỏ, đậm), góc dưới bên trái khung | AI từ ảnh | `S0_03` |
| O24 | Các khoản khác gần tổng tiền | Không có | AI từ ảnh | `S0_03` |
| O25 | Nút "Tiếp tục mua sắm" | Không có nút nhãn "Tiếp tục mua sắm". Ở cùng vị trí có "← Mua tiếp": Dạng nút (có viền xám nhạt), nền trắng, chữ xám, góc dưới bên phải, bên trái nút "Tiến hành thanh toán" | AI từ ảnh | `S0_03` |
| O26 | Các nút khác trên trang | "Tiến hành thanh toán": Nền xanh lá, chữ trắng, góc dưới bên phải. Không có nút xóa toàn bộ | AI từ ảnh | `S0_03` |
| | **Giỏ hàng trống** | | | |
| O27 | Hình minh họa | Không có | AI từ ảnh | `S0_05` |
| O28 | Thông báo nguyên văn | "Giỏ hàng của bạn đang trống" (chữ đen, cỡ lớn, giữa trang) | AI từ ảnh | `S0_05` |
| O29 | Nút hoặc liên kết khi giỏ trống | "Tiếp tục mua sắm": Chữ xanh dương, không nền, không viền (dạng liên kết), giữa trang, ngay dưới thông báo | AI từ ảnh | `S0_05` |
| O30 | Bảng, tên cột, nhãn tổng tiền khi giỏ trống | Không hiển thị bảng, tên cột, nhãn tổng tiền; không có tiêu đề "Giỏ Hàng" | AI từ ảnh | `S0_05` |
| | **Trang có nút thêm vào giỏ (đường vào, FR-06)** | | | |
| O31 | Trang chủ: Nút thêm vào giỏ trên từng sản phẩm | Có. Mỗi sản phẩm có "Xem chi tiết" (nền xám nhạt, chữ đen) và "Thêm vào giỏ" (nền xanh dương, chữ trắng); không có ô số lượng. Thấy rõ ở 3 sản phẩm hàng trên; 2 sản phẩm hàng dưới bị cắt phần nút | AI từ ảnh | `S0_01` |
| O32 | Trang chi tiết sản phẩm | Nhãn "Số lượng:", giá trị mặc định "1", ô có viền (ảnh không cho biết là ô số hay ô chữ); nút "Thêm vào giỏ hàng" nền xanh lá, chữ trắng. Đường dẫn `localhost:5173/product/1`, sản phẩm "iPhone 15 Pro Max", giá "30,000,000 ₫" | AI từ ảnh | `S0_02` |
| | **Dialog xác nhận xóa** | | | |
| O33 | Tiêu đề và nội dung dialog | (Để trống theo quyết định 3(a), xem ở S6) | | |
| O34 | Các nút trong dialog | (Để trống theo quyết định 3(a), xem ở S6) | | |

Dữ liệu sản phẩm thấy trên trang chủ (`S0_01`, giá ghi nguyên văn, có thể còn sản phẩm khác bên dưới phần đã chụp):

| Sản phẩm | Giá trên trang chủ |
|---|---|
| iPhone 15 Pro Max | 30,000,000 VND |
| Samsung Galaxy S24 Ultra | 28,000,000 VND |
| MacBook Pro M3 | 45,000,000 VND |
| Tai nghe AirPods Pro 2 | 6,000,000 VND |
| Bàn phím cơ Keychron Q1 | 4,000,000 VND |

### 5.3 Ảnh

| Tên file | Trạng thái | Ghi chú |
|---|---|---|
| `S0_01_trang_chu.png` | Có | Thấy tab, thanh địa chỉ, navbar; 2 sản phẩm hàng dưới bị cắt phần nút (không ảnh hưởng ô nào) |
| `S0_02_chi_tiet_san_pham.png` | Có | Đủ |
| `S0_03_gio_hang_co_hang.png` | Có (chụp lại lúc 2:54) | Thấy đủ bảng 2 dòng, tổng tiền, các nút |
| `S0_04_gio_hang_phan_tong.png` | Không cần | `S0_03` đã thấy tổng tiền và các nút |
| `S0_05_gio_hang_trong.png` | Có | Đủ |
| `S0_06_dialog_xoa.png` | Bỏ | Quyết định 3(a) |

## 6. Ô để trống và điểm cần sinh viên bổ sung

| Mã | Vấn đề | Trạng thái |
|---|---|---|
| O02 | Giá trị sinh viên đưa còn để chỗ trống `<sản phẩm 1>`, `<sản phẩm 2>` | Đã xử lý ở cập nhật lần 1: Sinh viên ghi tên hai sản phẩm |
| O02, `S0_03` | O02 ghi đã thêm 2 sản phẩm, nhưng `S0_03` lúc 2:34 chỉ có 1 dòng | Đã xử lý ở cập nhật lần 1: Theo sinh viên, ảnh cũ chụp trước khi thêm sản phẩm thứ hai; `S0_03` chụp lại lúc 2:54 có đủ 2 dòng |
| O33, O34 | Để trống theo quyết định 3(a) | Không cần làm gì ở S0 |

Ngoài O33, O34, mọi ô đều đã điền.

## 7. Khác biệt giữa giao diện và đặc tả

Mọi khác biệt dưới đây là **chờ xác nhận ở S6**, chưa kết luận là bug.

| Mã | Yêu cầu | Đặc tả nói | Quan sát thấy | Căn cứ |
|---|---|---|---|---|
| D01 | FR07-R02 | Có cột **Đơn giá** | Cột có nhãn "Giá" | `S0_03` (O15) |
| D02 | FR07-R04, FR07-R05 | Số lượng "có nút +/- để chỉnh" | Cột Số lượng chỉ có số "1", không có nút | `S0_03` (O18, O19) |
| D03 | FR07-R12 | Có nút **Tiếp tục mua sắm** | Giỏ có hàng: Không có nút nhãn này, chỉ có "← Mua tiếp". Giỏ trống: Có "Tiếp tục mua sắm" dạng liên kết. Theo Q28, xét ở cả hai trạng thái; liên kết ở giỏ trống có đạt "nút" không chờ Q30 | `S0_03`, `S0_05` (O25, O29) |
| D04 | FR07-R14 | Nhãn chính xác **"Tổng cộng"** (không phải "Tổng tạm tính") | Nhãn "Tổng tạm tính:" | `S0_03` (O23) |
| D05 | FR07-R15 | Giỏ trống phải có hình minh họa | Không thấy hình minh họa | `S0_05` (O27) |
| D06 | FR07-R23 | Navbar highlight trang đang được chọn | Link "Giỏ hàng" trông giống hệt ở mọi trang | `S0_01`, `S0_02`, `S0_03` (O10) |
| D07 | FR07-R24 | Link "Giỏ hàng" có badge số lượng | Không có badge khi giỏ có 2 dòng | `S0_03` (O08) |
| D08 | FR07-R25 | Breadcrumb bắt buộc ở trang Giỏ hàng | Không có breadcrumb | `S0_03`, `S0_05` (O11) |
| D09 | FR07-R18 | Nút hành động tích cực (Submit, Mua hàng) màu xanh dương | "Tiến hành thanh toán" nền xanh lá. Có phải nút "tích cực" hay không chờ Q22 | `S0_03` (O26) |
| D10 | FR07-R17 | Toàn bộ giao diện dùng tiếng Việt | Tiêu đề tab "frontend-web". Sinh viên chốt tiêu đề tab tính là giao diện (quyết định 7) | `S0_03`, `S0_05` (O05, O14) |

Khớp với đặc tả theo quan sát (vẫn kiểm lại ở S6): FR07-R01, R03, R06, R07 (tên cột); FR07-R10 (có "Xóa" ở mỗi dòng); FR07-R16 (có thông báo, mức "rõ ràng" chờ Q20); FR07-R19 ("Xóa" chữ đỏ, chờ Q22); FR07-R20 (dấu phẩy phân cách, ký hiệu chờ Q29).

### 7.1 Ngoài phạm vi (khác biệt thuộc feature khác, chỉ ghi nhận)

| Feature | Đặc tả nói | Quan sát thấy | Căn cứ |
|---|---|---|---|
| FR-05, FR-21 ý 3 | Giá dùng ký hiệu `₫` | Trang chủ ghi "VND" (ví dụ "30,000,000 VND") | `S0_01` |
| FR-23 ý 3 | Nút nhãn "Đăng xuất" (không phải "Thoát") | Nút "Thoát" trên navbar mọi trang | `S0_01`, `S0_02`, `S0_03` |
| FR-06, FR-21 ý 2 | Nút hành động tích cực màu xanh dương | "Thêm vào giỏ hàng" ở trang chi tiết nền xanh lá (ở trang chủ "Thêm vào giỏ" nền xanh dương) | `S0_02`, `S0_01` |
| FR-23 ý 4 | Breadcrumb ở trang Chi tiết sản phẩm | Không có breadcrumb | `S0_02` |

## 8. Các chỗ AI đã sửa so với bản sinh viên điền

Sinh viên ghi O01 đến O03; các ô còn lại do AI điền từ ảnh theo yêu cầu của sinh viên (mục 9).

| Mã | Sinh viên ghi | Đã sửa thành | Lý do |
|---|---|---|---|
| O01, O03 | Như bảng | Không sửa | Khớp `S0_05` (giỏ trống lúc 2:30, sau lúc reset 02:25) và `S0_03` (link "Giỏ hàng" trên navbar) |
| O02 | Như bảng (bản cập nhật lần 1) | Không sửa | Khớp `S0_02` (trang chi tiết iPhone 15 Pro Max), `S0_01` (nút "Thêm vào giỏ" ở trang chủ) và `S0_03` chụp lại (2 dòng, cùng số lượng 1) |

## 9. Quyết định của sinh viên

| # | Vấn đề | Quyết định |
|---|---|---|
| 1 | Phạm vi yêu cầu | (a) Giữ cả 5 nhóm: Chính, phụ, liên quan (FR07-R27), API, tham khảo |
| 2 | Cách đưa sản phẩm vào giỏ ở S0 | (a) Hai sản phẩm khác nhau, mỗi sản phẩm một lần, số lượng mặc định |
| 3 | Dialog xác nhận xóa | (a) Để S6; bỏ ảnh `S0_06`; O33, O34 để trống |
| 4 | Ảnh giỏ trống | (a) Reset dữ liệu mẫu (đã reset lúc 02:25, giỏ trống ngay sau đăng nhập) |
| 5 | Người điền bảng quan sát | Sinh viên ghi O01 đến O03; yêu cầu AI điền các ô còn lại từ ảnh, ô ảnh không thể hiện thì để trống; sinh viên kiểm lại |
| 6 | Q28: Xét FR07-R12, FR07-R13 ở trạng thái nào | Cả hai trạng thái: Giỏ có hàng và giỏ trống (cập nhật lần 1) |
| 7 | D10: Tiêu đề tab có tính là giao diện theo FR07-R17 không | Có tính (cập nhật lần 1) |
| 8 | O02 và `S0_03` | Bổ sung tên sản phẩm ở O02; chụp lại `S0_03` sau khi thêm sản phẩm thứ hai (cập nhật lần 1) |

## 10. Trả lời câu hỏi khi review

Không có câu hỏi của sinh viên ở lượt này.

## 11. Kiểm tra mâu thuẫn

| Quyết định hoặc câu hỏi | Kết quả kiểm tra |
|---|---|
| Quyết định 2(a) và `S0_03` | Ở bản pha 3 bị vướng (`S0_03` chỉ có 1 dòng). Cập nhật lần 1: Thống nhất, `S0_03` chụp lại có 2 dòng (quyết định 8) |
| Quyết định 6 (Q28) và D03 | Thống nhất: D03 xét cả hai trạng thái. Phát sinh Q30 (liên kết có tính là nút không), để S2 đặt giả định |
| Quyết định 7 (D10) và FR07-R17 | Thống nhất: FR-21 chỉ miễn "thuật ngữ kỹ thuật chuẩn"; "frontend-web" là tên kỹ thuật của ứng dụng, không phải thuật ngữ chuẩn, nên D10 giữ là khác biệt chờ S6 |
| Quyết định 3(a) và O33, O34, Q10 | Thống nhất: O33, O34 để trống, Q10 làm rõ ở S6 |
| Quyết định 4(a) và O01 | Thống nhất: Giỏ đã trống sau reset nên không cần xóa sản phẩm |
| Quyết định 1(a) và D02, D06 đến D08 | Thống nhất: Yêu cầu vẫn giữ trong thiết kế dù giao diện chưa thấy chức năng tương ứng; test case dự kiến ghi nhận khác biệt ở S6 |
| Quyết định 5 và quy trình | Vướng quy trình: WORKFLOW mục 3.1 bước 2 và skill quy định sinh viên điền bảng quan sát, AI không điền thay. Xử lý: Ghi rõ người ghi từng ô, AI chỉ chép những gì thấy trong ảnh, sinh viên kiểm lại; nên ghi điểm này vào AI Audit Report |

## 12. Ghi chú cho bước sau

- Trên giao diện, số lượng chỉ vào giỏ qua hai đường: Nút "Thêm vào giỏ" ở trang chủ (không có ô số lượng) và ô "Số lượng:" (mặc định 1) cùng nút "Thêm vào giỏ hàng" ở trang chi tiết. S1 cần xét cả hai đường cho FR07-R08, FR07-R09 (và Q08).
- Không có nút `+`, `-` (D02) và chưa biết có API đổi số lượng hay không (Q26): S1 vẫn giữ FR07-R04, FR07-R05 nhưng phải ghi cách thực thi; test case qua giao diện có thể không thực hiện được bước chỉnh số lượng.
- Dấu hiệu kết quả lấy trên trang Giỏ hàng: Số dòng, Số lượng, Thành tiền, giá trị tổng tiền, trạng thái giỏ trống (thông báo "Giỏ hàng của bạn đang trống"); và `GET /api/cart`. Không dùng badge (chưa thấy) hay toast của FR-06.
- Kết quả mong đợi viết theo chữ của đặc tả ("Đơn giá", "Tổng cộng", "Tiếp tục mua sắm"), không theo chữ đang hiển thị ("Giá", "Tổng tạm tính", "← Mua tiếp").
- Dữ liệu sản phẩm mẫu và giá ở mục 5.2 dùng để chọn đại diện và tính Thành tiền, Tổng cộng ở S2 đến S4. Giá trên trang chủ ghi "VND", trên trang chi tiết và giỏ ghi ký hiệu tiền.
- Câu hỏi dự kiến thành giả định ở S2: Q01, Q02, Q04 đến Q09, Q15 đến Q17, Q20, Q22, Q24, Q25, Q30. Q28 đã chốt (cả hai trạng thái), D10 đã chốt (tiêu đề tab tính là giao diện).
- Trạng thái giỏ khi khảo sát (O02): iPhone 15 Pro Max (30,000,000) và Samsung Galaxy S24 Ultra (28,000,000), mỗi sản phẩm số lượng 1, tổng hiển thị 58,000,000. Có thể dùng làm dữ liệu cơ sở ở S3.

## 13. Thay đổi so với bản AI (`ai_raw/S0_khao_sat.md`)

Phạm vi: Các chỗ sinh viên chốt hoặc thay đổi so với bản AI. Việc điền bảng quan sát là đầu vào theo quy trình; các mục AI viết ở pha 3 (đối chiếu ảnh, mục 4.2, 4.3, 5 đến 8, 11, 12) không phải phần sinh viên sửa nên không ghi ở đây.

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 6 bản AI, điểm 1; mục 3 | Chọn (a): Giữ 5 nhóm yêu cầu, gồm FR07-R27 | Quyết định của SV | Sinh viên quyết định |
| Mục 6 bản AI, điểm 2; mục 5.1 | Chọn (a): Hai sản phẩm khác nhau, mỗi sản phẩm một lần, số lượng mặc định | Quyết định của SV | Sinh viên quyết định |
| Mục 6 bản AI, điểm 3; O33, O34; ảnh `S0_06` | Chọn (a): Dialog xóa để S6; bỏ `S0_06`; O33, O34 để trống | Quyết định của SV | Sinh viên quyết định |
| Mục 6 bản AI, điểm 4 | Chọn (a): Reset dữ liệu mẫu lúc 02:25 trước khi khảo sát | Quyết định của SV | Sinh viên quyết định |
| Mục 5.2, cột người ghi | O04 đến O32 do AI điền từ ảnh thay vì sinh viên điền như bản AI hướng dẫn | Quyết định của SV | Sinh viên yêu cầu vì thiếu thời gian; lệch WORKFLOW mục 3.1 bước 2, sinh viên kiểm lại |
| Mục 4.3, Q28 | Chốt: Xét FR07-R12, FR07-R13 ở cả giỏ có hàng và giỏ trống; thêm Q30 phát sinh từ quyết định này | Quyết định của SV | Sinh viên quyết định (cập nhật lần 1); Q30 do AI bổ sung khi cập nhật |
| Mục 7, D10 | Chốt: Tiêu đề tab tính là giao diện theo FR07-R17, D10 giữ là khác biệt chờ S6 | Quyết định của SV | Sinh viên quyết định (cập nhật lần 1) |
| Mục 5.2 (O02, O08, O16 đến O18, O21 đến O23), mục 5.3, mục 6 | Cập nhật theo O02 sinh viên bổ sung và ảnh `S0_03` chụp lại lúc 2:54 (giỏ 2 dòng) | Quyết định của SV | Sinh viên bổ sung thông tin và chụp lại ảnh (cập nhật lần 1); không phải lỗi của bản AI |
