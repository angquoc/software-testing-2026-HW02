# Ví dụ: Feature FR-01 Đăng ký (EShop, Web)

Ví dụ rút gọn để minh họa mức chi tiết mong đợi. Chỉ theo **một biến** (Mật khẩu) đi qua S1 đến S4, kèm vài dòng bảng thay đổi.

Nguồn đầy đủ: `Homeworks/HW02/features/A_FR-01_DangKy/` (`00_spec.md` đến `04_bva.md`, `ai_raw/`). **Phiên đang làm feature khác không mở các file đó** nếu quy trình của dự án chỉ cho đọc thư mục feature đang làm; mọi thứ cần dùng đã tóm tắt ở đây.

## Đặc tả liên quan (trích)

> **Yêu cầu mật khẩu mạnh**: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).

Tách thành 5 yêu cầu có mã: `FR01-R06` (tối thiểu 8 ký tự) đến `FR01-R10` (ký tự đặc biệt trong tập).

## S1: Biến

| Mã | Biến | Tên trên giao diện | Trường API | Ràng buộc từ đặc tả | Yêu cầu |
|---|---|---|---|---|---|
| IN3 | Mật khẩu | "Mật khẩu" | `password` | Bắt buộc; tối thiểu 8 ký tự; ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự trong tập `@ $ ! % * ? &` | FR01-R03, FR01-R06 đến FR01-R10 |

Output lỗi: ERR5 (thiếu mật khẩu), ERR6 (không đạt yêu cầu mạnh, gộp 5 điều kiện ở phía Output vì đặc tả gọi chung).

## S2: Giả định và lớp (trích)

Câu hỏi mở đã thành giả định, sinh viên chốt:

| Mã | Câu hỏi | Phương án chọn |
|---|---|---|
| A08 | Độ dài tối đa | (a) Không giới hạn, không lập lớp độ dài trên |
| A09 | Tập ký tự đặc biệt đóng hay mở | (a) Đóng, vì đặc tả liệt kê cụ thể 7 ký tự |
| A10 | Ký tự ngoài 4 loại | (a) Cho phép; khoảng trắng là ký tự bình thường, không cắt, tính vào độ dài |
| A11 | Chữ có dấu có tính là chữ hoa, thường | (a) Chỉ `A-Z`, `a-z` |

| Mã | Điều kiện | Lớp | Loại | Đại diện | Kết quả |
|---|---|---|---|---|---|
| EC26 | Độ dài | Từ 8 ký tự | H | `Abcdef1!` | OUT1 |
| EC27 | Độ dài | Từ 1 đến 7 ký tự | KH | `Abcd1!` | ERR6 |
| EC36 | Ký tự đặc biệt | Có ký tự trong tập | H | `Abcdef1!` | OUT1 |
| EC38 | Ký tự đặc biệt | Ký tự đặc biệt duy nhất nằm ngoài tập | KH | `Abcdef1#` | ERR6 (A09) |
| EC68 | Độ dài | Chỉ đủ 8 ký tự khi tính khoảng trắng ở đầu hoặc cuối | H | `Abcde1!␣` | OUT1 (A10) |
| EC69 | Bắt buộc | Chỉ gồm khoảng trắng | H với điều kiện "bắt buộc" | 8 dấu cách | ERR6, không phải ERR5. Ngoại lệ: Không thể chỉ vi phạm một lớp |

Ghi chú cho S4: Cận dưới 8 (lớp hợp lệ), lớp không hợp lệ 1 đến 7; xét khoảng trắng ở đầu và ở cuối tại biên.

## S3: Test case (trích)

| TC | Lớp | Mật khẩu | Kết quả |
|---|---|---|---|
| TC-REG-01 | Các lớp cơ sở, EC36 (`!`) | `Abcdef1!` | OUT1 |
| TC-REG-02 đến TC-REG-07 | EC36, xoay vòng 6 ký tự còn lại vào các test case hợp lệ của Họ Tên | `Abcdef1@`, `Abcdef1$`... | OUT1 |
| TC-REG-50 | EC27 | `Abcd1!` | ERR6 |
| TC-REG-57 | EC38 | `Abcdef1#` | ERR6 |
| TC-REG-58 | EC69 (ngoại lệ) | 8 dấu cách | ERR6 (không phải ERR5) |
| TC-REG-76 | EC27 qua API | `Abcd1!` | Không trả về phản hồi thành công; gửi lại cùng email với dữ liệu hợp lệ để chứng minh chưa tạo tài khoản |

Giới hạn quan sát: Việc mật khẩu có khoảng trắng được lưu đúng nguyên văn chỉ kiểm được khi đăng nhập (feature khác), nên ghi thành rủi ro.

## S4: Biên của phân vùng độ dài Mật khẩu

| Điểm | Giá trị | Độ dài | Loại | Kết quả | Test case |
|---|---|---|---|---|---|
| Nhỏ nhất giao diện cho nhập | (để trống) | 0 | KH | ERR5 | TC-REG-49 (đã có) |
| Nhỏ nhất chỉ vi phạm độ dài | `Aa1!` | 4 | KH | ERR6 | TC-REG-106 |
| LB-1 | `Abcde1!` | 7 | KH | ERR6 | TC-REG-107 |
| LB | `Abcdef1!` | 8 | H | OUT1 | TC-REG-01 (đã có) |
| LB+1 | `Abcdefg1!` | 9 | H | OUT1 | TC-REG-108 |
| Giữa, UB | Không áp dụng | | | | Không có cận trên (A08) |
| Lớn nhất giao diện cho nhập | `Abcdef1!` + 992 chữ `a` | 1000 | H | OUT1, ghi số ký tự ô nhận | TC-REG-110 |
| LB, khoảng trắng ở đầu | `␣Abcde1!` | 8 | H | OUT1 | TC-REG-111 |

Không dùng mật khẩu 1 ký tự (LB của lớp 1 đến 7): Không thể đủ 4 loại ký tự nên vi phạm nhiều điều kiện cùng lúc.

## Bảng thay đổi (trích từ S4)

| Vị trí | Thay đổi | Loại | Lý do hoặc căn cứ |
|---|---|---|---|
| TC-REG-105 | Bỏ mật khẩu 1 ký tự | Thừa | Vi phạm nhiều điều kiện cùng lúc, không xác định được nguyên nhân. Sinh viên phát hiện |
| TC-REG-109 | Bỏ mật khẩu 20 ký tự làm điểm "giữa" | Thừa | Phân vùng không có cận trên nên không có điểm giữa; cùng lớp với 9 ký tự. Sinh viên phát hiện |
| Mục 4.1, TC-REG-131 | Thêm Họ Tên `␣A␣` | Thiếu | S2 đã ghi biến thể này cho S4, bản AI bỏ qua. Sinh viên phát hiện |
| TC-REG-124 | Bỏ Email là 1 dấu cách | Thừa | Qua giao diện, ô `type="email"` cắt thành rỗng nên trùng test case Email rỗng (một phiên AI khác phát hiện, sinh viên chuyển sang); qua API đã có test case 3 dấu cách (sinh viên quyết định) |
