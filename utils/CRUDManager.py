import json
from typing import Any, List, Dict, Optional
from utils.FileManager import FileManager

class CRUDManager:
    """
    Implements the full CRUD operations. Records are dictionaries stored in a list.
    Uses FileManager for data persistence in JSON.
    """

    # The name of the file used for persistence
    DATA_FILE = 'registry.json'

    def __init__(self):
        # Load existing data (or an empty list) when the application starts
        self.records: List[Dict[str, Any]] = FileManager.load_data(self.DATA_FILE)
        print(f"Manager initialized. Total records loaded: {len(self.records)}")

    def _save_and_persist(self) -> None:
        """Private method to save the list of records to the JSON file."""
        FileManager.save_data(self.records, self.DATA_FILE)

    def _generate_new_id(self) -> int:
        """Generates a unique ID (the highest existing ID + 1)."""
        if not self.records:
            return 1
        # Get the maximum ID from all records and add 1
        max_id = max(record.get('id', 0) for record in self.records)
        return max_id + 1
