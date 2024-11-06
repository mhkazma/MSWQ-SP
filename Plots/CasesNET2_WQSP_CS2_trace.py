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
# Adjusted for 36 sensor nodes and 24 combinations for NET2 case
num_combinations = 24
num_time_diffs = 36  # Adjusted to 36 for NET2


# Define function to load and process data for a given sensor configuration
def load_sensor_data(filename, row_index):
    mat_data = scipy.io.loadmat(filename)
    cell_array = mat_data[list(mat_data.keys())[-1]]  # Access the last entry in the dict
    num_time_steps = cell_array.shape[1]              # Number of time steps (e.g., 24)
    num_sensors = cell_array[row_index, 0].shape[0]   # Number of sensors (e.g., 11)
    
    # Initialize an empty array to hold the extracted data
    extracted_data = np.zeros((num_sensors, num_time_steps))

    # Iterate through each cell and extract the elements
    for i in range(num_time_steps):
        ndarray_in_cell = cell_array[row_index, i]
        
        # Ensure it's a 2D array with shape (num_sensors, 1)
        if ndarray_in_cell.shape == (num_sensors, 1):
            extracted_data[:, i] = ndarray_in_cell.flatten()
        else:
            print(f"Unexpected shape {ndarray_in_cell.shape} in cell {i} for row {row_index}")
    
    return extracted_data

# Load data for LogDet with 4 and 6 sensors for CS2
logdet_12_CS1 = load_sensor_data('Copt_M_CS2.mat', 0)  # Row 0 for 4 sensors
logdet_18_CS1 = load_sensor_data('Copt_M_CS2.mat', 1)  # Row 1 for 6 sensors

# Load data for Trace with 4 and 6 sensors for CS2
trace_12_CS1 = load_sensor_data('Copt_M_trace_CS2.mat', 0)  # Row 0 for 4 sensors
trace_18_CS1 = load_sensor_data('Copt_M_trace_CS2.mat', 1)  # Row 1 for 6 sensors


# # Generating random data with the new shape for simulation purposes
# extracted_data_3 = np.random.rand(num_time_diffs, num_combinations)
# extracted_data = np.random.rand(num_time_diffs, num_combinations)

# Setting up the labels for the x-axis
fault_lines = [f"{i+1}-{(i+1)%10+1}" for i in range(num_combinations)]

# Create a 1x24 array with elements from 1 to 24
array_24 = np.arange(1, 25)

# Define parameters for the plot
# Sensor Locations for NET2 with 36 sensors, where the 36th node is 'T1' instead of 'J36'
sensor_LOC = [f"J{i+1}" if i != 35 else "T1" for i in range(36)]  # Generates ['J1', ..., 'J25', 'J27', ..., ''T1']

# Define color palette
palette = sns.color_palette("blend:#EDA,#7AB", as_cmap=True)
sns.set_theme(style="white")
    
# Creating the heatmaps with square cells, without annotations, grey borders, and a wider colorbar with less spacing between subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5), gridspec_kw={'wspace': 0.1})

# Heatmap for the first data with square cells, no annotations and grey borders
heatmap1 = sns.heatmap(trace_12_CS1, annot=False, ax=ax1, cmap=palette, linewidths=1, linecolor='grey', square=True,
                       cbar=False)

# # Set y-tick positions and labels to show every 2nd label, starting from J2
# ax1.set_yticks(np.arange(1, len(sensor_LOC), 2) + 0.5)  # Offset to center the labels
# ax1.set_yticklabels(sensor_LOC[1::2], rotation=0)

# Adjust the slicing to handle odd-length lists correctly
ax1.set_yticks(np.arange(1, len(sensor_LOC), 2) + 0.5)  # Offset to center the labels

# Manually append the last label if it's missing
ytick_labels = sensor_LOC[1::2]
if len(sensor_LOC) % 2 == 1:
    ytick_labels = sensor_LOC[1::2] + [sensor_LOC[-1]]  # Append last item if necessary

ax1.set_yticklabels(ytick_labels, rotation=0)

# Set x-tick positions and labels to start from the second label and display every two hours
ax1.set_xticks(np.arange(3, len(array_24), 4) + 0.5)  # Start from the fourth label
ax1.set_xticklabels(array_24[3::4], rotation=0, ha="center")

ax1.set_ylabel(r"Sensor Node")
ax1.set_xlabel(r"Time (hr)")
ax1.set_title(r"(c) Trace with 12 Sensors")
ax1.title.set_position((0.1, 1.0))

# Heatmap for the second data with square cells, no annotations and grey borders
heatmap2 = sns.heatmap(trace_18_CS1, annot=False, ax=ax2, cmap=palette, linewidths=1, linecolor='grey', square=True,
                       cbar=False)

# # Set y-tick positions and labels to show every 2nd label, starting from J2
# ax2.set_yticks(np.arange(1, len(sensor_LOC), 2) + 0.5)  # Offset to center the labels
# ax2.set_yticklabels(sensor_LOC[1::2], rotation=0)

# Adjust the slicing to handle odd-length lists correctly
ax2.set_yticks(np.arange(1, len(sensor_LOC), 2) + 0.5)  # Offset to center the labels

# Manually append the last label if it's missing
ytick_labels = sensor_LOC[1::2]
if len(sensor_LOC) % 2 == 1:
    ytick_labels = sensor_LOC[1::2] + [sensor_LOC[-1]]  # Append last item if necessary

ax2.set_yticklabels(ytick_labels, rotation=0)

# Set x-tick positions and labels for every two hours, starting from the second label
ax2.set_xticks(np.arange(3, len(array_24), 4) + 0.5)  # Start from the fourth label
ax2.set_xticklabels(array_24[3::4], rotation=0, ha="center")

ax2.set_ylabel(r"Sensor Node")
ax2.set_xlabel(r"Time (hr)")
ax2.set_title(r"(d) Trace with 18 Sensors")
ax2.title.set_position((0.1, 1.0))

# Save the figure as a PDF
plt.savefig('OSP_trace_Net2.pdf', dpi=600, format='pdf', bbox_inches='tight')
plt.show()