"""
CST8002 - Data-Driven Programming
Professor: Stanley Pieda
Due Date: [Due Date]
Author: Jefperry Achu Chi

main.py - Main program for reading and processing Pacific Rim NPR Coastal Marine Kelp Fish Community data
"""

import csv
from KelpFishRecord import KelpFishRecord

def read_kelp_fish_data(filename):
    """
    Read kelp fish community data from CSV file and create record objects.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of KelpFishRecord objects
        
    Raises:
        FileNotFoundError: If the CSV file is not found
        Exception: For other file reading errors
    """
    records = []
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            # Use csv.reader to properly handle CSV format
            csv_reader = csv.reader(csvfile)
            
            # Skip the header row (first row)
            next(csv_reader)
            
            # Read first few records for demonstration
            record_count = 0
            for row in csv_reader:
                if record_count >= 10:  # Limit to first 10 records for demonstration
                    break
                    
                if len(row) >= 8:  # Ensure we have all required columns
                    # Create KelpFishRecord object using column names from dataset
                    record = KelpFishRecord(
                        site_identification=row[0].strip(),
                        year=int(row[1]) if row[1].strip() else 0,
                        diver_identication=int(row[2]) if row[2].strip() else 0,
                        transect=int(row[3]) if row[3].strip() else 0,
                        average_depth_ft=row[4].strip(),
                        species_code=row[5].strip(),
                        count=int(row[6]) if row[6].strip() else 0,
                        survey_type=row[7].strip()
                    )
                    records.append(record)
                    record_count += 1
                    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please ensure the CSV file is in the correct location.")
        raise
    except Exception as e:
        print(f"Error reading the file: {e}")
        raise
    
    return records

def main():
    """
    Main function to execute the program.
    """
    print("=" * 60)
    print("Pacific Rim NPR Coastal Marine Kelp Fish Community Data")
    print("=" * 60)
    print()
    
    # CSV filename - using the exact dataset column names in processing
    csv_filename = "pacific_rim_npr_coastalmarine_kelp_fish_community_2008-2016_data.csv"
    
    try:
        # Read data from CSV file using File-IO
        kelp_fish_records = read_kelp_fish_data(csv_filename)
        
        if kelp_fish_records:
            print(f"Successfully loaded {len(kelp_fish_records)} records from the dataset.")
            print()
        else:
            print("No records were loaded from the dataset.")
            
    except Exception:
        # Exception handling for file operations
        print("Program terminated due to file reading error.")
        return

if __name__ == "__main__":
    main()