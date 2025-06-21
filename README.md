# 🤖 Knowledgebase Local

> Build a complete RAG (Retrieval-Augmented Generation) system using local LLMs in just one weekend!

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/yourusername/weekend-rag-local)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **completely local, private, and free** RAG system that lets you chat with your documents using state-of-the-art LLMs like Hermes and Llama - no API keys required!

## 🎯 What You'll Build

By the end of this weekend project, you'll have:

- 📚 **Document Knowledge Base**: Upload PDFs and build a searchable knowledge base
- 🧠 **Local AI Brain**: Hermes 2.5 Mistral or Llama 3.1 running completely offline
- 💬 **Chat Interface**: Clean Streamlit web app to interact with your documents
- 🔍 **Smart Search**: Semantic search powered by ChromaDB vector database
- 🔒 **100% Private**: Your documents never leave your machine

![Demo Screenshot](docs/images/demo-screenshot.png)

## ✨ Features

- 🚀 **Zero API Costs** - Everything runs locally
- 🔒 **Complete Privacy** - Your data stays on your machine
- 🧠 **Multiple LLM Support** - Hermes, Llama, Phi-3, and more
- 📄 **PDF Processing** - Intelligent document chunking and indexing
- 💬 **Chat Interface** - Conversational Q&A with source citations
- ⚡ **Fast Setup** - Get running in under 15 minutes
- 🐳 **Docker Ready** - One-command deployment
- 📊 **Performance Monitoring** - Built-in metrics and debugging

## 🚀 Quick Start (5 Minutes)

### Prerequisites

- **Hardware**: 8GB RAM minimum, 6GB VRAM recommended
- **OS**: Linux, macOS, or Windows with WSL2
- **Python**: 3.8 or higher

### 1. Install Ollama

```bash
# Linux/macOS
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Download a Model

```bash
# Recommended: Hermes 2.5 Mistral 7B (~4.8GB)
ollama pull adrienbrault/nous-hermes2-mistral:7b-dpo

# Alternative: Llama 3.1 8B (~5.2GB)
ollama pull llama3.1:8b

# Lightweight: Phi-3.5 Mini (~2.5GB)
ollama pull phi3.5:latest
```

### 3. Clone and Setup

```bash
git clone https://github.com/yourusername/weekend-rag-local.git
cd weekend-rag-local

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 4. Run the App

```bash
# Start Ollama server (if not already running)
ollama serve &

# Launch the Streamlit app
streamlit run main.py
```

Open your browser to `http://localhost:8501` and start chatting with your documents! 🎉

## 📚 Supported Models

| Model | Size | VRAM | Performance | Quality | Best For |
|-------|------|------|-------------|---------|----------|
| **Hermes 2.5 Mistral 7B** | 4.8GB | 6GB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Balanced (Recommended) |
| **Llama 3.1 8B** | 5.2GB | 7GB | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Best Quality |
| **Phi-3.5 Mini** | 2.5GB | 3GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Low-end Hardware |
| **Code Llama 13B** | 8.5GB | 10GB | ⭐⭐ | ⭐⭐⭐⭐⭐ | Code Documents |

## 🏗️ Architecture

```
📄 PDF Upload → 🔄 LangChain Processing → 💾 ChromaDB Storage
                                    ↓
💬 User Question → 🔍 Vector Search → 🧠 Local LLM → 📱 Response
```

For detailed architecture, see [ARCHITECTURE.md](docs/ARCHITECTURE.md)

## 📖 Usage

### 1. Upload Documents
- Click "Upload Documents" in the sidebar
- Select one or more PDF files
- Wait for processing (automatic chunking and indexing)

### 2. Ask Questions
- Type your question in the chat input
- Get AI-powered answers with source citations
- Follow up with additional questions

### 3. Configure Settings
- Adjust similarity threshold for search precision
- Change max retrieved documents
- Modify LLM temperature for creativity
- Switch between different models

## 🛠️ Development

### Project Structure

```
weekend-rag-local/
├── 📁 src/                    # Core application code
│   ├── config.py             # Configuration settings
│   ├── llm_client.py         # Ollama client wrapper
│   ├── rag_chain.py          # Main RAG logic
│   └── document_processor.py # PDF processing
├── 📁 data/                  # Data storage
│   ├── uploads/              # Uploaded documents
│   └── chromadb/             # Vector database
├── 📁 docs/                  # Documentation
│   ├── ROADMAP.md            # Development roadmap
│   └── ARCHITECTURE.md       # System architecture
├── 📁 tests/                 # Test files
├── main.py                   # Streamlit application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container setup
└── docker-compose.yml       # Multi-service deployment
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run linting
black src/ tests/
flake8 src/ tests/
```

## 🐳 Docker Deployment

### Single Container

```bash
# Build the image
docker build -t weekend-rag-local .

# Run with GPU support
docker run -d \
  --name rag-local \
  --gpus all \
  -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  weekend-rag-local
```

### Multi-Service with Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## ⚡ Performance Optimization

### Hardware Recommendations

| Use Case | RAM | VRAM | Storage | Model |
|----------|-----|------|---------|--------|
| **Personal Use** | 8GB | 4GB | 10GB | Phi-3.5 Mini |
| **Professional** | 16GB | 8GB | 20GB | Hermes 2.5 Mistral |
| **Power User** | 32GB | 12GB+ | 50GB | Llama 3.1 8B |

### Optimization Tips

```bash
# CPU-only mode (no GPU)
export CUDA_VISIBLE_DEVICES=""

# Limit Ollama memory usage
export OLLAMA_MAX_LOADED_MODELS=1

# Use quantized models for speed
ollama pull hermes2.5-mistral:7b-q4_0
```

## 🔧 Troubleshooting

### Common Issues

**Ollama not connecting:**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama
pkill ollama
ollama serve
```

**Out of memory errors:**
```bash
# Switch to smaller model
ollama pull phi3.5:latest

# Update config.py
LLM_MODEL = "phi3.5:latest"
```

**Slow performance:**
```bash
# Check GPU usage
nvidia-smi

# Reduce context length
# In config.py: CHUNK_SIZE = 400
```

**ChromaDB errors:**
```bash
# Reset database
rm -rf data/chromadb/*
# Restart application
```

## 📈 Roadmap

- [x] **Phase 1**: Basic RAG with PDF support
- [x] **Phase 2**: Streamlit UI and chat interface
- [ ] **Phase 3**: Multi-format support (DOCX, TXT, HTML)
- [ ] **Phase 4**: Conversation memory and context
- [ ] **Phase 5**: Advanced retrieval techniques
- [ ] **Phase 6**: REST API and integrations
- [ ] **Phase 7**: Multi-user support and authentication

See [ROADMAP.md](docs/ROADMAP.md) for detailed planning.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

### Ways to Contribute

- 🐛 **Bug Reports**: Found an issue? Open an issue!
- 💡 **Feature Requests**: Have an idea? We'd love to hear it!
- 📝 **Documentation**: Help improve our docs
- 🧪 **Testing**: Add tests or test on different hardware
- 💻 **Code**: Submit pull requests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for making local LLMs accessible
- [LangChain](https://langchain.com/) for the RAG framework
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [Nous Research](https://nousresearch.com/) for the Hermes models
- [Meta](https://ai.meta.com/) for the Llama models

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/weekend-rag-local)
![GitHub forks](https://img.shields.io/github/forks/yourusername/weekend-rag-local)
![GitHub issues](https://img.shields.io/github/issues/yourusername/weekend-rag-local)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/weekend-rag-local)

---

**Built with ❤️ for the AI community**

*Star ⭐ this repo if you found it helpful!*