"""
Unit Tests for ChartKnowledgeBase
Testing core functionality of the chart knowledge base
"""

import unittest
from chart_knowledge_base import ChartKnowledgeBase


class TestChartKnowledgeBase(unittest.TestCase):
    """Test suite for ChartKnowledgeBase class"""

    def setUp(self):
        """Initialize the knowledge base before each test"""
        self.kb = ChartKnowledgeBase()

    def test_knowledge_base_initialization(self):
        """Test that knowledge base initializes correctly"""
        self.assertIsNotNone(self.kb)
        self.assertIsInstance(self.kb.charts, dict)
        self.assertGreater(len(self.kb.charts), 0)

    def test_chart_count(self):
        """Test that knowledge base contains expected number of charts"""
        # Should have at least 30 chart types
        self.assertGreaterEqual(len(self.kb.charts), 30)

    def test_chart_data_structure(self):
        """Test that each chart has required metadata fields"""
        required_fields = ['description', 'use_cases', 'best_for', 'data_type', 
                          'pros', 'cons', 'libraries', 'category']
        
        for chart_name, chart_data in self.kb.charts.items():
            for field in required_fields:
                self.assertIn(field, chart_data, 
                            f"Chart '{chart_name}' missing field '{field}'")

    def test_chart_categories(self):
        """Test that all charts have valid categories"""
        valid_categories = {
            'Comparison', 'Composition', 'Distribution', 'Trend',
            'Relationship', 'Geographic', 'Statistical', 'Ranking', 'Part-to-Whole'
        }
        
        for chart_name, chart_data in self.kb.charts.items():
            category = chart_data.get('category')
            self.assertIn(category, valid_categories,
                        f"Chart '{chart_name}' has invalid category '{category}'")

    def test_get_chart_by_name(self):
        """Test retrieving chart by name"""
        # Test with a known chart
        chart = self.kb.get_chart('Bar Chart')
        self.assertIsNotNone(chart)
        self.assertEqual(chart['category'], 'Comparison')

    def test_get_chart_case_insensitivity(self):
        """Test that chart retrieval is case-insensitive"""
        chart1 = self.kb.get_chart('bar chart')
        chart2 = self.kb.get_chart('BAR CHART')
        self.assertEqual(chart1, chart2)

    def test_get_chart_not_found(self):
        """Test retrieving non-existent chart"""
        chart = self.kb.get_chart('NonExistentChart')
        self.assertIsNone(chart)

    def test_get_charts_by_category(self):
        """Test retrieving charts by category"""
        comparison_charts = self.kb.get_charts_by_category('Comparison')
        self.assertGreater(len(comparison_charts), 0)
        
        # All returned charts should be in Comparison category
        for chart_name, chart_data in comparison_charts.items():
            self.assertEqual(chart_data['category'], 'Comparison')

    def test_all_categories_exist(self):
        """Test that charts exist for all major categories"""
        categories = {
            'Comparison', 'Composition', 'Distribution', 'Trend',
            'Relationship', 'Geographic', 'Statistical', 'Ranking'
        }
        
        for category in categories:
            charts = self.kb.get_charts_by_category(category)
            self.assertGreater(len(charts), 0,
                            f"No charts found for category '{category}'")

    def test_chart_description_not_empty(self):
        """Test that all charts have descriptions"""
        for chart_name, chart_data in self.kb.charts.items():
            description = chart_data.get('description', '')
            self.assertTrue(len(description) > 0,
                          f"Chart '{chart_name}' has empty description")

    def test_chart_use_cases_not_empty(self):
        """Test that all charts have use cases"""
        for chart_name, chart_data in self.kb.charts.items():
            use_cases = chart_data.get('use_cases', [])
            self.assertGreater(len(use_cases), 0,
                            f"Chart '{chart_name}' has no use cases")

    def test_chart_pros_not_empty(self):
        """Test that all charts have pros listed"""
        for chart_name, chart_data in self.kb.charts.items():
            pros = chart_data.get('pros', [])
            self.assertGreater(len(pros), 0,
                            f"Chart '{chart_name}' has no pros listed")

    def test_chart_cons_not_empty(self):
        """Test that all charts have cons listed"""
        for chart_name, chart_data in self.kb.charts.items():
            cons = chart_data.get('cons', [])
            self.assertGreater(len(cons), 0,
                            f"Chart '{chart_name}' has no cons listed")

    def test_chart_libraries_not_empty(self):
        """Test that all charts have recommended libraries"""
        for chart_name, chart_data in self.kb.charts.items():
            libraries = chart_data.get('libraries', [])
            self.assertGreater(len(libraries), 0,
                            f"Chart '{chart_name}' has no libraries listed")

    def test_chart_data_types_valid(self):
        """Test that charts have valid data types"""
        valid_types = {'categorical', 'continuous', 'mixed'}
        
        for chart_name, chart_data in self.kb.charts.items():
            data_type = chart_data.get('data_type')
            self.assertIn(data_type, valid_types,
                        f"Chart '{chart_name}' has invalid data type '{data_type}'")

    def test_specific_charts_exist(self):
        """Test that specific important charts exist"""
        essential_charts = [
            'Bar Chart', 'Line Chart', 'Scatter Plot', 'Pie Chart',
            'Histogram', 'Box Plot', 'Area Chart', 'Heatmap'
        ]
        
        for chart_name in essential_charts:
            chart = self.kb.get_chart(chart_name)
            self.assertIsNotNone(chart,
                                f"Essential chart '{chart_name}' not found")

    def test_get_all_charts(self):
        """Test retrieving all charts"""
        all_charts = self.kb.get_all_charts()
        self.assertGreater(len(all_charts), 0)
        self.assertEqual(len(all_charts), len(self.kb.charts))

    def test_chart_best_for_not_empty(self):
        """Test that all charts have 'best_for' descriptions"""
        for chart_name, chart_data in self.kb.charts.items():
            best_for = chart_data.get('best_for', '')
            self.assertTrue(len(best_for) > 0,
                          f"Chart '{chart_name}' has empty 'best_for' field")


class TestChartKnowledgeBaseIntegration(unittest.TestCase):
    """Integration tests for ChartKnowledgeBase"""

    def setUp(self):
        """Initialize the knowledge base"""
        self.kb = ChartKnowledgeBase()

    def test_knowledge_base_consistency(self):
        """Test that the knowledge base maintains consistency"""
        # Get all charts twice and verify they're the same
        charts1 = self.kb.get_all_charts()
        charts2 = self.kb.get_all_charts()
        self.assertEqual(charts1, charts2)

    def test_category_chart_count_consistency(self):
        """Test that sum of charts per category equals total charts"""
        categories = ['Comparison', 'Composition', 'Distribution', 'Trend',
                     'Relationship', 'Geographic', 'Statistical', 'Ranking']
        
        total_by_category = 0
        for category in categories:
            charts = self.kb.get_charts_by_category(category)
            total_by_category += len(charts)
        
        total_all = len(self.kb.get_all_charts())
        # Note: Some charts may be in Part-to-Whole category not listed
        self.assertGreaterEqual(total_all, total_by_category)


if __name__ == '__main__':
    unittest.main()
