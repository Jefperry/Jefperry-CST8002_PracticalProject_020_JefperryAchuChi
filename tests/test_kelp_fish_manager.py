"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: October 12, 2025
Author: Jefperry Achu Chi

test_kelp_fish_manager.py - Unit tests for KelpFishManager business logic
"""

from model.kelp_fish_record import KelpFishRecord
from business.kelp_fish_manager import KelpFishManager
import unittest
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestKelpFishManager(unittest.TestCase):
    """
    Unit test class for testing KelpFishManager functionality.
    Tests business layer operations and data management.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        """
        self.manager = KelpFishManager()
        # Create test data
        self.test_record = KelpFishRecord(
            site_identification="TEST",
            year=2023,
            diver_identication=1,
            transect=1,
            average_depth_ft="10",
            species_code="TESTFISH",
            count=5,
            survey_type="test survey"
        )

    def test_add_record_to_memory_structure(self):
        """
        Unit test: Does the program add a new record into the sequential data structure?

        This test verifies that the business layer correctly adds a new record
        to the in-memory data structure and that the record can be retrieved.
        """
        # Arrange - setup is done in setUp()
        initial_count = self.manager.get_record_count()

        # Act - add the test record
        success = self.manager.add_record(self.test_record)

        # Assert - verify the record was added successfully
        self.assertTrue(success, "Record should be added successfully")
        self.assertEqual(self.manager.get_record_count(), initial_count + 1,
                         "Record count should increase by 1")

        # Verify the record is actually in the data structure
        all_records = self.manager.get_all_records()
        added_record = all_records[-1]  # Should be the last record added

        self.assertEqual(added_record.get_site_identification(), "TEST")
        self.assertEqual(added_record.get_year(), 2023)
        self.assertEqual(added_record.get_species_code(), "TESTFISH")
        self.assertEqual(added_record.get_count(), 5)

    def test_validation_for_invalid_record(self):
        """
        Additional test: Does the program handle invalid record types correctly?

        This test verifies that the business layer correctly rejects non-KelpFishRecord objects.
        """
        # Test with invalid object type (string instead of KelpFishRecord)
        success = self.manager.add_record("invalid_record")

        self.assertFalse(success, "Should reject non-KelpFishRecord objects")

    def tearDown(self):
        """
        Clean up after each test method.
        """
        # Reset the manager for next test
        self.manager = None


if __name__ == "__main__":
    # Run the unit tests
    print()
    print("Running Unit Tests for Kelp Fish Manager")
    print("Program by: Jefperry Achu Chi")
    print()

    unittest.main(verbosity=2)
