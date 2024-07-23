import pandas as pd
from glob import glob
from pathlib import Path
import os
import functions

# --------------------------------------------------------------
# Get the directory where the script is located and changing the working directory
# --------------------------------------------------------------

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------

# List all data in data/raw/MetaMotion
files = glob(
    "../../data/raw/MetaMotion/*.csv")
data_path = "../../data/raw/MetaMotion/"

acc_df, gyr_df = functions.read_data_from_files(files,data_path)
print(acc_df)

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
