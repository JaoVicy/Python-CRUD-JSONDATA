import json

class Writer:
    def __init__(self):
        DATA: str = 'registry.json'

    def save_data(self, data, filename: str) -> None:
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