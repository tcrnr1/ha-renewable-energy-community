"""Constants for Renewable Energy Community."""

# Base component constants
NAME = "Renewable Energy Community"
DOMAIN = "renewable_energy_community"
VERSION = "0.1.0"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Services
SERVICE_IMPORT_REPORT = "import_report"

# CSV Keys
CSV_DATE_KEY = "Datum"
CSV_TIME_KEY = "Uhrzeit"

CSV_FEEDIN_GRID = "EinspeiseNetz"
CSV_FEEDIN_COMMUNITY = "EinspeiseGemeinschaft"
CSV_CONSUMPTION_GRID = "BezugNetz"
CSV_CONSUMPTION_COMMUNITY = "BezugGemeinschaft"

# Configuration and options
DEFAULT_NAME = "SmartMeter"
CONF_METER_POINT_NUMBER = "meter_point_number"
CONF_NAME = "name"
