# S0. Đặc tả FR-17: Quản lý Mã Giảm Giá (Coupon CRUD)

| Mục | Giá trị |
|---|---|
| Pool / nền tảng | C, Web Admin (`http://localhost:5174`) |
| SUT | EShop, commit `85af3ba` (bản mới nhất trên GitHub ngày 17/10/2026) |
| Nguồn đặc tả | `README.md` (System Requirements Specification v2.0, cập nhật 2026-05-14) và `api_specification.md` của repo EShop |
| Cách làm | Kiểm thử hộp đen: Thiết kế test case **chỉ dựa trên tài liệu đặc tả**, không đọc mã nguồn |

---

## 1. Trích nguyên văn đặc tả

### 1.1 FR-17 (README, mục 6)

> ### FR-17: Quản lý Mã Giảm Giá (Coupon CRUD)
>
> - Admin có thể Thêm / Xem / Xóa mã giảm giá.
> - Các trường bắt buộc: `code` (duy nhất), `type` (percent/fixed), `discount_value` (dương), `expired_at`, `min_order_amount` (>= 0), `max_uses_per_user` (>= 1).

### 1.2 FR-12: Kiểm soát truy cập (README, mục 6)

> - Phân hệ Admin chỉ dành cho tài khoản có `role = 'admin'`.
> - **Tất cả** các API Admin (`/api/admin/*`) và các API có tính ảnh hưởng dữ liệu (`POST/PUT/DELETE /api/products`, `/api/categories`, `/api/coupons`) đều phải yêu cầu:
>   1. Token JWT hợp lệ.
>   2. `role = 'admin'` trong Token.

### 1.3 FR-09: Cách mã giảm giá được sử dụng (README, mục 4), dùng làm ngữ cảnh

FR-09 không thuộc FR-17, nhưng cho biết ý nghĩa của từng trường mà admin nhập.

> | #   | Điều kiện              | Mô tả                                                       |
> | --- | ---------------------- | ----------------------------------------------------------- |
> | C1  | **Mã tồn tại**         | Mã phải có trong CSDL và đang hoạt động (`is_active = 1`)   |
> | C2  | **Còn hạn sử dụng**    | Ngày hiện tại phải trước `expired_at`                       |
> | C3  | **Đủ ngưỡng đơn hàng** | Tổng đơn hàng **>= (lớn hơn hoặc bằng)** `min_order_amount` |
> | C4  | **Đã đăng nhập**       | Người dùng phải có JWT Token hợp lệ                         |
> | C5  | **Chưa dùng hết lượt** | Số lần đã dùng mã này của user < `max_uses_per_user`        |
>
> **Công thức tính giảm giá:**
>
> - Loại `percent`: `discount_amount = total × discount_value / 100`
> - Loại `fixed`: `discount_amount = discount_value`
> - `final_amount = total - discount_amount`
>
> **Mã giảm giá mẫu trong hệ thống:**
>
> | Mã        | Loại    | Giá trị   | Ngưỡng tối thiểu | Hạn dùng   | Số lần/người |
> | --------- | ------- | --------- | ---------------- | ---------- | ------------ |
> | `SAVE10`  | percent | 10%       | 300,000 ₫        | 2099-12-31 | 1            |
> | `BIGBUY`  | fixed   | 50,000 ₫  | 500,000 ₫        | 2099-12-31 | 1            |
> | `VIP100`  | fixed   | 100,000 ₫ | 300,000 ₫        | 2099-12-31 | 2            |
> | `EXPIRED` | percent | 20%       | 100,000 ₫        | 2020-01-01 | 1            |

### 1.4 FR-21, FR-22: Yêu cầu giao diện và form (README, mục 8)

> **FR-21:**
> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
> - **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
> - **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
>
> **FR-22:**
> - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
> - Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.

### 1.5 Bảo mật (README, mục 9)

> | SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ. |
> | SEC-03 | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token. |
> | SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |

### 1.6 API (api_specification.md, mục 5.2 và 6.4)

> ### 5.2 Lấy danh sách mã giảm giá (Dành cho Admin)
> - **Endpoint:** `GET /api/coupons`
> - **Header:** `Authorization: Bearer <token>`
>
> ## 6. API Dành cho Admin
> *Tất cả API dưới đây yêu cầu `Authorization: Bearer <token>` và tài khoản phải có quyền Admin.*
>
> ### 6.4 Quản lý Mã Giảm Giá
> - **Thêm mới mã:** `POST /api/admin/coupons`
>   - **Body (JSON):**
>     ```json
>     {
>       "code": "TET2025",
>       "type": "percent",
>       "discount_value": 15,
>       "min_order_amount": 200000,
>       "expired_at": "2025-01-31",
>       "max_uses_per_user": 1
>     }
>     ```
> - **Xóa mã:** `DELETE /api/admin/coupons/:id`

---

## 2. Danh sách yêu cầu (dùng để truy vết test case)

Mỗi yêu cầu được tách từ đoạn trích ở mục 1 thành một câu kiểm chứng được. Cột "Nguồn" trỏ về đoạn gốc.

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| FR17-R01 | Admin thêm được mã giảm giá mới khi mọi trường hợp lệ | FR-17 |
| FR17-R02 | Admin xem được danh sách mã giảm giá | FR-17, API 5.2 |
| FR17-R03 | Admin xóa được mã giảm giá | FR-17, API 6.4 |
| FR17-R04 | `code` là bắt buộc | FR-17 |
| FR17-R05 | `code` là duy nhất: Không tạo được mã trùng với mã đã có | FR-17 |
| FR17-R06 | `type` là bắt buộc và chỉ nhận `percent` hoặc `fixed` | FR-17 |
| FR17-R07 | `discount_value` là bắt buộc và phải dương (> 0) | FR-17 |
| FR17-R08 | `expired_at` là bắt buộc | FR-17 |
| FR17-R09 | `min_order_amount` là bắt buộc và phải >= 0 | FR-17 |
| FR17-R10 | `max_uses_per_user` là bắt buộc và phải >= 1 | FR-17 |
| FR17-R11 | Chỉ tài khoản `role = 'admin'` có JWT hợp lệ mới thêm/xem/xóa được mã | FR-12, SEC-02, SEC-03, API mục 6 |
| FR17-R12 | Trường bắt buộc trên form có ký hiệu `*` | FR-22 |
| FR17-R13 | Thông báo lỗi hiện **trên** nút submit | FR-22 |
| FR17-R14 | Giao diện tiếng Việt; nút tích cực màu xanh dương, nút nguy hiểm màu đỏ; tiền dùng `₫` có phân cách hàng nghìn | FR-21 |
| FR17-R15 | Dữ liệu admin nhập (ví dụ `code`) khi hiển thị lại phải được escape, không render HTML | SEC-04 |

---

## 3. Những điểm SRS chưa nói rõ

Cột "Trả lời sau S0" tổng hợp từ giao diện (mục 4). Kết quả SV nhập thử ở S0 (E01–E07) được tách sang file riêng, không để trong file này. Cột cuối cho biết thông tin nào được đưa vào prompt cho AI ở S1–S4:

- **Có**: Thông tin nhìn thấy trên giao diện (loại ô nhập, nhãn, nút). Đây là thông tin bất kỳ tester nào cũng có khi bắt đầu thiết kế.
- **Không**: Kết quả SV đã nhập thử. Không đưa cho AI để phần AI gap analysis (S8) còn trung thực. Điểm nào vẫn chưa rõ thì ghi thành **giả định** ở S2.

| # | Câu hỏi | Liên quan | Trả lời sau S0 | Đưa vào prompt S1–S4 |
|---|---|---|---|---|
| Q1 | `discount_value` loại `percent` có giới hạn trên không (ví dụ tối đa 100)? SRS chỉ yêu cầu "dương" | FR17-R07 | Giao diện không ghi giới hạn (placeholder "Giá trị % (VD: 10)"). Đã thử ở S0 (E01) | Chỉ phần giao diện |
| Q2 | `discount_value` có nhận số thập phân không (ví dụ 10.5% hoặc 0.01 ₫)? | FR17-R07 | Giao diện không ghi. Đã thử ở S0 (E02) | Không |
| Q3 | `min_order_amount`, `max_uses_per_user` có nhận số thập phân không? Có giới hạn trên không? | FR17-R09, R10 | Đã thử ở S0 (E03, E04). Giới hạn trên: Chưa thử | Không |
| Q4 | `code` có giới hạn độ dài, ký tự cho phép (chữ, số, ký tự đặc biệt, khoảng trắng) không? Có phân biệt hoa/thường khi kiểm tra trùng không? | FR17-R04, R05 | Giao diện không ghi giới hạn (placeholder "Mã coupon (VD: SAVE10)"). Đã thử ở S0 (E05, E07). Độ dài, khoảng trắng, trùng hoa/thường: Chưa thử | Chỉ phần giao diện |
| Q5 | `expired_at` có được là ngày trong quá khứ, hoặc là hôm nay không? Định dạng ngày là gì? | FR17-R08 | Giao diện: Ô chọn ngày, nhập theo `mm/dd/yyyy`, bảng hiển thị `yyyy-mm-dd`; khi mở lịch, các ngày trước hôm nay không bị làm mờ (ảnh `S0_06`). Có lưu được ngày quá khứ, hôm nay hay không: Chưa ghi nhận | Có |
| Q6 | Admin có sửa được mã không? FR-17 chỉ ghi Thêm / Xem / Xóa | FR17-R01–R03 | Không có nút sửa | Có |
| Q7 | Xóa mã có hộp thoại xác nhận không? (FR-24 chỉ yêu cầu cho xóa sản phẩm trong giỏ) | FR17-R03 | Đã thử ở S0 (E06) | Không |
| Q8 | Trường `is_active` (FR-09, C1) có nhập được trên form không, và giá trị mặc định khi tạo mới là gì? | FR-09 | Form và bảng **không có** trường `is_active` (cột "Hết hạn" là `expired_at`, không phải `is_active`). Admin không bật/tắt mã được trên giao diện | Có |

---

## 4. Khám phá giao diện

Bản SV điền ban đầu nằm ở commit `[C-FR17][S0] Record UI exploration and screenshots`. Bảng dưới đây được viết lại sau khi đối chiếu với ảnh chụp trong `screenshots/`.

### 4.1 Trang quản lý mã giảm giá

| Mục | Quan sát | Ảnh |
|---|---|---|
| Đăng nhập | Trang đăng nhập Web Admin `http://localhost:5174` | `S0_01` |
| Đường dẫn tới trang | Menu bên trái gồm: Dashboard, Danh mục, Sản phẩm, **Mã Giảm Giá**, Đơn hàng, Người dùng, Đăng xuất. URL giữ nguyên `http://localhost:5174/` khi chuyển trang | `S0_02`, `S0_03` |
| Tiêu đề | Tiêu đề trang: "Quản lý Mã Giảm Giá". Tiêu đề khung form: "Tạo mã giảm giá mới". Tên app ở thanh bên: "EShop Admin" | `S0_03` |
| Bảng danh sách | Các cột: Mã, Loại, Giá trị, Đơn tối thiểu, Hết hạn, Giới hạn/người, Hành động | `S0_03` |
| Cách hiển thị | Tiền: `300,000 ₫` (phân cách hàng nghìn bằng dấu phẩy). Ngày: `yyyy-mm-dd`. Mã: Chữ hoa, màu cam | `S0_03` |
| Ô chọn ngày | Mở lịch: Các ngày trước hôm nay (18/10/2026) không bị làm mờ, có nút "Clear" và "Today" | `S0_06` |

### 4.2 Dữ liệu mẫu đang có (ảnh `S0_03`)

| Mã | Loại | Giá trị | Đơn tối thiểu | Hết hạn | Giới hạn/người |
|---|---|---|---|---|---|
| `SAVE10` | Phần trăm | 10% | 300,000 ₫ | 2099-12-31 | 1 lần |
| `BIGBUY` | Cố định | 50,000 ₫ | 500,000 ₫ | 2099-12-31 | 1 lần |
| `VIP100` | Cố định | 100,000 ₫ | 300,000 ₫ | 2099-12-31 | 2 lần |
| `EXPIRED` | Phần trăm | 20% | 100,000 ₫ | "Hết hạn" (chữ đỏ, không hiện ngày) | 1 lần |

Khớp với bảng mã mẫu ở FR-09. Riêng `EXPIRED` không hiện ngày hết hạn (FR-09 ghi 2020-01-01) mà hiện chữ "Hết hạn".

### 4.3 Form "Tạo mã giảm giá mới" (ảnh `S0_03`, `S0_04`, `S0_05`, `S0_06`)

Form **không có nhãn**, chỉ có placeholder (chữ mờ trong ô, biến mất khi gõ). Không trường nào có dấu `*`.

| # | Placeholder / nội dung hiển thị | Loại ô | Giá trị mặc định |
|---|---|---|---|
| (1) | "Mã coupon (VD: SAVE10)" | Ô chữ | Trống |
| (2) | Dropdown, 2 lựa chọn: "Phần trăm (%)", "Số tiền cố định (₫)" | Dropdown | "Phần trăm (%)" |
| (3) | "Giá trị % (VD: 10)" | Ô số | Trống |
| (4) | "Đơn tối thiểu (₫)" | Ô số | `0` |
| (5) | `mm/dd/yyyy` | Ô chọn ngày | Trống |
| (6) | "Số lần dùng tối đa/người" | Ô số | `1` |

Ảnh `S0_04` chụp sau khi SV tự xóa giá trị mặc định ở (4) và (6) để xem placeholder.

### 4.4 Nút (ảnh `S0_07_nut_thao_tac_tao_ma`, `S0_07_nut_thao_tac_xoa`)

| Nút | Vị trí | Màu |
|---|---|---|
| "Tạo mã" | Dưới form | Cam |
| "Xóa" | Cột Hành động, mỗi dòng một nút | Đỏ |

Không có nút sửa.

**Điểm cần đối chiếu với đặc tả ở S6** (mới là quan sát, chưa kết luận là lỗi):

- Không trường bắt buộc nào có dấu `*` (FR-22, FR17-R12).
- Nút "Tạo mã" màu cam, trong khi FR-21 yêu cầu nút hành động tích cực màu xanh dương (FR17-R14).
- Ô (3) luôn ghi "Giá trị %" dù loại có thể là số tiền cố định: Chưa ghi nhận placeholder có đổi khi chọn "Số tiền cố định (₫)" không.
- Ngày nhập theo `mm/dd/yyyy` nhưng hiển thị `yyyy-mm-dd`.
