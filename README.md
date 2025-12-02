# ChartGPT - Chart Analysis & Recommendation System

ChartGPT is a specialized AI-powered QA system designed for intelligent chart analysis, visualization recommendations, and data interpretation. It provides a comprehensive knowledge base for 30+ chart types with expert-curated use cases, pros/cons analysis, and intelligent query-based recommendations.

## 🎯 Features

- **30+ Chart Types**: Comprehensive database of chart types including Bar, Line, Scatter, Pie, Area, Bubble, Heatmap, Box Plot, Violin Plot, Treemap, Sunburst, and more
- **Intelligent Query Analysis**: Natural language processing for user intent recognition
- **Smart Recommendations**: AI-powered suggestions based on data type and visualization purpose
- **Interactive CLI Interface**: User-friendly command-line interface for interactive exploration
- **Category-Based Filtering**: Charts organized by purpose (Comparison, Composition, Distribution, Trend, Relationship, Geographic, Statistical, Ranking, Part-to-Whole)
- **Comprehensive Metadata**: Each chart includes use cases, best practices, libraries, pros, cons, and data requirements

## 📁 Project Structure

```
chartgpt-qa-system/
├── chart_knowledge_base.py      # Core knowledge base with 30+ chart types
├── chart_qa_engine.py           # Query analysis and recommendation engine
├── chart_main.py                # Interactive CLI interface
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── .gitignore                   # Git ignore configuration
```

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/danial12322/chartgpt-qa-system.git
cd chartgpt-qa-system
```

2. Install dependencies (Python 3.8+ required):
```bash
# The system uses only Python built-in libraries, no external dependencies needed
# Optional: Install visualization libraries for extended functionality
pip install matplotlib seaborn plotly pandas
```

3. Run ChartGPT:
```bash
python chart_main.py
```

## 💬 Usage Examples

### Interactive Mode

```bash
$ python chart_main.py

============================================================
Welcome to ChartGPT - Chart Analysis & Recommendation System
============================================================

You: What chart should I use to show sales trends over time?
ChartGPT: Based on your data (continuous data over time with trend analysis purpose), 
I recommend using a Line Chart. This is ideal for showing trends and changes over time.

You: Compare bar chart and line chart
ChartGPT: Both Bar and Line charts serve different purposes:
- Bar Chart: Best for comparing values across categories
- Line Chart: Best for showing trends and continuous data over time

You: list
# Shows all 30+ available chart types

You: categories
# Shows all chart categories

You: help
# Shows help and example queries

You: exit
# Quit the application
```

## 🏗️ Architecture

### ChartKnowledgeBase (chart_knowledge_base.py)

Stores comprehensive metadata for all chart types including:
- Chart name and description
- Use cases and best practices
- Ideal data types and sizes
- Pros and cons
- Recommended visualization libraries
- Category classification

### ChartQAEngine (chart_qa_engine.py)

Provides intelligent query processing:
- **Intent Recognition**: Identifies user intent (recommendation, comparison, information request)
- **Keyword Extraction**: Analyzes query for relevant keywords
- **Chart Matching**: Matches user requirements to appropriate chart types
- **Response Generation**: Generates contextual responses with template-based formatting

### ChartGPTInterface (chart_main.py)

User-facing interactive interface:
- Welcome and help functionality
- Query processing pipeline
- Conversation history tracking
- Interactive commands (list, categories, history, help, exit)

## 📊 Supported Chart Types

### Comparison Charts
- Bar Chart
- Column Chart
- Dot Plot
- Range Chart

### Composition Charts
- Pie Chart
- Donut Chart
- 100% Stacked Bar Chart
- Waffle Chart

### Distribution Charts
- Histogram
- Box Plot
- Violin Plot
- Density Plot

### Trend Charts
- Line Chart
- Area Chart
- Multi-Line Chart
- Combination Chart

### Relationship Charts
- Scatter Plot
- Bubble Chart
- Correlation Matrix
- Network Diagram

### Geographic Charts
- Map
- Choropleth Map
- Flow Map

### Statistical Charts
- Waterfall Chart
- Funnel Chart
- Sankey Diagram

### Ranking Charts
- Slope Chart
- Lollipop Chart
- Bump Chart

### Part-to-Whole Charts
- Treemap
- Sunburst Chart
- Hierarchical Bar Chart

## 🔧 Development

### Requirements
- Python 3.8 or higher
- Standard library only for core functionality
- Optional: matplotlib, seaborn, plotly, pandas for extended features

### Key Classes

**ChartKnowledgeBase**
```python
from chart_knowledge_base import ChartKnowledgeBase
kb = ChartKnowledgeBase()
```

**ChartQAEngine**
```python
from chart_qa_engine import ChartQAEngine
qa_engine = ChartQAEngine(knowledge_base)
response = qa_engine.answer_query("What chart for sales data?")
```

**ChartGPTInterface**
```python
from chart_main import ChartGPTInterface
interface = ChartGPTInterface()
interface.run()
```

## 📚 Example Queries

- "What chart should I use to show market share?"
- "Compare line chart vs bar chart for time series data"
- "Tell me about scatter plots and when to use them"
- "What visualization is best for categorical data comparison?"
- "Show me charts for trending data analysis"
- "How do I visualize correlations between variables?"
- "What's the best chart for hierarchical data?"

## 🎓 Learning Resources

ChartGPT includes comprehensive metadata for each chart type:
- **Use Cases**: Specific scenarios where each chart excels
- **Best Practices**: Guidelines for effective visualization
- **Pros/Cons**: Advantages and limitations of each chart
- **Libraries**: Recommended Python visualization libraries
- **Data Requirements**: Ideal data types and sizes

## 🔄 Query Intent Types

1. **Recommendation** - "What chart should I use for...?"
2. **Comparison** - "Compare X chart with Y chart"
3. **Information** - "Tell me about X chart"
4. **Visualization Type** - "What visualization for...?"
5. **General** - Open-ended chart questions

## 📝 Future Enhancements

- [ ] Web-based interface with Flask
- [ ] REST API for integration
- [ ] Machine learning-based chart recommendations
- [ ] Integration with popular visualization libraries
- [ ] Chart effectiveness scoring
- [ ] Custom chart template suggestions
- [ ] Data upload and automatic visualization suggestion

## 📄 License

This project is open source and available under the MIT License.

## 👥 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📧 Contact

For questions or suggestions, please reach out through GitHub issues.

---

**Happy Chart Recommending! 📊✨**
