This repository involves three QGIS Model files in combination with two python scripts created for mapping the progress of a wildfire in QGIS on the base of the Active Fire (AF) data that can be downloaded from NASA's Land, Atmosphere Near real-time Capability for Earth observation (LANCE) / Fire Information for Resource Management System (FIRMS).

For this purpose, the first model is created for the delimitation of the boundaries of wildfire zones (Delimitation of Burned Areas.model3) on the base of Sentinel 2 or Landsat 8-9 data. The second model is created for pooling the Active Fire (AF) data from MODIS and VIIRS (Pooling MODIS and VIIRS.model3). The first two models is actually designed to prepare data for the last model (Fire Progression Mapping.model3). The third mode is created for the Fire Progression Mapping on the base of AFs data pooled by using the second model according to the wildfire zones identified by using the first model.

Below there is a sample image from one of the outcomes of third model created for mapping the progression of a wildfire;

![FPM_sample](https://github.com/user-attachments/assets/bc0f6731-eb69-479d-8198-0e6cfce91f9d)
