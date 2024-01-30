from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.pipeline.data_ingestion_pipeline import Pipeline
from src.mlproject.pipeline.data_validation_pipeline import DataValidationPipeline
'''
try:
    
    logging.info("data_ingestion is stared")
    obj = Pipeline()
    obj.DataIngestionPipeline()
    logging.info("data Ingestion is completed")
    
    
    
except Exception as e:
    raise CustomException(e,sys)
'''

try:
    logging.info('stage 2 has started: data validation')
    
    obj = DataValidationPipeline()
    obj.get_status()
    logging.info("dart validation is completed completed susscessfully")
    
    
except Exception as e:
    raise CustomException(e,sys)