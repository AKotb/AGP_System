from osgeo import gdal
import numpy as np
import glob

# Compute NDWI using MODIS bands 1&7

def compute_ndwi(data_source, data_output, band1, band7, threshold):

    band1_str = '*_b0' + str(band1)
    band7_str = '*_b0' + str(band7)
    band1_list = glob.glob(data_source + '/' + band1_str + '.tif')
    band7_list = glob.glob(data_source + '/' + band7_str + '.tif')
    print band1_list

    for i in range(len(band1_list)):
        print '+++++', band1_list[i], band7_list[i]
        ds = gdal.Open(band1_list[i])
        band1_data = ds.GetRasterBand(1).ReadAsArray()
        rows1, cols1 = band1_data.shape
        print (i+1), 'Data Dimensions band1 (Rows, Cols):', rows1, cols1
        band1_data.astype(np.float32)

        geoT = ds.GetGeoTransform()
        proj = ds.GetProjection()

        ds = gdal.Open(band7_list[i])
        band2_data = ds.GetRasterBand(1).ReadAsArray()
        rows2, cols2 = band2_data.shape
        print (i+1), 'Data Dimensions band7 (Rows, Cols):', rows2, cols2
        band2_data.astype(np.float32)

        ndwi_tiff_path = data_output + '/' + band1_list[i][1+len(data_source):24+len(data_source)] + '_ndwi_float.tiff'
        print '****', ndwi_tiff_path

        #ndwi_tiff = gdal.GetDriverByName('GTiff').Create(ndwi_tiff_path, cols1, rows1, 1, gdal.GDT_Float32)
        #ndwi_tiff.SetGeoTransform(geoT)
        #ndwi_tiff.SetProjection(proj)

        ndwi_tiff_thr_path = data_output + '/' + band1_list[i][1+len(data_source):24+len(data_source)] + '_ndwi.tiff'
        ndwi_tiff_thr = gdal.GetDriverByName('GTiff').Create(ndwi_tiff_thr_path, cols1, rows1, 1, gdal.GDT_UInt16)
        ndwi_tiff_thr.SetGeoTransform(geoT)
        ndwi_tiff_thr.SetProjection(proj)

        ndwi_thr = np.empty([rows1, cols1], dtype=np.uint8)
        print 'Calc ndwi ...'
        ndwi_arr = ((1.0 * band1_data) - (1.0 * band2_data)) / ((1.0 * band2_data) + (1.0 * band2_data))
        ndwi_thr = 1 * np.ma.getmaskarray(np.ma.masked_inside(ndwi_arr, threshold, 1000))#.filled()
        #ndwi_tiff.GetRasterBand(1).WriteArray(ndwi_arr)
        ndwi_tiff_thr.GetRasterBand(1).WriteArray(ndwi_thr)
        print np.sum(ndwi_thr)
        print 'ndwi process Finished'

'''
if __name__ == "__main__":

    data_source = r'F:\Modis Data\Test Samples\Compute NDWI\input_data_dir'  # directory of data
    data_output = r'F:\Modis Data\Test Samples\Compute NDWI\output_ndwi_dir'

    compute_ndwi(data_source, data_output, 1, 7, 0.5)
'''