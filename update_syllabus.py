import os

content = """# Giáo Trình Chi Tiết Các Buổi Học: Thành Thạo AI Tools × Vận Hành AI Project

> **Nguồn tham chiếu:** `plan-dao-tao-PM-AI-integrated.md` (Plan chính thức)  
> **Thời lượng tiêu chuẩn:** **2.5 – 3 tiếng / buổi** (150 – 180 phút)  
> **Mô hình học tập:** **Interactive Demo tại lớp + Homework áp dụng dự án thật sau buổi học**

---

## Cấu Trúc Khung Thời Gian Chuẩn Cho Mỗi Buổi Học (180 phút)

| Thời gian | Phân bổ | Hoạt động chính |
|---|---|---|
| **00:00 - 00:30** (30m) | **Review Homework Buổi Trước** | Chữa bài tập về nhà buổi trước, Trainer & Peer feedback 2-3 bài xuất sắc / bài còn lỗi |
| **00:30 - 01:10** (40m) | **Lý Thuyết & Context** | Đặt vấn đề thực tế, bối cảnh Agentic SDLC, tư duy & nguyên tắc cốt lõi |
| **01:10 - 02:10** (60m) | **Live Demo & Case Analysis** | Trainer thao tác trực tiếp trên Tool (ChatGPT/Claude/Copilot/Jira), mổ xẻ prompt mẫu & chạy các kịch bản |
| **02:10 - 02:40** (30m) | **Mini Guided-Practice** | Học viên thực hành nhanh tại lớp (15-20m) để nắm thao tác dưới sự hướng dẫn trực tiếp của Trainer |
| **02:40 - 03:00** (20m) | **Giao Bài Tập Về Nhà & Q&A** | Hướng dẫn đề bài tập về nhà trên dự án thật, giải thích Rubric chấm điểm & quy trình Peer Review |

---

## Quy Trình Bài Tập & Peer Review Sau Mỗi Buổi Học (Homework Cycle)

```mermaid
flowchart LR
    A["1. Học tại lớp (180 phút)<br/>Nghe Demo & Mini-Practice"] --> B["2. Bài tập về nhà (3-5 ngày)<br/>Thực hành trên DỰ ÁN THẬT"]
    B --> C["3. Nộp bài & Peer Review (1-2 ngày)<br/>Chấm chéo giữa các PM"]
    C --> D["4. Trainer Audit & Sign-off<br/>Chữa bài đầu buổi học tiếp theo"]
```

1. **Thực hành trên Dự án thật (Homework):** Học viên áp dụng kiến thức/tool đã học vào dự án thực tế đang quản lý (viết PRD thật, User Story thật, Status Report thật, Token tracking thật...).
2. **Nộp bài & Peer Review (Async):** Nộp sản phẩm lên kênh chung (Notion/Jira/Drive). Phân công cặp đôi chấm chéo (Peer Review) dựa trên Rubric chuẩn.
3. **Trainer Audit:** Trainer chọn 2-3 bài tiêu biểu (1 bài làm tốt + 1 bài còn nhiều lỗi) để nhận xét chi tiết vào 30 phút đầu buổi học tiếp theo.

---

# GIAI ĐOẠN 1: ONBOARDING & NỀN TẢNG (L0 → L1)

---

### Buổi 1: Giới Thiệu Landscape AI Tools cho PM & Context Agentic SDLC
* **Mã buổi:** B01 (Tham chiếu Khóa 1)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** PM hiểu toàn cảnh các công cụ AI đang có (ChatGPT, Claude, Copilot, Notion AI, Jira AI), vị thế PM là Orchestrator giữa Người + AI, và ranh giới an toàn dữ liệu.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Khởi động & Đặt vấn đề**
  * Thảo luận thực trạng làm việc hiện tại của PM: Tốn bao nhiêu % thời gian cho họp hành, viết tài liệu, báo cáo thủ công?
  * Khái niệm Agentic SDLC: Tại sao khi Dev/Tester dùng AI agent, vai trò PM thay đổi từ "người giục task" sang "người chỉ huy workflow & quản lý Quality Gate"?
* **00:30 - 01:10 (40m) — Tổng quan Landscape AI Tool cho PM 2026**
  * So sánh 3 nhóm tool: LLM Chat (Claude, ChatGPT, Gemini), AI nhúng sẵn (M365 Copilot, Notion AI, Jira AI), AI Code Agents.
  * Phân tích ưu/nhược điểm từng tool cho từng tác vụ PM (Tốc độ, độ dài context, bảo mật, tích hợp).
* **01:10 - 02:10 (60m) — Live Demo & Thiết lập môi trường**
  * Trainer Demo: Nhập cùng 1 yêu cầu vào ChatGPT vs Claude vs M365 Copilot -> Phân tích khác biệt output.
  * Hướng dẫn thiết lập môi trường: System Prompt / Custom Instructions cá nhân hóa cho PM.
  * Nguyên tắc bảo mật Red-line: Loại dữ liệu tuyệt đối KHÔNG đưa vào AI công cộng.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên mở 3 tool (ChatGPT, Claude, Copilot), gõ 1 câu lệnh giới thiệu dự án của mình để thử nghiệm phản hồi của từng tool.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Q&A**

#### 📝 Bài Tập Về Nhà Sau Buổi 1 (Homework B01)
* **Đề bài:** 
  1. Hoàn thành đăng nhập 100% các tài khoản AI tool công ty cấp.
  2. Làm bài Quiz 10 câu về Nguyên tắc Bảo mật dữ liệu (đạt ≥ 70%).
  3. Viết 1 bài thu hoạch ngắn (khoảng 300 từ) đánh giá 3 tác vụ PM trong tuần tới bạn dự định áp dụng AI.
* **Quy trình nộp & Peer Review:** Nộp file text/markdown lên hệ thống trước Buổi 2 24h.

---

### Buổi 2: Thực Hành Prompt Library & Tác Vụ PM Cơ Bản
* **Mã buổi:** B02 (Tham chiếu Khóa 2)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Sử dụng thành thạo Prompt Library seed của team; chuyển đổi transcript cuộc họp thô thành Meeting Notes chuẩn chỉnh & Action Items rõ ràng.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B01 & Chữa bài**
  * Trainer chữa bài Quiz an toàn dữ liệu, giải đáp các thắc mắc về cài đặt tool từ Buổi 1.
* **00:30 - 01:10 (40m) — Lý thuyết & Nguyên tắc xử lý Meeting Transcript**
  * Giới thiệu Prompt Library Seed của công ty.
  * Cách trích xuất transcript từ Teams/Zoom/Meet.
  * Kỹ thuật ép AI lọc nhiễu, trích xuất đúng: (1) Key Decisions, (2) Action Items (Ai làm - Việc gì - Deadline), (3) Open Questions.
* **01:10 - 02:10 (60m) — Live Demo: Chuyển Transcript thô thành Meeting Notes**
  * Trainer demo trực tiếp với 1 đoạn transcript cuộc họp Refinement 15 phút rắc rối.
  * Mổ xẻ cách xử lý khi AI bịa ra Action Item (Hallucination check) và cách chỉnh prompt để bắt AI xuất ra định dạng Bảng Markdown.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Trainer cấp 1 đoạn transcript mẫu ngắn (5 phút). Học viên dùng Prompt seed dán vào Claude/ChatGPT để sinh ra Meeting Notes trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Q&A**

#### 📝 Bài Tập Về Nhà Sau Buổi 2 (Homework B02)
* **Đề bài (Thực hành dự án thật):** 
  * Lấy 1 file transcript cuộc họp THẬT trong tuần của dự án bạn đang quản lý.
  * Dùng AI tạo bản Meeting Notes chính thức + 1 Email tóm tắt gửi cho Stakeholders.
* **Quy trình nộp & Peer Review:** 
  * Nộp bài lên kênh chung. Phân công cặp đôi chấm chéo (Peer Review) kiểm tra xem có thông tin nào bị AI bịa ra không.

---

### Buổi 3: Quality Gate & Token Economics Cơ Bản
* **Mã buổi:** B03 (Tham chiếu Khóa 3)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Nắm vững khái niệm Quality Gate (Cổng chất lượng); hiểu Token Cost là gì, cách đọc Dashboard chi phí AI tool.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B02 & Chữa Meeting Notes thật**
  * Trainer chiếu 2 bản Meeting Notes bài tập của học viên lên màn hình, chỉ ra các lỗi Hallucination thường gặp.
* **00:30 - 01:10 (40m) — Lý thuyết Quality Gate & Token Economics**
  * Quy trình Quality Gate 4 bước: Self-check -> AI Audit -> Human Peer Review -> Merge.
  * Token Economics: Input vs Output Token, Context Window, cách đọc Dashboard chi phí OpenAI/Anthropic/Azure.
* **01:10 - 02:10 (60m) — Live Demo: Phân tích Dashboard Token & Role-play Quality Gate**
  * Trainer Demo đọc file log Token Usage, phát hiện điểm bất thường (spike) do agent chạy lặp.
  * Trainer Demo kịch bản ứng phó khi Dev đòi bypass Quality Gate vì cháy deadline.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Cho 1 bảng dữ liệu Token mẫu. Học viên gõ lệnh nhờ AI phân tích top 3 task tốn token nhất trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Tổng kết L1**

#### 📝 Bài Tập Về Nhà Sau Buổi 3 (Homework B03)
* **Đề bài:** 
  1. Hoàn thành bài Quiz 15 câu về Token Economics & Quality Gate (đạt ≥ 70%).
  2. Viết 1 kịch bản ứng phó (500 từ) khi khách hàng hoặc Tech Lead yêu cầu bỏ qua Quality Gate trong dự án của bạn.
* **Điều kiện Tốt nghiệp L1:** Pass Quiz + Sign-off bài tập B01, B02, B03.

---

# GIAI ĐOẠN 2: STANDARD PM TASKS & ARTIFACTS (L1 → L2)

---

### Buổi 4: Prompt Engineering Cơ Bản Cho PM
* **Mã buổi:** B04 (Tham chiếu Khóa 5)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Thành thạo công thức viết prompt 5 thành phần chuẩn (Role - Context - Task - Format - Constraint); biết kỹ thuật bổ sung ví dụ (Few-shot prompting).

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review & Tổng kết Giai đoạn L1**
  * Chúc mừng các PM hoàn thành L1, trao Badge L1.
* **00:30 - 01:10 (40m) — Khung Cấu Trúc Prompt Chuẩn (RISEN / RCTFC Framework)**
  * 5 thành phần chuẩn: Role - Context - Task - Format - Constraint.
  * Kỹ thuật Few-shot (đưa ví dụ mẫu) & Refinement Loop (sửa lỗi hội thoại).
* **01:10 - 02:10 (60m) — Live Demo: Chuyển Prompt "rác" thành Prompt chuyên nghiệp**
  * Trainer demo biến câu lệnh ngắn "viết PRD cho tôi" thành prompt 5 phần chi tiết.
  * Demo kỹ thuật Few-shot: Đưa 1 đoạn User Story mẫu để AI bắt chước đúng chuẩn công ty.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên viết 1 prompt chuẩn 5 thành phần cho tác vụ "Tóm tắt rủi ro dự án" trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Q&A**

#### 📝 Bài Tập Về Nhà Sau Buổi 4 (Homework B04)
* **Đề bài (Thực hành dự án thật):** 
  * Viết **3 Prompt chuẩn 5 thành phần** ứng dụng cho 3 công việc thực tế trong tuần tới của dự án bạn (gồm 1 prompt phân tích requirement, 1 prompt viết mail gửi khách, 1 prompt tổng hợp task).
* **Quy trình nộp & Peer Review:** Nộp lên kho Prompt cá nhân, đổi bài cho bạn bên cạnh review theo Rubric 5 thành phần.

---

### Buổi 5: AI-Assisted User Story & Acceptance Criteria (AC)
* **Mã buổi:** B05 (Tham chiếu Khóa 6)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Dùng AI generate User Story từ requirement thô, tạo Acceptance Criteria theo chuẩn Given-When-Then; phát hiện mơ hồ & edge case bằng AI.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B04 & Sửa 3 Prompt mẫu**
  * Trainer chữa 3 bài prompt về nhà tiêu biểu, chỉ ra các lỗi thiếu Constraint hoặc thiếu Context.
* **00:30 - 01:10 (40m) — Quy trình 3 bước tạo User Story & AC với AI**
  * Bước 1: Input Requirement -> AI draft User Story breakdown.
  * Bước 2: Dán Story -> AI generate AC (Given-When-Then).
  * Bước 3: AI Challenge (Yêu cầu AI đóng vai QA tìm Edge cases ẩn).
* **01:10 - 02:10 (60m) — Live Demo: Tìm 10 Edge Cases ẩn cho 1 tính năng**
  * Trainer demo lấy 1 tính năng "Đăng ký tài khoản" -> Đưa prompt cho AI đóng vai "QA khó tính" để bới ra 10 lỗi tiềm ẩn về mạng, OTP, ký tự đặc biệt.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên cho AI tạo 1 User Story + 3 dòng AC cho 1 tính năng đơn giản trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Q&A**

#### 📝 Bài Tập Về Nhà Sau Buổi 5 (Homework B05)
* **Đề bài (Thực hành dự án thật):** 
  * Chọn 1 Epics/Feature THẬT trong dự án hiện tại.
  * Dùng AI tạo bộ **5 User Story + Acceptance Criteria đầy đủ** (Happy path + Unhappy path) + Danh sách Edge Cases đã được AI audit.
* **Quy trình nộp & Peer Review:** Nộp lên Jira/Backlog nháp, Peer Review kiểm tra tính rõ ràng trước khi chuyển cho Dev.

---

### Buổi 6: AI-Assisted PRD (Draft PRD < 30 Phút)
* **Mã buổi:** B06 (Tham chiếu Khóa 7)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Đạt cột mốc tạo bản thảo PRD (Product Requirement Document) đầy đủ cấu trúc từ Brief ngắn trong **dưới 30 phút**.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B05 & Chữa User Story thật**
  * Trainer review bộ User Story & AC của 2 học viên, đánh giá độ phủ của Edge cases.
* **00:30 - 01:10 (40m) — Framework Tốc Độ Tạo PRD Với AI**
  * Cấu trúc PRD 6 mục chuẩn.
  * Chiến lược "Phân rã Section" (Tạo khung -> Nhồi chi tiết từng mục -> AI Self-Review).
* **01:10 - 02:10 (60m) — Live Demo: 20 phút từ Brief đến PRD hoàn chỉnh**
  * Trainer thao tác trực tiếp trên Claude: Phút 0-3 tạo khung, phút 4-12 điền Problem/Goal, phút 13-18 điền Functional Specs, phút 19-20 AI tự audit.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Cho 1 đoạn Brief ngắn 1 trang. Học viên dùng AI tạo khung PRD và điền 2 mục đầu tiên (Problem & Goals) trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Q&A**

#### 📝 Bài Tập Về Nhà Sau Buổi 6 (Homework B06 - ĐẠT COT MỐC L2)
* **Đề bài (Thực hành dự án thật):** 
  * Lấy 1 Yêu cầu/Brief tính năng THẬT sắp triển khai của dự án bạn.
  * Thao tác tạo 1 bản **PRD Draft hoàn chỉnh 6 mục trong dưới 30 phút** bằng AI.
* **Quy trình nộp & Peer Review:** Nộp bài đính kèm video quay màn hình hoặc log thời gian làm bài (<30m). Peer review đánh giá chất lượng PRD.

---

### Buổi 7: AI-Assisted Status Report Cho Stakeholders (Non-Technical)
* **Mã buổi:** B07 (Tham chiếu Khóa 8)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Dùng AI dịch thuật ngữ kỹ thuật/số liệu sprint thô thành báo cáo 1 trang ngắn gọn, ngôn ngữ kinh doanh (Business Value) khiến Stakeholders hiểu ngay.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B06 (PRD Draft < 30m)**
  * Trainer tuyên dương các bài PRD làm dưới 30 phút đạt chất lượng tốt.
* **00:30 - 01:10 (40m) — Tư duy Dịch Thuật Báo Cáo Cho Stakeholders**
  * Chuyển đổi Technical Metrics (Velocity, Defect density, Refactoring) -> Business Value (Lead Time, Cost, Customer Experience).
  * Prompt Template "Executive Status Report 4 ô vuông".
* **01:10 - 02:10 (60m) — Live Demo: Biến Sprint Log hỗn loạn thành Báo cáo 1 trang**
  * Trainer dán log sprint gồm bug, task trễ, token cost tăng -> AI viết thành Executive Summary 1 trang cực kỳ lịch sự và chuyên nghiệp.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên dán 1 đoạn log bug thô vào AI, gõ prompt nhờ AI dịch thành câu văn báo cáo khách hàng trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà & Q&A**

#### 📝 Bài Tập Về Nhà Sau Buổi 7 (Homework B07)
* **Đề bài (Thực hành dự án thật):** 
  * Lấy dữ liệu Sprint tuần này của dự án thật.
  * Dùng AI tạo bản **Status Report 1 trang dành cho Stakeholder Non-technical** (COO/CMO/Khách hàng).
* **Quy trình nộp & Peer Review:** Nộp bài cho Mentor review trước khi gửi thật cho Sếp/Khách hàng.

---

### Buổi 8: Token Tracking & ROI Calculation (Nộp Drill 1)
* **Mã buổi:** B08 (Tham chiếu Khóa 9 & 11)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Thực hành kỹ năng theo dõi chi phí Token & Hướng dẫn hoàn thành **Drill 1 (Tính toán ROI ứng dụng AI)**.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B07 & Chữa Status Report**
  * Trainer nhận xét các mẫu Status Report gửi Stakeholder.
* **00:30 - 01:10 (40m) — Phương pháp Tính ROI & Theo Dõi Token Cost**
  * Công thức ROI (%): $(Net Savings - Tool Cost) / Tool Cost \times 100\%$.
  * Quy đổi giờ làm tiết kiệm của PM/Dev thành tiền.
  * Viết Prompt để AI tóm tắt Dashboard Token Usage hàng tuần.
* **01:10 - 02:10 (60m) — Live Demo: Lập Bảng Tính ROI Defendable Trước CFO**
  * Trainer demo nhập số liệu dự án 3 tháng vào AI -> AI hỗ trợ tính toán và viết bài luận bảo vệ ngân sách mua license AI trước CFO.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên tính nhanh ROI cá nhân khi dùng ChatGPT Plus trong 1 tháng vừa qua (15 phút).
* **02:40 - 03:00 (20m) — Giao Đề Bài Drill 1 (Bắt buộc L2)**

#### 📝 Bài Tập Về Nhà Sau Buổi 8 (NỘP BÀI DRILL 1 CHÍNH THỨC)
* **Đề bài Drill 1:** 
  * Nhận bộ số liệu bài toán mẫu + Lấy số liệu thực tế dự án mình.
  * Lập Bảng tính ROI đầy đủ + Viết bài giải trình 500 từ bảo vệ trước CFO/Tech Lead bằng AI.
* **Quy trình nộp:** Nộp bài Drill 1 chính thức để lấy điểm chứng nhận L2.

---

### Buổi 9: Quality Gate Role-Play & Xử Lý Tình Huống Rủi Ro (Pass Drill 5)
* **Mã buổi:** B09 (Tham chiếu Khóa 10)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Thực hành kịch bản đàm phán & Giữ vững Cổng Chất lượng (Quality Gate) trước áp lực tiến độ.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài nộp Drill 1 & Chấm điểm ROI**
  * Trainer công bố kết quả chấm Drill 1.
* **00:30 - 01:10 (40m) — 3 Kịch bản Sức ép Quality Gate & Kỹ thuật Đàm phán**
  * Sức ép từ Khách hàng, sức ép từ Dev Lead, sức ép khi AI score thấp.
  * Dùng AI chuẩn bị kịch bản đàm phán (Talking Points) và quy trình Emergency Bypass.
* **01:10 - 02:10 (60m) — Live Demo & Role-play Mẫu Tại Lớp**
  * Trainer đóng vai Tech Lead đòi bypass Quality Gate vs 1 Học viên đóng vai PM.
  * Phân tích các câu đáp trả thông minh giúp PM giữ vững cổng chất lượng.
* **02:10 - 02:40 (30m) — Mini Guided-Practice (Đóng vai theo cặp 15m)**
  * Học viên chia cặp tập đóng vai nhanh tình huống khách hàng đòi release gấp.
* **02:40 - 03:00 (20m) — Giao Bài tập Video Role-play Drill 5**

#### 📝 Bài Tập Về Nhà Sau Buổi 9 (NỘP BÀI DRILL 5 CHÍNH THỨC)
* **Đề bài Drill 5:** 
  * Quay 1 **Video Role-play 5 phút** (hoặc thu âm) giữa bạn (PM) và đồng nghiệp (Tech Lead/Khách hàng) về 1 tình huống sức ép Quality Gate.
* **Quy trình nộp & Peer Review:** Nộp video lên hệ thống. Trainer & Peer xem và chấm điểm Pass/Fail Drill 5.

---

### Buổi 10: Xây Dựng & Quản Trị Prompt Library Cá Nhân (Đạt Milestone L2)
* **Mã buổi:** B10 (Tham chiếu Khóa 12)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Hoàn thiện **Thư viện Prompt cá nhân ≥ 10 prompt** có tổ chức, metadata rõ ràng, sẵn sàng cho giai đoạn Solo PM.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Video Drill 5 & Ký duyệt Sign-off**
  * Công bố danh sách PM pass Drill 5.
* **00:30 - 01:10 (40m) — Cấu trúc Quản trị Prompt Library Cá Nhân**
  * Tiêu chuẩn Thẻ Metadata Prompt (ID, Task, Tool, Input, Content, Output, Version).
  * Hướng dẫn sử dụng Notion Database / Obsidian / Git để quản lý prompt.
* **01:10 - 02:10 (60m) — Live Demo: Chuẩn hóa 1 Thư viện Prompt mẫu**
  * Trainer demo đưa 10 prompt rải rác vào 1 Notion Database cực kỳ khoa học và tra cứu trong 3 giây.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên đưa 2 prompt tốt nhất của mình vào bảng chuẩn hóa trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập Hoàn thiện Thư viện Prompt & Tổng kết L2**

#### 📝 Bài Tập Về Nhà Sau Buổi 10 (HOÀN THÀNH MILESTONE L2)
* **Đề bài:** 
  * Nộp đường link **Thư viện Prompt cá nhân gồm ≥ 10 prompt** đã được chuẩn hóa đầy đủ Metadata.
* **Điều kiện Cấp Chứng Nhận L2:** 
  * [x] Pass PRD draft < 30 phút (B06)
  * [x] Pass Status report non-tech (B07)
  * [x] Pass Drill 1 (B08) & Drill 5 (B09)
  * [x] Thư viện Prompt ≥ 10 prompt chuẩn (B10)
  * Phân công Mentor hỗ trợ cho đợt **OJT Solo PM dự án nhỏ (3-4 tuần)**.

---

# GIAI ĐOẠN 3: ADVANCED WORKFLOW & TEAM STANDARDIZATION (L2 → L3)

---

### Buổi 11 & 12: Prompt Nâng Cao & Tích Hợp AI Vào Toàn Bộ Sprint Cycle
* **Mã buổi:** B11 & B12 (Tham chiếu Khóa 14 - 2 buổi)
* **Thời lượng:** **2 buổi × 3 tiếng** (Tổng 360 phút)
* **Mục tiêu:** Kỹ thuật Chain-of-Thought & Multi-Agent; Nhúng AI xuyên suốt Sprint Cycle (Target: Tiết kiệm ≥ 30% thời gian).

#### Timetable Buổi 11 (180 phút): Prompting Nâng Cao (Chain-of-Thought & Multi-Agent)
* **00:00 - 00:30 (30m) — Review OJT Solo PM & Khởi động L3**
* **00:30 - 01:10 (40m) — Kỹ thuật Chain-of-Thought & Meta-Prompting**
  * Ép AI suy luận từng bước (`Think step by step`). Meta-prompting: Dùng AI viết prompt cho AI.
* **01:10 - 02:10 (60m) — Live Demo: Multi-perspective Prompting**
  * Demo 1 AI đóng vai Dev, 1 AI đóng vai Tester cùng phản biện 1 Epic.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Thực hành gõ prompt Chain-of-thought breakdown 1 Epic phức tạp trong 15 phút.
* **02:40 - 03:00 (20m) — Giao bài tập về nhà Buổi 11**

#### Timetable Buổi 12 (180 phút): Tích Hợp AI Xuyên Suốt Sprint Cycle
* **00:00 - 00:30 (30m) — Review Bài tập Buổi 11**
* **00:30 - 01:10 (40m) — Bản đồ AI Sprint Cycle (Planning -> Refinement -> Standup -> Retro)**
* **01:10 - 02:10 (60m) — Live Demo: Chạy thử 1 Sprint Workflow bằng AI**
  * Demo AI hỗ trợ Planning, Refine story trên Jira, tóm tắt Daily standup, phân tích Retro feedback.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Cho dữ liệu Retro thô. Học viên dùng AI phân loại feedback thành Action Items trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà Buổi 12**

#### 📝 Bài Tập Về Nhà Sau Buổi 11 & 12 (Homework Đo Lường Saved Time)
* **Đề bài (Thực hành dự án thật):** 
  * Áp dụng AI Workflow đầy đủ vào 1 Sprint thực tế của dự án bạn.
  * Lập bảng đo đạc thời gian trước và sau khi có AI cho các tác vụ PM -> **Chứng minh tiết kiệm ≥ 30% thời gian**.
* **Quy trình nộp:** Nộp Bảng đo đạc Saved Time kèm minh chứng artifact.

---

### Buổi 13: Token Budget Forecast & Variance Management (Nộp Drill 2)
* **Mã buổi:** B13 (Tham chiếu Khóa 15)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Hướng dẫn & Nộp **Drill 2 (Dự báo ngân sách Token chính xác ±20%)**.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bảng Saved Time ≥ 30% của học viên**
* **00:30 - 01:10 (40m) — Phương pháp Dự Báo Token 3 Kịch Bản (Best/Expected/Worst Case)**
  * Xây dựng khoảng tin cậy (Confidence Interval) và cơ chế Cảnh báo tự động (Alert).
* **01:10 - 02:10 (60m) — Live Demo: Xây dựng Mô hình Dự báo Token trên Excel/AI**
  * Trainer demo nhập dữ liệu 3 sprint trước để AI dự báo token cost cho 3 sprint tới.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Cho dữ liệu bài tập nhỏ, học viên nhờ AI tính nhanh kịch bản Expected Case trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Đề Bài Drill 2 (Bắt buộc L3)**

#### 📝 Bài Tập Về Nhà Sau Buổi 13 (NỘP BÀI DRILL 2 CHÍNH THỨC)
* **Đề bài Drill 2:** 
  * Nhận bộ dữ liệu bài toán mẫu. Dùng AI tính toán dự báo Token Cost cho 3 Sprint tới đạt độ chính xác sai số $\le \pm 20\%$.
* **Quy trình nộp:** Nộp bài Drill 2 để Trainer chấm và công nhận.

---

### Buổi 14 & 15: Risk Management AI Project (Drill 3) & Stakeholder Transparency (Drill 4)
* **Mã buổi:** B14 & B15 (Tham chiếu Khóa 16 & 17 - 2 buổi)
* **Thời lượng:** **2 buổi × 3 tiếng** (Tổng 360 phút)
* **Mục tiêu:** Complete **Drill 3 (Risk Register 15 rủi ro AI)** & **Drill 4 (Chính sách minh bạch AI + Video Walkthrough 5m)**.

#### Timetable Buổi 14 (180 phút): Risk Management trong AI Project (Hướng dẫn Drill 3)
* **00:00 - 00:30 (30m) — Review kết quả Drill 2 (Forecast ±20%)**
* **00:30 - 01:10 (40m) — 5 Rủi ro đặc thù của dự án AI & Cách quản lý**
* **01:10 - 02:10 (60m) — Live Demo: Xây dựng Risk Register 15 rủi ro với AI**
* **02:10 - 02:40 (30m) — Mini Guided-Practice:** Cho 1 rủi ro AI, học viên dùng AI đề xuất 3 giải pháp Mitigation trong 15m.
* **02:40 - 03:00 (20m) — Giao bài tập Drill 3**

#### Timetable Buổi 15 (180 phút): Stakeholder Transparency & Policy (Hướng dẫn Drill 4)
* **00:00 - 00:30 (30m) — Review Bài nộp Drill 3**
* **00:30 - 01:10 (40m) — Nguyên tắc Minh Bạch AI Với Khách Hàng & Policy mẫu**
* **01:10 - 02:10 (60m) — Live Demo: Soạn Status Report 1 trang + kịch bản Video Walkthrough 5m**
* **02:10 - 02:40 (30m) — Mini Guided-Practice:** Học viên viết 3 câu khẳng định minh bạch AI gửi khách hàng trong 15m.
* **02:40 - 03:00 (20m) — Giao bài tập Drill 4**

#### 📝 Bài Tập Về Nhà Sau Buổi 14 & 15 (NỘP DRILL 3 & DRILL 4)
* **Bài tập Drill 3:** Nộp bảng Risk Register 15 rủi ro (đã verify, phân loại T1-T4, có Owner & Mitigation Plan).
* **Bài tập Drill 4:** Nộp Status Report 1 trang + **Video Walkthrough 5 phút** thuyết trình về tiến độ và chính sách minh bạch AI.

---

### Buổi 16: AI-Assisted Sprint Data Analysis & Rút Insight
* **Mã buổi:** B16 (Tham chiếu Khóa 18)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Dùng AI phân tích dữ liệu thô của Sprint (Velocity, Quality, Token/Feature, Bug Rate) -> Rút ra Actionable Insights.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Video Drill 4 & Chấm bài**
* **00:30 - 01:10 (40m) — Kỹ thuật Data Prompting Phân Tích Raw Data**
  * Export dữ liệu Jira/GitHub -> Ép AI tìm Anomalies & Root Causes.
* **01:10 - 02:10 (60m) — Live Demo: Phân tích 200 dòng log Jira thô**
  * Trainer dán CSV log ticket -> AI chỉ ra module bị nghẽn và ngốn token cao nhất.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Cho file CSV nhỏ, học viên gõ lệnh nhờ AI tìm 1 bất thường trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà Buổi 16**

#### 📝 Bài Tập Về Nhà Sau Buổi 16 (Homework B16)
* **Đề bài (Thực hành dự án thật):** 
  * Export dữ liệu 3 Sprint gần nhất của dự án thật.
  * Dùng AI phân tích xuất ra **3 Insight quan trọng + 3 Action Items** cho Sprint tiếp theo.

---

### Buổi 17: Chọn Đúng Tool Cho Đúng Task & Anti-Pattern Workshop
* **Mã buổi:** B17 (Tham chiếu Khóa 19 & 20)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Xây dựng **Tool Selection Matrix**; Nhận diện và phòng tránh **10 Anti-patterns** khi dùng AI.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Bài tập B16 & Chữa báo cáo Insight**
* **00:30 - 01:10 (40m) — Ma Trận Chọn Tool & 10 Anti-Patterns Cần Tránh**
  * Bảng tra cứu "Task X -> Tool Y". Mổ xẻ 10 sai lầm phổ biến khi dùng AI trong quản lý dự án.
* **01:10 - 02:10 (60m) — Live Demo & Case Study Discussion**
  * Trainer đưa 2 Case Study thực tế dính Anti-pattern -> Hướng dẫn dùng AI phân tích Root Cause.
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên điền 5 dòng vào Tool Selection Matrix cá nhân trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập về nhà Buổi 17**

#### 📝 Bài Tập Về Nhà Sau Buổi 17 (Homework B17)
* **Đề bài:** Hoàn thiện bảng Tool Selection Matrix cho toàn bộ tác vụ PM của dự án bạn đang lead.

---

### Buổi 18: Chuẩn Hóa Template Cho Team & Đóng Gói Skill (Hoàn Thành L3)
* **Mã buổi:** B18 (Tham chiếu Khóa 21)
* **Thời lượng:** 2.5 - 3 tiếng (180 phút)
* **Mục tiêu:** Xây dựng **tối thiểu 1 Prompt Template / Skill được team adopt thực tế**.

#### Timetable Chi Tiết Tại Lớp (180 phút)
* **00:00 - 00:30 (30m) — Review Tool Selection Matrix của học viên**
* **00:30 - 01:10 (40m) — Quy Trình Đóng Gói Prompt Thành Team Skill / Template**
  * Tiêu chuẩn Deterministic output, User guide kèm ví dụ Input/Output.
* **01:10 - 02:10 (60m) — Live Demo: Showcase 3 Team Template Mẫu**
  * Trainer demo 3 template chuẩn công ty đang dùng (Auto PRD, Jira Ticket Refiner, Weekly Digest).
* **02:10 - 02:40 (30m) — Mini Guided-Practice tại lớp**
  * Học viên viết User Guide ngắn cho 1 prompt tốt nhất của mình trong 15 phút.
* **02:40 - 03:00 (20m) — Giao Bài tập Đóng gói Template & Tổng kết L3 Assessment**

#### 📝 Bài Tập Về Nhà Sau Buổi 18 (ĐẠT CHỨNG NHẬN L3 - PROFICIENT)
* **Đề bài:** Nộp **1 Prompt Template / Skill đã được đóng gói hoàn chỉnh** kèm bằng chứng có ít nhất 1 đồng nghiệp trong team sử dụng thực tế.
* **Điều kiện Đạt Cấp Độ L3:**
  * [x] AI Workflow tiết kiệm ≥ 30% thời gian (có data đo)
  * [x] Pass đầy đủ Drill 1, 2, 3, 4, 5
  * [x] Có ≥ 1 Template được team adopt
  * [x] Lead Medium Project pass 30-Day Rollout

---

## Bảng Tổng Hợp Bài Tập Về Nhà & Output Bắt Buộc (Homework & Deliverables)

| Buổi | Tên buổi | Bài tập về nhà (Homework thực hiện sau buổi học) | Quy trình Review & Sign-off |
|---|---|---|---|
| **B01** | Landscape AI & Agentic SDLC | Quiz An toàn dữ liệu + Bài thu hoạch 3 tác vụ AI | Quiz ≥ 70%, Trainer check bài thu hoạch |
| **B02** | Meeting Notes & Prompt Seed | **Dự án thật:** Tạo Meeting Notes + Email từ transcript thật | Peer review kiểm tra Hallucination |
| **B03** | Quality Gate & Token Economics | Quiz Token + Bài kịch bản ứng phó 500 từ | Trainer audit & **Ký duyệt L1** |
| **B04** | Prompt Engineering Cơ Bản | **Dự án thật:** 3 Prompt chuẩn 5 thành phần cho 3 task | Peer review theo Rubric 5 thành phần |
| **B05** | User Story & AC | **Dự án thật:** Bộ 5 User Story + AC + Edge cases audit | Peer review trước khi giao Dev |
| **B06** | AI-Assisted PRD | **Dự án thật:** Draft PRD hoàn chỉnh 6 mục < 30 phút | Nộp log thời gian (<30m) + PRD draft |
| **B07** | Status Report Non-technical | **Dự án thật:** Status Report 1 trang cho Stakeholder | Mentor review trước khi gửi Khách |
| **B08** | ROI & Token Tracking | **Nộp Drill 1:** Lập bảng ROI + Giải trình CFO bằng AI | Trainer chấm & tính điểm L2 |
| **B09** | Quality Gate Role-play | **Nộp Drill 5:** Video Role-play 5m tình huống Quality Gate | Trainer & Peer xem video chấm Pass/Fail |
| **B10** | Prompt Library Cá Nhân | Nộp Thư viện Prompt cá nhân ≥ 10 prompt chuẩn | Trainer check Metadata & **Ký duyệt L2** |
| **B11-12**| Advanced Prompt & Sprint | **Dự án thật:** Bảng đo Saved Time (Target ≥ 30%) | Kiểm tra chứng minh Saved Time |
| **B13** | Token Budget Forecast | **Nộp Drill 2:** Bảng dự báo Token 3 Sprint (±20%) | Trainer chấm sai số forecast $\le \pm 20\%$ |
| **B14-15**| Risk & Transparency | **Nộp Drill 3 (Risk 15) + Drill 4 (Video 5m Transparency)** | Trainer & Peer chấm bài nộp Drill 3 & 4 |
| **B16** | Sprint Data Analysis | **Dự án thật:** Export CSV 3 Sprint -> 3 Insights + 3 Actions | Trainer review tính khả thi của Action |
| **B17** | Tool Matrix & Anti-patterns | **Dự án thật:** Bảng Tool Selection Matrix cho dự án | Peer review bảng chọn tool |
| **B18** | Template Standardization | **Nộp 1 Template/Skill đóng gói** + Bằng chứng Team Adopt | Trainer audit & **Ký duyệt Badge L3** |

---

*Cập nhật cấu trúc: Chuyển toàn bộ phần thực hành chi tiết trên dự án thật & Peer review thành Bài tập về nhà (Homework Cycle) sau mỗi buổi học.*
"""

output_path = r'c:\Users\Admin\Claude\Projects\PlanPM\syllabus-chi-tiet-tung-buoi-hoc-PM-AI.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {output_path} successfully!")
