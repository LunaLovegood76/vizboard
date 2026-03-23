# Vizboard

> 一句话，把任何数据变成漂亮的可视化仪表盘。

Vizboard 是一个遵循 [AgentSkills](https://agentskills.io) 开放标准的 AI 技能，能将 Excel、CSV、JSON 等数据文件或直接粘贴的数据，转化为精美的、交互式的独立 HTML 仪表盘页面。图表渲染基于字节跳动的 [VChart](https://github.com/VisActor/VChart)。

兼容 **Claude Code**、**OpenClaw** 及所有支持 AgentSkills 标准的 AI Agent 平台。

## 功能特性

- **多格式输入** — 支持 Excel (.xlsx/.xls)、CSV、TSV、JSON、JSONL，也可以直接粘贴数据
- **15+ 图表类型** — 柱状图、折线图、面积图、饼图、环形图、雷达图、散点图、仪表盘、漏斗图、树形图、旭日图、桑基图、词云、瀑布图、热力图、直方图
- **KPI 指标卡片** — 自动提取关键指标，智能格式化（万/亿后缀）
- **5 种内置主题** — 暗色科技风、明亮简约风、商务报告风、活力多彩风、柔和粉彩风
- **智能选图** — 根据数据结构自动推荐最佳图表类型
- **完全独立** — 输出单个 HTML 文件，无需服务器，浏览器直接打开
- **响应式设计** — 桌面端和移动端都好看
- **丰富交互** — 悬停提示、动画效果，基于 VChart 引擎

## 效果预览

以一份电商运营 Excel 数据为例，Vizboard 自动生成：

<img width="2988" height="4973" alt="image" src="https://github.com/user-attachments/assets/a4c13a28-53c7-49cf-a397-182bf80e7560" />

*KPI 卡片 + 分组柱状图 + 环形图 + 雷达图 + 数据表格 — 全部集成在一个页面中。*

## 兼容性

Vizboard 遵循 [AgentSkills](https://agentskills.io) 开放标准，支持所有兼容 `SKILL.md` 的平台：

- **Claude Code** — Anthropic 官方 CLI 工具
- **OpenClaw** — AI Agent 网关（支持 30+ 消息渠道）
- 其他任何兼容 AgentSkills 标准的 Agent 平台

## 安装

### Claude Code

```bash
claude install-skill LunaLovegood76/vizboard
```

### OpenClaw

```bash
# 克隆到 OpenClaw skills 目录
git clone https://github.com/LunaLovegood76/vizboard.git ~/.openclaw/skills/vizboard

# 或者如果已经克隆到别处，用软链接
ln -s /path/to/vizboard ~/.openclaw/skills/vizboard
```

重启网关生效：`openclaw gateway restart`

### 手动安装

下载或克隆本仓库，将文件夹放入你的 Agent 平台的 skills 目录即可。

## 使用方式

安装后，用自然语言告诉 AI 你想做什么：

```
上传一个 Excel 文件，然后说：
"帮我把这个数据做成仪表盘"

或者直接粘贴数据：
"这是我们的月度销售数据，帮我可视化：
1月: 12000, 2月: 15000, 3月: 18000..."

或者描述你的需求：
"用 sales.csv 生成一个仪表盘，要有按地区的营收柱状图和产品类别的饼图"
```

### 工作流程

1. **上传/粘贴数据** → Vizboard 自动提取并分析数据结构
2. **选择主题** → 从 5 种内置风格中选择（也可以让 AI 自动选）
3. **获得仪表盘** → 生成完整的 HTML 文件，可直接打开或分享

## 支持的图表类型

| 图表类型 | 适用场景 |
|---|---|
| 柱状图 / 分组柱状图 | 分类对比 |
| 折线图 / 多线图 | 趋势变化 |
| 面积图 / 堆叠面积图 | 累积趋势 |
| 饼图 / 环形图 | 占比构成 |
| 雷达图 | 多维度对比 |
| 散点图 | 相关性分析 |
| 仪表盘 | 单一 KPI 进度 |
| 漏斗图 | 转化流程 |
| 树形图 / 旭日图 | 层级数据 |
| 桑基图 | 流向关系 |
| 词云 | 文本频次 |
| 瀑布图 | 增量变化 |
| 热力图 | 密集矩阵 |
| 直方图 | 分布情况 |

## 主题一览

| 暗色科技风 | 明亮简约风 | 商务报告风 | 活力多彩风 | 柔和粉彩风 |
|---|---|---|---|---|
| 实时监控、数据大屏 | 报告、演示文稿 | 管理层报表、财务 | 营销分析、社媒 | 医疗、教育、家庭 |

## 项目结构

```
vizboard/
├── SKILL.md                  # 技能定义与工作流
├── scripts/
│   └── extract_data.py       # 数据提取脚本（Excel/CSV/JSON → JSON）
├── references/
│   ├── vchart-specs.md       # VChart 各图表类型 spec 模板
│   └── dashboard-styles.md   # 5 种主题预设 + 布局 CSS
└── assets/
    └── template.html         # 仪表盘 HTML 基础模板
```

## 技术栈

- **[VChart](https://github.com/VisActor/VChart)** (v2.0.19) — 字节跳动 VisActor 图表渲染引擎
- **CSS Grid** — 响应式仪表盘布局
- **Python** (pandas + openpyxl) — 数据提取与转换

## 环境要求

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 或 [OpenClaw](https://openclaw.ai) 或其他兼容平台
- Python 3.8+（`pandas` 和 `openpyxl` 缺失时会自动安装）

## 参与贡献

欢迎贡献！你可以：

- 新增图表类型或主题风格
- 改进数据提取逻辑
- 添加更多布局模板
- 修复 Bug 或完善文档

## 开源协议

MIT License — 详见 [LICENSE](LICENSE)
