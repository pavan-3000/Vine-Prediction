from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.mlproject.config.configuration import ConfigManager

import pandas as pd

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config
        
    
    def validate_all_columns(self):
        try:
            validation_status= None
            
            df = pd.read_csv(self.config.unzip_path)
            all_col = list(df.columns)
            valid_col = self.config.all_schema.keys()
            
            for col in all_col:
                if col not in valid_col:
                    validation_status = False
                    with open(self.config.STATUS_file,'w') as f:
                        f.write(validation_status)
                else:
                    validation_status = True
                    with open(self.config.STATUS_file,'w') as f:
                        f.write(f"validation status : {validation_status}")
            
            return validation_status
                    
            
            
            
        except Exception as e:
            raise CustomException(e,sys)