"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: October 12, 2025
Author: Jefperry Achu Chi

run_tests.py - Test runner that properly handles imports
"""

import sys
import os
import unittest

# Add the current directory to the Python path to enable imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import test modules
from tests.test_kelp_fish_manager import TestKelpFishManager


def main():
    """
    Main function to run unit tests with proper header.
    """
    print("=" * 60)
    print("Running Unit Tests for Kelp Fish Manager")
    print("Program by: Jefperry Achu Chi")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestKelpFishManager)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print(f"Tests completed by: Jefperry Achu Chi")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 60)


if __name__ == "__main__":
    main()