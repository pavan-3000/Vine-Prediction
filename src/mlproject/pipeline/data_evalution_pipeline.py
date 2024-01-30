from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig
from src.mlproject.config.configuration import ConfigManager

from src.mlproject.components.data_evalution import ModelEvaluation


class ModelEvalutionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            
            eva_config = ConfigManager()
            eva_config = eva_config.ModelEvalutionManager()
            Model_eva = ModelEvaluation(config=eva_config)
        
        
            Model_eva.save_result()
        
        except Exception as e:
            raise CustomException(e,sys)