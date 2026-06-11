# Renewable Energy Community - Importer for Home-Assistant

Extension of the LINZ NETZ Importer for Home Assistant integration by DarkC35 for displaying the delivered energy amount of a renewable energy community, e.g. Energy Community 4E – Schwertberg, and the grid share of your electricity supplier.
To use this integration, you need a free account at https://www.linznetz.at/ or https://linzag.at and access to the quarter-hour(QH) analysis ("Viertelstundenauswertung"). On both websites, quarter-hour(QH) analysis can be downloaded as a CSV file. 

However, the two websites present the data differently:

LinzNetz provides the total consumption and the residual grid import. The share from the energy community must be calculated from these two values in the CSV file.

LinzAG provides the respective values for the energy community and grid import. Feed-in data for the energy community and the grid would also be available, but these are not yet taken into account in this integration.


**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Placeholder to import statistics by the service.

## Installation

### HACS (Custom Repository)

1. Navigate to `HACS` on your Home-Assistant dashboard.
2. Select `Integrations`.
3. Click on the menu in the top right corner and choose `Custom Repositories`.
4. Insert `https://github.com/tcrnr1/renewable-energy-community` for repository and select category `integration`.
5. Search for `Renewable Energy Community` in the integration tab.
6. Click on the integration and install it with the button on the bottom right corner.
7. Restart Home-Assistant as prompted.
8. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Renewable Energy Community".

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `renewable-energy-community`.
4. Download _all_ the files from the `custom_components/linznetz/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant.
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Renewable Energy Community".

Using your HA configuration directory (folder) as a starting point you should now also have this:


## Import Data:

To import the data, the CSV file must be prepared accordingly. The CSV file may only contain the following columns: date, time, and the respective column you want to import, either energy community or residual grid import. Delete all unnecessary columns from the CSV file.

Note: For CSV files from LinzNetz.at, you first have to calculate the value of the energy community in the CSV file!

Upload your CSV file to a directory in your config folder, (for example: MyDirectory), using the File Editor.

To import the data, go to Settings → Developer Tools → Actions and search for Import Report. Select the corresponding report.

Under entity_id, select the suggested sensor, and under path, enter the corresponding path to your CSV file, for example: /config/MyDirectory/your_csv_file.csv

## Visualization of the data
To display the data, you need the Energy Custom Graph Card by Thyraz: (https://github.com/Thyraz/energy-custom-graph)
Displaying the data in the standard Home Assistant Energy Dashboard is not possible!
Another visualization option is the Energy Flow Card Plus by flixlix: (https://github.com/flixlix/energy-flow-card-plus)
Please refer to the respective repository for the card configuration.
