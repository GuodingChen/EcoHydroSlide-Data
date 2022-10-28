# EcoHydroSlide-Data
####  All the data are arranged by folders and with detailed description as follows:



#### Future_Hydro

There are three files recording the hydrological results in the complete simulation over a 100-yr period (2023~2122). The timestep is 1 day. The results include all computational scenarios of Bare, S-Veg, and D-Veg.

* ##### Results100yr_Bare.csv

* ##### Results100yr_DVeg.csv

* ##### Results100yr_SVeg.csv

#### Future_Hydro

This fold contains the monthly landslide modeling results with regard to Factor of Safety (FS) and Probability of Failure (PF). The results include all computational scenarios of Bare, S-Veg, and D-Veg. The landslide depth (ce) is set as fixed values (1,5 m and 5 m) or random values ranging from 1.5 m and 5 m. All the data in this folder are saved as HDF5 data format.

* ##### FS&PF_percentage_Bare_ce=1.5.h5

* ##### FS&PF_percentage_Bare_ce=5.h5

* ##### FS&PF_percentage_BareRandomCe-5yr.h5

* ##### FS&PF_percentage_Dveg_ce=1.5.h5

* ##### FS&PF_percentage_Dveg_ce=5.h5

* ##### FS&PF_percentage_DvegRandomCe-5yr.h5

* ##### FS&PF_percentage_SVeg_ce=1.5.h5

* ##### FS&PF_percentage_SVeg_ce=5.h5

* ##### FS&PF_percentage_SVegRandomCe-5yr.h5

#### Future_weather

This fold contains one HDF5 file that packs all the climate data in future (2023~2122). The data are presented as the daily value, monthly value, and annual value. 

* ##### daily&monthly&annual_data.h5

#### History_Hydro

This fold contains two files that records hydrological results that simulated during 2009~2012. These data are used to model the hydrographs against the observed streamflow from 2010 to 2012, for both vegetated and bare configurations (Bare and D-veg).

* ##### Results_Bare_09_12.xlsx

* ##### Results_Dveg_09_12.xlsx

#### HydroSpatial_Bare

This fold contains the 

* ##### OutDT_R_20230807.asc

* ##### OutDT_R_20230808.asc

* ##### ...

* ##### OutDT_SM_20230807.asc

* ##### OutDT_SM_20230808.asc

* ##### ...
