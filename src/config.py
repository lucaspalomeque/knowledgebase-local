# src/config.py
import os
from pathlib import Path
from typing import Dict, Any

class Config:
    """Configuración centralizada para el sistema RAG"""
    
    # Paths del proyecto
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    UPLOADS_DIR = DATA_DIR / "uploads"
    CHROMADB_DIR = DATA_DIR / "chromadb"
    CACHE_DIR = DATA_DIR / "cache"
    LOGS_DIR = DATA_DIR / "logs"
    
    # Configuración de Ollama
    OLLAMA_URL = "http://localhost:11434"
    LLM_MODEL = "openhermes"  # El modelo que acabas de instalar
    
    # Configuración de embeddings
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Configuración RAG
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 150
    MAX_RETRIEVAL_DOCS = 4
    SIMILARITY_THRESHOLD = 0.6
    
    # Configuración LLM
    TEMPERATURE = 0.1
    MAX_TOKENS = 512
    CONTEXT_LENGTH = 4096
    
    # Configuración ChromaDB
    COLLECTION_NAME = "lucas_rag_documents"
    
    # Configuración UI
    STREAMLIT_PORT = 8501
    ENABLE_WIDE_MODE = True
    
    @classmethod
    def setup_directories(cls):
        """Crear directorios necesarios si no existen"""
        for directory in [cls.DATA_DIR, cls.UPLOADS_DIR, cls.CHROMADB_DIR, 
                         cls.CACHE_DIR, cls.LOGS_DIR]:
            directory.mkdir(parents=True, exist_ok=True)
        print("✅ Directorios creados/verificados")
    
    @classmethod
    def get_model_config(cls) -> Dict[str, Any]:
        """Configuración optimizada para tu RTX 4080"""
        return {
            "model": cls.LLM_MODEL,
            "temperature": cls.TEMPERATURE,
            "max_tokens": cls.MAX_TOKENS,
            "top_p": 0.9,
            "top_k": 40,
            "repeat_penalty": 1.1
        }
    
    @classmethod
    def get_system_prompt(cls) -> str:
        """Prompt del sistema para RAG"""
        return """Eres un asistente experto en análisis de documentos. Tu tarea es responder preguntas basándote ÚNICAMENTE en el contexto proporcionado.

INSTRUCCIONES:
1. Usa solo la información del contexto para responder
2. Si la información no está en el contexto, di "No encontré esa información en los documentos"
3. Sé conciso pero completo en tus respuestas
4. Cita las fuentes cuando sea relevante
5. Si hay información contradictoria, menciona ambas perspectivas

Responde en español de manera clara y profesional."""