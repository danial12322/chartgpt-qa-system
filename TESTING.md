# Testing Guide for ChartGPT

Comprehensive guide for running, writing, and understanding tests in the ChartGPT system.

## 🧪 Overview

ChartGPT includes comprehensive unit and integration tests for both the knowledge base and QA engine components. All tests use Python's built-in `unittest` framework.

## 📦 Test Files

### 1. test_chart_knowledge_base.py
Tests for the ChartKnowledgeBase class covering:
- Knowledge base initialization
- Chart data structure validation
- Category validation
- Chart retrieval (exact, case-insensitive, partial)
- Metadata field validation (descriptions, use cases, pros, cons, libraries)
- Data type validation
- Essential chart existence

**Test Count:** 21 unit tests + integration tests

### 2. test_chart_qa_engine.py  
Tests for the ChartQAEngine class covering:
- QA engine initialization
- Keyword extraction and stopword removal
- Chart matching (exact, case-insensitive, partial)
- Query answering for different intent types (recommendation, comparison, information)
- Chart recommendations by data type and purpose
- Chart information retrieval
- Response template validation
- Error handling and edge cases

**Test Count:** 30+ unit tests + integration tests

## 🚀 Running Tests

### Run All Tests
```bash
python -m unittest discover -s . -p "test_*.py" -v
```

### Run Specific Test File
```bash
# Test knowledge base
python -m unittest test_chart_knowledge_base -v

# Test QA engine
python -m unittest test_chart_qa_engine -v
```

### Run Specific Test Class
```bash
python -m unittest test_chart_knowledge_base.TestChartKnowledgeBase -v
python -m unittest test_chart_qa_engine.TestChartQAEngineIntegration -v
```

### Run Specific Test Method
```bash
python -m unittest test_chart_knowledge_base.TestChartKnowledgeBase.test_chart_count -v
python -m unittest test_chart_qa_engine.TestChartQAEngine.test_answer_recommendation_query -v
```

## 📊 Test Categories

### Unit Tests
Test individual methods and functions in isolation.

**ChartKnowledgeBase Unit Tests:**
- `test_knowledge_base_initialization()` - Verify KB initializes properly
- `test_chart_count()` - Verify minimum chart count (30+)
- `test_chart_data_structure()` - Verify all required fields present
- `test_chart_categories()` - Verify valid category assignments
- `test_get_chart_*()` - Various chart retrieval tests
- `test_chart_*_not_empty()` - Validate metadata is populated

**ChartQAEngine Unit Tests:**
- `test_qa_engine_initialization()` - Verify QA engine initializes
- `test_extract_keywords_*()` - Keyword extraction validation
- `test_find_chart_match_*()` - Chart matching tests
- `test_answer_*_query()` - Response generation for different queries
- `test_get_recommendation_*()` - Chart recommendation tests
- `test_response_templates_exist()` - Template validation

### Integration Tests
Test how components work together.

**ChartKnowledgeBase Integration Tests:**
- `test_knowledge_base_consistency()` - Verify consistent data retrieval
- `test_category_chart_count_consistency()` - Verify chart counts across categories

**ChartQAEngine Integration Tests:**
- `test_query_to_recommendation_flow()` - Complete user query workflow
- `test_multiple_queries_consistency()` - Response consistency
- `test_qa_engine_error_handling()` - Edge case handling

## ✅ Test Coverage

### ChartKnowledgeBase Coverage
- ✅ Initialization and setup
- ✅ Data structure validation
- ✅ Chart retrieval methods
- ✅ Category filtering
- ✅ Metadata completeness
- ✅ Data type validation
- ✅ Essential chart existence

### ChartQAEngine Coverage  
- ✅ Initialization and setup
- ✅ Keyword extraction
- ✅ Chart matching algorithms
- ✅ Query type recognition
- ✅ Recommendation generation
- ✅ Response formatting
- ✅ Error handling
- ✅ Edge case management

## 🔍 Understanding Test Results

### Success Output
```
Ran 21 tests in 0.123s

OK
```

### Failure Example
```
FAIL: test_chart_count (test_chart_knowledge_base.TestChartKnowledgeBase)
Test that knowledge base contains expected number of charts
----------------------------------------------------------------------
AssertionError: 25 not >= 30
```

### Error Example  
```
ERROR: test_extract_keywords (test_chart_qa_engine.TestChartQAEngine)
Test keyword extraction removes common stopwords
----------------------------------------------------------------------
AttributeError: 'ChartQAEngine' object has no attribute 'extract_keywords'
```

## 🛠️ Common Test Debugging

### Issue: Missing Test File
**Solution:** Ensure test files are in repository root with `test_*.py` naming

### Issue: Import Errors
**Solution:** Run tests from repository root:
```bash
cd chartgpt-qa-system
python -m unittest discover
```

### Issue: KeyError in Tests
**Solution:** Verify knowledge_base.py has required fields in chart dictionary

### Issue: Assertion Failures
**Solution:** Check test expectations match actual implementation

## 📝 Writing New Tests

### Template for Unit Test
```python
def test_feature_name(self):
    """Test description of what is being tested"""
    # Arrange: Set up test data
    test_input = "sample query"
    
    # Act: Call the method being tested
    result = self.qa_engine.some_method(test_input)
    
    # Assert: Verify the result
    self.assertIsNotNone(result)
    self.assertTrue(len(result) > 0)
```

### Template for Integration Test
```python
def test_complete_workflow(self):
    """Test complete user workflow"""
    # Set up components
    kb = ChartKnowledgeBase()
    qa_engine = ChartQAEngine(kb)
    
    # Execute complete workflow
    user_query = "What chart for trends?"
    response = qa_engine.answer_query(user_query)
    
    # Verify results
    self.assertIsNotNone(response)
    self.assertTrue(isinstance(response, str))
```

## 🔄 Continuous Integration

To set up CI/CD testing:

1. Create `.github/workflows/tests.yml`
2. Configure GitHub Actions to run:
   ```yaml
   python -m unittest discover -s . -p "test_*.py" -v
   ```
3. Tests run automatically on push/pull request

## 📈 Test Metrics

**Current Test Suite:**
- Total Tests: 50+
- Knowledge Base Tests: 21+
- QA Engine Tests: 30+
- Integration Tests: 5+
- Code Coverage: Comprehensive

## ✨ Best Practices

1. **Run tests before committing:**
   ```bash
   python -m unittest discover -v
   ```

2. **Write tests for new features:**
   - Unit test for individual functionality
   - Integration test for workflows

3. **Keep tests focused:**
   - One assertion per test when possible
   - Clear test names describing what is tested

4. **Use descriptive error messages:**
   ```python
   self.assertEqual(chart['category'], 'Comparison',
       f"Chart '{chart_name}' has wrong category")
   ```

5. **Test edge cases:**
   - Empty strings
   - None values
   - Non-existent items
   - Case variations

## 🐛 Troubleshooting

### Tests Pass Locally But Fail in CI
- Verify all imports are correct
- Check for hardcoded paths
- Ensure test isolation (no shared state)

### Random Test Failures
- Check for race conditions
- Verify setUp() and tearDown() methods
- Ensure tests don't depend on execution order

### Slow Test Execution
- Profile test code with cProfile
- Consider mocking expensive operations
- Break large tests into smaller units

## 📚 Additional Resources

- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Testing best practices](https://docs.python.org/3/library/unittest.html#best-practices)
- Project README for system overview
- Individual module docstrings for API details

---

**Last Updated:** December 2, 2025
**Test Framework:** Python unittest
**Python Version:** 3.8+
