"""
.PHONY: help install install-dev clean test lint format type-check run docker-build docker-run setup

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  clean        Clean up generated files"
	@echo "  test         Run tests"
	@echo "  lint         Run linting"
	@echo "  format       Format code"
	@echo "  type-check   Run type checking"
	@echo "  run          Run the application"
	@echo "  docker-build Build Docker image"
	@echo "  docker-run   Run in Docker"
	@echo "  setup        Initial project setup"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt -r requirements-dev.txt
	pre-commit install

# Setup
setup:
	@echo "🚀 Setting up Local RAG Weekend project..."
	python -m venv venv
	@echo "📦 Virtual environment created"
	@echo "Activate with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"
	@echo "Then run: make install-dev"

# Cleaning
clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf build/ dist/ htmlcov/ .coverage coverage.xml

# Testing
test:
	@echo "🧪 Running tests..."
	pytest tests/ -v

test-cov:
	@echo "🧪 Running tests with coverage..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Code quality
lint:
	@echo "🔍 Running linting..."
	flake8 src/ tests/
	mypy src/

format:
	@echo "🎨 Formatting code..."
	black src/ tests/
	isort src/ tests/

type-check:
	@echo "📝 Running type checking..."
	mypy src/

# Development
run:
	@echo "🚀 Starting Local RAG Weekend..."
	streamlit run main.py

run-debug:
	@echo "🐛 Starting in debug mode..."
	DEBUG_MODE=true streamlit run main.py

# Docker
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t local-rag-weekend .

docker-run:
	@echo "🐳 Running in Docker..."
	docker run -p 8501:8501 -v $(PWD)/data:/app/data local-rag-weekend

docker-compose-up:
	@echo "🐳 Starting with Docker Compose..."
	docker-compose up -d

docker-compose-down:
	@echo "🐳 Stopping Docker Compose..."
	docker-compose down

# Data management
clean-data:
	@echo "🗑️ Cleaning data directories..."
	rm -rf data/uploads/* data/chromadb/* data/cache/* data/logs/*
	@echo "Data directories cleaned (structure preserved)"

backup-data:
	@echo "💾 Backing up data..."
	tar -czf data-backup-$(shell date +%Y%m%d-%H%M%S).tar.gz data/

# Performance
benchmark:
	@echo "⚡ Running benchmarks..."
	python scripts/benchmark.py

profile:
	@echo "📊 Profiling application..."
	python -m cProfile -o profile.stats main.py

# Git hooks
pre-commit:
	@echo "🔍 Running pre-commit hooks..."
	pre-commit run --all-files

# Documentation
docs-serve:
	@echo "📚 Serving documentation..."
	mkdocs serve

docs-build:
	@echo "📚 Building documentation..."
	mkdocs build

# All quality checks
qa: format lint type-check test
	@echo "✅ All quality checks passed!"
"""

# ================================
# .gitkeep files (para mantener estructura de directorios)
# ================================

# data/uploads/.gitkeep
"""
# This file ensures the uploads directory is tracked by git
# while keeping the directory empty of actual uploads
"""

# data/chromadb/.gitkeep  
"""
# This file ensures the chromadb directory is tracked by git
# while keeping the directory empty of database files
"""

# data/cache/.gitkeep
"""
# This file ensures the cache directory is tracked by git
# while keeping the directory empty of cache files
"""

# data/logs/.gitkeep
"""
# This file ensures the logs directory is tracked by git
# while keeping the directory empty of log files
"""
