import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate timestamp in milliseconds (0 to 30000 ms for 30 seconds)
timestamps = np.arange(0, 30001, 100)  # 100ms intervals

# Generate sensor data with noise
# True distance values decreasing from 250mm to 50mm
true_distances = np.linspace(250, 50, len(timestamps))

# Adding random noise (e.g., normal distribution with mean=0 and std=5)
noise1 = np.random.normal(0, 5, len(timestamps))  # Sensor 1 noise
noise2 = np.random.normal(0, 5, len(timestamps))  # Sensor 2 noise
noise3 = np.random.normal(0, 5, len(timestamps))  # Sensor 3 noise

# Create sensor data with noise
sensor1_data = true_distances + noise1
sensor2_data = true_distances + noise2
sensor3_data = true_distances + noise3

# Create a DataFrame
df = pd.DataFrame({
    'Timestamp (ms)': timestamps,
    'Sensor 1 (mm)': sensor1_data,
    'Sensor 2 (mm)': sensor2_data,
    'Sensor 3 (mm)': sensor3_data
})

# Save to a CSV file
csv_file_path = 'sensor_data_new.csv'  # Specify your desired file path
df.to_csv(csv_file_path, index=False)

print(f"CSV file generated: {csv_file_path}")
