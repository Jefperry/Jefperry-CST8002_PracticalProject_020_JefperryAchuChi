"""
CST8002 - Data-Driven Programming - Practical Project 3
Professor: Stanley Pieda
Due Date: November 16, 2025
Author: Jefperry Achu Chi

kelp_fish_manager.py - Business layer: Manages kelp fish data operations and business logic
Enhanced with advanced data structure sorting capabilities
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

    def sort_records(self, sort_by="year", reverse=False):
        """
        Sort records in the data structure based on specified criteria.
        Demonstrates advanced data structure manipulation and sorting algorithms.

        Algorithm Details:
        - Uses Python's Timsort algorithm (hybrid merge-sort/insertion-sort)
        - Time Complexity: O(n log n) average and worst case
        - Space Complexity: O(n) for the sorting operation
        - Stable sort: maintains relative order of equal elements

        Sorting Strategy:
        - Each sort uses compound keys (primary field + secondary year/site)
        - Secondary keys ensure consistent ordering when primary values match
        - Lambda functions create dynamic sort keys based on user selection

        Supported Sort Fields:
        - 'year': Sort by survey year (with site as tiebreaker)
        - 'site': Sort by site identification (with year as tiebreaker)
        - 'species': Sort by species code (with year as tiebreaker)
        - 'count': Sort by observation count (with year as tiebreaker)
        - 'diver': Sort by diver identification (with year as tiebreaker)
        - 'transect': Sort by transect number (with year as tiebreaker)

        Args:
            sort_by (str): Field to sort by - options: 'year', 'site', 'species', 'count', 'diver', 'transect'
            reverse (bool): If True, sort in descending order; if False, ascending order (default)

        Returns:
            bool: True if sorting successful, False if error or no records to sort

        Example:
            >>> manager.sort_records(sort_by="year", reverse=False)  # Ascending by year
            >>> manager.sort_records(sort_by="count", reverse=True)  # Descending by count
        """
        try:
            if not self.records:
                print("No records to sort.")
                return False

            # Define key functions for different sorting criteria
            sort_keys = {
                'year': lambda record: (record.get_year(), record.get_site_identification()),
                'site': lambda record: (record.get_site_identification(), record.get_year()),
                'species': lambda record: (record.get_species_code(), record.get_year()),
                'count': lambda record: (record.get_count(), record.get_year()),
                'diver': lambda record: (record.get_diver_identication(), record.get_year()),
                'transect': lambda record: (record.get_transect(), record.get_year())
            }

            # Validate sort criteria
            if sort_by not in sort_keys:
                print(f"Invalid sort criteria: {sort_by}")
                return False

            # Sort records using the appropriate key function
            self.records.sort(key=sort_keys[sort_by], reverse=reverse)

            return True

        except Exception as e:
            print(f"Failed to sort records: {e}")
            return False

    def sort_records_by_multiple_criteria(self, criteria_list):
        """
        Sort records by multiple criteria in order of priority.
        Advanced sorting feature demonstrating compound key sorting with hierarchical ordering.

        Algorithm Details:
        - Builds composite sort key from multiple field values
        - Primary criterion has highest priority, secondary has next priority, etc.
        - Uses tuple comparison for natural multi-level sorting
        - Time Complexity: O(n log n) with compound key evaluation O(k) where k is criteria count

        Compound Key Construction:
        - Creates tuple of values in priority order: (primary_value, secondary_value, ...)
        - Python's tuple comparison automatically handles multi-level sorting
        - Each level is compared only when previous levels are equal

        Implementation Strategy:
        - Dynamic key function generated based on user-specified criteria
        - Supports any combination of available sort fields
        - Primary criterion's reverse flag determines overall sort direction

        Use Cases:
        - Sort by site, then by year within each site
        - Sort by species, then by count within each species
        - Complex hierarchical data organization

        Args:
            criteria_list (list): List of tuples (field, reverse) where field is the sort field
                                 and reverse is boolean for sort order
                                 Example: [('year', False), ('species', False)]
                                 First tuple is primary criterion, second is secondary, etc.

        Returns:
            bool: True if sorting successful, False if error, no records, or invalid criteria

        Example:
            >>> criteria = [('site', False), ('year', False)]
            >>> manager.sort_records_by_multiple_criteria(criteria)  # Sort by site, then year
        """
        try:
            if not self.records:
                print("No records to sort.")
                return False

            if not criteria_list:
                print("No sorting criteria provided.")
                return False

            # Build compound key function
            def compound_key(record):
                key_values = []
                for field, _ in criteria_list:
                    if field == 'year':
                        key_values.append(record.get_year())
                    elif field == 'site':
                        key_values.append(record.get_site_identification())
                    elif field == 'species':
                        key_values.append(record.get_species_code())
                    elif field == 'count':
                        key_values.append(record.get_count())
                    elif field == 'diver':
                        key_values.append(record.get_diver_identication())
                    elif field == 'transect':
                        key_values.append(record.get_transect())
                return tuple(key_values)

            # Sort using compound key (primary criterion determines overall reverse)
            primary_reverse = criteria_list[0][1] if criteria_list else False
            self.records.sort(key=compound_key, reverse=primary_reverse)

            return True

        except Exception as e:
            print(f"Failed to sort records by multiple criteria: {e}")
            return False

    def get_sorted_copy(self, sort_by="year", reverse=False):
        """
        Get a sorted copy of records without modifying the original list.
        Demonstrates non-destructive sorting operation for data structure preservation.

        Algorithm Details:
        - Uses Python's sorted() function which creates a new list
        - Original self.records list remains unchanged
        - Maintains data integrity while providing sorted view
        - Memory efficient: only creates copy when needed

        Non-Destructive Strategy:
        - Original data structure preserved for continued operations
        - Allows multiple sorted views without data loss
        - Useful for preview operations before committing sort
        - Enables comparison between sorted and unsorted data

        Use Cases:
        - Preview sorted data before applying permanent sort
        - Generate reports without altering working dataset
        - Maintain original load order while displaying sorted view
        - Testing and validation of sort algorithms

        Args:
            sort_by (str): Field to sort by - same options as sort_records()
            reverse (bool): Sort order (True=descending, False=ascending)

        Returns:
            list: New sorted list of KelpFishRecord objects, or empty list if error/no records

        Example:
            >>> sorted_view = manager.get_sorted_copy(sort_by="species")
            >>> # Original manager.records unchanged
        """
        try:
            if not self.records:
                return []

            sort_keys = {
                'year': lambda record: (record.get_year(), record.get_site_identification()),
                'site': lambda record: (record.get_site_identification(), record.get_year()),
                'species': lambda record: (record.get_species_code(), record.get_year()),
                'count': lambda record: (record.get_count(), record.get_year()),
                'diver': lambda record: (record.get_diver_identication(), record.get_year()),
                'transect': lambda record: (record.get_transect(), record.get_year())
            }

            if sort_by not in sort_keys:
                return []

            # Use sorted() to create new sorted list
            return sorted(self.records, key=sort_keys[sort_by], reverse=reverse)

        except Exception as e:
            print(f"Failed to create sorted copy: {e}")
            return []

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
