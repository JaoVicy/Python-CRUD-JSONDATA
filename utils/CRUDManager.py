from typing import Any, List, Dict, Optional
from .FileManager import FileManager

class CRUDManager:
    """
    Implementa as operações CRUD completas. Os registros são dicionários armazenados em uma lista.
    Usa o FileManager para persistência de dados em JSON.
    """

    # O nome do arquivo usado para persistência
    DATA_FILE = 'registry.json'

    def __init__(self):
        # Carrega os dados existentes (ou uma lista vazia) quando o aplicativo inicia
        self.records: List[Dict[str, Any]] = FileManager.load_data(self.DATA_FILE)
        print(f"Manager initialized. Total records loaded: {len(self.records)}")

    def _save_and_persist(self) -> None:
        """Método privado para salvar a lista de registros no arquivo JSON."""
        FileManager.save_data(self.records, self.DATA_FILE)

    def _generate_new_id(self) -> int:
        """Gera um ID único (o maior ID existente + 1)."""
        if not self.records:
            return 1
        # Obtém o ID máximo de todos os registros e adiciona 1
        max_id = max(record.get('id', 0) for record in self.records)
        return max_id + 1

    # =========================================================
    # C - CREATE (Adicionar Registro)
    # =========================================================
    def add_record(self, data: Dict[str, Any]) -> int:
        """Adiciona um novo registro e persiste os dados."""

        # 1. Gera e atribui um ID único
        new_id = self._generate_new_id()
        data['id'] = new_id

        # 2. Adiciona o novo registro à lista em memória
        self.records.append(data)

        # 3. Salva a lista atualizada no arquivo JSON
        self._save_and_persist()

        return new_id

    # =========================================================
    # R - READ (Recuperar/Listar)
    # =========================================================
    def get_record_by_id(self, target_id: int) -> Optional[Dict[str, Any]]:
        """Encontra um único registro pelo seu ID."""
        for record in self.records:
            if record.get('id') == target_id:
                return record
        return None  # Retorna None se não for encontrado

    def list_all_records(self) -> List[Dict[str, Any]]:
        """Retorna a lista completa de todos os registros em memória."""
        return self.records

    # =========================================================
    # U - UPDATE (Modificar)
    # =========================================================
    def update_record(self, target_id: int, new_data: Dict[str, Any]) -> bool:
        """Atualiza um registro existente, preservando seu ID."""
        for i, record in enumerate(self.records):
            if record.get('id') == target_id:
                # 1. Atualiza o registro, mantendo o ID original
                # Usa .update() para mesclar novos dados com dados existentes
                self.records[i].update(new_data)
                self.records[i]['id'] = target_id  # Garante que o ID não seja sobrescrito

                # 2. Persiste a alteração
                self._save_and_persist()
                return True  # Atualização bem-sucedida

        return False  # Registro não encontrado

    # =========================================================
    # D - DELETE (Remover)
    # =========================================================
    def delete_record(self, target_id: int) -> bool:
        """Exclui um registro pelo seu ID e persiste a alteração."""

        # Cria uma nova lista que exclui o registro com o ID de destino
        original_size = len(self.records)
        self.records = [r for r in self.records if r.get('id') != target_id]

        # Verifica se o tamanho mudou
        if len(self.records) < original_size:
            # Se um registro foi removido, persiste a nova lista
            self._save_and_persist()
            return True  # Exclusão bem-sucedida

        return False  # Registro não encontrado