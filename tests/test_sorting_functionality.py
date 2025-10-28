"""
CST8002 - Data-Driven Programming - Practical Project 3
Professor: Stanley Pieda
Due Date: October 27, 2025
Author: Jefperry Achu Chi

test_sorting_functionality.py - Unit tests for sorting algorithms and data structure operations
Tests the advanced data structure manipulation and sorting functionality added in Project 3
"""

from model.kelp_fish_record import KelpFishRecord
from business.kelp_fish_manager import KelpFishManager
import unittest
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestSortingFunctionality(unittest.TestCase):
    """
    Unit test class for testing sorting algorithms and data structure operations.
    Tests advanced data structure manipulation added in Practical Project 3.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        Creates a set of test records with known values for sorting verification.
        """
        self.manager = KelpFishManager()
        
        # Create test records with varying values for sorting
        self.test_records = [
            KelpFishRecord(
                site_identification="SITE_C",
                year=2015,
                diver_identication=3,
                transect=2,
                average_depth_ft="15",
                species_code="FISH_Z",
                count=10,
                survey_type="test survey"
            ),
            KelpFishRecord(
                site_identification="SITE_A",
                year=2010,
                diver_identication=1,
                transect=1,
                average_depth_ft="10",
                species_code="FISH_A",
                count=5,
                survey_type="test survey"
            ),
            KelpFishRecord(
                site_identification="SITE_B",
                year=2020,
                diver_identication=2,
                transect=3,
                average_depth_ft="20",
                species_code="FISH_M",
                count=15,
                survey_type="test survey"
            ),
            KelpFishRecord(
                site_identification="SITE_A",
                year=2012,
                diver_identication=4,
                transect=1,
                average_depth_ft="12",
                species_code="FISH_B",
                count=8,
                survey_type="test survey"
            ),
            KelpFishRecord(
                site_identification="SITE_C",
                year=2010,
                diver_identication=5,
                transect=2,
                average_depth_ft="18",
                species_code="FISH_C",
                count=3,
                survey_type="test survey"
            )
        ]
        
        # Add all test records to manager
        for record in self.test_records:
            self.manager.add_record(record)

    def test_sort_by_year_ascending(self):
        """
        Unit test: Does the program correctly sort records by year in ascending order?
        
        This test verifies that the sorting algorithm correctly orders records
        by year from oldest to newest.
        """
        # Act - sort by year ascending
        success = self.manager.sort_records(sort_by="year", reverse=False)
        
        # Assert - verify sorting was successful
        self.assertTrue(success, "Sorting by year should succeed")
        
        # Get sorted records
        sorted_records = self.manager.get_all_records()
        
        # Verify records are in ascending year order
        self.assertEqual(sorted_records[0].get_year(), 2010)
        self.assertEqual(sorted_records[-1].get_year(), 2020)
        
        # Verify the list is properly sorted
        for i in range(len(sorted_records) - 1):
            self.assertLessEqual(sorted_records[i].get_year(), 
                               sorted_records[i + 1].get_year(),
                               "Records should be sorted by year in ascending order")

    def test_sort_by_year_descending(self):
        """
        Unit test: Does the program correctly sort records by year in descending order?
        
        This test verifies that the sorting algorithm correctly orders records
        by year from newest to oldest.
        """
        # Act - sort by year descending
        success = self.manager.sort_records(sort_by="year", reverse=True)
        
        # Assert - verify sorting was successful
        self.assertTrue(success, "Sorting by year descending should succeed")
        
        # Get sorted records
        sorted_records = self.manager.get_all_records()
        
        # Verify records are in descending year order
        self.assertEqual(sorted_records[0].get_year(), 2020)
        self.assertEqual(sorted_records[-1].get_year(), 2010)
        
        # Verify the list is properly sorted in reverse
        for i in range(len(sorted_records) - 1):
            self.assertGreaterEqual(sorted_records[i].get_year(), 
                                  sorted_records[i + 1].get_year(),
                                  "Records should be sorted by year in descending order")

    def test_sort_by_site_identification(self):
        """
        Unit test: Does the program correctly sort records by site identification?
        
        This test verifies that the sorting algorithm correctly orders records
        alphabetically by site identification.
        """
        # Act - sort by site
        success = self.manager.sort_records(sort_by="site", reverse=False)
        
        # Assert - verify sorting was successful
        self.assertTrue(success, "Sorting by site should succeed")
        
        # Get sorted records
        sorted_records = self.manager.get_all_records()
        
        # Verify records are in alphabetical order by site
        self.assertEqual(sorted_records[0].get_site_identification(), "SITE_A")
        self.assertEqual(sorted_records[-1].get_site_identification(), "SITE_C")
        
        # Verify alphabetical ordering
        for i in range(len(sorted_records) - 1):
            self.assertLessEqual(sorted_records[i].get_site_identification(), 
                               sorted_records[i + 1].get_site_identification(),
                               "Records should be sorted alphabetically by site")

    def test_sort_by_species_code(self):
        """
        Unit test: Does the program correctly sort records by species code?
        
        This test verifies that the sorting algorithm correctly orders records
        by species code alphabetically.
        """
        # Act - sort by species
        success = self.manager.sort_records(sort_by="species", reverse=False)
        
        # Assert - verify sorting was successful
        self.assertTrue(success, "Sorting by species should succeed")
        
        # Get sorted records
        sorted_records = self.manager.get_all_records()
        
        # Verify records are sorted by species code
        self.assertEqual(sorted_records[0].get_species_code(), "FISH_A")
        self.assertEqual(sorted_records[-1].get_species_code(), "FISH_Z")

    def test_sort_by_count(self):
        """
        Unit test: Does the program correctly sort records by count?
        
        This test verifies that the sorting algorithm correctly orders records
        by numeric count value.
        """
        # Act - sort by count ascending
        success = self.manager.sort_records(sort_by="count", reverse=False)
        
        # Assert - verify sorting was successful
        self.assertTrue(success, "Sorting by count should succeed")
        
        # Get sorted records
        sorted_records = self.manager.get_all_records()
        
        # Verify records are in ascending count order
        self.assertEqual(sorted_records[0].get_count(), 3)
        self.assertEqual(sorted_records[-1].get_count(), 15)
        
        # Verify numeric ordering
        for i in range(len(sorted_records) - 1):
            self.assertLessEqual(sorted_records[i].get_count(), 
                               sorted_records[i + 1].get_count(),
                               "Records should be sorted by count in ascending order")

    def test_sort_by_multiple_criteria(self):
        """
        Unit test: Does the program correctly sort records by multiple criteria?
        
        This test verifies that the compound sorting algorithm correctly orders records
        using multiple sort keys in priority order.
        """
        # Arrange - criteria list: primary by site, secondary by year
        criteria = [('site', False), ('year', False)]
        
        # Act - sort by multiple criteria
        success = self.manager.sort_records_by_multiple_criteria(criteria)
        
        # Assert - verify sorting was successful
        self.assertTrue(success, "Multiple criteria sorting should succeed")
        
        # Get sorted records
        sorted_records = self.manager.get_all_records()
        
        # Verify primary sort (site) is correct
        self.assertEqual(sorted_records[0].get_site_identification(), "SITE_A")
        
        # Verify secondary sort within same site
        # Find all SITE_A records and verify they are sorted by year
        site_a_records = [r for r in sorted_records if r.get_site_identification() == "SITE_A"]
        if len(site_a_records) > 1:
            for i in range(len(site_a_records) - 1):
                self.assertLessEqual(site_a_records[i].get_year(), 
                                   site_a_records[i + 1].get_year(),
                                   "Within same site, records should be sorted by year")

    def test_get_sorted_copy_non_destructive(self):
        """
        Unit test: Does get_sorted_copy return a sorted list without modifying the original?
        
        This test verifies that the non-destructive sorting method returns a sorted copy
        while leaving the original data structure unchanged.
        """
        # Arrange - get original order
        original_records = self.manager.get_all_records()
        original_first_year = original_records[0].get_year()
        
        # Act - get sorted copy
        sorted_copy = self.manager.get_sorted_copy(sort_by="year", reverse=False)
        
        # Assert - verify sorted copy is different from original
        self.assertNotEqual(original_first_year, sorted_copy[0].get_year(),
                          "Sorted copy should have different order than original")
        
        # Verify original is unchanged
        current_records = self.manager.get_all_records()
        self.assertEqual(current_records[0].get_year(), original_first_year,
                        "Original records should remain unchanged")
        
        # Verify sorted copy is properly sorted
        self.assertEqual(sorted_copy[0].get_year(), 2010,
                        "Sorted copy should start with earliest year")

    def test_sort_empty_records(self):
        """
        Unit test: Does the program handle sorting of empty record list gracefully?
        
        This test verifies that sorting an empty data structure doesn't cause errors.
        """
        # Arrange - create empty manager
        empty_manager = KelpFishManager()
        
        # Act - attempt to sort empty list
        success = empty_manager.sort_records(sort_by="year")
        
        # Assert - should return False but not crash
        self.assertFalse(success, "Sorting empty records should return False")

    def test_sort_with_invalid_criteria(self):
        """
        Unit test: Does the program handle invalid sort criteria properly?
        
        This test verifies that invalid sort field names are rejected gracefully.
        """
        # Act - attempt to sort with invalid criteria
        success = self.manager.sort_records(sort_by="invalid_field")
        
        # Assert - should return False
        self.assertFalse(success, "Invalid sort criteria should return False")

    def test_record_comparison_operators(self):
        """
        Unit test: Do the KelpFishRecord comparison operators work correctly?
        
        This test verifies that the comparison operators implemented for sorting
        work correctly at the object level.
        """
        # Arrange - create two records with different years
        record1 = KelpFishRecord(site_identification="SITE_A", year=2010, species_code="FISH_A", count=5)
        record2 = KelpFishRecord(site_identification="SITE_A", year=2015, species_code="FISH_B", count=10)
        
        # Assert - test comparison operators
        self.assertTrue(record1 < record2, "Record with earlier year should be less than record with later year")
        self.assertTrue(record2 > record1, "Record with later year should be greater than record with earlier year")
        self.assertTrue(record1 <= record2, "Less than or equal should work")
        self.assertTrue(record2 >= record1, "Greater than or equal should work")
        self.assertFalse(record1 == record2, "Different records should not be equal")

    def tearDown(self):
        """
        Clean up after each test method.
        """
        # Reset the manager for next test
        self.manager = None


if __name__ == "__main__":
    # Run the unit tests
    print("=" * 70)
    print("Running Unit Tests for Sorting Functionality - Project 3")
    print("Program by: Jefperry Achu Chi")
    print("=" * 70)
    print()

    unittest.main(verbosity=2)
