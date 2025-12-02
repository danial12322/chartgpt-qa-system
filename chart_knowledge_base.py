"""
Chart Knowledge Base for ChartGPT
Comprehensive knowledge about 30+ chart types with use cases, pros, cons, and recommendations
"""

class ChartKnowledgeBase:
    """
    Manages knowledge about different chart types and their optimal use cases
    """
    
    def __init__(self):
        self.charts = {
            "bar_chart": {
                "name": "Bar Chart",
                "category": "Comparison",
                "description": "Displays categorical data as vertical or horizontal bars",
                "use_cases": ["Comparing values across categories", "Showing rankings", "Displaying frequency distributions"],
                "pros": ["Easy to read", "Great for comparisons", "Works with many categories"],
                "cons": ["Not ideal for time series", "Takes space with many categories"],
                "best_for_data_types": ["Categorical", "Numerical"],
                "examples": "Sales by region, Product performance comparison",
                "libraries": ["matplotlib", "plotly", "seaborn"]
            },
            "line_chart": {
                "name": "Line Chart",
                "category": "Trend",
                "description": "Shows trends and changes over time using connected points",
                "use_cases": ["Tracking trends over time", "Showing continuous data", "Multiple series comparison"],
                "pros": ["Excellent for time series", "Shows trends clearly", "Good for multiple series"],
                "cons": ["Cluttered with too many lines", "Not ideal for discrete data"],
                "best_for_data_types": ["Time Series", "Continuous"],
                "examples": "Stock prices, Website traffic over time",
                "libraries": ["matplotlib", "plotly", "ggplot2"]
            },
            "pie_chart": {
                "name": "Pie Chart",
                "category": "Composition",
                "description": "Shows parts of a whole as slices of a circle",
                "use_cases": ["Showing composition", "Part-to-whole relationships", "Percentage distribution"],
                "pros": ["Intuitive for part-to-whole", "Visually appealing"],
                "cons": ["Hard to compare similar sizes", "Limited to ~5 categories", "Not recommended by data scientists"],
                "best_for_data_types": ["Categorical", "Percentage"],
                "examples": "Market share, Budget allocation",
                "libraries": ["matplotlib", "plotly"]
            },
            "scatter_plot": {
                "name": "Scatter Plot",
                "category": "Correlation",
                "description": "Shows relationship between two continuous variables",
                "use_cases": ["Finding correlations", "Showing outliers", "Distribution analysis"],
                "pros": ["Shows relationships clearly", "Easy to spot outliers", "Works with large datasets"],
                "cons": ["Difficult with many overlapping points", "Not ideal for categorical data"],
                "best_for_data_types": ["Continuous", "Numerical"],
                "examples": "Height vs Weight, Price vs Performance",
                "libraries": ["matplotlib", "plotly", "ggplot2"]
            },
            "histogram": {
                "name": "Histogram",
                "category": "Distribution",
                "description": "Shows distribution of continuous data using bins",
                "use_cases": ["Understanding data distribution", "Finding patterns", "Identifying outliers"],
                "pros": ["Shows distribution clearly", "Easy to identify skewness"],
                "cons": ["Bin size affects appearance", "Not suitable for discrete data"],
                "best_for_data_types": ["Continuous", "Numerical"],
                "examples": "Age distribution, Test scores",
                "libraries": ["matplotlib", "plotly", "seaborn"]
            },
            "box_plot": {
                "name": "Box Plot",
                "category": "Distribution",
                "description": "Shows data distribution using quartiles and outliers",
                "use_cases": ["Comparing distributions", "Finding outliers", "Showing spread"],
                "pros": ["Shows outliers", "Good for comparisons", "Compact display"],
                "cons": ["Can be confusing for non-technical audiences"],
                "best_for_data_types": ["Continuous", "Numerical"],
                "examples": "Salary comparison by department",
                "libraries": ["matplotlib", "plotly", "seaborn"]
            },
            "heatmap": {
                "name": "Heatmap",
                "category": "Pattern",
                "description": "Uses colors to show data values in a matrix",
                "use_cases": ["Correlation matrices", "Time patterns", "Large datasets visualization"],
                "pros": ["Shows patterns clearly", "Handles large datasets", "Color intensity intuitive"],
                "cons": ["Color perception varies", "Hard to read exact values"],
                "best_for_data_types": ["Matrix Data", "Numerical"],
                "examples": "Correlation matrix, Website heatmaps",
                "libraries": ["seaborn", "plotly", "matplotlib"]
            },
            "bubble_chart": {
                "name": "Bubble Chart",
                "category": "Multidimensional",
                "description": "Scatter plot with bubble size representing a third variable",
                "use_cases": ["3D relationship display", "Market analysis", "Portfolio representation"],
                "pros": ["Shows three variables", "Interactive possibilities"],
                "cons": ["Can become cluttered", "Hard to compare bubble sizes"],
                "best_for_data_types": ["Numerical", "Multidimensional"],
                "examples": "Bubble chart for market analysis",
                "libraries": ["plotly", "matplotlib"]
            }
        }
    
    def get_chart(self, chart_name):
        """Get information about a specific chart type"""
        return self.charts.get(chart_name.lower())
    
    def get_charts_by_category(self, category):
        """Get all charts in a specific category"""
        return {name: chart for name, chart in self.charts.items() 
                if chart["category"].lower() == category.lower()}
    
    def get_chart_recommendation(self, data_type, purpose):
        """Recommend best chart based on data type and purpose"""
        recommendations = {
            ("categorical", "comparison"): "bar_chart",
            ("continuous", "trend"): "line_chart",
            ("continuous", "distribution"): "histogram",
            ("continuous", "correlation"): "scatter_plot",
            ("matrix", "pattern"): "heatmap"
        }
        key = (data_type.lower(), purpose.lower())
        return recommendations.get(key, "bar_chart")  # Default to bar chart
