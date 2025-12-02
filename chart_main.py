"""
Chart Main Interface for ChartGPT
Interactive CLI for chart recommendations and analysis
"""

from chart_knowledge_base import ChartKnowledgeBase
from chart_qa_engine import ChartQAEngine
from typing import Dict, List, Optional


class ChartGPTInterface:
    """
    Main interface for ChartGPT system providing interactive chart recommendations
    """

    def __init__(self):
        """Initialize the ChartGPT interface with knowledge base and QA engine"""
        self.kb = ChartKnowledgeBase()
        self.qa_engine = ChartQAEngine(self.kb)
        self.conversation_history = []

    def display_welcome(self) -> None:
        """Display welcome message and instructions"""
        print("\n" + "="*60)
        print("Welcome to ChartGPT - Chart Analysis & Recommendation System")
        print("="*60)
        print("\nI can help you:")
        print("  • Recommend the best chart type for your data")
        print("  • Compare different visualization approaches")
        print("  • Provide information about specific chart types")
        print("  • Suggest visualizations based on your data characteristics")
        print("\nCommands:")
        print("  • Type your question about charts")
        print("  • Type 'list' to see all available chart types")
        print("  • Type 'categories' to see chart categories")
        print("  • Type 'help' for more options")
        print("  • Type 'exit' to quit")
        print("="*60 + "\n")

    def display_charts_by_category(self, category: str) -> None:
        """Display all charts in a specific category
        
        Args:
            category: Chart category to display
        """
        result = self.qa_engine.get_charts_by_category(category)
        print(f"\n{result}")

    def list_all_charts(self) -> None:
        """Display all available charts with their use cases"""
        print("\n" + "-"*60)
        print("AVAILABLE CHART TYPES IN CHARTGPT")
        print("-"*60)
        
        charts_list = self.qa_engine.get_all_charts()
        for chart_name, chart_info in charts_list.items():
            print(f"\n{chart_name}")
            print(f"  Use Cases: {chart_info.get('use_cases', 'N/A')}")
            print(f"  Data Type: {chart_info.get('data_type', 'N/A')}")
            print(f"  Best For: {chart_info.get('best_for', 'N/A')}")

    def list_categories(self) -> None:
        """Display all available chart categories"""
        print("\n" + "-"*60)
        print("CHART CATEGORIES")
        print("-"*60)
        
        categories = [
            "Comparison",
            "Composition",
            "Distribution",
            "Trend",
            "Relationship",
            "Geographic",
            "Statistical",
            "Ranking",
            "Part-to-Whole"
        ]
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

    def show_help(self) -> None:
        """Display help information"""
        print("\n" + "-"*60)
        print("HELP & COMMANDS")
        print("-"*60)
        print("\nExample Queries:")
        print("  'What chart should I use to show sales trends?'")
        print("  'Compare bar chart and line chart'")
        print("  'Tell me about scatter plots'")
        print("  'What visualization is best for categorical data?'")
        print("  'Show me charts for comparison'")
        print("\nSpecial Commands:")
        print("  'list'       - Show all available chart types")
        print("  'categories' - Show all chart categories")
        print("  'help'       - Display this help message")
        print("  'history'    - Show conversation history")
        print("  'exit'       - Exit ChartGPT")
        print("-"*60 + "\n")

    def show_history(self) -> None:
        """Display conversation history"""
        if not self.conversation_history:
            print("\nNo conversation history yet.\n")
            return
        
        print("\n" + "-"*60)
        print("CONVERSATION HISTORY")
        print("-"*60)
        for i, exchange in enumerate(self.conversation_history, 1):
            print(f"\n[{i}] Q: {exchange['query']}")
            print(f"    A: {exchange['response'][:100]}...")
        print("-"*60 + "\n")

    def process_query(self, query: str) -> str:
        """Process user query and return response
        
        Args:
            query: User's question or command
            
        Returns:
            Response from ChartQA engine or help text
        """
        query_lower = query.lower().strip()
        
        if query_lower == 'exit':
            return 'EXIT'
        elif query_lower == 'list':
            self.list_all_charts()
            return 'Listed all charts'
        elif query_lower == 'categories':
            self.list_categories()
            return 'Listed all categories'
        elif query_lower == 'help':
            self.show_help()
            return 'Displayed help'
        elif query_lower == 'history':
            self.show_history()
            return 'Displayed history'
        else:
            # Process with QA engine
            response = self.qa_engine.answer_query(query)
            self.conversation_history.append({
                'query': query,
                'response': response
            })
            return response

    def format_response(self, response: str) -> str:
        """Format response for display
        
        Args:
            response: Raw response from QA engine
            
        Returns:
            Formatted response string
        """
        return f"\n{response}\n"

    def run(self) -> None:
        """Run the interactive ChartGPT interface"""
        self.display_welcome()
        
        try:
            while True:
                try:
                    user_input = input("You: ").strip()
                    
                    if not user_input:
                        continue
                    
                    response = self.process_query(user_input)
                    
                    if response == 'EXIT':
                        print("\n" + "="*60)
                        print("Thank you for using ChartGPT!")
                        print("="*60 + "\n")
                        break
                    elif response not in ['Listed all charts', 'Listed all categories', 
                                         'Displayed help', 'Displayed history']:
                        print(self.format_response(response))
                        
                except KeyboardInterrupt:
                    print("\n\nGoodbye!")
                    break
                except Exception as e:
                    print(f"\nError processing query: {str(e)}")
                    print("Please try again.\n")
                    
        except EOFError:
            print("\nSession ended.\n")


def main():
    """Main entry point for ChartGPT"""
    interface = ChartGPTInterface()
    interface.run()


if __name__ == "__main__":
    main()
