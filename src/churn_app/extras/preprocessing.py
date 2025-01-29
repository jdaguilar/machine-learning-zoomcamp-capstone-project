# preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_input(data):
    # Assuming data is a dictionary with input features
    df = pd.DataFrame(data, index=[0])
    
    # Example preprocessing steps
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    
    return df_scaled