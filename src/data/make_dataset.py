import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------

single_file_acc = pd.read_csv(
    "/Users/jasonjoelpinto/Documents/GitHub/ml-barbel-workout-tracking/data/raw/MetaMotion/E-row-medium_MetaWear_2019-01-18T18.30.48.777_C42732BE255C_Gyroscope_25.000Hz_1.4.41.csv")

single_file_gyr = pd.read_csv(
    "/Users/jasonjoelpinto/Documents/GitHub/ml-barbel-workout-tracking/data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv")

# --------------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------

files = glob(
    "/Users/jasonjoelpinto/Documents/GitHub/ml-barbel-workout-tracking/data/raw/MetaMotion/*.csv")
len(files)
# --------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------

data_path = ""/Users/jasonjoelpinto/Documents/GitHub/ml-barbel-workout-tracking/data/raw/MetaMotion/*.csv""

# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------


# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------


# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------


# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------
