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


def display_record(record: Optional[Dict[str, Any]]) -> None:
    """Exibe um único registro de forma formatada."""
    if record:
        print("\n--- Registro Encontrado ---")
        for key, value in record.items():
            print(f"  {key.capitalize()}: {value}")
        print("--------------------------")
    else:
        print("\nRegistro não encontrado.")
