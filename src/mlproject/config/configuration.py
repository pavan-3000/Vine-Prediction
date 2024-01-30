from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig

from src.mlproject.constants import *



from src.mlproject.utils.common import read_yaml,create_directory


class ConfigManager:
    def __init__(
        self,
        config_path = CONFIG_FILE_PATH,
        params_path = PARAMS_FILE_PATH,
        schema_path = SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)
        
        logging.info('read the yamll fliel')
        
        create_directory([self.config.artifacts_root])
        
        
        
    def DataIngestionManager(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            create_directory([config.root_dir])
            
            get_data_ingestion = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_file_path=config.local_file_path,
                unzip_path=config.unzip_path
            )
            
            return get_data_ingestion
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    def DataValidationManager(self):
        try:
            config = self.config.data_validation
            schema = self.schema.COLUMNS_NAME
            
            create_directory([config.root_dir])
            
            get_data_validation = DataValidationConfig(
                root_dir=config.root_dir,
                unzip_path=config.unzip_path,
                STATUS_file=config.STATUS_file,
                all_schema=schema
            )
            
            
            return get_data_validation
            
        except Exception as e:
            raise CustomException(e,sys)