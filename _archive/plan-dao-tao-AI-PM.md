# Plan Đào Tạo Năng Lực AI cho Project Manager (PM)

> ⚠️ **BẢN LƯU TRỮ (superseded)** — Bản này đã được gộp vào bản chính thức `../plan-dao-tao-PM-AI-integrated.md`. Giữ lại để tham khảo, không dùng làm plan chính. Nội dung thiên về vận hành/Agentic SDLC.
>
> **Phạm vi:** Đào tạo kỹ năng AI / Agentic SDLC cho role PM  
> **Timeline:** 6 tháng  
> **Framework:** L1 → L5 (tập trung đạt L3 trong 6 tháng)  
> **Nguồn tham chiếu:** `3.1.2_PM_Roadmap.md` + `huong-dan-plan-dao-tao.md`

---

## Bước 1: Khung Năng Lực AI theo Level (PM)

Trong mô hình Agentic SDLC, PM chuyển từ **"Người theo dõi tiến độ"** thành **"Orchestrator của hệ Người + AI"** — quản trị throughput tổng thể, kiểm soát chất lượng quy trình AI + Human, tối ưu chi phí token + nhân lực, educate stakeholder. Giá trị đo bằng **outcome** (feature shipped + verified) thay vì hour worked.

### 1.1. Tư duy cốt lõi cần chuyển đổi (3 Mental Model Shifts)

| Tư duy cũ | → | Tư duy mới |
|---|---|---|
| Theo dõi từng task của từng người | → | Theo dõi **throughput** tổng thể của hệ Người + AI |
| Đôn đốc nhân sự nhanh hơn | → | Tối ưu **bottleneck** (thường là review, không phải coding) |
| Báo cáo "X% task completed" | → | Báo cáo Quality Velocity + token cost + AI hallucination rate |
| Bill theo số giờ làm việc | → | Bill theo **giá trị bàn giao** (Outcome-billing) |
| Velocity thô (story/sprint) | → | **Quality Velocity** = story đã pass tất cả Quality Gate / sprint |

> **Quality Velocity:** Velocity thô 20 story; Quality Velocity 12 story (8 stuck ở Code Gate vì coverage thấp) → Velocity thực = **12**. Báo cáo cho stakeholder dùng Quality Velocity; velocity thô chỉ dùng nội bộ debug.

### 1.2. Năng lực cốt lõi theo Level

| Level | Vai trò & Năng lực | Phạm vi tự chủ | Milestone xác nhận |
|---|---|---|---|
| **L1 Apprentice** 🌱 | Học cơ chế tracking AI metric + Quality Gate; hiểu 3 mental model shifts; theo dõi project nhỏ dưới mentor | Shadow PM L3+; hỗ trợ 1 sprint | Hoàn thành onboarding + 1 sprint shadow PM L3+ + quiz kiến thức cơ bản đạt 70% |
| **L2 Practitioner** 🥉 | Tự lead 1 project nhỏ; áp dụng AI capacity planning + token tracking cơ bản; tạo Risk Register; viết status report cho non-technical | Solo PM 1 project ≤ 3 sprint | Solo PM 1 project ≤ 3 sprint, đạt KPI baseline, token cost trong budget |
| **L3 Proficient** 🥈 | Lead project size medium; risk mitigation thuần thục; báo cáo stakeholder solid; kiên định trước deadline pressure; forecast token budget ±20% | Lead ≥ 1 project medium | Lead ≥ 1 project medium pass full 30-Day Rollout với ROI dương, Quality Velocity ổn định |
| **L4 Expert** 🥇 | Lead multi-project; coach PM junior lên L2; define best practice cho team; xây dựng training material chuẩn cho khách; thiết lập alert + buffer contract | Lead ≥ 3 project + coach ≥ 2 PM | Coach ≥ 2 PM lên L2; lead ≥ 3 project với ROI dương |
| **L5 Master** 💎 | Strategy SBU/công ty; define KPI standards; thought leadership AI Operations; define chính sách chuẩn toàn SBU | Lead transformation ≥ 1 SBU | Lead transformation ≥ 1 SBU; thought piece (talk/article/framework) |

### 1.3. Năng lực cốt lõi cần phát triển (5 kỹ năng chính)

| Kỹ năng | Mô tả | Tại sao quan trọng |
|---|---|---|
| **Hybrid Resource Allocation** | AI vs Human task mapping; capacity planning theo capability mix (L2/L3/L4) của team | AI và human có strength khác nhau — phân sai = lãng phí cả 2 phía |
| **Token Economics** | Tracking weekly; forecast budget dựa trên baseline; set alert thresholds; investigate khi spike | Token cost là chi phí mới — không track = ngân sách dự án có thể vỡ trong 1-2 sprint |
| **Quality Gate Enforcement** | Honesty về data; áp dụng Emergency Bypass Procedure đúng quy trình; communication skill khi từ chối bypass | Bypass 1 lần = open Pandora's box — stakeholder/team sẽ liên tục push để bypass |
| **Stakeholder Education** | Translate AI metrics → business value; status report cho non-technical; handle 3 concern phổ biến (AI thay người? Code an toàn? Sao bill cao?) | Khách không hiểu Agentic SDLC sẽ có expectation sai về delivery và billing |
| **Risk Management** | Risk Matrix với AI-specific risks (hallucination, vendor lock-in, token cost variance, team resistance); T1 mitigation plan trước rollout; risk review cadence | Agentic SDLC có loại risk mới chưa từng có trong PM truyền thống |

---

## Bước 2: Lộ Trình Đào Tạo Theo Transition

### L0 → L1 (Onboarding AI Mindset) — ~4 tuần

**Mục tiêu:** Nắm 3 mental model shifts, hiểu Quality Velocity và Token Economics cơ bản, có trải nghiệm thực tế qua shadow sprint.

| # | Khóa học | Nội dung chính | Hình thức | Thời lượng | Bắt buộc? |
|---|---|---|---|---|---|
| 1 | **AI Mindset cho PM** | Agentic SDLC là gì; vai trò Orchestrator; 3 mental model shifts (Tracker→Orchestrator, Time-billing→Outcome-billing, Velocity→Quality Velocity) | Internal training | 2 buổi × 2h | Bắt buộc |
| 2 | **Quality Velocity 101** | Phân biệt velocity thô vs Quality Velocity; cách đọc và báo cáo dashboard; tại sao velocity thô đánh lừa trong môi trường AI | Internal training | 1 buổi × 2h | Bắt buộc |
| 3 | **Token Economics cơ bản** | Token là gì; cách track theo project/agent/developer; tại sao cost matter; đọc dashboard cơ bản | E-learning / self-study | 2h | Bắt buộc |
| 4 | **Shadow sprint (OJT)** | Theo dõi 1 sprint thực tế dưới mentor PM L3+; quan sát cách PM xử lý Quality Gate, token tracking, stakeholder report | OJT | 1 sprint (~2 tuần) | Bắt buộc |
| 5 | Đọc: *The Phoenix Project* | DevOps & flow management — nền tảng hiểu throughput thinking | Self-study | 8h | Khuyến nghị |

**Milestone L1:** Onboarding hoàn thành + 1 sprint shadow + quiz kiến thức cơ bản đạt 70%

---

### L1 → L2 (Apply trong project nhỏ) — ~6 tuần

**Mục tiêu:** Tự lead 1 project nhỏ, áp dụng được 3 kỹ năng cốt lõi (Hybrid Resource Allocation, Token Economics, Quality Gate).

| # | Khóa học | Nội dung chính | Hình thức | Thời lượng | Bắt buộc? |
|---|---|---|---|---|---|
| 6 | **Hybrid Resource Allocation** | AI vs Human task mapping; capacity planning theo capability mix; ví dụ: team 5 người 1L4+2L3+2L2 vs team 5 người toàn L2 — capacity khác nhau dù headcount giống | Internal workshop | 2 buổi × 2h | Bắt buộc |
| 7 | **Token Budget Forecast** — Drill 2 | Thực hành với 3 sprint data thực tế; forecast tháng tới với confidence interval (best/expected/worst case); mục tiêu forecast nằm trong ±20% actual | Workshop + drill | 1 buổi × 2h | Bắt buộc |
| 8 | **Quality Gate Enforcement** — Drill 5 | Role-play 3 scenario: (1) deadline pressure, (2) score dưới ngưỡng, (3) khách hàng push back; mentor đánh giá tính kiên định + empathy + giải pháp thay thế; thực hành Emergency Bypass Procedure | Workshop role-play | 1 buổi × 2h | Bắt buộc |
| 9 | **ROI Calculation cơ bản** — Drill 1 | 1 feature 2 sprint, team 5 người, baseline traditional; tính effort traditional vs AI-enhanced; token cost; net savings; ROI %; kết quả phải defendable trước Tech Lead | Self-practice + review | 2h | Bắt buộc |
| 10 | Khóa online: **CSM hoặc PSM I** | Agile/Scrum foundation | E-learning | 16h | Khuyến nghị |
| 11 | Đọc: *Accelerate* | DORA metrics; evidence-based PM | Self-study | 8h | Khuyến nghị |

**Milestone L2:** Solo PM 1 project nhỏ ≤ 3 sprint, đạt KPI baseline, token cost trong budget

---

### L2 → L3 (Lead project medium, thuần thục) — ~8 tuần

**Mục tiêu:** Lead project medium độc lập, risk mitigation thuần thục, báo cáo stakeholder solid, ROI dương.

| # | Khóa học | Nội dung chính | Hình thức | Thời lượng | Bắt buộc? |
|---|---|---|---|---|---|
| 12 | **Stakeholder Education** — Drill 4 | Translate AI metrics → business value (Lead Time ↓, Defect Density ↓, Cost per feature ↓); handle 3 concern phổ biến; thực hành Drill 4: viết Status Report 1 trang cho non-technical + record video walkthrough 5 phút | Internal workshop + peer review | 2 buổi × 2h | Bắt buộc |
| 13 | **Risk Management AI Project** — Drill 3 | AI-specific risks: hallucination, vendor lock-in, token cost variance, team resistance; thực hành Drill 3: Risk Register 15 risks (5 AI-specific), prioritize T1-T4, gán owner + mitigation cho top T1; risk review cadence | Workshop + drill | 2 buổi × 2h | Bắt buộc |
| 14 | **Anti-pattern Workshop** | Review và thảo luận 10 anti-pattern từ thực tế (xem Phần Anti-patterns); case study với từng pattern; cách nhận diện sớm và phòng tránh | Discussion + case study | 1 buổi × 2h | Bắt buộc |
| 15 | OJT: **Lead project medium** | Áp dụng 30-Day Rollout, track Quality Velocity + Token Cost / Feature + Defect Density Trend; mentor PM L4+ giám sát | Live project | Suốt T5-T6 | Bắt buộc |
| 16 | Đọc: *Inspired* | PM mindset, outcome > output | Self-study | 8h | Khuyến nghị |
| 17 | Đọc: *Crucial Conversations* | Skill khi từ chối Quality Gate bypass; communication dưới áp lực | Self-study | 8h | Khuyến nghị |
| 18 | Khóa: **Prosci Change Management** | Quản lý transition sang Agentic SDLC cho team và khách hàng | E-learning | 16h | Khuyến nghị |

**Milestone L3:** Lead ≥ 1 project medium pass full 30-Day Rollout với ROI dương, Quality Velocity ổn định

---

### L3 → L4 (Expert, Coach junior) — tham khảo, ngoài 6 tháng

| # | Khóa học | Hình thức | Thời lượng |
|---|---|---|---|
| 19 | **Coaching & Mentoring PM** — Kỹ năng coach PM L1/L2; feedback framework | Workshop | 2 buổi |
| 20 | **Multi-project Management với AI** — Orchestrate nhiều team AI cùng lúc; resource allocation across projects | Advanced workshop | 3 buổi |
| 21 | **Contract & Pricing cho AI Project** — Buffer token cost 20-30%; outcome-billing model; clause cho LLM pricing change | Internal | 2 buổi |
| 22 | **DORA Assessment** (Google Cloud) — đo & cải thiện DORA metrics | External | Ongoing |
| 23 | Đọc: *The Lean Startup* + *Sprint* (Jake Knapp) | Hypothesis-driven development; design sprint pattern | Self-study | 16h |

---

## Bước 3: Survey Đánh Giá Level Hiện Tại

> **File survey đầy đủ:** [survey-danh-gia-level-AI-PM.md](./survey-danh-gia-level-AI-PM.md)  
> Gửi file survey cho từng PM tự điền, sau đó manager tổng hợp vào bảng mapping bên dưới.  
> Bắt buộc collect baseline ở T0 — không có baseline = không thể prove ROI sau 6 tháng.

### Bảng mapping nhân sự (điền sau khi thu survey)

| STT | Họ tên | Level tự đánh giá | Level manager xác nhận | Gap chính cần bổ sung | Ưu tiên Q3 | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| ... | | | | | | |

---

## Bước 4: Mục Tiêu Tỷ Lệ Level (6 tháng)

> Template dưới dùng cho team 10 PM — điều chỉnh số lượng theo thực tế sau khi có kết quả survey.

| Thời điểm | L0 | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|---|
| **T0 — Hiện tại** | _ | _ | _ | _ | _ | _ |
| **T+2 tháng** | 0 | 60% | 30% | 10% | 0 | 0 |
| **T+4 tháng** | 0 | 20% | 50% | 30% | 0 | 0 |
| **T+6 tháng** | 0 | 10% | 30% | 50% | 10% | 0 |

**Mục tiêu cốt lõi 6 tháng:** ≥ 50% PM đạt L3 (tự lead project medium với AI, ROI dương)

**3 KPI quan trọng nhất PM phải đạt sau 6 tháng:**
1. **Quality Velocity** — biết tính và báo cáo đúng cho stakeholder
2. **Token Cost / Feature** — track được và forecast trong ±20%
3. **Defect Density Trend** — hiểu trend và có action khi xấu đi

---

### Kế hoạch từng khóa học (6 tháng)

| # | Tên khóa | Đối tượng | Giảng viên/phụ trách | Tháng dự kiến | Số học viên | Đánh giá |
|---|---|---|---|---|---|---|
| 1 | AI Mindset cho PM | PM L0 | PM L4/L5 nội bộ | Tháng 1 | Toàn bộ PM | Quiz 70% |
| 2 | Quality Velocity 101 | PM L0 | PM L4/L5 nội bộ | Tháng 1 | Toàn bộ PM | Quiz + discussion |
| 3 | Token Economics cơ bản | PM L0 | Self-study + Q&A session | Tháng 1 | Toàn bộ PM | Bài tập đọc dashboard |
| 4 | Shadow sprint (OJT) | PM L0→L1 | Mentor PM L3+ | Tháng 1-2 | Từng cặp mentor-mentee | Mentor sign-off |
| 5 | Hybrid Resource Allocation | PM ≥ L1 | PM L4+ | Tháng 2 | PM đã qua L1 | Drill capacity plan |
| 6 | Token Budget Forecast (Drill 2) | PM ≥ L1 | PM L4+ | Tháng 2 | PM đã qua L1 | Forecast ±20% actual |
| 7 | Quality Gate Enforcement (Drill 5) | PM ≥ L1 | PM L4+ | Tháng 3 | PM đã qua L1 | Role-play pass — mentor sign-off |
| 8 | ROI Calculation (Drill 1) | PM ≥ L1 | PM L4+ | Tháng 3 | PM đã qua L1 | Drill 1 defendable trước Tech Lead |
| 9 | Stakeholder Education (Drill 4) | PM ≥ L2 | PM L4+ | Tháng 4 | PM đạt L2 | Status report + video walkthrough 5' |
| 10 | Risk Management AI Project (Drill 3) | PM ≥ L2 | PM L4+ | Tháng 4 | PM đạt L2 | Risk Register T1 đầy đủ |
| 11 | Anti-pattern Workshop | PM ≥ L2 | PM L4+ | Tháng 5 | PM đạt L2 | Discussion + case study quiz |
| 12 | OJT: Lead project medium | PM ≥ L2 đủ điều kiện | PM L4+ giám sát | Tháng 5-6 | PM đạt L2 | 30-Day Rollout ROI dương |
| 13 | Review tổng kết 6 tháng | Toàn PM | PM Lead | Tháng 6 | Tất cả | L3 Assessment chính thức |

---

## Bước 5: Lịch Đào Tạo Tổng Thể (6 tháng)

| Tháng | Tuần | Hoạt động | Đối tượng | Hình thức | Ghi chú |
|---|---|---|---|---|---|
| **T1** | T1 | Thu survey đánh giá level + collect KPI baseline (T0) | Toàn PM | Meeting | Bắt buộc — không collect baseline = không prove ROI |
| **T1** | T1 | Kick-off: set expectation về Agentic SDLC | Toàn PM | Seminar | Manager confirm level |
| **T1** | T2 | Khóa 1: AI Mindset cho PM (3 mental model shifts) | Toàn PM | Offline/Online | 2 buổi × 2h |
| **T1** | T3 | Khóa 2: Quality Velocity 101 | Toàn PM | Offline | 1 buổi × 2h |
| **T1** | T4 | Khóa 3: Token Economics cơ bản | Toàn PM | E-learning + Q&A | Deadline cuối T1 |
| **T2** | T1-T4 | Khóa 4: Shadow sprint (OJT) | PM L0→L1 | OJT theo cặp mentor | Song song với sprint thật |
| **T2** | T3 | Khóa 5: Hybrid Resource Allocation | PM ≥ L1 | Workshop | 2 buổi × 2h |
| **T2** | T4 | Khóa 6: Token Budget Forecast (Drill 2) | PM ≥ L1 | Workshop + drill | 1 buổi × 2h |
| **T3** | T1 | L1 Assessment — Check-in progress | PM shadow xong | Mentor review | Sign-off L1 |
| **T3** | T2 | Khóa 7: Quality Gate Enforcement (Drill 5) | PM ≥ L1 | Role-play | 1 buổi × 2h |
| **T3** | T3 | Khóa 8: ROI Calculation (Drill 1) | PM ≥ L1 | Practice + review | 1 buổi × 2h |
| **T3** | T4 | Retrospective Sprint 1: Review AI metrics + lessons | PM ≥ L1 | Team meeting (15') | Dành 15' trong retro thường |
| **T4** | T1 | L2 Assessment — confirm danh sách | PM ≥ L2 | Manager review | |
| **T4** | T2 | Khóa 9: Stakeholder Education (Drill 4) | PM ≥ L2 | Workshop | 2 buổi × 2h |
| **T4** | T3 | Khóa 10: Risk Management AI Project (Drill 3) | PM ≥ L2 | Workshop + drill | 2 buổi × 2h |
| **T4** | T4 | PM solo project nhỏ (OJT L2) tiếp tục | PM ≥ L2 | Live project | Với mentor support |
| **T5** | T1 | Khóa 11: Anti-pattern Workshop | PM ≥ L2 | Discussion + case study | 1 buổi × 2h |
| **T5** | T2-T4 | OJT: Lead project medium (hướng tới L3) | PM ≥ L2 đủ điều kiện | Live project | PM Lead L4+ giám sát |
| **T6** | T1-T2 | Tiếp tục lead project / OJT — 30-Day Rollout | PM đang trong project | Live | Track 3 KPI chính |
| **T6** | T3 | Review tổng kết 6 tháng — Showcase results | Toàn PM | Seminar | So sánh T0 vs T6 |
| **T6** | T4 | L3 Assessment chính thức | PM đủ điều kiện | PM Lead đánh giá | Badge L3 |

---

## Anti-patterns cần tránh trong quá trình đào tạo và vận hành

| # | Anti-pattern | Triệu chứng | Cách phòng |
|---|---|---|---|
| 1 | **Bypass Quality Gate vì deadline** | "Lần này thôi, lần sau bù" | Áp dụng Emergency Bypass đúng quy trình; never silent skip |
| 2 | **Treat AI as unlimited capacity** | Token cost > budget 50%, project lỗ | Track weekly; alert ở 80% budget |
| 3 | **So sánh velocity AI với baseline truyền thống** | "Velocity tăng 3×, sao Lead Time vẫn vậy?" | Track Quality Velocity — không velocity thô |
| 4 | **Promise fixed-price không buffer cho token cost** | Token spike → mất margin | Buffer 20-30% trong contract; clause cho LLM pricing change |
| 5 | **Micromanage prompts của Dev** | Dev frustrated, không tự chủ | PM track outcome; Dev tự chủ prompt; chỉ intervene khi outcome lệch |
| 6 | **Skip retrospective về AI usage** | Same mistake lặp lại sprint sau | Mỗi retro dành 15' review AI metrics + lessons |
| 7 | **Không collect baseline trước rollout** | Không thể prove ROI cho leadership | Tuần 0 mandatory baseline |
| 8 | **Treat Kari như chi phí tách rời** | Cut Kari subscription để giảm cost | Kari là enabler; ROI dài hạn — cut = mất compound effect |
| 9 | **Không train PM team về Token Economics** | Sprint 3 phát hiện budget thiếu, không biết tại sao | Training PM về token tracking từ tuần đầu |
| 10 | **Báo cáo AI metrics quá technical** | Stakeholder không hiểu, mất buy-in | Translate sang business metrics (Lead Time, Defect Density, Cost per feature) |

---

## Gợi ý bài tập thực hành (5 Drills)

> ⚠️ **Đây là gợi ý drill** để team tham khảo — không phải bài tập bắt buộc theo mẫu duy nhất. Mỗi team có thể design drill phù hợp với context dự án và level học viên.

### Drill 1: ROI Calculation *(áp dụng ở L1→L2)*
**Đầu vào:** 1 feature 2 sprint, team 5 người, baseline traditional.  
**Yêu cầu:** Tính effort traditional vs AI-enhanced; token cost; net savings; ROI %. Kết quả phải **defendable trước Tech Lead**.

### Drill 2: Token Budget Forecast *(áp dụng ở L1→L2)*
**Đầu vào:** Token consumption 3 sprint gần nhất + plan 4 feature mới.  
**Yêu cầu:** Forecast tháng tới với confidence interval (best/expected/worst case). Mục tiêu: forecast nằm trong **±20% actual**.

### Drill 3: Risk Register cho New Project *(áp dụng ở L2→L3)*
**Đầu vào:** 1 project brief mới.  
**Yêu cầu:** Tạo Risk Register với 15 risks (trong đó 5 AI-specific), prioritize T1-T4, gán owner + mitigation cho top T1.

### Drill 4: Stakeholder Status Report *(áp dụng ở L2→L3)*
**Đầu vào:** Sprint actual data (KPIs).  
**Yêu cầu:** Viết Status Report **1 trang** cho stakeholder non-technical; record **video walkthrough 5 phút**.

### Drill 5: Quality Gate Role-play *(áp dụng ở L1→L2)*
**Đầu vào:** 3 scenario — (1) deadline pressure, (2) score dưới ngưỡng 8.0, (3) khách hàng push back.  
**Yêu cầu:** Role-play với peer; mentor đánh giá **tính kiên định + empathy + giải pháp thay thế**.

---

## Tài liệu tự học

### Sách (foundation)

| Sách | Tác giả | Vì sao đọc | Giai đoạn |
|---|---|---|---|
| **Inspired** | Marty Cagan | PM mindset, outcome > output | L1→L2 |
| **Accelerate** | Forsgren, Humble, Kim | DORA metrics, evidence-based PM | L1→L2 |
| **The Phoenix Project** | Gene Kim | DevOps & flow management | L0→L1 |
| **The Lean Startup** | Eric Ries | Hypothesis-driven development | L2→L3 |
| **Sprint** | Jake Knapp | 5-day design sprint pattern | L2→L3 |
| **Crucial Conversations** | Patterson et al. | Skill khi từ chối Quality Gate bypass | L2→L3 |

### Khóa học & Cộng đồng

| Khóa / Nguồn | Mục tiêu | Giai đoạn |
|---|---|---|
| **DORA Assessment** (Google Cloud) | Đo & cải thiện DORA metrics theo chu kỳ | L3+ |
| **Coursera — Project Management Principles** (UC Irvine) | PM foundation | L0→L1 |
| **Certified ScrumMaster (CSM)** hoặc **PSM I** | Agile/Scrum certification | L1→L2 |
| **Prosci Change Management** | Quản lý transition sang Agentic SDLC | L2→L3 |
| **Mind the Product** community | Cập nhật PM trends | Liên tục |
| **Vietnamese:** Facebook group "Project Manager Vietnam" | Peer learning trong nước | Liên tục |

### Tài liệu nội bộ

- Lessons Learned hub về PM gotcha (Chapter 5.2 §5)
- PM Skill library (Kari Hub)
- Workflow chi tiết & Quality Gate: Chapter 4 + Chapter 7.2
- 30-Day Rollout + KPI definitions: Chapter 6.1
- Risk Management: Chapter 4.3
- Cost benchmarks (Token economics): Chapter 9.1 §10

---

## Hướng Phát Triển Sự Nghiệp sau L5

| Hướng | Mô tả | Yêu cầu thêm |
|---|---|---|
| **VP Engineering / Engineering Director** | Quản lý SBU, định hướng kỹ thuật | L5 ≥ 2 năm; MBA optional |
| **Chief AI Operations Officer** | Vận hành Agentic SDLC ở scale công ty | Deep Kari + DevOps + Finance literacy |
| **Senior Program Manager (multi-SBU)** | Chương trình đa SBU | ≥ 5 dự án L5 ROI dương + leadership |
| **Customer Success / Account Director** | Pivot sang side khách hàng | Strong stakeholder skill; ngành dọc expertise |

---

## Checklist Tổng Hợp

- [ ] **Bước 3 — Ưu tiên làm đầu tiên:** Thu survey + collect KPI baseline T0
- [ ] Điền số liệu thực tế vào bảng tỷ lệ level T0 (Bước 4)
- [ ] Xác nhận giảng viên / mentor cho từng khóa
- [ ] Confirm lịch cụ thể không xung đột dự án (Bước 5)
- [ ] Thiết lập cơ chế theo dõi: token dashboard, Quality Velocity, Defect Density Trend
- [ ] Kick-off với toàn bộ PM + set expectation rõ ràng về Agentic SDLC

---

*Tài liệu này là template — cần điền số liệu thực tế sau khi có kết quả survey nhân sự.*  
*Nguồn tham chiếu chính: `3.1.2_PM_Roadmap.md`*  
*Cập nhật lần cuối: 2026-06-22*
