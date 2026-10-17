"""Tạo file Excel để nhóm chọn feature HW02: group/HW02_Chon_feature_Nhom.xlsx

Mức độ Nặng/Vừa/Nhẹ chỉ dựa trên SRS (README của eshop-sut): số biến input và số biên có thể làm BVA.
Chạy:  python tools/make_feature_sheet.py [đường dẫn output]
"""
import os
import sys
from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "group", "HW02_Chon_feature_Nhom.xlsx")
MEMBERS = 3

# (Pool, FR, Tên, Biến input chính, Biên / ràng buộc cho BVA, Mức độ, Lý do, Có trên Mobile?)
FEATURES = [
    ("A", "FR-01", "Đăng ký tài khoản",
     "Họ tên, Email, Mật khẩu, Xác nhận mật khẩu",
     "Mật khẩu ≥ 8 ký tự (7/8/9); đủ 4 loại ký tự; ký tự đặc biệt chỉ trong tập @$!%*?&; email đúng định dạng, không trùng; xác nhận phải khớp",
     "Nặng", "Nhiều biến, mỗi biến nhiều điều kiện; biên độ dài rõ ràng", "Có (FR-20)"),
    ("A", "FR-02", "Đăng nhập & khóa tài khoản",
     "Email, Mật khẩu, số lần sai liên tiếp, thời gian chờ",
     "Khóa khi sai ≥ 3 lần (2/3/4); khóa 30 giây (29/30/31 s); bộ đếm tăng đúng 1",
     "Vừa", "Ít biến nhưng có biên số lần và biên thời gian (khó canh giờ khi test)", "Có (FR-20)"),
    ("A", "FR-03", "Quên & đặt lại mật khẩu (2 bước)",
     "Email, OTP, Mật khẩu mới, Xác nhận mật khẩu mới",
     "OTP đúng 6 chữ số (5/6/7); mật khẩu mới theo luật FR-01; OTP chỉ dùng cho email đã yêu cầu; OTP có hạn, dùng 1 lần (SEC-07)",
     "Nặng", "2 bước, kế thừa toàn bộ luật mật khẩu FR-01 cộng thêm OTP", "Cần xác nhận khi chạy app"),
    ("A", "FR-04", "Quản lý hồ sơ cá nhân",
     "Họ tên, Số điện thoại, Địa chỉ giao hàng",
     "SĐT bắt đầu bằng 0, 10–11 chữ số (9/10/11/12); không đổi được email, role",
     "Vừa", "Biên chính nằm ở số điện thoại; các trường còn lại ít ràng buộc", "Có (FR-20)"),
    ("A", "FR-05", "Danh sách & tìm kiếm sản phẩm",
     "Từ khóa tìm kiếm",
     "Từ khóa rỗng, có/không có kết quả, ký tự đặc biệt/HTML; SRS không nêu độ dài tối đa",
     "Nhẹ", "1 biến, không có biên số rõ ràng", "Có (FR-20)"),
    ("A", "FR-06", "Chi tiết sản phẩm",
     "Số lượng",
     "Số nguyên dương, tối thiểu 1 (0/1/2); số âm, số thập phân, chữ; SRS không nêu tối đa",
     "Nhẹ", "1 biến, chỉ có biên dưới", "Có (FR-20)"),
    ("B", "FR-07", "Giỏ hàng",
     "Số lượng (nút +/−), sản phẩm thêm vào",
     "Thêm trùng sản phẩm → tăng số lượng; giảm số lượng về biên dưới; tính Thành tiền / Tổng cộng",
     "Vừa", "Có biên số lượng và output là tiền cần tính đúng", "Có (FR-20)"),
    ("B", "FR-08", "Thanh toán",
     "Trạng thái đăng nhập, giỏ hàng, total_amount (backend tự tính)",
     "Đã/chưa đăng nhập; giỏ rỗng/có hàng; client gửi total sai",
     "Vừa", "Ít biến nhập tay; phân vùng chủ yếu theo trạng thái", "Có (FR-20)"),
    ("B", "FR-09", "Mã giảm giá (Coupon)",
     "Mã, tổng đơn, ngày hiện tại, trạng thái đăng nhập, số lần đã dùng, loại percent/fixed",
     "Tổng đơn ≥ min_order (biên 299.999/300.000/300.001); ngày so với expired_at; số lần dùng < max_uses; 5 điều kiện C1–C5 cùng lúc",
     "Nặng", "Nhiều điều kiện kết hợp, biên số tiền rõ, có công thức tính", "Cần xác nhận khi chạy app"),
    ("B", "FR-10", "Trạng thái đơn hàng (State machine)",
     "Trạng thái hiện tại, hành động, vai trò (User/Admin)",
     "5 trạng thái; trạng thái kết thúc; User không hủy được khi shipping",
     "Vừa", "Hợp với kỹ thuật State Transition hơn; domain chỉ chia theo tập trạng thái", "Có — chỉ phần hủy đơn (FR-20)"),
    ("B", "FR-11", "Lịch sử đơn hàng (User)",
     "Người dùng đang đăng nhập",
     "Chỉ thấy đơn của mình; hiển thị và dịch trạng thái",
     "Nhẹ", "Chủ yếu kiểm tra hiển thị, gần như không có biên", "Có (FR-20)"),
    ("C", "FR-12", "Kiểm soát truy cập",
     "Token (có/không/sai), role trong token",
     "Không token / token sai / token user / token admin cho từng nhóm API",
     "Vừa", "Phân vùng rõ nhưng không có biên số", "Không"),
    ("C", "FR-13", "Dashboard",
     "Trạng thái các đơn hàng",
     "Doanh thu chỉ tính đơn delivered; tổng số đơn",
     "Nhẹ", "Output tính từ dữ liệu, không có input nhập tay", "Không"),
    ("C", "FR-14", "Quản lý danh mục (CRUD)",
     "Tên danh mục",
     "Bắt buộc, không rỗng (rỗng, chỉ khoảng trắng); SRS không nêu độ dài tối đa",
     "Nhẹ", "1 biến, 1 ràng buộc", "Không"),
    ("C", "FR-15", "Quản lý sản phẩm (CRUD)",
     "Tên, Giá, Danh mục",
     "Tên bắt buộc, ≤ 255 ký tự (254/255/256); giá > 0 (−1/0/0,01/1); danh mục phải có trong danh sách; sửa 1 SP không ảnh hưởng SP khác",
     "Nặng", "3 biến, biên độ dài và biên giá rõ ràng", "Không"),
    ("C", "FR-16", "Import sản phẩm từ CSV",
     "File (đuôi, header, nội dung từng dòng)",
     "Đuôi .csv; header đúng; trường có dấu phẩy bọc nháy kép (RFC 4180); name không rỗng, price > 0; lỗi 1 dòng → rollback toàn bộ",
     "Nặng", "Phải tự tạo nhiều file test; nhiều phân vùng theo cấu trúc file", "Không"),
    ("C", "FR-17", "Quản lý mã giảm giá (CRUD)",
     "code, type, discount_value, expired_at, min_order_amount, max_uses_per_user",
     "code duy nhất; type ∈ {percent, fixed}; discount_value > 0; min_order ≥ 0; max_uses ≥ 1; ngày hết hạn",
     "Nặng", "6 biến, nhiều biên số (0/1, −1/0)", "Không"),
    ("C", "FR-18", "Quản lý đơn hàng (Admin)",
     "Trạng thái đơn, hành động của Admin",
     "Chuyển trạng thái theo FR-10; địa chỉ hiển thị an toàn",
     "Vừa", "Giống FR-10 (thiên về State Transition)", "Không"),
    ("C", "FR-19", "Quản lý người dùng (Admin)",
     "Người dùng cần xóa",
     "Không được xóa chính mình; không lộ mật khẩu",
     "Nhẹ", "Ít phân vùng", "Không"),
]

HEAD_FILL = PatternFill("solid", fgColor="1F4E78")
HEAD_FONT = Font(bold=True, color="FFFFFF")
GREY = PatternFill("solid", fgColor="D9D9D9")
LEVEL_FILL = {"Nặng": "F8CBAD", "Vừa": "FFE699", "Nhẹ": "C6EFCE"}
THIN = Side(style="thin", color="999999")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def header(ws, cols, widths):
    ws.append(cols)
    for i, w in enumerate(widths, 1):
        c = ws.cell(row=1, column=i)
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[c.column_letter].width = w
    ws.freeze_panes = "A2"


wb = Workbook()

# --- Hướng dẫn
ws = wb.active
ws.title = "Hướng dẫn"
ws.column_dimensions["A"].width = 110
for line in [
    "HW02 – Domain Testing on EShop: chọn feature cho nhóm",
    "",
    "1. Điền họ tên 3 thành viên ở sheet 'Thành viên' trước.",
    "2. Ở sheet 'Chọn feature', mỗi người chọn đúng 4 feature: 1 ở Pool A, 1 ở Pool B, 1 ở Pool C (Web)"
    " và 1 ở Pool D (Mobile), bằng cách chọn tên mình ở cột 'Người chọn'.",
    "3. Mỗi ô chỉ chọn được 1 tên → một dòng feature không thể có 2 người.",
    "4. Pool D (Mobile): là các FR của Pool A/B được làm trên app mobile (SRS FR-20). Pool C (Web Admin) không có trên mobile.",
    "5. QUY TẮC CHẶT (giảng viên chưa trả lời nên nhóm chọn cách hiểu an toàn nhất): mỗi FR chỉ được làm"
    " MỘT LẦN trong cả nhóm, tính chung cả Web và Mobile. FR nào đã có người làm trên Web thì không ai làm trên Mobile"
    " nữa, và ngược lại. Cột 'Cảnh báo' báo đỏ khi vi phạm.",
    "6. Cách này luôn khả thi: Pool A + B có 11 FR, nhóm cần 3 (A) + 3 (B) + 3 (Mobile) = 9 FR, còn dư 2.",
    "7. Để chọn nhanh, xem sheet 'Gói gợi ý': 3 gói đã chia sẵn, cân bằng độ nặng và không trùng FR. Mỗi người nhận 1 gói"
    " (có thể đổi feature giữa các gói, miễn không trùng).",
    "8. Sheet 'Kiểm tra' tự đếm số feature của từng người theo Pool và báo khi chưa đúng.",
    "",
    "Mức độ (Nặng / Vừa / Nhẹ): đánh giá theo SRS (README của eshop-sut), dựa trên số biến input"
    " và số biên có thể áp dụng BVA. Chỉ mang tính tham khảo.",
    "Policy môn học: chọn task quá đơn giản sẽ giới hạn điểm tối đa có thể đạt.",
    "Ghi chú ở các dòng Pool D: 'Có (FR-20)' = SRS FR-20 có liệt kê; 'Cần xác nhận khi chạy app' = SRS không ghi rõ, cần mở app kiểm tra.",
]:
    ws.append([line])
ws["A1"].font = Font(bold=True, size=14)
for row in ws.iter_rows(min_row=2):
    row[0].alignment = Alignment(wrap_text=True, vertical="top")

# --- Thành viên
wm = wb.create_sheet("Thành viên")
header(wm, ["STT", "Họ tên", "MSSV"], [6, 30, 14])
for i in range(1, MEMBERS + 1):
    wm.append([i, None, None])
    for c in wm[i + 1]:
        c.border = BORDER
NAMES = f"'Thành viên'!$B$2:$B${MEMBERS + 1}"

# --- Chọn feature
wf = wb.create_sheet("Chọn feature")
header(wf, ["Pool", "Mã FR", "Nền tảng", "Tên feature", "Biến input chính (theo SRS)", "Biên / ràng buộc có thể làm BVA",
            "Mức độ", "Lý do", "Người chọn", "Cảnh báo", "Ghi chú"],
       [6, 8, 10, 26, 34, 52, 9, 34, 18, 34, 24])
# Pool A, B, C trên Web; Pool D = các FR có trên app mobile
ROWS = [(f[0], f[1], "Web", f[2], f[3], f[4], f[5], f[6], None) for f in FEATURES]
ROWS += [("D", f[1], "Mobile", f[2], f[3], f[4], f[5], f[6], f[7]) for f in FEATURES if f[7] != "Không"]
last = len(ROWS) + 1
fr_rng, pick_rng = f"$B$2:$B${last}", f"$I$2:$I${last}"
dv = DataValidation(type="list", formula1=NAMES, allow_blank=True)
wf.add_data_validation(dv)
dv.add(f"I2:I{last}")
D_FILL = PatternFill("solid", fgColor="DDEBF7")
for r, row in enumerate(ROWS, 2):
    wf.append(list(row[:8]) + [None, None, row[8]])
    # Quy tắc chặt: mỗi FR chỉ được 1 người chọn, tính chung Web và Mobile
    wf.cell(row=r, column=10).value = (
        f'=IF(AND(I{r}<>"",COUNTIFS({fr_rng},B{r},{pick_rng},"<>")>1),'
        f'"VI PHẠM: "&B{r}&" đã được chọn ở cả Web và Mobile","")'
    )
    for c in wf[r]:
        c.alignment, c.border = WRAP, BORDER
        if row[0] == "D":
            c.fill = D_FILL
    wf.cell(row=r, column=7).fill = PatternFill("solid", fgColor=LEVEL_FILL[row[6]])
wf.auto_filter.ref = f"A1:K{last}"
wf.conditional_formatting.add(
    f"J2:J{last}", FormulaRule(formula=[f'J2<>""'], font=Font(color="C00000", bold=True)))

# --- Gói gợi ý: mỗi FR của Pool A/B chỉ xuất hiện 1 lần trong cả 3 gói; điểm nặng: Nặng 3, Vừa 2, Nhẹ 1
LEVEL = {f[1]: f[5] for f in FEATURES}
NAME = {f[1]: f[2] for f in FEATURES}
BUNDLES = [
    ("Gói 1", "FR-01", "FR-07", "FR-17", "FR-04"),
    ("Gói 2", "FR-03", "FR-08", "FR-15", "FR-10"),
    ("Gói 3", "FR-02", "FR-09", "FR-16", "FR-06"),
]
SCORE = {"Nặng": 3, "Vừa": 2, "Nhẹ": 1}
wg = wb.create_sheet("Gói gợi ý")
header(wg, ["Gói", "Pool A (Web)", "Pool B (Web)", "Pool C (Web)", "Pool D (Mobile)", "Tổng độ nặng", "Người nhận"],
       [8, 30, 30, 30, 34, 13, 18])
for b in BUNDLES:
    cells = [f"{fr} {NAME[fr]} ({LEVEL[fr]})" for fr in b[1:]]
    wg.append([b[0]] + cells + [sum(SCORE[LEVEL[fr]] for fr in b[1:]), None])
    for c in wg[wg.max_row]:
        c.alignment, c.border = WRAP, BORDER
dvg = DataValidation(type="list", formula1=NAMES, allow_blank=True)
wg.add_data_validation(dvg)
dvg.add(f"G2:G{len(BUNDLES) + 1}")
used = [fr for b in BUNDLES for fr in b[1:]]
assert len(used) == len(set(used)), "Có FR bị trùng giữa các gói"
for note in [
    "",
    "Độ nặng: Nặng = 3, Vừa = 2, Nhẹ = 1. Các FR trong 3 gói không trùng nhau, tính chung cả Web và Mobile.",
    "Không dùng: FR-05, FR-11 (nhẹ nhất) và FR-12, FR-13, FR-14, FR-18, FR-19 của Pool C.",
    "Pool D chỉ 15 điểm (A, B, C mỗi pool 25 điểm) nên FR nặng được ưu tiên đặt ở Web.",
    "FR-06 trên Mobile: cần mở app xác nhận màn chi tiết sản phẩm có ô nhập số lượng. Nếu không có, đổi sang FR-05 (tìm kiếm).",
]:
    wg.append([note])

# --- Kiểm tra
wk = wb.create_sheet("Kiểm tra")
header(wk, ["Thành viên", "Pool A (Web)", "Pool B (Web)", "Pool C (Web)", "Pool D (Mobile)", "Trạng thái"],
       [30, 13, 13, 13, 15, 34])
rng = f"'Chọn feature'!$A$2:$A${last}"
pick = f"'Chọn feature'!$I$2:$I${last}"
for i in range(2, MEMBERS + 2):
    wk.append([
        f"=IF('Thành viên'!B{i}=\"\",\"\",'Thành viên'!B{i})",
        *[f'=IF(A{i}="","",COUNTIFS({rng},"{p}",{pick},A{i}))' for p in "ABCD"],
        f'=IF(A{i}="","",IF(AND(B{i}=1,C{i}=1,D{i}=1,E{i}=1),"Đủ 4 feature",'
        f'"Chưa đúng: mỗi Pool phải đúng 1"))',
    ])
    for c in wk[i]:
        c.border = BORDER
        c.alignment = Alignment(horizontal="center")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
wb.save(OUT)
print("Đã tạo", os.path.normpath(OUT))
