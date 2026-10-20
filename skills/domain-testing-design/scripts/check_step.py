#!/usr/bin/env python3
"""Kiểm tra máy móc cho các file của skill domain-testing-design.

Script không đánh giá nội dung (kết quả mong đợi đúng hay sai). Nó chỉ bắt các lỗi
đếm, đánh mã, tham chiếu và định dạng mà AI hay mắc khi làm tay.

Lệnh:
  format   FILE...                      Dấu "—", "·" ngoài phần trích nguyên văn (dòng bắt đầu bằng ">");
                                        bỏ qua chỗ chỉ nhắc tới ký tự trong dấu nháy
  changes  FILE...                      Cột Loại của bảng "Thay đổi so với bản AI" chỉ nhận 5 giá trị
  classes  EC_FILE                      Mã lớp trùng; đếm lớp theo Loại (H, KH, GĐ, Output)
  coverage EC_FILE TC_FILE...           Lớp chưa có test case; mã test case trùng; mã được nhắc mà không tồn tại
  all --ec EC_FILE --tc TC_FILE... --files FILE...

Quy ước mà script dựa vào (theo assets/templates và references/step-s*.md):
  - Lớp được định nghĩa ở dòng bảng có ô đầu là "ECnn".
  - Test case được định nghĩa ở dòng bảng có ô đầu là "TC-<MÔĐUN>-NN", hoặc ở cột "Test case"
    của bảng giá trị biên (bảng có ô tiêu đề đầu là "Điểm"), trừ ô có chữ "đã có".
  - Khoảng mã viết dạng "EC13 đến EC18", "TC-REG-01 đến TC-REG-18".
  - Bỏ qua mục "Thay đổi so với bản AI" và "Bảng đổi mã" khi tìm định nghĩa và tham chiếu.

Mã thoát: 1 nếu có ERROR, 0 nếu không.
"""
import argparse
import io
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LOAI = ["Sai", "Thiếu", "Thừa", "Mơ hồ", "Quyết định của SV"]
SKIP_SECTIONS = ("Thay đổi so với bản AI", "Bảng đổi mã")
EC_ID = re.compile(r"^EC\d+$")
TC_ID = re.compile(r"^TC-[A-Z0-9]+-\d+$")
EC_ANY = re.compile(r"\bEC\d+\b")
TC_ANY = re.compile(r"\bTC-[A-Z0-9]+-\d+\b")
RANGE = re.compile(r"\b(EC|TC-[A-Z0-9]+-)(\d+) đến \1(\d+)\b")

errors = 0


def report(level, msg):
    global errors
    if level == "ERROR":
        errors += 1
    print(f"{level}: {msg}")


def read(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def tables(text):
    """Trả về (tiêu đề mục, ô tiêu đề, [(số dòng, ô)]) cho mỗi bảng Markdown."""
    lines = text.splitlines()
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
        if (line.lstrip().startswith("|") and i + 1 < len(lines)
                and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1])):
            header = split_row(line)
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append((j + 1, split_row(lines[j])))
                j += 1
            yield heading, header, rows
            i = j
            continue
        i += 1


def skipped(heading):
    return any(s in heading for s in SKIP_SECTIONS)


def body_text(text):
    """Văn bản đã bỏ các mục SKIP_SECTIONS."""
    out, skip = [], False
    for line in text.splitlines():
        if line.startswith("#"):
            skip = skipped(line)
        if not skip:
            out.append(line)
    return "\n".join(out)


def mentioned_ids(text):
    ecs, tcs = set(EC_ANY.findall(text)), set(TC_ANY.findall(text))
    for m in RANGE.finditer(text):
        prefix, a, b = m.group(1), m.group(2), m.group(3)
        width = len(a)
        for k in range(int(a), int(b) + 1):
            (ecs if prefix == "EC" else tcs).add(f"{prefix}{k:0{width}d}")
    return ecs, tcs


def col(header, name):
    for i, h in enumerate(header):
        if h.strip().lower() == name.lower():
            return i
    return None


# ---------------------------------------------------------------- format
def cmd_format(files):
    for path in files:
        for n, line in enumerate(read(path).splitlines(), 1):
            if line.lstrip().startswith(">"):
                continue
            for ch in ("—", "·"):
                # Bỏ qua chỗ chỉ nhắc tới ký tự, ví dụ: Không dùng dấu "—"
                bare = line.replace(f'"{ch}"', "").replace(f"`{ch}`", "")
                if ch in bare:
                    report("ERROR", f'{path}:{n}: có dấu "{ch}" ngoài phần trích nguyên văn')
    print(f"format: Đã kiểm {len(files)} file")


# ---------------------------------------------------------------- changes
def cmd_changes(files):
    for path in files:
        found = False
        counts = {k: 0 for k in LOAI}
        for heading, header, rows in tables(read(path)):
            if "Thay đổi so với bản AI" not in heading:
                continue
            idx = col(header, "Loại")
            if idx is None:
                report("ERROR", f"{path}: Bảng thay đổi không có cột Loại")
                continue
            found = True
            for n, cells in rows:
                value = cells[idx] if idx < len(cells) else ""
                if value in counts:
                    counts[value] += 1
                else:
                    report("ERROR", f'{path}:{n}: Loại "{value}" không thuộc {LOAI}')
        if found:
            summary = ", ".join(f"{k} {v}" for k, v in counts.items())
            print(f"changes: {path}: {summary}")
        else:
            report("WARN", f'{path}: Không có bảng "Thay đổi so với bản AI" (bản review bắt buộc có)')


# ---------------------------------------------------------------- classes
def load_classes(path):
    classes = {}
    for heading, header, rows in tables(read(path)):
        if skipped(heading) or not rows:
            continue
        idx = col(header, "Loại")
        for n, cells in rows:
            if not EC_ID.match(cells[0]):
                continue
            if cells[0] in classes:
                report("ERROR", f"{path}:{n}: Mã lớp {cells[0]} bị định nghĩa lại (lần đầu ở dòng {classes[cells[0]][0]})")
                continue
            if idx is None:
                kind = "Output"
            else:
                v = cells[idx] if idx < len(cells) else ""
                kind = "GĐ" if v.startswith("GĐ") else "KH" if v.startswith("KH") else "H" if v.startswith("H") else f"? ({v})"
            classes[cells[0]] = (n, kind)
    return classes


def cmd_classes(ec_file):
    classes = load_classes(ec_file)
    counts = {}
    for _, kind in classes.values():
        counts[kind] = counts.get(kind, 0) + 1
    for kind, c in counts.items():
        if kind.startswith("?"):
            report("ERROR", f"{ec_file}: {c} lớp có Loại không đọc được: {kind}")
    nums = sorted(int(k[2:]) for k in classes)
    gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in nums] if nums else []
    print(f"classes: {ec_file}: {len(classes)} lớp; " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    if gaps:
        report("WARN", f"{ec_file}: Các số lớp bị bỏ trống (kiểm xem có cố ý không): {gaps}")
    return classes


# ---------------------------------------------------------------- coverage
def cmd_coverage(ec_file, tc_files):
    classes = load_classes(ec_file)
    defined = {}
    referenced_tc, referenced_ec = set(), set()
    covered_by_table = {}

    for path in tc_files:
        text = read(path)
        for heading, header, rows in tables(text):
            if skipped(heading) or not rows:
                continue
            tc_col = col(header, "Test case")
            first = header[0].strip().lower() if header else ""
            for n, cells in rows:
                # Định nghĩa ở ô đầu
                if TC_ID.match(cells[0]):
                    key = cells[0]
                    if key in defined:
                        report("ERROR", f"{path}:{n}: {key} bị định nghĩa lại (đã có ở {defined[key]})")
                    else:
                        defined[key] = f"{path}:{n}"
                # Định nghĩa ở cột Test case của bảng giá trị biên
                if first == "điểm" and tc_col is not None and tc_col < len(cells):
                    cell = cells[tc_col]
                    if "đã có" not in cell:
                        for key in TC_ANY.findall(cell):
                            if key in defined:
                                report("ERROR", f"{path}:{n}: {key} bị định nghĩa lại (đã có ở {defined[key]})")
                            else:
                                defined[key] = f"{path}:{n}"
                # Bảng phủ lớp: ô đầu là lớp, có cột Test case
                if EC_ID.match(cells[0]) and tc_col is not None and first in ("lớp", "mã"):
                    cell = cells[tc_col] if tc_col < len(cells) else ""
                    covered_by_table[cells[0]] = bool(mentioned_ids(cell)[1])
        ecs, tcs = mentioned_ids(body_text(text))
        referenced_ec |= ecs
        referenced_tc |= tcs

    if covered_by_table:
        for ec in classes:
            if ec not in covered_by_table:
                report("ERROR", f"{ec} không có dòng trong bảng phủ lớp")
            elif not covered_by_table[ec]:
                report("ERROR", f"{ec} có dòng trong bảng phủ lớp nhưng không có test case")
    else:
        report("WARN", "Không tìm thấy bảng phủ lớp (bảng có cột Lớp và Test case); chỉ kiểm theo việc lớp có được nhắc tới")
        for ec in classes:
            if ec not in referenced_ec:
                report("ERROR", f"{ec} không được nhắc tới trong file test case")

    unknown_ec = sorted(referenced_ec - set(classes), key=lambda x: int(x[2:]))
    if unknown_ec:
        report("WARN", f"Mã lớp được nhắc mà không có trong {ec_file}: {unknown_ec}")
    undefined = sorted(referenced_tc - set(defined))
    if undefined:
        report("WARN", "Mã test case được nhắc mà không được định nghĩa (kiểm xem có phải mã đã bỏ, nhắc có chủ ý không): "
               + ", ".join(undefined))
    print(f"coverage: {len(classes)} lớp, {len(defined)} test case được định nghĩa trong {len(tc_files)} file")


# ---------------------------------------------------------------- main
def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("format").add_argument("files", nargs="+")
    sub.add_parser("changes").add_argument("files", nargs="+")
    sub.add_parser("classes").add_argument("ec_file")
    c = sub.add_parser("coverage")
    c.add_argument("ec_file")
    c.add_argument("tc_files", nargs="+")
    a = sub.add_parser("all")
    a.add_argument("--ec")
    a.add_argument("--tc", nargs="*", default=[])
    a.add_argument("--files", nargs="*", default=[])
    args = p.parse_args()

    if args.cmd == "format":
        cmd_format(args.files)
    elif args.cmd == "changes":
        cmd_changes(args.files)
    elif args.cmd == "classes":
        cmd_classes(args.ec_file)
    elif args.cmd == "coverage":
        cmd_coverage(args.ec_file, args.tc_files)
    elif args.cmd == "all":
        if args.files:
            cmd_format(args.files)
            cmd_changes([f for f in args.files if "ai_raw" not in f.replace("\\", "/")])
        if args.ec:
            cmd_classes(args.ec)
            if args.tc:
                cmd_coverage(args.ec, args.tc)

    print(f"Kết quả: {errors} ERROR")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
