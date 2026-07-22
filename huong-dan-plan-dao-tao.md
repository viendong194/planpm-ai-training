# Hướng Dẫn Xây Dựng Plan Đào Tạo Năng Lực Nhân Sự

## Tổng Quan

Quy trình xây dựng plan đào tạo gồm **5 bước chính**, áp dụng cho các role: **PM, DEV, QA** theo khung năng lực từ **L1 → L5**.

---

## Bước 1: Định Nghĩa Khung Năng Lực (L1 → L5)

**Mục tiêu:** Xây dựng bảng mô tả rõ ràng từng level cho từng role.

**Với mỗi level, cần xác định:**
- Năng lực cốt lõi cần có (hard skill + soft skill)
- Phạm vi công việc có thể đảm nhận độc lập
- Mức độ tự chủ và trách nhiệm
- Kỳ vọng về output/KPI

**Output:** Bảng định nghĩa năng lực theo role × level

| Level | PM | DEV | QA |
|---|---|---|---|
| L1 | Mô tả năng lực PM L1 | Mô tả năng lực DEV L1 | Mô tả năng lực QA L1 |
| L2 | ... | ... | ... |
| ... | ... | ... | ... |
| L5 | ... | ... | ... |

---

## Bước 2: Định Nghĩa Lộ Trình Đào Tạo Theo Transition

**Mục tiêu:** Xác định để chuyển từ level này lên level tiếp theo cần học những gì.

**Với mỗi transition (L0→L1, L1→L2, ..., L4→L5), và từng role, cần xác định:**
- Danh sách khóa học bắt buộc
- Danh sách khóa học khuyến nghị (tùy chọn)
- Thời lượng ước tính mỗi khóa
- Hình thức học (internal training, external course, OJT, mentoring...)

**Output:** Bảng lộ trình đào tạo

| Transition | Role | Khóa học | Hình thức | Thời lượng |
|---|---|---|---|---|
| L0 → L1 | PM | Khóa A: Nhập môn PM | Internal | 2 buổi |
| L0 → L1 | PM | Khóa B: Agile cơ bản | E-learning | 8 giờ |
| L1 → L2 | DEV | Khóa C: Clean Code | Internal | 3 buổi |
| ... | ... | ... | ... | ... |

---

## Bước 3: Mapping Năng Lực Nhân Sự Hiện Tại

**Mục tiêu:** Đánh giá và xác định level hiện tại của từng nhân sự.

**Cách thực hiện:**
- Dùng bảng năng lực ở Bước 1 làm tiêu chí đánh giá
- Kết hợp: tự đánh giá + manager đánh giá + peer review (nếu có)
- Ghi nhận gap so với level tiếp theo

**Output:** Bảng danh sách nhân sự × level hiện tại

| Nhân sự | Role | Level hiện tại | Gap cần bổ sung | Ghi chú |
|---|---|---|---|---|
| Nguyễn A | PM | L1 | Khóa B, Khóa C | Ưu tiên đào tạo Q3 |
| Trần B | DEV | L2 | Khóa D | Sẵn sàng Q4 |
| Lê C | QA | L0 | Khóa A, B, C | Mới onboard |
| ... | ... | ... | ... | ... |

---

## Bước 4: Lập Plan Đào Tạo & Mục Tiêu Tỷ Lệ Level

**Mục tiêu:** Đặt mục tiêu cụ thể về phân bố level và timeline đạt được.

**4a. Xác định mục tiêu tỷ lệ level theo thời gian**

Ví dụ mục tiêu cho team PM (10 người):

| Thời điểm | L0 | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|---|
| Hiện tại (T0) | 2 | 5 | 3 | 0 | 0 | 0 |
| Sau 6 tháng | 0 | 3 | 5 | 2 | 0 | 0 |
| Sau 12 tháng | 0 | 1 | 4 | 4 | 1 | 0 |

**4b. Lập plan từng khóa học**

Với mỗi khóa học, cần xác định:
- Tên khóa học và mục tiêu
- Đối tượng học (role, level)
- Người đứng lớp / phụ trách
- Thời gian tổ chức (ngày, số buổi)
- Số lượng học viên dự kiến
- Phương pháp đánh giá sau khóa

---

## Bước 5: Lập Lịch Đào Tạo (Schedule)

**Mục tiêu:** Sắp xếp thứ tự ưu tiên và lịch cụ thể các khóa học.

**Nguyên tắc sắp xếp:**
- Ưu tiên các khóa nền tảng (L0→L1) trước
- Tránh xung đột lịch dự án của học viên
- Phân bổ đều tải giảng dạy cho người đứng lớp
- Có buffer time để đánh giá và điều chỉnh

**Output:** Bảng lịch đào tạo tổng thể

| Tháng | Tuần | Khóa học | Role | Level | Giảng viên | Học viên | Hình thức |
|---|---|---|---|---|---|---|---|
| T7/2025 | Tuần 1 | Nhập môn PM | PM | L0→L1 | Anh X | 5 người | Offline |
| T7/2025 | Tuần 3 | Agile cơ bản | PM, DEV | L0→L1 | Chị Y | 12 người | Online |
| T8/2025 | Tuần 2 | Clean Code | DEV | L1→L2 | Anh Z | 8 người | Offline |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Checklist Tổng Hợp

- [ ] Bước 1: Bảng định nghĩa năng lực L1→L5 (PM, DEV, QA)
- [ ] Bước 2: Bảng lộ trình đào tạo theo transition
- [ ] Bước 3: Bảng mapping nhân sự × level hiện tại
- [ ] Bước 4: Bảng mục tiêu tỷ lệ level theo thời gian + plan từng khóa
- [ ] Bước 5: Lịch đào tạo tổng thể (schedule)

---

*Tài liệu này là template hướng dẫn — cần điều chỉnh số liệu, tên khóa học và timeline phù hợp với thực tế tổ chức.*
