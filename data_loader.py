# Alexandros Metsai
# alexmetsai@gmail.com

import pandas as pd
import numpy as np

def load_data(path = "data.csv"):
    # Load data from csv.
    data = pd.read_csv(path, header=None, names=["t",
    "CPU",
    "RxKBTot",
    "TxKBTot",
    "WriteKBTot",
    "Watts",
    "Amps",
    "RMS",
    "diff_encoder_l",
    "flag"])
    
    # Convert string values to float.
    for col in data.columns:
        data[col] = data[col].astype(float)
    
    
    # Drop the t (time) values, since they won't be of use.
    data = data.drop("t", axis=1)
    
    # Print some info about the dataset.
    proportions = data["flag"].value_counts()
    print("Data loaded sucessfully.")
    print("Anomally Percentage:", proportions[1]/proportions.sum())
    
    # Normalize numeric values, except "flag".
    cols_to_norm = ["CPU",
    "RxKBTot",
    "TxKBTot",
    "WriteKBTot",
    "Watts",
    "Amps",
    "RMS",
    "diff_encoder_l"]
    
    min_cols = data.loc[data["flag"] == 0, cols_to_norm].min()
    max_cols = data.loc[data["flag"] == 0, cols_to_norm].max()
    
    data.loc[:, cols_to_norm] = (data[cols_to_norm] - min_cols) / (max_cols - min_cols)
    
    return data.values
    
if __name__ == "__main__":
    pass
