# Code for Exercise 1: Implementing a Simple State Graph
from langgraph.graph import StateGraph, START, END 
from typing import Dict, List, TypedDict
from IPython.display import Image, display

# Define the State Variable. 
class AgentState(TypedDict):
    name: str
    message: str

# Define greeting_node 
def greeting_node(state: AgentState) -> AgentState:
    """Greet the user and ask for the state variable values"""
    # Print a greeting message to inform the currently running node
    print("Inside the greeting node.")
    # Priting the current state for debugging purposes
    print(f"Current state: {state}")
    # Setting up the message state variable
    state['message'] = f"{state['name']}, you're doing an amazing job learning LangGraph!"
    # Priting the updated state for debugging purposes
    print(f"Updated state: {state}")
    return state

# Define the state graph
graph = StateGraph(AgentState)
graph.add_node("greeting_node", greeting_node)
graph.add_edge(START, "greeting_node")
graph.add_edge("greeting_node", END)
# Compile the Graph
app = graph.compile()

