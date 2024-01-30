from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.config.configuration import ConfigManager
from src.mlproject.components.data_validation import DataValidation


class DataValidationPipeline:
    def __init__(self):
        pass
    
    
    def get_status(self):
        try:
            validation_config  = ConfigManager()
            validation_config = validation_config.DataValidationManager()
            data_validation  = DataValidation(config=validation_config)
            data_validation.validate_all_columns()
            
        
        except Exception as e:
            raise CustomException(e,sys)