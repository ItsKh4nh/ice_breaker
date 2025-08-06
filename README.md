# 🧊 Ice Breaker

**An intelligent ice breaker generator powered by LangChain and social media intelligence**

![Ice Breaker Demo](/static/demo.gif)

[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-brightgreen)](https://langchain.com/)
[![Tavily](https://img.shields.io/badge/Tavily-🔍-orange)](https://app.tavily.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-red)](https://flask.palletsprojects.com/)

## 🎯 Overview

**Ice Breaker** is a sophisticated AI-powered web application that creates personalized ice breakers by analyzing LinkedIn profiles. This project serves as a comprehensive learning tool for mastering LangChain while building a practical Generative AI application that combines professional profile intelligence with natural language generation.

### ✨ Key Features

**AI Pipeline Flow:**

1. 🔍 **Profile Discovery**: Intelligent lookup and discovery of LinkedIn profiles
2. 🌐 **Data Extraction**: Advanced web scraping of social media data
3. 🧠 **AI Analysis**: Deep analysis of personality, interests, and professional background
4. ✍️ **Ice Breaker Generation**: Context-aware creation of personalized conversation starters
5. 🎨 **Smart Formatting**: Professional presentation of generated content
6. 💬 **Interactive Interface**: User-friendly web interface powered by Flask
7. 🚀 **Real-time Processing**: Fast end-to-end pipeline from profile input to ice breaker output


_Ice Breaker intelligently analyzes social profiles to craft tailored, engaging conversation starters that spark meaningful connections._

## 🛠️ Tech Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| 🖥️ **Frontend** | Flask | Web application framework |
| 🧠 **AI Framework** | LangChain 🦜🔗 | Orchestrates the AI pipeline |
| 🔍 **LinkedIn Data** | Scrapin.io | Professional profile scraping |
| 🌐 **Web Search** | Tavily | Enhanced profile discovery |
| 🤖 **LLM** | OpenAI GPT | Powers the conversation generation |
| 📊 **Monitoring** | LangSmith | Optional tracing and debugging |
| 🐍 **Backend** | Python 3.10+ | Core application logic |

## 🚀 Quick Start

### Prerequisites

* Python 3.10 or higher
* OpenAI API key
* Scrapin.io API key
* Tavily API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ItsKh4nh/ice_breaker.git
   cd ice_breaker
   ```

2. **Set up environment variables**
   
   Create a `.env` file in the root directory with your API keys (see [Environment Variables](#-environment-variables) section for details).

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
pytest .
```

## 💰 API Usage

> - **[Scrapin.io](https://app.scrapin.io/auth/register)** 💼 - LinkedIn data scraping  
> 
> - **[Tavily](https://app.tavily.com)** 🌐 - Enhanced web search and profile discovery  

## 📁 Project Structure

```
ice_breaker/
├── agents/                    # AI agents for profile lookup
│   ├── linkedin_lookup_agent.py
├── chains/                    # LangChain custom chains
│   └── custom_chains.py
├── third_parties/            # External API integrations
│   ├── linkedin.py
├── tools/                    # Utility tools and functions
│   └── tools.py
├── templates/                # Flask HTML templates
│   └── index.html
├── static/                   # Static assets
│   └── demo.gif
├── app.py                    # Flask application entry point
├── ice_breaker.py           # Core ice breaker logic
├── output_parsers.py        # Response formatting utilities
└── requirements.txt         # Python dependencies
```

## 🔧 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
SCRAPIN_API_KEY=your_scrapin_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

# Optional: Enable LangSmith tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=ice_breaker
```

> **⚠️ Important Note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error. If you don't need tracing, simply remove or comment out these environment variables.

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for LLM access | ✅ |
| `SCRAPIN_API_KEY` | Scrapin.io API key for LinkedIn scraping | ✅ |
| `TAVILY_API_KEY` | Tavily API key for enhanced web search | ✅ |
| `LANGCHAIN_TRACING_V2` | Enable LangSmith tracing (optional) | ⚪ |
| `LANGCHAIN_API_KEY` | LangSmith API key (required if tracing enabled) | ⚪ |
| `LANGCHAIN_PROJECT` | LangSmith project name (optional) | ⚪ |