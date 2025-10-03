"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: October 12, 2025
Author: Jefperry Achu Chi

console_interface.py - Presentation layer: Handles all user interactions and display logic
"""

from model.kelp_fish_record import KelpFishRecord
from business.kelp_fish_manager import KelpFishManager
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ConsoleInterface:
    """
    Presentation layer class that handles all user interactions.
    Provides console-based interface with menu system for the application.
    """

    def __init__(self):
        """
        Initialize the ConsoleInterface with business manager.
        """
        self.manager = KelpFishManager()
        self.author_name = "Jefperry Achu Chi"

    def display_header(self):
        """
        Display the application header with author name.
        """
        print()
        print("Pacific Rim NPR Coastal Marine Kelp Fish Community Data Manager")
        print(f"Program by: {self.author_name}")
        print()
        print()

    def display_menu(self):
        """
        Display the main menu options.
        """
        print()
        print(f"MAIN MENU - Program by {self.author_name}")
        print()
        print("1. Load/Reload Data from Dataset")
        print("2. Display Records")
        print("3. Search Records")
        print("4. Create New Record")
        print("5. Edit Record")
        print("6. Delete Record")
        print("7. Persist Data to File")
        print("8. Show Statistics")
        print("9. Exit")
        print()

    def get_user_choice(self):
        """
        Get user menu choice with input validation.

        Returns:
            int: User's menu choice, or -1 if invalid
        """
        try:
            choice = input(
                f"\nEnter your choice (1-9) - {self.author_name}: ").strip()
            return int(choice)
        except ValueError:
            return -1

    def load_data_menu(self):
        """
        Handle loading/reloading data from dataset.
        """
        print(f"\n--- Load/Reload Data - {self.author_name} ---")
        try:
            max_records = input(
                "Enter max records to load (default 100): ").strip()
            max_records = int(max_records) if max_records else 100

            print("Loading data from dataset...")
            if self.manager.reload_data(max_records):
                count = self.manager.get_record_count()
                print(f"Successfully loaded {count} records from dataset.")
            else:
                print("Failed to load data from dataset.")
        except ValueError:
            print("Invalid number entered. Using default of 100 records.")
            if self.manager.reload_data(100):
                count = self.manager.get_record_count()
                print(f"Successfully loaded {count} records from dataset.")

    def display_records_menu(self):
        """
        Handle displaying records with various options.
        """
        print(f"\n-Display Records - {self.author_name} ")
        print("1. Display all records")
        print("2. Display single record by index")
        print("3. Display records by site")
        print("4. Display records by species")

        try:
            choice = int(input("Choose display option (1-4): "))

            if choice == 1:
                self.display_all_records()
            elif choice == 2:
                self.display_single_record()
            elif choice == 3:
                self.display_records_by_site()
            elif choice == 4:
                self.display_records_by_species()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

    def display_all_records(self):
        """
        Display all records in memory.
        """
        records = self.manager.get_all_records()
        if not records:
            print("No records in memory. Please load data first.")
            return

        print(
            f"\n--- All Records ({len(records)} total) - {self.author_name} ---")
        for i, record in enumerate(records):
            print(f"\nRecord {i + 1}:")
            self.print_record_details(record)

            # Display author name every 10 records as required
            if (i + 1) % 10 == 0:
                print(
                    f"\n*** Program by {self.author_name} - Record {i + 1} of {len(records)} ***")

    def display_single_record(self):
        """
        Display a single record by index.
        """
        try:
            index = int(input("Enter record index (1-based): ")) - 1
            record = self.manager.get_record_by_index(index)

            if record:
                print(
                    f"\n--- Record at Index {index + 1} - {self.author_name} ---")
                self.print_record_details(record)
            else:
                print("Invalid index or no record found.")
        except ValueError:
            print("Invalid index entered.")

    def display_records_by_site(self):
        """
        Display records filtered by site identification.
        """
        site = input("Enter site identification: ").strip()
        records = self.manager.get_records_by_site(site)

        if records:
            print(
                f"\n--- Records for Site '{site}' ({len(records)} found) - {self.author_name} ---")
            for i, record in enumerate(records, 1):
                print(f"\nRecord {i}:")
                self.print_record_details(record)
        else:
            print(f"No records found for site '{site}'.")

    def display_records_by_species(self):
        """
        Display records filtered by species code.
        """
        species = input("Enter species code: ").strip()
        records = self.manager.get_records_by_species(species)

        if records:
            print(
                f"\n--- Records for Species '{species}' ({len(records)} found) - {self.author_name} ---")
            for i, record in enumerate(records, 1):
                print(f"\nRecord {i}:")
                self.print_record_details(record)
        else:
            print(f"No records found for species '{species}'.")

    def search_records_menu(self):
        """
        Handle searching records by any field.
        """
        print(f"\n--- Search Records - {self.author_name} ---")
        search_term = input("Enter search term: ").strip()

        if search_term:
            records = self.manager.search_records(search_term)
            if records:
                print(
                    f"\n--- Search Results for '{search_term}' ({len(records)} found) - {self.author_name} ---")
                for i, record in enumerate(records, 1):
                    print(f"\nResult {i}:")
                    self.print_record_details(record)
            else:
                print(f"No records found containing '{search_term}'.")
        else:
            print("Search term cannot be empty.")

    def create_record_menu(self):
        """
        Handle creating a new record.
        """
        print(f"\n--- Create New Record - {self.author_name} ---")
        print("Enter the following information for the new record:")

        try:
            # Get input for all dataset column names
            site_identification = input("Site identification: ").strip()
            year = int(input("Year: "))
            diver_identication = int(input("Diver identification: "))
            transect = int(input("Transect: "))
            average_depth_ft = input("Average depth (ft) [optional]: ").strip()
            species_code = input("Species code: ").strip()
            count = int(input("Count: "))
            survey_type = input("Survey type: ").strip()

            # Validate the data
            is_valid, error_msg = self.manager.validate_record_data(
                site_identification, year, diver_identication, transect,
                average_depth_ft, species_code, count, survey_type
            )

            if is_valid:
                # Create new record with dataset column names
                new_record = KelpFishRecord(
                    site_identification=site_identification,
                    year=year,
                    diver_identication=diver_identication,
                    transect=transect,
                    average_depth_ft=average_depth_ft,
                    species_code=species_code,
                    count=count,
                    survey_type=survey_type
                )

                if self.manager.add_record(new_record):
                    print("Record created successfully!")
                    print(
                        f"Total records in memory: {self.manager.get_record_count()}")
                else:
                    print("Failed to create record.")
            else:
                print(f"Validation error: {error_msg}")

        except ValueError:
            print("Invalid input. Please ensure numeric fields contain valid numbers.")

    def edit_record_menu(self):
        """
        Handle editing an existing record.
        """
        print(f"\n--- Edit Record - {self.author_name} ---")

        try:
            index = int(input("Enter record index to edit (1-based): ")) - 1
            current_record = self.manager.get_record_by_index(index)

            if not current_record:
                print("Invalid index or no record found.")
                return

            print(f"\nCurrent record at index {index + 1}:")
            self.print_record_details(current_record)

            print("\nEnter new values (press Enter to keep current value):")

            # Get new values with current values as defaults
            site_identification = input(
                f"Site identification [{current_record.get_site_identification()}]: ").strip()
            site_identification = site_identification if site_identification else current_record.get_site_identification()

            year_input = input(f"Year [{current_record.get_year()}]: ").strip()
            year = int(year_input) if year_input else current_record.get_year()

            diver_input = input(
                f"Diver identification [{current_record.get_diver_identication()}]: ").strip()
            diver_identication = int(
                diver_input) if diver_input else current_record.get_diver_identication()

            transect_input = input(
                f"Transect [{current_record.get_transect()}]: ").strip()
            transect = int(
                transect_input) if transect_input else current_record.get_transect()

            average_depth_ft = input(
                f"Average depth (ft) [{current_record.get_average_depth_ft()}]: ").strip()
            average_depth_ft = average_depth_ft if average_depth_ft else current_record.get_average_depth_ft()

            species_code = input(
                f"Species code [{current_record.get_species_code()}]: ").strip()
            species_code = species_code if species_code else current_record.get_species_code()

            count_input = input(
                f"Count [{current_record.get_count()}]: ").strip()
            count = int(
                count_input) if count_input else current_record.get_count()

            survey_type = input(
                f"Survey type [{current_record.get_survey_type()}]: ").strip()
            survey_type = survey_type if survey_type else current_record.get_survey_type()

            # Validate the data
            is_valid, error_msg = self.manager.validate_record_data(
                site_identification, year, diver_identication, transect,
                average_depth_ft, species_code, count, survey_type
            )

            if is_valid:
                # Create updated record
                updated_record = KelpFishRecord(
                    site_identification=site_identification,
                    year=year,
                    diver_identication=diver_identication,
                    transect=transect,
                    average_depth_ft=average_depth_ft,
                    species_code=species_code,
                    count=count,
                    survey_type=survey_type
                )

                if self.manager.update_record(index, updated_record):
                    print("Record updated successfully!")
                else:
                    print("Failed to update record.")
            else:
                print(f"Validation error: {error_msg}")

        except ValueError:
            print("Invalid input. Please ensure numeric fields contain valid numbers.")

    def delete_record_menu(self):
        """
        Handle deleting a record.
        """
        print(f"\n--- Delete Record - {self.author_name} ---")

        try:
            index = int(input("Enter record index to delete (1-based): ")) - 1
            record = self.manager.get_record_by_index(index)

            if not record:
                print("Invalid index or no record found.")
                return

            print(f"\nRecord to be deleted (index {index + 1}):")
            self.print_record_details(record)

            confirm = input(
                "\nAre you sure you want to delete this record? (y/N): ").strip().lower()

            if confirm == 'y' or confirm == 'yes':
                if self.manager.delete_record(index):
                    print("Record deleted successfully!")
                    print(
                        f"Total records in memory: {self.manager.get_record_count()}")
                else:
                    print("Failed to delete record.")
            else:
                print("Delete operation cancelled.")

        except ValueError:
            print("Invalid index entered.")

    def persist_data_menu(self):
        """
        Handle persisting data to file with GUID filename.
        """
        print(f"\n--- Persist Data to File - {self.author_name} ---")

        if self.manager.get_record_count() == 0:
            print("No data to persist. Please load data first.")
            return

        print(
            f"Persisting {self.manager.get_record_count()} records to CSV file...")
        filename = self.manager.persist_data()

        if filename:
            print(f"Data successfully persisted to: {filename}")
        else:
            print("Failed to persist data.")

    def show_statistics_menu(self):
        """
        Display statistics about the current data.
        """
        print(f"\n--- Data Statistics - {self.author_name} ---")

        total_records = self.manager.get_record_count()
        if total_records == 0:
            print("No data loaded. Please load data first.")
            return

        records = self.manager.get_all_records()

        # Count unique sites
        sites = set(record.get_site_identification() for record in records)

        # Count unique species
        species = set(record.get_species_code() for record in records)

        # Count by year
        years = {}
        for record in records:
            year = record.get_year()
            years[year] = years.get(year, 0) + 1

        print(f"Total Records: {total_records}")
        print(f"Unique Sites: {len(sites)} - {', '.join(sorted(sites))}")
        print(f"Unique Species: {len(species)} - {', '.join(sorted(species))}")
        print("Records by Year:")
        for year in sorted(years.keys()):
            print(f"  {year}: {years[year]} records")

    def print_record_details(self, record):
        """
        Print formatted details of a single record using dataset column names.

        Args:
            record (KelpFishRecord): Record to display
        """
        print(f"  Site Identification: {record.get_site_identification()}")
        print(f"  Year: {record.get_year()}")
        print(f"  Diver Identification: {record.get_diver_identication()}")
        print(f"  Transect: {record.get_transect()}")
        print(
            f"  Average Depth (ft): {record.get_average_depth_ft() if record.get_average_depth_ft() else 'N/A'}")
        print(f"  Species Code: {record.get_species_code()}")
        print(f"  Count: {record.get_count()}")
        print(f"  Survey Type: {record.get_survey_type()}")

    def run(self):
        """
        Main application loop with menu system and decision structures.
        """
        self.display_header()

        # Load initial data
        print("Loading initial data from dataset...")
        if self.manager.load_data(100):
            count = self.manager.get_record_count()
            print(f"Successfully loaded {count} records from dataset.\n")
        else:
            print("Failed to load initial data. You can try again from the menu.\n")

        # Main menu loop with decision structure
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            # Decision structure for menu handling
            if choice == 1:
                self.load_data_menu()
            elif choice == 2:
                self.display_records_menu()
            elif choice == 3:
                self.search_records_menu()
            elif choice == 4:
                self.create_record_menu()
            elif choice == 5:
                self.edit_record_menu()
            elif choice == 6:
                self.delete_record_menu()
            elif choice == 7:
                self.persist_data_menu()
            elif choice == 8:
                self.show_statistics_menu()
            elif choice == 9:
                print(f"\nThank you for using the Kelp Fish Data Manager!")
                print(f"Program by {self.author_name}")
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

            # Pause for user to see results
            input(
                f"\nPress Enter to continue... (Program by {self.author_name})")
