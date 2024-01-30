from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.config.configuration import ConfigManager
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_validation import DataValidation


class Pipeline:
    def __init__(self):
        pass
    
    
    def DataIngestionPipeline(self):
        try:
            ingestion_config = ConfigManager()
            ingestion_config = ingestion_config.DataIngestionManager()
            data_ingestion = DataIngestion(config=ingestion_config)
            data_ingestion.download_zip_file()
            data_ingestion.unzip_file()
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def DataValidationPipeline(self):
        try:
            validation_config  = ConfigManager()
            validation_confg = validation_config.DataValidationManager()
            data_validation  = DataValidation(config=validation_config)
            data_validation.validate_all_columns()
            
        
        except Exception as e:
            raise CustomException(e,sys)