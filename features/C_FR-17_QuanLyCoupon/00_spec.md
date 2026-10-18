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

Các điểm dưới đây sẽ ảnh hưởng tới kết quả mong đợi ở S1–S4. Cần quan sát giao diện (mục 4) trước, chỗ nào vẫn chưa rõ thì ghi thành **giả định** trong test case.

| # | Câu hỏi | Liên quan |
|---|---|---|
| Q1 | `discount_value` loại `percent` có giới hạn trên không (ví dụ tối đa 100)? SRS chỉ yêu cầu "dương" | FR17-R07 |
| Q2 | `discount_value` có nhận số thập phân không (ví dụ 10.5% hoặc 0.01 ₫)? | FR17-R07 |
| Q3 | `min_order_amount`, `max_uses_per_user` có nhận số thập phân không? Có giới hạn trên không? | FR17-R09, R10 |
| Q4 | `code` có giới hạn độ dài, ký tự cho phép (chữ, số, ký tự đặc biệt, khoảng trắng) không? Có phân biệt hoa/thường khi kiểm tra trùng không? | FR17-R04, R05 |
| Q5 | `expired_at` có được là ngày trong quá khứ, hoặc là hôm nay không? Định dạng ngày là gì? | FR17-R08 |
| Q6 | Admin có sửa được mã không? FR-17 chỉ ghi Thêm / Xem / Xóa | FR17-R01–R03 |
| Q7 | Xóa mã có hộp thoại xác nhận không? (FR-24 chỉ yêu cầu cho xóa sản phẩm trong giỏ) | FR17-R03 |
| Q8 | Trường `is_active` (FR-09, C1) có nhập được trên form không, và giá trị mặc định khi tạo mới là gì? | FR-09 |

---

## 4. Khám phá giao diện (SV điền)

Đăng nhập `http://localhost:5174` bằng `admin@eshop.com` / `Admin123!`, mở trang quản lý mã giảm giá. Lưu ảnh vào `screenshots/` (`S0_01_danh_sach_coupon.png`, `S0_02_form_them_coupon.png`, ...).

**Chỉ quan sát, chưa nhập dữ liệu sai để thử.** Việc thử là của bước S6.

| Cần ghi lại | Quan sát |
|---|---|
| Đường dẫn tới trang (menu nào, URL) | |
| Tiêu đề trang | |
| Các cột của bảng danh sách | |
| Các mã đang có sẵn | |
| Tên **chính xác** từng trường trên form thêm mã (nhãn hiển thị) | |
| Loại ô nhập của từng trường (ô chữ, ô số, chọn ngày, dropdown) | |
| Trường nào có dấu `*` | |
| Giá trị mặc định của từng trường | |
| Tên nút thêm, nút xóa (chữ hiển thị, màu) | |
| Có nút sửa không (Q6) | |
| Q7 (hộp thoại xác nhận khi xóa): **Không bấm Xóa ở S0.** Nếu không có hộp thoại, mã mẫu sẽ bị xóa thật. Để dành cho S6 | Không áp dụng ở S0 |
| Có trường `is_active` / trạng thái hoạt động không (Q8) | |
| Ghi chú khác | |
