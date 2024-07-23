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

# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


data_merged = pd.concat([acc_df.iloc[:,:3],gyr_df],axis=1)
data_merged.columns = [
    "acc_x",
    "acc_y",
    "acc_z",
    "gyr_x",
    "gyr_y",
    "gyr_z",
    "participant",
    "label",
    "category",
    "set"
]
# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz

sampling = {
    "acc_x" : "mean",
    "acc_y" : "mean",
    "acc_z" : "mean",
    "gyr_x" : "mean",
    "gyr_y" : "mean",
    "gyr_z" : "mean",
    "participant" : "last",
    "label" : "last",
    "category" : "last",
    "set" : "last"
}


data_merged[:100].resample(rule="200ms").apply(sampling)

days = [g for n, g in data_merged.groupby(pd.Grouper(freq="D"))]
days[1]

data_resampled = pd.concat([df.resample(rule="200ms").apply(sampling).dropna() for df in days])

data_resampled["set"] = data_resampled["set"].astype("int")

data_resampled.info()
# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------

data_resampled.to_pickle("../../data/interim/01_data_processed.pkl")