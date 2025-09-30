import json
from typing import Any, Dict, List, Optional
from utils.FileManager import FileManager
from utils.CRUDManager import CRUDManager


# --- 1. FUNÇÕES DE UTILIDADE (INPUT/OUTPUT) ---

def get_user_data() -> Dict[str, Any]:
    """Solicita e coleta dados do usuário para um novo registro ou atualização."""
    print("\n--- Coleta de Dados ---")

    # Exemplo: Solicita nome e email
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()

    return {
        "nome": nome,
        "email": email
    }
