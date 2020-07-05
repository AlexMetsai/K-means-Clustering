# Alexandros Metsai
# alexmetsai@gmail.com

import pandas as pd

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
    
if __name__ == "__main__":
    pass
