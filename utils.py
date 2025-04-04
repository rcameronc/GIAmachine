import xarray as xr
import numpy as np

def load_austermann2022(f, save_path):
    
    """Function to load .mat files from Austermann et al. (2022)."""
    
    ESL = np.array(f['ESL']).squeeze()
    RSL = np.array(f['RSL'])
    age = np.array(f['ice_time_new']).squeeze()
    lat = np.array(f['lat_out'][0,:])
    lon = np.array(f['lon_out'][:,0])
    TOPO = np.array(f['topo'])
    ICE = np.array(f['ice_corrected'])
    
    ds = xr.Dataset(
        data_vars=dict(
            rsl=(["age", "lon", "lat", ], RSL),
            esl=(["age"], ESL),
            topo=(["age", "lon", "lat", ], TOPO),
            ice=(["age", "lon", "lat", ], ICE)
        ),
        coords=dict(
            lon=(lon),
            lat=(lat),
            age=age,
        ),
        attrs=dict(
            description="TKTKTK",
        ),
    )
    ds.to_netcdf(save_dir + save_name)

def load_austermann2021(f, save_path):

    """Function to load netcdf files from Austermann et al. (2021)"""

    try:
        RSL_1D = f['RSL_VM5_1D'].data
        RSL_3D = f['RSL_VM5_3D'].data
    except:
        RSL_1D = f['RSL_p55_1D'].data
        RSL_3D = f['RSL_p55_3D'].data
        
    age = f['time'].values
    lat = f['latitude'].values
    lon = f['longitude'].values
    
    ds = xr.Dataset(
        data_vars=dict(
            RSL_VM5_1D=(["age","lon", "lat",  ], RSL_1D),
            RSL_VM5_3D=(["age", "lon", "lat", ], RSL_3D),
        ),
        coords=dict(
            lon=lon,
            lat=lat,
            age=age,
        ),
        attrs=dict(
            description="TKTKTK",
        ),
    )
    ds.to_netcdf(save_path)


def load_dyer2021(f, save_path):

    """Function to load .mat files from Dyer et al. (2021)"""

    lon = f['lon_out']
    lat = f['lat_out']
    age = f['ice_time_new']
    RSL = f['RSL']
    
    ds = xr.Dataset(
        data_vars=dict(
            rsl=(["lon", "lat", "age"], RSL),
        ),
        coords=dict(
            lon=lon,
            lat=lat,
            age=age,
        ),
        attrs=dict(
            description="TKTKTK",
        ),
    )
    ds.to_netcdf(save_path)