# MCP (Multi-Client Protocol) Projects

This repository contains a collection of projects implementing various Multi-Client Protocol (MCP) services and clients. Each project serves a specific purpose in the MCP ecosystem, ranging from sentiment analysis to AI-powered chat interfaces.

## Project Structure

```
.
├── hello-world/           # Basic Node.js examples and utilities
├── mcp-client-node/      # Node.js MCP client implementation
├── mcp-sentiment/        # Sentiment analysis service
└── mcp-wiki/            # AI-powered chat and wiki service
```

## Projects Overview

### 1. MCP Sentiment Analysis Service (`mcp-sentiment/`)
A sentiment analysis service built with Python and Gradio that provides text sentiment analysis capabilities.

**Features:**
- Real-time sentiment analysis using TextBlob
- Web interface powered by Gradio
- Provides polarity, subjectivity, and sentiment assessment
- Deployable as a Hugging Face Space

**Tech Stack:**
- Python
- Gradio
- TextBlob
- Hugging Face Spaces

### 2. MCP Wiki Service (`mcp-wiki/`)
An AI-powered chat and wiki service that leverages Ollama for natural language processing.

**Features:**
- Interactive chat interface using Streamlit
- Integration with Ollama for AI model inference
- Support for DeepSeek-R1 model
- Real-time chat history management
- Web-based interface

**Tech Stack:**
- Python
- Streamlit
- Ollama
- Gemma 3 4B model

### 3. MCP Client Node (`mcp-client-node/`)
A Node.js implementation of the MCP client for interacting with MCP services.

**Features:**
- Node.js-based client implementation
- Integration with MCP services
- Custom agent implementation

**Tech Stack:**
- Node.js
- Custom agent framework

### 4. Hello World (`hello-world/`)
A collection of basic Node.js examples and utilities.

**Contents:**
- Basic Node.js examples
- Utility functions
- Math operations
- File operations

## Getting Started

### Prerequisites
- Node.js (for Node.js projects)
- Python 3.x (for Python projects)
- Ollama (for MCP Wiki service)
- Virtual environment (recommended for Python projects)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Node-js
```

2. Install dependencies for each project:

For Node.js projects:
```bash
cd mcp-client-node
npm install
```

For Python projects:
```bash
# MCP Sentiment
cd mcp-sentiment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# MCP Wiki
cd mcp-wiki
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Services

### MCP Sentiment Service
```bash
cd mcp-sentiment
python app.py
```

### MCP Wiki Service
```bash
cd mcp-wiki
streamlit run streamlit_new.py
```

### MCP Client Node
```bash
cd mcp-client-node
node client.js
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- TextBlob for sentiment analysis capabilities
- Ollama for AI model hosting
- Streamlit and Gradio for web interfaces
- Node.js community for client implementation support 