import json
from typing import Any, Dict, List, Optional

class FileManager:
    """
    Classe utilitária para manipular arquivos JSON, garantindo que a
    lógica de leitura/escrita esteja separada da lógica de negócios (CRUD).
    """

    @staticmethod
    def save_data(data: Any, filename: str) -> None:
        """Salva a estrutura de dados (data) em um arquivo JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Usa indent=4 para legibilidade e ensure_ascii=False para suportar acentos
                json.dump(data, f, indent=4, ensure_ascii=False)
            # print(f"Dados salvos com sucesso em '{filename}'") # Comentado para não poluir o console
        except IOError as e:
            print(f"ERRO: Falha ao escrever no arquivo '{filename}': {e}")

    @staticmethod
    def load_data(filename: str) -> List[Dict[str, Any]]:
        """Carrega dados de um arquivo JSON. Retorna uma lista vazia em caso de erro."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # print(f"AVISO: Arquivo '{filename}' não encontrado. Iniciando com dados vazios.")
            return []
        except json.JSONDecodeError:
            print(f"ERRO: Arquivo '{filename}' corrompido ou JSON inválido. Iniciando com dados vazios.")
            return []