# S0: Trích đặc tả và khảo sát giao diện (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S0 (Trích đặc tả, khảo sát giao diện; chuẩn bị cho Step 1 của slide S04)
- Bản này: Bản S0 sau pha 3 (AI điền bảng quan sát từ ảnh, đối chiếu đặc tả, cập nhật câu hỏi mở). Bản gốc của AI: `ai_raw/S0_khao_sat.md`
- Thời gian tạo bản AI: 2026-10-21 06:50 (UTC+07:00)
- Cập nhật theo ảnh và quyết định của sinh viên: 2026-10-21 07:10 (UTC+07:00). Mục 1 đến 4 giữ nguyên bản AI; mục 5 trở đi viết ở pha 3; thay đổi so với bản AI liệt kê ở mục cuối
- Căn cứ: Như bản AI (`Homeworks/eshop-sut/README.md`, `Homeworks/eshop-sut/api_specification.md`, `Homeworks/HW02/WORKFLOW.md`, `Homeworks/HW02/README.md`, đề bài), cộng 5 ảnh trong `screenshots/` (`S0_01`, `S0_02`, `S0_04`, `S0_06`, `S0_07`) và thông tin sinh viên cung cấp khi gửi ảnh
- Nền tảng: Mobile. Ứng dụng EShop chạy bằng Expo Go trên Android, thiết bị Samsung Galaxy S21 Ultra
- Tài khoản khảo sát: `test@eshop.com` (mật khẩu theo SRS mục 1). Không dùng chức năng đăng ký; không bấm "Cập nhật", không bấm "Thoát"
- Cách điền bảng quan sát (theo yêu cầu của sinh viên, khác WORKFLOW mục 3.1 bước 2): Sinh viên chỉ chụp ảnh; AI điền bảng từ ảnh, cột "Nguồn" ghi "AI từ ảnh". Thông tin sinh viên nói thêm (không có trong ảnh) ghi nguồn "Sinh viên cung cấp". Ô ảnh không cho thấy để trống và liệt kê ở mục 6

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

## 5. Bảng quan sát (đã điền)

Mỗi ô ghi đúng những gì thấy trong ảnh. Chữ trong dấu nháy là nguyên văn trên giao diện.

| Mã | Nhóm | Mục quan sát | Giá trị quan sát | Nguồn | Ảnh |
|---|---|---|---|---|---|
| O01 | Đường vào | Màn hình đầu tiên sau khi đăng nhập: Tiêu đề, thanh điều hướng | Thanh trên cùng nền xanh dương, chữ trắng: Bên trái "EShop Mobile"; bên phải "Chào, Test User" và "Giỏ (0)". Không có thanh tab ở dưới; cuối màn hình là dải nền tối "© 2026 EShop SUT. Dành cho mục đích kiểm thử.". Nội dung: Tiêu đề "Danh sách sản phẩm", ô "Tìm kiếm...", nút "Tìm", các thẻ sản phẩm, dòng "Hiển thị 5 sản phẩm" | AI từ ảnh | `S0_01_sau_dang_nhap.png` |
| O02 | Đường vào | Cách mở màn hình Hồ sơ; mục đang chọn có được làm nổi không | Cách mở: Bấm "Chào, Test User" trên thanh trên. Làm nổi: "Chào, Test User" ở `S0_02` trông giống hệt ở `S0_01` (cùng chữ trắng, không gạch chân, không có nền riêng); không thấy dấu hiệu làm nổi | Sinh viên cung cấp (cách mở); AI từ ảnh (làm nổi) | `S0_01_sau_dang_nhap.png`, `S0_02_ho_so.png` |
| O03 | Đường vào | Tiêu đề màn hình Hồ sơ và các tiêu đề khác | Không có thanh tiêu đề riêng của màn hình; thanh trên vẫn là "EShop Mobile". Khung thứ nhất có tiêu đề "Hồ sơ của bạn"; khung thứ hai phía dưới có tiêu đề "Lịch sử đơn hàng" | AI từ ảnh | `S0_02_ho_so.png` |
| O04 | Chế độ xem | Vừa mở là chế độ xem hay form sửa | Form sửa: Các ô nhập hiện sẵn, không có chế độ xem riêng | AI từ ảnh | `S0_02_ho_so.png` |
| O05 | Chế độ xem | Thông tin hiển thị (nhãn, giá trị) | Từ trên xuống: "Email (Không đổi)" `test@eshop.com`; "Họ Tên" `Test User`; "Số điện thoại" trống (chỉ có placeholder, xem O13); "Địa chỉ giao hàng" trống. Khung "Lịch sử đơn hàng": "Bạn chưa có đơn hàng nào.". Không có số tiền nào trên màn hình | AI từ ảnh | `S0_02_ho_so.png` |
| O06 | Chế độ xem | Các nút và liên kết | "Cập nhật": Nền xanh dương, chữ trắng đậm, rộng hết khung, ngay dưới ô Địa chỉ. "Thoát": Nền đỏ, chữ trắng đậm, rộng hết khung, ngay dưới "Cập nhật". Thanh trên có "Chào, Test User", "Giỏ (0)" dạng chữ trắng, không có nền nút. Trong khung Hồ sơ không có liên kết nào khác | AI từ ảnh | `S0_02_ho_so.png` |
| O07 | Chế độ xem | Chữ không phải tiếng Việt | "EShop Mobile", "EShop SUT" (tên sản phẩm); "Email" (thuật ngữ); `Test User` là dữ liệu của tài khoản, không phải chữ giao diện. Các nhãn, nút, tiêu đề còn lại bằng tiếng Việt | AI từ ảnh | `S0_02_ho_so.png` |
| O08 | Form sửa | Cách vào form; tiêu đề; dòng hướng dẫn | Không phải bấm nút nào, form có sẵn khi mở màn hình; tiêu đề "Hồ sơ của bạn"; không có dòng hướng dẫn | AI từ ảnh | `S0_02_ho_so.png` |
| O09 | Ô Họ Tên | Nhãn, `*`, placeholder, giá trị, loại ô, biểu tượng | Nhãn "Họ Tên"; không có `*`; placeholder không thấy được vì ô đang có giá trị; giá trị `Test User`; ô một dòng (cao bằng ô Email, ô Số điện thoại); không có biểu tượng | AI từ ảnh | `S0_02_ho_so.png` |
| O10 | Ô Họ Tên | Loại bàn phím; tự viết hoa; thanh gợi ý từ | Bàn phím chữ QWERTY có hàng số `1` đến `0` ở trên; phím cách ghi "English (US)"; phím góc phải dưới "H.tất". Chữ trên phím đang là chữ thường, nhưng con trỏ nằm giữa chữ có sẵn nên ảnh này không cho biết có tự viết hoa chữ đầu không. Phía trên bàn phím là thanh công cụ (emoji, bộ nhớ tạm, dịch, cài đặt, thêm), không thấy thanh gợi ý từ | AI từ ảnh | `S0_04_ban_phim_ho_ten.png` |
| O11 | Email | Có hiển thị không; dạng hiển thị; nhãn; giá trị | Có hiển thị. Nhãn "Email (Không đổi)"; ô nền xám nhạt, chữ xám `test@eshop.com`, khác các ô còn lại (nền trắng, chữ đen) | AI từ ảnh | `S0_02_ho_so.png` |
| O12 | Email | Chạm vào vùng Email: Bàn phím có hiện không | Không hiện bàn phím; màn hình giữ nguyên như `S0_02` (không chụp ảnh riêng) | Sinh viên cung cấp | `S0_02_ho_so.png` (màn hình giống) |
| O13 | Ô Số điện thoại | Nhãn, `*`, placeholder, giá trị, loại ô, biểu tượng, chữ gợi ý | Nhãn "Số điện thoại"; không có `*`; placeholder "VD: 0912345678" (chữ xám; ở `S0_06` con trỏ đứng trước chữ "VD", nên ô chưa có giá trị); giá trị trống; ô một dòng; không có biểu tượng; không có chữ gợi ý nào khác | AI từ ảnh | `S0_02_ho_so.png`, `S0_06_ban_phim_sdt.png` |
| O14 | Ô Số điện thoại | Loại bàn phím; có phím dấu cách, `+`, `-`, `.` không | Bàn phím số kiểu điện thoại: Phím `1` đến `9` và `0` (kèm chữ ABC, DEF...), `*`, `#`, `,`, `+` (chữ nhỏ trên phím `0`), phím "*+#", phím xóa, phím "H.tất". Trên trang bàn phím này không thấy phím dấu cách, phím chữ, `-`, `.` | AI từ ảnh | `S0_06_ban_phim_sdt.png` |
| O15 | Ô Địa chỉ | Nhãn, `*`, placeholder, giá trị, loại ô, biểu tượng | Nhãn "Địa chỉ giao hàng" (đặc tả viết "Địa chỉ giao hàng mặc định"); không có `*`; không có placeholder; giá trị trống; ô nhiều dòng (cao khoảng gấp đôi ô Họ Tên); không có biểu tượng | AI từ ảnh | `S0_02_ho_so.png` |
| O16 | Ô Địa chỉ | Loại bàn phím; phím xuống dòng hay phím xong | Bàn phím chữ QWERTY như O10; chữ trên phím in hoa, phím Shift sáng xanh (ô trống, bàn phím đang viết hoa chữ đầu); phím góc phải dưới là phím xuống dòng (mũi tên ↵), không phải "H.tất" | AI từ ảnh | `S0_07_ban_phim_dia_chi.png` |
| O17 | Form sửa | Ô hoặc thông tin khác (vai trò, mật khẩu, ảnh đại diện) | Không có | AI từ ảnh | `S0_02_ho_so.png` |
| O18 | Form sửa | Nút lưu | "Cập nhật": Nền xanh dương, chữ trắng đậm, rộng hết khung, dưới ô Địa chỉ (không bấm) | AI từ ảnh | `S0_02_ho_so.png` |
| O19 | Form sửa | Nút hủy, quay lại, bỏ thay đổi | Không có nút hủy, quay lại hay bỏ thay đổi. Chỉ có "Thoát" (nền đỏ, chữ trắng đậm, dưới "Cập nhật"); chưa biết chức năng vì sinh viên không bấm (Q26) | AI từ ảnh; Sinh viên cung cấp (không bấm) | `S0_02_ho_so.png` |
| O20 | Form sửa | Khi bàn phím mở, nút lưu có bị che không | Ở cả 3 ảnh có bàn phím, bàn phím che phần dưới form: Ô Địa chỉ bị cắt, không thấy "Cập nhật" và "Thoát". Ảnh không cho biết có cuộn được để thấy nút không | AI từ ảnh | `S0_04_ban_phim_ho_ten.png`, `S0_06_ban_phim_sdt.png`, `S0_07_ban_phim_dia_chi.png` |

## 6. Đối chiếu danh sách ảnh

| Ảnh trong danh sách | Trạng thái | Ghi chú |
|---|---|---|
| `S0_01_sau_dang_nhap.png` | Có | Thấy đủ thanh trên và nội dung đầu trang |
| `S0_02_ho_so.png` | Có | Thấy toàn bộ màn hình Hồ sơ tới dải cuối trang; không cần ảnh `_cuon` |
| `S0_03_form_sua.png` | Không cần | Màn Hồ sơ đã là form sửa (O04), đúng điều kiện bỏ ảnh ở bản AI |
| `S0_04_ban_phim_ho_ten.png` | Có | |
| `S0_05_cham_email.png` | Không chụp | Sinh viên cho biết chạm vào không hiện bàn phím, màn hình giống `S0_02` (O12) |
| `S0_06_ban_phim_sdt.png` | Có | |
| `S0_07_ban_phim_dia_chi.png` | Có | |
| `S0_08_hoi_bo_thay_doi.png` | Không áp dụng | Không có nút hủy; sinh viên không bấm "Thoát" |

Không có ô nào trong bảng quan sát còn trống. Không cần chụp thêm cho S0.

## 7. Câu hỏi mở sau quan sát

### 7.1 Trạng thái các câu hỏi Q01 đến Q25

| Mã | Trạng thái | Kết quả quan sát hoặc ghi chú |
|---|---|---|
| Q01 | Vẫn mở | Ô Họ Tên không có `*` (O09). Đặc tả không nói Họ Tên bắt buộc; thành giả định ở S2 |
| Q02 | Vẫn mở | |
| Q03 | Vẫn mở | Bàn phím ghi "English (US)" (O10): Chữ tiếng Việt có dấu có thể phải đổi bàn phím hoặc dán khi chạy S6 |
| Q04 | Vẫn mở | |
| Q05 | Vẫn mở | Ô không có `*` (O13); hồ sơ ban đầu có Số điện thoại trống (Q23). Quan sát này chưa nói hệ thống có chấp nhận lưu khi trống hay không |
| Q06 | Vẫn mở | Bàn phím điện thoại không có phím dấu cách, `-`, `.` (O14): Các ký tự này không gõ trực tiếp được qua ứng dụng; nếu S2 có lớp cho chúng thì kiểm qua API hoặc dán |
| Q07 | Vẫn mở | Placeholder "VD: 0912345678" có 10 chữ số tính cả số `0` đầu; đây là ví dụ, không phải quy tắc, nên chưa trả lời được Q07 |
| Q08 | Vẫn mở | Bàn phím điện thoại không có phím dấu cách (O14) |
| Q09 | Vẫn mở | |
| Q10 | Trả lời một phần | Không có `*`; ô nhiều dòng, bàn phím có phím xuống dòng (O15, O16). Độ dài tối đa, ký tự cho phép, có chấp nhận xuống dòng hay không: Vẫn mở |
| Q11 | Vẫn mở | |
| Q12 | Đã trả lời | Email hiển thị trong ô nền xám, nhãn "Email (Không đổi)" (O11); chạm vào không hiện bàn phím (O12) |
| Q13 | Vẫn mở | |
| Q14 | Vẫn mở | Giao diện không có ô vai trò (O17) |
| Q15 | Vẫn mở | Giao diện không có cách chọn hồ sơ người khác |
| Q16 | Vẫn mở | |
| Q17 | Chưa áp dụng được | Chạy thử S6 |
| Q18 | Chưa áp dụng được | Chạy thử S6 |
| Q19 | Chưa áp dụng được | Chạy thử S6 |
| Q20 | Vẫn mở | Không có trong đặc tả; ghi nhận ở S6 |
| Q21 | Chưa áp dụng được | Chạy thử S6 |
| Q22 | Trả lời một phần | Không có nút hủy hay bỏ thay đổi (O19). Rời màn hình khi chưa lưu thì sao: Chạy thử S6 |
| Q23 | Đã trả lời | Họ Tên `Test User`; Số điện thoại trống; Địa chỉ giao hàng trống (O05). Vế "Số điện thoại ban đầu có hợp lệ không" không áp dụng vì đang trống |
| Q24 | Đã trả lời | Không có thông tin nào khác trong khung Hồ sơ (O17); cùng màn hình có khung "Lịch sử đơn hàng" (thuộc FR-11, ngoài phạm vi) |
| Q25 | Chưa áp dụng được | Chạy thử S6 |

### 7.2 Câu hỏi mới

| Mã | Câu hỏi | Liên quan | Có thể làm rõ bằng |
|---|---|---|---|
| Q26 | Nút "Thoát" làm gì: Đăng xuất, rời màn hình Hồ sơ, hay bỏ thay đổi chưa lưu? | FR04-R12, FR04-R16, Q22 | Chạy thử S6 |
| Q27 | Ứng dụng không có thanh tab; thanh trên ("EShop Mobile", "Chào, Test User", "Giỏ (0)") có được coi là thanh điều hướng theo FR-23 để áp FR04-R15 không? | FR04-R15 | Không có trong đặc tả (sinh viên chốt) |

## 8. Đối chiếu giao diện với đặc tả

### 8.1 Yêu cầu khớp ở mức quan sát

Khớp ở mức nhìn thấy được trong ảnh; vẫn chạy lại ở S6.

| Yêu cầu | Quan sát |
|---|---|
| FR04-R06 | Email hiển thị trong ô nền xám, nhãn "(Không đổi)", chạm không hiện bàn phím (O11, O12). Thử sửa thật (giữ, dán) để S6 |
| FR04-R09 | Mở được màn hình Hồ sơ từ "Chào, Test User" (O02) |
| FR04-R10 | Mọi nhãn, nút, tiêu đề nhìn thấy bằng tiếng Việt, trừ tên sản phẩm và thuật ngữ "Email" (O07). Thông báo thành công, lỗi để S6 |
| FR04-R11 | "Cập nhật" nền xanh dương (O18) |
| FR04-R12 | "Thoát" nền đỏ (O19). Khớp nếu "Thoát" là nút nguy hiểm hoặc hủy bỏ (Q26) |

### 8.2 Khác biệt (chờ xác nhận ở S6, chưa kết luận bug)

| Mã | Yêu cầu | Đặc tả nói | Quan sát thấy | Căn cứ |
|---|---|---|---|---|
| D01 | FR04-R16 (FR-23) | Nút đăng xuất phải có nhãn "Đăng xuất" (không phải "Thoát") | Màn hình Hồ sơ có nút đỏ "Thoát". Nếu S6 xác nhận "Thoát" là đăng xuất (Q26) thì nhãn khác đặc tả | O06, O19, `S0_02_ho_so.png` |
| D02 | FR04-R15 (FR-23) | Thanh điều hướng phải làm nổi trang đang được chọn | Ở màn hình Hồ sơ, "Chào, Test User" không khác gì ở màn hình đầu. Chỉ là khác biệt nếu sinh viên chốt thanh trên là thanh điều hướng (Q27) | O02, `S0_01_sau_dang_nhap.png`, `S0_02_ho_so.png` |
| D03 | FR04-R13 (FR-22) | Mọi trường bắt buộc có `*` bên cạnh nhãn | Không ô nào có `*`. Chỉ là khác biệt nếu S2 chốt trường nào đó là bắt buộc (Q01, Q05, Q10) | O09, O13, O15, `S0_02_ho_so.png` |

### 8.3 Ngoài phạm vi

| Mã | Quan sát | Ghi chú |
|---|---|---|
| N01 | Ở mọi ảnh, giờ và biểu tượng của thanh trạng thái Android nằm đè lên thanh trên của ứng dụng (chồng lên chữ "EShop Mobile") | Không thuộc yêu cầu nào của FR-04; không thiết kế test case |
| N02 | Khung "Lịch sử đơn hàng" ("Bạn chưa có đơn hàng nào.") nằm cùng màn hình Hồ sơ | Thuộc FR-11 |

## 9. Quyết định của sinh viên

| # | Vấn đề | Quyết định |
|---|---|---|
| 1 | Phạm vi trích đặc tả (mục 7 bản AI, điểm 1) | (a) FR-04 làm trọng tâm, yêu cầu giao diện chung làm nhóm phụ, API, bảo mật làm nhóm tham khảo |
| 2 | FR-23 viết cho Web (điểm 2) | (a) Giữ FR04-R15, FR04-R16 làm nhóm phụ, chỉ kiểm nếu thành phần đó có trên màn hình Hồ sơ |
| 3 | Kênh API (điểm 3) | (a) Giữ nhóm API để kiểm `role`, `email`, trường hợp không có token |
| 4 | FR-04 trên Web (điểm 4) | (a) Ngoài phạm vi |
| 5 | Ảnh `S0_03` | Không chụp, vì màn Hồ sơ đã là form sửa |
| 6 | Ảnh `S0_05` | Không chụp; sinh viên cho biết chạm vào Email không hiện bàn phím, màn hình giống `S0_02` |
| 7 | Ảnh `S0_08` | Không chụp; không có nút hủy; không bấm "Thoát" |
| 8 | Cách điền bảng quan sát | AI điền từ ảnh, đánh dấu "AI từ ảnh" (sinh viên yêu cầu từ đầu S0) |

Q26 (chạy thử S6) và Q27 (sinh viên chốt) chưa có quyết định. Q27 được xử lý khi chốt nhóm checklist ở S1 (`ai_raw/S1_input_output.md`, mục "Điểm cần sinh viên quyết định").

## 10. Trả lời câu hỏi khi review

Sinh viên không đặt câu hỏi ở lượt này.

## 11. Kiểm tra mâu thuẫn

| Quyết định hoặc quan sát | Kết quả kiểm tra |
|---|---|
| Quyết định 2 với O06, O19, O02 | Nút "Thoát" có trên màn hình Hồ sơ nên FR04-R16 áp dụng nếu "Thoát" là đăng xuất (Q26). Thanh trên có mặt nên FR04-R15 áp dụng tùy Q27. Không vướng |
| Quyết định 3 với O14 | Thống nhất: Ký tự không gõ được bằng bàn phím điện thoại (dấu cách, `-`, `.`, chữ) có đường API để kiểm |
| Quyết định 6 với FR04-R06 | Không vướng: O12 đã có giá trị từ thông tin sinh viên; việc thử sửa thật Email qua giao diện để S6 |
| Yêu cầu "không bấm Lưu" | Ảnh không có trạng thái sau khi lưu; mọi giá trị ở O05 là dữ liệu ban đầu |

## 12. Ghi chú cho bước sau

- **Tên trên giao diện cho S1:** "Họ Tên", "Số điện thoại", "Địa chỉ giao hàng", "Email (Không đổi)", nút "Cập nhật", nút "Thoát". Giao diện có đủ 3 trường đặc tả cho sửa; `role` có trong đặc tả nhưng không có trên giao diện (chỉ kiểm qua API).
- **Dấu hiệu thành công trong phạm vi FR-04:** Mở lại màn hình Hồ sơ (qua "Chào, Test User") thấy giá trị mới trong ô, hoặc `GET /api/users/me` trả giá trị mới. Không dùng màn Thanh toán, không dựa vào lời chào "Chào, ..." như bằng chứng duy nhất (S1 xét có dùng được không).
- **Giá trị ban đầu:** Họ Tên `Test User`, Số điện thoại trống, Địa chỉ trống. Dùng để khôi phục sau mỗi đợt chạy và để S2 xét lớp "giá trị trống".
- **Môi trường:** Bàn phím điện thoại cho Số điện thoại (O14); bàn phím chữ "English (US)", tự viết hoa chữ đầu ở ô Địa chỉ (O16); bàn phím che nút "Cập nhật" (O20), nên S6 phải ẩn bàn phím trước khi bấm. Ghi phiên bản Android, Expo Go ở S6.
- **Câu hỏi thành giả định ở S2:** Q01 đến Q11, Q13 đến Q16, Q18, Q19.
- **Quy mô:** Mục tiêu cả bộ khoảng 25 đến 35 test case.

## 13. Thay đổi so với bản AI (`ai_raw/S0_khao_sat.md`)

Phạm vi: Chỉ ghi chỗ sinh viên thay đổi hoặc chốt so với bản AI. Việc điền bảng quan sát (mục 5) là đầu vào theo quy trình; các mục 6 đến 8 do AI viết ở pha 3, không phải phần sinh viên sửa.

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| Mục 7 bản AI, điểm 1 | Chốt (a): Phạm vi gồm FR-04, nhóm phụ, API, bảo mật tham khảo | Quyết định của SV | Sinh viên chấp nhận phương án đã áp tạm |
| Mục 7 bản AI, điểm 2 | Chốt (a): Giữ FR04-R15, FR04-R16, chỉ kiểm khi có trên màn hình Hồ sơ | Quyết định của SV | Sinh viên chấp nhận phương án đã áp tạm |
| Mục 7 bản AI, điểm 3 | Chốt (a): Giữ nhóm API | Quyết định của SV | Sinh viên chấp nhận phương án đã áp tạm |
| Mục 7 bản AI, điểm 4 | Chốt (a): FR-04 trên Web ngoài phạm vi | Quyết định của SV | Sinh viên chấp nhận phương án đã áp tạm |
| Mục 6 bản AI, `S0_05_cham_email.png` | Không chụp; O12 lấy từ lời sinh viên ("không hiện bàn phím, giống `S0_02`") | Quyết định của SV | Bản AI yêu cầu ảnh này không kèm điều kiện; sinh viên đánh giá màn hình không đổi khi chạm nên không cần ảnh |
| Mục 6 bản AI, `S0_08_hoi_bo_thay_doi.png` | Không chụp; không bấm "Thoát" | Quyết định của SV | Không có nút hủy; sinh viên chọn không bấm nút "Thoát" vì chưa rõ chức năng |
