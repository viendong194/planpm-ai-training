# Survey Đánh Giá Level Dùng AI Tool — Project Manager

> **Nguồn tham chiếu:** `plan-dao-tao-PM-AI-integrated.md` (bản chính thức) + `level-AI-PM-tools.md`
> **Mục đích:** Xác định PM đang ở level nào về (1) **mindset dùng AI** và (2) **dùng AI tool** để quản trị dự án tốt hơn.
> **Cách điền:** Với mỗi câu, chọn **1 đáp án** mô tả đúng nhất tình trạng hiện tại. Mỗi đáp án có ví dụ minh họa cụ thể — chọn theo việc bạn **đã thực sự làm**, không phải điều bạn nghĩ mình "có thể làm được".

---

## Thông tin cá nhân

| | |
|---|---|
| **Họ tên** | |
| **Dự án hiện tại** | |
| **Ngày điền** | |

### Baseline hiện tại (để so sánh sau 6 tháng — điền số gần đúng)

| Chỉ số | Hiện tại |
|---|---|
| Thời gian trung bình để viết **1 PRD / tài liệu yêu cầu** | ______ giờ |
| Thời gian trung bình để viết **1 status report** cho stakeholder | ______ phút/giờ |
| Ước tính **% công việc PM mỗi tuần hiện có AI hỗ trợ** | ______ % |

---

# PHẦN A — Nền tảng dùng AI

## Câu 1 — Làm quen công cụ AI

*Bạn đã dùng công cụ AI (ChatGPT, Claude, Copilot...) trong công việc như thế nào?*

- **A.** Chưa dùng, hoặc chỉ tò mò thử vài lần không có mục đích công việc cụ thể.
- **B.** Dùng được với prompt/mẫu có sẵn từ thư viện team. *Ví dụ: lấy prompt "tóm tắt meeting" có sẵn, dán transcript vào, sửa lại một chút.*
- **C.** Tự viết prompt cho nhu cầu riêng mà không cần mẫu có sẵn. *Ví dụ: tự gõ "Đóng vai BA, viết 5 user story từ đoạn brief sau, format theo Given-When-Then" mà không cần ai đưa mẫu.*
- **D.** Dùng AI như một bước mặc định trong mọi việc liên quan (không phải "nhớ ra mới dùng"). *Ví dụ: mỗi sáng mở AI để review dashboard token, mỗi cuối sprint tự động dùng AI phân tích retro — thành thói quen.*

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 2 — Cấu trúc viết prompt

*Khi cần AI làm một việc phức tạp (không phải hỏi 1 câu đơn giản), bạn viết prompt như thế nào?*

- **A.** Gõ một câu ngắn, không có ngữ cảnh, nếu sai thì thử lại câu khác. *Ví dụ: "viết PRD giúp tôi" rồi chờ xem AI ra gì.*
- **B.** Biết thêm role + yêu cầu cơ bản nhưng chưa có cấu trúc rõ ràng. *Ví dụ: "Bạn là PM, hãy viết PRD cho tính năng đăng nhập."*
- **C.** Viết đủ cấu trúc Role + Context + Yêu cầu + Format + Ví dụ, và biết refine lại khi output sai. *Ví dụ: "Đóng vai BA. Đây là brief: [...]. Viết PRD gồm 5 mục: Problem, Goal, User Story, AC, Out-of-scope. Format bảng. Nếu thiếu thông tin, hỏi lại tôi trước khi viết."*
- **D.** Dùng kỹ thuật nâng cao: chain-of-thought (yêu cầu AI suy luận từng bước) hoặc few-shot (đưa ví dụ mẫu để AI bắt chước format). *Ví dụ: đưa 2 user story mẫu, yêu cầu AI viết thêm 5 story đúng văn phong đó.*

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

# PHẦN B — Dùng AI cho tác vụ PM

## Câu 3 — Tạo PRD bằng AI

*Bạn đã dùng AI để soạn PRD (Product Requirement Document) chưa?*

- **A.** Chưa từng, vẫn viết tay 100%.
- **B.** Có thử nhưng phải sửa lại gần hết, mất nhiều thời gian hơn viết tay. *Ví dụ: AI ra PRD chung chung, thiếu context dự án, phải viết lại 80%.*
- **C.** Ra được bản PRD draft đầy đủ cấu trúc từ 1 đoạn brief, trong dưới 30 phút, chỉ cần review và chỉnh sửa nhỏ.
- **D.** Có checklist review chuẩn trước khi giao team, và đã dùng cách này cho nhiều dự án khác nhau, biết điều chỉnh cấu trúc PRD theo loại dự án (feature nhỏ / dự án lớn).

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 4 — Tạo User Story & Acceptance Criteria bằng AI

*Bạn dùng AI để viết User Story và AC như thế nào?*

- **A.** Chưa dùng AI cho việc này.
- **B.** Có dùng nhưng chưa biết cách review — copy nguyên output vào Jira mà không kiểm tra kỹ. *Ví dụ: dán nguyên story AI viết, sau đó dev báo thiếu edge case.*
- **C.** Dùng AI generate User Story từ PRD, generate AC từ Story, và tự phát hiện được chỗ AI viết mơ hồ hoặc thiếu edge case trước khi giao team.
- **D.** Có quy trình chuẩn: brief → AI draft → tự review theo checklist riêng → AI refine lần 2 → giao team. Áp dụng nhất quán cho toàn bộ backlog, không chỉ vài story lẻ tẻ.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 5 — Status Report cho Stakeholder

*Bạn dùng AI để viết báo cáo tiến độ cho stakeholder như thế nào?*

- **A.** Chưa dùng, tự viết tay hoàn toàn.
- **B.** Dùng AI viết nháp nhưng vẫn còn thuật ngữ kỹ thuật, stakeholder non-technical đọc không hiểu, phải hỏi lại. *Ví dụ: báo cáo còn ghi "Quality Velocity 12/20, token cost spike 15%" mà không giải thích ý nghĩa.*
- **C.** Dùng AI translate số liệu kỹ thuật (velocity, token cost, defect...) sang business value dễ hiểu (Lead Time giảm, chi phí/feature giảm...), report 1 trang, stakeholder hiểu ngay không cần hỏi thêm.
- **D.** Ngoài report viết, còn dùng AI hỗ trợ chuẩn bị talking points cho các câu hỏi khó từ khách hàng, và có thể present bằng video/slide.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 6 — Theo dõi Token Cost bằng AI

*Bạn dùng AI để theo dõi token cost như thế nào?*

- **A.** Không theo dõi token cost, hoặc để việc này cho Dev/Tech Lead.
- **B.** Có đọc dashboard nhưng không phân tích, chỉ nhìn con số tổng.
- **C.** Dùng AI tóm tắt dashboard, nhận diện được task/agent nào đang dùng nhiều token hơn dự tính, phân biệt được spike bình thường và spike đáng lo.
- **D.** Dùng AI để so sánh token/feature qua nhiều sprint, phát hiện pattern (feature nào hay bị overrun), và tự forecast budget 1-2 sprint tới từ baseline.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 7 — Prompt Library cá nhân

*Bạn có lưu lại prompt để dùng lại không?*

- **A.** Không lưu, mỗi lần cần lại gõ lại từ đầu.
- **B.** Có lưu vài prompt rời rạc (note, chat history) nhưng không có tổ chức, khó tìm lại.
- **C.** Có thư viện prompt cá nhân ≥ 10 prompt, có ghi chú (task nào, dùng tool gì, khi nào dùng), tìm lại dễ dàng.
- **D.** Ngoài thư viện cá nhân, đã chia sẻ/đóng góp prompt cho team dùng chung, có ít nhất 1 template được team khác áp dụng thực tế.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 8 — AI trong Workflow Sprint hàng ngày

*AI có mặt trong công việc sprint của bạn ở mức nào?*

- **A.** Chỉ dùng AI khi "chợt nhớ ra", không phải việc thường xuyên.
- **B.** Dùng AI cho 1-2 việc cố định (vd: luôn dùng AI viết status report) nhưng chưa mở rộng ra các bước khác.
- **C.** AI có mặt xuyên suốt sprint cycle: hỗ trợ Sprint Planning (breakdown task, estimate), Backlog Refinement (refine story), Retrospective (phân tích feedback).
- **D.** Đã đo được: workflow có AI tiết kiệm ≥ 30% thời gian so với làm tay (có số liệu cụ thể, không phải ước chừng).

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 9 — Phân tích dữ liệu & rút insight bằng AI

*Bạn dùng AI để phân tích dữ liệu (feedback, metrics, sprint data) như thế nào?*

- **A.** Chưa dùng AI cho việc phân tích, chỉ đọc số liệu thô.
- **B.** Dùng AI tóm tắt dữ liệu nhưng dừng ở việc liệt kê lại, chưa có insight hay đề xuất hành động.
- **C.** Dùng AI đi từ raw data (feedback khảo sát, NPS, sprint metrics) ra được insight cụ thể và đề xuất hành động rõ ràng.
- **D.** Kết hợp phân tích insight với forecast (vd: dự đoán rủi ro token budget sprint tới dựa trên pattern quá khứ), dùng kết quả để điều chỉnh kế hoạch trước khi vấn đề xảy ra.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 10 — Chọn đúng tool cho đúng việc

*Bạn có phân biệt được nên dùng tool AI nào cho việc gì không?*

- **A.** Chỉ biết 1 tool, dùng cho mọi việc bất kể phù hợp hay không.
- **B.** Biết vài tool khác nhau (ChatGPT, Claude, Notion AI, Jira AI...) nhưng chọn theo thói quen, chưa so sánh rõ ưu nhược điểm.
- **C.** Biết so sánh và chọn đúng tool theo use case cụ thể. *Ví dụ: dùng Jira AI cho backlog vì tích hợp sẵn dữ liệu; dùng Claude/ChatGPT cho viết PRD vì cần ngữ cảnh dài và tùy biến prompt.*
- **D.** Từng tham gia đánh giá/thử nghiệm (pilot) tool mới trước khi đề xuất cho team, có tiêu chí đánh giá rõ ràng (bảo mật, chi phí, độ chính xác).

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

# PHẦN C — Mindset & Phán đoán khi dùng AI

> Phần này đánh giá **tư duy dùng AI đúng cách**, không chỉ thao tác. Một PM giỏi AI phải biết khi nào KHÔNG nên dùng, và luôn chịu trách nhiệm cuối cùng với output.

## Câu 11 — Biết khi nào KHÔNG nên dùng AI

*Bạn có phân biệt được việc nào nên và không nên giao cho AI không?*

- **A.** Nghĩ AI dùng được cho gần như mọi việc, cứ thử là được.
- **B.** Mơ hồ cảm thấy có việc AI không hợp, nhưng chưa rõ ranh giới, thường vẫn dùng rồi mới biết. *Ví dụ: ép AI ra quyết định thay mình rồi mới thấy không ổn.*
- **C.** Xác định rõ loại việc không nên giao AI và chủ động không dùng. *Ví dụ: quyết định nhạy cảm về nhân sự/khách hàng, số liệu cần chính xác tuyệt đối chưa kiểm chứng được, cam kết pháp lý — những việc này tự làm/tự chịu trách nhiệm, AI chỉ tham khảo.*
- **D.** Hướng dẫn được người khác phân biệt task nên/không nên dùng AI, và giải thích được lý do (rủi ro, chi phí, độ tin cậy) trong từng trường hợp.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 12 — Review output & trách nhiệm với hallucination

*Bạn xử lý kết quả AI đưa ra như thế nào?*

- **A.** Tin tưởng và dùng thẳng output AI, ít khi kiểm tra lại. *Ví dụ: copy nguyên số liệu AI đưa vào báo cáo gửi khách.*
- **B.** Có đọc lại nhưng chủ yếu kiểm tra câu chữ, không đối chiếu số liệu/nguồn — dễ để lọt thông tin AI bịa ra (hallucination).
- **C.** Luôn review, đối chiếu số liệu và logic với nguồn thật, sửa chỗ AI bịa trước khi dùng; hiểu rõ **con người chịu trách nhiệm cuối cùng**, không đổ lỗi cho AI.
- **D.** Có checklist/quy trình verify chuẩn cho output AI (nhất là số liệu, cam kết với khách), và hướng dẫn team cùng áp dụng để tránh hallucination lọt ra ngoài.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

# PHẦN D — Bảo mật & Tuân thủ

## Câu 13 — Bảo mật dữ liệu khi dùng AI

*Bạn kiểm soát dữ liệu đưa vào công cụ AI như thế nào?*

- **A.** Chưa nghĩ tới rủi ro này — đưa mọi thứ vào AI kể cả spec, dữ liệu khách hàng, source code nhạy cảm.
- **B.** Biết là có rủi ro bảo mật nhưng chưa rõ ranh giới dữ liệu nào được/không được đưa vào.
- **C.** Phân loại được và tuân thủ: biết dữ liệu nào KHÔNG được đưa vào tool AI công cộng (PII, thông tin NDA, source code/khóa bí mật), chỉ dùng tool/kênh được công ty cho phép cho dữ liệu nhạy cảm.
- **D.** Tham gia xây dựng hoặc phổ biến policy về acceptable use / phân loại dữ liệu cho team, và nhắc/kiểm tra để đồng nghiệp tuân thủ.

→ A = **cảnh báo, cần đào tạo ngay** · B = L1 · C = L2 · D = L3+

---

# PHẦN E — Kết nối, Skill, Tự động hóa

## Câu 14 — Kết nối AI với dữ liệu/công cụ khác (MCP)

*Bạn có dùng AI kết nối trực tiếp với công cụ khác (Jira, Backlog, Slack, Notion...) qua MCP/connector để lấy hoặc cập nhật dữ liệu, thay vì copy-paste thủ công không?*

- **A.** Chưa biết MCP/connector là gì — luôn copy-paste dữ liệu thủ công vào AI.
- **B.** Biết khái niệm MCP/connector, nghe đồng nghiệp hoặc admin nhắc tới, nhưng chưa tự dùng.
- **C.** Đã tự dùng AI kết nối với ít nhất 1 công cụ qua MCP để lấy/cập nhật dữ liệu trực tiếp. *Ví dụ: yêu cầu AI tự đọc issue trong Jira/Backlog qua connector để tổng hợp status, không cần copy tay từng issue.*
- **D.** Kết hợp nhiều MCP/connector trong cùng một quy trình để tự động hóa việc lặp lại. *Ví dụ: AI tự đọc ticket từ Jira, đọc thảo luận từ Slack, rồi ghi báo cáo tổng hợp vào Notion — không cần PM thao tác thủ công ở bước nào.*

→ A = chưa tới L2 · B = L2 · C = L3 · D = L4

---

## Câu 15 — Dùng/tạo Skill (quy trình AI đóng gói sẵn)

*Bạn đã dùng hoặc tự tạo "Skill" — gói hướng dẫn/quy trình AI đóng gói sẵn cho một việc lặp lại (vd: skill tạo báo cáo tuần, skill review PRD theo checklist) — chưa?*

- **A.** Chưa biết khái niệm Skill — mỗi lần làm việc lặp lại vẫn gõ prompt lại từ đầu, không có gì đóng gói sẵn.
- **B.** Có dùng Skill có sẵn (do công ty/đồng nghiệp tạo) cho một vài việc quen thuộc, nhưng chưa tự tạo Skill riêng.
- **C.** Tự tạo được ít nhất 1 Skill cho việc lặp lại của riêng mình. *Ví dụ: skill tự động review Status Report theo checklist chuẩn của team, chạy lại được nhiều lần không cần viết lại hướng dẫn.*
- **D.** Skill do bạn tạo đang được **người khác trong team dùng lại thật**, và bạn có cập nhật/cải tiến Skill dựa trên phản hồi thực tế khi dùng.

→ A = chưa tới L2 · B = L2/L3 · C = L3 · D = L4

---

## Câu 16 — Bộ công cụ SDLC nội bộ (Spec → RAG → BD/DD/SRS → Testcase → Code)

*Công ty có bộ công cụ SDLC dùng AI: đưa spec trao đổi với khách hàng vào storage, dùng RAG phân tích nội dung, tự động tạo BD/DD/SRS, sinh testcase checklist, rồi sinh code. Bạn đã dùng bộ công cụ này ở mức nào?*

- **A.** Chưa từng nghe nói về bộ công cụ này.
- **B.** Có nghe/được giới thiệu, nhưng chưa tự dùng vào dự án thực tế nào.
- **C.** Đã dùng thử trong ít nhất 1 dự án — đưa spec vào storage, để hệ thống RAG phân tích và sinh ra BD/DD/SRS, testcase; nhưng vẫn phải sửa/review khá nhiều trước khi dùng được.
- **D.** Đã dùng thường xuyên trong dự án đang chạy, tự tin chuẩn hóa input (viết spec rõ ràng, tổ chức storage hợp lý) để RAG phân tích ra BD/DD/SRS/testcase chất lượng cao, hạn chế phải sửa lại nhiều; biết đánh giá được chỗ nào code sinh ra cần review kỹ hơn.

→ A = chưa tới L1 · B = L1 · C = L2 · D = L3+

---

## Câu 17 — Custom tool / Automation

*Bạn đã từng xây dựng công cụ AI riêng hoặc automation chưa?*

- **A.** Chưa từng, chỉ dùng tool có sẵn qua giao diện chat thông thường.
- **B.** Có nghe/tìm hiểu về Custom GPT, Zapier, Make... nhưng chưa tự làm.
- **C.** Đã tự xây 1 Custom GPT/Agent hoặc automation đơn giản (vd: tự động tóm tắt Jira + Slack) và đang dùng thật cho công việc.
- **D.** Công cụ/automation do bạn xây đang được **cả team** dùng thực tế (không chỉ riêng bạn), và bạn đã training lại cho người khác cách dùng.

→ A = chưa tới L3 · B = L3 · C = L4 · D = L4+

---

# PHẦN F — Lan tỏa & Chiến lược

## Câu 18 — Xây dựng & chia sẻ template cho team

*Bạn đã đóng góp gì cho việc chuẩn hóa AI trong team chưa?*

- **A.** Chưa từng chia sẻ, chỉ dùng cho việc cá nhân.
- **B.** Có chia sẻ 1-2 prompt cho đồng nghiệp khi họ hỏi, nhưng không chủ động.
- **C.** Chủ động xây dựng prompt template chuẩn kèm hướng dẫn sử dụng (khi nào dùng, input cần gì, output mong đợi), có ít nhất 1 template team đang dùng thật.
- **D.** Đã hướng dẫn/mentor được ít nhất 1 PM khác (level thấp hơn) áp dụng AI vào công việc, và họ áp dụng thành công.

→ A = chưa tới L2 · B = L2 · C = L3 · D = L3+

---

## Câu 19 — Chiến lược AI Tool cấp tổ chức

*Bạn có tham gia vào việc định hướng dùng AI tool ở quy mô lớn hơn nhóm mình không?*

- **A.** Chưa, chỉ quan tâm ở phạm vi công việc cá nhân/dự án mình.
- **B.** Có đóng góp ý kiến khi được hỏi nhưng chưa chủ động đề xuất.
- **C.** Đã chủ động đề xuất roadmap/ngân sách adoption AI tool cho nhóm/phòng ban.
- **D.** Đã xây dựng chiến lược AI tool được lãnh đạo phê duyệt (approve) và đang triển khai ở cấp SBU/công ty; hoặc có bài viết/talk chia sẻ được cộng đồng bên ngoài đón nhận.

→ A = chưa tới L4 · B = L4 · C = L4/L5 · D = L5

---

# PHẦN G — Câu hỏi mở

*Trả lời tự do — giúp manager cá nhân hóa lộ trình đào tạo.*

**1. Khó khăn lớn nhất của bạn khi đưa AI vào công việc PM là gì?**

> _(Điền tự do)_

**2. Kỹ năng hoặc công cụ AI nào bạn muốn học nhất trong 3 tháng tới?**

> _(Điền tự do)_

**3. Bạn đã ứng dụng thành công công cụ AI nào vào công việc PM chưa? Bạn có sẵn sàng chia sẻ/mentor lại cho team không?**

> _(Điền tự do)_

**4. Với bộ công cụ SDLC nội bộ (spec → RAG → BD/DD/SRS → testcase → code), bạn thấy vướng mắc hoặc rủi ro đặc thù gì?**

> _(Điền tự do)_

**5. Bạn muốn học theo hình thức nào? (có thể chọn nhiều)**

☐ Workshop offline  ☐ Online  ☐ Tự học + Q&A  ☐ OJT kèm mentor  ☐ Linh hoạt theo lịch dự án

---

## Cách xác định Level (dành cho manager tổng hợp)

Tham chiếu khung năng lực trong `level-AI-PM-tools.md`. **Nguyên tắc: Level xác nhận = level thấp nhất trong các điều kiện bắt buộc của level đó** (không lấy trung bình). PM trả lời D ở câu nâng cao nhưng còn A/B ở câu nền tảng nghĩa là chưa vững gốc — ưu tiên củng cố trước.

| Level | Mô tả | Điều kiện bắt buộc (theo số câu) |
|---|---|---|
| **⚠️ Cần đào tạo gấp** | Rủi ro bảo mật | Câu 13 chọn A (đưa dữ liệu nhạy cảm vào AI) — xử lý ngay bất kể level khác |
| **L1 – Apprentice** 🌱 | Dùng AI với prompt có sẵn | Câu 1-2 ≥ B; các câu 3-10, 16 phần lớn A/B |
| **L2 – Practitioner** 🥉 | Tự viết prompt; tạo PRD/User Story/Status Report; có phán đoán & ý thức bảo mật; đã thử SDLC nội bộ | Câu 1-2 = C; câu 3-6 ≥ C; câu 7 ≥ C; **câu 11-12 (mindset) ≥ C**; **câu 13 (bảo mật) ≥ C**; câu 16 ≥ C |
| **L3 – Proficient** 🥈 | Workflow AI tiết kiệm ≥ 30%; chuẩn hóa template; dùng MCP/Skill/SDLC nội bộ thành thạo | Câu 8 = D (đo được ≥30%); câu 11-12 ≥ C; câu 14-15 ≥ C; câu 16 = D; câu 18 ≥ C |
| **L4 – Expert** 🥇 | Custom GPT/Agent; automation qua MCP; tự tạo Skill team dùng; train team | Câu 14-15 = D; câu 17 ≥ C; câu 18 = D |
| **L5 – Master** 💎 | AI tool strategy cấp tổ chức; thought leadership | Câu 19 = D |

---

## Bảng Tổng Hợp Kết Quả (Manager điền)

| STT | Họ tên | Level tự đánh giá | Level manager xác nhận | Cờ bảo mật (câu 13=A?) | Gap chính cần bổ sung | Ưu tiên | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

---

*Nguồn tham chiếu: `plan-dao-tao-PM-AI-integrated.md` (bản chính thức), `level-AI-PM-tools.md`.*
*Kết quả dùng để cá nhân hóa lộ trình đào tạo — không dùng cho mục đích đánh giá KPI.*
