# -*- coding: utf-8 -*-
import arcpy
from datetime import datetime

time_start = datetime.now() # time object
print("Starting Rasters Clipping Process: " + str(time_start)[:-7])

ws = r"D:\research_project_data_samples\clip_mosaic\input"
Features_polygon_shp = r"D:\research_project_data_samples\clip_mosaic\shp\Features-polygon.shp"
v_name = "clipped_{0}"

geometries = arcpy.CopyFeatures_management(Features_polygon_shp, arcpy.Geometry())
extent_str = ""
extent_str += str(geometries[0].extent.XMin) + " "
extent_str += str(geometries[0].extent.YMin) + " "
extent_str += str(geometries[0].extent.XMax) + " "
extent_str += str(geometries[0].extent.YMax)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = ws
ras_names = arcpy.ListRasters()
i = 1
for inRas in ras_names:
    print("\n{0}] Clipping {1} @ {2}".format(i, inRas, str(datetime.now())[1:19]))
    arcpy.Clip_management(inRas, extent_str, v_name.format(inRas), Features_polygon_shp, "-3.402823e+038", "ClippingGeometry", "NO_MAINTAIN_EXTENT")
    print("\t" + v_name.format(inRas))
    i += 1
else:
    print("\n\n\tFinishing Rasters Clipping Process ...")

time_end = datetime.now() # time object
print("\nEnding Rasters Clipping Process @ " + str(time_end)[1:19])
elapsed_time = time_end - time_start
print("Elapsed time(hh:mm:ss): " + str(elapsed_time)[:-7])
