# VChart Spec Reference

CDN: `https://cdn.jsdelivr.net/npm/@visactor/vchart@2.0.19/build/index.min.js`

Constructor (CDN mode): `new VChart.default(spec, { dom: 'container-id' })` then `.renderAsync()`

Resize: `window.addEventListener('resize', () => chart.resize())`

## Chart Selection Guide

| Data Pattern | Recommended Chart | type |
|---|---|---|
| Categories + values | Bar chart | `bar` |
| Trend over time | Line chart | `line` |
| Part-of-whole | Pie / Rose chart | `pie` / `rose` |
| Filled trend | Area chart | `area` |
| Correlation of 2 vars | Scatter plot | `scatter` |
| Multi-dimension compare | Radar chart | `radar` |
| Distribution | Histogram | `histogram` |
| Progress / KPI | Gauge | `gauge` |
| Flow / conversion | Funnel chart | `funnel` |
| Hierarchy | Treemap / Sunburst | `treemap` / `sunburst` |
| Flow between nodes | Sankey | `sankey` |
| Text frequency | Word cloud | `wordCloud` |
| Cumulative effect | Waterfall | `waterfall` |
| Dense matrix | Heatmap | `heatmap` |
| Single KPI number | Indicator card | (custom HTML) |

## Common Spec Patterns

### Bar Chart (vertical)

```json
{
  "type": "bar",
  "data": [{ "id": "data", "values": [{"x": "A", "y": 10}, {"x": "B", "y": 20}] }],
  "xField": "x",
  "yField": "y",
  "seriesField": "category",
  "label": { "visible": true },
  "tooltip": { "visible": true }
}
```

Horizontal bar: swap `xField`/`yField` and set `"direction": "horizontal"`.

Stacked bar: add `"stack": true`.

Grouped bar: use `seriesField` with different categories (grouped is default when seriesField is set).

### Line Chart

```json
{
  "type": "line",
  "data": [{ "id": "data", "values": [{"x": "Jan", "y": 10, "cat": "A"}, {"x": "Feb", "y": 20, "cat": "A"}] }],
  "xField": "x",
  "yField": "y",
  "seriesField": "cat",
  "point": { "visible": true },
  "label": { "visible": false }
}
```

Smooth line: add `"line": { "style": { "curveType": "monotone" } }`.

### Area Chart

```json
{
  "type": "area",
  "data": [{ "id": "data", "values": [{"x": "Jan", "y": 30, "cat": "Revenue"}] }],
  "xField": "x",
  "yField": "y",
  "seriesField": "cat",
  "stack": true
}
```

### Pie Chart

```json
{
  "type": "pie",
  "data": [{ "id": "data", "values": [{"type": "A", "value": 40}, {"type": "B", "value": 60}] }],
  "valueField": "value",
  "categoryField": "type",
  "label": { "visible": true },
  "outerRadius": 0.8
}
```

Donut: add `"innerRadius": 0.5`.

### Rose Chart

```json
{
  "type": "rose",
  "data": [{ "id": "data", "values": [{"type": "A", "value": 40}] }],
  "valueField": "value",
  "categoryField": "type",
  "seriesField": "type",
  "outerRadius": 0.8,
  "innerRadius": 0.2
}
```

### Radar Chart

```json
{
  "type": "radar",
  "data": [{ "id": "data", "values": [{"key": "Speed", "value": 80, "cat": "Product A"}] }],
  "categoryField": "key",
  "valueField": "value",
  "seriesField": "cat",
  "area": { "visible": true, "style": { "fillOpacity": 0.3 } },
  "point": { "visible": true }
}
```

### Scatter Plot

```json
{
  "type": "scatter",
  "data": [{ "id": "data", "values": [{"x": 10, "y": 20, "size": 5, "cat": "A"}] }],
  "xField": "x",
  "yField": "y",
  "seriesField": "cat",
  "sizeField": "size",
  "size": { "type": "linear", "range": [5, 30] }
}
```

### Gauge Chart

```json
{
  "type": "gauge",
  "data": [{ "id": "data", "values": [{"type": "target", "value": 75}] }],
  "categoryField": "type",
  "valueField": "value",
  "outerRadius": 0.8,
  "innerRadius": 0.6,
  "startAngle": -225,
  "endAngle": 45
}
```

### Funnel Chart

```json
{
  "type": "funnel",
  "data": [{ "id": "data", "values": [
    {"name": "Visit", "value": 1000},
    {"name": "Click", "value": 600},
    {"name": "Purchase", "value": 200}
  ]}],
  "categoryField": "name",
  "valueField": "value",
  "label": { "visible": true }
}
```

### Treemap

```json
{
  "type": "treemap",
  "data": [{ "id": "data", "values": [
    {"name": "A", "children": [
      {"name": "A1", "value": 10},
      {"name": "A2", "value": 20}
    ]},
    {"name": "B", "value": 30}
  ]}],
  "valueField": "value",
  "categoryField": "name",
  "label": { "visible": true }
}
```

### Sunburst

```json
{
  "type": "sunburst",
  "data": [{ "id": "data", "values": [
    {"name": "Root", "children": [
      {"name": "A", "value": 10, "children": [{"name": "A1", "value": 5}]},
      {"name": "B", "value": 20}
    ]}
  ]}],
  "valueField": "value",
  "categoryField": "name",
  "innerRadius": 0.2
}
```

### Sankey Diagram

```json
{
  "type": "sankey",
  "data": [{ "id": "data", "values": {
    "nodes": [{"name": "A"}, {"name": "B"}, {"name": "C"}],
    "links": [{"source": "A", "target": "C", "value": 10}, {"source": "B", "target": "C", "value": 20}]
  }}],
  "categoryField": "name",
  "valueField": "value",
  "sourceField": "source",
  "targetField": "target"
}
```

### Word Cloud

```json
{
  "type": "wordCloud",
  "data": [{ "id": "data", "values": [{"text": "Hello", "value": 100}, {"text": "World", "value": 60}] }],
  "nameField": "text",
  "valueField": "value"
}
```

### Waterfall Chart

```json
{
  "type": "waterfall",
  "data": [{ "id": "data", "values": [
    {"x": "Revenue", "y": 1000},
    {"x": "Cost", "y": -600},
    {"x": "Tax", "y": -100}
  ]}],
  "xField": "x",
  "yField": "y",
  "total": { "type": "end", "text": "Profit" }
}
```

### Histogram

```json
{
  "type": "histogram",
  "data": [{ "id": "data", "values": [{"value": 10}, {"value": 15}, {"value": 20}] }],
  "xField": "value",
  "yField": "count",
  "bar": { "style": { "stroke": "#fff", "lineWidth": 1 } }
}
```

### Heatmap

```json
{
  "type": "common",
  "series": [{
    "type": "heatmap",
    "xField": "week",
    "yField": "day",
    "valueField": "value",
    "cell": {
      "style": {
        "fill": { "field": "value", "scale": "color" }
      }
    }
  }],
  "scales": [{
    "id": "color",
    "type": "linear",
    "domain": { "dataId": "data", "fields": ["value"] },
    "range": ["#e0f3db", "#006837"]
  }],
  "data": [{ "id": "data", "values": [{"week": "W1", "day": "Mon", "value": 5}] }]
}
```

## Theming

Apply theme colors via spec-level `color` field:

```json
{
  "type": "bar",
  "color": ["#5B8FF9", "#5AD8A6", "#F6BD16", "#E8684A", "#6DC8EC"],
  ...
}
```

Or use `theme` field:

```json
{
  "theme": {
    "colorScheme": {
      "default": ["#5B8FF9", "#5AD8A6", "#F6BD16", "#E8684A"]
    }
  }
}
```

## Title & Legend

```json
{
  "title": { "visible": true, "text": "Chart Title", "subtext": "Subtitle" },
  "legends": { "visible": true, "orient": "bottom" }
}
```

## Axes Formatting

```json
{
  "axes": [
    { "orient": "bottom", "label": { "style": { "angle": -45 } } },
    { "orient": "left", "label": { "formatMethod": "(v) => v.toLocaleString()" } }
  ]
}
```
