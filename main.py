import json
from typing import Any, Dict, List, Optional
from utils.CRUDManager import CRUDManager


# --- 1. FUNÇÕES DE UTILIDADE (INPUT/OUTPUT) ---

def get_user_data() -> Dict[str, Any]:
    """Solicita e coleta dados do usuário para um novo registro ou atualização."""
    print("\n--- Coleta de Dados ---")

    # Solicita nome e email
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

    # Exibe arte ASCII de boas-vindas
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

    while True:
        print("\n" + "=" * 40)
        print("  SISTEMA DE GERENCIAMENTO DE REGISTROS (CRUD)")
        print("=" * 40)
        print("1. Cadastrar Novo Registro (CREATE)")
        print("2. Buscar Registro por ID (READ)")
        print("3. Listar Todos os Registros (READ)")
        print("4. Atualizar Registro (UPDATE)")
        print("5. Excluir Registro (DELETE)")
        print("6. Sair")
        print("=" * 40)

        escolha = input("Escolha uma opção (1-6): ").strip()

        try:
            if escolha == '1':
                # CREATE: Chama manager.add_record()
                print("\n[ CADASTRAR NOVO REGISTRO ]")
                dados = get_user_data()
                new_id = manager.add_record(dados)
                print(f"\n✅ SUCESSO: Registro '{dados.get('nome', 'Novo')}' cadastrado com ID: {new_id}")

            elif escolha == '2':
                # READ (Busca por ID): Chama manager.get_record_by_id()
                print("\n[ BUSCAR REGISTRO POR ID ]")
                id_alvo = int(input("Digite o ID do registro: "))
                registro = manager.get_record_by_id(id_alvo)
                display_record(registro)

            elif escolha == '3':
                # READ (Listar Todos): Chama manager.list_all_records()
                display_all_records(manager.list_all_records())

            elif escolha == '4':
                # UPDATE: Chama manager.update_record()
                print("\n[ ATUALIZAR REGISTRO ]")
                id_alvo = int(input("Digite o ID do registro a ser atualizado: "))

                # Validação rápida
                if not manager.get_record_by_id(id_alvo):
                    print(f"❌ ERRO: Registro com ID {id_alvo} não encontrado.")
                    continue

                novos_dados = get_user_data()

                if manager.update_record(id_alvo, novos_dados):
                    print(f"✅ SUCESSO: Registro ID {id_alvo} atualizado com sucesso.")
                else:
                    print("❌ ERRO: Falha ao atualizar (ID não encontrado).")

            elif escolha == '5':
                # DELETE: Chama manager.delete_record()
                print("\n[ EXCLUIR REGISTRO ]")
                id_alvo = int(input("Digite o ID do registro a ser excluído: "))

                if manager.delete_record(id_alvo):
                    print(f"✅ SUCESSO: Registro ID {id_alvo} excluído com sucesso.")
                else:
                    print(f"❌ ERRO: Registro com ID {id_alvo} não encontrado.")

            elif escolha == '6':
                print("\nEncerrando o programa. Até mais!")
                break

            else:
                print("\nOpção inválida. Por favor, escolha um número de 1 a 6.")

        except ValueError:
            # Captura erro se o usuário digitar texto onde um número (ID) é esperado
            print("\n❌ ERRO: Entrada inválida. Por favor, digite um número.")
        except Exception as e:
            # Captura outros erros inesperados
            print(f"\n❌ ERRO INESPERADO: {e}")


# --- 3. EXECUÇÃO PROTEGIDA ---

if __name__ == '__main__':
    main()