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
