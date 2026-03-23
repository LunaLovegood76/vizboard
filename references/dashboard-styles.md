# Dashboard Styles Reference

## Style Presets

When user doesn't specify a preference, ask which style they prefer. Below are 5 built-in presets.

---

### 1. Dark Tech (暗色科技风)

Best for: real-time monitoring, tech dashboards, data center displays.

```css
:root {
  --bg-primary: #0d1117;
  --bg-card: #161b22;
  --bg-card-hover: #1c2333;
  --border-color: #30363d;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #484f58;
  --accent: #58a6ff;
  --accent-secondary: #3fb950;
  --danger: #f85149;
  --warning: #d29922;
  --shadow: 0 2px 8px rgba(0,0,0,0.4);
  --radius: 12px;
}
```

Chart colors: `["#58a6ff", "#3fb950", "#d29922", "#f85149", "#bc8cff", "#39d2c0", "#ff7b72", "#79c0ff"]`

Font: `'Inter', 'SF Pro Display', system-ui, sans-serif`

---

### 2. Light Minimal (明亮简约风)

Best for: reports, presentations, business analysis.

```css
:root {
  --bg-primary: #f8f9fa;
  --bg-card: #ffffff;
  --bg-card-hover: #f1f3f5;
  --border-color: #e9ecef;
  --text-primary: #212529;
  --text-secondary: #6c757d;
  --text-muted: #adb5bd;
  --accent: #4263eb;
  --accent-secondary: #20c997;
  --danger: #fa5252;
  --warning: #fab005;
  --shadow: 0 1px 3px rgba(0,0,0,0.08);
  --radius: 10px;
}
```

Chart colors: `["#4263eb", "#20c997", "#fab005", "#fa5252", "#7950f2", "#15aabf", "#ff922b", "#51cf66"]`

Font: `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`

---

### 3. Business Pro (商务报告风)

Best for: executive reports, financial dashboards, investor decks.

```css
:root {
  --bg-primary: #f5f5f0;
  --bg-card: #ffffff;
  --bg-card-hover: #fafaf5;
  --border-color: #d4d4c8;
  --text-primary: #1a1a2e;
  --text-secondary: #4a4a68;
  --text-muted: #9898a8;
  --accent: #2d5a7b;
  --accent-secondary: #3a7d6e;
  --danger: #c0392b;
  --warning: #d4a017;
  --shadow: 0 2px 6px rgba(0,0,0,0.06);
  --radius: 8px;
}
```

Chart colors: `["#2d5a7b", "#3a7d6e", "#d4a017", "#c0392b", "#6b4c9a", "#2e86ab", "#a45a52", "#4a7c59"]`

Font: `'Georgia', 'Times New Roman', serif` for titles; `'Inter', sans-serif` for body.

---

### 4. Vibrant Pop (活力多彩风)

Best for: marketing reports, social media analytics, creative dashboards.

```css
:root {
  --bg-primary: #fefcfb;
  --bg-card: #ffffff;
  --bg-card-hover: #fff5f5;
  --border-color: #ffe0e0;
  --text-primary: #2d2d2d;
  --text-secondary: #666666;
  --text-muted: #aaaaaa;
  --accent: #ff6b6b;
  --accent-secondary: #4ecdc4;
  --danger: #ff4757;
  --warning: #ffa502;
  --shadow: 0 4px 15px rgba(255,107,107,0.1);
  --radius: 16px;
}
```

Chart colors: `["#ff6b6b", "#4ecdc4", "#45b7d1", "#f9ca24", "#6c5ce7", "#a8e6cf", "#ff9ff3", "#feca57"]`

Font: `'Poppins', 'Nunito', sans-serif`

---

### 5. Soft Pastel (柔和粉彩风)

Best for: healthcare, wellness, education, family-oriented data.

```css
:root {
  --bg-primary: #faf8ff;
  --bg-card: #ffffff;
  --bg-card-hover: #f5f0ff;
  --border-color: #e8e0f0;
  --text-primary: #3d3552;
  --text-secondary: #6b6085;
  --text-muted: #a89ec0;
  --accent: #9b8ec4;
  --accent-secondary: #7ec8a4;
  --danger: #e88b9c;
  --warning: #e8c87a;
  --shadow: 0 2px 10px rgba(155,142,196,0.12);
  --radius: 14px;
}
```

Chart colors: `["#9b8ec4", "#7ec8a4", "#e8c87a", "#e88b9c", "#82b4d9", "#c9a8e8", "#8dd3c7", "#f4b4c9"]`

Font: `'Nunito', 'Quicksand', sans-serif`

---

## KPI Card Styles

KPI cards display single key metrics. CSS pattern:

```css
.kpi-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 20px 24px;
  box-shadow: var(--shadow);
}
.kpi-card .label { font-size: 13px; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px; }
.kpi-card .value { font-size: 32px; font-weight: 700; color: var(--text-primary); margin: 8px 0 4px; }
.kpi-card .change { font-size: 13px; }
.kpi-card .change.up { color: var(--accent-secondary); }
.kpi-card .change.down { color: var(--danger); }
```

## Dashboard Layout (CSS Grid)

```css
.dashboard {
  display: grid;
  gap: 20px;
  padding: 24px;
  max-width: 1400px;
  margin: 0 auto;
}

/* KPI row: auto columns */
.kpi-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

/* Chart grid */
.chart-row-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.chart-row-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }
.chart-full { display: grid; grid-template-columns: 1fr; gap: 20px; }
.chart-2-1 { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }
.chart-1-2 { display: grid; grid-template-columns: 1fr 2fr; gap: 20px; }

/* Responsive */
@media (max-width: 768px) {
  .chart-row-2, .chart-row-3, .chart-2-1, .chart-1-2 {
    grid-template-columns: 1fr;
  }
}
```

## Chart Card Wrapper

```css
.chart-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 20px;
  box-shadow: var(--shadow);
}
.chart-card h3 {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 16px;
}
.chart-container {
  width: 100%;
  height: 300px;
}
```
