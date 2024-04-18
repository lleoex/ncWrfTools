from netCDF4 import Dataset
import numpy as np
import sys



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #data_dir='C:\\Users\\gonchukov-lv\\Documents\\gis4wrf\\projects\\prim5\\run_wps'
    #file_name= data_dir + '\\' + 'met_em.d01.2018-06-30_12_00_00_1.nc'
    file_name = sys.argv[1]
    var_name= sys.argv[2]
    val = float(sys.argv[3])

    ds = Dataset(file_name,'r+')

    field = ds[var_name][:]
    mod_field = np.zeros_like(field)
    mod_field.fill(val)
    ds[var_name][:] = mod_field
    ds.close()

    #print(ds)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
