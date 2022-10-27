# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:06:24 2022

@author: Guoding Chen
"""

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

import xlrd

# set the family font 
font1={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':40}
font_xylable={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':40}
font_legend={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':15}

date_RootArea = xlrd.open_workbook('./RootArea.xlsx')
table_RootArea=date_RootArea.sheets()[0]

date_RootNumber = xlrd.open_workbook('./RootNumber.xlsx')
table_RootNumber = date_RootNumber.sheets()[0]

date_force = xlrd.open_workbook('./RootForce.xlsx')
table_force=date_force.sheets()[0]

date_FS = xlrd.open_workbook('./FS_tree_2.xlsx')
table_FS=date_FS.sheets()[0]


# read the tree data: root area
Cal_SoilDepth_tree = [i for i in table_RootArea.col_values(4) if isinstance(i, (int, float))]
Cal_RootArea_tree = [i for i in table_RootArea.col_values(5) if isinstance(i, (int, float))]
Exp_SoilDepth_tree = [i for i in table_RootArea.col_values(6) if isinstance(i, (int, float))]
Exp_RootArea_tree = [i for i in table_RootArea.col_values(7) if isinstance(i, (int, float))]

# read the tree data: root number
Cal_SoilDepth_tree_2 = [i for i in table_RootNumber.col_values(4) if isinstance(i, (int, float))]
Cal_RootNumber_tree = [i for i in table_RootNumber.col_values(5) if isinstance(i, (int, float))]
Exp_SoilDepth_tree_2 = [i for i in table_RootNumber.col_values(6) if isinstance(i, (int, float))]
Exp_RootNumber_tree = [i for i in table_RootNumber.col_values(7) if isinstance(i, (int, float))]

# read the tree data: force
Cal_SoilDepth_tree_3 = [i for i in table_force.col_values(6) if isinstance(i, (int, float))]
Cal_RootForce_tree = [i for i in table_force.col_values(7) if isinstance(i, (int, float))]
Exp_SoilDepth_tree_3 = [i for i in table_force.col_values(8) if isinstance(i, (int, float))]
Exp_RootForce_tree = [i for i in table_force.col_values(9) if isinstance(i, (int, float))]

#  read soil depth:FS
SoilDepth = [i for i in table_FS.col_values(0) if isinstance(i, (int, float))]

# read the FS value:FS
FS_inf_NoVeg =  [i for i in table_FS.col_values(1) if isinstance(i, (int, float))]
FS_inf_Veg =  [i for i in table_FS.col_values(2) if isinstance(i, (int, float))]
FS3D_NoVeg = [i for i in table_FS.col_values(3) if isinstance(i, (int, float))]
FS3D_Veg = [i for i in table_FS.col_values(4) if isinstance(i, (int, float))]



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharey=False, figsize=(7, 6))



ax1.plot(Cal_RootArea_tree, Cal_SoilDepth_tree, color="k", linewidth = 4, linestyle='-', label = "Cal. value")
ax1.scatter(Exp_RootArea_tree, Exp_SoilDepth_tree, marker="o", 
            edgecolor="darkgray", s=30, linewidths=4, color="darkgray", label = "Exp. data")

ax1.set_xlim([0, 40])
ax1.set_xticks([0, 10, 20, 30, 40])
ax1.set_xticklabels([0, 10, 20, 30, 40], fontsize=18)
ax1.set_xlabel('Root area ($cm^2$)', fontsize=18)

ax1.set_ylim([-1600, 0])
ax1.set_yticks([-1500, -1000, -500, 0])
ax1.set_yticklabels([-1.5, -1, -0.5, 0], fontsize=18)
ax1.grid(linestyle='--')
ax1.set_ylabel('Soil depth (m)', fontsize=18)
ax1.text(30,-1500,"(a)", fontsize=25)

ax2.scatter(Exp_RootNumber_tree, Exp_SoilDepth_tree_2, marker="o", 
                  edgecolor="darkgray",s=30,linewidths=4, color="darkgray", label = "Tree data")
ax2.plot(Cal_RootNumber_tree, Cal_SoilDepth_tree_2, color="k", 
              linewidth = 4, linestyle='-', label="Modeled tree")

ax2.set_xlim([0, 40])
ax2.set_xticks([0, 10, 20, 30, 40])
ax2.set_xticklabels([0, 10, 20, 30, 40], fontsize=18)
ax2.set_xlabel('Root number (-)', fontsize=18)

ax2.axhline(y=-200, xmin=0, xmax=35, color="k", linewidth = 3, linestyle='--')

ax2.set_ylim([-1600, 0])
ax2.set_yticks([-1500, -1000, -500, -200, 0])
ax2.set_yticklabels([-1.5, -1, -0.5, -0.2, 0], fontsize=18)
ax2.grid(linestyle='--')
ax2.set_ylabel('Soil depth (m)', fontsize=18)
ax2.text(30,-1500,"(b)", fontsize=25)

ax3.scatter(Exp_RootForce_tree, Exp_SoilDepth_tree_3, marker="o", 
                  edgecolor="darkgray",s=30,linewidths=4, color="darkgray", label = "Tree data")
ax3.plot(Cal_RootForce_tree, Cal_SoilDepth_tree_3, color="k", 
              linewidth = 4, linestyle='-', label="Modeled tree")

ax3.set_xlim([0, 10])
ax3.set_xticks([0, 2, 4, 6, 8, 10])
ax3.set_xticklabels([0, 2, 4, 6, 8, 10], fontsize=18)
ax3.set_xlabel('Root force (kN)', fontsize=18)

ax3.set_ylim([-1600, 0])
ax3.set_yticks([-1500, -1000, -500, 0])
ax3.set_yticklabels([-1.5, -1, -0.5, 0], fontsize=18)
ax3.grid(linestyle='--')
ax3.set_ylabel('Soil depth (m)', fontsize=18)
ax3.text(7.5,-1500,"(c)", fontsize=25)



ax4.plot(FS_inf_NoVeg, SoilDepth, color="C0", linewidth = 2, linestyle='--', label="FS_{inf}: NoVeg")
ax4.plot(FS_inf_Veg, SoilDepth, color="C0", linewidth = 2, linestyle='-', label="FSinf-Veg")

ax4.plot(FS3D_NoVeg, SoilDepth, color="C3", linewidth = 2, linestyle='--', label="FS3D-NoVeg")

ax4.plot(FS3D_Veg, SoilDepth, color="C3", linewidth = 2, linestyle='-', label="FS3D-Veg")

# plt.fill_between(np.array(SoilDepth), np.array(FS3D_NoVeg), np.array(FS3D_Veg), 
#                   where = (np.array(SoilDepth) < -1500) & (np.array(SoilDepth) > -3000), color='g')
ax4.fill_betweenx(SoilDepth, FS3D_NoVeg, FS3D_Veg, where = (np.array(SoilDepth) <= -1500) & (np.array(SoilDepth) >= -3000),
                  color='C2', alpha=0.7)

ax4.axvline(x = 1, color="k", linewidth = 3, linestyle='--')
ax4.text(3,-2800,"(d)", fontsize=25)


ax4.set_xlim([0, 4])
ax4.set_xticks([0, 1, 2, 4])
ax4.set_xticklabels([0, 1, 2, 4], fontsize=18)
ax4.set_xlabel('Factor of safety (-)', fontsize=18)

ax4.set_ylim([-3000, 0])
ax4.set_yticks([-3000, -2000, -1500, -1000,0])
ax4.set_yticklabels([-3, -2,-1.5, -1, 0], fontsize=18)
ax4.grid(linestyle='--')
ax4.set_ylabel('Failure depth (m)', fontsize=18)

plt.tight_layout()
plt.show()




