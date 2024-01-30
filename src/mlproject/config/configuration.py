from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig

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
        
    def DataTransformationManager(self):
        try:
            config = self.config.data_transformation
            create_directory([config.root_dir])
            
            get_data_transformation = DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path
            )
            
            return get_data_transformation
            
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def ModelTrainerManager(self):
        try:
            config = self.config.model_trainer
            schema = self.schema.target_column
            params = self.params.ElasticNet
            
            create_directory([config.root_dir])
            
            get_model_trainer = ModelTrainerConfig(
                root_dir=config.root_dir,
                train_data_path=config.train_data_path,
                test_data_path=config.test_data_path,
                model_name=config.model_name,
                alpha=params.alpha,
                l1_ratio=params.l1_ratio,
                target_column=schema.name
            )
            
            return get_model_trainer
        
        
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def ModelEvalutionManager(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.target_column
        
        create_directory([config.root_dir])
        
        
        get_model_evalution = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            metric_file_name=config.metric_file_name,
            model_path=config.model_path,
            all_param=params,
            target_column=schema.name
        )
        
        return get_model_evalution
        