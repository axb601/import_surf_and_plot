# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:12:56 2020

@author: BIRCHHAWKINS

This is a script for importing a Petrel surface as a Pandas dataframe
The Petrel surface must be converted to a point set within Petrel and exported as Irap classic points (ASCII)
It is useful to convert the Z values to positive integers

The script then takes the X, Y, and Z values and plots them in a standard 3D chart (visualisation for QC purposes only, no CRS used)

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#CHANGE PATH TO POINT TO A PETREL POINTS SET IRAP ASCII FORMAT FILE
with open('C:\\Users\\BIRCHHAWKINS\\Python\\data\\NTO_2', 'r') as f:
    data = pd.read_csv(f, sep=" ", names=["X", "Y", "Z"])       

    ax = plt.axes(projection='3d')
    ax.set_xlabel("X (m)", fontweight='bold') #SET X AXIS LABELS
    ax.set_ylabel("Y (m)", fontweight='bold') #SET Y AXIS LABELS
    ax.set_zlabel("Z (m)", fontweight='bold') #SET Z AXIS LABELS
    ax.ticklabel_format(axis='both', style='plain')
    ax.set_xticks(np.arange(474000,479000,2000)) #SET MIN/MAX/STEP X VALUES FOR CHART AXIS
    ax.set_yticks(np.arange(9868000, 9878000, 4000)) #SET MIN/MAX/STEP Y VALUES FOR CHART AXIS
    ax.set_zticks(np.arange(1250, 2750, 500)) #SET MIN/MAX/STEP Z VALUES FOR CHART AXIS
    ax.plot_trisurf(data.X, data.Y, data.Z, linewidth=0, antialiased=False,
                cmap='gist_rainbow') #SET COLOUR MAP
    ax.invert_zaxis()
    ax.set_title('NTO reservoir surface') #SET CHART TITLE
    ax.view_init(elev=30, azim=260) #SETS CAMERA POSITION FOR CHART VIEW

plt.savefig('chart_output.png') #SAVES CHART AS PNG FILE IN WORKING DIR