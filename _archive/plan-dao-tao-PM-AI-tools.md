# Plan Đào Tạo PM Dùng AI Tool Thành Thạo

> ⚠️ **BẢN LƯU TRỮ (superseded)** — Bản này đã được gộp vào bản chính thức `../plan-dao-tao-PM-AI-integrated.md`. Giữ lại để tham khảo, không dùng làm plan chính. Nội dung thiên về kỹ năng dùng tool.
>
> **Phạm vi:** PM cá nhân ứng dụng AI tool vào công việc hàng ngày  
> **Timeline:** 6 tháng  
> **Framework:** L1 → L5 theo `level-AI-PM-tools.md`  
> **Mục tiêu cốt lõi:** ≥ 50% PM đạt L3 sau 6 tháng — tự chủ hoàn toàn với AI tools và có workflow tiết kiệm ≥ 30% thời gian

---

## Bước 1: Khung Năng Lực (tóm tắt)

> Chi tiết đầy đủ: xem `level-AI-PM-tools.md`

| Level | Mô tả ngắn | Milestone |
|---|---|---|
| **L1 Apprentice** 🌱 | Dùng AI với prompt có sẵn; tạo meeting notes, email | Onboarding xong + tự chạy 5 prompt không cần hỗ trợ |
| **L2 Practitioner** 🥉 | Tự viết prompt; tạo User Story, PRD, Status Report bằng AI | Prompt library cá nhân ≥ 10 prompt; PRD draft < 30 phút |
| **L3 Proficient** 🥈 | Workflow AI tiết kiệm ≥ 30% thời gian; chuẩn hóa template cho team | ≥ 1 template team đang dùng; hướng dẫn được PM L2 |
| **L4 Expert** 🥇 | Custom GPT/Agent; automation workflow; train team | ≥ 1 custom tool đang chạy thực tế; đã train ≥ 3 PM |
| **L5 Master** 💎 | AI tool strategy cấp tổ chức; thought leadership | AI strategy được leadership approve |

---

## Bước 2: Lộ Trình Đào Tạo Theo Transition

### L0 → L1 (AI Onboarding) — ~2 tuần

**Mục tiêu:** PM biết tool nào đang có, dùng được với prompt sẵn, tự tạo output cơ bản.

| # | Khóa học | Nội dung | Hình thức | Thời lượng | Bắt buộc? |
|---|---|---|---|---|---|
| 1 | **Giới thiệu AI Tools cho PM** | Landscape tool: ChatGPT, Claude, Notion AI, Jira AI, Copilot; cái nào dùng cho việc gì; giới hạn cần biết | Internal training | 1 buổi × 2h | Bắt buộc |
| 2 | **Thực hành với Prompt Library** | Chạy thử ≥ 5 prompt có sẵn từ thư viện team; so sánh output các tool; cách copy-paste và chỉnh sửa output | Workshop thực hành | 1 buổi × 2h | Bắt buộc |
| 3 | **AI cho task cơ bản** | Thực hành: tóm tắt meeting transcript, viết email từ bullet points, tạo agenda họp | Self-practice | 3h | Bắt buộc |

**Milestone L1:** Tự chạy 5 prompt từ thư viện + tạo được 1 meeting notes hoàn chỉnh từ transcript thô

---

### L1 → L2 (AI cho PM Tasks tiêu chuẩn) — ~4 tuần

**Mục tiêu:** PM tự viết prompt cho các task PM hàng ngày, có prompt library cá nhân.

| # | Khóa học | Nội dung | Hình thức | Thời lượng | Bắt buộc? |
|---|---|---|---|---|---|
| 4 | **Prompt Engineering cơ bản cho PM** | Cấu trúc prompt hiệu quả: Role + Context + Yêu cầu + Format + Ví dụ; tại sao context quan trọng; cách refine khi output sai | Internal workshop | 1 buổi × 2h | Bắt buộc |
| 5 | **AI-assisted User Story & Acceptance Criteria** | Viết User Story từ requirement thô; generate AC từ User Story; review và chỉnh output AI | Workshop + drill | 1 buổi × 2h | Bắt buộc |
| 6 | **AI-assisted PRD** | Tạo PRD draft từ brief; structure PRD với AI; điền section chi tiết; review checklist | Workshop + drill | 1 buổi × 2h | Bắt buộc |
| 7 | **AI-assisted Status Report & Stakeholder Update** | Viết status report non-technical từ data sprint; tạo executive summary; generate slide talking points | Workshop + drill | 1 buổi × 2h | Bắt buộc |
| 8 | **AI-assisted Token Tracking** | Dùng AI đọc và tóm tắt token dashboard; nhận diện task/agent đang dùng nhiều token hơn dự tính; phân biệt spike bình thường vs spike đáng lo; viết weekly token summary để PM chủ động dự đoán rủi ro budget trước khi vỡ | Workshop + drill | 1 buổi × 2h | Bắt buộc |
| 9 | **Xây dựng Prompt Library cá nhân** | Template cách lưu prompt; metadata (task, tool, khi nào dùng); peer review prompt library | Self-practice + peer review | 2h | Bắt buộc |
| 10 | **Thực hành tự do** | Áp dụng AI vào task thực tế của sprint đang chạy; ghi lại thời gian tiết kiệm và token weekly | OJT | 2 tuần | Bắt buộc |

**Milestone L2:** Tự viết prompt cho ≥ 5 task PM khác nhau + Prompt library ≥ 10 prompt + PRD draft trong < 30 phút + nhận diện được spike token và giải thích nguyên nhân

---

### L2 → L3 (Workflow AI & Chuẩn hóa) — ~6 tuần

**Mục tiêu:** Tích hợp AI vào toàn bộ quy trình PM, tối ưu workflow, bắt đầu chuẩn hóa cho team.

| # | Khóa học | Nội dung | Hình thức | Thời lượng | Bắt buộc? |
|---|---|---|---|---|---|
| 10 | **Prompt nâng cao** | Chain-of-thought prompting; few-shot examples; khi nào không nên dùng AI; nhận biết hallucination trong output PM | Internal workshop | 1 buổi × 2h | Bắt buộc |
| 11 | **AI Workflow cho Sprint Cycle** | Tích hợp AI vào Sprint Planning (breakdown task, estimate, risk check), Backlog Refinement (refine story, priority scoring), Retrospective (pattern analysis từ feedback) | Workshop + drill | 2 buổi × 2h | Bắt buộc |
| 12 | **AI-assisted Data Analysis & Insight** | Dùng AI phân tích: survey feedback, NPS data, sprint metrics; từ raw data → actionable insight → recommendation. **Token analysis nâng cao:** so sánh token/feature qua các sprint, nhận diện pattern feature nào hay overrun, dùng AI forecast budget 1–2 sprint tới từ baseline | Workshop + drill | 2 buổi × 2h | Bắt buộc |
| 13 | **Chọn đúng tool cho đúng task** | So sánh ChatGPT vs Claude vs Gemini cho các use case PM; Notion AI vs standalone tool; Jira AI cho backlog management | Discussion + hands-on | 1 buổi × 2h | Bắt buộc |
| 14 | **Chuẩn hóa và chia sẻ template** | Xây dựng prompt template chuẩn cho team; viết hướng dẫn sử dụng (when to use, input cần có, output expect); peer workshop chia sẻ best practice | Workshop | 1 buổi × 2h | Bắt buộc |
| 15 | **OJT: Áp dụng toàn bộ workflow** | Dùng AI toàn bộ sprint cycle; đo thời gian tiết kiệm; ghi chép điều gì hoạt động, điều gì không | OJT | 3 tuần | Bắt buộc |

**Milestone L3:** Workflow AI tiết kiệm ≥ 30% thời gian (có data đo) + ≥ 1 template team adopt + hướng dẫn được ≥ 1 PM L2

---

### L3 → L4 (Custom Tool & Training) — tham khảo, ngoài 6 tháng

| # | Khóa học | Hình thức | Thời lượng |
|---|---|---|---|
| 16 | **Custom GPT cho PM Workflow** — Xây GPT riêng cho User Story generation, Risk Assessment, Sprint Report | Workshop | 2 buổi |
| 17 | **AI Automation với Zapier / Make** — Kết nối Jira + AI để auto-generate summary; Slack + AI cho standup digest | Advanced workshop | 2 buổi |
| 18 | **AI Tool Evaluation Framework** — Tiêu chí đánh giá tool mới; pilot process; security checklist trước khi adopt | Internal | 1 buổi |
| 19 | **Thiết kế Training Curriculum** — Xây dựng khóa học AI tools cho PM junior; coaching framework | Workshop | 1 buổi |

---

### L4 → L5 (Strategy & Thought Leadership) — tham khảo

| # | Khóa học | Hình thức | Thời lượng |
|---|---|---|---|
| 20 | **AI Tool Strategy cho SBU** — Roadmap adoption, budget planning, governance framework | Strategic workshop | 2 buổi |
| 21 | **ROI Measurement cho AI Tool Adoption** — Framework đo ROI ở cấp tổ chức; cách present cho leadership | Internal | 1 buổi |
| 22 | **Thought Leadership** — Viết article, prepare talk về AI tools cho PM; build personal brand | Mentoring | Ongoing |

---

## Bước 3: Survey Đánh Giá Level Hiện Tại

Gửi survey tự đánh giá cho từng PM trước khi bắt đầu chương trình.

**Các câu hỏi đánh giá chính:**

| Câu hỏi | Phân biệt level |
|---|---|
| Bạn có thể tự viết prompt không cần template có sẵn không? | L1 vs L2 |
| Bạn đã dùng AI tạo PRD hoặc User Story chưa? | L1 vs L2 |
| Bạn có prompt library cá nhân không? Bao nhiêu prompt? | L2 vs L3 |
| AI có trong workflow hàng ngày của bạn không (không chỉ dùng khi "nhớ ra")? | L2 vs L3 |
| Bạn đã chia sẻ/hướng dẫn người khác dùng AI chưa? | L3 vs L4 |
| Bạn đã xây custom tool hoặc automation với AI chưa? | L3 vs L4 |

### Bảng mapping nhân sự (điền sau khi thu survey)

| STT | Họ tên | Level tự đánh giá | Level manager xác nhận | Gap chính | Ưu tiên | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| ... | | | | | | |

---

## Bước 4: Mục Tiêu Tỷ Lệ Level (6 tháng)

> Template cho team 10 PM — điều chỉnh theo thực tế sau survey.

| Thời điểm | L0 | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|---|
| **T0 — Hiện tại** | _ | _ | _ | _ | _ | _ |
| **T+2 tháng** | 0 | 40% | 50% | 10% | 0 | 0 |
| **T+4 tháng** | 0 | 10% | 50% | 35% | 5% | 0 |
| **T+6 tháng** | 0 | 0 | 30% | 55% | 15% | 0 |

**Mục tiêu cốt lõi 6 tháng:** ≥ 50% PM đạt L3 — AI tool là một phần tự nhiên trong workflow hàng ngày, không phải dùng khi "nhớ ra".

**3 KPI đo lường tiến độ:**
1. **Thời gian tiết kiệm/tuần** — PM tự đo và báo cáo (target L3: ≥ 30%)
2. **Prompt Library size** — số prompt tái sử dụng được (target L2: ≥ 10; L3: có chia sẻ team)
3. **Adoption rate** — % task PM hàng ngày có AI hỗ trợ (target L3: ≥ 60% task tiêu chuẩn)

---

### Kế hoạch từng khóa học (6 tháng)

| # | Tên khóa | Đối tượng | Phụ trách | Tháng | Số học viên | Đánh giá |
|---|---|---|---|---|---|---|
| 1 | Giới thiệu AI Tools cho PM | PM L0 | PM L4+ nội bộ | Tháng 1 | Toàn bộ PM | Checklist tool biết dùng |
| 2 | Thực hành với Prompt Library | PM L0 | PM L4+ nội bộ | Tháng 1 | Toàn bộ PM | 5 prompt chạy được |
| 3 | AI cho task cơ bản | PM L0 | Self-practice | Tháng 1 | Toàn bộ PM | 1 meeting notes hoàn chỉnh |
| 4 | Prompt Engineering cơ bản | PM ≥ L1 | PM L4+ | Tháng 2 | PM qua L1 | Viết được prompt chuẩn cấu trúc |
| 5 | AI-assisted User Story & AC | PM ≥ L1 | PM L4+ | Tháng 2 | PM qua L1 | Drill: 5 User Story từ brief |
| 6 | AI-assisted PRD | PM ≥ L1 | PM L4+ | Tháng 2 | PM qua L1 | PRD draft < 30 phút |
| 7 | AI-assisted Status Report | PM ≥ L1 | PM L4+ | Tháng 3 | PM qua L1 | Status report non-technical pass |
| 8 | Xây dựng Prompt Library cá nhân | PM ≥ L1 | Peer review | Tháng 3 | PM qua L1 | ≥ 10 prompt có metadata |
| 9 | OJT: Áp dụng L2 vào thực tế | PM ≥ L1 | Mentor PM L3+ | Tháng 3-4 | PM qua L1 | L2 sign-off |
| 10 | Prompt nâng cao | PM ≥ L2 | PM L4+ | Tháng 4 | PM đạt L2 | Drill chain-of-thought |
| 11 | AI Workflow cho Sprint Cycle | PM ≥ L2 | PM L4+ | Tháng 4 | PM đạt L2 | Workflow map có AI |
| 12 | AI Data Analysis & Insight | PM ≥ L2 | PM L4+ | Tháng 5 | PM đạt L2 | Drill: raw data → recommendation |
| 13 | Chọn đúng tool cho đúng task | PM ≥ L2 | PM L4+ | Tháng 5 | PM đạt L2 | Tool selection matrix |
| 14 | Chuẩn hóa & chia sẻ template | PM ≥ L2 | PM L4+ | Tháng 5 | PM đạt L2 | ≥ 1 template team adopt |
| 15 | OJT: Workflow AI đầy đủ | PM ≥ L2 | Mentor PM L3+ | Tháng 5-6 | PM đạt L2 | L3 sign-off |
| 16 | Review tổng kết 6 tháng | Toàn PM | PM Lead | Tháng 6 | Tất cả | L3 Assessment + showcase |

---

## Bước 5: Lịch Đào Tạo Tổng Thể (6 tháng)

| Tháng | Tuần | Hoạt động | Đối tượng | Hình thức | Ghi chú |
|---|---|---|---|---|---|
| **T1** | T1 | Thu survey đánh giá level + baseline (thời gian làm task hiện tại) | Toàn PM | Async | Bắt buộc — cần baseline để đo ROI |
| **T1** | T1 | Kick-off: tại sao AI tools quan trọng với PM | Toàn PM | Seminar 1h | Demo live, không slide lý thuyết |
| **T1** | T2 | Khóa 1: Giới thiệu AI Tools | Toàn PM | Workshop 2h | Hands-on ngay trong buổi |
| **T1** | T3 | Khóa 2: Thực hành Prompt Library | Toàn PM | Workshop 2h | Mỗi người chạy ≥ 5 prompt |
| **T1** | T4 | Khóa 3: AI task cơ bản (self-practice) | Toàn PM | Self-practice | Deadline: nộp 1 meeting notes cuối T1 |
| **T2** | T1 | L1 Assessment | Toàn PM | Manager check | Sign-off L1 |
| **T2** | T2 | Khóa 4: Prompt Engineering cơ bản | PM ≥ L1 | Workshop 2h | |
| **T2** | T3 | Khóa 5: AI User Story & AC | PM ≥ L1 | Workshop + drill | |
| **T2** | T4 | Khóa 6: AI PRD | PM ≥ L1 | Workshop + drill | |
| **T3** | T1 | Khóa 7: AI Status Report | PM ≥ L1 | Workshop + drill | |
| **T3** | T2 | Khóa 8: Xây dựng Prompt Library | PM ≥ L1 | Peer review | |
| **T3** | T3-T4 | OJT: Áp dụng vào sprint thực tế | PM ≥ L1 | Live + mentor | Track thời gian tiết kiệm |
| **T4** | T1 | L2 Assessment | PM qua OJT | Manager + peer | Prompt library review + demo |
| **T4** | T2 | Khóa 10: Prompt nâng cao | PM ≥ L2 | Workshop 2h | |
| **T4** | T3-T4 | Khóa 11: AI Workflow cho Sprint Cycle | PM ≥ L2 | Workshop 2 buổi | |
| **T5** | T1 | Khóa 12: AI Data Analysis | PM ≥ L2 | Workshop + drill | |
| **T5** | T2 | Khóa 13: Chọn đúng tool | PM ≥ L2 | Discussion + hands-on | |
| **T5** | T3 | Khóa 14: Chuẩn hóa template | PM ≥ L2 | Workshop + peer share | |
| **T5** | T4 — T6 T2 | OJT: Workflow AI đầy đủ | PM ≥ L2 | Live + mentor | Đo: % task dùng AI, thời gian tiết kiệm |
| **T6** | T3 | Review tổng kết 6 tháng — Showcase | Toàn PM | Seminar | Mỗi PM share 1 workflow/template hay nhất |
| **T6** | T4 | L3 Assessment chính thức | PM đủ điều kiện | PM Lead đánh giá | Badge L3 |

---

## Anti-patterns cần tránh

| Anti-pattern | Triệu chứng | Cách phòng |
|---|---|---|
| **Học lý thuyết, không thực hành ngay** | PM biết prompt structure nhưng không dùng trong công việc thật | Mỗi khóa có drill áp dụng vào task thực tế của sprint đang chạy |
| **Dùng AI cho mọi thứ** | Mất nhiều thời gian hơn vì cố dùng AI cho task không phù hợp | Dạy rõ khi nào **không** nên dùng AI ngay từ L1 |
| **Copy-paste output AI không review** | Document chứa thông tin sai, hallucination lọt vào PRD/User Story | Quy tắc: AI output là draft — luôn phải human review trước khi dùng |
| **Không lưu prompt hay dùng** | Mỗi lần làm task phải viết lại prompt từ đầu | Xây dựng prompt library từ L2, review định kỳ |
| **Không đo thời gian tiết kiệm** | Không biết AI có thực sự giúp ích không | Baseline T0 bắt buộc; track thời gian mỗi tháng |
| **PM L4+ không chia sẻ** | Team mỗi người tự mày mò, kiến thức không lan tỏa | Build sharing culture: monthly "AI tips" session 30 phút |
| **Dùng AI nhưng giấu khách hàng** | Khách biết được, mất trust | Có policy rõ ràng: AI hỗ trợ gì, human chịu trách nhiệm gì |

---

## Tài liệu tự học

### Để học Prompt Engineering
- **Anthropic Prompt Engineering Guide** — docs.anthropic.com (free)
- **OpenAI Prompt Engineering** — platform.openai.com/docs (free)
- **Prompting Guide** — promptingguide.ai (free, nhiều ví dụ thực tế)

### Để học AI Workflow & Automation
- **Zapier Learn** — zapier.com/learn (free)
- **Make Academy** — academy.make.com (free)

### Để hiểu sâu hơn về AI cho PM
- **"The AI-Powered Product Manager"** — Reid Hoffman + GPT-4 (đọc với mindset critical)
- **Lenny's Newsletter** — lennysletters.com (nhiều case study AI cho PM thực tế)
- **Mind the Product** — mindtheproduct.com (community + articles)

---

## Checklist Tổng Hợp

- [ ] Thu survey + đo baseline thời gian task T0 — **làm đầu tiên**
- [ ] Xác nhận PM L4+ làm trainer và mentor
- [ ] Xây dựng / tổng hợp Prompt Library seed (≥ 20 prompt) cho team dùng từ ngày 1
- [ ] Setup tool access: confirm team có account ChatGPT/Claude/Notion AI
- [ ] Confirm data security policy: task nào, data nào được/không được đưa vào AI tool
- [ ] Kick-off với toàn bộ PM — demo live, không slide thuần lý thuyết
- [ ] Setup cơ chế track: thời gian tiết kiệm, prompt library size, adoption rate

---

*Tài liệu này là template — cần điền số liệu thực tế sau khi có kết quả survey nhân sự.*  
*Cập nhật lần cuối: 2026-06-22*
