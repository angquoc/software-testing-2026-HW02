# S2: Chia lớp tương đương (FR-01 Đăng ký tài khoản)

- Bước: S2 (Chia lớp tương đương, Complete Set of Partitions, theo Step 2 của slide S04)
- Thời gian tạo: 2026-10-19 23:35 (+07:00)
- Căn cứ: `00_spec.md` (yêu cầu, câu hỏi mở, quyết định ở mục 3.9), `01_io.md` (biến IN1 đến IN5, OUT1 đến OUT4, ERR1 đến ERR7, quyết định ở mục 5)

---

## 1. Cách chia

Áp dụng các guideline của slide S04:

| Guideline | Áp dụng cho |
|---|---|
| Điều kiện "must be": 1 lớp hợp lệ, 1 lớp không hợp lệ | Bắt buộc cung cấp (Họ Tên, Email, Mật khẩu); Email đúng định dạng; Email duy nhất; Mật khẩu có chữ hoa, chữ thường, chữ số, ký tự đặc biệt; Xác nhận mật khẩu khớp |
| Khoảng giá trị: 1 lớp hợp lệ, 2 lớp không hợp lệ | Độ dài Mật khẩu. Đặc tả chỉ có cận dưới (tối thiểu 8), không có cận trên, nên chỉ có 1 lớp không hợp lệ (dưới cận) |
| Tập giá trị: Mỗi phần tử 1 lớp hợp lệ nếu có lý do tin rằng chúng được xử lý khác nhau, cộng 1 lớp không hợp lệ | Tập ký tự đặc biệt `@ $ ! % * ? &` (xem điểm 1 ở mục 7) |
| Tách lớp khi có lý do tin rằng các phần tử được xử lý khác nhau | Nêu lý do ở từng chỗ tách, cột "Lý do tách" |

Quy ước:

- Cột "Loại": **H** là hợp lệ, **KH** là không hợp lệ, **GĐ** là lớp mà kết quả phụ thuộc giả định chưa chốt (mục 6). Lớp GĐ sẽ thành H hoặc KH sau khi sinh viên chọn phương án.
- Cột "Kết quả mong đợi" dùng mã Output của `01_io.md`. Kết quả của một lớp hợp lệ là OUT1 **khi mọi input khác cũng hợp lệ**. Kết quả của lớp không hợp lệ là OUT2 kèm mã lỗi.
- Ví dụ trong cột "Đại diện" chỉ để minh họa lớp; giá trị cụ thể chọn ở S3 và S4.
- Tiền điều kiện chung (`01_io.md` mục 1.1): Chưa đăng nhập; dữ liệu đã reset về dữ liệu mẫu.

---

## 2. IN1: Họ Tên

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|
| EC01 | Bắt buộc cung cấp | Có ít nhất 1 ký tự khác khoảng trắng | H | `Nguyen Van A` | OUT1 | FR01-R01 | |
| EC02 | Bắt buộc cung cấp | Rỗng | KH | (để trống) | OUT2, ERR1 | FR01-R01 | |
| EC03 | Bắt buộc cung cấp | Chỉ gồm khoảng trắng | GĐ (A03) | 3 dấu cách | Theo A03 | FR01-R01 | Hệ thống có thể cắt khoảng trắng trước khi kiểm tra hoặc không, nên xử lý có thể khác EC01 và EC02 |
| EC04 | Tập ký tự | Chỉ chữ Latin không dấu và khoảng trắng | H | `Nguyen Van A` | OUT1 | FR01-R01 | Lớp cơ sở |
| EC05 | Tập ký tự | Có chữ tiếng Việt có dấu | GĐ (A02) | `Nguyễn Thị Ánh` | Theo A02 | FR01-R01 | Ký tự Unicode có thể bị xử lý khác (mã hóa, lưu trữ) |
| EC06 | Tập ký tự | Có chữ số hoặc dấu câu thông thường | GĐ (A02) | `Anh-Ngoc 2` | Theo A02 | FR01-R01 | Có thể có kiểm tra "tên chỉ gồm chữ cái" mà đặc tả không nêu |
| EC07 | Tập ký tự | Có ký tự đặc biệt của HTML hoặc SQL (`<`, `>`, `'`, `"`) | GĐ (A02) | `<b>An</b>`, `O'Brien` | Theo A02. Nếu được chấp nhận: Đăng ký thành công, không xuất hiện lỗi hệ thống | FR01-R01, FR01-R24, FR01-R25 | Lớp theo rủi ro (risk-based equivalence): Dữ liệu này có thể làm hỏng câu truy vấn hoặc bị render thành HTML. Xem mục 5 |

Độ dài Họ Tên: Đặc tả không nêu giới hạn (Q01, giả định A01). Chưa lập lớp theo độ dài; S4 sẽ xét giá trị lớn nhất giao diện cho nhập.

---

## 3. IN2: Email

### 3.1 Bắt buộc cung cấp (FR01-R02)

| Mã | Lớp | Loại | Đại diện | Kết quả mong đợi | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|
| EC08 | Có giá trị | H | `user01@domain.com` | OUT1 | |
| EC09 | Rỗng | KH | (để trống) | OUT2, ERR2 | |
| EC10 | Chỉ gồm khoảng trắng | KH | 3 dấu cách | OUT2, ERR2 hoặc ERR3 (theo A07) | Bị từ chối trong mọi trường hợp; chỉ mã lỗi phụ thuộc việc có cắt khoảng trắng không |

### 3.2 Đúng định dạng (FR01-R04)

| Mã | Lớp | Loại | Đại diện | Kết quả mong đợi | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|
| EC11 | Đúng dạng như ví dụ của đặc tả: `phần_trước@tên_miền.đuôi` | H | `user01@domain.com` | OUT1 | Lớp cơ sở |
| EC12 | Đúng chuẩn email nhưng phức tạp hơn ví dụ: Có `.` hoặc `+` ở phần trước `@`, có tên miền con | GĐ (A04) | `an.nguyen+1@mail.domain.com` | Theo A04 | Đặc tả chỉ đưa một ví dụ, không nêu quy tắc |
| EC13 | Thiếu `@` | KH | `user01domain.com` | OUT2, ERR3 | Mỗi lớp từ EC13 đến EC18 vi phạm một luật định dạng khác nhau. Việc kiểm tra định dạng có thể diễn ra ở 2 nơi (trình duyệt với `type="email"` theo FR01-R19, và hệ thống), mỗi nơi có thể bắt một số luật mà bỏ sót luật khác |
| EC14 | Thiếu phần trước `@` | KH | `@domain.com` | OUT2, ERR3 | Như trên |
| EC15 | Thiếu phần sau `@` | KH | `user01@` | OUT2, ERR3 | Như trên |
| EC16 | Phần sau `@` không có dấu chấm | GĐ (A04) | `user01@domain` | Theo A04 | Ví dụ của đặc tả có `.com`, nhưng `type="email"` của HTML5 chấp nhận dạng này |
| EC17 | Có từ 2 dấu `@` trở lên | KH | `user01@@domain.com` | OUT2, ERR3 | Như EC13 |
| EC18 | Có khoảng trắng ở giữa | KH | `user 01@domain.com` | OUT2, ERR3 | Như EC13 |
| EC19 | Có khoảng trắng ở đầu hoặc cuối, phần còn lại đúng dạng | GĐ (A07) | ` user01@domain.com ` | Theo A07 | Hệ thống có thể cắt khoảng trắng hoặc không |

### 3.3 Duy nhất trong hệ thống (FR01-R05, liên quan IN5)

| Mã | Lớp | Loại | Đại diện | Kết quả mong đợi | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|
| EC20 | Chưa có trong hệ thống | H | `user01@domain.com` (chưa đăng ký) | OUT1 | |
| EC21 | Trùng chính xác một email có trong dữ liệu mẫu | KH | `test@eshop.com` | OUT2, ERR4 | |
| EC22 | Trùng chính xác một email vừa được tạo bằng chức năng đăng ký (đăng ký thành công trước đó trong cùng đợt test) | KH | Email của một lần đăng ký thành công trước đó | OUT2, ERR4 | Dữ liệu mẫu được nạp sẵn, còn email này do chính chức năng đăng ký lưu; hai cách lưu có thể khác nhau (ví dụ chuẩn hóa chữ hoa thường). Đây cũng là bước "đăng ký lại cùng email" ở `01_io.md` mục 3.4 |
| EC23 | Trùng một email có sẵn nhưng khác chữ hoa, chữ thường | GĐ (A06) | `Test@Eshop.com` | Theo A06 | |

Độ dài Email: Đặc tả không nêu giới hạn (Q05, giả định A05). Chưa lập lớp theo độ dài; S4 sẽ xét giá trị lớn nhất giao diện cho nhập.

---

## 4. IN3: Mật khẩu

Theo quyết định 3 ở `01_io.md`: Phía Input tách riêng từng điều kiện của mật khẩu; phía Output mọi vi phạm từ FR01-R06 đến FR01-R10 đều là ERR6.

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|---|
| EC24 | Bắt buộc cung cấp | Có giá trị | H | `Abcdef1!` | OUT1 | FR01-R03 | |
| EC25 | Bắt buộc cung cấp | Rỗng | KH | (để trống) | OUT2, ERR5 | FR01-R03 | |
| EC26 | Độ dài (khoảng giá trị, chỉ có cận dưới 8) | Từ 8 ký tự trở lên | H | `Abcdef1!` (8 ký tự) | OUT1 | FR01-R06 | Cận trên chưa có (Q08, giả định A08); S4 xét giá trị lớn nhất giao diện cho nhập |
| EC27 | Độ dài | Từ 1 đến 7 ký tự | KH | `Abcd1!` (6 ký tự) | OUT2, ERR6 | FR01-R06 | |
| EC28 | Chữ hoa | Có ít nhất 1 chữ hoa `A-Z` | H | `Abcdef1!` | OUT1 | FR01-R07 | |
| EC29 | Chữ hoa | Không có chữ hoa nào | KH | `abcdef1!` | OUT2, ERR6 | FR01-R07 | |
| EC30 | Chữ hoa | Chữ hoa duy nhất là chữ có dấu | GĐ (A11) | `Ăbcdef1!` | Theo A11 | FR01-R07 | Chữ có dấu có thể không được nhận là chữ hoa |
| EC31 | Chữ thường | Có ít nhất 1 chữ thường `a-z` | H | `Abcdef1!` | OUT1 | FR01-R08 | |
| EC32 | Chữ thường | Không có chữ thường nào | KH | `ABCDEF1!` | OUT2, ERR6 | FR01-R08 | |
| EC33 | Chữ thường | Chữ thường duy nhất là chữ có dấu | GĐ (A11) | `ABCDEă1!` | Theo A11 | FR01-R08 | Như EC30 |
| EC34 | Chữ số | Có ít nhất 1 chữ số `0-9` | H | `Abcdef1!` | OUT1 | FR01-R09 | |
| EC35 | Chữ số | Không có chữ số nào | KH | `Abcdefg!` | OUT2, ERR6 | FR01-R09 | |
| EC36 | Ký tự đặc biệt (tập giá trị) | Có ít nhất 1 ký tự trong tập `@ $ ! % * ? &` | H | `Abcdef1!` | OUT1 | FR01-R10 | Có tách thành 7 lớp hay không: Xem điểm 1 ở mục 7 |
| EC37 | Ký tự đặc biệt | Không có ký tự đặc biệt nào | KH | `Abcdefg1` | OUT2, ERR6 | FR01-R10 | |
| EC38 | Ký tự đặc biệt | Ký tự đặc biệt duy nhất nằm ngoài tập của đặc tả | GĐ (A09) | `Abcdef1#` | Theo A09 | FR01-R10 | Đặc tả liệt kê tập ký tự trong ngoặc, nhưng không nói là danh sách đóng |
| EC39 | Ký tự khác ngoài 4 loại | Đủ 4 loại, có thêm khoảng trắng | GĐ (A10) | `Abc def1!` | Theo A10 | FR01-R06 đến FR01-R10 | Khoảng trắng có thể bị cắt hoặc bị cấm |
| EC40 | Ký tự khác ngoài 4 loại | Đủ 4 loại, có thêm ký tự không thuộc 4 loại (chữ có dấu, ký tự ngoài tập) | GĐ (A10) | `Abcdef1!é` | Theo A10 | FR01-R06 đến FR01-R10 | Đặc tả chỉ nói "có ít nhất", không nói có cấm ký tự khác không |

---

## 5. IN4: Xác nhận mật khẩu

Giữ theo quyết định Q26, dù giao diện hiện không có trường này (D01). Các lớp này chưa thực thi được qua giao diện; cách thực thi chốt ở S3.

| Mã | Lớp | Loại | Đại diện (khi Mật khẩu là `Abcdef1!`) | Kết quả mong đợi | Yêu cầu | Lý do tách hoặc ghi chú |
|---|---|---|---|---|---|---|
| EC41 | Giống hệt Mật khẩu | H | `Abcdef1!` | OUT1 | FR01-R12 | |
| EC42 | Khác Mật khẩu ít nhất 1 ký tự | KH | `Abcdef2!` | OUT2, ERR7 | FR01-R12 | |
| EC43 | Rỗng trong khi Mật khẩu có giá trị | GĐ (A13) | (để trống) | Theo A13 | FR01-R11, FR01-R12 | Kiểm tra "bắt buộc" và kiểm tra "khớp" có thể được xử lý riêng |
| EC44 | Chỉ khác Mật khẩu ở chữ hoa, chữ thường | GĐ (A14) | `abcdef1!` | Theo A14 | FR01-R12 | So sánh có thể không phân biệt hoa thường |
| EC45 | Chỉ khác Mật khẩu ở khoảng trắng đầu hoặc cuối | GĐ (A14) | `Abcdef1! ` | Theo A14 | FR01-R12 | Một trong hai trường có thể bị cắt khoảng trắng |

---

## 6. Lớp tương đương của Output

Theo slide S04 (ví dụ EC9 "SUM" và EC10 "Invalid Input"), mỗi Output cũng là một lớp cần được phủ.

| Mã | Output | Lớp Input dẫn tới |
|---|---|---|
| EC46 | OUT1: Đăng ký thành công | Mọi input thuộc lớp hợp lệ |
| EC47 | OUT2, ERR1: Thiếu Họ Tên | EC02 (và EC03 nếu A03 chọn "coi như rỗng") |
| EC48 | OUT2, ERR2: Thiếu Email | EC09, EC10 (theo A07) |
| EC49 | OUT2, ERR3: Email sai định dạng | EC13 đến EC18; EC10, EC12, EC16, EC19 tùy giả định |
| EC50 | OUT2, ERR4: Email đã tồn tại | EC21, EC22; EC23 tùy A06 |
| EC51 | OUT2, ERR5: Thiếu Mật khẩu | EC25 |
| EC52 | OUT2, ERR6: Mật khẩu không đạt yêu cầu mạnh | EC27, EC29, EC32, EC35, EC37; EC30, EC33, EC38 đến EC40 tùy giả định |
| EC53 | OUT2, ERR7: Mật khẩu và Xác nhận mật khẩu không khớp | EC42; EC43 đến EC45 tùy giả định |

OUT3 và OUT4 (phản hồi API) chỉ thêm lớp nếu S3 quyết định test qua API.

---

## 7. Giả định cần chốt

Đây là những điểm đặc tả không nói rõ, ảnh hưởng trực tiếp tới việc một lớp là hợp lệ hay không hợp lệ. Mã giả định trùng số với câu hỏi mở tương ứng trong `00_spec.md` (A01 ứng với Q01...). AI không chọn phương án; cột "Chữ đặc tả" chỉ ghi đặc tả viết gì, nếu có liên quan.

| Mã | Câu hỏi gốc | Phương án | Lớp bị ảnh hưởng | Chữ đặc tả |
|---|---|---|---|---|
| A01 | Q01: Độ dài Họ Tên | (a) Không giới hạn trên, không lập lớp độ dài; (b) Đặt một giới hạn L, lập thêm lớp "dài hơn L" (KH) | Thêm lớp mới nếu chọn (b) | Không nêu |
| A02 | Q02: Ký tự cho phép trong Họ Tên | (a) Mọi ký tự đều hợp lệ, EC05 đến EC07 là H; (b) Giới hạn một số ký tự, lớp bị cấm thành KH và phát sinh loại lỗi mới ngoài ERR1 đến ERR7 | EC05, EC06, EC07 | Chỉ nói "phải cung cấp", không giới hạn ký tự |
| A03 | Q03: Họ Tên chỉ gồm khoảng trắng | (a) Coi như rỗng: EC03 là KH, ERR1; (b) Coi là đã cung cấp: EC03 là H | EC03 | Không nêu |
| A04 | Q04: Quy tắc định dạng email | (a) Theo chuẩn email thông dụng: EC12 là H, EC16 là KH; (b) Theo `type="email"` của HTML5: EC12 và EC16 đều là H; (c) Chỉ chấp nhận đúng dạng ví dụ: EC12 và EC16 đều là KH | EC12, EC16 | "định dạng hợp lệ (`user@domain.com`)" |
| A05 | Q05: Độ dài Email | Như A01 | Thêm lớp mới nếu đặt giới hạn | Không nêu |
| A06 | Q06: So trùng email có phân biệt hoa thường | (a) Không phân biệt: EC23 là KH, ERR4; (b) Phân biệt: EC23 là H | EC23 | Không nêu |
| A07 | Q07: Khoảng trắng đầu cuối của email | (a) Cắt bỏ trước khi kiểm tra: EC19 là H, EC10 cho ERR2; (b) Không cắt: EC19 là KH (ERR3), EC10 cho ERR3 | EC10, EC19 | Không nêu |
| A08 | Q08: Độ dài tối đa của Mật khẩu | Như A01 | Thêm lớp mới nếu đặt giới hạn | Chỉ nêu "Tối thiểu 8 ký tự" |
| A09 | Q09: Tập ký tự đặc biệt đóng hay mở | (a) Đóng: EC38 là KH, ERR6; (b) Mở: EC38 là H | EC38 | Liệt kê 7 ký tự trong ngoặc sau "1 ký tự đặc biệt" |
| A10 | Q10: Ký tự ngoài 4 loại trong mật khẩu | (a) Cho phép: EC39, EC40 là H; (b) Cấm: EC39, EC40 là KH, ERR6; (c) Tách riêng khoảng trắng và ký tự khác | EC39, EC40 | "có ít nhất 1...", không nêu cấm |
| A11 | Q11: Chữ có dấu có tính là chữ hoa, chữ thường | (a) Chỉ tính `A-Z`, `a-z`: EC30, EC33 là KH, ERR6; (b) Tính cả chữ có dấu: EC30, EC33 là H | EC30, EC33 | "chữ hoa", "chữ thường", không nêu phạm vi |
| A13 | Q13: Xác nhận mật khẩu để trống | (a) Là trường hợp "không khớp": EC43 là KH, ERR7; (b) Là lỗi riêng "thiếu Xác nhận mật khẩu": EC43 là KH, thêm loại lỗi mới | EC43 | Chỉ có quy tắc "từ chối nếu hai trường không khớp" |
| A14 | Q14: "Khớp" có phải trùng chính xác từng ký tự | (a) Trùng chính xác: EC44, EC45 là KH, ERR7; (b) Bỏ qua hoa thường hoặc khoảng trắng: Lớp tương ứng là H | EC44, EC45 | "không khớp", không định nghĩa thêm |

Câu Q12 (Xác nhận mật khẩu có dùng `type="password"`) thuộc checklist giao diện, không ảnh hưởng chia lớp. Các câu Q15 đến Q23, Q25 thuộc S3 (cách thực thi, nội dung thông báo lỗi, API) hoặc checklist.

---

## 8. Kết luận về dữ liệu chứa HTML hoặc ký tự đặc biệt (FR01-R24, FR01-R25)

Theo yêu cầu ở `00_spec.md` mục 1.6, xét có cần lớp tương đương riêng cho dữ liệu chứa HTML hoặc ký tự đặc biệt không.

- **Có lập** lớp EC07 cho Họ Tên. Lý do: Theo slide (cách nhìn "risk-based" về tương đương), giá trị có `<`, `>`, `'`, `"` có thể đi vào nhánh xử lý khác (ghép vào câu truy vấn, hiển thị thành HTML), nên không tương đương với EC04.
- **Giới hạn quan sát trong FR-01:** Trang Đăng ký không hiển thị lại Họ Tên sau khi đăng ký, nên trong phạm vi FR-01 chỉ quan sát được: Đăng ký thành công hay bị từ chối, và có xuất hiện lỗi hệ thống hay không. Việc Họ Tên có được escape khi hiển thị (FR01-R24) chỉ kiểm chứng được ở trang khác có hiển thị tên, thuộc feature khác.
- **Không lập** lớp riêng cho Email chứa ký tự HTML hoặc SQL, vì các ký tự này hoặc đã làm email sai định dạng (rơi vào EC13 đến EC18), hoặc phụ thuộc quy tắc định dạng chưa chốt (A04).
- **Không lập** lớp riêng cho Mật khẩu, vì ký tự `'`, `"`, `<`, `>` đã thuộc EC38 hoặc EC40.

---

## 9. Tổng hợp (Complete Set of Partitions)

| Biến | Lớp hợp lệ | Lớp không hợp lệ | Lớp phụ thuộc giả định |
|---|---|---|---|
| IN1 Họ Tên | EC01, EC04 | EC02 | EC03, EC05, EC06, EC07 |
| IN2 Email | EC08, EC11, EC20 | EC09, EC10, EC13, EC14, EC15, EC17, EC18, EC21, EC22 | EC12, EC16, EC19, EC23 |
| IN3 Mật khẩu | EC24, EC26, EC28, EC31, EC34, EC36 | EC25, EC27, EC29, EC32, EC35, EC37 | EC30, EC33, EC38, EC39, EC40 |
| IN4 Xác nhận mật khẩu | EC41 | EC42 | EC43, EC44, EC45 |
| Output | EC46 | EC47 đến EC53 | |

Tổng: 53 lớp, gồm 12 lớp Input hợp lệ, 17 lớp Input không hợp lệ, 16 lớp phụ thuộc giả định, 8 lớp Output.

IN5 (danh sách email đã có) không có lớp riêng; ảnh hưởng của nó nằm trong EC20 đến EC23.

---

## 10. Điểm cần sinh viên quyết định khi review

Ngoài các giả định ở mục 7:

| # | Vấn đề | Các lựa chọn |
|---|---|---|
| 1 | Tập ký tự đặc biệt `@ $ ! % * ? &`: Có tách EC36 thành 7 lớp hợp lệ, mỗi ký tự một lớp không? Lý do có thể tách: Nhiều ký tự trong tập (`$`, `*`, `?`) là ký tự đặc biệt của biểu thức chính quy, nếu cài kiểm tra sai thì một số ký tự sẽ không được nhận | (a) Giữ 1 lớp, ở S3 hoặc S4 chọn đủ 7 ký tự làm giá trị thử; (b) Tách thành 7 lớp |
| 2 | Định dạng email: Giữ 6 lớp không hợp lệ (EC13 đến EC18) hay gộp thành 1 lớp như guideline "must be" cơ bản? | (a) Giữ 6 lớp; (b) Gộp 1 lớp |
| 3 | Giữ EC22 (trùng email vừa tạo bằng chức năng đăng ký) không? | (a) Giữ; (b) Bỏ, chỉ dùng EC21 |
| 4 | Giữ EC07 (Họ Tên chứa ký tự HTML hoặc SQL) với giới hạn quan sát ở mục 8 không? | (a) Giữ; (b) Bỏ, để cho feature có hiển thị tên |
