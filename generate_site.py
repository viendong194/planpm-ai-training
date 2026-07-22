import os
import json

def build_site():
    base_dir = r"c:\Users\Admin\Claude\Projects\PlanPM"
    
    plan_path = os.path.join(base_dir, "plan-dao-tao-PM-AI-integrated.md")
    syllabus_path = os.path.join(base_dir, "syllabus-chi-tiet-tung-buoi-hoc-PM-AI.md")
    survey_path = os.path.join(base_dir, "survey-level-AI-tool-PM.md")
    
    with open(plan_path, "r", encoding="utf-8") as f:
        plan_md = f.read()
        
    with open(syllabus_path, "r", encoding="utf-8") as f:
        syllabus_md = f.read()
        
    with open(survey_path, "r", encoding="utf-8") as f:
        survey_md = f.read()

    # Escape for JS string embedding
    plan_json = json.dumps(plan_md)
    syllabus_json = json.dumps(syllabus_md)
    survey_json = json.dumps(survey_md)

    html_content = f"""<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlanPM - Chương Trình Đào Tạo PM AI-Integrated</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- CDN Marked.js, Highlight.js, Mermaid.js -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

    <style>
        :root {{
            --bg-body: #0f172a;
            --bg-sidebar: #1e293b;
            --bg-card: #1e293b;
            --bg-card-hover: #334155;
            --border-color: #334155;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-purple: #a855f7;
            --accent-green: #4ade80;
            --header-bg: rgba(15, 23, 42, 0.85);
        }}

        html.light {{
            --bg-body: #f8fafc;
            --bg-sidebar: #ffffff;
            --bg-card: #ffffff;
            --bg-card-hover: #f1f5f9;
            --border-color: #e2e8f0;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --accent-blue: #0284c7;
            --accent-purple: #7e22ce;
            --accent-green: #16a34a;
            --header-bg: rgba(248, 250, 252, 0.85);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.7;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            transition: background-color 0.3s, color 0.3s;
        }}

        /* Header Navbar */
        header {{
            position: sticky;
            top: 0;
            z-index: 50;
            background-color: var(--header-bg);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 1.5rem;
        }}

        .logo-area {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .logo-badge {{
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
            color: #fff;
            font-weight: 800;
            font-size: 0.85rem;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            letter-spacing: 0.5px;
        }}

        .logo-title {{
            font-size: 1.1rem;
            font-weight: 700;
            background: linear-gradient(90deg, var(--text-main), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .nav-tabs {{
            display: flex;
            gap: 0.5rem;
            background: var(--border-color);
            padding: 0.25rem;
            border-radius: 8px;
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.4rem 1rem;
            font-size: 0.88rem;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: inherit;
        }}

        .tab-btn.active {{
            background: var(--bg-card);
            color: var(--text-main);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
        }}

        .header-actions {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .search-box {{
            position: relative;
        }}

        .search-input {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 0.4rem 0.8rem 0.4rem 2rem;
            border-radius: 6px;
            font-size: 0.85rem;
            outline: none;
            width: 220px;
            transition: width 0.3s ease;
        }}

        .search-input:focus {{
            width: 280px;
            border-color: var(--accent-blue);
        }}

        .search-icon {{
            position: absolute;
            left: 0.6rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 0.85rem;
        }}

        .theme-toggle {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.88rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        /* App Layout */
        .app-container {{
            display: flex;
            flex: 1;
            overflow: hidden;
        }}

        /* Sidebar TOC */
        aside {{
            width: 280px;
            background-color: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            padding: 1.25rem 1rem;
            overflow-y: auto;
            flex-shrink: 0;
        }}

        .toc-title {{
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-bottom: 0.75rem;
            padding-left: 0.5rem;
        }}

        .toc-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }}

        .toc-item a {{
            display: block;
            padding: 0.35rem 0.6rem;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.85rem;
            border-radius: 6px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            transition: all 0.15s ease;
        }}

        .toc-item.level-2 a {{
            padding-left: 0.6rem;
            font-weight: 600;
            color: var(--text-main);
        }}

        .toc-item.level-3 a {{
            padding-left: 1.2rem;
            font-size: 0.8rem;
        }}

        .toc-item a:hover, .toc-item a.active {{
            background-color: var(--bg-card-hover);
            color: var(--accent-blue);
        }}

        /* Main Article Content */
        main {{
            flex: 1;
            padding: 2.5rem 3.5rem;
            overflow-y: auto;
            max-width: 1100px;
            margin: 0 auto;
        }}

        .markdown-body {{
            font-size: 1rem;
            color: var(--text-main);
        }}

        .markdown-body h1 {{
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 1.2rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
            background: linear-gradient(90deg, var(--text-main), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .markdown-body h2 {{
            font-size: 1.4rem;
            font-weight: 700;
            margin-top: 2rem;
            margin-bottom: 0.8rem;
            color: var(--accent-blue);
        }}

        .markdown-body h3 {{
            font-size: 1.15rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.6rem;
        }}

        .markdown-body p {{
            margin-bottom: 1rem;
            color: var(--text-main);
        }}

        .markdown-body blockquote {{
            background: rgba(56, 189, 248, 0.08);
            border-left: 4px solid var(--accent-blue);
            padding: 0.8rem 1.2rem;
            margin: 1.2rem 0;
            border-radius: 0 8px 8px 0;
            font-size: 0.95rem;
        }}

        .markdown-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            background: var(--bg-card);
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}

        .markdown-body th, .markdown-body td {{
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            font-size: 0.9rem;
        }}

        .markdown-body th {{
            background: var(--bg-card-hover);
            font-weight: 700;
            color: var(--accent-blue);
        }}

        .markdown-body tr:last-child td {{
            border-bottom: none;
        }}

        .markdown-body ul, .markdown-body ol {{
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }}

        .markdown-body li {{
            margin-bottom: 0.4rem;
        }}

        .markdown-body code {{
            font-family: 'JetBrains Mono', monospace;
            background: var(--bg-card-hover);
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-size: 0.85em;
            color: var(--accent-purple);
        }}

        .markdown-body pre {{
            background: #1e1e1e !important;
            padding: 1.2rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.2rem 0;
            border: 1px solid var(--border-color);
        }}

        .markdown-body pre code {{
            background: transparent;
            color: #d4d4d4;
            padding: 0;
        }}

        .mermaid {{
            display: flex;
            justify-content: center;
            background: var(--bg-card);
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            margin: 1.5rem 0;
        }}

        /* Responsive Design */
        @media (max-width: 900px) {{
            aside {{
                display: none;
            }}
            main {{
                padding: 1.5rem 1rem;
            }}
            .search-input {{
                width: 140px;
            }}
            .search-input:focus {{
                width: 180px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Header Navbar -->
    <header>
        <div class="logo-area">
            <span class="logo-badge">PM AI</span>
            <span class="logo-title">PlanPM Knowledge Hub</span>
        </div>

        <div class="nav-tabs">
            <button class="tab-btn active" onclick="switchTab('syllabus')">📚 Giáo Trình 18 Buổi</button>
            <button class="tab-btn" onclick="switchTab('plan')">🗺️ Plan Đào Tạo</button>
            <button class="tab-btn" onclick="switchTab('survey')">📋 Survey Đánh Giá</button>
        </div>

        <div class="header-actions">
            <div class="search-box">
                <span class="search-icon">🔍</span>
                <input type="text" class="search-input" id="searchInput" placeholder="Tìm kiếm nội dung..." onkeyup="handleSearch()">
            </div>
            <button class="theme-toggle" onclick="toggleTheme()">
                <span id="themeIcon">🌙</span> <span id="themeText">Dark</span>
            </button>
        </div>
    </header>

    <!-- App Main Container -->
    <div class="app-container">
        <!-- Sidebar TOC -->
        <aside>
            <div class="toc-title">MỤC LỤC TRUY CẬP NHANH</div>
            <ul class="toc-list" id="tocList">
                <!-- Auto generated TOC -->
            </ul>
        </aside>

        <!-- Content Area -->
        <main>
            <article class="markdown-body" id="contentArea">
                <!-- Rendered Markdown Content -->
            </article>
        </main>
    </div>

    <!-- Data Injection -->
    <script>
        const PLAN_MD = {plan_json};
        const SYLLABUS_MD = {syllabus_json};
        const SURVEY_MD = {survey_json};

        let currentTab = 'syllabus';

        mermaid.initialize({{ startOnLoad: false, theme: 'dark' }});

        function renderTab(tabName) {{
            currentTab = tabName;
            let rawMd = '';
            if (tabName === 'syllabus') rawMd = SYLLABUS_MD;
            else if (tabName === 'plan') rawMd = PLAN_MD;
            else if (tabName === 'survey') rawMd = SURVEY_MD;

            // Render Markdown
            const htmlContent = marked.parse(rawMd);
            const contentArea = document.getElementById('contentArea');
            contentArea.innerHTML = htmlContent;

            // Render Highlight.js
            hljs.highlightAll();

            // Render Mermaid diagrams
            renderMermaid();

            // Build Sidebar TOC
            buildTOC();
            
            // Scroll to top
            document.querySelector('main').scrollTop = 0;
        }}

        function switchTab(tabName) {{
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            if (tabName === 'syllabus') document.querySelectorAll('.tab-btn')[0].classList.add('active');
            if (tabName === 'plan') document.querySelectorAll('.tab-btn')[1].classList.add('active');
            if (tabName === 'survey') document.querySelectorAll('.tab-btn')[2].classList.add('active');
            
            renderTab(tabName);
        }}

        function renderMermaid() {{
            const codeBlocks = document.querySelectorAll('pre code.language-mermaid');
            codeBlocks.forEach((codeBlock, index) => {{
                const pre = codeBlock.parentElement;
                const mermaidDiv = document.createElement('div');
                mermaidDiv.className = 'mermaid';
                mermaidDiv.textContent = codeBlock.textContent;
                pre.replaceWith(mermaidDiv);
            }});
            mermaid.run();
        }}

        function buildTOC() {{
            const tocList = document.getElementById('tocList');
            tocList.innerHTML = '';

            const headings = document.querySelectorAll('#contentArea h2, #contentArea h3');
            headings.forEach((h, index) => {{
                const id = 'heading-' + index;
                h.id = id;

                const li = document.createElement('li');
                li.className = 'toc-item ' + (h.tagName === 'H2' ? 'level-2' : 'level-3');

                const a = document.createElement('a');
                a.href = '#' + id;
                a.textContent = h.textContent.replace(/^#+\s*/, '');
                a.onclick = (e) => {{
                    e.preventDefault();
                    h.scrollIntoView({{ behavior: 'smooth' }});
                }};

                li.appendChild(a);
                tocList.appendChild(li);
            }});
        }}

        function toggleTheme() {{
            const html = document.documentElement;
            if (html.classList.contains('dark')) {{
                html.classList.remove('dark');
                html.classList.add('light');
                document.getElementById('themeIcon').textContent = '☀️';
                document.getElementById('themeText').textContent = 'Light';
                mermaid.initialize({{ startOnLoad: false, theme: 'default' }});
            }} else {{
                html.classList.remove('light');
                html.classList.add('dark');
                document.getElementById('themeIcon').textContent = '🌙';
                document.getElementById('themeText').textContent = 'Dark';
                mermaid.initialize({{ startOnLoad: false, theme: 'dark' }});
            }}
            renderMermaid();
        }}

        function handleSearch() {{
            const query = document.getElementById('searchInput').value.toLowerCase();
            const elements = document.querySelectorAll('#contentArea p, #contentArea li, #contentArea tr, #contentArea h2, #contentArea h3');
            
            elements.forEach(el => {{
                if (!query) {{
                    el.style.opacity = '1';
                }} else {{
                    if (el.textContent.toLowerCase().includes(query)) {{
                        el.style.opacity = '1';
                    }} else {{
                        el.style.opacity = '0.2';
                    }}
                }}
            }});
        }}

        // Initial Load
        window.addEventListener('DOMContentLoaded', () => {{
            renderTab('syllabus');
        }});
    </script>
</body>
</html>
"""

    output_index = os.path.join(base_dir, "index.html")
    with open(output_index, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Generated index.html successfully at {output_index}")

    # Also generate vercel.json for Vercel deployment configuration
    vercel_config = {
        "version": 2,
        "name": "planpm-ai-training",
        "cleanUrls": True
    }
    vercel_path = os.path.join(base_dir, "vercel.json")
    with open(vercel_path, "w", encoding="utf-8") as f:
        json.dump(vercel_config, f, indent=2)
    print(f"Generated vercel.json successfully at {vercel_path}")

if __name__ == "__main__":
    build_site()
