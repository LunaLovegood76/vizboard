# Vizboard

> Turn any data into a beautiful, interactive dashboard — in one sentence.

Vizboard is an [AgentSkills](https://agentskills.io)-compatible skill that transforms data files (Excel, CSV, JSON) or inline data into stunning, self-contained HTML dashboard pages powered by [VChart](https://github.com/VisActor/VChart) (by ByteDance VisActor). Works with **Claude Code**, **OpenClaw**, and any AgentSkills-compatible agent.

Just tell Claude what you want to visualize. Vizboard handles the rest — data extraction, chart selection, layout design, and HTML generation.

## Features

- **Multi-format input** — Excel (.xlsx/.xls), CSV, TSV, JSON, JSONL, or paste data directly
- **15+ chart types** — Bar, Line, Area, Pie, Donut, Radar, Scatter, Gauge, Funnel, Treemap, Sunburst, Sankey, Word Cloud, Waterfall, Heatmap, Histogram
- **KPI indicator cards** — Auto-extracts key metrics with smart formatting (K/M/B suffixes)
- **5 built-in themes** — Dark Tech, Light Minimal, Business Pro, Vibrant Pop, Soft Pastel
- **Smart chart selection** — Automatically picks the best chart types based on your data shape
- **Fully self-contained** — Output is a single HTML file, no server needed, opens in any browser
- **Responsive design** — Looks great on desktop and mobile
- **Interactive** — Tooltips, hover effects, and smooth animations via VChart

## Demo

Given an e-commerce Excel file with store performance data, Vizboard generates:

<img width="2988" height="4973" alt="image" src="https://github.com/user-attachments/assets/a4c13a28-53c7-49cf-a397-182bf80e7560" />

*KPI cards + grouped bar charts + donut charts + radar plots + data tables — all in one page.*

## Compatibility

Vizboard follows the [AgentSkills](https://agentskills.io) open standard. It works with any platform that supports `SKILL.md` skills, including:

- **Claude Code** — Anthropic's official CLI
- **OpenClaw** — AI Agent Gateway (30+ messaging channels)
- Any AgentSkills-compatible agent

## Installation

### Claude Code

```bash
claude install-skill LunaLovegood76/vizboard
```

### OpenClaw

```bash
# Clone to OpenClaw skills directory
git clone https://github.com/LunaLovegood76/vizboard.git ~/.openclaw/skills/vizboard

# Or symlink if you already cloned elsewhere
ln -s /path/to/vizboard ~/.openclaw/skills/vizboard
```

Then restart the gateway: `openclaw gateway restart`

### Manual

Download or clone this repo and place the folder in your agent's skills directory.

## Usage

Once installed, just talk to Claude naturally:

```
Upload an Excel file and say:
"Help me visualize this data as a dashboard"

Or paste data directly:
"Here's our monthly sales data, make a dashboard:
Jan: 12000, Feb: 15000, Mar: 18000..."

Or describe what you want:
"Create a dashboard from sales.csv with a bar chart for revenue by region
and a pie chart for product category distribution"
```

### Workflow

1. **Upload/paste data** → Vizboard extracts and analyzes the structure
2. **Pick a theme** → Choose from 5 built-in styles (or let it auto-select)
3. **Get your dashboard** → A complete HTML file, ready to open or share

## Supported Chart Types

| Chart | Best For |
|---|---|
| Bar / Grouped Bar | Category comparison |
| Line / Multi-line | Trends over time |
| Area / Stacked Area | Cumulative trends |
| Pie / Donut | Part-of-whole composition |
| Radar | Multi-dimension comparison |
| Scatter | Correlation analysis |
| Gauge | Single KPI with target |
| Funnel | Conversion flow |
| Treemap / Sunburst | Hierarchical data |
| Sankey | Flow between entities |
| Word Cloud | Text frequency |
| Waterfall | Incremental changes |
| Heatmap | Dense matrix data |
| Histogram | Distribution |

## Theme Gallery

| Dark Tech | Light Minimal | Business Pro | Vibrant Pop | Soft Pastel |
|---|---|---|---|---|
| Real-time monitoring | Reports & presentations | Executive dashboards | Marketing analytics | Healthcare & education |

## Project Structure

```
vizboard/
├── SKILL.md                  # Core skill definition & workflow
├── scripts/
│   └── extract_data.py       # Data extraction (Excel/CSV/JSON → JSON)
├── references/
│   ├── vchart-specs.md       # VChart chart type spec templates
│   └── dashboard-styles.md   # 5 theme presets + layout CSS
└── assets/
    └── template.html         # Base dashboard HTML template
```

## Tech Stack

- **[VChart](https://github.com/VisActor/VChart)** (v2.0.19) — Chart rendering engine by ByteDance VisActor
- **CSS Grid** — Responsive dashboard layout
- **Python** (pandas + openpyxl) — Data extraction and transformation

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- Python 3.8+ with `pandas` and `openpyxl` (auto-installed if missing)

## Contributing

Contributions are welcome! Feel free to:

- Add new chart types or themes
- Improve data extraction logic
- Add more layout templates
- Fix bugs or improve documentation

## License

MIT License — see [LICENSE](LICENSE) for details.
