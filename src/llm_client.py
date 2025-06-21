# src/llm_client.py
import requests
import json
import time
import logging
from typing import Dict, Any, Optional
from .config import Config

logger = logging.getLogger(__name__)

class OllamaClient:
    """Cliente simple y robusto para Ollama"""
    
    def __init__(self, base_url: str = None, model: str = None):
        self.base_url = base_url or Config.OLLAMA_URL
        self.model = model or Config.LLM_MODEL
        self.timeout = 120  # 2 minutos timeout
        
    def test_connection(self) -> bool:
        """Probar conexión con Ollama"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error conectando con Ollama: {e}")
            return False
    
    def is_model_available(self) -> bool:
        """Verificar si el modelo está disponible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                model_names = [model['name'] for model in models]
                return self.model in model_names or f"{self.model}:latest" in model_names
            return False
        except Exception as e:
            logger.error(f"Error verificando modelo: {e}")
            return False
    
    def generate(self, prompt: str, system_prompt: str = None, **kwargs) -> Dict[str, Any]:
        """Generar respuesta con el modelo"""
        
        # Configuración del request
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": Config.get_model_config()
        }
        
        # Añadir system prompt si se proporciona
        if system_prompt:
            payload["system"] = system_prompt
        
        # Override con kwargs adicionales
        payload["options"].update(kwargs)
        
        try:
            start_time = time.time()
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            result = response.json()
            
            end_time = time.time()
            generation_time = end_time - start_time
            
            return {
                "response": result.get("response", ""),
                "success": True,
                "generation_time": generation_time,
                "model": self.model,
                "prompt_tokens": result.get("prompt_eval_count", 0),
                "completion_tokens": result.get("eval_count", 0)
            }
            
        except requests.exceptions.Timeout:
            return {
                "response": "⏰ Timeout: El modelo tardó demasiado en responder",
                "success": False,
                "error": "timeout"
            }
        except requests.exceptions.RequestException as e:
            return {
                "response": f"❌ Error de conexión: {str(e)}",
                "success": False,
                "error": "connection_error"
            }
        except Exception as e:
            return {
                "response": f"❌ Error inesperado: {str(e)}",
                "success": False,
                "error": "unexpected_error"
            }
    
    def health_check(self) -> Dict[str, Any]:
        """Verificación completa del estado del sistema"""
        health = {
            "ollama_connected": False,
            "model_available": False,
            "model_name": self.model,
            "base_url": self.base_url,
            "status": "unhealthy"
        }
        
        # Test conexión
        if self.test_connection():
            health["ollama_connected"] = True
            
            # Test modelo
            if self.is_model_available():
                health["model_available"] = True
                health["status"] = "healthy"
            else:
                health["status"] = "model_not_found"
        else:
            health["status"] = "ollama_not_running"
        
        return health
    
    def get_available_models(self) -> list:
        """Obtener lista de modelos disponibles"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                return [model['name'] for model in models]
            return []
        except Exception as e:
            logger.error(f"Error obteniendo modelos: {e}")
            return []

# Función de conveniencia para testing rápido
def test_ollama_setup():
    """Test rápido del setup de Ollama"""
    print("🔍 Probando configuración de Ollama...")
    
    client = OllamaClient()
    health = client.health_check()
    
    print(f"📡 Conexión Ollama: {'✅' if health['ollama_connected'] else '❌'}")
    print(f"🤖 Modelo '{health['model_name']}': {'✅' if health['model_available'] else '❌'}")
    print(f"🔗 URL: {health['base_url']}")
    print(f"📊 Estado: {health['status']}")
    
    if health['status'] == 'healthy':
        print("\n🧪 Probando generación...")
        result = client.generate("Hola! Responde brevemente: ¿estás funcionando?")
        
        if result['success']:
            print(f"✅ Respuesta: {result['response']}")
            print(f"⏱️ Tiempo: {result['generation_time']:.2f}s")
        else:
            print(f"❌ Error: {result['response']}")
    
    available_models = client.get_available_models()
    if available_models:
        print(f"\n📋 Modelos disponibles: {', '.join(available_models)}")
    
    return health['status'] == 'healthy'

if __name__ == "__main__":
    test_ollama_setup()