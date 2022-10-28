# EcoHydroSlide-Data
####  All the data are arranged by folders and with detailed descriptions as follows:



#### 1. Future_Hydro

There are three files recording the hydrological results in the complete simulation over a 100-year period (2023~2122). The timestep is 1 day. The results include all computational scenarios of Bare, S-Veg, and D-Veg.

* ##### Results100yr_Bare.csv

* ##### Results100yr_DVeg.csv

* ##### Results100yr_SVeg.csv

#### 2. Future_Hydro

This folder contains the monthly landslide modeling results with regard to Factor of Safety (FS) and Probability of Failure (PF). The results include all computational scenarios of Bare, S-Veg, and D-Veg. The landslide depth (ce) is set as fixed values (1,5 m and 5 m) or random values ranging from 1.5 m to 5 m. All the data in this folder are saved in HDF5 data format.

* ##### FS&PF_percentage_Bare_ce=1.5.h5

* ##### FS&PF_percentage_Bare_ce=5.h5

* ##### FS&PF_percentage_BareRandomCe-5yr.h5

* ##### FS&PF_percentage_Dveg_ce=1.5.h5

* ##### FS&PF_percentage_Dveg_ce=5.h5

* ##### FS&PF_percentage_DvegRandomCe-5yr.h5

* ##### FS&PF_percentage_SVeg_ce=1.5.h5

* ##### FS&PF_percentage_SVeg_ce=5.h5

* ##### FS&PF_percentage_SVegRandomCe-5yr.h5

#### 3. Future_weather

This folder contains one HDF5 file that packs all the climate data in the future (2023~2122). The data are presented as the daily value, monthly value, and annual value. 

* ##### daily&monthly&annual_data.h5

#### 4. History_Hydro

This folder contains two files that record hydrological results that are simulated for the duration of  2009~2012. These data are used to model the hydrographs against the observed streamflow from 2010 to 2012, for both vegetated and bare configurations (Bare and D-veg).

* ##### Results_Bare_09_12.xlsx

* ##### Results_Dveg_09_12.xlsx

#### 5. HydroSpatial_Bare

This folder contains the spatial patterns of the hydrological runoff and soil moisture at the specific simulation moments for the scenario of Bare. "R" and "SM" refer to runoff and soil moisture, respectively.

* ##### OutDT_R_20230807.asc

* ##### OutDT_R_20230808.asc

* ##### ...

* ##### OutDT_SM_20230807.asc

* ##### OutDT_SM_20230808.asc

* ##### ...

#### 6. HydroSpatial_Dveg and HydroSpatial_Sveg

This folder contains all the files similar to "HydroSpatial_Bare" but for the scenarios of D-Veg and S-Veg.

#### 7. LAI_data

This folder contains a file recording the modeled time-series LAI is compared to the MODIS data from 2011 to 2021.

* ##### LAI_validation

#### 8. LandSpatial_Bare

This folder contains the spatial patterns of the Factor of Safety modeled by the 3D slope stability model at the specific moments. 

* ##### FS_3D_20230808.tif

* ##### FS_3D_20240713.tif

#### 9. LandSpatial_Dveg and LandSpatial_Sveg

This folder contains all the files similar to "LandSpatial_Bare" but for the scenarios of D-Veg and S-Veg.

#### 10. LongTerm_hazard

This folder contains two files that pack all the long-lasting modeling results, including annual peak flow ($Q_{max}$) and annual landslide hazard ($R_{L}$), for three scenarios in a 100-year future time period. The $\Delta Q_{max}$ and $\Delta R_{L}$ are also calculated to quantify the contributions of vegetation and its dynamics. The only difference between these two files is that, for the file with a suffix of "NoRoot", the root cohesion was set to zero to distinguish the components (water uptake and root reinforcement) in the compound effect of vegetation on landslide hazard moderation.

* ##### 100Yr_assess_NoRoot.h5

* ##### 100Yr_assess.h5

#### 11. Representive_year

This folder contains four files that record the exceedance probabilities for runoff and percentages of unstable area during three defined representative years for D-Veg series: average year, growth year, and decay year.

* ##### P_Landslide.xlsx

* ##### P_Q_average.xlsx

* ##### P_Q_decay.xlsx

* ##### P_Q_growth.xlsx

#### 12. Root_data

This folder contains the files that record the modeled and literature values, including the root area, root number, root force, and root cohesion. The Factor of safety (FS) for the ideal slope with various failure depths is estimated by 1D and 3D slope stability models using specific parameters.

* ##### FS_tree.xlsx

* ##### RootArea.xlsx

* ##### RootCohesion.xlsx

* ##### RootForce.xlsx

* ##### RootNumber.xlsx

#### 13. Validation_ROC

This folder has the file to store the receiver operating characteristic (ROC) plot comparing slope-stability results from two configurations (Bare and D-Veg). The areas under the ROC curve (AUC) are also calculated. 

* ##### ROC_AUC.xlsx
