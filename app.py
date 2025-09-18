"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: October 12, 2025
Author: Jefperry Achu Chi

app.py - Main application entry point for the layered architecture kelp fish data manager
"""

from presentation.console_interface import ConsoleInterface
import sys
import os

# Add the current directory to the Python path to enable imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    """
    Main function to start the application.
    Demonstrates layered architecture with Presentation, Business, Persistence, and Model layers.
    """
    try:
        # Create and run the console interface (Presentation layer)
        app = ConsoleInterface()
        app.run()

    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        print("Program by Jefperry Achu Chi")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Program by Jefperry Achu Chi")


if __name__ == "__main__":
    main()
