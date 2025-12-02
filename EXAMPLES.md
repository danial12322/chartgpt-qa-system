# ChartGPT - Usage Examples

Practical examples for using ChartGPT in different scenarios.

## 🚀 Quick Start

### Running ChartGPT CLI

```bash
python chart_main.py
```

This starts the interactive chatbot interface where you can ask questions about charts.

## 📊 Example Queries

### 1. Getting Chart Recommendations

**User Query:**
```
What chart should I use to show sales trends over the past 12 months?
```

**Expected Response:**
ChartGPT will recommend a **Line Chart** because:
- You're showing data over time (continuous timeline)
- Focus is on trends (how values change)
- Line charts are ideal for displaying trends across time periods

**Other suitable options:** Area Chart, Multi-Line Chart (if comparing multiple products)

---

### 2. Comparing Different Chart Types

**User Query:**
```
Compare bar chart and pie chart for showing market share
```

**Expected Response:**
- **Pie Chart:** Better for showing proportions of a whole (100%)
  - Easy to see relative sizes
  - Best for 2-5 categories
  - Not good for many categories

- **Bar Chart:** Better for accurate value comparison
  - Easier to read exact percentages
  - Works well with many categories
  - Better for comparing against each other

**Recommendation:** Use Pie Chart for simplicity, Bar Chart for accuracy

---

### 3. Getting Detailed Chart Information

**User Query:**
```
Tell me about scatter plots
```

**Expected Response:**
- **Description:** Shows relationship between two continuous variables
- **Best For:** Finding correlations and outliers
- **Use Cases:** 
  - Price vs. demand analysis
  - Height vs. weight distribution
  - Performance metrics comparison
- **Data Type:** Continuous
- **Recommended Libraries:** matplotlib, seaborn, plotly
- **Pros:** Easy correlation identification, shows distribution patterns
- **Cons:** Hard to read with many overlapping points

---

### 4. Finding Charts by Data Characteristics

**User Query:**
```
What visualization is best for categorical data with many categories?
```

**Expected Response:**
- **Bar Chart:** Standard choice, works with many categories
- **Horizontal Bar Chart:** Better when category names are long
- **Treemap:** Alternative for showing hierarchical categories

---

## 💫 Interactive Commands

### View All Available Charts

```
You: list

ChartGPT Response: [Shows all 30+ chart types with descriptions]
```

### See Chart Categories

```
You: categories

ChartGPT Response:
1. Comparison
2. Composition
3. Distribution
4. Trend
5. Relationship
6. Geographic
7. Statistical
8. Ranking
9. Part-to-Whole
```

### View Command Help

```
You: help

ChartGPT Response: [Shows all available commands and example queries]
```

### Check Conversation History

```
You: history

ChartGPT Response: [Lists all previous queries and responses]
```

### Exit ChartGPT

```
You: exit

ChartGPT Response: "Thank you for using ChartGPT!"
```

---

## 📄 Use Case Examples

### Sales Dashboard

**Scenario:** Building a sales analytics dashboard

```
You: I need to show: 
- Monthly sales trend
- Sales by region
- Top products comparison
- Sales target achievement

ChartGPT Recommendations:
1. Monthly sales trend → Line Chart
2. Sales by region → Pie Chart or Bar Chart
3. Top products comparison → Horizontal Bar Chart
4. Sales target achievement → Bullet Chart or Gauge Chart
```

### Customer Analysis

**Scenario:** Analyzing customer demographics

```
You: Show me customer age distribution and how it correlates with purchase frequency

ChartGPT Recommendations:
1. Age distribution → Histogram or Box Plot
2. Age vs. purchase frequency → Scatter Plot
3. Both together → 2D Scatter Plot with color coding
```

### Product Performance

**Scenario:** Comparing product performance metrics

```
You: Compare 5 products across 4 metrics (quality, price, speed, reliability)

ChartGPT Recommendations:
1. Radar Chart - Shows all metrics for each product
2. Multiple Bar Charts - One per metric
3. Heatmap - Color-coded performance matrix
```

---

## 💻 Developer Usage

### Using ChartGPT as a Library

```python
from chart_knowledge_base import ChartKnowledgeBase
from chart_qa_engine import ChartQAEngine

# Initialize
kb = ChartKnowledgeBase()
qa_engine = ChartQAEngine(kb)

# Get chart recommendation
response = qa_engine.answer_query("What chart for time series data?")
print(response)

# Get specific chart info
bar_chart_info = qa_engine.get_chart_info('Bar Chart')
print(bar_chart_info['use_cases'])

# Get recommendation by data type and purpose
rec = qa_engine.get_recommendation('continuous', 'trend')
print(rec)

# Get all charts in a category
comparison_charts = qa_engine.get_charts_by_category('Comparison')
for chart_name in comparison_charts:
    print(chart_name)
```

### Running Tests

```bash
# Run all tests
python -m unittest discover -v

# Run specific test
python -m unittest test_chart_knowledge_base.TestChartKnowledgeBase.test_chart_count -v
```

---

## 🌟 Advanced Scenarios

### Multi-Dimensional Data Visualization

**Data:** Product sales across 3 dimensions (time, region, product)

```
You: I have sales data with time, region, and product. How should I visualize all three?

ChartGPT Options:
1. Small Multiples - One line chart per region
2. Animated Chart - Show changes over time
3. 3D Scatter - If data points are limited
4. Dashboard - Combine multiple charts
```

### Statistical Analysis Visualization

**Data:** Test scores distribution

```
You: I need to show test score distribution with mean, median, outliers

ChartGPT Recommendations:
1. Box Plot - Shows all statistics clearly
2. Violin Plot - Shows distribution shape
3. Histogram + density curve - Shows distribution pattern
```

---

## ❓ Tips & Tricks

1. **Always specify context** - Include what data you have and what insight you want
2. **Ask for comparisons** - ChartGPT can compare charts to help you choose
3. **Request alternatives** - Ask for multiple chart options
4. **Check examples** - Use `help` command to see example queries
5. **Review metadata** - Get full chart information before deciding

---

## 🛠️ Troubleshooting Examples

### "I don't know which chart to use"

**Solution:**
```
You: Tell me about all comparison charts

ChartGPT will list all charts in the Comparison category
```

### "I need something different"

**Solution:**
```
You: What's an alternative to pie charts?

ChartGPT will suggest: Donut Chart, 100% Stacked Bar, Waffle Chart
```

### "I want to compare multiple options"

**Solution:**
```
You: Compare scatter plot, bubble chart, and heatmap

ChartGPT will compare all three with pros/cons
```

---

**Last Updated:** December 2, 2025
**ChartGPT Version:** 1.0
