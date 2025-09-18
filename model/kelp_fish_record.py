"""
CST8002 - Data-Driven Programming - Practical Project 2
Professor: Stanley Pieda
Due Date: October 12, 2025
Author: Jefperry Achu Chi

kelp_fish_record.py - Model layer: Record object class for Pacific Rim NPR Coastal Marine Kelp Fish Community data
"""


class KelpFishRecord:
    """
    Model/Entity object for storing kelp fish community survey data.
    Uses column names from the pacific_rim_npr_coastalmarine_kelp_fish_community_2008-2016_data.csv dataset.
    This class represents the data model in the layered architecture.
    """

    def __init__(self, site_identification="", year=0, diver_identication=0, transect=0,
                 average_depth_ft="", species_code="", count=0, survey_type=""):
        """
        Initialize a new KelpFishRecord object.

        Args:
            site_identification (str): Site identification code
            year (int): Year of the survey
            diver_identication (int): Diver identification number
            transect (int): Transect number
            average_depth_ft (str): Average depth in feet (can be empty)
            species_code (str): Species code identifier
            count (int): Count of species observed
            survey_type (str): Type of survey conducted
        """
        self.site_identification = site_identification
        self.year = year
        self.diver_identication = diver_identication
        self.transect = transect
        self.average_depth_ft = average_depth_ft
        self.species_code = species_code
        self.count = count
        self.survey_type = survey_type

    def get_site_identification(self):
        """
        Get the site identification.

        Returns:
            str: Site identification code
        """
        return self.site_identification

    def set_site_identification(self, site_identification):
        """
        Set the site identification.

        Args:
            site_identification (str): Site identification code
        """
        self.site_identification = site_identification

    def get_year(self):
        """
        Get the survey year.

        Returns:
            int: Year of the survey
        """
        return self.year

    def set_year(self, year):
        """
        Set the survey year.

        Args:
            year (int): Year of the survey
        """
        self.year = year

    def get_diver_identication(self):
        """
        Get the diver identification number.

        Returns:
            int: Diver identification number
        """
        return self.diver_identication

    def set_diver_identication(self, diver_identication):
        """
        Set the diver identification number.

        Args:
            diver_identication (int): Diver identification number
        """
        self.diver_identication = diver_identication

    def get_transect(self):
        """
        Get the transect number.

        Returns:
            int: Transect number
        """
        return self.transect

    def set_transect(self, transect):
        """
        Set the transect number.

        Args:
            transect (int): Transect number
        """
        self.transect = transect

    def get_average_depth_ft(self):
        """
        Get the average depth in feet.

        Returns:
            str: Average depth in feet
        """
        return self.average_depth_ft

    def set_average_depth_ft(self, average_depth_ft):
        """
        Set the average depth in feet.

        Args:
            average_depth_ft (str): Average depth in feet
        """
        self.average_depth_ft = average_depth_ft

    def get_species_code(self):
        """
        Get the species code.

        Returns:
            str: Species code identifier
        """
        return self.species_code

    def set_species_code(self, species_code):
        """
        Set the species code.

        Args:
            species_code (str): Species code identifier
        """
        self.species_code = species_code

    def get_count(self):
        """
        Get the species count.

        Returns:
            int: Count of species observed
        """
        return self.count

    def set_count(self, count):
        """
        Set the species count.

        Args:
            count (int): Count of species observed
        """
        self.count = count

    def get_survey_type(self):
        """
        Get the survey type.

        Returns:
            str: Type of survey conducted
        """
        return self.survey_type

    def set_survey_type(self, survey_type):
        """
        Set the survey type.

        Args:
            survey_type (str): Type of survey conducted
        """
        self.survey_type = survey_type

    def to_dict(self):
        """
        Convert the record to a dictionary for easier data manipulation.

        Returns:
            dict: Dictionary representation of the record
        """
        return {
            'site_identification': self.site_identification,
            'year': self.year,
            'diver_identication': self.diver_identication,
            'transect': self.transect,
            'average_depth_ft': self.average_depth_ft,
            'species_code': self.species_code,
            'count': self.count,
            'survey_type': self.survey_type
        }

    def from_dict(self, data_dict):
        """
        Populate the record from a dictionary.

        Args:
            data_dict (dict): Dictionary containing record data
        """
        self.site_identification = data_dict.get('site_identification', '')
        self.year = data_dict.get('year', 0)
        self.diver_identication = data_dict.get('diver_identication', 0)
        self.transect = data_dict.get('transect', 0)
        self.average_depth_ft = data_dict.get('average_depth_ft', '')
        self.species_code = data_dict.get('species_code', '')
        self.count = data_dict.get('count', 0)
        self.survey_type = data_dict.get('survey_type', '')

    def __str__(self):
        """
        String representation of the KelpFishRecord.

        Returns:
            str: Formatted string representation of the record
        """
        return (f"Site: {self.site_identification}, Year: {self.year}, "
                f"Diver: {self.diver_identication}, Transect: {self.transect}, "
                f"Depth: {self.average_depth_ft if self.average_depth_ft else 'N/A'}, "
                f"Species: {self.species_code}, Count: {self.count}, Survey: {self.survey_type}")

    def __eq__(self, other):
        """
        Check equality between two KelpFishRecord objects.

        Args:
            other (KelpFishRecord): Another KelpFishRecord to compare with

        Returns:
            bool: True if records are equal, False otherwise
        """
        if not isinstance(other, KelpFishRecord):
            return False
        return (self.site_identification == other.site_identification and
                self.year == other.year and
                self.diver_identication == other.diver_identication and
                self.transect == other.transect and
                self.average_depth_ft == other.average_depth_ft and
                self.species_code == other.species_code and
                self.count == other.count and
                self.survey_type == other.survey_type)
