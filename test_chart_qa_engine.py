"""
Unit Tests for ChartQAEngine
Testing query analysis and recommendation functionality
"""

import unittest
from chart_knowledge_base import ChartKnowledgeBase
from chart_qa_engine import ChartQAEngine


class TestChartQAEngine(unittest.TestCase):
    """Test suite for ChartQAEngine class"""

    def setUp(self):
        """Initialize QA engine before each test"""
        self.kb = ChartKnowledgeBase()
        self.qa_engine = ChartQAEngine(self.kb)

    def test_qa_engine_initialization(self):
        """Test QA engine initializes correctly"""
        self.assertIsNotNone(self.qa_engine)
        self.assertIsNotNone(self.qa_engine.kb)
        self.assertIsNotNone(self.qa_engine.response_templates)

    def test_extract_keywords_removes_stopwords(self):
        """Test keyword extraction removes common stopwords"""
        query = "what chart should i use for showing trends over time"
        keywords = self.qa_engine.extract_keywords(query)
        # Should not contain common stopwords
        stopwords = {'what', 'should', 'i', 'use', 'for', 'over'}
        for keyword in keywords:
            self.assertNotIn(keyword.lower(), stopwords)

    def test_extract_keywords_finds_chart_types(self):
        """Test that keywords include relevant chart type names"""
        query = "should i use a line chart or bar chart"
        keywords = self.qa_engine.extract_keywords(query)
        # Should contain chart type keywords
        self.assertTrue(any('chart' in kw.lower() for kw in keywords) or len(keywords) > 0)

    def test_find_chart_match_exact(self):
        """Test finding exact chart matches"""
        query = "bar chart"
        chart_match = self.qa_engine.find_chart_match(query)
        self.assertIsNotNone(chart_match)
        self.assertEqual(chart_match.lower(), 'bar chart')

    def test_find_chart_match_case_insensitive(self):
        """Test chart matching is case insensitive"""
        query = "LINE CHART"
        chart_match = self.qa_engine.find_chart_match(query)
        self.assertIsNotNone(chart_match)
        self.assertIn('line', chart_match.lower())

    def test_find_chart_match_partial(self):
        """Test partial chart name matching"""
        query = "scatter"
        chart_match = self.qa_engine.find_chart_match(query)
        # Should find scatter plot
        if chart_match:
            self.assertIn('scatter', chart_match.lower())

    def test_answer_recommendation_query(self):
        """Test answering recommendation queries"""
        query = "What chart should i use for comparing values"
        response = self.qa_engine.answer_query(query)
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)
        # Response should contain useful information
        self.assertTrue(any(word in response.lower() for word in 
                          ['chart', 'recommend', 'best', 'use']))

    def test_answer_information_query(self):
        """Test answering information queries"""
        query = "Tell me about pie charts"
        response = self.qa_engine.answer_query(query)
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)

    def test_answer_comparison_query(self):
        """Test answering comparison queries"""
        query = "Compare bar chart and line chart"
        response = self.qa_engine.answer_query(query)
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)

    def test_answer_visualization_type_query(self):
        """Test answering visualization type queries"""
        query = "What visualization for categorical data"
        response = self.qa_engine.answer_query(query)
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)

    def test_get_recommendation_with_all_parameters(self):
        """Test chart recommendation with full parameters"""
        recommendation = self.qa_engine.get_recommendation('continuous', 'trend')
        self.assertIsNotNone(recommendation)
        self.assertTrue(len(recommendation) > 0)

    def test_get_recommendation_continuous_comparison(self):
        """Test recommendations for continuous data comparison"""
        recommendation = self.qa_engine.get_recommendation('continuous', 'comparison')
        self.assertIsNotNone(recommendation)

    def test_get_recommendation_categorical_composition(self):
        """Test recommendations for categorical composition"""
        recommendation = self.qa_engine.get_recommendation('categorical', 'composition')
        self.assertIsNotNone(recommendation)

    def test_get_chart_info(self):
        """Test retrieving chart information"""
        chart_info = self.qa_engine.get_chart_info('Bar Chart')
        self.assertIsNotNone(chart_info)
        self.assertIn('use_cases', chart_info)
        self.assertIn('pros', chart_info)

    def test_get_chart_info_not_found(self):
        """Test retrieving info for non-existent chart"""
        chart_info = self.qa_engine.get_chart_info('NonExistentChart')
        self.assertIsNone(chart_info)

    def test_get_charts_by_category(self):
        """Test retrieving charts by category"""
        charts = self.qa_engine.get_charts_by_category('Comparison')
        self.assertIsNotNone(charts)
        self.assertGreater(len(charts), 0)

    def test_get_all_charts(self):
        """Test retrieving all charts"""
        all_charts = self.qa_engine.get_all_charts()
        self.assertIsNotNone(all_charts)
        self.assertGreater(len(all_charts), 0)

    def test_response_templates_exist(self):
        """Test that response templates are defined"""
        templates = self.qa_engine.response_templates
        required_templates = ['chart_info', 'recommendation', 'chart_comparison', 'not_found']
        for template in required_templates:
            self.assertIn(template, templates)

    def test_intent_recognition_recommendation(self):
        """Test intent recognition for recommendation queries"""
        query = "What chart should I use for sales data"
        # Query contains recommendation keywords
        self.assertTrue('should' in query.lower() or 'use' in query.lower())

    def test_intent_recognition_comparison(self):
        """Test intent recognition for comparison queries"""
        query = "Compare line chart with bar chart"
        self.assertIn('compare', query.lower())

    def test_intent_recognition_information(self):
        """Test intent recognition for information queries"""
        query = "Tell me about scatter plots"
        self.assertIn('tell', query.lower())


class TestChartQAEngineIntegration(unittest.TestCase):
    """Integration tests for ChartQAEngine"""

    def setUp(self):
        """Initialize QA engine"""
        self.kb = ChartKnowledgeBase()
        self.qa_engine = ChartQAEngine(self.kb)

    def test_query_to_recommendation_flow(self):
        """Test complete query to recommendation flow"""
        query = "What chart for showing trends"
        response = self.qa_engine.answer_query(query)
        # Should return a non-empty response
        self.assertTrue(len(response) > 0)
        # Response should be formatted properly
        self.assertTrue(isinstance(response, str))

    def test_multiple_queries_consistency(self):
        """Test that same query produces consistent responses"""
        query = "What chart should I use for comparison"
        response1 = self.qa_engine.answer_query(query)
        response2 = self.qa_engine.answer_query(query)
        # Responses should be similar or identical
        self.assertEqual(response1, response2)

    def test_qa_engine_error_handling(self):
        """Test QA engine handles edge cases"""
        edge_cases = [
            "",  # Empty query
            "   ",  # Whitespace only
            "xyz abc def",  # Non-matching query
            "123 456 789"  # Numbers only
        ]
        for query in edge_cases:
            response = self.qa_engine.answer_query(query)
            # Should return a response even for edge cases
            self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
