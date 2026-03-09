# Fire Progression Mapping (FPM) on the base of satellite data

## About
This repository involves three QGIS Model files in combination with two python scripts created for mapping the progress of a wildfire in QGIS on the base of the Active Fire (AF) data that can be downloaded from NASA's Land, Atmosphere Near real-time Capability for Earth observation (LANCE) / Fire Information for Resource Management System (FIRMS).

For this purpose, the first model is created for the delimitation of the boundaries of wildfire zones (Delimitation of Burned Areas.model3) on the base of Sentinel 2 or Landsat 8-9 data. The second model is created for pooling the Active Fire (AF) data from MODIS and VIIRS (Pooling MODIS and VIIRS.model3). The first two models is actually designed to prepare data for the last model (Fire Progression Mapping.model3). The third mode is created for the Fire Progression Mapping on the base of AFs data pooled by using the second model according to the wildfire zones identified by using the first model.

Below there is a sample image from one of the outcomes of third model created for mapping the progression of a wildfire;

![FPM_sample](https://github.com/user-attachments/assets/bc0f6731-eb69-479d-8198-0e6cfce91f9d)

How to cite this material;

Beyhan, B. (2025). Wildfires as incidences of ecological crime: A comprehensive examination of the wildfires in İzmir city-region between 25 June and 5 July 2025. Geoadria, 30 (2). https://doi.org/10.15291/geoadria.4869

Beyhan, B. (2026, March 9). Fire Progression Mapping (FPM) on the base of satellite data: First release (Version 2.0). Zenodo. http://doi.org/10.5281/zenodo.18924076

## Installation and Use
In order to install QGIS Models, file named “*.model3” should be copied to the model folder (“processing/models”) of QGIS installation. In a typical Windows-based operating system, the default address for the respective folder is as following;

C:\Users\Aidata\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\models

Additionally, the main model (Fire Progression Mapping.model3) draws on two additional python scripts (FPM vector legend.py and FPM raster legend.py) that should be copied to the script folder (“processing/scripts”) of QGIS installation. In a typical Windows-based operating system, the default address for the respective folder is as following;

C:\Users\Aidata\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts

Extra information about the use of each model can be obtained by running the models concerned in QGIS.

## Software Requirements
QGIS - https://qgis.org/ 

SAGA tools should be available under processing toolbox in QGIS. If these tools are not listed under processing toolbox, you can install them via the required plugin from "Processing Saga NextGen Provider" directly in QGIS.
