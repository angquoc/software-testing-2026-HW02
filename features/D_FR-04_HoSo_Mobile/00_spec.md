# S0: Trích đặc tả và khảo sát giao diện (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S0 (Trích đặc tả, khảo sát giao diện; chuẩn bị cho Step 1 của slide S04)
- Thời gian tạo: 2026-10-21 06:50 (UTC+07:00)
- Căn cứ: `Homeworks/eshop-sut/README.md` (SRS, mục 1, FR-02, FR-04, FR-20 đến FR-24, mục 9), `Homeworks/eshop-sut/api_specification.md` (mục 2), `Homeworks/HW02/WORKFLOW.md`, `Homeworks/HW02/README.md`, đề bài `2026.HW02.Domain Testing_En.md` (mục 4, 5)
- Nền tảng: Mobile. Ứng dụng EShop chạy bằng Expo Go trên Android, thiết bị Samsung Galaxy S21 Ultra
- Tài khoản khảo sát: `test@eshop.com` (mật khẩu theo SRS mục 1). Không dùng chức năng đăng ký
- Cách điền bảng quan sát (theo yêu cầu của sinh viên, khác WORKFLOW mục 3.1 bước 2): Sinh viên chỉ chụp ảnh theo danh sách ở mục 6; AI điền bảng quan sát từ ảnh ở pha 3, mỗi ô ghi nguồn "AI từ ảnh". Ô nào ảnh không cho thấy thì AI để trống và yêu cầu chụp thêm, không suy đoán

---

## 1. Cách làm

- Trích **nguyên văn** các đoạn đặc tả liên quan, ghi nguồn. Phần trích đặt sau dấu `>` và giữ nguyên ký tự gốc (kể cả dấu "–" trong "10–11" và các ký tự mà quy tắc định dạng không cho dùng).
- Tách thành yêu cầu có mã `FR04-Rnn`, mỗi mã một điều kiện kiểm được. Chia 4 nhóm: Chính (FR-04), phụ (yêu cầu giao diện chung áp cho màn hình Hồ sơ trên Mobile), API, tham khảo (bảo mật). Yêu cầu chung không áp dụng cho màn hình này ghi riêng kèm lý do.
- Câu hỏi mở `Qnn`: Chỉ hỏi, không trả lời bằng cách đoán. Cột "Có thể làm rõ bằng" chỉ nhận "Quan sát S0", "Chạy thử S6", "Không có trong đặc tả".
- Bảng quan sát `Onn`: Chỉ hỏi những gì nhìn thấy được mà không cần gõ dữ liệu. Trên Mobile được chạm vào ô để xem loại bàn phím, nhưng **không gõ** và **không bấm nút Lưu** (hoặc nút tương đương).

## 2. Trích nguyên văn đặc tả

### 2.1 FR-04 (SRS mục 2)

> ### FR-04: Quản lý hồ sơ cá nhân
>
> - Người dùng đã đăng nhập có thể cập nhật: **Họ Tên**, **Số điện thoại**, **Địa chỉ giao hàng mặc định**.
> - **Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số.
> - Email không được phép thay đổi qua giao diện.
> - Người dùng chỉ có thể cập nhật hồ sơ của chính mình; không thể tự thay đổi thuộc tính `role`.

### 2.2 Dữ liệu mẫu (SRS mục 1)

> | Mobile App   | React Native + Expo         | IP LAN của máy chủ      |
>
> **Tài khoản mặc định:**
>
> - Admin: `admin@eshop.com` / `Admin123!`
> - User test: `test@eshop.com` / `Test1234!`

Ghi chú: SRS không nêu Họ Tên, Số điện thoại, Địa chỉ giao hàng ban đầu của tài khoản `test@eshop.com` (xem Q23).

### 2.3 Phân hệ Mobile (SRS mục 7)

> ### FR-20: Tính năng Mobile
>
> - Đầy đủ các chức năng: Xem sản phẩm, Đăng nhập, Đăng xuất, Đăng ký, Giỏ hàng, Thanh toán, Hồ sơ, Lịch sử đơn hàng.

### 2.4 Yêu cầu giao diện chung (SRS mục 8, chỉ trích các dòng có thể liên quan tới màn hình Hồ sơ)

> ### FR-21: Tiêu chuẩn Giao diện Chung
>
> - **Nhất quán ngôn ngữ**: Toàn bộ giao diện dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn).
> - **Nhất quán màu sắc**: Các nút hành động tích cực (Submit, Mua hàng) dùng màu xanh dương. Các nút nguy hiểm/hủy bỏ dùng màu đỏ.
> - **Nhất quán đơn vị tiền**: Luôn dùng ký hiệu `₫` với định dạng phân cách hàng nghìn.
> - **Tiêu đề trang**: Mỗi trang có đúng 1 thẻ `<h1>` mô tả nội dung trang.
> - **Tab Order**: Thứ tự focus theo Tab phải đi từ trên xuống dưới, trái sang phải.
>
> ### FR-22: Form Requirements
>
> - Tất cả trường bắt buộc phải có ký hiệu `*` bên cạnh nhãn.
> - Trường Email phải dùng `type="email"`.
> - Trường Mật khẩu phải dùng `type="password"` (không hiển thị rõ).
> - Thông báo lỗi phải xuất hiện **trên** nút submit, không phải bên dưới.
> - Các form có từ 2 bước trở lên phải có **Step Indicator** rõ ràng.
>
> ### FR-23: Navigation Requirements
>
> - Thanh điều hướng (Navbar) phải **highlight** trang đang được chọn.
> - Nút Đăng xuất phải nhãn là "Đăng xuất" (không phải "Thoát").

### 2.5 API (api_specification.md mục 2)

> ## 2. Người dùng (Users)
>
> *Lưu ý: Các API dưới đây yêu cầu truyền Token ở Header: `Authorization: Bearer <token>`*
>
> ### 2.1 Lấy thông tin cá nhân
> - **Endpoint:** `GET /api/users/me`
>
> ### 2.2 Cập nhật hồ sơ cá nhân
> - **Endpoint:** `PUT /api/users/me`
> - **Mô tả:** Chỉ cho phép cập nhật thông tin cá nhân cơ bản.
> - **Body (JSON):**
>   ```json
>   {
>     "name": "Nguyen Van A",
>     "shipping_address": "123 Le Loi, Q1, TP.HCM",
>     "phone": "0912345678"
>   }
>   ```

Liên quan (SRS FR-02, cách lấy token để gọi API):

> - Đăng nhập thành công trả về JWT Token. Token được lưu phía client và gửi kèm tất cả các yêu cầu có xác thực qua header `Authorization: Bearer <token>`.

### 2.6 Bảo mật tham khảo (SRS mục 9, Yêu cầu Bảo mật)

> | SEC-02 | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ.                                                          |
> | SEC-04 | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. |
> | SEC-05 | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp.                                         |
> | SEC-06 | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client.                                        |

## 3. Danh sách yêu cầu có mã

### 3.1 Nhóm chính (FR-04)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR04-R01 | Người dùng đã đăng nhập cập nhật được Họ Tên | FR-04 dòng 1 | |
| FR04-R02 | Người dùng đã đăng nhập cập nhật được Số điện thoại | FR-04 dòng 1 | |
| FR04-R03 | Người dùng đã đăng nhập cập nhật được Địa chỉ giao hàng mặc định | FR-04 dòng 1 | |
| FR04-R04 | Số điện thoại hợp lệ phải bắt đầu bằng số `0` | FR-04 dòng 2 | Số điện thoại không bắt đầu bằng `0` bị từ chối (hệ quả của chữ "hợp lệ") |
| FR04-R05 | Số điện thoại hợp lệ gồm từ 10 đến 11 chữ số | FR-04 dòng 2 | Cách đếm và ký tự không phải chữ số: Q06, Q07 |
| FR04-R06 | Email không thay đổi được qua giao diện | FR-04 dòng 3 | Giao diện có thể hiển thị Email ở dạng không sửa được, hoặc không hiển thị (Q12) |
| FR04-R07 | Người dùng chỉ cập nhật được hồ sơ của chính mình | FR-04 dòng 4 | Trên giao diện, người dùng không chọn được hồ sơ người khác; kiểm chủ yếu qua API (Q15) |
| FR04-R08 | Người dùng không tự thay đổi được thuộc tính `role` | FR-04 dòng 4 | Giao diện có thể không có ô `role`; kiểm qua API (FR04-R19) |

### 3.2 Nhóm phụ (giao diện chung áp cho màn hình Hồ sơ trên Mobile)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR04-R09 | Ứng dụng Mobile có chức năng Hồ sơ | FR-20 | Kiểm bằng việc mở được màn hình Hồ sơ |
| FR04-R10 | Toàn bộ giao diện màn hình Hồ sơ dùng tiếng Việt (trừ thuật ngữ kỹ thuật chuẩn) | FR-21 | Gồm cả thông báo thành công, thông báo lỗi (S6) |
| FR04-R11 | Nút hành động tích cực trên màn hình Hồ sơ (ví dụ nút lưu) dùng màu xanh dương | FR-21 | |
| FR04-R12 | Nút nguy hiểm hoặc hủy bỏ trên màn hình Hồ sơ dùng màu đỏ | FR-21 | Chỉ áp dụng nếu màn hình có nút loại này (O06, O19) |
| FR04-R13 | Mọi trường bắt buộc có ký hiệu `*` bên cạnh nhãn | FR-22 | Đặc tả không nói trường nào của hồ sơ là bắt buộc (Q01, Q05, Q10) |
| FR04-R14 | Thông báo lỗi xuất hiện phía trên nút submit (nút lưu), không phải bên dưới | FR-22 | Chỉ thấy khi có lỗi (S6) |
| FR04-R15 | Thanh điều hướng làm nổi (highlight) mục đang được chọn khi ở màn hình Hồ sơ | FR-23 | Đặc tả viết "Navbar" cho Web; trên Mobile hiểu là thanh điều hướng của ứng dụng (thanh tab hoặc tương đương), nếu có (O02) |
| FR04-R16 | Nút đăng xuất, nếu nằm trên màn hình Hồ sơ, có nhãn "Đăng xuất" (không phải "Thoát") | FR-23 | Chỉ kiểm nhãn; chức năng đăng xuất thuộc feature khác. Không áp dụng nếu nút không nằm trên màn hình Hồ sơ |

### 3.3 Nhóm API

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR04-R17 | `GET /api/users/me` trả thông tin cá nhân của người dùng đang đăng nhập | API mục 2.1 | Đặc tả không mô tả cấu trúc phản hồi (Q20) |
| FR04-R18 | `PUT /api/users/me` cập nhật hồ sơ với các trường `name`, `shipping_address`, `phone` | API mục 2.2 | |
| FR04-R19 | `PUT /api/users/me` chỉ cho phép cập nhật thông tin cá nhân cơ bản | API mục 2.2 | Đặc tả không định nghĩa "cơ bản"; liên quan `email` (Q13) và `role` (Q14) |
| FR04-R20 | Các API mục 2 (Users) yêu cầu header `Authorization: Bearer <token>` | API mục 2, SEC-02 | Gọi không có token hoặc token sai thì không được trả hoặc sửa hồ sơ (phản hồi cụ thể: Q20) |

### 3.4 Nhóm tham khảo (bảo mật)

| Mã | Yêu cầu | Nguồn | Ghi chú |
|---|---|---|---|
| FR04-R21 | API cập nhật hồ sơ không cho phép thay đổi trường `role` từ client | SEC-06 | Là cách kiểm FR04-R08 qua API |
| FR04-R22 | Dữ liệu người dùng nhập (Họ Tên, Địa chỉ) khi hiển thị lại được hiển thị an toàn, không thực thi như mã | SEC-04 | SEC-04 viết theo Web (`innerHTML`); trên Mobile chỉ quan sát được việc chuỗi có thẻ HTML hiển thị nguyên văn hay không |
| FR04-R23 | Truy vấn CSDL dùng Parameterized Query | SEC-05 | Không quan sát trực tiếp bằng hộp đen; chỉ suy ra qua hành vi khi nhập chuỗi có ký tự đặc biệt của SQL (ví dụ dấu nháy đơn) |

### 3.5 Yêu cầu chung không áp dụng cho màn hình này

| Yêu cầu | Nguồn | Lý do không áp dụng |
|---|---|---|
| Đúng 1 thẻ `<h1>` | FR-21, FR-05 | Ứng dụng React Native không có thẻ HTML; không kiểm được bằng hộp đen trên Mobile. Tiêu đề màn hình chỉ ghi nhận ở O03 |
| Tab Order | FR-21 | Thao tác bằng chạm, không có phím Tab; thứ tự chuyển ô bằng nút trên bàn phím ảo (nếu có) không phải yêu cầu của đặc tả |
| Ký hiệu `₫` | FR-21 | Màn hình Hồ sơ không có số tiền (nếu O05 thấy có số tiền thì xét lại) |
| `type="email"`, `type="password"` | FR-22 | Không có HTML; Email không sửa được ở màn hình này (FR04-R06); FR-04 không có trường mật khẩu |
| Step Indicator | FR-22 | Áp cho form từ 2 bước; nếu quan sát thấy form sửa hồ sơ có nhiều bước thì xét lại |
| Badge giỏ hàng, Breadcrumb | FR-23 | Thuộc Giỏ hàng, Thanh toán, Chi tiết sản phẩm |
| Toast thêm giỏ, dialog xóa item, Empty State, `alt` ảnh sản phẩm | FR-24 | Thuộc các màn hình sản phẩm và giỏ hàng |

## 4. Câu hỏi mở

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| **Họ Tên** | | | |
| Q01 | Họ Tên có bắt buộc không? Lưu với Họ Tên rỗng thì hệ thống chấp nhận hay từ chối? | FR04-R01, FR04-R13 | Quan sát S0 (dấu `*`), Chạy thử S6 |
| Q02 | Họ Tên có độ dài tối thiểu, tối đa không? | FR04-R01 | Không có trong đặc tả |
| Q03 | Họ Tên cho phép những ký tự nào: Chữ tiếng Việt có dấu, chữ số, dấu câu, ký tự đặc biệt, emoji? | FR04-R01 | Không có trong đặc tả |
| Q04 | Khoảng trắng ở đầu, cuối, nhiều dấu cách liền nhau ở giữa, Họ Tên chỉ gồm khoảng trắng: Hệ thống cắt, giữ nguyên hay từ chối? | FR04-R01 | Không có trong đặc tả |
| **Số điện thoại** | | | |
| Q05 | Số điện thoại có bắt buộc không? Xóa trống Số điện thoại rồi lưu thì chấp nhận hay từ chối? | FR04-R02, FR04-R13 | Quan sát S0 (dấu `*`), Chạy thử S6 |
| Q06 | Ký tự không phải chữ số (dấu cách, `-`, `.`, `(`, `)`, dạng `+84...`) bị từ chối, hay được bỏ đi trước khi kiểm? | FR04-R04, FR04-R05 | Không có trong đặc tả |
| Q07 | "Từ 10–11 chữ số" có tính cả chữ số `0` đầu tiên không? | FR04-R05 | Không có trong đặc tả |
| Q08 | Khoảng trắng ở đầu, cuối Số điện thoại: Cắt hay từ chối? | FR04-R05 | Không có trong đặc tả |
| Q09 | Ngoài chữ số `0` đầu, hệ thống có kiểm đầu số theo nhà mạng Việt Nam (ví dụ `09`, `03`) không, hay `00...` cũng hợp lệ? | FR04-R04 | Không có trong đặc tả |
| **Địa chỉ giao hàng mặc định** | | | |
| Q10 | Địa chỉ có bắt buộc không? Có độ dài tối đa không? Cho phép những ký tự nào (dấu phẩy, `/`, xuống dòng)? | FR04-R03, FR04-R13 | Quan sát S0 (dấu `*`, ô một dòng hay nhiều dòng), Không có trong đặc tả |
| Q11 | Khoảng trắng ở đầu, cuối, Địa chỉ chỉ gồm khoảng trắng: Cắt, giữ nguyên hay từ chối? | FR04-R03 | Không có trong đặc tả |
| **Email, role, quyền** | | | |
| Q12 | Màn hình Hồ sơ hiển thị Email ở dạng nào: Ô không sửa được, chữ thường, hay không hiển thị? | FR04-R06 | Quan sát S0 |
| Q13 | Đặc tả chỉ cấm đổi Email "qua giao diện". Gửi `email` trong `PUT /api/users/me` thì hệ thống bỏ qua, từ chối hay đổi Email? | FR04-R06, FR04-R19 | Không có trong đặc tả |
| Q14 | Gửi `role` trong `PUT /api/users/me`: Hệ thống bỏ qua trường đó (vẫn cập nhật các trường khác) hay từ chối cả yêu cầu? | FR04-R08, FR04-R21 | Không có trong đặc tả |
| Q15 | API dùng `/me`, không có mã người dùng trên đường dẫn. Gửi thêm `id` hoặc `user_id` của người khác trong body thì hệ thống làm gì? Có cách nào khác để thử cập nhật hồ sơ người khác không? | FR04-R07 | Không có trong đặc tả |
| **Hành vi chung khi lưu** | | | |
| Q16 | Gửi `PUT /api/users/me` thiếu một trường (ví dụ chỉ có `name`): Trường không gửi giữ nguyên, bị xóa, hay yêu cầu bị từ chối? | FR04-R18 | Không có trong đặc tả |
| Q17 | Thông báo khi lưu thành công và khi bị từ chối: Câu chữ, hình thức (hộp thoại, toast, chữ dưới ô), vị trí? | FR04-R10, FR04-R14 | Chạy thử S6 |
| Q18 | Nhiều trường sai cùng lúc: Báo tất cả lỗi hay chỉ lỗi đầu tiên? | FR04-R14 | Chạy thử S6 |
| Q19 | Khi bị từ chối: Dữ liệu đã nhập có giữ lại trong ô không? Dữ liệu cũ trên hệ thống có giữ nguyên không (không lưu một phần)? | FR04-R01 đến FR04-R05 | Chạy thử S6 |
| Q20 | Phản hồi API khi thành công và thất bại (mã HTTP, nội dung, cấu trúc `GET /api/users/me`) là gì? | FR04-R17 đến FR04-R20 | Không có trong đặc tả |
| Q21 | Sau khi lưu thành công, ứng dụng làm gì: Ở lại form, quay về chế độ xem, cập nhật giá trị hiển thị ngay? | FR04-R01 đến FR04-R03 | Chạy thử S6 |
| Q22 | Có nút hủy hoặc bỏ thay đổi không? Rời màn hình khi chưa lưu thì thay đổi bị bỏ hay được giữ? | FR04-R12 | Quan sát S0 (có nút hay không), Chạy thử S6 (hành vi) |
| Q23 | Giá trị ban đầu của Họ Tên, Số điện thoại, Địa chỉ của tài khoản `test@eshop.com` là gì? Số điện thoại ban đầu (nếu có) có hợp lệ theo FR04-R04, FR04-R05 không? | FR04-R01 đến FR04-R05 | Quan sát S0 |
| Q24 | Ngoài Họ Tên, Email, Số điện thoại, Địa chỉ, màn hình Hồ sơ có hiển thị hay cho sửa thông tin khác không (vai trò, mật khẩu, ảnh đại diện)? | FR04-R08, FR04-R19 | Quan sát S0 |
| Q25 | Phiên đăng nhập hết hạn hoặc token không hợp lệ khi đang ở màn hình Hồ sơ: Ứng dụng hiển thị gì khi lưu? | FR04-R20 | Chạy thử S6 |

## 5. Bảng quan sát

Cột "Giá trị quan sát" và "Nguồn" để trống; AI điền ở pha 3 từ ảnh sinh viên chụp và ghi nguồn "AI từ ảnh". Cột "Ảnh" ghi tên file theo danh sách ở mục 6.

| Mã | Nhóm | Mục quan sát | Giá trị quan sát | Nguồn | Ảnh |
|---|---|---|---|---|---|
| O01 | Đường vào | Màn hình đầu tiên sau khi đăng nhập: Tiêu đề, thanh điều hướng (vị trí, các mục, nhãn nguyên văn, biểu tượng) | | | |
| O02 | Đường vào | Cách mở màn hình Hồ sơ (mục trên thanh điều hướng, nút, menu); mục đang chọn có được làm nổi không (màu, đậm) khi ở màn hình Hồ sơ | | | |
| O03 | Đường vào | Tiêu đề màn hình Hồ sơ (thanh tiêu đề phía trên) và các tiêu đề khác nhìn thấy | | | |
| O04 | Chế độ xem | Màn hình Hồ sơ khi vừa mở là chế độ xem hay đã là form sửa | | | |
| O05 | Chế độ xem | Các thông tin hiển thị: Nhãn nguyên văn và giá trị đang hiển thị (Họ Tên, Email, Số điện thoại, Địa chỉ, và thông tin khác nếu có) | | | |
| O06 | Chế độ xem | Các nút và liên kết: Nhãn nguyên văn, màu nền, màu chữ, vị trí (ví dụ nút sửa, nút đăng xuất, lịch sử đơn hàng, nếu có) | | | |
| O07 | Chế độ xem | Chữ không phải tiếng Việt nhìn thấy trên màn hình Hồ sơ | | | |
| O08 | Form sửa | Cách vào form sửa (bấm nút nào, hay đã ở sẵn); tiêu đề form; dòng hướng dẫn hiển thị sẵn | | | |
| O09 | Ô Họ Tên | Nhãn nguyên văn; dấu `*`; placeholder; giá trị đang có; loại ô (một dòng, nhiều dòng); biểu tượng trong ô | | | |
| O10 | Ô Họ Tên | Loại bàn phím khi chạm vào ô (chữ, số, email); bàn phím có tự viết hoa chữ đầu, có thanh gợi ý từ không | | | |
| O11 | Email | Email có hiển thị không; dạng hiển thị (ô nhập, ô mờ hoặc xám, chữ thường); nhãn nguyên văn; giá trị | | | |
| O12 | Email | Chạm vào vùng Email: Bàn phím có hiện không, con trỏ có xuất hiện không (không gõ) | | | |
| O13 | Ô Số điện thoại | Nhãn nguyên văn; dấu `*`; placeholder; giá trị đang có; loại ô; biểu tượng trong ô; chữ gợi ý định dạng hiển thị sẵn | | | |
| O14 | Ô Số điện thoại | Loại bàn phím khi chạm vào ô (chữ, số, bàn phím điện thoại); bàn phím có phím dấu cách, `+`, `-`, `.` không | | | |
| O15 | Ô Địa chỉ | Nhãn nguyên văn; dấu `*`; placeholder; giá trị đang có; loại ô (một dòng, nhiều dòng); biểu tượng trong ô | | | |
| O16 | Ô Địa chỉ | Loại bàn phím khi chạm vào ô; có phím xuống dòng hay phím xong (Done) | | | |
| O17 | Form sửa | Ô hoặc thông tin khác trong form (vai trò, mật khẩu, ảnh đại diện...); có hay không | | | |
| O18 | Form sửa | Nút lưu: Nhãn nguyên văn, màu nền, màu chữ, vị trí (không bấm) | | | |
| O19 | Form sửa | Nút hủy, quay lại hoặc bỏ thay đổi: Có hay không; nhãn nguyên văn, màu nền, màu chữ, vị trí | | | |
| O20 | Form sửa | Khi bàn phím mở, nút lưu có bị che không (chỉ ghi nhận, không bấm) | | | |

## 6. Ảnh cần chụp

Quy ước: `screenshots/S0_NN_<nội dung>.png`, chụp cả màn hình điện thoại (có thanh trạng thái; có thể che biểu tượng thông báo cá nhân). Chỉ quan sát: Không gõ vào ô nào, không bấm nút lưu. Màn hình dài thì cuộn và chụp thêm, thêm hậu tố `_cuon` (ví dụ `S0_02_ho_so_cuon.png`).

| Ảnh | Nội dung phải thấy | Dùng cho |
|---|---|---|
| `S0_01_sau_dang_nhap.png` | Màn hình ngay sau khi đăng nhập bằng `test@eshop.com`, thấy toàn bộ thanh điều hướng | O01 |
| `S0_02_ho_so.png` | Màn hình Hồ sơ vừa mở: Thanh tiêu đề, toàn bộ nội dung, thanh điều hướng với mục đang chọn | O02 đến O07 |
| `S0_03_form_sua.png` | Form sửa hồ sơ, chưa chạm vào ô nào, thấy đủ các ô và nút lưu, nút hủy (nếu có). Nếu màn hình Hồ sơ đã là form sửa thì không cần ảnh này, chỉ báo lại | O08, O09, O11, O13, O15, O17 đến O19 |
| `S0_04_ban_phim_ho_ten.png` | Đã chạm vào ô Họ Tên, bàn phím đang mở, chưa gõ | O10, O20 |
| `S0_05_cham_email.png` | Đã chạm vào vùng Email, chụp dù bàn phím có hiện hay không | O12 |
| `S0_06_ban_phim_sdt.png` | Đã chạm vào ô Số điện thoại, bàn phím đang mở, chưa gõ | O14 |
| `S0_07_ban_phim_dia_chi.png` | Đã chạm vào ô Địa chỉ, bàn phím đang mở, chưa gõ | O16 |

Sau khi chụp xong: Thoát form bằng nút hủy hoặc quay lại (không bấm lưu). Nếu ứng dụng hỏi có bỏ thay đổi không thì chụp thêm `S0_08_hoi_bo_thay_doi.png` (dùng cho Q22) rồi chọn bỏ.

## 7. Điểm cần sinh viên quyết định

Theo yêu cầu của sinh viên, các điểm nhỏ dưới đây đã **áp tạm phương án AI đề xuất** trong bản này; sinh viên duyệt ở lượt review.

| # | Vấn đề | Các lựa chọn | Đã áp tạm |
|---|---|---|---|
| 1 | Phạm vi trích đặc tả | (a) FR-04 làm trọng tâm, yêu cầu giao diện chung làm nhóm phụ, API, bảo mật làm nhóm tham khảo; (b) chỉ FR-04 và API | (a) |
| 2 | FR-23 (làm nổi mục trên thanh điều hướng, nhãn "Đăng xuất") viết cho Web | (a) Giữ làm nhóm phụ (FR04-R15, FR04-R16), chỉ kiểm nếu thành phần đó có trên màn hình Hồ sơ; (b) bỏ khỏi phạm vi | (a) |
| 3 | Kênh API: Ứng dụng Mobile dùng chung backend với Web | (a) Giữ nhóm API (Postman hoặc cURL) để kiểm những gì giao diện không gửi được (`role`, `email`, không có token); (b) chỉ kiểm qua ứng dụng | (a) |
| 4 | FR-04 trên Web | (a) Ngoài phạm vi feature D, không khảo sát; (b) khảo sát thêm để so sánh | (a) |

## 8. Ghi chú cho bước sau

- **Pha 3 S0:** Kiểm tra đủ 7 ảnh (và ảnh `_cuon`, `S0_08` nếu có) trước khi điền bảng. Mục nào ảnh không cho thấy thì yêu cầu chụp thêm, không điền bằng suy đoán. Điền Q23, Q24, Q12 và phần quan sát của Q01, Q05, Q10, Q22 từ ảnh.
- **Kiểm chứng tác động (S1):** Trong phạm vi FR-04, dấu hiệu lưu thành công là giá trị mới hiển thị lại trên màn hình Hồ sơ sau khi mở lại màn hình, hoặc `GET /api/users/me` trả giá trị mới. Không dùng màn hình Thanh toán (FR-08) để kiểm Địa chỉ giao hàng mặc định, vì thuộc feature khác.
- **Input gián tiếp (S1):** Trạng thái đăng nhập (token có, không, sai), giá trị hồ sơ hiện có (Q23), người dùng nào đang đăng nhập (FR04-R07).
- **Môi trường (S2 đến S4):** Bàn phím của ô Số điện thoại (O14) quyết định ký tự nào gõ được qua ứng dụng; ký tự không gõ được thì xét kiểm qua API hoặc dán. Bàn phím tự viết hoa, gợi ý từ (O10) có thể làm giá trị gửi đi khác giá trị định gõ; ghi tên thiết bị, phiên bản Android, phiên bản Expo Go ở S6.
- **Câu hỏi sẽ thành giả định ở S2:** Q01 đến Q11, Q13 đến Q16, Q18, Q19.
- **Quy mô:** Sinh viên đặt mục tiêu cả bộ khoảng 25 đến 35 test case (S3 và S4 cộng lại). S2 cần giữ số lớp ở mức phủ được trong ngân sách này; S3 cân nhắc gộp lớp hợp lệ và dùng chung test case cho biên ở S4.
- **Dữ liệu:** Mỗi lần chạy ở S6 làm thay đổi hồ sơ của `test@eshop.com`; cần ghi giá trị ban đầu (Q23) để khôi phục hoặc reset dữ liệu mẫu.
