# ChartGPT API Reference

Detailed API documentation for the ChartGPT system.

## Classes and Methods

### ChartKnowledgeBase

The main knowledge base class for managing chart information.

#### Initialization

```python
ChartKnowledgeBase()
```

Initializes the knowledge base with predefined chart data.

**Returns:** ChartKnowledgeBase instance

#### Methods

##### `get_all_charts()`

Retrieves all charts in the knowledge base.

```python
get_all_charts() -> List[Dict[str, any]]
```

**Returns:** List of all chart dictionaries

**Example:**
```python
from chart_knowledge_base import ChartKnowledgeBase

kb = ChartKnowledgeBase()
all_charts = kb.get_all_charts()
print(f"Total charts: {len(all_charts)}")
```

##### `get_chart_by_name(name)`

Retrrieves a specific chart by its name.

```python
get_chart_by_name(name: str) -> Optional[Dict[str, any]]
```

**Parameters:**
- `name` (str): Chart name to search for

**Returns:** Chart dictionary if found, None otherwise

**Example:**
```python
chart = kb.get_chart_by_name("Line Chart")
if chart:
    print(chart['description'])
```

##### `search_charts(query)`

Searches charts by keyword.

```python
search_charts(query: str) -> List[Dict[str, any]]
```

**Parameters:**
- `query` (str): Search query string

**Returns:** List of matching chart dictionaries

**Example:**
```python
results = kb.search_charts("comparison")
for chart in results:
    print(chart['name'])
```

##### `filter_charts(criteria)`

Filters charts by specified criteria.

```python
filter_charts(criteria: Dict[str, any]) -> List[Dict[str, any]]
```

**Parameters:**
- `criteria` (dict): Filter criteria (e.g., {'category': 'Trend'})

**Returns:** List of matching charts

**Example:**
```python
trend_charts = kb.filter_charts({'category': 'Trend'})
for chart in trend_charts:
    print(f"{chart['name']}: {chart['description']}")
```

### ChartQAEngine

The query analysis and recommendation engine.

#### Initialization

```python
ChartQAEngine(knowledge_base: ChartKnowledgeBase)
```

Initializes the QA engine with a knowledge base instance.

**Parameters:**
- `knowledge_base` (ChartKnowledgeBase): Knowledge base instance

**Returns:** ChartQAEngine instance

**Example:**
```python
from chart_knowledge_base import ChartKnowledgeBase
from chart_qa_engine import ChartQAEngine

kb = ChartKnowledgeBase()
engine = ChartQAEngine(kb)
```

#### Methods

##### `process_query(query)`

Processes a user query and returns recommendations.

```python
process_query(query: str) -> Dict[str, any]
```

**Parameters:**
- `query` (str): User query string

**Returns:** Dictionary containing:
- `success` (bool): Whether query was processed successfully
- `response` (str): Main response message
- `recommendations` (List): List of recommended charts
- `explanation` (str): Explanation of recommendations

**Example:**
```python
result = engine.process_query("I want to show sales trends over time")

if result['success']:
    print(result['response'])
    for chart in result['recommendations']:
        print(f"  - {chart['name']}")
```

##### `analyze_query(query)`

Analyzes a query to extract intent and key terms.

```python
analyze_query(query: str) -> Dict[str, any]
```

**Parameters:**
- `query` (str): Query string to analyze

**Returns:** Dictionary containing:
- `intent` (str): Detected intent
- `keywords` (List[str]): Extracted keywords
- `entities` (List[str]): Extracted entities

**Example:**
```python
analysis = engine.analyze_query("Show me distribution of customer ages")
print(f"Intent: {analysis['intent']}")
print(f"Keywords: {analysis['keywords']}")
```

##### `rank_charts(candidates, query_analysis)`

Ranks candidate charts by relevance.

```python
rank_charts(candidates: List[Dict], query_analysis: Dict) -> List[Tuple[Dict, float]]
```

**Parameters:**
- `candidates` (List[Dict]): Candidate charts to rank
- `query_analysis` (Dict): Query analysis results

**Returns:** List of (chart, score) tuples, sorted by relevance

**Example:**
```python
ranked = engine.rank_charts(candidates, analysis)
for chart, score in ranked:
    print(f"{chart['name']}: {score:.2f}")
```

##### `generate_response(recommendations, query)`

Generates a formatted response with recommendations.

```python
generate_response(recommendations: List[Dict], query: str) -> str
```

**Parameters:**
- `recommendations` (List[Dict]): List of recommended charts
- `query` (str): Original user query

**Returns:** Formatted response string

### ChartGPTInterface

Interactive CLI interface for the ChartGPT system.

#### Initialization

```python
ChartGPTInterface()
```

Initializes the interactive interface.

**Example:**
```python
from chart_main import ChartGPTInterface

interface = ChartGPTInterface()
interface.run()
```

#### Methods

##### `run()`

Starts the interactive CLI session.

```python
run() -> None
```

Displays welcome message and enters query loop.

##### `display_welcome()`

Displays the welcome banner and instructions.

```python
display_welcome() -> None
```

##### `get_user_query()`

Prompts user for input.

```python
get_user_query() -> str
```

**Returns:** User input string

##### `process_and_display(query)`

Processes query and displays formatted results.

```python
process_and_display(query: str) -> None
```

## Data Structures

### Chart Dictionary

Each chart is represented as a dictionary with:

```python
{
    'name': str,              # Chart type name
    'description': str,       # What it visualizes
    'use_cases': List[str],   # When to use it
    'pros': List[str],        # Advantages
    'cons': List[str],        # Disadvantages
    'best_for': str,          # Data types it's best for
    'libraries': List[str],   # Recommended libraries
    'category': str           # Classification
}
```

### Query Analysis Dictionary

```python
{
    'intent': str,            # User's goal
    'keywords': List[str],    # Key terms
    'entities': List[str]     # Identified entities
}
```

### Process Query Response

```python
{
    'success': bool,          # Process success
    'response': str,          # Main message
    'recommendations': [],    # Suggested charts
    'explanation': str        # Why these charts
}
```

## Error Handling

All methods handle errors gracefully:

```python
try:
    result = engine.process_query(user_input)
    if not result['success']:
        print(f"Error: {result['response']}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

## Best Practices

1. **Always check success flag** in responses
2. **Handle None returns** from get_chart_by_name()
3. **Use try-except** blocks for error handling
4. **Cache results** for frequently asked queries
5. **Validate user input** before processing

## Integration Example

```python
from chart_knowledge_base import ChartKnowledgeBase
from chart_qa_engine import ChartQAEngine

def get_chart_recommendation(user_query: str) -> dict:
    # Initialize components
    kb = ChartKnowledgeBase()
    engine = ChartQAEngine(kb)
    
    # Process query
    result = engine.process_query(user_query)
    
    return result

# Usage
if __name__ == "__main__":
    query = "What chart shows comparison between multiple categories?"
    recommendation = get_chart_recommendation(query)
    print(recommendation['response'])
```

---

**Last Updated:** December 2, 2025
**API Version:** 1.0
