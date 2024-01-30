from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig
from src.mlproject.config.configuration import ConfigManager
from src.mlproject.constants import *
from src.mlproject.utils.common import save_json
import os
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import joblib
import numpy as np




class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_squared_error(actual,pred)
        r2 = r2_score(actual,pred)
        
        return rmse,mae,r2
    
    
    def save_result(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        x_test = test_data.drop([self.config.target_column],axis=1)
        y_test = test_data[[self.config.target_column]]
        
        predicted  = model.predict(x_test)
        
        (rmse,mae,r2) = self.eval_metrics(y_test,predicted)
        
        
        score = {"rmse": rmse,"mae": mae , "r2":r2}
        save_json(path=Path(self.config.metric_file_name),data = score)