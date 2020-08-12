import os
import fiona
import rasterio
import rasterio.mask
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt


def calculate_zonal_stats(dir_data, input_file, input_shp, index):
    input_data = dir_data + '\\' + input_file
    with fiona.open(input_shp, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]

    with rasterio.open(input_data) as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
        out_meta = src.meta

    data_all = np.ma.getdata(out_image)
    data_vec = data_all.flatten()
    data_nz = data_vec[data_vec > 0]

    # zonal_count = np.size(data_nz)
    # zonal_sum = np.sum(data_nz)
    zonal_mean = np.average(data_nz)
    # zonal_min = np.min(data_nz)
    # zonal_max = np.max(data_nz)
    # zonal_range = zonal_max - zonal_min
    # return index, zonal_count, zonal_min, zonal_max, zonal_range, zonal_mean, zonal_sum, input_file
    return [index, input_file, zonal_mean]


def single_calculate_zonal_stats(dir_data, dir_out, file, input_shp):
    print("\nStarting Single Zonal Statistics Process ...\n")

    workbook = xlsxwriter.Workbook(os.path.join(dir_out, "out_single.xlsx"))
    ws_zonal = workbook.add_worksheet()

    if (file.endswith('.tif') or file.endswith('.tiff')):
        row = calculate_zonal_stats(dir_data, file, input_shp, 1)
        print row
        ws_zonal.write_row(1, 0, row)

    ws_zonal.write_row(0, 0, ["Index", "Input File", "Mean"])


def batch_calculate_zonal_stats(dir_data, dir_out, input_shp):
    if dir_data.endswith("\n"):
        dir_data = dir_data[:-1]

    if dir_out.endswith("\n"):
        dir_out = dir_out[:-1]

    if input_shp.endswith("\n"):
        input_shp = input_shp[:-1]

    print("1] Starting Batch Zonal Statistics Process ...")

    outfilename = "out_batch"
    print("2] Data dir: " + dir_data)

    all_files = os.listdir(dir_data)  # [f for f in os.listdir(dir_data) if os.path.isfile(f)]
    print(type(all_files))
    print(all_files)

    workbook = xlsxwriter.Workbook(os.path.join(dir_out, outfilename + ".xlsx"))
    ws_zonal = workbook.add_worksheet()

    index_list = []
    filename_list = []
    mean_list = []

    print("4] Start looping over files ...")
    index = 1
    for file in all_files:
        if (file.endswith('.tif') or file.endswith('.tiff')):
            row = calculate_zonal_stats(dir_data, file, input_shp, index)
            print ("Row: ", row)
            index_list.append(str(row[0]).zfill(3))  # replace 2 with 3 if # files >= 100
            filename_list.append(row[1])
            mean_list.append(row[2])
            ws_zonal.write_row(index, 0, row)
            index += 1
        else:
            print(file, "not tif file ...")

    ws_zonal.write_row(0, 0, ["Index", "Input File", "Mean"])
    workbook.close()
    x = index_list
    y = mean_list

    plt.plot(x, y, linewidth=3, color="r")

    # commented block of code plotting trend line

    # x = range(1, len(x)+1)
    # z = np.polyfit(x, y, 1)
    # p = np.poly1d(z)
    # plt.plot(x, p(x), "r--")

    plt.xticks(rotation=-40)

    plt.savefig(os.path.join(dir_out, outfilename + ".png"))  # comment if you show only
    plt.show()  # comment if you save only
    '''
    '''


'''
if __name__ == "__main__":

    dir_data = r'D:\NARSS\Research Project\2018-2019\01-01-2020\Zonal_Statistics\CLM'  # directory of data
    dir_out = r'D:\NARSS\Research Project\2018-2019\01-01-2020\Zonal_Statistics\temp out'
    shp_file = r'D:\NARSS\Research Project\2018-2019\01-01-2020\Zonal_Statistics\shp_nb\Features-polygon.shp'

    batch_calculate_zonal_stats(dir_data, dir_out, shp_file)

    single_filename = 'month_CLM1_06.tif'
    single_calculate_zonal_stats(dir_data, dir_out, single_filename, shp_file)
'''