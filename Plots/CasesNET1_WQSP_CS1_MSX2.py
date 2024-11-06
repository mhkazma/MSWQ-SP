import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import seaborn as sns

# Set up plot parameters
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams.update({'font.size': 14})
plt.rcParams['text.usetex'] = True
sns.set_theme(style="white")

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

# Load data for LogDet with 4 and 6 sensors for CS1
logdet_4_CS1 = load_sensor_data('Copt_M_CS1_MSX2.mat', 0)  # Row 0 for 4 sensors
logdet_6_CS1 = load_sensor_data('Copt_M_CS1_MSX2.mat', 1)  # Row 1 for 6 sensors

# Load data for Trace with 4 and 6 sensors for CS1
trace_4_CS1 = load_sensor_data('Copt_M_trace_CS1_MSX2.mat', 0)  # Row 0 for 4 sensors
trace_6_CS1 = load_sensor_data('Copt_M_trace_CS1_MSX2.mat', 1)  # Row 1 for 6 sensors

# Define parameters for the plot
sensor_LOC = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'R1', 'T1']
time_labels = [f"{i}" for i in range(1, 25)]  # Assuming 24 time steps

# Update: Set x-tick positions and labels for every two hours, starting from hour 2
time_labels_two_hour = time_labels[1::2]  # Starting from hour 2 and showing every two hours

# Plot LogDet heatmaps
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5.5), gridspec_kw={'hspace': 0.3})
palette = sns.color_palette("blend:#EDA,#7AB", as_cmap=True)

# LogDet with 4 Sensors
sns.heatmap(logdet_4_CS1, annot=False, ax=ax1, cmap=palette, linewidths=1.5, linecolor='grey', square=True, cbar=False)
ax1.set_yticks(np.arange(len(sensor_LOC)) + 0.5)
ax1.set_yticklabels(sensor_LOC, rotation=0)
ax1.set_xticks(np.arange(1, len(time_labels), 2) + 0.5)  # Offset to center the labels, starting from hour 2
ax1.set_xticklabels(time_labels_two_hour, rotation=0, ha="center")
ax1.set_ylabel("Sensor Node")
ax1.set_title(r"(e) Logdet with 4 Sensors")
ax1.title.set_position((0.1, 1.0))

# LogDet with 6 Sensors
sns.heatmap(logdet_6_CS1, annot=False, ax=ax2, cmap=palette, linewidths=1.5, linecolor='grey', square=True, cbar=False)
ax2.set_yticks(np.arange(len(sensor_LOC)) + 0.5)
ax2.set_yticklabels(sensor_LOC, rotation=0)
ax2.set_xticks(np.arange(1, len(time_labels), 2) + 0.5)
ax2.set_xticklabels(time_labels_two_hour, rotation=0, ha="center")
ax2.set_ylabel("Sensor Node")
ax2.set_xlabel("Time (hr)")
ax2.set_title(r"(f) Logdet with 6 Sensors")
ax2.title.set_position((0.1, 1.0))

plt.savefig('LogDet_CS1_MSX2.pdf', dpi=600, format='pdf', bbox_inches='tight')
plt.show()

# Plot Trace heatmaps
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5.5), gridspec_kw={'hspace': 0.3})

# Trace with 4 Sensors
sns.heatmap(trace_4_CS1, annot=False, ax=ax1, cmap=palette, linewidths=1.5, linecolor='grey', square=True, cbar=False)
ax1.set_yticks(np.arange(len(sensor_LOC)) + 0.5)
ax1.set_yticklabels(sensor_LOC, rotation=0)
ax1.set_xticks(np.arange(1, len(time_labels), 2) + 0.5)
ax1.set_xticklabels(time_labels_two_hour, rotation=0, ha="center")
ax1.set_ylabel("Sensor Node")
ax1.set_title(r"(c) Trace with 4 Sensors")
ax1.title.set_position((0.1, 1.0))

# Trace with 6 Sensors
sns.heatmap(trace_6_CS1, annot=False, ax=ax2, cmap=palette, linewidths=1.5, linecolor='grey', square=True, cbar=False)
ax2.set_yticks(np.arange(len(sensor_LOC)) + 0.5)
ax2.set_yticklabels(sensor_LOC, rotation=0)
ax2.set_xticks(np.arange(1, len(time_labels), 2) + 0.5)
ax2.set_xticklabels(time_labels_two_hour, rotation=0, ha="center")
ax2.set_ylabel("Sensor Node")
ax2.set_xlabel("Time (hr)")
ax2.set_title(r"(h) Trace with 6 Sensors")
ax2.title.set_position((0.1, 1.0))

plt.savefig('Trace_CS1_MSX2.pdf', dpi=600, format='pdf', bbox_inches='tight')
plt.show()