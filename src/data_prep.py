import pandas as pd
import numpy as np
import os
train_data= pd.read_csv("D://workflow//mlops//Water-Potablity-using-DVC//data//raw//test.csv")
test_data=pd.read_csv("D://workflow//mlops//Water-Potablity-using-DVC//data//raw//train.csv")
def fill_missing_with_mean(df):
    for column in df.columns:
        if df[column].isnull().any():
            median_value = df[column].median()
            df.fillna({column: median_value}, inplace=True)

    return df
    
train_processed_data= fill_missing_with_mean(train_data)
test_processed_data= fill_missing_with_mean(test_data)
data_path=os.path.join("data","processed")
os.makedirs(data_path)
train_processed_data.to_csv(os.path.join(data_path,"train_processed.csv"),index=False)
test_processed_data.to_csv(os.path.join(data_path,"test_processed.csv"),index=False)