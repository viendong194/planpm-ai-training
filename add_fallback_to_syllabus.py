import os

file_path = r'c:\Users\Admin\Claude\Projects\PlanPM\syllabus-chi-tiet-tung-buoi-hoc-PM-AI.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

fallback_section = """
---

## 🛡️ Phương Án Dự Phòng Khi Dự Án Thật Không Có Tình Huống (Fallback Options)

Trường hợp dự án hiện tại của PM đang ở giai đoạn bảo trì, tạm dừng, hoặc không có đủ tình huống thực tế (ví dụ: không có cuộc họp mới để lấy transcript, không có PRD mới cần viết, không có dữ liệu token...), học viên được chủ động lựa chọn **1 trong 3 phương án thay thế** sau để làm bài tập về nhà:

| Phương án | Cách thực hiện | Khi nào áp dụng |
|---|---|---|
| **PA 1: Ngân Hàng Case Study Mẫu** *(Khuyên dùng)* | Ban đào tạo cung cấp sẵn 3 Dự án giả lập chuẩn (E-Commerce *TechMart*, Fintech *PayEasy*, SaaS *WorkFlowPro*) với đầy đủ Brief, Transcript thô, Bug Log và Token Data để học viên dùng xuyên suốt khóa học. | Dự án thật chưa khởi chạy, PM chưa được gán dự án, hoặc dự án quá ít activity. |
| **PA 2: Làm lại (Re-do) Dự án Quá khứ** | Lấy 1 tính năng / tài liệu cũ mà PM từng viết bằng tay trước đây -> Sử dụng AI làm lại từ đầu để so sánh đối chiếu chất lượng & đo đạc thời gian tiết kiệm. | Muốn so sánh chính xác % thời gian tiết kiệm (Saved Time) giữa làm tay vs AI. |
| **PA 3: Ghép cặp Co-PM với Đồng nghiệp** | Ghép cặp 2 người với 1 PM khác trong lớp đang lead dự án lớn/nóng -> Cùng tham gia làm bài tập trên dữ liệu dự án của đồng nghiệp đó. | Muốn cọ xát với bài toán thực tế phức tạp của team khác. |

---
"""

# Insert fallback_section right after "Trainer Audit & Sign-off..." block
target_str = "3. **Trainer Audit:** Trainer chọn 2-3 bài tiêu biểu (1 bài làm tốt + 1 bài còn nhiều lỗi) để nhận xét chi tiết vào 30 phút đầu buổi học tiếp theo."

if target_str in content:
    new_content = content.replace(target_str, target_str + "\n" + fallback_section)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fallback section added successfully!")
else:
    print("Target string not found!")
