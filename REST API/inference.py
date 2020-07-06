# Alexandros Metsai
# alexmetsai@gmail.com

import pickle
import pandas as pd

def inference(body_dict, filename="model.pk"):
    '''
    Convert input data to pandas DataFrame and 
    predict input type (normal/anomalous).
    '''
    
    input_ = {"t": [body_dict["t"]], 
        "CPU": [body_dict["CPU"]],
        "RxKBTot": [body_dict["RxKBTot"]],
        "TxKBTot": [body_dict["TxKBTot"]],
        "WriteKBTot": [body_dict["WriteKBTot"]],
        "Watts": [body_dict["Watts"]],
        "Amps": [body_dict["Amps"]],
        "RMS": [body_dict["RMS"]],
        "diff_encoder_l": [body_dict["diff_encoder_l"]],
        "flag": [-1]}
    
    input_df =  pd.DataFrame(data=input_)
    
    data = input_df
    
    # Convert string values to float.
    for col in data.columns:
        data[col] = data[col].astype(float)
    
    # Drop the t (time) values, since they won't be of use.
    data = data.drop("t", axis=1)
    
    # Normalize numeric values, except "flag".
    cols_to_norm = ["CPU",
    "RxKBTot",
    "TxKBTot",
    "WriteKBTot",
    "Watts",
    "Amps",
    "RMS",
    "diff_encoder_l"]
    
    # Min/max values for normalization.
    # Hard-coded for increased performance.
    min_cols = {"CPU": [0.0],
    "RxKBTot": [0.0],
    "TxKBTot": [0.0],
    "WriteKBTot": [0.0],
    "Watts": [62.7],
    "Amps": [0.401004],
    "RMS": [0.008099],
    "diff_encoder_l": [0.000012]}
    min_cols = pd.DataFrame(data=min_cols)
    
    max_cols = {"CPU": [8801.0],
    "RxKBTot": [506.0],
    "TxKBTot": [10.0],
    "WriteKBTot": [101.199602],
    "Watts": [101.199602],
    "Amps": [0.635988],
    "RMS": [1.1361],
    "diff_encoder_l": [89.718974]}
    max_cols = pd.DataFrame(data=max_cols)
    
    # Normalize input.
    data.loc[:, cols_to_norm] = (data[cols_to_norm] - min_cols) / (max_cols - min_cols)
    
    input_model_ready =  data.values
    
    # Load trained model.
    loaded_model = pickle.load(open(filename, 'rb'))
    
    # Perform classification.
    out = loaded_model.predict(input_model_ready[:,:-1])

    if out[0] == 0:
        return "Normal"
    elif out[0] == 1:
        return "Anomalous"
    else:
        return -1
