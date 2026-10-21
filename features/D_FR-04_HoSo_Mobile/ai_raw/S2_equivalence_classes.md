# S2: Chia lớp tương đương (FR-04 Quản lý hồ sơ cá nhân, Mobile)

- Bước: S2 (Chia lớp tương đương, theo Step 2 của slide S04)
- Thời gian tạo: 2026-10-21 07:30 (UTC+07:00)
- Căn cứ: `00_spec.md` (mục 3 yêu cầu, mục 4 và 7 câu hỏi mở, mục 5 bảng quan sát, mục 12 ghi chú), `01_io.md` (biến IN1 đến IN10, Output OUT1 đến OUT4, ERR1 đến ERR6, quyết định mục 8, ghi chú mục 11)

---

## 1. Cách làm

- Theo Step 2 của slide S04: Hai giá trị cùng lớp nếu kết quả mong đợi giống nhau. Theo yêu cầu của sinh viên, **chỉ tách lớp khi kết quả mong đợi khác nhau** (khác mã Output, hoặc khác dạng dữ liệu được lưu), hoặc khi có lý do rõ ràng tin rằng hệ thống xử lý khác (ghi ở cột cuối). Không tách theo mọi nhóm ký tự.
- Guideline đã dùng: Khoảng giá trị (số chữ số 10 đến 11: 1 lớp H, 2 lớp KH), điều kiện "must be" (bắt đầu bằng `0`, chỉ gồm chữ số, bắt buộc), tách theo rủi ro (ký tự HTML, SQL), tách theo bước chuẩn hóa (khoảng trắng).
- Loại: H (hợp lệ), KH (không hợp lệ), theo điều kiện của dòng đó. Không còn lớp GĐ vì mọi giả định đã **áp tạm phương án đề xuất** (mục 2); nếu sinh viên đổi phương án thì lớp đổi Loại theo cột "Hệ quả".
- Kết quả mong đợi dùng mã của `01_io.md`. Lớp hợp lệ cho kết quả thành công khi mọi input khác cũng hợp lệ (OUT1 qua giao diện, OUT2 qua API).
- `␣` là một dấu cách; `↵` là ký tự xuống dòng. Đại diện chỉ để minh họa; giá trị cụ thể chọn ở S3, S4.
- Cột "Kênh": Đường thực thi được (Giao diện, API, cả hai). Lớp có ký tự không gõ được bằng bàn phím của ô (O10, O14) ghi "API" hoặc "Giao diện (dán)".

## 2. Giả định

Mã giả định trùng số câu hỏi mở gốc. Mỗi giả định đã áp tạm phương án ở cột "Đã áp tạm"; lý do đề xuất là nhận xét của AI, sinh viên duyệt ở lượt review.

| Mã | Câu hỏi gốc | Phương án | Đã áp tạm, lý do đề xuất | Lớp bị ảnh hưởng | Chữ đặc tả |
|---|---|---|---|---|---|
| A01 | Q01: Họ Tên có bắt buộc không | (a) Bắt buộc: Rỗng (sau khi cắt khoảng trắng) cho ERR1; (b) không bắt buộc: Rỗng cho OUT1 | (a). Họ Tên là dữ liệu FR-01 bắt buộc khi đăng ký; cho xóa trống sẽ làm hồ sơ mất dữ liệu bắt buộc. Hệ quả: Ô Họ Tên phải có `*` (FR04-R13), nên D03 thành khác biệt cần kiểm | EC06, EC07 (KH theo (a), H theo (b)) | FR-01: "Người dùng phải cung cấp: **Họ Tên**, ..." (đăng ký). FR-04 không nói |
| A02 | Q02: Độ dài Họ Tên | (a) Không có cận, không lập lớp độ dài; (b) đặt cận tạm (ví dụ 255) | (a). Đặc tả không nêu con số nào; đặt cận là tự đặt quy tắc | Không có lớp độ dài; S4 chỉ xét cận dưới suy ra từ A01 (1 ký tự) | Không có |
| A03 | Q03: Ký tự cho phép trong Họ Tên | (a) Mọi ký tự in được, gồm chữ có dấu, chữ số, dấu câu, ký tự HTML, SQL: Đều H; (b) chỉ chữ cái (kể cả có dấu) và khoảng trắng: Chữ số, ký tự đặc biệt cho ERR1 | (a). Đặc tả không giới hạn ký tự; (b) là tự đặt quy tắc | EC02, EC04, EC05 (H theo (a); EC04, EC05 thành KH theo (b)) | Không có |
| A04 | Q04: Khoảng trắng trong Họ Tên | (a) Cắt khoảng trắng đầu cuối trước khi lưu; chỉ khoảng trắng tính như rỗng; khoảng trắng giữa giữ nguyên; (b) lưu nguyên văn, chỉ khoảng trắng là H | (a). Cách xử lý thông thường cho trường tên; (b) cho phép lưu tên vô nghĩa | EC03 (lưu đã cắt), EC07 (KH theo (a) kèm A01 (a)) | Không có |
| A05 | Q05: Số điện thoại có bắt buộc không | (a) Không bắt buộc: Để trống cho OUT1, lưu trống; (b) bắt buộc: Trống cho ERR2 | (a). FR-04 chỉ nêu điều kiện của số "hợp lệ" khi có nhập; hồ sơ mẫu đang trống (Q23); ô không có `*` (O13). Lưu ý: Đọc chặt chữ "bắt đầu bằng số `0`" thì chuỗi trống không thỏa, nên (b) cũng có căn cứ | EC09 (H theo (a), KH theo (b)) | "**Số điện thoại hợp lệ**: bắt đầu bằng số `0`, từ 10–11 chữ số." |
| A06 | Q06: Ký tự không phải chữ số trong Số điện thoại | (a) Từ chối (ERR2), không chuẩn hóa; (b) bỏ dấu phân cách (`␣`, `-`, `.`) rồi mới kiểm, ký tự khác vẫn từ chối | (a). Đặc tả viết "chữ số", không nhắc chuẩn hóa | EC13 (KH theo cả hai), EC14 (KH theo (a), H theo (b)) | "từ 10–11 chữ số" |
| A07 | Q07: "10–11 chữ số" có tính số `0` đầu không | (a) Có: Tổng số chữ số, kể cả `0` đầu, từ 10 đến 11; (b) không: Sau số `0` có 10 đến 11 chữ số | (a). Ví dụ `0912345678` trong API spec có 10 chữ số tính cả `0`; theo (b) thì ví dụ đó không hợp lệ | EC08, EC11, EC12 và các biên ở S4 | API spec mục 2.2: `"phone": "0912345678"` |
| A08 | Q08: Khoảng trắng đầu cuối Số điện thoại | (a) Cắt rồi kiểm: H, lưu đã cắt; (b) tính là ký tự không phải chữ số: ERR2 theo A06 (a) | (a). Thống nhất với A04 (a) | EC15 (H theo (a), KH theo (b)) | Không có |
| A09 | Q09: Kiểm đầu số nhà mạng | (a) Chỉ kiểm chữ số `0` đầu, không lập lớp đầu số; (b) kiểm đầu số nhà mạng | (a). Đặc tả chỉ nói "bắt đầu bằng số `0`" | Không có lớp riêng | "bắt đầu bằng số `0`" |
| A10 | Q10: Địa chỉ bắt buộc, độ dài, ký tự, xuống dòng | (a) Không bắt buộc; không có cận độ dài; mọi ký tự in được, gồm xuống dòng, đều H; (b) bắt buộc: Trống cho ERR3 | (a). Đặc tả không đặt ràng buộc nào; hồ sơ mẫu đang trống; ô nhiều dòng có phím xuống dòng (O15, O16). Hệ quả: ERR3 không có lớp nào dẫn tới | EC17, EC19 (H theo (a), KH theo (b)) | Không có |
| A11 | Q11: Khoảng trắng trong Địa chỉ | (a) Cắt đầu cuối; chỉ khoảng trắng lưu thành trống (OUT1); (b) lưu nguyên văn | (a). Thống nhất với A04 (a) | EC19 (dạng lưu) | Không có |
| A13 | Q13: Gửi `email` qua `PUT /api/users/me` | (a) Bỏ qua trường `email`, trường khác vẫn cập nhật; (b) từ chối cả yêu cầu (ERR5); (c) chấp nhận (a) hoặc (b), chỉ bắt buộc Email không đổi (OUT4) | (c). Đặc tả chỉ đòi Email không đổi; không nói phản hồi | EC22 | FR-04: "Email không được phép thay đổi qua giao diện." API spec: "Chỉ cho phép cập nhật thông tin cá nhân cơ bản." |
| A14 | Q14: Gửi `role` qua `PUT /api/users/me` | (a) Bỏ qua `role`; (b) từ chối cả yêu cầu (ERR5); (c) chấp nhận (a) hoặc (b), chỉ bắt buộc vai trò không đổi (OUT4) | (c). Như A13 | EC24 | SEC-06: "API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client." |
| A15 | Q15: Gửi `id` của người khác trong body | (a) Bỏ qua `id`, cập nhật hồ sơ của chủ token; (b) từ chối (ERR5); (c) chấp nhận (a) hoặc (b), chỉ bắt buộc hồ sơ người khác không đổi (OUT4) | (c). Như A13 | EC31 | FR-04: "Người dùng chỉ có thể cập nhật hồ sơ của chính mình" |
| A16 | Q16: Body thiếu trường | (a) Trường không gửi giữ nguyên (OUT2); (b) trường không gửi bị xóa; (c) từ chối (ERR6); (d) chấp nhận (a) hoặc (c), (b) là sai vì xóa dữ liệu người dùng không yêu cầu | (d). Đặc tả không nói; (b) làm mất dữ liệu mà người dùng không yêu cầu sửa | EC29 | Không có |
| A18 | Q18: Nhiều lỗi cùng lúc | (a) Không lập lớp, không thiết kế test case nhiều lỗi (mỗi test case không hợp lệ chỉ vi phạm một lớp); (b) thêm một test case nhiều lỗi để ghi nhận hành vi | (a). Đặc tả không nói; tiết kiệm ngân sách | Không có lớp | Không có |
| A19 | Q19: Lưu một phần khi bị từ chối | (a) Một trường sai thì cả lần lưu bị từ chối, không trường nào được lưu; (b) trường hợp lệ vẫn được lưu | (a). Hệ quả cho S3: Test case không hợp lệ đổi thêm một trường hợp lệ khác để phát hiện lưu một phần | Mọi lớp KH của IN1, IN2 | Không có |

Không đặt giả định cho Q12, Q22, Q23, Q24 (đã trả lời ở S0), Q17, Q21 (chỉ ghi nhận câu chữ, hành vi ở S6), Q20 (mã HTTP, cấu trúc phản hồi ghi nhận ở S6; kết quả mong đợi chỉ dùng "thành công" hoặc "thất bại"), Q25 (giao diện dùng PC1, không thiết kế token hết hạn trên ứng dụng), Q26 (chức năng nút "Thoát", ghi nhận ở S6 cho checklist), Q27 (đã đóng ở S1).

Hệ quả cần lưu ý của các giả định:

- A01 (a) kèm A04 (a): Cận dưới của Họ Tên là 1 ký tự **sau khi cắt**; `␣A␣` là H, `␣␣␣` là KH (S4).
- A07 (a): `0` kèm 9 chữ số là H (10 chữ số); `0` kèm 8 chữ số là KH.
- A06 (a) kèm A08 (a): Dấu cách ở **giữa** số là KH (EC14), dấu cách ở **đầu cuối** là H (EC15). Hai lớp cùng ký tự nhưng khác vị trí nên khác kết quả.
- A10 (a), A11 (a): ERR3 không phát sinh; S3 không có test case cho ERR3.
- A13, A14, A15, A16 theo phương án "chấp nhận hai cách": Kết quả mong đợi của các lớp này là điều kiện trên dữ liệu (OUT4, trường không bị xóa), không phải một phản hồi cụ thể.

## 3. Lớp tương đương của Input

### 3.1 IN1 Họ Tên

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Kênh | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC01 | Nội dung | Chữ cái không dấu và khoảng trắng giữa các từ | H | `Nguyen Van An` | OUT1, OUT2 | FR04-R01 | Cả hai | Lớp cơ sở. Chữ số, dấu câu thông thường thuộc lớp này theo A03 (a), không tách vì cùng kết quả |
| EC02 | Nội dung | Có chữ tiếng Việt có dấu | H | `Trần Thị Bích` | OUT1, OUT2; lưu đúng dấu | FR04-R01 | Giao diện (dán hoặc đổi bàn phím), API | Ký tự ngoài ASCII có thể bị mã hóa, lưu khác; bàn phím đang là "English (US)" (O10) |
| EC03 | Khoảng trắng | Có khoảng trắng ở đầu và cuối | H | `␣Nguyen Van An␣` | OUT1, OUT2; lưu là `Nguyen Van An` (A04 (a)) | FR04-R01 | Cả hai; kiểm dạng lưu bằng EV3 | Bước chuẩn hóa là nhánh xử lý riêng; khác dạng lưu |
| EC04 | Rủi ro | Có thẻ HTML | H | `<b>An</b>` | OUT1, OUT2; hiển thị lại nguyên văn trong ô, không in đậm | FR04-R01, FR04-R22 | Cả hai | Rủi ro bảo mật (SEC-04); dữ liệu được hiển thị lại ở ô Họ Tên và có thể ở lời chào "Chào, ..." |
| EC05 | Rủi ro | Có dấu nháy đơn | H | `O'Neil An` | OUT1, OUT2; lưu đúng nguyên văn | FR04-R01, FR04-R23 | Cả hai | Rủi ro bảo mật (SEC-05); chỉ suy ra qua hành vi |
| EC06 | Bắt buộc | Rỗng | KH | (để trống) | ERR1; hồ sơ không đổi | FR04-R01 | Cả hai | A01 (a) |
| EC07 | Bắt buộc | Chỉ gồm khoảng trắng | KH | `␣␣␣` | ERR1; hồ sơ không đổi | FR04-R01 | Cả hai | A01 (a) kèm A04 (a): Tách khỏi EC06 vì phải qua bước cắt khoảng trắng mới thành rỗng |

### 3.2 IN2 Số điện thoại

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Kênh | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC08 | Số chữ số và chữ số đầu | Bắt đầu bằng `0`, chỉ gồm chữ số, từ 10 đến 11 chữ số | H | `0912345678` | OUT1, OUT2 | FR04-R02, FR04-R04, FR04-R05 | Cả hai | Lớp cơ sở; khoảng giá trị 10 đến 11 là một lớp H (guideline khoảng giá trị); 10 và 11 xét ở S4 |
| EC09 | Bắt buộc | Trống (xóa số đang có) | H | (để trống) | OUT1, OUT2; lưu trống | FR04-R02 | Cả hai | A05 (a). Tiền điều kiện: Số điện thoại đang có giá trị (`01_io.md` mục 11) |
| EC10 | Chữ số đầu | Không bắt đầu bằng `0`, đủ 10 chữ số | KH | `1912345678` | ERR2; hồ sơ không đổi | FR04-R04 | Cả hai | Điều kiện "must be" |
| EC11 | Số chữ số | Bắt đầu bằng `0`, ít hơn 10 chữ số | KH | `091234567` (9 chữ số) | ERR2; hồ sơ không đổi | FR04-R05 | Cả hai | Khoảng giá trị: Lớp dưới (A07 (a)) |
| EC12 | Số chữ số | Bắt đầu bằng `0`, nhiều hơn 11 chữ số | KH | `091234567890` (12 chữ số) | ERR2; hồ sơ không đổi | FR04-R05 | Cả hai | Khoảng giá trị: Lớp trên |
| EC13 | Ký tự | Có ký tự không phải chữ số, không phải dấu phân cách (chữ cái hoặc ký hiệu `*`, `#`, `+`, `,`) | KH | `0912*345678` (10 chữ số và 1 dấu `*`) | ERR2; hồ sơ không đổi | FR04-R05 | Giao diện (ký hiệu có trên bàn phím điện thoại, O14), API (chữ cái) | A06 (a). Đại diện giữ đúng 10 chữ số và bắt đầu bằng `0`, nên chỉ vi phạm điều kiện "chỉ gồm chữ số" |
| EC14 | Ký tự | Có dấu phân cách ở giữa (`-`, `.`, `␣`) | KH | `0912-345678` (10 chữ số và 1 dấu `-`) | ERR2; hồ sơ không đổi | FR04-R05 | API (bàn phím không có `-`, `.`, `␣`, O14) | A06 (a). Tách khỏi EC13 vì hệ thống hay chuẩn hóa dấu phân cách (A06 (b)) mà không chuẩn hóa chữ cái |
| EC15 | Khoảng trắng | Có khoảng trắng ở đầu và cuối, phần còn lại hợp lệ | H | `␣0912345678␣` | OUT2; lưu là `0912345678` (A08 (a)) | FR04-R05 | API | Bước chuẩn hóa là nhánh riêng; khác dạng lưu. Bàn phím không có dấu cách |

### 3.3 IN3 Địa chỉ giao hàng mặc định

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Kênh | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC16 | Nội dung | Một dòng, có chữ có dấu, chữ số, dấu phẩy, `/` | H | `12/3 Lê Lợi, Quận 1, TP.HCM` | OUT1, OUT2; lưu đúng nguyên văn | FR04-R03 | Cả hai | Lớp cơ sở. Chữ có dấu gộp vào lớp cơ sở vì địa chỉ ở Việt Nam thường có dấu; nếu sai thì ghi nhận riêng ở S6 |
| EC17 | Bắt buộc | Trống (xóa địa chỉ đang có) | H | (để trống) | OUT1, OUT2; lưu trống | FR04-R03 | Cả hai | A10 (a). Tiền điều kiện: Địa chỉ đang có giá trị |
| EC18 | Xuống dòng | Nhiều dòng | H | `12 Lê Lợi` `↵` `Quận 1` | OUT1, OUT2; lưu và hiển thị lại đủ 2 dòng | FR04-R03 | Cả hai (phím xuống dòng, O16) | Ô nhiều dòng là nhánh nhập riêng; ký tự xuống dòng có thể bị bỏ hoặc đổi khi lưu |
| EC19 | Khoảng trắng | Chỉ gồm khoảng trắng | H | `␣␣␣` | OUT1, OUT2; lưu thành trống (A11 (a)) | FR04-R03 | Cả hai; kiểm dạng lưu bằng EV3 | Bước chuẩn hóa; khác dạng lưu với EC16 |
| EC20 | Rủi ro | Có thẻ HTML | H | `<i>Kho A</i>, Quận 1` | OUT1, OUT2; hiển thị lại nguyên văn | FR04-R03, FR04-R22 | Cả hai | Rủi ro bảo mật (SEC-04). Dấu nháy đơn (FR04-R23) chỉ xét ở Họ Tên (EC05) để giữ ngân sách (`01_io.md` mục 8 điểm 10) |

### 3.4 IN4 Email, IN5 Vai trò (nhóm API, trừ EC21 có cả giao diện)

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Kênh | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC21 | Có gửi Email | Không gửi `email` (giao diện không cho sửa) | H | Body chỉ có `name`, `shipping_address`, `phone` | OUT1, OUT2 | FR04-R06 | Cả hai | Lớp cơ sở; phần giao diện của FR04-R06 kiểm ở checklist |
| EC22 | Có gửi Email | Gửi `email` khác Email hiện tại | KH | `"email": "khac@eshop.com"` kèm 3 trường hợp lệ | OUT4 (Email không đổi); phản hồi là OUT2 hoặc ERR5 đều chấp nhận (A13 (c)) | FR04-R06, FR04-R19 | API | |
| EC23 | Có gửi vai trò | Không gửi `role` | H | Body chỉ có 3 trường | OUT1, OUT2 | FR04-R08 | Cả hai | Lớp cơ sở |
| EC24 | Có gửi vai trò | Gửi `role` khác vai trò hiện tại | KH | `"role": "admin"` kèm 3 trường hợp lệ | OUT4 (vai trò không đổi); phản hồi là OUT2 hoặc ERR5 đều chấp nhận (A14 (c)) | FR04-R08, FR04-R19, FR04-R21 | API | Kiểm vai trò bằng EV3 nếu có `role` (`01_io.md` mục 8 điểm 7) |

### 3.5 IN6 Trạng thái xác thực (nhóm API)

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Kênh | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC25 | Token | Token hợp lệ của chủ hồ sơ | H | Token từ `POST /api/login` (PC2) | OUT2, OUT3 | FR04-R17, FR04-R20 | API | Lớp cơ sở |
| EC26 | Token | Không có header `Authorization` | KH | (không gửi header) | ERR4; hồ sơ không đổi | FR04-R20 | API | |
| EC27 | Token | Có header nhưng token không hợp lệ | KH | `Authorization: Bearer abc` | ERR4; hồ sơ không đổi | FR04-R20 | API | Tách khỏi EC26: Thiếu header và token sai là hai nhánh kiểm khác nhau. Token hết hạn không lập lớp (cần chờ thời gian hết hạn, đặc tả không nêu thời hạn) |

### 3.6 IN8 Các trường trong body, IN9 và IN10 Hồ sơ người khác (nhóm API)

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Kênh | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|---|
| EC28 | Trường trong body | Đủ 3 trường | H | `name`, `shipping_address`, `phone` | OUT2 | FR04-R18 | API | Lớp cơ sở |
| EC29 | Trường trong body | Thiếu trường (chỉ gửi `name`) | H | `{"name": "Nguyen Van Binh"}` khi hồ sơ đang có Số điện thoại và Địa chỉ | OUT2 với Số điện thoại, Địa chỉ giữ nguyên; hoặc ERR6 với hồ sơ không đổi (A16 (d)). Số điện thoại, Địa chỉ bị xóa là sai | FR04-R18 | API | Loại H vì đặc tả không cấm gửi thiếu |
| EC30 | Mã người khác | Không gửi mã người dùng | H | Body chỉ có 3 trường | OUT2 | FR04-R07 | API | Lớp cơ sở |
| EC31 | Mã người khác | Gửi `id` của tài khoản `admin@eshop.com` bằng token của `test@eshop.com` | KH | `"id": <id của admin>` kèm 3 trường hợp lệ | OUT4 (hồ sơ admin không đổi, kiểm bằng EV3 với token admin); phản hồi là OUT2 hoặc ERR5 đều chấp nhận (A15 (c)) | FR04-R07 | API | IN10 không chia lớp riêng: Tài khoản admin chỉ là điều kiện của lớp này (`01_io.md` mục 8 điểm 5). Lấy `id` của admin từ EV3 bằng token admin; nếu phản hồi không có `id` (Q20) thì test case Blocked |

### 3.7 Biến không chia lớp

- IN7 (hồ sơ hiện có): Là tiền điều kiện PC3 (`01_io.md` mục 8 điểm 3).
- IN10: Xem EC31.

## 4. Lớp Output

| Mã | Output | Lớp Input dẫn tới | Ghi chú |
|---|---|---|---|
| EC32 | OUT1 Cập nhật thành công qua giao diện | Lớp H của IN1, IN2, IN3 có kênh giao diện (EC01 đến EC05, EC08, EC09, EC16 đến EC20), EC21, EC23 | |
| EC33 | OUT2 Cập nhật thành công qua API | Lớp H của IN1 đến IN3, EC15, EC21, EC23, EC25, EC28, EC29, EC30 | Có thể đi kèm EC22, EC24, EC31 (A13, A14, A15 (c)) |
| EC34 | OUT3 Lấy hồ sơ qua API | EC25 | Dùng trong mọi lần kiểm chứng bằng EV3 |
| EC35 | OUT4 Thuộc tính được bảo vệ giữ nguyên | EC22, EC24, EC31 | Kết quả bắt buộc của 3 lớp này dù phản hồi là gì |
| EC36 | ERR1 Họ Tên không hợp lệ | EC06, EC07 | |
| EC37 | ERR2 Số điện thoại không hợp lệ | EC10 đến EC14 | |
| EC38 | ERR4 Không xác thực được | EC26, EC27 | |

Không lập lớp cho:

- ERR3: Không có lớp Input nào dẫn tới theo A10 (a), A11 (a).
- ERR5, ERR6: Là một trong hai phản hồi được chấp nhận của EC22, EC24, EC31, EC29 (A13 đến A16), không phải kết quả bắt buộc; không thiết kế test case riêng.

## 5. Dữ liệu có rủi ro bảo mật

| Trường | Ký tự HTML, SQL có đi tới bước lưu không | Lớp | Giới hạn quan sát |
|---|---|---|---|
| Họ Tên | Có, theo A03 (a) mọi ký tự in được đều H | EC04, EC05 | Chỉ quan sát được hiển thị lại trên ứng dụng (ô Họ Tên, lời chào); hiển thị trên Web, Web Admin thuộc feature khác. Parameterized Query (FR04-R23) chỉ suy ra: Lưu đúng nguyên văn, không lỗi hệ thống |
| Số điện thoại | Không, theo A06 (a) mọi ký tự không phải chữ số đều bị từ chối | Không lập lớp riêng | |
| Địa chỉ | Có, theo A10 (a) | EC20 | Như Họ Tên |

## 6. Tổng hợp

| Biến | Lớp H | Lớp KH | Lớp |
|---|---|---|---|
| IN1 Họ Tên | 5 | 2 | EC01 đến EC07 |
| IN2 Số điện thoại | 3 | 5 | EC08 đến EC15 |
| IN3 Địa chỉ | 5 | 0 | EC16 đến EC20 |
| IN4 Email | 1 | 1 | EC21, EC22 |
| IN5 Vai trò | 1 | 1 | EC23, EC24 |
| IN6 Token | 1 | 2 | EC25 đến EC27 |
| IN8 Trường trong body | 2 | 0 | EC28, EC29 |
| IN9, IN10 Hồ sơ người khác | 1 | 1 | EC30, EC31 |
| Output | | | EC32 đến EC38 (7 lớp) |
| **Tổng** | **19** | **12** | **38 lớp** (31 lớp Input, 7 lớp Output) |

Số liệu đếm bằng `check_step.py classes`.

## 7. Điểm cần sinh viên quyết định

Theo yêu cầu của sinh viên, các điểm dưới đây đã **áp tạm phương án đề xuất**; sinh viên duyệt ở lượt review. Không điểm nào đổi cấu trúc cả bảng lớp: Đổi phương án chỉ đổi Loại hoặc kết quả của các lớp ghi ở cột "Lớp bị ảnh hưởng" (mục 2).

| # | Vấn đề | Các lựa chọn | Đã áp tạm |
|---|---|---|---|
| 1 | Giả định A01 đến A19 (mục 2) | Theo từng giả định | Phương án ghi ở cột "Đã áp tạm" |
| 2 | Chữ có dấu của Địa chỉ | (a) Gộp vào lớp cơ sở EC16; (b) tách lớp riêng như EC02 | (a) |
| 3 | Dấu nháy đơn (FR04-R23) | (a) Chỉ ở Họ Tên (EC05); (b) thêm một lớp cho Địa chỉ | (a) |
| 4 | Token hết hạn | (a) Không lập lớp; (b) lập lớp, chạy khi biết thời hạn token | (a) |
| 5 | Lớp đầu số nhà mạng (ví dụ `00...`) | (a) Không lập (A09 (a)); (b) lập một lớp H để thăm dò luật không nêu | (a) |
| 6 | ERR5, ERR6 | (a) Không lập lớp Output riêng, là phản hồi được chấp nhận của EC22, EC24, EC29, EC31; (b) lập lớp và chốt một phản hồi bắt buộc | (a) |

## 8. Ghi chú cho bước sau

- **Phân vùng có thứ tự cho S4:**
  - Số chữ số của Số điện thoại (A07 (a)): KH 9 trở xuống (EC11), H 10 đến 11 (EC08), KH 12 trở lên (EC12). LB = 10, UB = 11; LB-1 = 9, UB+1 = 12. Không có điểm "giữa" riêng vì giữa 10 và 11 không có số nguyên nào. Nhỏ nhất chỉ vi phạm số chữ số: `0` (1 chữ số). Lớn nhất giao diện cho nhập: Chưa biết, thăm dò ở S6.
  - Độ dài Họ Tên: Không có cận trên (A02 (a)); cận dưới suy ra là 1 ký tự sau khi cắt (A01 (a), A04 (a)). Biến thể tại biên: `A`, `␣A␣` (H), `␣` (KH, trùng lớp EC07 nếu đã có).
  - Địa chỉ: Không có cận (A10 (a)); không làm BVA.
- **Lớp không có đại diện chỉ vi phạm một điều kiện:** Không có. Lưu ý giữ đúng 10 chữ số ở đại diện của EC13, EC14 để không vi phạm thêm FR04-R05.
- **Cách thực thi:**
  - Lớp chỉ đi được qua API: EC14, EC15, EC22, EC24 đến EC31. EC02 qua giao diện cần dán hoặc đổi bàn phím tiếng Việt.
  - Ràng buộc Số điện thoại có thể chỉ được kiểm ở ứng dụng: Nên có ít nhất một test case API cho một lớp KH của FR04-R04 và một của FR04-R05.
  - Test case không hợp lệ (A19 (a)): Đổi thêm một trường hợp lệ khác trong cùng lần lưu (ví dụ Họ Tên), rồi kiểm cả hai trường không đổi.
  - EC09, EC17, EC29: Tiền điều kiện trường đang có giá trị (khác PC3 mặc định).
  - EC03, EC15, EC19: Kiểm dạng lưu bằng EV3 vì giao diện không cho thấy khoảng trắng cuối.
- **Checklist (`01_io.md` mục 7):** Theo A01 (a), ô Họ Tên phải có `*` (FR04-R13); quan sát S0 không có (D03). FR04-R14 chạy kèm một test case bị từ chối qua giao diện (ví dụ EC10 hoặc EC06).
- **Ngân sách:** 31 lớp Input. Ước tính S3: 1 test case cơ sở, khoảng 11 test case cho lớp H bất thường, 12 test case không hợp lệ, 1 đến 2 test case checklist; S4 thêm khoảng 2 đến 4 test case. Tổng khoảng 27 đến 30, trong mục tiêu 25 đến 35.
