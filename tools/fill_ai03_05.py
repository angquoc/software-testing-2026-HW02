"""Điền form [AI-03] Disclosure và [AI-05] Privacy Checklist cho HW02 từ mẫu gốc trong "../AI Templates".

Chạy:  python tools/fill_ai03_05.py
- [AI-03]: Bảng thông tin, 6 câu khai báo, khối chữ ký (ảnh chữ ký lấy từ form [AI-02] đã ký của HW01).
- [AI-05]: Khối chữ ký và checklist (đánh dấu giống HW01 theo quyết định của sinh viên).
Luôn dựng lại từ mẫu gốc nên chạy nhiều lần không bị trùng; chạy TRƯỚC khi ký và tick tay.
"""
import io
import os
import docx
from docx.oxml.ns import qn
from docx.shared import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
HW = os.path.dirname(HERE)
TPL = os.path.join(HW, "..", "AI Templates")
FORMS = os.path.join(HW, "forms")

SIGN = {
    "Họ tên sinh viên (in hoa)": "NGUYỄN THỊ ÁNH NGỌC",
    "MSSV": "23120061",
    "Lớp / Khoá": "Kiểm thử phần mềm - CQ2023/3",
    "Giảng viên": "Lâm Quang Vũ\nHồ Tuấn Thanh\nTrương Phước Lộc",
    "Ngày": "21/10/2026",
}
INFO = {
    "Mã bài tập": "HW02-AI",
    "Tên bài tập": "Domain Testing on EShop (Domain Testing và Boundary Value Analysis cho FR-01, FR-07, FR-17, FR-04)",
    "Cấp độ AI (1–5)": "Cấp 4 – AI hỗ trợ sản xuất",
    "Ngày": "21/10/2026",
    "Họ tên sinh viên": "Nguyễn Thị Ánh Ngọc",
    "MSSV": "23120061",
}

ANSWERS = {
    "1. Công cụ AI đã dùng:": [
        "Claude Code (Anthropic, claude-opus-5-5), chạy trong VS Code: 1 phiên điều phối (305c705a) và 4 phiên thiết kế "
        "(FR-01: 38378bef; FR-17: 1648c211; FR-07: 709e0d24; FR-04: 633ed316). Không dùng công cụ AI nào khác.",
    ],
    "2. Giai đoạn nào của bài tập có dùng AI:": [
        "Tick: [x] brainstorm  [x] outline  [x] viết nháp  [x] phản hồi  [x] sửa chữa  [x] code  [x] phân tích dữ liệu  [ ] thiết kế đồ hoạ  [x] khác (ghi rõ).",
        "Khác: Thiết kế test case Domain Testing và BVA theo từng bước của slide S04 (bản gốc của AI lưu trong ai_raw/ của từng feature); "
        "điền bảng kết quả S6 theo ảnh và log do sinh viên chạy; viết nháp bug report và trang link tạo issue; điều phối nhiều phiên và soát thao tác bị cấm. "
        "Code: Script chạy test API, script xuất prompt log, xuất PDF, điền form, Agent Skill domain-testing-design. "
        "Phân tích dữ liệu: Đếm bảng \"Thay đổi so với bản AI\" cho AI gap analysis (S8).",
    ],
    "3. Prompt / nhiệm vụ chính cho AI:": [
        "(1) C255 – Claude Code – 06:47 21/10/2026 (gọi Agent Skill cho FR-04, có quay video): \"/domain-testing-design Feature D, FR-04 Quản lý hồ sơ cá nhân trên Mobile (app EShop chạy bằng Expo Go trên Android, Samsung Galaxy S21 Ultra), thư mục Homeworks/HW02/features/D_FR-04_HoSo_Mobile/. Lưu ý: Bắt đầu từ S0. [...] Tuân thủ WORKFLOW.md: Hộp đen, không đọc mã nguồn EShop, không đọc file của feature khác trừ khi tôi cho phép.\"",
        "(2) C121 – Claude Code – 15:55 20/10/2026 (gọi Agent Skill cho FR-17): \"/domain-testing-design Feature C, FR-17 Quản lý mã giảm giá trên Web Admin (http://localhost:5174) [...] Ở S0 tôi có nhập thử vài trường hợp; kết quả được cất riêng, không cung cấp. Không hỏi về kết quả này, thiết kế như thể chưa biết.\"",
        "(3) C160 – Claude Code – 22:09 20/10/2026 (review S5 của FR-17): \"Bạn hãy kiểm tra lại các ý sau. Tôi đang thắc mắc, cảm thấy sai sai khi đọc bài của bạn chứ cũng chưa chắc đúng 100%, hãy kiểm chứng: Xem lại giúp tôi logic endpoint [...] Chưa có API kiểm tra cắt khoảng trắng đầu/cuối [...]\"",
        "Toàn bộ prompt có timestamp, nguyên văn: Phụ lục A (prompt_log.md).",
    ],
    "4. Phần cụ thể AI đóng góp:": [
        "Với cả 4 feature: AI viết bản gốc của S0 đến S5 (trích đặc tả, biến Input/Output, lớp tương đương, test case Domain Testing, BVA, bộ test cuối; lưu nguyên văn trong ai_raw/), "
        "script chạy test API, điền bảng kết quả S6 từ ảnh và log của sinh viên, nháp bug report, nháp AI gap analysis (S8). "
        "Khác: WORKFLOW.md, Agent Skill domain-testing-design, các script trong tools/, khung report.md và README, nháp AI Critique, Mandatory Disclosure, Phụ lục B. "
        "AI KHÔNG đóng góp vào: Ảnh khảo sát và ảnh chạy test (sinh viên chụp), việc chạy test và script, 48 issue trên GitHub (sinh viên tự tạo), các quyết định chọn phương án ở từng bước, "
        "phần Kết luận của Phụ lục B, điểm tự chấm. Chi tiết từng artifact: AI Audit Report (Phụ lục B của report.md, B01 đến B19).",
    ],
    "5. Cách tôi rà soát / chỉnh sửa / xác minh đầu ra AI:": [
        "Mỗi bước review bản AI và ghi mọi chỗ sửa vào bảng \"Thay đổi so với bản AI\" (Loại: Sai, Thiếu, Thừa, Mơ hồ, Quyết định của SV; kèm người phát hiện); "
        "đối chiếu với đặc tả EShop (README, API spec) và slide S04; chạy script check_step.py để kiểm mọi lớp có test case phủ và định dạng; "
        "chạy test thật trên Web, Web Admin và điện thoại để kiểm kết quả mong đợi; một phiên Claude riêng làm điều phối, đọc transcript để soát thao tác bị cấm "
        "(đọc mã nguồn, đọc ghi chú điều phối) và đếm lại số liệu S8; giữ toàn bộ prompt trong prompt log. Kết quả rà soát: Phụ lục B (VALID, INCOMPLETE, INVALID).",
    ],
    "6. Trích dẫn (nếu môn yêu cầu):": [
        "[1] Anthropic, \"Claude Code (claude-opus-5-5),\" [Large language model], 2026. [Online]. Available: https://claude.ai",
    ],
}


def set_cell(cell, text):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    p.add_run(text)


def signature():
    """Ảnh chữ ký của sinh viên, lấy từ form [AI-02] đã ký của HW01 (sinh viên đồng ý dùng lại)."""
    src = docx.Document(os.path.join(HW, "..", "HW01", "forms", "[AI-02] - FIT@HCMUS - AI Audit Report_Vn.docx"))
    for t in src.tables:
        for r in t.rows:
            if r.cells[0].text.strip().startswith("Chữ ký"):
                blip = r.cells[1]._element.findall(".//" + qn("a:blip"))[0]
                ext = r.cells[1]._element.findall(".//" + qn("wp:extent"))[0]
                return src.part.related_parts[blip.get(qn("r:embed"))].blob, int(ext.get("cx"))
    raise SystemExit("Không tìm thấy ảnh chữ ký trong form HW01")


def fill_sign(table):
    blob, width = signature()
    for r in table.rows:
        key = r.cells[0].text.strip().rstrip(":")
        if key in SIGN:
            set_cell(r.cells[1], SIGN[key])
        elif key == "Chữ ký":
            set_cell(r.cells[1], "")
            r.cells[1].paragraphs[0].add_run().add_picture(io.BytesIO(blob), width=Emu(width))


def ai03():
    d = docx.Document(os.path.join(TPL, "[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.docx"))
    info, sign = d.tables[:2]
    for r in info.rows:
        key = r.cells[0].text.strip().rstrip(":")
        if key in INFO:
            set_cell(r.cells[1], INFO[key])
    fill_sign(sign)
    paras = d.paragraphs
    for i, p in enumerate(paras):
        q = p.text.strip()
        if q in ANSWERS:
            # Bỏ qua dòng hướng dẫn ngay sau câu hỏi; các dòng gạch dưới phía sau dùng để ghi câu trả lời
            blanks = []
            for p2 in paras[i + 1:]:
                t = p2.text.strip()
                if t in ANSWERS or t.startswith("3. Cam đoan"):
                    break
                if t and set(t) == {"_"}:
                    blanks.append(p2)
            if q.startswith("2."):
                # Câu 2: Thay luôn dòng "Tick tất cả" bằng dòng đã tick
                tick = next(p2 for p2 in paras[i + 1:i + 3] if p2.text.strip().startswith("Tick tất cả"))
                for r in list(tick.runs):
                    r._element.getparent().remove(r._element)
                tick.add_run(ANSWERS[q][0])
                lines = ANSWERS[q][1:]
            else:
                lines = ANSWERS[q]
            for j, p2 in enumerate(blanks):
                for r in list(p2.runs):
                    r._element.getparent().remove(r._element)
                if j < len(lines):
                    p2.add_run(lines[j])
                else:
                    p2._element.getparent().remove(p2._element)
    out = os.path.join(FORMS, "[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.docx")
    d.save(out)
    print("Đã ghi", os.path.basename(out))


def ai05():
    d = docx.Document(os.path.join(TPL, "[AI-05] - FIT@HCMUS - AI Privacy Checklist_Vn.docx"))
    fill_sign(d.tables[0])
    # Checklist: Sinh viên chọn đánh dấu giống HW01 (21/10/2026): Tick mọi ô, trừ 2 ô dưới đây
    # (đã đưa tên, MSSV và đặc tả EShop cho AI, nên để trống là trung thực)
    keep_empty = ("Không nhập dữ liệu cá nhân", "Không paste nguyên si tài liệu có bản quyền")
    for p in d.paragraphs:
        t = p.text.strip()
        if t.startswith("[ ]") and not any(k in t for k in keep_empty):
            run = next(r for r in p.runs if "[ ]" in r.text)
            run.text = run.text.replace("[ ]", "[x]", 1)
    out = os.path.join(FORMS, "[AI-05] - FIT@HCMUS - AI Privacy Checklist_Vn.docx")
    d.save(out)
    print("Đã ghi", os.path.basename(out))


if __name__ == "__main__":
    os.makedirs(FORMS, exist_ok=True)
    ai03()
    ai05()
