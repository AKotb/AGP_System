import rasterio
from rasterio.merge import merge
import glob
import os

# Generate mosaic data

def generate_ndwi_mosaic_batch(input_dir_data, out_dir_mosaic):
    all_dirs = [name for name in os.listdir(input_dir_data) if os.path.isdir(os.path.join(input_dir_data, name))]  # os.listdir(input_dir_data)
    for i in range(0, len(all_dirs)):
        generate_ndwi_mosaic(input_dir_data + '/' + all_dirs[i], out_dir_mosaic + '/' + all_dirs[i] + '.tif')


def generate_ndwi_mosaic(dir_data, out_mosaic):
    search_criteria = "*.tif" # "*ndwi*.tif"
    q = os.path.join(dir_data, search_criteria)
    dem_fps = glob.glob(q)
    src_files_to_mosaic = []
    for fp in dem_fps:
        src = rasterio.open(fp)
        src_files_to_mosaic.append(src)
    mosaic, out_trans = merge(src_files_to_mosaic)
    out_meta = src.meta.copy()
    out_meta.update({"driver": "GTiff",
                         "height": mosaic.shape[1],
                         "width": mosaic.shape[2],
                        "transform": out_trans,
                         "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                         }
                       )
    with rasterio.open(out_mosaic, "w", **out_meta) as dest:
        dest.write(mosaic)
        print("Mosaic created at: ", out_mosaic)

'''
if __name__ == "__main__":

    input_dir_data = r'F:\Modis Data\Test Samples\Generate Mosaic\input_mosaic_tiles_folders'  # directory of data
    out_dir_mosaic = r"F:\Modis Data\Test Samples\Generate Mosaic\output_mosaic_files"
    generate_ndwi_mosaic_batch(input_dir_data, out_dir_mosaic)
'''