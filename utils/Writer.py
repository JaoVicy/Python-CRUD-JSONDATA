import json

class Writer:
    def __init__(self):
        DATA: str = 'registry.json'

    @staticmethod
    def save_data(data, filename: str) -> None:
        """Saves data to a JSON file."""
        try:
            # Abrir o arquivo no modo de escrita ('w')
            # encoding='utf-8' garante que caracteres especiais (acentos) sejam preservados
            with open(filename, 'w', encoding='utf-8') as f:
                # json.dump escreve o objeto Python (data) como JSON no arquivo (f)
                # indent=4 é uma boa prática para formatar o arquivo, tornando-o legível por humanos
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Dados salvos com sucesso em {filename}")
        except IOError as e:
            print(f"Erro ao escrever no arquivo: {e}")

    @staticmethod
    def load_data(filename: str) -> None:
        """Carrega dados de um arquivo JSON. Retorna uma lista vazia se o arquivo não existir."""
        try:
            # Abrir o arquivo no modo de leitura ('r')
            with open(filename, 'r', encoding='utf-8') as f:
                # json.load lê o JSON do arquivo (f) e o converte para um objeto Python
                return json.load(f)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com dados vazios.")
            return []  # Retorna uma lista vazia se o arquivo não existir
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON em {filename}. O arquivo pode estar corrompido.")
            return []  # Retorna uma lista vazia se o JSON for inválido
