"""
Chart QA Engine for ChartGPT
Query analysis and intelligent chart recommendations
"""

import re
from typing import Dict, List, Tuple, Optional
from chart_knowledge_base import ChartKnowledgeBase

class ChartQAEngine:
    """
    Question Answering Engine specialized for chart-related queries
    """
    
    def __init__(self, knowledge_base: ChartKnowledgeBase):
        self.kb = knowledge_base
        self.response_templates = {
            "chart_info": "The {chart_name} is ideal for {use_case}. {description} Pros: {pros}. Cons: {cons}.",
            "chart_recommendation": "Based on your data type ({data_type}) and purpose ({purpose}), I recommend using a {chart_name} chart.",
            "chart_comparison": "Both {chart1} and {chart2} work for comparing data, but {chart1} is better for {comparison_reason}.",
            "not_found": "I don't have specific information about that chart type. Ask about common charts like bar, line, pie, or scatter plots."
        }
    
    def extract_keywords(self, query: str) -> List[str]:
        """Extract meaningful keywords from user query"""
        words = query.lower().split()
        stop_words = {'what', 'is', 'the', 'a', 'an', 'about', 'tell', 'me', 'how', 'which', 'best', 'use', 'for', 'should', 'can'}
        return [w for w in words if w not in stop_words and len(w) > 2]
    
    def identify_intent(self, query: str) -> str:
        """Identify user intent from query"""
        query_lower = query.lower()
        
        if re.search(r'recommend|suggest|best|which|should', query_lower):
            return 'recommendation'
        elif re.search(r'compare|difference|vs|versus|better', query_lower):
            return 'comparison'
        elif re.search(r'what|how|tell|info|about', query_lower):
            return 'information'
        elif re.search(r'visualize|show|display|represent|plot', query_lower):
            return 'visualization_type'
        else:
            return 'general'
    
    def find_chart_match(self, keywords: List[str]) -> Optional[str]:
        """Find matching chart from keywords"""
        charts = self.kb.get_all_charts()
        for keyword in keywords:
            for chart_id, chart_info in charts.items():
                if keyword in chart_id.replace('_', '') or keyword in chart_info['name'].lower():
                    return chart_id
        return None
    
    def get_chart_info(self, chart_id: str) -> str:
        """Get formatted information about a chart"""
        chart = self.kb.get_chart(chart_id)
        if not chart:
            return self.response_templates['not_found']
        
        return self.response_templates['chart_info'].format(
            chart_name=chart['name'],
            use_case=chart['use_cases'][0],
            description=chart['description'],
            pros=', '.join(chart['pros'][:2]),
            cons=', '.join(chart['cons'][:2])
        )
    
    def get_recommendation(self, data_type: str, purpose: str) -> str:
        """Get chart recommendation based on data type and purpose"""
        recommended_chart_id = self.kb.get_chart_recommendation(data_type, purpose)
        chart = self.kb.get_chart(recommended_chart_id)
        
        return self.response_templates['chart_recommendation'].format(
            data_type=data_type,
            purpose=purpose,
            chart_name=chart['name']
        )
    
    def analyze_query(self, query: str) -> str:
        """Main method to analyze query and provide response"""
        if not query or len(query.strip()) == 0:
            return "Please ask me about chart types, recommendations, or visualization techniques."
        
        intent = self.identify_intent(query)
        keywords = self.extract_keywords(query)
        
        if intent == 'recommendation':
            if 'categorical' in query.lower() or 'categories' in query.lower():
                return self.get_recommendation('categorical', 'comparison')
            elif 'time' in query.lower() or 'trend' in query.lower():
                return self.get_recommendation('continuous', 'trend')
            elif 'correlation' in query.lower():
                return self.get_recommendation('continuous', 'correlation')
            else:
                return "To recommend a chart, tell me: (1) Your data type (categorical/continuous), (2) Your purpose (comparison/trend/correlation)"
        
        elif intent == 'information':
            chart_match = self.find_chart_match(keywords)
            if chart_match:
                return self.get_chart_info(chart_match)
        
        elif intent == 'visualization_type':
            chart_match = self.find_chart_match(keywords)
            if chart_match:
                chart = self.kb.get_chart(chart_match)
                return f"Use a {chart['name']} for {chart['use_cases'][0]}. Best libraries: {', '.join(chart['libraries'])}"
        
        return self.response_templates['not_found']
    
    def get_charts_by_category(self, category: str) -> str:
        """Get all charts in a category"""
        charts = self.kb.get_charts_by_category(category)
        if not charts:
            return f"No charts found for category: {category}"
        
        chart_list = ', '.join([info['name'] for info in charts.values()])
        return f"Charts for {category}: {chart_list}"
