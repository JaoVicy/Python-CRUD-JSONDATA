from typing import Any, List, Dict, Optional
from .FileManager import FileManager

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

    # =========================================================
    # C - CREATE (Add Record)
    # =========================================================
    def add_record(self, data: Dict[str, Any]) -> int:
        """Adds a new record and persists the data."""

        # 1. Generate and assign a unique ID
        new_id = self._generate_new_id()
        data['id'] = new_id

        # 2. Add the new record to the in-memory list
        self.records.append(data)

        # 3. Save the updated list to the JSON file
        self._save_and_persist()

        return new_id

    # =========================================================
    # R - READ (Retrieve/List)
    # =========================================================
    def get_record_by_id(self, target_id: int) -> Optional[Dict[str, Any]]:
        """Finds a single record by its ID."""
        for record in self.records:
            if record.get('id') == target_id:
                return record
        return None  # Return None if not found

    def list_all_records(self) -> List[Dict[str, Any]]:
        """Returns the complete list of all in-memory records."""
        return self.records

    # =========================================================
    # U - UPDATE (Modify)
    # =========================================================
    def update_record(self, target_id: int, new_data: Dict[str, Any]) -> bool:
        """Updates an existing record, preserving its ID."""
        for i, record in enumerate(self.records):
            if record.get('id') == target_id:
                # 1. Update the record, keeping the original ID
                # Use .update() to merge new data with existing data
                self.records[i].update(new_data)
                self.records[i]['id'] = target_id  # Ensure ID is not overwritten

                # 2. Persist the change
                self._save_and_persist()
                return True  # Successful update

        return False  # Record not found

    # =========================================================
    # D - DELETE (Remove)
    # =========================================================
    def delete_record(self, target_id: int) -> bool:
        """Deletes a record by its ID and persists the change."""

        # Create a new list that excludes the record with the target ID
        original_size = len(self.records)
        self.records = [r for r in self.records if r.get('id') != target_id]

        # Check if the size changed
        if len(self.records) < original_size:
            # If a record was removed, persist the new list
            self._save_and_persist()
            return True  # Successful deletion

        return False  # Record not found
