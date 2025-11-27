# CST8002 Practical Project 4 - Advanced Multi-Column Filtering

**Author:** Jefperry Achu Chi  
**Professor:** Stanley Pieda  
**Due Date:** November 30, 2025  
**Course:** CST8002 - Data-Driven Programming

## Project Overview

This project implements an **Advanced Multi-Column Filtering** feature for the Pacific Rim NPR Coastal Marine Kelp Fish Community Data Manager. The application uses a layered architecture (Model, Business, Persistence, Presentation) to manage and analyze kelp fish survey data.

## Project 4 Features

### Advanced Multi-Column Filtering

- **Field-Specific Matching:** Filter records by any combination of fields (year, site, species, count, diver, transect, survey_type)
- **AND Logic:** Find records that match ALL specified criteria
- **OR Logic:** Find records that match AT LEAST ONE criterion
- **Interactive UI:** User-friendly interface to build complex filter queries step-by-step
- **Result Pagination:** Automatically limits display for large result sets

### Implementation Details

**Model Layer (`model/kelp_fish_record.py`):**

- Added `matches_filter(field_name, value)` method for individual field matching
- Supports case-insensitive string matching and exact numeric matching
- Validates field names against supported fields

**Business Layer (`business/kelp_fish_manager.py`):**

- Implemented `filter_records_advanced(criteria, logic="AND")` method
- Processes list of (field, value) tuples with configurable AND/OR logic
- Returns filtered list of matching KelpFishRecord objects
- Comprehensive error handling and validation

**Presentation Layer (`presentation/console_interface.py`):**

- Added menu option 8: "Advanced Multi-Column Filter"
- Interactive criteria builder with field validation
- Logic selection (AND/OR)
- Result display with pagination for large datasets
- Author name displayed throughout filtering process

## Project Architecture

```
Jefperry-CST8002_PracticalProject_020_JefperryAchuChi/
│
├── model/
│   ├── __init__.py
│   └── kelp_fish_record.py          # Data entity with filtering support
│
├── business/
│   ├── __init__.py
│   └── kelp_fish_manager.py         # Business logic with advanced filtering
│
├── persistence/
│   ├── __init__.py
│   └── data_access.py               # CSV file operations
│
├── presentation/
│   ├── __init__.py
│   └── console_interface.py         # Console UI with filter menu
│
├── tests/
│   ├── __init__.py
│   ├── test_kelp_fish_manager.py
│   └── test_sorting_functionality.py
│
├── app.py                            # Application entry point
├── main.py                           # Alternative entry point
└── pacific_rim_npr_coastalmarine_kelp_fish_community_2008-2016_data.csv
```

## How to Use Advanced Filtering

1. **Launch the application:** Run `python app.py`
2. **Load data:** Select option 1 to load records from the dataset
3. **Access filter menu:** Select option 8 "Advanced Multi-Column Filter"
4. **Choose logic:** Select AND (all criteria match) or OR (any criterion matches)
5. **Add criteria:** Enter field names and values (e.g., year=2015, species=SMYS)
6. **View results:** See all matching records with full details

### Example Filter Scenarios

**Scenario 1: AND Logic**

- Find all SMYS species observations from 2015 at site BLMA
- Criteria: `[('year', 2015), ('species', 'SMYS'), ('site', 'BLMA')]`
- Logic: AND

**Scenario 2: OR Logic**

- Find records from either 2015 or 2016
- Criteria: `[('year', 2015), ('year', 2016)]`
- Logic: OR

## Previous Projects

### Project 3: Sorting Algorithms

- Implemented comparison operators (`__lt__`, `__le__`, `__gt__`, `__ge__`)
- Added single-criterion and multi-criteria sorting
- Non-destructive sorting with `get_sorted_copy()`
- Comprehensive unit tests (10 tests, all passing)

### Project 2: CRUD Operations & Layered Architecture

- Complete CRUD functionality (Create, Read, Update, Delete)
- 4-layer architecture design
- CSV file persistence with GUID filenames
- Input validation and error handling

## Technologies Used

- **Python 3.13+**
- **CSV Module:** For data file operations
- **UUID Module:** For unique filename generation
- **Git/GitHub:** Version control with branching strategy
- **Object-Oriented Programming:** Classes, encapsulation, inheritance

## Running the Application

```powershell
# Navigate to project directory
cd D:\Downloads\Python\Jefperry-CST8002_PracticalProject_020_JefperryAchuChi

# Run the application
python app.py
```

## Git Workflow

```powershell
# View branches
git branch

# Current branch: Practical_Project_04

# Commit history for Project 4:
# - "Update headers and add matches_filter() to model layer"
# - "Implement advanced multi-column filtering in business layer"
# - "Add advanced filter menu to presentation layer"

# To be tagged: V4.0
```

## Evidence of Learning - Project 4

### Concepts Demonstrated

1. **Advanced Filtering Algorithms:** Multi-criteria filtering with boolean logic
2. **Tuple Data Structures:** Using tuples for (field, value) criteria pairs
3. **Interactive UI Design:** Step-by-step criteria building with validation
4. **Boolean Logic Operations:** AND/OR logic for combining filter conditions
5. **Method Chaining:** Calling model methods from business layer
6. **Error Handling:** ValueError for invalid logic parameters
7. **Result Set Management:** Pagination for large result sets
8. **Code Reusability:** Extending existing architecture without breaking changes

### Skills Applied

- Designing user-friendly interactive workflows
- Implementing complex business logic with multiple conditions
- Validating user input against valid field sets
- Managing dynamic data structures (lists of tuples)
- Writing comprehensive docstrings with examples
- Incremental development with Git commits

## Author

**Jefperry Achu Chi**  
CST8002 - Data-Driven Programming  
Algonquin College
