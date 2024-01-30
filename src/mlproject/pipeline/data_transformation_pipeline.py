from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataTransformationConfig
from src.mlproject.config.configuration import ConfigManager
from src.mlproject.components.data_transformation import DataTransformation



class DataTransformationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            tranformation_config = ConfigManager()
            tranformation_config = tranformation_config.DataTransformationManager()
            data_transformation = DataTransformation(config=tranformation_config)
            data_transformation.get_data_transformation()
            
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        