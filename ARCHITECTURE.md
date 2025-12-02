# ChartGPT - System Architecture

## Overview

ChartGPT is a knowledge-based question-answering system specialized in chart recommendations and visualization guidance. It uses a domain-specific knowledge base combined with intelligent query analysis to recommend optimal chart types for various data visualization scenarios.

## System Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface                            │
│            (CLI/Interactive Interface)                       │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                  ChartGPT Engine                             │
│          (Query Processing & Analysis)                       │
│                                                              │
│  ┌──────────────┐      ┌──────────────┐                     │
│  │ Query Parser │◄────►│ Analyzer     │                     │
│  └──────────────┘      └──────────────┘                     │
└──────────────┬───────────────────────────────────────────┬──┘
               │                                           │
               ▼                                           ▼
┌──────────────────────────┐        ┌────────────────────────┐
│ Chart Knowledge Base     │        │ Recommendation Engine  │
│  (30+ Chart Types)       │        │ (Scoring & Ranking)    │
│                          │        │                        │
│ - Chart Metadata         │        │ - Relevance Scoring    │
│ - Use Cases              │        │ - Ranking Algorithm    │
│ - Pros/Cons              │        │ - Result Filtering     │
│ - Libraries              │        │                        │
└──────────────────────────┘        └────────────────────────┘
```

## Component Details

### 1. Chart Knowledge Base (ChartKnowledgeBase)

**File:** `chart_knowledge_base.py`

**Responsibilities:**
- Maintain comprehensive database of 30+ chart types
- Store chart metadata (name, description, use cases, pros, cons, libraries)
- Provide efficient chart retrieval methods
- Support flexible querying mechanisms

**Key Classes:**
```python
class ChartKnowledgeBase:
    - __init__()          # Initialize with chart data
    - get_all_charts()    # Retrieve all charts
    - get_chart_by_name() # Find chart by name
    - search_charts()     # Full-text search
    - filter_charts()     # Filter by criteria
```

**Data Structure:**
Each chart contains:
- `name`: Chart identifier
- `description`: What the chart visualizes
- `use_cases`: When to use this chart
- `pros`: Advantages
- `cons`: Disadvantages
- `best_for`: Data types and scenarios
- `libraries`: Recommended visualization libraries
- `category`: Chart classification (Comparison, Trend, Distribution, etc.)

### 2. Chart QA Engine (ChartQAEngine)

**File:** `chart_qa_engine.py`

**Responsibilities:**
- Process user queries about charts
- Analyze query intent and extract key information
- Rank and recommend suitable charts
- Provide detailed explanations

**Key Classes:**
```python
class ChartQAEngine:
    - __init__()              # Initialize with knowledge base
    - process_query()         # Main entry point
    - analyze_query()         # Extract query intent
    - rank_charts()           # Score and rank candidates
    - generate_response()     # Format response
```

**Query Analysis Pipeline:**
1. **Input Normalization**: Clean and standardize query
2. **Intent Detection**: Identify what user wants (recommendation, comparison, etc.)
3. **Entity Extraction**: Extract key terms (chart types, data types, etc.)
4. **Chart Matching**: Find relevant charts in knowledge base
5. **Ranking**: Score charts by relevance
6. **Response Generation**: Format and present recommendations

### 3. Interactive CLI Interface (ChartGPTInterface)

**File:** `chart_main.py`

**Responsibilities:**
- Provide user-friendly command-line interface
- Handle user input and display results
- Manage interactive session state
- Support various interaction modes

**Key Features:**
- Welcome banner and usage instructions
- Query input prompt with validation
- Formatted output display
- Error handling and user guidance
- Exit functionality

## Data Flow

### Query Processing Flow

```
User Input
    ↓
Input Validation & Sanitization
    ↓
Query Intent Detection
    ↓
Key Term Extraction
    ↓
Chart Knowledge Base Query
    ↓
Candidate Chart Filtering
    ↓
Relevance Scoring & Ranking
    ↓
Top Results Selection
    ↓
Response Formatting
    ↓
User Output
```

## Design Patterns

### 1. Singleton Pattern
- ChartKnowledgeBase acts as single source of truth
- Prevents duplicate data loading
- Ensures consistency across engine instances

### 2. Strategy Pattern
- Different chart retrieval strategies (by name, by category, by use case)
- Flexible filtering and search mechanisms

### 3. Template Method Pattern
- Query processing follows defined steps
- Each step can be customized independently

### 4. Factory Pattern
- Response formatting varies by query type
- Appropriate response structure selected at runtime

## Dependencies

**External Libraries:**
- `json`: Data serialization (built-in)
- `re`: Regular expressions for text processing (built-in)
- `difflib`: Fuzzy string matching (built-in)

**No external dependencies** - Uses only Python standard library for maximum portability.

## Extensibility

### Adding New Charts
1. Add chart entry to `CHARTS` list in `chart_knowledge_base.py`
2. Include all required metadata fields
3. Update category if new type introduced
4. Run tests to verify integration

### Customizing Analysis Logic
1. Modify scoring weights in `ChartQAEngine.rank_charts()`
2. Adjust intent detection patterns
3. Extend entity extraction rules

### Adding New Features
1. Chart comparison: Compare pros/cons of multiple charts
2. Visualization templates: Provide code examples
3. Performance metrics: Compare charts by rendering performance
4. Interactive filters: Filter recommendations by constraints

## Performance Considerations

### Optimization Strategies
- In-memory storage for quick lookups
- Cached search results for common queries
- Efficient string matching with difflib
- Lazy loading of detailed chart information

### Scalability
- Current implementation supports 30+ charts efficiently
- Linear O(n) search complexity
- Easily handles 100+ charts with minimal performance impact
- Consider indexing for 1000+ chart database

## Testing Architecture

### Test Organization
- **Unit Tests**: Individual component functionality
  - `test_chart_knowledge_base.py`: 21+ tests
  - `test_chart_qa_engine.py`: 30+ tests

### Test Coverage
- Chart data integrity and validation
- Query processing and analysis
- Ranking and scoring logic
- Edge cases and error handling
- Integration between components

## Security Considerations

- **Input Validation**: Sanitize user input to prevent injection attacks
- **Error Handling**: Graceful error messages without exposing internals
- **Data Privacy**: No user data persistence without consent
- **Safe Defaults**: Conservative recommendations when uncertain

## Future Enhancements

### Short-term
1. Advanced filtering options
2. Chart comparison functionality
3. Code generation for recommended charts
4. Performance benchmarking

### Medium-term
1. Machine learning-based relevance scoring
2. User feedback integration
3. Personalized recommendations
4. Integration with popular visualization libraries

### Long-term
1. Multi-language support
2. Real-time data analysis
3. Collaborative chart design
4. Advanced visualization patterns

## Deployment

### Requirements
- Python 3.8+
- Minimal dependencies (standard library only)
- ~5MB disk space for codebase

### Installation
```bash
clone repository
install dependencies: pip install -r requirements.txt
run system: python chart_main.py
```

## Documentation

- **README.md**: Project overview and quick start
- **TESTING.md**: Testing guide and procedures
- **EXAMPLES.md**: Usage examples and scenarios
- **ARCHITECTURE.md** (this file): System design details

---

**Last Updated:** December 2, 2025
**Version:** 1.0
**Status:** Active Development
