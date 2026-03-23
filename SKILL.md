---
name: vizboard
description: >
  Transform data from Excel (.xlsx/.xls), CSV, TSV, JSON, JSONL files, or inline
  text/tables into beautiful, interactive dashboard web pages (standalone HTML) with
  rich chart components powered by VChart (by ByteDance VisActor). Supports bar, line,
  area, pie, donut, radar, scatter, gauge, funnel, treemap, sunburst, sankey, word cloud,
  waterfall, heatmap, histogram charts, KPI indicator cards, and data tables.
  Use when: (1) user uploads a data file and wants visualization, (2) user pastes data
  or describes data and wants charts, (3) user asks for a dashboard, report, or data
  visualization, (4) user asks to "make this data visual" or "create charts from this".
  Do NOT use for: editing Excel files (use xlsx skill), creating presentations (use pptx skill).
---

# Data Dashboard

Transform any data into a beautiful, interactive HTML dashboard with VChart.

## Workflow

### Phase 1: Understand Data

1. **File upload**: Run `scripts/extract_data.py <file> --preview` to inspect structure, column types, and stats.
2. **Inline data**: If user pastes text/table or describes data verbally, parse it directly into the same JSON structure (sheets → headers, rows, dtypes, stats).
3. Review the extracted data summary. Identify:
   - **Categorical columns** (string type) → x-axis, grouping, pie slices
   - **Numeric columns** (number type) → y-axis, values, sizes
   - **Date/time columns** (date type) → time-series x-axis
   - **Hierarchical patterns** → treemap, sunburst
   - **Flow/conversion patterns** → funnel, sankey

### Phase 2: Ask User Preferences

Ask the user (only what's not already clear):
- **Dashboard style** — show 5 options: (1) Dark Tech 暗色科技风, (2) Light Minimal 明亮简约风, (3) Business Pro 商务报告风, (4) Vibrant Pop 活力多彩风, (5) Soft Pastel 柔和粉彩风. Default to Light Minimal if user says "随便" or doesn't care.
- **Key metrics** — which numbers should be highlighted as KPI cards?
- **Specific chart requests** — does the user want particular chart types?

If user says "just do it" or similar, auto-select based on data characteristics and use Light Minimal style.

### Phase 3: Design Dashboard Layout

Plan the layout:

```
[Header: title + subtitle + timestamp]
[KPI Row: 3-5 key metric cards]
[Row: main chart (full or 2/3 width) + secondary chart]
[Row: 2-3 medium charts]
[Row: detail table or additional charts]
[Footer]
```

**Layout rules:**
- KPI cards: 3-5 max. Pick the most important aggregate numbers.
- Primary chart: the single most informative visualization, full width or 2/3 width.
- Supporting charts: 2-4 additional perspectives on the data.
- Optional data table: if dataset is small (<20 rows) or user wants raw data.
- Total charts per dashboard: 3-7. More than 7 is overwhelming.

### Phase 4: Build HTML

1. Read `assets/template.html` as the base structure.
2. Read `references/dashboard-styles.md` for the chosen style — replace CSS `:root` variables.
3. Read `references/vchart-specs.md` for chart spec templates.
4. Build the complete HTML file:
   - Replace template placeholders (`{{DASHBOARD_TITLE}}`, etc.).
   - Swap CSS variables for chosen style.
   - Add Google Fonts link if style requires (Poppins, Nunito, etc.).
   - Build KPI cards HTML inline.
   - Build chart cards with unique container IDs (`chart-1`, `chart-2`, etc.).
   - Build `<script>` block with VChart initialization.
   - Store all chart instances in `window._charts = []` for resize.
5. Write HTML to user's preferred location.

### Phase 5: Verify

Open or preview the generated HTML. Fix any rendering issues.

## Chart Selection Heuristic

Auto-select charts based on data shape:

| Data shape | Best chart |
|---|---|
| 1 category + 1 number | Bar (≤12 cats) or horizontal bar (>12) |
| 1 category + 1 number (parts of whole) | Pie (≤6) or donut (≤8) |
| 1 date + 1 number | Line |
| 1 date + multiple numbers | Multi-line or stacked area |
| 1 category + multiple numbers | Grouped bar or radar |
| 2 numbers | Scatter |
| 2 numbers + 1 category | Scatter with seriesField |
| Hierarchical (parent-child) | Treemap or sunburst |
| Sequential stages | Funnel |
| Flow between entities | Sankey |
| Single KPI with target | Gauge |
| Text frequency | Word cloud |
| Dense matrix (cat × cat → num) | Heatmap |
| Incremental changes | Waterfall |

## KPI Card Generation

Compute potential KPIs per numeric column:
- **Sum/Total** — revenue, count, quantity columns
- **Average** — rate, score, price columns
- **Max/Min** — peak values
- **Count distinct** — category columns
- **Latest value** — time-series data

Format for readability:
- Large numbers: K/M/B suffixes (¥1.2M, 3.5K)
- Percentages: one decimal + %
- Currency: ¥ or $ prefix as appropriate

KPI HTML pattern:
```html
<div class="kpi-card">
  <div class="label">Total Revenue</div>
  <div class="value">¥1.2M</div>
  <div class="change up">↑ 12.3% vs last month</div>
</div>
```

Show change indicator only when comparison data is available.

## VChart Key Rules

- CDN: `https://cdn.jsdelivr.net/npm/@visactor/vchart@2.0.19/build/index.min.js`
- Constructor: `new VChart.default(spec, { dom: containerId })` — note `.default`!
- Always call `.renderAsync()` after construction.
- Always include `tooltip: { visible: true }`.
- Use `color` array from chosen style for consistent theming.
- See `references/vchart-specs.md` for all chart type spec templates.

Chart init pattern:
```javascript
window._charts = [];
function createChart(domId, spec) {
  const chart = new VChart.default(spec, { dom: domId });
  chart.renderAsync();
  window._charts.push(chart);
}
```

## Data Transformation Tips

- **Wide → Long**: Transform wide format (columns = series) to long format for multi-series.
- **Aggregate**: Group by category, sum/avg for bar/pie.
- **Top N**: For pie/donut, top 5-8 categories, merge rest as "Other".
- **Date format**: Use YYYY-MM-DD or readable ("Jan 2024").
- **Null handling**: Filter out null/undefined before charting.

## Output

- Default filename: `dashboard.html` in same directory as source file.
- HTML is fully self-contained (CDN + inline data + inline CSS).
- Openable directly in any browser, no server needed.

## References

- **Chart specs**: [references/vchart-specs.md](references/vchart-specs.md) — all VChart chart type spec templates
- **Style presets**: [references/dashboard-styles.md](references/dashboard-styles.md) — 5 theme presets + layout CSS
- **Data extraction**: [scripts/extract_data.py](scripts/extract_data.py) — parse Excel/CSV/JSON to standardized JSON
- **HTML template**: [assets/template.html](assets/template.html) — base dashboard HTML structure
