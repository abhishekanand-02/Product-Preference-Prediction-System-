import os
import sys
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.logger import logging
from src.exception import customexception

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class DataTransformation:
    def __init__(self):
        self.preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

    def initiate_data_transformation(self, train_path: str, test_path: str):
        try:
            logging.info("Data Transformation started.")

            # Load data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and test data loaded successfully.")

            # Drop unnecessary columns
            drop_columns = ["product_id", "user_id", "user_name", "review_id", "img_link", "product_link"]
            train_df.drop(columns=drop_columns, inplace=True, errors='ignore')
            test_df.drop(columns=drop_columns, inplace=True, errors='ignore')

            logging.info(f"Dropped columns: {drop_columns}")

            # Convert price columns to numeric
            price_columns = ["discounted_price", "actual_price"]
            for col in price_columns:
                train_df[col] = train_df[col].astype(str).str.replace("₹", "", regex=True).str.replace(",", "", regex=True).astype(float)
                test_df[col] = test_df[col].astype(str).str.replace("₹", "", regex=True).str.replace(",", "", regex=True).astype(float)

            # Fill missing values with median
            for col in train_df.select_dtypes(include=['number']).columns:
                train_df[col] = train_df[col].fillna(train_df[col].median())
                test_df[col] = test_df[col].fillna(test_df[col].median())

            logging.info("Missing values handled successfully.")

            # Define preprocessing pipeline
            numeric_features = train_df.select_dtypes(include=['number']).columns.tolist()
            categorical_features = train_df.select_dtypes(include=['object']).columns.tolist()

            preprocessor = ColumnTransformer([
                ("num", StandardScaler(), numeric_features),
                ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_features)
            ])

            # Fit the preprocessor on the training data
            preprocessor.fit(train_df)

            # Save the preprocessor
            with open(self.preprocessor_obj_file_path, 'wb') as file:
                pickle.dump(preprocessor, file)

            logging.info(f"Preprocessor saved at {self.preprocessor_obj_file_path}")

            # Save the transformed data
            transformed_train_path = os.path.join(os.path.dirname(train_path), "train_transformed.csv")
            transformed_test_path = os.path.join(os.path.dirname(test_path), "test_transformed.csv")

            train_df.to_csv(transformed_train_path, index=False)
            test_df.to_csv(transformed_test_path, index=False)

            logging.info(f"Transformed data saved at {transformed_train_path} and {transformed_test_path}.")
            logging.info("Data Transformation completed successfully.")

        except Exception as e:
            logging.error("Exception occurred during data transformation", exc_info=True)
            raise customexception(e, sys)

if __name__ == "__main__":
    train_path = "/home/abhishek.anand/Desktop/Product_Preference_Prediction_System/artifacts/train.csv"  
    test_path = "/home/abhishek.anand/Desktop/Product_Preference_Prediction_System/artifacts/test.csv"    

    transformer = DataTransformation()
    transformer.initiate_data_transformation(train_path, test_path)
