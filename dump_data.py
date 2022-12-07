import pandas as pd
import pymongo
import json


# Provide the mongodb  url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")

database_name = 'aps'
collection_name = 'sensor'

data_file_path = r"E:\DATA_SCIENCE\PROJECT\\airps_failure_training_set1.csv"

if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f"rows and columns:{df.shape}")

    #convert dataset into json file so that we can dump these record in mongodb
    #droping the default index
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    #insert record to mongodb
    client[database_name][collection_name].insert_many(json_record)

