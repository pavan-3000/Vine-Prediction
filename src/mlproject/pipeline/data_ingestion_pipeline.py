from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.config.configuration import ConfigManager
from src.mlproject.components.data_ingestion import DataIngestion


class Pipeline:
    def __init__(self):
        pass
    
    
    def DataIngestionPipeline(self):
        try:
            config = ConfigManager()
            config = config.DataIngestionManager()
            data_ingestion = DataIngestion(config=config)
            data_ingestion.download_zip_file()
            data_ingestion.unzip_file()
        except Exception as e:
            raise CustomException(e,sys)