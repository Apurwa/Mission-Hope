# app.py - Main Chatbot Application

import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

def create_chatbot(anthropic_api_key):
    """
    Create and return a compiled LangGraph chatbot using Claude
    """
    # Initialize the LLM
    llm = ChatAnthropic(
        anthropic_api_key=anthropic_api_key,
        model_name="claude-3-5-sonnet-latest"
    )
    
    # Create the graph builder
    graph_builder = StateGraph(State)
    
    # Define the chatbot node function
    def chatbot(state: State):
        return {"messages": llm.invoke(state['messages'])}
    
    # Add node and edges
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    
    # Compile the graph
    return graph_builder.compile()

def run_chat_loop(graph, display_visualization=False):
    """
    Run an interactive chat loop with the provided graph
    """
    # Optionally display graph visualization
    if display_visualization:
        try:
            from IPython.display import Image, display
            display(Image(graph.get_graph().draw_mermaid_png()))
        except Exception:
            print("Visualization not available outside of notebook environment")
    
    # Chat loop
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "q"]:
            print("Good Bye")
            break
            
        for event in graph.stream({'messages': ("user", user_input)}):
            for value in event.values():
                print("Assistant:", value["messages"].content)

if __name__ == "__main__":
    # Check for environment variables
    anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        anthropic_api_key = input("Please enter your Anthropic API key: ")
        os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key
    
    # Set up LangSmith tracing if available
    langsmith_api_key = os.environ.get("LANGCHAIN_API_KEY")
    if langsmith_api_key:
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "CourseLanggraph"
    
    # Create and run the chatbot
    graph = create_chatbot(anthropic_api_key)
    run_chat_loop(graph)