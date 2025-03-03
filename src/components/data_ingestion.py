from src.logger import logging
from src.exception import customexception
from sklearn.model_selection import train_test_split
import pandas as pd
import os 

class DataIngestionConfig:
    def __init__(self):
        self.raw_data_path = os.path.join("artifacts","raw.csv")
        self.train_data_path = os.path.join("artifacts","train.csv")
        self.test_data_path = os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion is Initiated.")
            
            file_path = "/home/abhishek.anand/Desktop/Product_Preference_Prediction_System/data/1/amazon.csv"
            data = pd.read_csv(f"{file_path}")
            logging.info(f"Reading data from {file_path} is completed")
            # logging.info(data.head(3))

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            logging.info("Performing train-test split")
            train_data, test_data = train_test_split(data,test_size=0.25, random_state=42)
            logging.info("Train-test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info(f"Train data saved at {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at {self.ingestion_config.test_data_path}")

            logging.info("Data ingestion completed successfully")

            return self.ingestion_config.train_data_path, self.ingestion_config.train_data_path


        except Exception as e:
            logging.exception("Exception occurred during data ingestion")   
            raise customexception(e)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()