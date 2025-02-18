import pandas as pd

def read_data_from_files(files,data_path):

    acc_df = pd.DataFrame()
    gyr_df = pd.DataFrame()

    acc_set = 1
    gyr_set = 1

    for f in files:
        
        # Extract features from filename
        participants = f.split("-")[0].replace(data_path, "")
        label = f.split("-")[1]
        category = f.split("-")[2].rstrip("123").rstrip("_MetaWear_2019")

        df = pd.read_csv(f)

        df['participants'] = participants
        df['label'] = label
        df['category'] = category

        # Concat all the accelerometer dataset into one acc_df dataframe
        if "Accelerometer" in f:
            df["set"] = acc_set
            acc_set += 1
            acc_df = pd.concat([acc_df, df])

        # Concat all the gyroscrope dataset into one acc_df dataframe
        if "Gyroscope" in f:
            df["set"] = gyr_set
            gyr_set += 1
            gyr_df = pd.concat([gyr_df, df])
    
    # Working with datetimes & setting the index as epoch (ms)       
    acc_df.index = pd.to_datetime(acc_df['epoch (ms)'], unit="ms")
    gyr_df.index = pd.to_datetime(gyr_df['epoch (ms)'], unit="ms")

    del acc_df["epoch (ms)"]
    del acc_df["time (01:00)"]
    del acc_df["elapsed (s)"]

    del gyr_df["epoch (ms)"]
    del gyr_df["time (01:00)"]
    del gyr_df["elapsed (s)"]

    return acc_df, gyr_df