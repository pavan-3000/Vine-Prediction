from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from src.mlproject.config.configuration import ConfigManager

from sklearn.model_selection import train_test_split
import pandas as pd
import os


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        
    def get_data_transformation(self):
        try:
            
            df = pd.read_csv(self.config.data_path)
            
            df = df.drop('type',axis=1)
            df = df.dropna()
            train,test = train_test_split(df,test_size=0.2,random_state=42)
            
            train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
            test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
            
            logging.info('train test splited successfuuly')


            
            
            
        except Exception as e:
            raise CustomException(e,sys)
