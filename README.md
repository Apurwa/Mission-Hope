# LangGraph Chatbot

A simple conversational AI chatbot built with LangGraph, LangChain, and Claude AI model from Anthropic.

## Overview

This project implements a basic chatbot using LangGraph for workflow management and the Claude 3.5 Sonnet model from Anthropic as the language model. The chatbot processes user input and generates conversational responses in a streaming manner.

## Features

- Simple and straightforward chat interface
- State management with LangGraph
- Integration with Claude 3.5 Sonnet
- Optional LangSmith tracing for monitoring and debugging

## Prerequisites

- Python 3.8+
- An Anthropic API key
- (Optional) A LangSmith API key for tracing

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/langgraph-chatbot.git
cd langgraph-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (or you will be prompted for them when running):
```bash
export ANTHROPIC_API_KEY="your_anthropic_api_key"
export LANGCHAIN_API_KEY="your_langsmith_api_key"  # Optional
export LANGCHAIN_TRACING_V2="true"  # Optional
export LANGCHAIN_PROJECT="CourseLanggraph"  # Optional
```

## Usage

Run the chatbot:
```bash
python app.py
```

Type your messages at the prompt. Type "quit" or "q" to exit the conversation.

## Project Structure

- `app.py`: Main application file containing the chatbot implementation
- `requirements.txt`: List of required Python packages
- `README.md`: This documentation file

## Extending the Chatbot

To extend this chatbot with additional functionality:

1. Modify the `State` class to include additional state information
2. Add new nodes to the graph for different processing steps
3. Update the graph's edges to represent the new workflow

## Credits

Based on LangGraph tutorial: https://www.youtube.com/watch?v=gqvFmK7LpDo

## License

MIT