"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: [Due Date]
Author: Jefperry Achu Chi

data_access.py - Persistence layer: Handles all File-IO operations for CSV data
"""

import csv
import uuid
import os
from model.kelp_fish_record import KelpFishRecord


class DataAccess:
    """
    Persistence layer class responsible for all File-IO operations.
    Handles reading from and writing to CSV files with proper exception handling.
    """

    def __init__(self):
        """
        Initialize the DataAccess object.
        """
        self.dataset_filename = "pacific_rim_npr_coastalmarine_kelp_fish_community_2008-2016_data.csv"

    def read_kelp_fish_data(self, max_records=100):
        """
        Read kelp fish community data from CSV file and create record objects.

        Args:
            max_records (int): Maximum number of records to read (default 100)

        Returns:
            list: List of KelpFishRecord objects

        Raises:
            FileNotFoundError: If the CSV file is not found
            Exception: For other file reading errors
        """
        records = []

        try:
            with open(self.dataset_filename, 'r', newline='', encoding='utf-8') as csvfile:
                # Use csv.reader API to properly handle CSV format
                csv_reader = csv.reader(csvfile)

                # Skip the header row (first row)
                next(csv_reader)

                # Read up to max_records for the application
                record_count = 0
                for row in csv_reader:
                    if record_count >= max_records:
                        break

                    if len(row) >= 8:  # Ensure we have all required columns
                        # Create KelpFishRecord object using dataset column names
                        record = KelpFishRecord(
                            site_identification=row[0].strip(),
                            year=int(row[1]) if row[1].strip() else 0,
                            diver_identication=int(
                                row[2]) if row[2].strip() else 0,
                            transect=int(row[3]) if row[3].strip() else 0,
                            average_depth_ft=row[4].strip(),
                            species_code=row[5].strip(),
                            count=int(row[6]) if row[6].strip() else 0,
                            survey_type=row[7].strip()
                        )
                        records.append(record)
                        record_count += 1

        except FileNotFoundError:
            print(f"Error: The file '{self.dataset_filename}' was not found.")
            print("Please ensure the CSV file is in the correct location.")
            raise
        except Exception as e:
            print(f"Error reading the file: {e}")
            raise

        return records

    def write_kelp_fish_data(self, records):
        """
        Write kelp fish community data to a new CSV file with GUID/UUID filename.

        Args:
            records (list): List of KelpFishRecord objects to write

        Returns:
            str: The filename of the created file

        Raises:
            Exception: For file writing errors
        """
        # Generate GUID/UUID for filename using API
        file_guid = str(uuid.uuid4())
        output_filename = f"kelp_fish_export_{file_guid}.csv"

        try:
            with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
                # Use csv.writer API to properly handle CSV format
                csv_writer = csv.writer(csvfile)

                # Write header row with dataset column names
                csv_writer.writerow([
                    'Site identification',
                    'Year',
                    'Diver identication',
                    'Transect',
                    'Average depth (ft)',
                    'Species code',
                    'Count',
                    'Survey type'
                ])

                # Write record data
                for record in records:
                    csv_writer.writerow([
                        record.get_site_identification(),
                        record.get_year(),
                        record.get_diver_identication(),
                        record.get_transect(),
                        record.get_average_depth_ft(),
                        record.get_species_code(),
                        record.get_count(),
                        record.get_survey_type()
                    ])

            print(f"Data successfully exported to: {output_filename}")
            return output_filename

        except Exception as e:
            print(f"Error writing to file: {e}")
            raise

    def file_exists(self, filename=None):
        """
        Check if the dataset file exists.

        Args:
            filename (str): Optional filename to check, defaults to dataset filename

        Returns:
            bool: True if file exists, False otherwise
        """
        if filename is None:
            filename = self.dataset_filename
        return os.path.isfile(filename)

    def get_dataset_filename(self):
        """
        Get the current dataset filename.

        Returns:
            str: The dataset filename
        """
        return self.dataset_filename

    def set_dataset_filename(self, filename):
        """
        Set a new dataset filename.

        Args:
            filename (str): New dataset filename
        """
        self.dataset_filename = filename
