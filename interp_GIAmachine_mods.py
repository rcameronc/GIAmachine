# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import xarray as xr
import numpy as np
import glob
from scipy.io import loadmat
import h5py
import os
from matplotlib import pyplot as plt
import pandas as pd

from utils import *


# %%
paths = glob.glob('raw_models/*/*')
for path in paths:

    
    filename = path.split('/')[-1]
    home_dir = '/'.join(path.split('/')[:-1]) + '/'
    save_dir = home_dir.replace('raw', 'processed')
    save_name = '_'.join(path.split('/')[1:]).split('.')[:-1][0]

    save_path = save_dir + save_name

    if not os.path.exists(save_dir):
        print('making', save_dir)
        os.makedirs(save_dir)

    if os.path.isfile(save_path):
        print(filename, "already exists")

    else:
        print("processing", filename)
        
        if '.nc' in filename:
            
            f = xr.open_mfdataset(path)
            if 'austermann2021' in path:
                load_austermann2021(f, save_path)

            if 'han' in path:
                continue
            if 'dyer2021' in path:
                load_dyer2021(f, save_path)
                
    
        if '.mat' in filename:
            try:
                f = loadmat(path)
            except:
                with h5py.File(path, 'r') as f:
    
                    if 'austermann2022' in path:
                        load_austermann2022(f, save_path)
                       


# %%
p = '/Volumes/Seagate Hub/whoi/GIAmachine/raw_models/dyer2021/out.l48C.ump3.lm3_Colleoni_Wael_S.mat'
f = loadmat(p)
lon = f['lon_out']
lat = f['lat_out']
age = f['ice_time_new']
RSL = f['RSL']
RSL.shape
# age[0], age[-1]

# %%

# %%
with h5py.File(path, 'r') as f:
    print(f.keys())

