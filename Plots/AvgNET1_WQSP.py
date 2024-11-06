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


def load_first_timestep_data(filename, row_index):
    mat_data = scipy.io.loadmat(filename)
    # Access the last entry in the dict
    cell_array = mat_data[list(mat_data.keys())[-1]]

    # Extract the sensor data for the first time step
    # Access the first time step for the given row (sensor count)
    first_timestep_data = cell_array[row_index, 0]
    return first_timestep_data.flatten()


# Load data for the first time step with 4 and 6 sensors
logdet_4_first_timestep = load_first_timestep_data(
    'Copt_avg_detM.mat', 0)  # Row 0 for 4 sensors
logdet_6_first_timestep = load_first_timestep_data(
    'Copt_avg_detM.mat', 1)  # Row 1 for 6 sensors
trace_4_first_timestep = load_first_timestep_data(
    'Copt_avg_traceM.mat', 0)  # Row 0 for 4 sensors
trace_6_first_timestep = load_first_timestep_data(
    'Copt_avg_traceM.mat', 1)  # Row 1 for 6 sensors

# Define parameters for the plot
sensor_LOC = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'R1', 'T1']
num_sensors = ["4 Sensors", "6 Sensors"]

# Create a figure with 1 row and 2 columns for LogDet and Trace
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(8, 4.5), gridspec_kw={'wspace': 0.3})
palette = sns.color_palette("blend:#EDA,#7AB", as_cmap=True)

# Prepare LogDet data by stacking for the two sensor configurations
# Each sensor configuration in separate column
logdet_data = np.column_stack(
    [logdet_4_first_timestep, logdet_6_first_timestep])

# Plot LogDet heatmap
sns.heatmap(logdet_data, annot=False, ax=ax1, cmap=palette, linewidths=1.5, linecolor='grey', cbar=False,
            xticklabels=num_sensors, yticklabels=sensor_LOC, square=False)
ax1.set_xticks([0.5, 1.5])
ax1.set_xticklabels(num_sensors, rotation=0, ha="center")
ax1.set_yticks(np.arange(len(sensor_LOC)) + 0.5)
ax1.set_yticklabels(sensor_LOC, rotation=0)
ax1.set_title(r"(a) Logdet")
ax1.set_ylabel(r"Sensor Node")
ax1.set_xlabel(r"Number of Sensors")
ax1.title.set_position((0.1, 1.0))


# Prepare Trace data by stacking for the two sensor configurations
trace_data = np.column_stack([trace_4_first_timestep, trace_6_first_timestep])

# Plot Trace heatmap
sns.heatmap(trace_data, annot=False, ax=ax2, cmap=palette, linewidths=1.5, linecolor='grey', cbar=False,
            xticklabels=num_sensors, yticklabels=sensor_LOC, square=False)
ax2.set_xticks([0.5, 1.5])
ax2.set_xticklabels(num_sensors, rotation=0, ha="center")
ax2.set_yticks(np.arange(len(sensor_LOC)) + 0.5)
ax2.set_yticklabels(sensor_LOC, rotation=0)
ax2.set_title(r"(b) Trace")
ax2.set_ylabel(r"Sensor Node")
ax2.set_xlabel(r"Number of Sensors")
ax2.title.set_position((0.1, 1.0))


# Save and display
plt.savefig('logdet_net1-1.pdf', dpi=600, format='pdf', bbox_inches='tight')
plt.show()
