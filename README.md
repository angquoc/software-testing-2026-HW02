# HW02-AI: Domain Testing on EShop (Software Testing 2026)

Sinh viên: Nguyễn Thị Ánh Ngọc 
MSSV: 23120061 

SUT: [EShop](https://github.com/ttbhanh/eshop-sut) (commit `85af3ba`)

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `report.md` / `report.pdf` | Báo cáo chính: Domain Testing + BVA cho 4 feature, AI gap analysis, AI Critique, Disclosure, Appendix B (AI Audit Report) |
| `prompt_log.md` / `.pdf` | Appendix A: Prompt log có timestamp |
| `features/` | Mỗi feature một thư mục: Đặc tả, output AI nguyên văn (`ai_raw/`), bản đã review từng bước, test case, ảnh chụp |
| `bugs/` | Bug report, liên kết tới GitHub Issues của nhóm |
| `skills/` | Agent Skills: Domain Testing, Boundary Value Analysis |
| `forms/` | [AI-02] Audit Report, [AI-03] Disclosure, [AI-05] Privacy Checklist |
| `tools/` | Script hỗ trợ (xuất prompt log, điền form, ...) |
| `git_log.txt` | Git commit log |

## Feature đã chọn

| Pool | Feature | Nền tảng | Thư mục |
|---|---|---|---|
| A | FR-01 Đăng ký tài khoản | Web | `features/A_FR-01_DangKy/` |
| B | FR-07 Giỏ hàng | Web | `features/B_FR-07_GioHang/` |
| C | FR-17 Quản lý mã giảm giá (CRUD) | Web Admin | `features/C_FR-17_QuanLyCoupon/` |
| D | FR-04 Quản lý hồ sơ cá nhân | Mobile | `features/D_FR-04_HoSo_Mobile/` |

## Test Summary Report

Số feature: 4. "Đã chạy" gồm cả test case Blocked, Khác giả định, Không áp dụng; trạng thái chi tiết ở `06_results.md` của từng feature. Bug: Số issue trên GitHub của nhóm.

| Feature | TC thiết kế | Đã chạy | Pass | Fail | Chưa chạy | Bug |
|---|---|---|---|---|---|---|
| A: FR-01 | 96 | 46 | 9 | 19 | 50 | 13 (#42 đến #54) |
| B: FR-07 | | | | | | |
| C: FR-17 | 115 | 46 | 26 | 13 | 69 | 12 (#55 đến #66) |
| D: FR-04 (Mobile) | | | | | | |
| **Tổng** | | | | | | |

## Video demo

| Nội dung | Link |
|---|---|
| Agent Skill `domain-testing-design`: Chạy trọn feature D (FR-04 Hồ sơ, Mobile) từ S0 đến S5 | https://youtu.be/c8caqIW1d7M |

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
|---|---|---|---|
| 1 | Feature A: FR-01 (Domain + Boundary) | 25 | |
| 2 | Feature B: FR-07 (Domain + Boundary) | 25 | |
| 3 | Feature C: FR-17 (Domain + Boundary) | 25 | |
| 4 | Feature D: FR-04 Mobile (Domain + Boundary) | 15 | |
| 5 | Agent Skills | 10 | |
| | **Total** | **100** | |
