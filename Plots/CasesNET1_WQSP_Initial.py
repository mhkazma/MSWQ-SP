#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:36:36 2024

@author: mkazma
"""
import numpy as np               # Array manipulation
import pandas as pd              # Data Manipulation
import matplotlib.pyplot as plt  # Plotting
import seaborn as sns            # Statistical plotting
import scipy.io                  # Load Mat File

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams.update({'font.size': 14})
plt.rcParams['text.usetex'] = True

# Simulating data
# Assuming there are 30 combinations of 'Fault and open lines' and 5 time differences
num_combinations = 24
num_time_diffs = 11
data = np.random.rand(num_time_diffs, num_combinations)
# Setting up the labels for the x-axis
fault_lines = [f"{i+1}-{(i+1)%10+1}" for i in range(num_combinations)]

# Setting up the labels for the y-axis
time_diffs = [f"{0.2 + 0.05 * i:.2f}" for i in range(num_time_diffs)]
##############################################################################

##############################################################################
# Load the .mat file
Case_3 = scipy.io.loadmat('OSP_water4.mat')

# Assuming the variable in the .mat file is named 'Copt_M' (replace 'Copt_M' with the actual variable name)
cell_array_3 = Case_3['Copt_M']

# Initialize an empty array to hold the extracted data
extracted_data_3 = np.zeros((11, 24))

# Iterate through each cell and extract the elements
for i in range(24):
    # Access the ndarray inside the i-th cell
    ndarray_in_cell_3 = cell_array_3[0, i]
    
    # Ensure it's a 2D array with shape (11, 1)
    if ndarray_in_cell_3.shape == (11, 1):
        extracted_data_3[:, i] = ndarray_in_cell_3.flatten()
    else:
        print(f"Unexpected shape {ndarray_in_cell_3.shape} in cell {i}")
############################################################################## 

##############################################################################
# Load the .mat file
Case_6 = scipy.io.loadmat('OSP_water6.mat')

# Assuming the variable in the .mat file is named 'Copt_M' (replace 'Copt_M' with the actual variable name)
cell_array = Case_6['Copt_M']

# Initialize an empty array to hold the extracted data
extracted_data = np.zeros((11, 24))

# Iterate through each cell and extract the elements
for i in range(24):
    # Access the ndarray inside the i-th cell
    ndarray_in_cell = cell_array[0, i]
    
    # Ensure it's a 2D array with shape (11, 1)
    if ndarray_in_cell.shape == (11, 1):
        extracted_data[:, i] = ndarray_in_cell.flatten()
    else:
        print(f"Unexpected shape {ndarray_in_cell.shape} in cell {i}")
##############################################################################        

# Create a 1x24 array with elements from 1 to 24
array_24 = np.arange(1, 25)

#Sensor Locations
sensor_LOC= ['J1','J2','J3','J4','J5','J6','J7','J8','J9','R1','T1']

# The original figure seems to have a 'coolwarm' color scheme, let's try that
#palette = sns.color_palette("blend:#7AB,#EDA", as_cmap=True)
#palette = sns.color_palette("Spectral", as_cmap=True)
#palette = sns.color_palette('Pastel2', as_cmap=True)
#palette = sns.color_palette('vlag', as_cmap=True)cividis
#palette = sns.light_palette("seagreen", as_cmap=True,reverse=True)
palette = sns.color_palette("blend:#EDA,#7AB", as_cmap=True)

#palette = sns.color_palette("light:b", as_cmap=True)

sns.set_theme(style="white")
    
# Creating the heatmaps with square cells, without annotations, grey borders, and a wider colorbar with less spacing between subplots
# Also, centering the figure on the canvas for better printing
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10), gridspec_kw={'hspace': 0.2})

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 7), gridspec_kw={'hspace': 0.2})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5.5), gridspec_kw={'hspace': 0.3})

# Heatmap for the first data with square cells, no annotations and grey borders
#heatmap1 = sns.heatmap(data, annot=False, ax=ax1, cmap=palette, linewidths=3, linecolor='grey', square=True,
#            cbar_kws={'label': 'Time (sec)','pad': 0.01, 'shrink': 0.1})

# #No Legend
# heatmap1 = sns.heatmap(extracted_data_3, annot=False, ax=ax1, cmap=palette, linewidths=1.5, linecolor='grey', square=True,
#             cbar=False)

# Heatmap for the first data with square cells, no annotations and grey borders
heatmap1 = sns.heatmap(extracted_data_3, annot=False, ax=ax1, cmap=palette, linewidths=1.5, linecolor='grey', square=True,
            cbar=False)

# ax1.set_xticklabels(array_24, rotation=0, ha="center")
# ax1.set_yticklabels(sensor_LOC, rotation=0)
# ax1.set_ylabel(r"Sensor Node")
# ax2.set_xlabel(r"Time")
# ax1.set_title(r"(a) Log-det with 4 Sensors")
# ax1.title.set_position((0.1, 1.0))

# # Set the y-tick positions to match sensor_LOC labels
# ax1.set_yticks(np.arange(len(sensor_LOC)) + 0.5)  # Offset to center the labels
# ax1.set_yticklabels(sensor_LOC, rotation=0)
# ax1.set_xticklabels(array_24, rotation=0, ha="center")
# ax1.set_ylabel(r"Sensor Node")
# ax1.set_title(r"(a) Log-det with 4 Sensors")
# ax1.title.set_position((0.1, 1.0))

# Set the y-tick positions to match sensor_LOC labels
ax1.set_yticks(np.arange(len(sensor_LOC)) + 0.5)  # Offset to center the labels
ax1.set_yticklabels(sensor_LOC, rotation=0)

# Set x-tick positions and labels for every two hours
ax1.set_xticks(np.arange(0, len(array_24), 2) + 0.5)  # Offset to center the labels
ax1.set_xticklabels(array_24[::2], rotation=0, ha="center")

ax1.set_ylabel(r"Sensor Node")
ax1.set_title(r"(a) Log-det with 4 Sensors")
ax1.title.set_position((0.1, 1.0))

# Move ticks inside the colorbar
#cbar = heatmap1.collections[0].colorbar
#cbar.ax.tick_params(size=8)  # Hide the default ticks

# Heatmap for the second data with square cells, no annotations and grey borders
#heatmap2 = sns.heatmap(data, annot=False, ax=ax2, cmap=palette, linewidths=3, linecolor='grey', square=True,
#            cbar_kws={'label': 'Time (sec)','pad': 0.01, 'shrink': 0.1})

# #No Legend
# heatmap2 = sns.heatmap(extracted_data, annot=False, ax=ax2, cmap=palette, linewidths=1.5, linecolor='grey', square=True,
#             cbar=False)

# ax2.set_xticklabels(array_24, rotation=0, ha="center")
# ax2.set_yticklabels(sensor_LOC, rotation=0)
# ax2.set_ylabel(r"Sensor Node")
# ax2.set_xlabel(r"Time")
# ax2.set_title(r"(b) Log-det with 6 Sensors")
# ax2.title.set_position((0.1, 1.0))

# Heatmap for the second data with square cells, no annotations and grey borders
heatmap2 = sns.heatmap(extracted_data, annot=False, ax=ax2, cmap=palette, linewidths=1.5, linecolor='grey', square=True,
            cbar=False)

# Set the y-tick positions to match sensor_LOC labels
ax2.set_yticks(np.arange(len(sensor_LOC)) + 0.5)  # Offset to center the labels
ax2.set_yticklabels(sensor_LOC, rotation=0)
ax2.set_xticklabels(array_24, rotation=0, ha="center")
ax2.set_ylabel(r"Sensor Node")
ax2.set_xlabel(r"Time (hr)")
ax2.set_title(r"(b) Log-det with 6 Sensors")
ax2.title.set_position((0.1, 1.0))

# Move ticks inside the colorbar
#cbar = heatmap2.collections[0].colorbar
#cbar.ax.tick_params(size=8)  # Hide the default ticks

#Adjust the colorbar to make it wider
#for ax in [ax1, ax2]:
#    cbar = ax.collections[0].colorbar
#    cbar.ax.set_aspect(15)



 #Center the figure on the canvas
 #.tight_layout(pad=2.0)

# Save the figure as a PDF
#plt.savefig('/mnt/data/Time.pdf', dpi=600, format='pdf', bbox_inches='tight')

# Show the plot as well
#plt.show()

# Returning the path to the saved file
#file_path = '/mnt/data/Time.pdf'
#file_path

#plt.tight_layout()
plt.savefig('Test.pdf', dpi=600, format='pdf', bbox_inches='tight')
plt.show()
