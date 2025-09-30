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


def display_all_records(records: List[Dict[str, Any]]) -> None:
    """Exibe todos os registros em formato de tabela simples."""
    if not records:
        print("\nNenhum registro encontrado.")
        return

    print("\n--- LISTA DE REGISTROS ---")

    # Lógica de formatação de tabela (mantida do código anterior)
    headers = list(records[0].keys()) if records else []

    header_line = " | ".join(h.upper().ljust(15) for h in headers)
    print("-" * (len(header_line) + len(headers)))
    print(header_line)
    print("-" * (len(header_line) + len(headers)))

    for record in records:
        row = " | ".join(str(record.get(h, '')).ljust(15) for h in headers)
        print(row)
    print("-" * (len(header_line) + len(headers)))


# --- 2. FUNÇÃO PRINCIPAL (MAIN) ---

def main():
    """Função principal que inicia a aplicação e exibe o menu interativo."""

    asccii_art: str = r""""
    $$\   $$\           $$\ $$\           $$\ 
    $$ |  $$ |          $$ |$$ |          $$ |
    $$ |  $$ | $$$$$$\  $$ |$$ | $$$$$$\  $$ |
    $$$$$$$$ |$$  __$$\ $$ |$$ |$$  __$$\ $$ |
    $$  __$$ |$$$$$$$$ |$$ |$$ |$$ /  $$ |\__|
    $$ |  $$ |$$   ____|$$ |$$ |$$ |  $$ |    
    $$ |  $$ |\$$$$$$$\ $$ |$$ |\$$$$$$  |$$\ 
    \__|  \__| \_______|\__|\__| \______/ \__|

    """
    print(asccii_art)

    # Inicializa o gerenciador de dados, carregando os registros do JSON
    manager = CRUDManager()
