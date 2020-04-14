try:
    import sys, getopt
    import arcpy
except ImportError:
    print 'error'

if __name__ == "__main__":
    input_raster_data = r'#'
    output_table = r'#'
    feature_zone = r'#'

    try:
        myopts, args = getopt.getopt(sys.argv[1:], "i:o:f:")
    except getopt.GetoptError:
        print 'Zonal_Statistics_Script.py -i <input_raster_data> -o <output_table> -f <feature_zone>'
        sys.exit(0)

    for o, a in myopts:
        if o == '-i':
            input_raster_data = a
        elif o == '-o':
            output_table = a
        elif o == '-f':
            feature_zone = a
        else:
            print("Usage: %s -i input_raster_data_directory -o output_table_directory -f feature_zone" %sys.argv[0])

    print("=========Passed Input Raster: "+input_raster_data)
    print("=========Passed Output Raster: " + output_table)
    print("=========Passed Input Feature Zone: " + feature_zone)

    #arcpy.ImportToolbox("Model Functions")
    arcpy.ImportToolbox("C:\Program Files (x86)\ArcGIS\Desktop10.4\ArcToolbox\Toolboxes\Mohamed_Ahmed_WMU.tbx")

    Input_Raster_Data = arcpy.GetParameterAsText(0)
    if Input_Raster_Data == '#' or not Input_Raster_Data:
        Input_Raster_Data = input_raster_data

    Output_Table = arcpy.GetParameterAsText(1)
    if Output_Table == '#' or not Output_Table:
        Output_Table = output_table+"\\%Value%.dbf"

    Feature_Zone = arcpy.GetParameterAsText(2)
    if Feature_Zone == '#' or not Feature_Zone:
        Feature_Zone = feature_zone

    print "Input_Raster_Data: "+Input_Raster_Data
    print "Output_Table: "+Output_Table
    print "Feature_Zone: "+Feature_Zone

    # Local variables:
    Zone_field = "Id"
    Raster_Format = "TIF"
    Name = Raster_Format
    month001_tif = "#"
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

