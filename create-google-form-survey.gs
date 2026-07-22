/**
 * Tạo Google Form "Survey Đánh Giá Level Dùng AI Tool — Project Manager"
 * từ nội dung file survey-level-AI-tool-PM.md
 *
 * CÁCH DÙNG:
 * 1. Mở https://script.google.com → New project
 * 2. Xóa hết code mặc định, dán toàn bộ nội dung file này vào
 * 3. Bấm Run (chọn hàm createSurveyForm) → cấp quyền khi được hỏi
 * 4. Xem log (Ctrl+Enter hoặc View > Logs) để lấy link Form (edit link + published link)
 * 5. Form sẽ tự xuất hiện trong Google Drive của bạn, có thể chỉnh sửa thêm nếu cần
 */

function createSurveyForm() {
  var form = FormApp.create('Survey Đánh Giá Level Dùng AI Tool — Project Manager');

  form.setDescription(
    'Nguồn tham chiếu: plan-dao-tao-PM-AI-tools.md + level-AI-PM-tools.md\n' +
    'Mục đích: Xác định PM đang ở level nào trong việc dùng AI tool để làm công việc PM ' +
    '(không đánh giá kỹ năng vận hành dự án nói chung).\n' +
    'Cách điền: Với mỗi câu, chọn 1 đáp án mô tả đúng nhất tình trạng hiện tại của bạn. ' +
    'Chọn theo việc bạn đã thực sự làm, không phải điều bạn nghĩ mình "có thể làm được".'
  );
  form.setCollectEmail(true);
  form.setProgressBar(true);

  // ----- Thông tin cá nhân -----
  form.addTextItem().setTitle('Họ tên').setRequired(true);
  form.addTextItem().setTitle('Dự án hiện tại').setRequired(true);
  form.addDateItem().setTitle('Ngày điền').setRequired(true);

  var questions = [
    {
      title: 'Câu 1 — Làm quen công cụ AI',
      desc: 'Bạn đã dùng công cụ AI (ChatGPT, Claude, Copilot...) trong công việc như thế nào?',
      choices: [
        'A. Chưa dùng, hoặc chỉ tò mò thử vài lần không có mục đích công việc cụ thể.',
        'B. Dùng được với prompt/mẫu có sẵn từ thư viện team. Ví dụ: lấy prompt "tóm tắt meeting" có sẵn, dán transcript vào, sửa lại một chút.',
        'C. Tự viết prompt cho nhu cầu riêng mà không cần mẫu có sẵn. Ví dụ: tự gõ "Đóng vai BA, viết 5 user story từ đoạn brief sau, format theo Given-When-Then" mà không cần ai đưa mẫu.',
        'D. Dùng AI như một bước mặc định trong mọi việc liên quan. Ví dụ: mỗi sáng mở AI để review dashboard token, mỗi cuối sprint tự động dùng AI phân tích retro — thành thói quen, không cần nhắc.'
      ]
    },
    {
      title: 'Câu 2 — Cấu trúc viết prompt',
      desc: 'Khi cần AI làm một việc phức tạp (không phải hỏi 1 câu đơn giản), bạn viết prompt như thế nào?',
      choices: [
        'A. Gõ một câu ngắn, không có ngữ cảnh, nếu sai thì thử lại câu khác. Ví dụ: "viết PRD giúp tôi" rồi chờ xem AI ra gì.',
        'B. Biết thêm role + yêu cầu cơ bản nhưng chưa có cấu trúc rõ ràng. Ví dụ: "Bạn là PM, hãy viết PRD cho tính năng đăng nhập."',
        'C. Viết đủ cấu trúc Role + Context + Yêu cầu + Format + Ví dụ, và biết refine lại khi output sai.',
        'D. Dùng kỹ thuật nâng cao: chain-of-thought hoặc few-shot (đưa ví dụ mẫu để AI bắt chước format).'
      ]
    },
    {
      title: 'Câu 3 — Tạo PRD bằng AI',
      desc: 'Bạn đã dùng AI để soạn PRD (Product Requirement Document) chưa?',
      choices: [
        'A. Chưa từng, vẫn viết tay 100%.',
        'B. Có thử nhưng phải sửa lại gần hết, mất nhiều thời gian hơn viết tay.',
        'C. Ra được bản PRD draft đầy đủ cấu trúc từ 1 đoạn brief, trong dưới 30 phút, chỉ cần review và chỉnh sửa nhỏ.',
        'D. Có checklist review chuẩn trước khi giao team, đã dùng cho nhiều dự án khác nhau, biết điều chỉnh cấu trúc PRD theo loại dự án.'
      ]
    },
    {
      title: 'Câu 4 — Tạo User Story & Acceptance Criteria bằng AI',
      desc: 'Bạn dùng AI để viết User Story và AC như thế nào?',
      choices: [
        'A. Chưa dùng AI cho việc này.',
        'B. Có dùng nhưng chưa biết cách review — copy nguyên output vào Jira mà không kiểm tra kỹ.',
        'C. Dùng AI generate User Story từ PRD, generate AC từ Story, và tự phát hiện được chỗ AI viết mơ hồ hoặc thiếu edge case.',
        'D. Có quy trình chuẩn: brief → AI draft → tự review theo checklist riêng → AI refine lần 2 → giao team, áp dụng nhất quán cho toàn bộ backlog.'
      ]
    },
    {
      title: 'Câu 5 — Status Report cho Stakeholder',
      desc: 'Bạn dùng AI để viết báo cáo tiến độ cho stakeholder như thế nào?',
      choices: [
        'A. Chưa dùng, tự viết tay hoàn toàn.',
        'B. Dùng AI viết nháp nhưng vẫn còn thuật ngữ kỹ thuật, stakeholder non-technical đọc không hiểu, phải hỏi lại.',
        'C. Dùng AI translate số liệu kỹ thuật sang business value dễ hiểu, report 1 trang, stakeholder hiểu ngay không cần hỏi thêm.',
        'D. Ngoài report viết, còn dùng AI hỗ trợ chuẩn bị talking points cho câu hỏi khó từ khách hàng, có thể present bằng video/slide.'
      ]
    },
    {
      title: 'Câu 6 — Theo dõi Token Cost bằng AI',
      desc: 'Bạn dùng AI để theo dõi token cost như thế nào?',
      choices: [
        'A. Không theo dõi token cost, hoặc để việc này cho Dev/Tech Lead.',
        'B. Có đọc dashboard nhưng không phân tích, chỉ nhìn con số tổng.',
        'C. Dùng AI tóm tắt dashboard, nhận diện được task/agent nào dùng nhiều token hơn dự tính, phân biệt spike bình thường và spike đáng lo.',
        'D. Dùng AI so sánh token/feature qua nhiều sprint, phát hiện pattern, và tự forecast budget 1-2 sprint tới từ baseline.'
      ]
    },
    {
      title: 'Câu 7 — Prompt Library cá nhân',
      desc: 'Bạn có lưu lại prompt để dùng lại không?',
      choices: [
        'A. Không lưu, mỗi lần cần lại gõ lại từ đầu.',
        'B. Có lưu vài prompt rời rạc nhưng không có tổ chức, khó tìm lại.',
        'C. Có thư viện prompt cá nhân ≥ 10 prompt, có ghi chú, tìm lại dễ dàng.',
        'D. Ngoài thư viện cá nhân, đã chia sẻ/đóng góp prompt cho team dùng chung, có ít nhất 1 template team khác áp dụng thực tế.'
      ]
    },
    {
      title: 'Câu 8 — AI trong Workflow Sprint hàng ngày',
      desc: 'AI có mặt trong công việc sprint của bạn ở mức nào?',
      choices: [
        'A. Chỉ dùng AI khi "chợt nhớ ra", không phải việc thường xuyên.',
        'B. Dùng AI cho 1-2 việc cố định nhưng chưa mở rộng ra các bước khác.',
        'C. AI có mặt xuyên suốt sprint cycle: Sprint Planning, Backlog Refinement, Retrospective.',
        'D. Đã đo được: workflow có AI tiết kiệm ≥ 30% thời gian so với làm tay (có số liệu cụ thể).'
      ]
    },
    {
      title: 'Câu 9 — Phân tích dữ liệu & rút insight bằng AI',
      desc: 'Bạn dùng AI để phân tích dữ liệu (feedback, metrics, sprint data) như thế nào?',
      choices: [
        'A. Chưa dùng AI cho việc phân tích, chỉ đọc số liệu thô.',
        'B. Dùng AI tóm tắt dữ liệu nhưng dừng ở liệt kê lại, chưa có insight hay đề xuất hành động.',
        'C. Dùng AI đi từ raw data ra được insight cụ thể và đề xuất hành động rõ ràng.',
        'D. Kết hợp phân tích insight với forecast, dùng kết quả để điều chỉnh kế hoạch trước khi vấn đề xảy ra.'
      ]
    },
    {
      title: 'Câu 10 — Chọn đúng tool cho đúng việc',
      desc: 'Bạn có phân biệt được nên dùng tool AI nào cho việc gì không?',
      choices: [
        'A. Chỉ biết 1 tool, dùng cho mọi việc bất kể phù hợp hay không.',
        'B. Biết vài tool khác nhau nhưng chọn theo thói quen, chưa so sánh rõ ưu nhược điểm.',
        'C. Biết so sánh và chọn đúng tool theo use case cụ thể (vd: Jira AI cho backlog, Claude/ChatGPT cho PRD).',
        'D. Từng tham gia đánh giá/thử nghiệm (pilot) tool mới trước khi đề xuất cho team, có tiêu chí đánh giá rõ ràng.'
      ]
    },
    {
      title: 'Câu 11 — Xây dựng & chia sẻ template cho team',
      desc: 'Bạn đã đóng góp gì cho việc chuẩn hóa AI trong team chưa?',
      choices: [
        'A. Chưa từng chia sẻ, chỉ dùng cho việc cá nhân.',
        'B. Có chia sẻ 1-2 prompt cho đồng nghiệp khi họ hỏi, nhưng không chủ động.',
        'C. Chủ động xây dựng prompt template chuẩn kèm hướng dẫn sử dụng, có ít nhất 1 template team đang dùng thật.',
        'D. Đã hướng dẫn/mentor được ít nhất 1 PM khác áp dụng AI vào công việc, và họ áp dụng thành công.'
      ]
    },
    {
      title: 'Câu 12 — Kết nối AI với dữ liệu/công cụ khác (MCP)',
      desc: 'Bạn có dùng AI kết nối trực tiếp với công cụ khác (Jira, Backlog, Slack, Notion...) qua MCP/connector để lấy hoặc cập nhật dữ liệu, thay vì copy-paste thủ công không?',
      choices: [
        'A. Chưa biết MCP/connector là gì — luôn copy-paste dữ liệu thủ công vào AI.',
        'B. Biết khái niệm MCP/connector nhưng chưa tự dùng.',
        'C. Đã tự dùng AI kết nối với ít nhất 1 công cụ qua MCP để lấy/cập nhật dữ liệu trực tiếp.',
        'D. Kết hợp nhiều MCP/connector trong cùng một quy trình để tự động hóa việc lặp lại (vd: AI đọc Jira, đọc Slack, ghi báo cáo vào Notion).'
      ]
    },
    {
      title: 'Câu 13 — Dùng/tạo Skill (quy trình AI đóng gói sẵn)',
      desc: 'Bạn đã dùng hoặc tự tạo "Skill" — gói hướng dẫn/quy trình AI đóng gói sẵn cho một việc lặp lại — chưa?',
      choices: [
        'A. Chưa biết khái niệm Skill — mỗi lần làm việc lặp lại vẫn gõ prompt lại từ đầu.',
        'B. Có dùng Skill có sẵn (do công ty/đồng nghiệp tạo) cho vài việc quen thuộc, chưa tự tạo Skill riêng.',
        'C. Tự tạo được ít nhất 1 Skill cho việc lặp lại của riêng mình (vd: skill tự động review Status Report theo checklist chuẩn).',
        'D. Skill do bạn tạo đang được người khác trong team dùng lại thật, và bạn có cập nhật/cải tiến dựa trên phản hồi thực tế.'
      ]
    },
    {
      title: 'Câu 14 — Bộ công cụ SDLC nội bộ (Spec → RAG → BD/DD/SRS → Testcase → Code)',
      desc: 'Công ty có bộ công cụ SDLC dùng AI: đưa spec trao đổi với khách hàng vào storage, dùng RAG phân tích nội dung, tự động tạo BD/DD/SRS, sinh testcase checklist, rồi sinh code. Bạn đã dùng bộ công cụ này ở mức nào?',
      choices: [
        'A. Chưa từng nghe nói về bộ công cụ này.',
        'B. Có nghe/được giới thiệu, nhưng chưa tự dùng vào dự án thực tế nào.',
        'C. Đã dùng thử trong ít nhất 1 dự án, nhưng vẫn phải sửa/review khá nhiều trước khi dùng được.',
        'D. Đã dùng thường xuyên trong dự án đang chạy, biết chuẩn hóa input để RAG ra kết quả chất lượng cao, hạn chế phải sửa lại nhiều.'
      ]
    },
    {
      title: 'Câu 15 — Custom tool / Automation',
      desc: 'Bạn đã từng xây dựng công cụ AI riêng hoặc automation chưa?',
      choices: [
        'A. Chưa từng, chỉ dùng tool có sẵn qua giao diện chat thông thường.',
        'B. Có nghe/tìm hiểu về Custom GPT, Zapier, Make... nhưng chưa tự làm.',
        'C. Đã tự xây 1 Custom GPT/Agent hoặc automation đơn giản và đang dùng thật cho công việc.',
        'D. Công cụ/automation do bạn xây đang được cả team dùng thực tế, và bạn đã training lại cho người khác cách dùng.'
      ]
    },
    {
      title: 'Câu 16 — Chiến lược AI Tool cấp tổ chức',
      desc: 'Bạn có tham gia vào việc định hướng dùng AI tool ở quy mô lớn hơn nhóm mình không?',
      choices: [
        'A. Chưa, chỉ quan tâm ở phạm vi công việc cá nhân/dự án mình.',
        'B. Có đóng góp ý kiến khi được hỏi nhưng chưa chủ động đề xuất.',
        'C. Đã chủ động đề xuất roadmap/ngân sách adoption AI tool cho nhóm/phòng ban.',
        'D. Đã xây dựng chiến lược AI tool được lãnh đạo phê duyệt và đang triển khai ở cấp SBU/công ty; hoặc có bài viết/talk được cộng đồng bên ngoài đón nhận.'
      ]
    }
  ];

  questions.forEach(function (q) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(q.title + '\n' + q.desc);
    item.setChoiceValues(q.choices);
    item.setRequired(true);
  });

  Logger.log('Form đã tạo xong!');
  Logger.log('Link để CHỈNH SỬA (chỉ bạn thấy): ' + form.getEditUrl());
  Logger.log('Link để GỬI cho mọi người điền: ' + form.getPublishedUrl());
}
