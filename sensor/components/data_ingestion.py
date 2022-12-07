from sensor.entity import config_entity,artifact_entity
from sensor import utils
from sensor.exception import SensorException
from sensor.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import os,sys




class DataIngestion:
    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"experting collection data as pandas data frame")
            #experting collection data as pandas data frame
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name,
                collection_name=self.data_ingestion_config.collection_name)
            
            logging.info(f"save data in feature store")
            # save data in feature store
            df.replace(to_replace='na', value=np.NAN, inplace=True)

            logging.info(f"create feature store folder if not available")
            #create feature store folder if not available
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)

            
            logging.info(f"save df to feature store folder")
            #save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path, index=False, header=True)

            logging.info(f"split the dataset inti train and test set")
            #split the dataset inti train and test set
            train_df,test_df = train_test_split(df, test_size=self.data_ingestion_config.test_size)

            logging.info(f"create dataset folder if not available")
            #create dataset folder if not available
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)

            logging.info(f"save df to feature store folder")
            #save df to feature store folder
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path, index=False, header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path, index=False, header=True)

            logging.info(f"prepare artifact")
            #prepare artifact

            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path)
        
                   
        except Exception as e:
            raise SensorException(e,sys)