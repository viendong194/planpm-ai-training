# Khung Năng Lực Tích Hợp: PM Vận Hành AI Project × Dùng AI Tool (L1 → L5)

> **Góc độ đánh giá:** Mỗi level định nghĩa **PM đang vận hành gì trong dự án** (operational context) và **dùng AI tool thành thạo đến đâu để thực hiện công việc đó** (tool proficiency). Hai chiều không tách rời — tool proficiency phục vụ trực tiếp cho công việc vận hành.  
> **Nguyên tắc level tăng theo 3 chiều:** Scope dự án lớn hơn → Tự chủ cao hơn → Tool usage phức tạp hơn.

---

## Tổng quan 5 Level

| Level | Tên | Operational Stage | Tool Proficiency |
|---|---|---|---|
| **L1** | Apprentice 🌱 | Shadow PM L3+, quan sát 1 sprint thực tế | Dùng AI với prompt có sẵn; capture và tóm tắt thông tin |
| **L2** | Practitioner 🥉 | Solo PM dự án nhỏ ≤ 3 sprint | Tự viết prompt; AI hỗ trợ toàn bộ PM artifacts tiêu chuẩn |
| **L3** | Proficient 🥈 | Lead dự án medium, ROI dương | AI tích hợp vào workflow; tối ưu và chuẩn hóa cho team |
| **L4** | Expert 🥇 | Multi-project, coach PM junior | Xây custom tool/agent; define AI tool standard cho team |
| **L5** | Master 💎 | Lead transformation ≥ 1 SBU | AI tool strategy cấp tổ chức; thought leadership |

---

## L1 — Apprentice 🌱

### Operational Context
PM đang trong giai đoạn **học và quan sát**. Nhiệm vụ chính: shadow PM L3+ qua 1 sprint thực tế, hiểu 3 mental model shifts (Tracker→Orchestrator, Time-billing→Outcome-billing, Velocity→Quality Velocity), làm quen với Quality Gate và token tracking cơ bản.

**Phạm vi công việc:** Không lead độc lập — hỗ trợ và học từ mentor.

### Tool Skills Cần Có Ở Level Này

| Công việc cần làm | Tool skill hỗ trợ |
|---|---|
| Ghi chép sprint meeting, standup | AI tóm tắt meeting transcript → meeting notes draft |
| Đọc hiểu tài liệu dự án, roadmap | AI tóm tắt document dài, explain khái niệm mới |
| Báo cáo nhỏ cho mentor | AI draft email, note ngắn từ bullet points |
| Làm quen với Quality Gate docs | AI giải thích checklist, Q&A về quy trình |

**Mức độ tool:** Dùng prompt có sẵn từ thư viện team, chưa tự viết prompt.

### Milestone Xác Nhận L1
- Hoàn thành onboarding AI tools + quiz kiến thức Agentic SDLC cơ bản đạt 70%
- Shadow 1 sprint dưới mentor PM L3+ — mentor sign-off
- Tự chạy được 5 prompt từ thư viện mà không cần hỗ trợ
- Tạo được 1 meeting notes hoàn chỉnh từ transcript sprint bằng AI

---

## L2 — Practitioner 🥉

### Operational Context
PM **tự lead 1 dự án nhỏ** ≤ 3 sprint. Nhiệm vụ chính: viết PRD và User Story rõ ràng, track token consumption hàng tuần, áp dụng Quality Gate đúng quy trình, báo cáo stakeholder cơ bản, tính ROI đơn giản.

**Phạm vi công việc:** Solo PM với mentor support khi cần. Scope nhỏ, team ≤ 5 người.

### Tool Skills Cần Có Ở Level Này

| Công việc cần làm | Tool skill hỗ trợ |
|---|---|
| Viết PRD từ requirement thô | AI-assisted PRD draft — từ brief input ra structure đầy đủ trong < 30 phút |
| Viết User Story + AC | AI generate User Story từ PRD; generate Acceptance Criteria từ User Story |
| Báo cáo stakeholder non-technical | AI-assisted Status Report — translate sprint data → business language |
| Tính ROI feature (Drill 1) | AI hỗ trợ tính effort traditional vs AI-enhanced; format bảng ROI |
| Theo dõi token cost cơ bản | Dùng AI đọc và tóm tắt dashboard data; nhận biết spike bất thường |
| Quality Gate role-play chuẩn bị (Drill 5) | AI tạo scenario practice; simulate stakeholder push-back |

**Mức độ tool:** Tự viết prompt đủ cấu trúc (role + context + yêu cầu + format). Có prompt library cá nhân ≥ 10 prompt. Thành thạo ≥ 2 tool.

### Milestone Xác Nhận L2
- Solo PM 1 dự án nhỏ ≤ 3 sprint, đạt KPI baseline, token cost trong budget
- PRD draft bằng AI trong < 30 phút từ brief input
- Status Report non-technical được stakeholder hiểu (không hỏi thêm về jargon)
- ROI tính được và defendable trước Tech Lead (Drill 1)
- Prompt library cá nhân ≥ 10 prompt có metadata (task, tool, khi nào dùng)

---

## L3 — Proficient 🥈

### Operational Context
PM **lead dự án medium** độc lập, pass full 30-Day Rollout với ROI dương. Nhiệm vụ chính: risk mitigation thuần thục (Risk Register đầy đủ), token budget forecast ±20%, báo cáo stakeholder solid, Quality Velocity ổn định, kiên định trước deadline pressure.

**Phạm vi công việc:** Lead độc lập, mentor support tối thiểu. Scope medium, team 5–10 người.

### Tool Skills Cần Có Ở Level Này

| Công việc cần làm | Tool skill hỗ trợ |
|---|---|
| Token Budget Forecast (Drill 2) | AI phân tích 3 sprint data → forecast best/expected/worst case với confidence interval ±20% |
| Risk Register 15 risks (Drill 3) | AI generate AI-specific risks (hallucination, vendor lock-in, token variance, team resistance); human verify và prioritize T1 |
| Stakeholder Status Report + video (Drill 4) | AI translate sprint metrics → business value (Lead Time ↓, Defect Density ↓, Cost/feature ↓); draft 1-page report |
| Handle 3 concern phổ biến của khách | AI chuẩn bị talking points; practice Q&A với AI đóng vai khách |
| Sprint data analysis | AI phân tích Quality Velocity trend, token cost/feature, defect density — rút actionable insight |
| Chuẩn hóa prompt template cho team | Xây dựng prompt library team-level; viết hướng dẫn sử dụng |

**Mức độ tool:** Chain-of-thought prompting, few-shot examples. Workflow AI tích hợp vào toàn bộ sprint cycle. Tiết kiệm ≥ 30% thời gian so với không dùng AI. Bắt đầu chia sẻ template cho team.

### Milestone Xác Nhận L3
- Lead ≥ 1 dự án medium pass full 30-Day Rollout, ROI dương, Quality Velocity ổn định
- Token forecast ±20% actual (Drill 2 pass)
- Risk Register đầy đủ T1 mitigation (Drill 3 pass)
- Stakeholder Status Report + video walkthrough 5 phút (Drill 4 pass)
- Workflow AI tiết kiệm ≥ 30% thời gian (có data đo)
- ≥ 1 prompt template team đang dùng thực tế

---

## L4 — Expert 🥇

### Operational Context
PM **lead multi-project** đồng thời, **coach PM junior lên L2**, define best practice cho team. Nhiệm vụ chính: orchestrate nhiều team AI, xây dựng contract/pricing model có buffer token, thiết lập alert system, chuẩn hóa quy trình cho toàn team.

**Phạm vi công việc:** Lead ≥ 3 project, coach ≥ 2 PM lên L2, define standard.

### Tool Skills Cần Có Ở Level Này

| Công việc cần làm | Tool skill hỗ trợ |
|---|---|
| Quản lý nhiều project cùng lúc | Custom GPT/Agent tự động tổng hợp status từ nhiều project; dashboard tự động |
| Tạo User Story hàng loạt | Agent tự động generate User Story từ meeting notes/Figma |
| Chuẩn hóa Risk Assessment cho team | Custom GPT với Risk Matrix chuẩn; auto-suggest mitigation |
| Training PM junior về AI tools | Xây curriculum chuẩn; có demo workflow live |
| Token monitoring tự động | Automation (Zapier/Make + AI) alert khi token cost > 80% budget |
| Contract/pricing với AI buffer | AI hỗ trợ tính buffer 20–30%; model outcome-billing |

**Mức độ tool:** Xây Custom GPT/Agent; kết nối AI với automation (Zapier/Make/n8n); define AI tool guideline cho team (tool nào dùng khi nào, data nào không đưa vào AI).

### Milestone Xác Nhận L4
- Lead ≥ 3 project với ROI dương đồng thời
- Coach ≥ 2 PM lên L2 thành công
- ≥ 1 Custom GPT/Agent đang được team dùng thực tế
- AI tool guideline được team adopt
- Đã train ≥ 3 PM về AI tools với curriculum chuẩn

---

## L5 — Master 💎

### Operational Context
PM **lead transformation ≥ 1 SBU** sang Agentic SDLC. Nhiệm vụ chính: define KPI standards toàn SBU, xây dựng AI tool governance, thought leadership về AI Operations, đo ROI ở cấp tổ chức.

**Phạm vi công việc:** Quyết định cấp tổ chức, thought leader trong cộng đồng PM.

### Tool Skills Cần Có Ở Level Này

| Công việc cần làm | Tool skill hỗ trợ |
|---|---|
| AI tool strategy cho SBU | AI hỗ trợ market research tool, compare vendor, draft strategy doc |
| ROI measurement cấp tổ chức | Automation đo ROI adoption; AI tổng hợp và visualize data |
| Governance & security policy | AI draft acceptable use policy, security checklist, review framework |
| Thought leadership content | AI co-write article, talk outline, framework documentation |
| Evaluate AI tool mới | Structured evaluation framework; AI hỗ trợ pilot testing |

**Mức độ tool:** Define AI tool strategy và governance cho tổ chức. Evaluate và onboard tool mới trước khi mainstream. Thought piece được cộng đồng bên ngoài đón nhận.

### Milestone Xác Nhận L5
- Lead transformation ≥ 1 SBU — Quality Velocity và ROI cải thiện đo được
- AI tool strategy được leadership approve và đang thực thi
- ≥ 1 thought piece (bài viết / talk / framework) được cộng đồng bên ngoài đón nhận

---

## Bảng So Sánh Tổng Hợp

| Tiêu chí | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| **Scope dự án** | Shadow 1 sprint | Solo ≤ 3 sprint | Lead medium, ROI dương | Multi-project | SBU transformation |
| **Tool task tiêu biểu** | Meeting notes, tóm tắt doc | PRD, User Story, Status Report, ROI | Token forecast, Risk Register, Sprint analysis | Custom GPT, automation | Strategy, governance |
| **Viết prompt** | Dùng prompt sẵn | Tự viết đủ cấu trúc | Chain-of-thought, few-shot | System prompt, custom agent | Org-wide framework |
| **Thời gian tiết kiệm** | — | Đo baseline | ≥ 30% | Nhân lên qua team | Đo ở cấp tổ chức |
| **Lan tỏa** | Nhận hỗ trợ | — | Chia sẻ template | Train team, define standard | Thought leadership |
| **Drills liên quan** | — | Drill 1, 5 | Drill 2, 3, 4 | — | — |

---

## Nguyên tắc đánh giá

Level xác nhận dựa trên **output thực tế từ dự án thật**, không phải bài tập lý thuyết:
- Drill là **bài tập luyện tập** chuẩn bị cho OJT — không phải milestone cuối cùng
- Milestone cuối luôn là **kết quả từ dự án thực**: ROI dương, token trong budget, stakeholder hiểu report, team dùng tool bạn tạo ra

---

*Nguồn tham chiếu: `3.1.2_PM_Roadmap.md` (operational context) + best practice AI tools cho PM (tool proficiency)*  
*Cập nhật lần cuối: 2026-06-23*
