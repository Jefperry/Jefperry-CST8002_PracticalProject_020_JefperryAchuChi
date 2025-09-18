"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: October 12, 2025
Author: Jefperry Achu Chi

kelp_fish_manager.py - Business layer: Manages kelp fish data operations and business logic
"""

from persistence.data_access import DataAccess
from model.kelp_fish_record import KelpFishRecord
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class KelpFishManager:
    """
    Business layer class that manages kelp fish data operations.
    Contains business logic and coordinates between presentation and persistence layers.
    Maintains the in-memory data structure (array/list) of records.
    """

    def __init__(self):
        """
        Initialize the KelpFishManager with data access and empty records list.
        """
        self.data_access = DataAccess()
        self.records = []  # Array/list data structure to hold records in memory

    def load_data(self, max_records=100):
        """
        Load data from the dataset file into memory.

        Args:
            max_records (int): Maximum number of records to load (default 100)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.records = self.data_access.read_kelp_fish_data(max_records)
            return True
        except Exception as e:
            print(f"Failed to load data: {e}")
            return False

    def reload_data(self, max_records=100):
        """
        Reload data from the dataset file, replacing current in-memory data.

        Args:
            max_records (int): Maximum number of records to load (default 100)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Clear current data and reload
            self.records.clear()
            return self.load_data(max_records)
        except Exception as e:
            print(f"Failed to reload data: {e}")
            return False

    def persist_data(self):
        """
        Persist current in-memory data to a new CSV file with GUID filename.

        Returns:
            str: Filename of created file, or None if failed
        """
        try:
            if not self.records:
                print("No data to persist.")
                return None
            return self.data_access.write_kelp_fish_data(self.records)
        except Exception as e:
            print(f"Failed to persist data: {e}")
            return None

    def get_all_records(self):
        """
        Get all records from memory.

        Returns:
            list: List of all KelpFishRecord objects
        """
        return self.records.copy()  # Return copy to prevent external modification

    def get_record_by_index(self, index):
        """
        Get a specific record by index.

        Args:
            index (int): Index of the record (0-based)

        Returns:
            KelpFishRecord: The record at the specified index, or None if invalid index
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

    def get_records_by_species(self, species_code):
        """
        Get all records for a specific species.

        Args:
            species_code (str): Species code to search for

        Returns:
            list: List of KelpFishRecord objects matching the species code
        """
        return [record for record in self.records
                if record.get_species_code().upper() == species_code.upper()]

    def get_records_by_site(self, site_identification):
        """
        Get all records for a specific site.

        Args:
            site_identification (str): Site identification to search for

        Returns:
            list: List of KelpFishRecord objects matching the site
        """
        return [record for record in self.records
                if record.get_site_identification().upper() == site_identification.upper()]

    def add_record(self, record):
        """
        Add a new record to the in-memory data structure.

        Args:
            record (KelpFishRecord): Record to add

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if isinstance(record, KelpFishRecord):
                self.records.append(record)
                return True
            else:
                print("Invalid record type. Expected KelpFishRecord.")
                return False
        except Exception as e:
            print(f"Failed to add record: {e}")
            return False

    def update_record(self, index, updated_record):
        """
        Update a record at the specified index.

        Args:
            index (int): Index of the record to update (0-based)
            updated_record (KelpFishRecord): New record data

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if 0 <= index < len(self.records) and isinstance(updated_record, KelpFishRecord):
                self.records[index] = updated_record
                return True
            return False
        except Exception as e:
            print(f"Failed to update record: {e}")
            return False

    def delete_record(self, index):
        """
        Delete a record from the in-memory data structure.

        Args:
            index (int): Index of the record to delete (0-based)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if 0 <= index < len(self.records):
                del self.records[index]
                return True
            return False
        except Exception as e:
            print(f"Failed to delete record: {e}")
            return False

    def get_record_count(self):
        """
        Get the total number of records in memory.

        Returns:
            int: Number of records
        """
        return len(self.records)

    def search_records(self, search_term):
        """
        Search records by any field containing the search term.

        Args:
            search_term (str): Term to search for

        Returns:
            list: List of KelpFishRecord objects containing the search term
        """
        search_term = search_term.lower()
        matching_records = []

        for record in self.records:
            # Check all string fields for the search term
            if (search_term in record.get_site_identification().lower() or
                search_term in record.get_species_code().lower() or
                search_term in record.get_survey_type().lower() or
                search_term in record.get_average_depth_ft().lower() or
                search_term in str(record.get_year()) or
                search_term in str(record.get_diver_identication()) or
                search_term in str(record.get_transect()) or
                    search_term in str(record.get_count())):
                matching_records.append(record)

        return matching_records

    def validate_record_data(self, site_identification, year, diver_identication,
                             transect, average_depth_ft, species_code, count, survey_type):
        """
        Validate record data before creating/updating a record.

        Args:
            site_identification (str): Site identification
            year (int): Year
            diver_identication (int): Diver identification
            transect (int): Transect number
            average_depth_ft (str): Average depth
            species_code (str): Species code
            count (int): Count
            survey_type (str): Survey type

        Returns:
            tuple: (is_valid (bool), error_message (str))
        """
        # Basic validation logic
        if not site_identification.strip():
            return False, "Site identification cannot be empty"

        if year < 1900 or year > 2030:
            return False, "Year must be between 1900 and 2030"

        if diver_identication < 0:
            return False, "Diver identification must be non-negative"

        if transect < 0:
            return False, "Transect must be non-negative"

        if not species_code.strip():
            return False, "Species code cannot be empty"

        if count < 0:
            return False, "Count must be non-negative"

        if not survey_type.strip():
            return False, "Survey type cannot be empty"

        return True, "Valid"
