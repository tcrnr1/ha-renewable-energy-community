"""Constants for Residual grid Consumption."""
# Base component constants
NAME = "Residual Grid Consumption"
DOMAIN = "residual-grid-consumption"
VERSION = "0.0.1"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Services
SERVICE_IMPORT_REPORT = "import_report"
END_TIME_KEY = "Datum bis"
START_TIME_KEY = "Datum von"

# Configuration and options
DEFAULT_NAME = "SmartMeter"
CONF_METER_POINT_NUMBER = "meter_point_number"
CONF_NAME = "name"
