from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.pipeline.data_ingestion_pipeline import Pipeline

try:
    
    logging.info("data_ingestion is stared")
    obj = Pipeline()
    obj.DataIngestionPipeline()
    logging.info("data Ingestion is completed")
    
    
    
except Exception as e:
    raise CustomException(e,sys)