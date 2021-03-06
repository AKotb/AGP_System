# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# zonalstatisticsscript.py
# Created on: 2020-02-23 09:16:44.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: zonalstatisticsscript <Input_Raster_Data> <Output_Table> <Feature_Zone> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")

# Script arguments
Input_Raster_Data = arcpy.GetParameterAsText(0)
if Input_Raster_Data == '#' or not Input_Raster_Data:
    Input_Raster_Data = "C:\\Test_2\\images" # provide a default value if unspecified

Output_Table = arcpy.GetParameterAsText(1)
if Output_Table == '#' or not Output_Table:
    Output_Table = "C:\\Test_2\\Zonal\\%Value%.dbf" # provide a default value if unspecified

Feature_Zone = arcpy.GetParameterAsText(2)
if Feature_Zone == '#' or not Feature_Zone:
    Feature_Zone = "S:\\Saudi_GRACE\\Recharge\\shapefiles\\arabian_peninsula_anomalies.shp" # provide a default value if unspecified

# Local variables:
Zone_field = "Id"
Raster_Format = "TIF"
Name = Raster_Format
month001_tif = "C:\\Test_2\\images\\TWS_mass_CSR_month_NDS_200km_001.tif"
Statistics_type = "ALL"
Value = Name
AddField = Output_Table
calcOut = Output_Table

# Process: Iterate Rasters
arcpy.IterateRasters_mb(Input_Raster_Data, "", Raster_Format, "RECURSIVE")

# Process: Parse Path
arcpy.ParsePath_mb(Name, "NAME")

# Process: Zonal Statistics as Table
arcpy.gp.ZonalStatisticsAsTable_sa(Feature_Zone, Zone_field, month001_tif, Output_Table, "DATA", Statistics_type)

# Process: Add Field
arcpy.AddField_management(Output_Table, "fileName", "TEXT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Output_Table, "filename", "\"%Value%\"", "PYTHON", "")

