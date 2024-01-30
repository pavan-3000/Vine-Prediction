from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import ModelTrainerConfig

from src.mlproject.config.configuration import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib
import pandas as pd
import os
class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
        
    def train(self):
        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)
        
        x_train = train.drop(self.config.target_column, axis=1)
        y_train = train[self.config.target_column]
        
        
        x_test = test.drop(self.config.target_column, axis=1)
        y_test = test[self.config.target_column]
        
        lr  = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        lr.fit(x_train,y_train)
        
        
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))