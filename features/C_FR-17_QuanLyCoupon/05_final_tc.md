# S5: Bộ test case cuối cùng (FR-17 Quản lý mã giảm giá)

- Bước: S5 (Review lần cuối, bổ sung test case AI bỏ sót). Bản này do AI gộp `03_tc.md` và `04_bva.md`, đã đưa vào phần sinh viên bổ sung khi yêu cầu gộp (mục 13); sinh viên review và bổ sung tiếp ngay trong `05_final_tc.md`
- Thời gian tạo: 2026-10-20 21:35 (UTC+07:00)
- Bản gốc của AI: `ai_raw/S5_final_test_cases.md`. `05_final_tc.md` lúc tạo giống hệt bản này
- Căn cứ: `03_tc.md` (bản review S3, 78 test case), `04_bva.md` (bản review S4, 32 test case), `ai_raw/S3_test_cases.md` và `ai_raw/S4_bva.md` (để xác định nguồn gốc), `01_io.md` (câu hỏi của sinh viên ở S1), `02_ec.md` (lớp), `00_spec.md` (yêu cầu); cấu trúc theo `A_FR-01_DangKy/05_final_tc.md` (sinh viên cho phép tham khảo)

---

## 1. Cách gộp và quy ước

### 1.1 Nguồn gốc

| Giá trị | Nghĩa | Ứng với trường `origin` của skill `test-case-writing` |
|---|---|---|
| AI | Test case có trong bản AI (`ai_raw/S3_test_cases.md` hoặc `ai_raw/S4_bva.md`) và giữ nguyên nội dung | `AI` |
| AI có SV sửa | Test case có trong bản AI nhưng đã đổi giá trị kiểm, kết quả mong đợi, bước, hoặc ghi chú giới hạn; hoặc test case mới do AI (phiên này hay phiên khác) đề xuất khi review | `Both` |
| SV thêm | Test case mới do sinh viên phát hiện thiếu khi review, hoặc sinh viên tự viết ở S5 | `Human` |

Nhãn của từng test case chỉ xét dòng của chính nó. Thay đổi ở phần quy ước chung (mục 1.2) ghi nguồn gốc và người phát hiện ở dòng quy ước, không đổi nhãn của các test case dùng quy ước đó.

Chi tiết từng test case không phải "AI" (mã trong bản AI, đã đổi gì, ai phát hiện) ở mục 9.1.

Cột **"Phát hiện"** ghi ai phát hiện điều gì dẫn tới test case đó, kể cả khi nguồn gốc vẫn là "AI":

| Ghi | Nghĩa |
|---|---|
| AI | Không có thay đổi hay bổ sung nào khi review; test case và lớp nó phủ đều có trong bản AI |
| SV: ... | Sinh viên phát hiện, ghi bước và số câu hỏi hoặc quyết định |
| AI bổ sung ... | AI ở phiên thiết kế (Claude Code) tự bổ sung khi viết bản review hoặc khi gộp ở S5 |
| Claude phiên điều phối `305c705a` | Một phiên AI khác phát hiện khi soát lại, sinh viên chuyển sang |

Một test case có thể có nhiều người phát hiện; các phần cách nhau bằng dấu chấm.

Cột **"Vì sao AI bỏ sót"** chỉ điền cho test case không phải "AI" hoặc có phần do người khác phát hiện; ghi lý do bản AI chưa có nội dung đó. Thay đổi do sinh viên chọn phương án thì ghi "Không bỏ sót: Quyết định của SV".

### 1.2 Ký hiệu, kết quả mong đợi và quy ước chung

- `␣` là **một dấu cách**. Chuỗi dài viết dạng "`FR17TC125` + 991 chữ `X`", ghi độ dài.
- Mã test case giữ như `03_tc.md` và `04_bva.md`; test case thêm ở S5 đánh mã TC-CPN-140 trở đi.
- Mã yêu cầu viết tắt `Rnn` thay cho `FR17-Rnn`.

Output và loại lỗi (theo `01_io.md`, `02_ec.md`):

| Mã | Lớp | Ý nghĩa |
|---|---|---|
| OUT1 | EC96 | Thêm thành công qua giao diện: Bảng có dòng mới với đúng giá trị (tiền có `₫`, phân cách hàng nghìn); còn sau khi tải lại trang |
| OUT2 | EC97 | Thêm thành công qua API: 2xx; `GET /api/coupons` có mã với đúng giá trị |
| OUT3 | EC98 | Mã vừa tạo hiển thị lại đúng nguyên văn, dạng chữ (không bị hiểu thành HTML) |
| OUT4 | EC99 | Thông báo lỗi: Bằng tiếng Việt, chỉ ra đúng nguyên nhân, nằm **trên** nút "Tạo mã" |
| OUT5 | EC100 | Danh sách mã đủ cột, đúng giá trị |
| OUT6 | EC101 | Trang trống có icon hoặc hình minh họa và message thân thiện |
| OUT7 | EC102 | `GET /api/coupons` trả danh sách; mỗi mã đủ 6 trường và `id` |
| OUT8 | EC103 | Xóa thành công qua giao diện: Dòng biến mất, kể cả sau khi tải lại |
| OUT9 | EC104 | Xóa thành công qua API: 2xx; mã không còn trong `GET` |
| OUT10 | EC105 | Hủy ở hộp thoại xác nhận: Mã còn nguyên |
| ERR1 đến ERR11 | EC106 đến EC116 | ERR1 thiếu `code`; ERR2 `code` trùng; ERR3 thiếu `type`; ERR4 `type` ngoài tập; ERR5 thiếu `discount_value`; ERR6 `discount_value` không dương; ERR7 thiếu `expired_at`; ERR8 thiếu `min_order_amount`; ERR9 `min_order_amount` âm; ERR10 thiếu `max_uses_per_user`; ERR11 `max_uses_per_user` nhỏ hơn 1 |
| ERR12, ERR13 | EC117, EC118 | ERR12 chưa xác thực; ERR13 không đủ quyền |
| ERR14 | EC119 | Xóa mã không tồn tại |
| ERR15, ERR16 | EC120, EC121 | ERR15 sai kiểu hoặc sai định dạng; ERR16 request không đọc được |
| ERR17, ERR20, ERR22 | EC122, EC125, EC127 | ERR17 `percent` lớn hơn 100; ERR20 `max_uses_per_user` không phải số nguyên; ERR22 vượt giới hạn mà đặc tả không nêu (thông báo phải chỉ ra trường) |

Đặc tả không nêu câu chữ thông báo nào, nên kết quả mong đợi chỉ ghi nguyên nhân.

Quy trình và kết quả mong đợi chung:

| Mã | Áp cho | Nội dung | Nguồn gốc | Phát hiện |
|---|---|---|---|---|
| QT-GD | Thêm qua giao diện | Nhập 6 ô theo bảng, bấm "Tạo mã" | AI | AI |
| KQ-H-GD | Lớp hợp lệ qua giao diện | OUT1, kiểm bằng tải lại trang (K1). Thông báo thành công, form có được xóa không: Ghi lại, không bắt buộc (A19) | AI | AI |
| KQ-KH-GD | Lớp không hợp lệ qua giao diện | Không có dòng mới, kể cả sau khi tải lại trang (K3; không dùng K4); OUT4 với đúng mã ERR của test case. Bong bóng của trình duyệt cũng tính là thông báo nhưng vẫn xét vị trí (A21); ghi lại ngôn ngữ trình duyệt nếu thông báo là bong bóng | AI có SV sửa | SV: Chỉ dùng K3 (S3, quyết định 1). AI bổ sung khi review S3: Thông báo phải bằng tiếng Việt (R14) |
| KQ-H-API | Lớp hợp lệ qua API | OUT2; kiểm giá trị từng trường qua `GET`. Nếu `GET` không trả đủ trường (A17), kiểm trên bảng của giao diện và ghi giới hạn GH11 | AI có SV sửa | SV: Kiểm từng trường (S3, quyết định 5). AI bổ sung khi review S3: Cách kiểm thay thế |
| KQ-KH-API | Lớp không hợp lệ qua API | 4xx, không phải 5xx (A20); mã của test case không có trong `GET` (hoặc số mã không đổi). Ghi lại mã trạng thái và body thực tế | AI | SV: Hỏi đặc tả có nêu mã HTTP không (S1, câu 3), dẫn tới giả định A20 |

Mọi phản hồi 5xx đều là "Sai". Kết quả khác **giả định** (không phải khác đặc tả) ghi trạng thái "Khác giả định" kèm mã giả định, xét ở S7 trước khi coi là bug (S4, quyết định 7).

### 1.3 Tiền điều kiện chung

- Giao diện: Đăng nhập Web Admin `http://localhost:5174` bằng `admin@eshop.com` / `Admin123!`, mở menu "Mã Giảm Giá". Ghi trình duyệt, phiên bản, múi giờ, ngày chạy ở S6.
- Dữ liệu đã reset về dữ liệu mẫu (4 mã `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`).
- API: Base URL `http://localhost:3000`. Token lấy bằng `POST /api/login`: Token admin dùng `admin@eshop.com`; token user thường dùng `test@eshop.com` / `Test1234!`. Header mặc định `Content-Type: application/json`, `Authorization: Bearer <token admin>`.

### 1.4 Giá trị cơ sở

| Input | Giao diện | API |
|---|---|---|
| `code` | `FR17TCNN` (NN là số test case; dòng của test case dạng bảng thêm `A`, `B`, `C`...) | `"FR17TCNN"` |
| `type` | "Phần trăm (%)" | `"percent"` |
| `discount_value` | `15` (với "Số tiền cố định (₫)" là `50000`) | `15` |
| `min_order_amount` | `300000` | `300000` |
| `expired_at` | `12/31/2099` | `"2099-12-31"` |
| `max_uses_per_user` | `3` | `3` |

Body API cơ sở:

```json
{"code": "FR17TCNN", "type": "percent", "discount_value": 15, "min_order_amount": 300000, "expired_at": "2099-12-31", "max_uses_per_user": 3}
```

---

## 2. Tổng hợp

| Nhóm | Mã | Số TC | AI | AI có SV sửa | SV thêm | Có phần do SV phát hiện |
|---|---|---|---|---|---|---|
| TS-01 Thêm hợp lệ qua giao diện (EP) | TC-CPN-01 đến TC-CPN-25 | 25 | 20 | 5 | 0 | 2 |
| TS-02 Thêm không hợp lệ qua giao diện (EP) | TC-CPN-30 đến TC-CPN-46 | 17 | 13 | 4 | 0 | 1 |
| TS-03 Xem, Xóa qua giao diện (EP) | TC-CPN-50 đến TC-CPN-56 | 7 | 6 | 1 | 0 | 2 |
| TS-04 Giá trị biên qua giao diện (BVA) | TC-CPN-100 đến TC-CPN-117, TC-CPN-119 đến TC-CPN-129 | 29 | 25 | 4 | 0 | 1 |
| TS-05 API (EP, BVA) | TC-CPN-60 đến TC-CPN-82, TC-CPN-118, TC-CPN-130, TC-CPN-131, TC-CPN-140 đến TC-CPN-142 | 29 | 22 | 4 | 3 | 8 |
| TS-06 Checklist giao diện | TC-CPN-90 đến TC-CPN-95 | 6 | 6 | 0 | 0 | 0 |
| **Tổng** | | **113** | **92** | **18** | **3** | **14** |

Cột cuối đếm test case mà cột "Phát hiện" có phần ghi "SV". Trong 14 test case đó có 6 test case vẫn mang nguồn gốc "AI" vì đã có trong bản AI, nhưng lớp chúng phủ bắt nguồn từ câu hỏi của sinh viên ở S1 (mục 9.2): TC-CPN-53, TC-CPN-55, TC-CPN-69, TC-CPN-70, TC-CPN-71, TC-CPN-73.

Theo kỹ thuật: 80 test case Domain Testing (EP) và checklist (78 từ S3, TC-CPN-140, TC-CPN-141 thêm ở S5), 33 test case BVA (32 từ S4, TC-CPN-142 thêm ở S5). Có điều kiện: TC-CPN-52 không áp dụng nếu không có hộp thoại xác nhận (A07); TC-CPN-82, TC-CPN-130 chỉ chạy các dòng cần thiết.

---

## 3. TS-01: Thêm mã hợp lệ qua giao diện (EP)

Quy trình QT-GD; kết quả KQ-H-GD cộng phần ghi ở cột "Kết quả mong đợi".

| TC | Tiêu đề | Lớp | Yêu cầu | `code` | `type` | `discount_value` | `min_order_amount` | `expired_at` | `max_uses_per_user` | Kết quả mong đợi | Nguồn gốc | Phát hiện | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-CPN-01 | Kiểm tra tạo mã thành công với dữ liệu hợp lệ cơ sở, loại phần trăm | EC01, EC08, EC15, EC24, EC30, EC44, EC53, EC62, EC82 | R01, R02, R04 đến R10, R14 | `FR17TC01` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; dòng hiện `FR17TC01`, "Phần trăm", `15%`, `300,000 ₫`, `2099-12-31`, `3 lần` | AI | AI | |
| TC-CPN-02 | Kiểm tra tạo mã thành công với dữ liệu hợp lệ cơ sở, loại số tiền cố định | EC25, EC35 | R01, R06, R07, R14 | `FR17TC02` | Số tiền cố định (₫) | `50000` | `300000` | `12/31/2099` | `3` | OUT1; cột "Giá trị" hiện `50,000 ₫` | AI | AI | |
| TC-CPN-03 | Kiểm tra tạo mã thành công khi Mã có dấu cách ở đầu | EC04 | R04, R05 | `␣FR17TC03` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện `FR17TC03`. K5: Tạo lại `FR17TC03`, mong đợi ERR2 | AI | AI | |
| TC-CPN-04 | Kiểm tra tạo mã thành công khi Mã có dấu cách ở cuối | EC05 | R04, R05 | `FR17TC04␣` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện `FR17TC04`. K5: Tạo lại `FR17TC04`, mong đợi ERR2 | AI | AI | |
| TC-CPN-05 | Kiểm tra tạo mã thành công khi Mã có dấu cách ở giữa | EC06 | R01 | `FR17␣TC05` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" giữ dấu cách ở giữa. K5: Tạo `FR17TC05`, mong đợi OUT1 (mã khác) | AI | AI | |
| TC-CPN-06 | Kiểm tra tạo mã thành công khi Mã gõ bằng chữ thường | EC07 | R01, R05 | `fr17tc06` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện `fr17tc06` hoặc `FR17TC06` (A10). K5: Tạo lại `FR17TC06`, mong đợi ERR2. Giới hạn GH9: Lớp EC07 kiểm thật ở TC-CPN-140 | AI có SV sửa | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ (S5) | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |
| TC-CPN-07 | Kiểm tra tạo mã thành công khi Mã chỉ gồm chữ số có số 0 ở đầu | EC09 | R01, R15 | `0017007` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện đúng `0017007` | AI | AI | |
| TC-CPN-08 | Kiểm tra tạo mã thành công khi Mã có dấu gạch ngang và gạch dưới | EC10 | R01 | `FR17-TC_08` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện đúng `FR17-TC_08` | AI | AI | |
| TC-CPN-09 | Kiểm tra tạo mã thành công khi Mã có chữ tiếng Việt có dấu | EC11 | R01, R15 | `TẾTFR17TC09` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện đúng ký tự, không thành ký tự lạ | AI | AI | |
| TC-CPN-10 | Kiểm tra Mã có thẻ HTML được hiển thị dạng chữ | EC12 | R15 | `<b>FR17TC10</b>` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; cột "Mã" hiện nguyên chuỗi dạng chữ, `<b>FR17TC10</b>` hoặc `<B>FR17TC10</B>` (ô tự chuyển chữ hoa) đều đạt; chữ không in đậm (OUT3). Giới hạn GH9 | AI có SV sửa | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ (S5). AI bổ sung ở S5: Hệ quả với chuỗi HTML (thẻ HTML không phân biệt hoa thường nên vẫn kiểm được escape) | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |
| TC-CPN-11 | Kiểm tra Mã có ký tự SQL được lưu nguyên văn | EC13 | R16 | `FR17TC11'OR'1` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; hiện nguyên văn; 4 mã mẫu giữ nguyên. K2: Tạo lại đúng chuỗi, mong đợi ERR2. Giới hạn GH4 | AI | AI | |
| TC-CPN-12 | Kiểm tra tạo mã với Mã dài 255 ký tự | EC14 | R01 | `FR17TC12` + 247 chữ `X` (255 ký tự) | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | Đạt nếu OUT1 với đủ 255 ký tự, hoặc ERR22 có thông báo rõ. Sai nếu lưu cắt cụt, lỗi máy chủ. Ghi số ký tự ô nhận. Giới hạn GH5, GH10 | AI | AI | |
| TC-CPN-13 | Kiểm tra tạo lại được mã trùng với mã đã bị xóa | EC21, EC71 | R03, R05 | `FR17TC13` (bước 1 tạo, bước 2 xóa, bước 3 tạo lại) | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | Bước 3: OUT1 (A16). K8 | AI | AI | |
| TC-CPN-14 | Kiểm tra tạo mã thành công khi giá trị phần trăm bằng 100 | EC31 | R07 | `FR17TC14` | Phần trăm (%) | `100` | `300000` | `12/31/2099` | `3` | OUT1; hiện `100%` | AI | AI | |
| TC-CPN-15 | Kiểm tra tạo mã thành công khi giá trị phần trăm là số thập phân | EC34 | R07 | `FR17TC15` | Phần trăm (%) | `12.5` | `300000` | `12/31/2099` | `3` | OUT1; hiện `12.5%`. Nếu trình duyệt chặn, chạy dòng A của TC-CPN-82. Giới hạn GH2 | AI có SV sửa | AI bổ sung khi review S3: Trỏ đúng dòng của TC-CPN-82 | Bản AI chỉ ghi "dòng tương ứng" |
| TC-CPN-16 | Kiểm tra tạo mã thành công khi số tiền cố định là số thập phân | EC37 | R07 | `FR17TC16` | Số tiền cố định (₫) | `1000.5` | `300000` | `12/31/2099` | `3` | OUT1; ghi cách hiển thị; K6: `GET` có `1000.5`. Nếu trình duyệt chặn, chạy dòng B của TC-CPN-82. Giới hạn GH1, GH2 | AI có SV sửa | AI bổ sung khi review S3: Trỏ đúng dòng của TC-CPN-82 | Bản AI chỉ ghi "chạy TC-CPN-82", không nói dòng nào |
| TC-CPN-17 | Kiểm tra tạo mã thành công khi số tiền cố định lớn hơn đơn tối thiểu | EC38 | R07, R09 | `FR17TC17` | Số tiền cố định (₫) | `500000` | `300000` | `12/31/2099` | `3` | OUT1 (A12) | AI | AI | |
| TC-CPN-18 | Kiểm tra tạo mã với số tiền cố định rất lớn | EC39 | R07 | `FR17TC18` | Số tiền cố định (₫) | `10000000000000000` | `300000` | `12/31/2099` | `3` | Đạt nếu OUT1 hiện đúng `10,000,000,000,000,000 ₫`, hoặc ERR22 có thông báo rõ. Sai nếu hiển thị, lưu giá trị khác, lỗi máy chủ. K6. Giới hạn GH5, GH8 | AI | AI | |
| TC-CPN-19 | Kiểm tra tạo mã thành công khi đơn tối thiểu bằng 0 | EC45 | R09 | `FR17TC19` | Phần trăm (%) | `15` | `0` | `12/31/2099` | `3` | OUT1; hiện `0 ₫` | AI | AI | |
| TC-CPN-20 | Kiểm tra tạo mã thành công khi đơn tối thiểu là số thập phân | EC47 | R09 | `FR17TC20` | Phần trăm (%) | `15` | `1000.5` | `12/31/2099` | `3` | OUT1; ghi cách hiển thị; K6: `GET` có `1000.5`. Nếu trình duyệt chặn, chạy dòng C của TC-CPN-82. Giới hạn GH1, GH2 | AI có SV sửa | AI bổ sung khi review S3: Trỏ đúng dòng của TC-CPN-82 | Bản AI chỉ ghi "chạy TC-CPN-82", không nói dòng nào |
| TC-CPN-21 | Kiểm tra tạo mã với đơn tối thiểu rất lớn | EC48 | R09 | `FR17TC21` | Phần trăm (%) | `15` | `10000000000000000` | `12/31/2099` | `3` | Như TC-CPN-18, với cột "Đơn tối thiểu". K6. Giới hạn GH5, GH8 | AI | AI | |
| TC-CPN-22 | Kiểm tra tạo mã có ngày hết hạn là hôm nay | EC54, EC83 | R02, R08 | `FR17TC22` | Phần trăm (%) | `15` | `300000` | Ngày chạy | `3` | OUT1 (A05); cột "Hết hạn" hiện chữ "Hết hạn" (A18). Giới hạn GH6 | AI | AI | |
| TC-CPN-23 | Kiểm tra tạo mã có ngày hết hạn trong quá khứ | EC55, EC84 | R02, R08 | `FR17TC23` | Phần trăm (%) | `15` | `300000` | `01/31/2025` | `3` | OUT1 (A05); hiện chữ "Hết hạn". Giới hạn GH6 | AI | AI | |
| TC-CPN-24 | Kiểm tra tạo mã có ngày hết hạn là 29 tháng 2 năm nhuận | EC57 | R08 | `FR17TC24` | Phần trăm (%) | `15` | `300000` | `02/29/2028` | `3` | OUT1; hiện `2028-02-29` | AI | AI | |
| TC-CPN-25 | Kiểm tra tạo mã với số lần dùng tối đa rất lớn | EC65 | R10 | `FR17TC25` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `10000000000000000` | Như TC-CPN-18, với cột "Giới hạn/người". K6. Giới hạn GH5, GH8 | AI | AI | |

---

## 4. TS-02: Thêm mã không hợp lệ qua giao diện (EP)

Quy trình QT-GD; kết quả KQ-KH-GD với mã lỗi ở cột "Kết quả mong đợi". Mỗi test case chỉ vi phạm đúng một lớp không hợp lệ.

| TC | Tiêu đề | Lớp | Yêu cầu | `code` | `type` | `discount_value` | `min_order_amount` | `expired_at` | `max_uses_per_user` | Kết quả mong đợi | Nguồn gốc | Phát hiện | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-CPN-30 | Kiểm tra tạo mã bị từ chối khi Mã để trống | EC02 | R04, R13 | (để trống) | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR1. Giới hạn GH3 | AI | AI | |
| TC-CPN-31 | Kiểm tra tạo mã bị từ chối khi Mã chỉ gồm 3 dấu cách | EC03 | R04, R13 | `␣␣␣` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR1. Giới hạn GH3 | AI | AI | |
| TC-CPN-32 | Kiểm tra tạo mã bị từ chối khi Mã trùng mã mẫu | EC16 | R05, R13 | `SAVE10` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR2; dòng `SAVE10` cũ giữ nguyên. Giới hạn GH3 | AI | AI | |
| TC-CPN-33 | Kiểm tra tạo mã bị từ chối khi Mã trùng mã vừa tạo | EC17 | R05, R13 | `FR17TC33` (tạo 2 lần) | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | Lần 1: OUT1. Lần 2: ERR2; bảng chỉ có một dòng `FR17TC33`. Giới hạn GH3 | AI | AI | |
| TC-CPN-34 | Kiểm tra tạo mã bị từ chối khi Mã chỉ khác mã mẫu ở chữ hoa, chữ thường | EC18 | R05, R13 | `save10` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR2. Giới hạn GH3, GH9: Lớp EC18 kiểm thật ở TC-CPN-141 | AI có SV sửa | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ (S5) | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |
| TC-CPN-35 | Kiểm tra tạo mã bị từ chối khi Mã trùng mã mẫu sau khi cắt dấu cách | EC19 | R05, R13 | `␣SAVE10` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR2. Giới hạn GH3 | AI | AI | |
| TC-CPN-36 | Kiểm tra tạo mã bị từ chối khi Mã trùng mã đã hết hạn | EC20 | R05, R13 | `EXPIRED` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR2. Chạy trước TC-CPN-55. Giới hạn GH3 | AI | AI | |
| TC-CPN-37 | Kiểm tra tạo mã bị từ chối khi giá trị phần trăm là 150 | EC32 | R07, R13 | `FR17TC37` | Phần trăm (%) | `150` | `300000` | `12/31/2099` | `3` | ERR17. Giới hạn GH3 | AI | AI | |
| TC-CPN-38 | Kiểm tra tạo mã bị từ chối khi giá trị phần trăm bằng 0 | EC33 | R07, R13 | `FR17TC38` | Phần trăm (%) | `0` | `300000` | `12/31/2099` | `3` | ERR6. Giới hạn GH3 | AI | AI | |
| TC-CPN-39 | Kiểm tra tạo mã bị từ chối khi số tiền cố định bằng 0 | EC36 | R07, R13 | `FR17TC39` | Số tiền cố định (₫) | `0` | `300000` | `12/31/2099` | `3` | ERR6. Giới hạn GH3 | AI | AI | |
| TC-CPN-40 | Kiểm tra tạo mã bị từ chối khi giá trị giảm để trống | EC40 | R07, R13 | `FR17TC40` | Phần trăm (%) | (để trống) | `300000` | `12/31/2099` | `3` | ERR5. Giới hạn GH3 | AI | AI | |
| TC-CPN-41 | Kiểm tra tạo mã bị từ chối khi đơn tối thiểu âm | EC46 | R09, R13 | `FR17TC41` | Phần trăm (%) | `15` | `-1` | `12/31/2099` | `3` | ERR9. Nếu trình duyệt chặn, chạy dòng E của TC-CPN-82. Giới hạn GH2, GH3 | AI có SV sửa | AI bổ sung khi review S3: Trỏ đúng dòng của TC-CPN-82 | Bản AI chỉ ghi "dòng tương ứng" |
| TC-CPN-42 | Kiểm tra tạo mã bị từ chối khi đơn tối thiểu để trống | EC49 | R09, R13 | `FR17TC42` | Phần trăm (%) | `15` | (xóa `0`, để trống) | `12/31/2099` | `3` | ERR8. Giới hạn GH3 | AI | AI | |
| TC-CPN-43 | Kiểm tra tạo mã bị từ chối khi ngày hết hạn để trống | EC56 | R08, R13 | `FR17TC43` | Phần trăm (%) | `15` | `300000` | (để trống) | `3` | ERR7. Giới hạn GH3 | AI | AI | |
| TC-CPN-44 | Kiểm tra tạo mã bị từ chối khi số lần dùng tối đa bằng 0 | EC63 | R10, R13 | `FR17TC44` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `0` | ERR11. Nếu trình duyệt chặn, chạy dòng F của TC-CPN-82. Giới hạn GH2, GH3 | AI có SV sửa | AI bổ sung khi review S3: Thêm dự phòng qua API (dòng F) | Bản AI ghi dòng F không khớp với giá trị `0` của test case này |
| TC-CPN-45 | Kiểm tra tạo mã bị từ chối khi số lần dùng tối đa là số thập phân | EC64 | R10, R13 | `FR17TC45` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `1.5` | ERR20. Nếu trình duyệt chặn, chạy dòng D của TC-CPN-82. Giới hạn GH2, GH3 | AI có SV sửa | AI bổ sung khi review S3: Trỏ đúng dòng của TC-CPN-82 | Bản AI chỉ ghi "chạy TC-CPN-82", không nói dòng nào |
| TC-CPN-46 | Kiểm tra tạo mã bị từ chối khi số lần dùng tối đa để trống | EC66 | R10, R13 | `FR17TC46` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | (xóa `1`, để trống) | ERR10. Giới hạn GH3 | AI | AI | |

---

## 5. TS-03: Xem và Xóa qua giao diện (EP)

| TC | Tiêu đề | Lớp | Yêu cầu | Bước | Kết quả mong đợi | Nguồn gốc | Phát hiện | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|
| TC-CPN-50 | Kiểm tra danh sách hiển thị đúng 4 mã mẫu | EC80, EC82, EC84 | R02, R14 | Ngay sau khi reset, mở trang "Mã Giảm Giá" | OUT5: 4 dòng `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`, đủ 7 cột, khớp bảng mã mẫu FR-09; tiền có `₫` và phân cách hàng nghìn; `SAVE10` hiện `2099-12-31`; `EXPIRED` hiện chữ "Hết hạn". Giới hạn GH6 | AI | AI | |
| TC-CPN-51 | Kiểm tra xóa mã vừa tạo | EC71, EC78 | R03 | 1. Tạo `FR17TC51`. 2. Bấm "Xóa" trên dòng đó; nếu có hộp thoại thì chọn đồng ý | OUT8; các dòng khác giữ nguyên. K7: Tải lại, dòng không còn. K8: Tạo lại `FR17TC51`, mong đợi OUT1 | AI | AI | |
| TC-CPN-52 | Kiểm tra hủy ở hộp thoại xác nhận xóa | EC79 | R03 | 1. Tạo `FR17TC52`. 2. Bấm "Xóa", chọn hủy | OUT10: Dòng còn nguyên sau khi tải lại. Không áp dụng nếu không có hộp thoại (A07) | AI | AI | |
| TC-CPN-53 | Kiểm tra xóa mã đã bị xóa ở tab khác | EC76 | R03 | 1. Tạo `FR17TC53`. 2. Mở trang ở tab thứ hai. 3. Ở tab 1, xóa `FR17TC53`. 4. Ở tab 2 (chưa tải lại), bấm "Xóa" trên dòng `FR17TC53` | Bước 4: Báo lỗi (ERR14) hoặc tự cập nhật danh sách đều đạt (A24); các mã khác không đổi sau khi tải lại | AI | SV: Hỏi biến gián tiếp của thao tác Xóa (S1, câu 1), dẫn tới IN13 và lớp EC76 | |
| TC-CPN-54 | Kiểm tra xóa mã mẫu còn hạn | EC70 | R03 | Bấm "Xóa" trên dòng `BIGBUY` | OUT8; tải lại, `BIGBUY` không còn; 3 mã mẫu còn lại giữ nguyên. **Phá dữ liệu mẫu**, chạy ở nhóm cuối | AI | AI | |
| TC-CPN-55 | Kiểm tra xóa mã mẫu đã hết hạn | EC72 | R03 | Bấm "Xóa" trên dòng `EXPIRED` | OUT8; tải lại, `EXPIRED` không còn. **Phá dữ liệu mẫu**, chạy sau TC-CPN-36, TC-CPN-50 | AI | SV: Hỏi biến gián tiếp của thao tác Xóa (S1, câu 1), dẫn tới IN13 và lớp EC72 | |
| TC-CPN-56 | Kiểm tra trang trống khi không còn mã nào | EC81 | R02, R18 | 1. Reset dữ liệu mẫu (chỉ còn 4 mã). 2. Xóa lần lượt 4 mã. 3. Tải lại trang | OUT6; `GET /api/coupons` trả danh sách rỗng (OUT7). **Chạy cuối cùng**, sau một lần reset riêng; reset ngay sau đó | AI có SV sửa | AI bổ sung khi review S3: Reset riêng trước khi chạy | Bản AI để test case chạy sau mọi test case khác, khi danh sách có hàng chục mã phải xóa tay |

---

## 6. TS-04: Giá trị biên qua giao diện (BVA)

Quy trình QT-GD. Phân vùng P1 đến P6 theo `04_bva.md` mục 2. Cột "Biên" ghi phân vùng và điểm.

| TC | Tiêu đề | Biên | Yêu cầu | `code` | `type` | `discount_value` | `min_order_amount` | `expired_at` | `max_uses_per_user` | Kết quả mong đợi | Nguồn gốc | Phát hiện | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-CPN-100 | Kiểm tra tạo mã bị từ chối khi giá trị phần trăm là -1 | P1, giá trị âm (EC33) | R07 | `FR17TC100` | Phần trăm (%) | `-1` | `300000` | `12/31/2099` | `3` | ERR6. Dự phòng: TC-CPN-130 dòng A. Giới hạn GH2, GH3 | AI | AI | |
| TC-CPN-101 | Kiểm tra tạo mã thành công khi giá trị phần trăm là 0.01 | P1, LB theo bước 0.01 (EC34) | R07 | `FR17TC101` | Phần trăm (%) | `0.01` | `300000` | `12/31/2099` | `3` | OUT1; hiện `0.01%`. Dự phòng: TC-CPN-130 dòng B. Giới hạn GH1, GH2 | AI | AI | |
| TC-CPN-102 | Kiểm tra tạo mã thành công khi giá trị phần trăm là 1 | P1, LB (EC30) | R07 | `FR17TC102` | Phần trăm (%) | `1` | `300000` | `12/31/2099` | `3` | OUT1; hiện `1%` | AI | AI | |
| TC-CPN-103 | Kiểm tra tạo mã thành công khi giá trị phần trăm là 2 | P1, LB+1 (EC30) | R07 | `FR17TC103` | Phần trăm (%) | `2` | `300000` | `12/31/2099` | `3` | OUT1; hiện `2%` | AI | AI | |
| TC-CPN-104 | Kiểm tra tạo mã thành công khi giá trị phần trăm là 99 | P1, UB-1 (EC30) | R07 | `FR17TC104` | Phần trăm (%) | `99` | `300000` | `12/31/2099` | `3` | OUT1; hiện `99%` | AI | AI | |
| TC-CPN-105 | Kiểm tra tạo mã bị từ chối khi giá trị phần trăm là 100.01 | P1, UB theo bước 0.01 (EC32) | R07 | `FR17TC105` | Phần trăm (%) | `100.01` | `300000` | `12/31/2099` | `3` | ERR17. Dự phòng: TC-CPN-130 dòng C. Giới hạn GH2, GH3 | AI | AI | |
| TC-CPN-106 | Kiểm tra tạo mã bị từ chối khi giá trị phần trăm là 101 | P1, UB+1 (EC32) | R07 | `FR17TC106` | Phần trăm (%) | `101` | `300000` | `12/31/2099` | `3` | ERR17. Giới hạn GH3 | AI | AI | |
| TC-CPN-107 | Kiểm tra tạo mã bị từ chối khi số tiền cố định là -1 | P2, giá trị âm (EC36) | R07 | `FR17TC107` | Số tiền cố định (₫) | `-1` | `300000` | `12/31/2099` | `3` | ERR6. Dự phòng: TC-CPN-130 dòng D. Giới hạn GH2, GH3 | AI | AI | |
| TC-CPN-108 | Kiểm tra tạo mã thành công khi số tiền cố định là 0.01 | P2, LB theo bước 0.01 (EC37) | R07 | `FR17TC108` | Số tiền cố định (₫) | `0.01` | `300000` | `12/31/2099` | `3` | OUT1; ghi cách hiển thị; K6 có `0.01`. Dự phòng: TC-CPN-130 dòng E. Giới hạn GH1, GH2 | AI | AI | |
| TC-CPN-109 | Kiểm tra tạo mã thành công khi số tiền cố định là 1 | P2, LB (EC35) | R07 | `FR17TC109` | Số tiền cố định (₫) | `1` | `300000` | `12/31/2099` | `3` | OUT1; hiện `1 ₫` | AI | AI | |
| TC-CPN-110 | Kiểm tra tạo mã thành công khi số tiền cố định là 2 | P2, LB+1 (EC35) | R07 | `FR17TC110` | Số tiền cố định (₫) | `2` | `300000` | `12/31/2099` | `3` | OUT1; hiện `2 ₫` | AI | AI | |
| TC-CPN-111 | Kiểm tra số tiền cố định 2^53 + 1 được lưu chính xác | P2, lớn nhất (độ chính xác) (EC39) | R07 | `FR17TC111` | Số tiền cố định (₫) | `9007199254740993` | `300000` | `12/31/2099` | `3` | Đạt nếu OUT1 hiện đúng `9,007,199,254,740,993 ₫` và K6 có đúng giá trị, hoặc ERR22 có thông báo rõ. Sai nếu hiện hoặc lưu `...992`, lỗi máy chủ. Chạy cùng TC-CPN-131 dòng A. Giới hạn GH5, GH7 | AI có SV sửa | Claude phiên điều phối `305c705a`: Giá trị có thể bị làm tròn trước khi gửi | Bản AI coi kết quả qua giao diện là kết quả của hệ thống, chưa xét việc làm tròn ở trình duyệt hoặc mã của trang |
| TC-CPN-112 | Kiểm tra tạo mã bị từ chối khi đơn tối thiểu là -0.01 | P3, LB-1 theo bước 0.01 (EC46) | R09 | `FR17TC112` | Phần trăm (%) | `15` | `-0.01` | `12/31/2099` | `3` | ERR9. Dự phòng: TC-CPN-130 dòng F. Giới hạn GH2, GH3 | AI | AI | |
| TC-CPN-113 | Kiểm tra tạo mã thành công khi đơn tối thiểu là 1 | P3, LB+1 (EC44) | R09 | `FR17TC113` | Phần trăm (%) | `15` | `1` | `12/31/2099` | `3` | OUT1; hiện `1 ₫` | AI | AI | |
| TC-CPN-114 | Kiểm tra đơn tối thiểu 2^53 + 1 được lưu chính xác | P3, lớn nhất (độ chính xác) (EC48) | R09 | `FR17TC114` | Phần trăm (%) | `15` | `9007199254740993` | `12/31/2099` | `3` | Như TC-CPN-111, với cột "Đơn tối thiểu". Chạy cùng TC-CPN-131 dòng B. Giới hạn GH5, GH7 | AI có SV sửa | Claude phiên điều phối `305c705a`: Giá trị có thể bị làm tròn trước khi gửi | Như TC-CPN-111 |
| TC-CPN-115 | Kiểm tra tạo mã bị từ chối khi số lần dùng tối đa là -1 | P4, giá trị âm (EC63) | R10 | `FR17TC115` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `-1` | ERR11. Dự phòng: TC-CPN-130 dòng G. Giới hạn GH2, GH3 | AI | AI | |
| TC-CPN-116 | Kiểm tra tạo mã thành công khi số lần dùng tối đa là 1 | P4, LB (EC62) | R10 | `FR17TC116` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `1` (gõ lại, không để mặc định) | OUT1; hiện `1 lần` | AI | AI | |
| TC-CPN-117 | Kiểm tra tạo mã thành công khi số lần dùng tối đa là 2 | P4, LB+1 (EC62) | R10 | `FR17TC117` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `2` | OUT1; hiện `2 lần` | AI | AI | |
| TC-CPN-119 | Kiểm tra số lần dùng tối đa 2^53 + 1 được lưu chính xác | P4, lớn nhất (độ chính xác) (EC65) | R10 | `FR17TC119` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `9007199254740993` | Như TC-CPN-111, với cột "Giới hạn/người". Chạy cùng TC-CPN-131 dòng C. Giới hạn GH5, GH7 | AI có SV sửa | Claude phiên điều phối `305c705a`: Giá trị có thể bị làm tròn trước khi gửi | Như TC-CPN-111 |
| TC-CPN-120 | Kiểm tra tạo mã bị từ chối khi Mã là 1 dấu cách | P5, LB-1 sau khi cắt (EC03) | R04 | `␣` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | ERR1. Giới hạn GH3 | AI | AI | |
| TC-CPN-121 | Kiểm tra tạo mã thành công khi Mã dài 1 ký tự | P5, LB (EC01) | R01, R04 | `Q` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; hiện `Q` | AI | AI | |
| TC-CPN-122 | Kiểm tra tạo mã thành công khi Mã 1 ký tự có dấu cách hai bên | P5, LB có khoảng trắng (EC04, EC05) | R01, R04 | `␣K␣` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; hiện `K`. K5: Tạo lại `K`, mong đợi ERR2 | AI | AI | |
| TC-CPN-123 | Kiểm tra tạo mã thành công khi Mã là 1 chữ thường | P5, LB chữ thường (EC07) | R01, R04 | `j` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; hiện `j` hoặc `J` (A10). Giới hạn GH9: Điểm này kiểm thật ở TC-CPN-142 | AI có SV sửa | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ (S5) | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |
| TC-CPN-124 | Kiểm tra tạo mã thành công khi Mã dài 2 ký tự | P5, LB+1 (EC01) | R01, R04 | `QZ` | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | OUT1; hiện `QZ` | AI | AI | |
| TC-CPN-125 | Kiểm tra tạo mã với Mã dài 1000 ký tự | P5, lớn nhất giao diện cho nhập (EC14) | R01 | `FR17TC125` + 991 chữ `X` (1000 ký tự) | Phần trăm (%) | `15` | `300000` | `12/31/2099` | `3` | Đạt nếu OUT1 đủ 1000 ký tự, hoặc ERR22 có thông báo rõ. Sai nếu cắt cụt, lỗi máy chủ. Ghi số ký tự ô nhận. Giới hạn GH5, GH10 | AI | AI | |
| TC-CPN-126 | Kiểm tra tạo mã có ngày hết hạn 01/01/0001 | P6, nhỏ nhất giao diện cho nhập (EC55) | R02, R08 | `FR17TC126` | Phần trăm (%) | `15` | `300000` | `01/01/0001` | `3` | OUT1; hiện chữ "Hết hạn". Ghi lại nếu ô không cho nhập năm này. Giới hạn GH6 | AI | AI | |
| TC-CPN-127 | Kiểm tra mã có ngày hết hạn là hôm qua hiện chữ "Hết hạn" | P6, hôm qua (EC55, EC84) | R02, R08 | `FR17TC127` | Phần trăm (%) | `15` | `300000` | Ngày chạy trừ 1 | `3` | OUT1; hiện chữ "Hết hạn". Giới hạn GH6 | AI | AI | |
| TC-CPN-128 | Kiểm tra mã có ngày hết hạn là ngày mai hiện đúng ngày | P6, ngày mai (EC53, EC82) | R02, R08 | `FR17TC128` | Phần trăm (%) | `15` | `300000` | Ngày chạy cộng 1 | `3` | OUT1; cột "Hết hạn" hiện đúng ngày dạng `yyyy-mm-dd`. Giới hạn GH6 | AI | AI | |
| TC-CPN-129 | Kiểm tra tạo mã có ngày hết hạn 12/31/9999 | P6, lớn nhất giao diện cho nhập (EC53) | R08 | `FR17TC129` | Phần trăm (%) | `15` | `300000` | `12/31/9999` | `3` | OUT1; hiện `9999-12-31` | AI | AI | |

---

## 7. TS-05: API (EP, BVA)

Kết quả KQ-H-API hoặc KQ-KH-API cộng phần ghi ở cột "Kết quả mong đợi". Cột "Request" ghi thao tác và phần khác body cơ sở. Test case dạng bảng có bảng chi tiết ở mục 7.1: Mỗi dòng là một request riêng chỉ thay đúng trường ghi ở cột "Thay đổi"; test case đạt khi mọi dòng đạt.

| TC | Tiêu đề | Lớp hoặc biên | Kỹ thuật | Yêu cầu | Request | Kết quả mong đợi | Nguồn gốc | Phát hiện | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|---|
| TC-CPN-60 | Kiểm tra API tạo mã thành công với dữ liệu hợp lệ cơ sở | EC85, EC90 và các lớp cơ sở | EP | R01, R11 | `POST /api/admin/coupons`, body cơ sở, `code` `"FR17TC60"` | OUT2; `FR17TC60` có trong `GET` và trên bảng của giao diện với đúng giá trị từng trường. Giới hạn GH11 | AI | AI | |
| TC-CPN-61 | Kiểm tra API trả danh sách mã đủ trường | EC80, EC85 | EP | R02, R11 | `GET /api/coupons`, token admin, ngay sau reset | OUT7: 2xx; có 4 mã mẫu, mỗi mã đủ 6 trường và `id` (A17). Thiếu `id` thì TC-CPN-62, TC-CPN-71, TC-CPN-78, TC-CPN-79, TC-CPN-81 ghi Blocked. Thiếu trường giá trị thì test case API hợp lệ kiểm trên bảng của giao diện (GH11) | AI có SV sửa | AI bổ sung khi review S3: Cách kiểm thay thế khi `GET` thiếu trường giá trị | Bản AI chỉ xử lý trường hợp thiếu `id` |
| TC-CPN-62 | Kiểm tra API xóa mã vừa tạo | EC71, EC85 | EP | R03, R11 | 1. Tạo `FR17TC62` bằng API. 2. Lấy `id` từ `GET`. 3. `DELETE /api/admin/coupons/<id>` | OUT9: 2xx; `FR17TC62` không còn trong `GET` | AI | AI | |
| TC-CPN-63 | Kiểm tra API nhận Mã là số JSON | EC23 | EP | R04 | `POST`, `"code": 2026` | 2xx; `GET` có mã `2026` (A14). Giới hạn GH11 | AI | AI | |
| TC-CPN-64 | Kiểm tra API nhận trường số gửi dạng chuỗi chứa số | EC42, EC51, EC68 | EP | R07, R09, R10 | `POST`, dạng bảng 3 dòng | Mỗi dòng: 2xx; `GET` có giá trị số đúng (A14). Giới hạn GH11 | AI | AI | |
| TC-CPN-65 | Kiểm tra API từ chối `type` không hợp lệ | EC26, EC27, EC28 | EP | R06 | `POST`, dạng bảng 3 dòng | Mỗi dòng: 4xx (ERR3 hoặc ERR4); mã không được tạo | AI | AI | |
| TC-CPN-66 | Kiểm tra API từ chối trường bắt buộc là `null` hoặc chuỗi rỗng | EC22, EC29, EC43, EC52, EC61, EC69 | EP | R04, R06 đến R10 | `POST`, dạng bảng 6 dòng | Mỗi dòng: 4xx, lỗi thiếu của đúng trường (A14); mã không được tạo | AI | AI | |
| TC-CPN-67 | Kiểm tra API từ chối trường số không phải số | EC41, EC50, EC67 | EP | R07, R09, R10 | `POST`, dạng bảng 3 dòng | Mỗi dòng: 4xx (ERR15); mã không được tạo | AI | AI | |
| TC-CPN-68 | Kiểm tra API từ chối ngày hết hạn sai định dạng | EC58, EC59, EC60 | EP | R08 | `POST`, dạng bảng 3 dòng | Mỗi dòng: 4xx (ERR15); mã không được tạo | AI | AI | |
| TC-CPN-69 | Kiểm tra API từ chối request không đọc được | EC91, EC92, EC93, EC94 | EP | R01 | `POST`, dạng bảng 4 dòng | Mỗi dòng: 4xx (ERR16; dòng B đến D chấp nhận cả lỗi thiếu mọi trường) (A23); không 5xx; mã không được tạo | AI | SV: Hỏi về body rỗng, JSON sai cú pháp, thiếu header (S1, câu 2), dẫn tới IN14 | |
| TC-CPN-70 | Kiểm tra API từ chối body rỗng `{}` | EC95 (ngoại lệ) | EP | R04, R06 đến R10 | `POST`, body `{}` | 4xx; số mã trong `GET` không đổi; ghi lại thông báo liệt kê đủ 6 trường hay chỉ một. **Ngoại lệ:** Vi phạm 6 lớp cùng lúc; mục đích duy nhất là kiểm từ chối an toàn | AI | SV: Hỏi về body rỗng (S1, câu 2) | |
| TC-CPN-71 | Kiểm tra API xóa với `id` không hợp lệ | EC73, EC74, EC75 | EP | R03 | `DELETE /api/admin/coupons/<id>`, dạng bảng 3 dòng | Mỗi dòng: 2xx hoặc 4xx đều đạt, không 5xx (A15); số mã không đổi (trừ mã dòng C tự xóa khi chuẩn bị) | AI | SV: Hỏi biến gián tiếp của thao tác Xóa (S1, câu 1), dẫn tới lớp EC75 (dòng C) | |
| TC-CPN-72 | Kiểm tra API từ chối tạo mã khi không có header Authorization | EC86 | EP | R11 | `POST`, không có header `Authorization`, `code` `"FR17TC72"` | ERR12: 4xx; `FR17TC72` không có trong `GET` (xem bằng token admin) | AI | AI | |
| TC-CPN-73 | Kiểm tra API từ chối tạo mã khi header Authorization thiếu `Bearer` | EC87 | EP | R11 | `POST`, `Authorization: <token admin>`, `code` `"FR17TC73"` | ERR12: 4xx; mã không được tạo | AI | SV: Hỏi về thiếu header (S1, câu 2), dẫn tới lớp header sai dạng | |
| TC-CPN-74 | Kiểm tra API từ chối tạo mã khi token không hợp lệ | EC88 | EP | R11 | `POST`, `Authorization: Bearer abc.def.ghi`, `code` `"FR17TC74"` | ERR12: 4xx; mã không được tạo | AI | AI | |
| TC-CPN-75 | Kiểm tra API từ chối tạo mã khi dùng token user thường | EC89 | EP | R11 | `POST`, token user thường, `code` `"FR17TC75"` | ERR13: 4xx; mã không được tạo | AI | AI | |
| TC-CPN-76 | Kiểm tra API từ chối xem danh sách khi không có header Authorization | EC86 | EP | R11 | `GET /api/coupons`, không có header | ERR12: 4xx; không trả danh sách | AI | AI | |
| TC-CPN-77 | Kiểm tra API từ chối xem danh sách khi dùng token user thường | EC89 | EP | R11 | `GET /api/coupons`, token user thường | ERR13: 4xx; không trả danh sách | AI | AI | |
| TC-CPN-78 | Kiểm tra API từ chối xóa mã khi không có header Authorization | EC86 | EP | R03, R11 | 1. Tạo `FR17TC78` bằng token admin, lấy `id`. 2. `DELETE` không có header | ERR12: 4xx; `FR17TC78` vẫn còn | AI | AI | |
| TC-CPN-79 | Kiểm tra API từ chối xóa mã khi dùng token user thường | EC89 | EP | R03, R11 | Như TC-CPN-78 với `FR17TC79`, bước 2 dùng token user thường | ERR13: 4xx; `FR17TC79` vẫn còn | AI | AI | |
| TC-CPN-80 | Kiểm tra đường `POST /api/coupons` của FR-12 không cho tạo mã khi không có header | EC86 | EP | R11 | `POST /api/coupons`, body cơ sở, `code` `"FR17TC80"`, không có header | Mã không được tạo; không 5xx; 404 cũng đạt (A22) | AI | AI | |
| TC-CPN-81 | Kiểm tra đường `DELETE /api/coupons/:id` của FR-12 không cho user thường xóa mã | EC89 | EP | R11 | 1. Tạo `FR17TC81` bằng token admin, lấy `id`. 2. `DELETE /api/coupons/<id>` bằng token user thường | `FR17TC81` vẫn còn; không 5xx; 404 cũng đạt | AI | AI | |
| TC-CPN-82 | Kiểm tra qua API các lớp số lẻ, số âm khi giao diện bị chặn (dự phòng) | EC34, EC37, EC46, EC47, EC63, EC64 | EP | R07, R09, R10 | `POST`, dạng bảng 6 dòng | Theo từng dòng; **chỉ chạy dòng nào** mà test case giao diện tương ứng bị trình duyệt chặn; dòng không chạy ghi "Không chạy" | AI có SV sửa | AI bổ sung khi review S3: Dòng F gửi `0`, chạy khi TC-CPN-44 bị chặn | Bản AI ghi dòng F gửi `-1` với điều kiện chạy trỏ sang S4, không khớp TC-CPN-44 |
| TC-CPN-118 | Kiểm tra API nhận số lần dùng tối đa viết là 1.0 | P4, LB dạng thập phân (EC62) | BVA | R10 | `POST`, `"max_uses_per_user": 1.0`, `code` `"FR17TC118"` | OUT2, lưu là 1 (A27). Giới hạn GH12 | AI có SV sửa | SV: Chốt A27 (S4, quyết định 1) | Không bỏ sót: Quyết định của SV |
| TC-CPN-130 | Kiểm tra qua API các điểm biên số lẻ, số âm khi giao diện bị chặn (dự phòng) | P1 đến P4 (EC33, EC34, EC36, EC37, EC46, EC63) | BVA | R07, R09, R10 | `POST`, dạng bảng 7 dòng | Theo từng dòng; **chỉ chạy dòng nào** mà test case giao diện tương ứng bị trình duyệt chặn | AI | AI | |
| TC-CPN-131 | Kiểm tra server lưu chính xác giá trị 2^53 + 1 | P2, P3, P4 lớn nhất (độ chính xác) (EC39, EC48, EC65) | BVA | R07, R09, R10 | `POST`, dạng bảng 3 dòng; luôn chạy cùng TC-CPN-111, TC-CPN-114, TC-CPN-119 | Theo từng dòng; đọc kết hợp với test case giao diện theo bảng ở mục 7.1. Giới hạn GH7 | AI có SV sửa | Claude phiên điều phối `305c705a`: Giá trị có thể bị làm tròn trước khi gửi | Bản AI chỉ chạy điểm này qua giao diện, nên không tách được phần server |
| TC-CPN-140 | Kiểm tra API tạo mã thành công khi Mã có chữ thường | EC07 | EP | R01, R05 | 1. `POST`, `"code": "fr17tc140"`. 2. `POST`, `"code": "FR17TC140"` | Bước 1: OUT2; `GET` có `fr17tc140` hoặc `FR17TC140` (A10). Bước 2 (K5): 4xx (ERR2), vì so trùng không phân biệt hoa thường (A04) | SV thêm | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ nên TC-CPN-06 không kiểm được EShop (S5) | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |
| TC-CPN-141 | Kiểm tra API từ chối Mã chỉ khác mã mẫu ở chữ hoa, chữ thường | EC18 | EP | R05 | `POST`, `"code": "save10"` | 4xx (ERR2); `GET` không có `save10`, `SAVE10` giữ nguyên giá trị. Cần dữ liệu mẫu nguyên vẹn | SV thêm | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ nên TC-CPN-34 không kiểm được EShop (S5) | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |
| TC-CPN-142 | Kiểm tra API tạo mã thành công khi Mã là 1 chữ thường | P5, LB chữ thường (EC07) | BVA | R01, R04 | `POST`, `"code": "m"` | OUT2; `GET` có `m` hoặc `M` (A10). Dùng `m` thay cho `j` để không trùng mã `J` mà TC-CPN-123 có thể đã tạo | SV thêm | SV: Ô Mã coupon tự chuyển chữ hoa khi gõ nên TC-CPN-123 không kiểm được EShop (S5). AI bổ sung ở S5: Đổi ký tự để tránh trùng dữ liệu | Thông tin này chỉ có từ lần nhập thử ở S0 và không được cung cấp cho AI khi thiết kế |

### 7.1 Chi tiết test case dạng bảng

**TC-CPN-64: Chuỗi chứa số (hợp lệ, A14)**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC42 | `FR17TC64A` | `"discount_value": "15"` | 2xx; `GET` có `discount_value` 15 |
| B | EC51 | `FR17TC64B` | `"min_order_amount": "300000"` | 2xx; `GET` có `min_order_amount` 300000 |
| C | EC68 | `FR17TC64C` | `"max_uses_per_user": "3"` | 2xx; `GET` có `max_uses_per_user` 3 |

**TC-CPN-65: `type` không hợp lệ**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC26 | `FR17TC65A` | Bỏ trường `type` | 4xx (ERR3) |
| B | EC27 | `FR17TC65B` | `"type": "free"` | 4xx (ERR4) |
| C | EC28 | `FR17TC65C` | `"type": "PERCENT"` | 4xx (ERR4, A11) |

**TC-CPN-66: `null` hoặc chuỗi rỗng (A14)**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC22 | (đối tượng) | `"code": null` | 4xx (ERR1); số mã không đổi |
| B | EC29 | `FR17TC66B` | `"type": ""` | 4xx (ERR3) |
| C | EC43 | `FR17TC66C` | `"discount_value": null` | 4xx (ERR5) |
| D | EC52 | `FR17TC66D` | `"min_order_amount": null` | 4xx (ERR8) |
| E | EC61 | `FR17TC66E` | `"expired_at": ""` | 4xx (ERR7) |
| F | EC69 | `FR17TC66F` | `"max_uses_per_user": null` | 4xx (ERR10) |

**TC-CPN-67: Không phải số**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC41 | `FR17TC67A` | `"discount_value": "abc"` | 4xx (ERR15) |
| B | EC50 | `FR17TC67B` | `"min_order_amount": "abc"` | 4xx (ERR15) |
| C | EC67 | `FR17TC67C` | `"max_uses_per_user": "abc"` | 4xx (ERR15) |

**TC-CPN-68: Định dạng ngày (A13)**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC58 | `FR17TC68A` | `"expired_at": "12/31/2027"` | 4xx (ERR15) |
| B | EC59 | `FR17TC68B` | `"expired_at": "2027-02-30"` | 4xx (ERR15) |
| C | EC60 | `FR17TC68C` | `"expired_at": "2027-12-31T10:00:00Z"` | 4xx (ERR15) |

**TC-CPN-69: Request không đọc được (A23)**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC91 | `FR17TC69A` | Body `{"code": "FR17TC69A",` (thiếu phần còn lại) | 4xx (ERR16); không 5xx |
| B | EC92 | `FR17TC69B` | Body cơ sở, bỏ header `Content-Type` | 4xx (ERR16 hoặc thiếu mọi trường); không 5xx |
| C | EC93 | `FR17TC69C` | Body cơ sở, `Content-Type: text/plain` | Như dòng B |
| D | EC94 | (không có) | Không có body | Như dòng B; số mã không đổi |

**TC-CPN-71: Xóa `id` không hợp lệ (A15)**

| Dòng | Lớp | Chuẩn bị | `id` gửi | Kết quả mong đợi |
|---|---|---|---|---|
| A | EC73 | Kiểm trước `999999` không có trong `GET` | `999999` | 2xx hoặc 4xx; không 5xx; số mã không đổi |
| B | EC74 | Không | `abc` | Như dòng A |
| C | EC75 | Tạo `FR17TC71C`, lấy `id`, xóa thành công | `id` vừa xóa | Như dòng A |

**TC-CPN-82: Dự phòng qua API cho lớp số lẻ, số âm (S3)**

| Dòng | Lớp | `code` | Thay đổi | Kết quả mong đợi | Chạy khi |
|---|---|---|---|---|---|
| A | EC34 | `FR17TC82A` | `"discount_value": 12.5` | 2xx; `GET` có `12.5` | TC-CPN-15 bị chặn |
| B | EC37 | `FR17TC82B` | `"type": "fixed"`, `"discount_value": 1000.5` | 2xx; `GET` có `1000.5` | TC-CPN-16 bị chặn |
| C | EC47 | `FR17TC82C` | `"min_order_amount": 1000.5` | 2xx; `GET` có `1000.5` | TC-CPN-20 bị chặn |
| D | EC64 | `FR17TC82D` | `"max_uses_per_user": 1.5` | 4xx (ERR20) | TC-CPN-45 bị chặn |
| E | EC46 | `FR17TC82E` | `"min_order_amount": -1` | 4xx (ERR9) | TC-CPN-41 bị chặn |
| F | EC63 | `FR17TC82F` | `"max_uses_per_user": 0` | 4xx (ERR11) | TC-CPN-44 bị chặn |

**TC-CPN-130: Dự phòng qua API cho điểm biên số lẻ, số âm (S4)**

| Dòng | Điểm | `code` | Thay đổi | Kết quả mong đợi | Chạy khi |
|---|---|---|---|---|---|
| A | P1 âm | `FR17TC130A` | `"discount_value": -1` | 4xx (ERR6) | TC-CPN-100 bị chặn |
| B | P1 LB bước 0.01 | `FR17TC130B` | `"discount_value": 0.01` | 2xx; `GET` có `0.01` | TC-CPN-101 bị chặn |
| C | P1 UB bước 0.01 | `FR17TC130C` | `"discount_value": 100.01` | 4xx (ERR17) | TC-CPN-105 bị chặn |
| D | P2 âm | `FR17TC130D` | `"type": "fixed"`, `"discount_value": -1` | 4xx (ERR6) | TC-CPN-107 bị chặn |
| E | P2 LB bước 0.01 | `FR17TC130E` | `"type": "fixed"`, `"discount_value": 0.01` | 2xx; `GET` có `0.01` | TC-CPN-108 bị chặn |
| F | P3 LB-1 bước 0.01 | `FR17TC130F` | `"min_order_amount": -0.01` | 4xx (ERR9) | TC-CPN-112 bị chặn |
| G | P4 âm | `FR17TC130G` | `"max_uses_per_user": -1` | 4xx (ERR11) | TC-CPN-115 bị chặn |

**TC-CPN-131: Độ chính xác của số lớn (luôn chạy)**

| Dòng | Điểm | `code` | Thay đổi | Kết quả mong đợi |
|---|---|---|---|---|
| A | P2 | `FR17TC131A` | `"type": "fixed"`, `"discount_value": 9007199254740993` | Đạt nếu 2xx và `GET` có đúng `9007199254740993`, hoặc 4xx có thông báo rõ (ERR22). Sai nếu `GET` có `9007199254740992`, hoặc 5xx |
| B | P3 | `FR17TC131B` | `"min_order_amount": 9007199254740993` | Như dòng A |
| C | P4 | `FR17TC131C` | `"max_uses_per_user": 9007199254740993` | Như dòng A |

Cách đọc TC-CPN-131 cùng test case giao diện (TC-CPN-111, TC-CPN-114, TC-CPN-119):

| Giao diện | API | Ý nghĩa |
|---|---|---|
| Đúng | Đúng | Đạt |
| Sai | Đúng | Làm tròn trước khi gửi (trình duyệt hoặc mã của trang Web Admin); mã của trang là một phần của hệ thống nên vẫn là lỗi của FR-17 từ phía admin |
| Sai | Sai | Server làm tròn |
| Đúng | Sai | Bất thường; ghi lại và kiểm lại cách gửi request |

---

## 8. TS-06: Checklist giao diện

| TC | Tiêu đề | Yêu cầu | Điểm kiểm tra | Kết quả mong đợi | Cách kiểm tra | Nguồn gốc | Phát hiện | Vì sao AI bỏ sót |
|---|---|---|---|---|---|---|---|---|
| TC-CPN-90 | Kiểm tra dấu `*` cạnh trường bắt buộc của form tạo mã | R12 | 6 ô của form | Có ký hiệu `*` cạnh nhãn (FR-22) | Quan sát | AI | AI | |
| TC-CPN-91 | Kiểm tra ngôn ngữ của trang Quản lý Mã Giảm Giá | R14 | Mọi chữ trên trang, form, bảng, thông báo | Tiếng Việt, trừ thuật ngữ kỹ thuật chuẩn (FR-21). Ghi riêng chữ thuộc lịch chọn ngày của trình duyệt | Quan sát | AI | AI | |
| TC-CPN-92 | Kiểm tra màu nút "Tạo mã" và "Xóa" | R14 | Màu nền nút | "Tạo mã" xanh dương; "Xóa" đỏ (FR-21) | Quan sát | AI | AI | |
| TC-CPN-93 | Kiểm tra định dạng tiền trong bảng | R14 | Cột "Giá trị" (loại cố định), "Đơn tối thiểu" | Có `₫` và phân cách hàng nghìn (FR-21) | Quan sát bảng sau TC-CPN-50 | AI | AI | |
| TC-CPN-94 | Kiểm tra menu "Mã Giảm Giá" được highlight | R17 | Menu bên trái | Mục "Mã Giảm Giá" được highlight khi đang ở trang này (FR-23) | Quan sát, so với khi ở trang khác | AI | AI | |
| TC-CPN-95 | Kiểm tra trang có đúng 1 thẻ `<h1>` | R19 | Số thẻ `<h1>` và nội dung | Đúng 1 thẻ, mô tả nội dung trang (FR-21) | DevTools ở S6 | AI | AI | |

Quan sát ở S6, không có Đạt hay Sai: Placeholder ô "Giá trị" có đổi khi chọn "Số tiền cố định (₫)" không (S3, quyết định 2).

---

## 9. Nguồn gốc chi tiết

### 9.1 Test case không phải "AI"

| # | TC | Nguồn gốc | Mã trong bản AI | Đã đổi gì so với bản AI | Người phát hiện | Căn cứ |
|---|---|---|---|---|---|---|
| 1 | TC-CPN-06 | AI có SV sửa | TC-CPN-06 (S3) | Thêm giới hạn GH9: Chỉ kiểm hành vi giao diện; lớp EC07 kiểm thật ở TC-CPN-140 | Sinh viên (S5: Ô tự chuyển chữ hoa, quan sát lúc nhập thử ở S0) | Mục 13 |
| 2 | TC-CPN-10 | AI có SV sửa | TC-CPN-10 (S3) | Kết quả mong đợi chấp nhận thêm dạng chữ hoa `<B>FR17TC10</B>`; thêm GH9 | Sinh viên cung cấp thông tin (S5); AI ở phiên này nhận ra hệ quả với TC-CPN-10 | Mục 13 |
| 3 | TC-CPN-15 | AI có SV sửa | TC-CPN-15 (S3) | Trỏ đúng dòng A của TC-CPN-82 | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 4 | TC-CPN-16 | AI có SV sửa | TC-CPN-16 (S3) | Trỏ đúng dòng B của TC-CPN-82 | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 5 | TC-CPN-20 | AI có SV sửa | TC-CPN-20 (S3) | Trỏ đúng dòng C của TC-CPN-82 | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 6 | TC-CPN-34 | AI có SV sửa | TC-CPN-34 (S3) | Thêm GH9: Lớp EC18 kiểm thật ở TC-CPN-141 | Sinh viên (S5) | Mục 13 |
| 7 | TC-CPN-41 | AI có SV sửa | TC-CPN-41 (S3) | Trỏ đúng dòng E của TC-CPN-82 | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 8 | TC-CPN-44 | AI có SV sửa | TC-CPN-44 (S3) | Thêm dự phòng dòng F của TC-CPN-82 | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 9 | TC-CPN-45 | AI có SV sửa | TC-CPN-45 (S3) | Trỏ đúng dòng D của TC-CPN-82 | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 10 | TC-CPN-56 | AI có SV sửa | TC-CPN-56 (S3) | Thêm bước reset riêng trước khi chạy, chỉ phải xóa 4 mã mẫu | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 11 | TC-CPN-61 | AI có SV sửa | TC-CPN-61 (S3) | Thêm cách kiểm thay thế khi `GET` thiếu trường giá trị | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 12 | TC-CPN-82 | AI có SV sửa | TC-CPN-82 (S3) | Dòng F gửi `0` thay cho `-1`, điều kiện chạy là TC-CPN-44 bị chặn | AI ở phiên này, khi review S3 | `03_tc.md` mục 17 |
| 13 | TC-CPN-111 | AI có SV sửa | TC-CPN-111 (S4) | Ghi kết quả phản ánh chung giao diện và hệ thống; chạy cùng TC-CPN-131 dòng A | Claude ở phiên điều phối, session `305c705a` | `04_bva.md` mục 10, 13 |
| 14 | TC-CPN-114 | AI có SV sửa | TC-CPN-114 (S4) | Như TC-CPN-111, dòng B | Claude ở phiên điều phối, session `305c705a` | `04_bva.md` mục 10, 13 |
| 15 | TC-CPN-118 | AI có SV sửa | TC-CPN-118 (S4) | Kết quả mong đợi từ "theo A27" thành OUT2, lưu là 1 | Sinh viên chốt A27 (S4, quyết định 1) | `04_bva.md` mục 13 |
| 16 | TC-CPN-119 | AI có SV sửa | TC-CPN-119 (S4) | Như TC-CPN-111, dòng C | Claude ở phiên điều phối, session `305c705a` | `04_bva.md` mục 10, 13 |
| 17 | TC-CPN-123 | AI có SV sửa | TC-CPN-123 (S4) | Thêm GH9: Điểm này kiểm thật ở TC-CPN-142 | Sinh viên (S5) | Mục 13 |
| 18 | TC-CPN-131 | AI có SV sửa | Không có (thêm khi review S4) | Test case API luôn chạy cho ba điểm `2^53 + 1` | Claude ở phiên điều phối, session `305c705a`; AI ở phiên này đề xuất cụ thể | `04_bva.md` mục 10, 13 |
| 19 | TC-CPN-140 | SV thêm | Không có (thêm ở S5) | Bản API của EC07 | Sinh viên (S5) | Mục 13 |
| 20 | TC-CPN-141 | SV thêm | Không có (thêm ở S5) | Bản API của EC18 | Sinh viên (S5) | Mục 13 |
| 21 | TC-CPN-142 | SV thêm | Không có (thêm ở S5) | Bản API của điểm P5 "1 chữ thường"; dùng `m` để tránh trùng | Sinh viên (S5); AI ở phiên này chọn ký tự | Mục 13 |
### 9.2 Test case "AI" có lớp bắt nguồn từ câu hỏi của sinh viên ở S1

Các test case dưới đây giữ nguyên bản AI (nên nguồn gốc là "AI"), nhưng biến hoặc lớp mà chúng phủ được thêm khi review S1 theo câu hỏi của sinh viên, rồi bản AI của S2, S3 mới lập lớp và test case. Ghi lại để S8 thấy đầy đủ đóng góp ở bước xác định biến.

| Lớp | Bắt nguồn từ | Test case phủ |
|---|---|---|
| EC72, EC75, EC76 | Sinh viên hỏi "Thao tác Xóa không có biến Input gián tiếp nào sao?" (S1, câu 1), dẫn tới IN13 | TC-CPN-55, TC-CPN-71 (dòng C), TC-CPN-53 |
| EC87 | Sinh viên hỏi về thiếu header khi gọi API (S1, câu 2), dẫn tới lớp header sai dạng của IN11 | TC-CPN-73 |
| EC91 đến EC95 | Sinh viên hỏi về body rỗng, JSON sai cú pháp, thiếu `Content-Type` (S1, câu 2), dẫn tới IN14 | TC-CPN-69, TC-CPN-70 |
| (quy ước KQ-KH-API) | Sinh viên hỏi đặc tả có nêu mã HTTP không (S1, câu 3), dẫn tới giả định A20 | Mọi test case API không hợp lệ |

### 9.3 Test case đã bỏ (không có trong bộ cuối)

Không có. Bản review S3, S4 không bỏ test case nào. Lớp EC77 (mã đã dùng trong đơn hàng) đã bỏ ở S2 nên không có test case (A16); điểm placeholder ô "Giá trị" không lập test case (S3, quyết định 2).

---

## 10. Thứ tự chạy

1. Reset dữ liệu mẫu. Ghi ngày chạy, múi giờ, trình duyệt và phiên bản.
2. Cần dữ liệu mẫu nguyên vẹn: TC-CPN-50, TC-CPN-61; checklist TC-CPN-90 đến TC-CPN-95 (TC-CPN-93 dùng bảng sau TC-CPN-50).
3. Thêm qua giao diện: TC-CPN-01 đến TC-CPN-25, TC-CPN-30 đến TC-CPN-46, TC-CPN-100 đến TC-CPN-117, TC-CPN-119 đến TC-CPN-129 (TC-CPN-32, TC-CPN-34, TC-CPN-35, TC-CPN-36 cần mã mẫu còn nguyên; TC-CPN-127, TC-CPN-22, TC-CPN-128 tạo và xem trong cùng ngày).
4. Xóa không phá dữ liệu mẫu: TC-CPN-51, TC-CPN-52, TC-CPN-53.
5. API: TC-CPN-60 đến TC-CPN-81, TC-CPN-118, TC-CPN-131 (cùng đợt với TC-CPN-111, TC-CPN-114, TC-CPN-119), TC-CPN-140 đến TC-CPN-142 (TC-CPN-141 cần `SAVE10` còn nguyên). TC-CPN-82, TC-CPN-130 chỉ chạy các dòng cần thiết.
6. Phá dữ liệu mẫu: TC-CPN-54, TC-CPN-55 (sau TC-CPN-36, TC-CPN-50).
7. Reset dữ liệu, rồi chạy TC-CPN-56.
8. Reset dữ liệu ngay sau TC-CPN-56. Nếu kết quả bất thường ở bất kỳ bước nào làm hỏng dữ liệu mẫu, ghi lại rồi reset trước khi chạy tiếp.

---

## 11. Giới hạn quan sát

| Mã | Giới hạn | Test case |
|---|---|---|
| GH1 | Bảng chỉ thấy dạng hiển thị, có thể làm tròn số lẻ; giá trị lưu thật kiểm bằng K6 (`GET`) | TC-CPN-16, TC-CPN-18, TC-CPN-20, TC-CPN-21, TC-CPN-25, TC-CPN-101, TC-CPN-108 |
| GH2 | Ô số của trình duyệt có thể chặn hoặc sửa số lẻ, số âm trước khi gửi; khi đó kết quả phản ánh trình duyệt. Chạy dòng dự phòng của TC-CPN-82 hoặc TC-CPN-130 | TC-CPN-15, TC-CPN-16, TC-CPN-20, TC-CPN-41, TC-CPN-44, TC-CPN-45, TC-CPN-100, TC-CPN-101, TC-CPN-105, TC-CPN-107, TC-CPN-108, TC-CPN-112, TC-CPN-115 |
| GH3 | Thông báo lỗi có thể là bong bóng của trình duyệt, ngôn ngữ theo trình duyệt; vẫn xét vị trí (A21), ghi nguồn và ngôn ngữ | TC-CPN-30 đến TC-CPN-46, TC-CPN-100, TC-CPN-105, TC-CPN-106, TC-CPN-107, TC-CPN-112, TC-CPN-115, TC-CPN-120 |
| GH4 | R16 (Parameterized Query) chỉ quan sát gián tiếp | TC-CPN-11 |
| GH5 | Nhiều kết quả được chấp nhận (nhận đúng giá trị, hoặc từ chối có thông báo rõ); điều kiện "Sai" ghi trong test case | TC-CPN-12, TC-CPN-18, TC-CPN-21, TC-CPN-25, TC-CPN-111, TC-CPN-114, TC-CPN-119, TC-CPN-125 |
| GH6 | Kết quả phụ thuộc ngày chạy và múi giờ | TC-CPN-22, TC-CPN-23, TC-CPN-50, TC-CPN-126 đến TC-CPN-129 |
| GH7 | `2^53 + 1` qua giao diện có thể bị làm tròn ở trình duyệt, mã của trang hoặc server; kết quả giao diện không tách được nguồn. Đọc cùng TC-CPN-131 | TC-CPN-111, TC-CPN-114, TC-CPN-119, TC-CPN-131 |
| GH8 | `10^16` biểu diễn chính xác được bằng số thực 64 bit, nên chỉ kiểm độ lớn, không kiểm độ chính xác; độ chính xác do TC-CPN-111, TC-CPN-114, TC-CPN-119, TC-CPN-131 kiểm | TC-CPN-18, TC-CPN-21, TC-CPN-25 |
| GH9 | Ô Mã coupon tự chuyển chữ thường thành chữ hoa ngay khi gõ (sinh viên quan sát lúc nhập thử ở S0), nên test case nhập chữ thường qua giao diện chỉ kiểm hành vi giao diện; lớp chữ thường kiểm thật qua API (TC-CPN-140 đến TC-CPN-142). TC-CPN-10 vẫn kiểm được escape vì thẻ HTML không phân biệt hoa thường | TC-CPN-06, TC-CPN-10, TC-CPN-34, TC-CPN-123 |
| GH10 | Ô `code` có thể giới hạn số ký tự; nếu S6 thấy giới hạn N, bổ sung N-1, N, N+1 | TC-CPN-12, TC-CPN-125 |
| GH11 | Giá trị lưu qua API chỉ thấy được nếu `GET` trả đủ trường (A17); thiếu thì kiểm trên bảng của giao diện | TC-CPN-60, TC-CPN-61, TC-CPN-63, TC-CPN-64 |
| GH12 | Nhiều bộ đọc JSON coi `1.0` và `1` là cùng một số, nên test case có thể không phân biệt được | TC-CPN-118 |
| GH13 | Không kiểm được trong FR-17: Mã mới có `is_active = 1` không (FR-09 C1); xóa mã đã dùng trong đơn hàng (A16); escape ở màn hình của feature khác | Toàn bộ |

---

## 12. Ma trận truy vết yêu cầu

| Yêu cầu | Nội dung ngắn | Test case | Mức phủ |
|---|---|---|---|
| FR17-R01 | Thêm được mã khi mọi trường hợp lệ | TC-CPN-01 đến TC-CPN-25, TC-CPN-60, TC-CPN-69, TC-CPN-121 đến TC-CPN-125, TC-CPN-140, TC-CPN-142 | Đủ |
| FR17-R02 | Xem danh sách mã | TC-CPN-50, TC-CPN-61, TC-CPN-22, TC-CPN-23, TC-CPN-126 đến TC-CPN-128 | Đủ |
| FR17-R03 | Xóa mã | TC-CPN-13, TC-CPN-51 đến TC-CPN-55, TC-CPN-62, TC-CPN-71, TC-CPN-78, TC-CPN-79 | Một phần: Không kiểm xóa mã đã dùng trong đơn hàng (GH13) |
| FR17-R04 | `code` bắt buộc | TC-CPN-30, TC-CPN-31, TC-CPN-66, TC-CPN-120 đến TC-CPN-124, TC-CPN-142 | Đủ |
| FR17-R05 | `code` duy nhất | TC-CPN-03, TC-CPN-06, TC-CPN-13, TC-CPN-32 đến TC-CPN-36, TC-CPN-140, TC-CPN-141 | Đủ |
| FR17-R06 | `type` bắt buộc, chỉ `percent`/`fixed` | TC-CPN-01, TC-CPN-02, TC-CPN-65, TC-CPN-66 | Đủ |
| FR17-R07 | `discount_value` bắt buộc, dương | TC-CPN-14 đến TC-CPN-18, TC-CPN-37 đến TC-CPN-40, TC-CPN-64, TC-CPN-67, TC-CPN-100 đến TC-CPN-111, TC-CPN-130, TC-CPN-131 | Đủ |
| FR17-R08 | `expired_at` bắt buộc | TC-CPN-22 đến TC-CPN-24, TC-CPN-43, TC-CPN-68, TC-CPN-126 đến TC-CPN-129 | Đủ |
| FR17-R09 | `min_order_amount` bắt buộc, >= 0 | TC-CPN-19 đến TC-CPN-21, TC-CPN-41, TC-CPN-42, TC-CPN-112 đến TC-CPN-114, TC-CPN-130, TC-CPN-131 | Đủ |
| FR17-R10 | `max_uses_per_user` bắt buộc, >= 1 | TC-CPN-25, TC-CPN-44 đến TC-CPN-46, TC-CPN-115 đến TC-CPN-119, TC-CPN-130, TC-CPN-131 | Đủ |
| FR17-R11 | Chỉ admin có JWT hợp lệ | TC-CPN-72 đến TC-CPN-81 | Đủ trên thiết kế; Xem, Xóa chỉ kiểm 2 trong 4 lớp không hợp lệ (S3, cách A1) |
| FR17-R12 | Dấu `*` | TC-CPN-90 | Đủ |
| FR17-R13 | Thông báo lỗi trên nút submit | TC-CPN-30 đến TC-CPN-46 | Đủ |
| FR17-R14 | Tiếng Việt, màu nút, tiền `₫` | TC-CPN-01, TC-CPN-50, TC-CPN-91 đến TC-CPN-93, TC-CPN-30 đến TC-CPN-46 (ngôn ngữ thông báo) | Đủ |
| FR17-R15 | Escape khi hiển thị | TC-CPN-07, TC-CPN-09, TC-CPN-10 | Một phần: Chỉ trên bảng của FR-17 (GH13) |
| FR17-R16 | Parameterized Query | TC-CPN-11 | Một phần: Quan sát gián tiếp (GH4) |
| FR17-R17 | Highlight menu | TC-CPN-94 | Đủ |
| FR17-R18 | Trang trống | TC-CPN-56 | Đủ |
| FR17-R19 | Đúng 1 thẻ `<h1>` | TC-CPN-95 | Đủ trên thiết kế, kiểm bằng DevTools ở S6 |

R16 đến R19 là yêu cầu bổ sung ở S1 (`01_io.md` mục 7.1), không có trong `00_spec.md` mục 2.

---

## 13. Phần sinh viên bổ sung ở S5

Đã đưa vào bộ test case theo yêu cầu khi gộp:

| Nội dung | Test case | Căn cứ |
|---|---|---|
| Sinh viên cho biết ô Mã coupon trên giao diện tự chuyển chữ thường thành chữ hoa ngay khi gõ (quan sát lúc nhập thử ở S0). Test case nhập chữ thường qua giao diện chỉ kiểm hành vi giao diện, không kiểm EShop | Thêm TC-CPN-140 (EC07), TC-CPN-141 (EC18), TC-CPN-142 (P5, 1 chữ thường) qua API; thêm GH9 cho TC-CPN-06, TC-CPN-34, TC-CPN-123 | Kết quả mong đợi theo giả định đã chốt: A10 (lưu, hiển thị chữ hoa hay giữ nguyên đều đạt), A04 (so trùng không phân biệt hoa thường) |
| Hệ quả AI nhận ra từ thông tin trên: Chuỗi `<b>FR17TC10</b>` sẽ thành `<B>FR17TC10</B>` khi gõ | Sửa kết quả mong đợi của TC-CPN-10, thêm GH9 | Thẻ HTML không phân biệt hoa thường nên test case vẫn kiểm được escape (R15) |

Phần sinh viên review và bổ sung thêm (điền khi review):

| TC | Nội dung | Lớp hoặc biên | Ghi chú |
|---|---|---|---|
| | | | |
