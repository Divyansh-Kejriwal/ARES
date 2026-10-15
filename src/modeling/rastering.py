
import rasterio
import matplotlib.pyplot as plt
import numpy as np

with rasterio.open("C:\\Users\\PC_30\\Documents\\GitHub\\OpusRouter\\yosamite_dem.tif") as dem:
    elevation = dem.read(1, masked=True)

    print("CRS:", dem.crs)
    print("Dimensions:", dem.width, "x", dem.height)
    print("Bounds:", dem.bounds)
    print("Valid elevation cells:", elevation.count())

    values = elevation.compressed()
    if values.size:
        print("Minimum elevation:", round(float(values.min()), 1), "m")
        print("Maximum elevation:", round(float(values.max()), 1), "m")

    plt.imshow(elevation, cmap="terrain")
    plt.colorbar(label="Elevation (m)")
    plt.title("Yosemite elevation raster")
    plt.show()
