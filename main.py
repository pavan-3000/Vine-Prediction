from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.pipeline.data_ingestion_pipeline import Pipeline
from src.mlproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.mlproject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.mlproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.mlproject.pipeline.data_evalution_pipeline  import ModelEvalutionPipeline
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



try:
    logging.info('data transformatoin has stasred ')
    
    trans = DataTransformationPipeline()
    trans.main()
    
    logging.info("data transformation has completed")
except Exception as e:
    raise CustomException(e,sys)



try:
    
    logging.info("model trainer has started ")
    
    model = ModelTrainerPipeline()
    model.main()
    
    logging.info("model had successfull complted")
    
    
    
    
except Exception as e:
    raise CustomException(e,sys)


try:
    model_eval = ModelEvalutionPipeline()
    model_eval.main()
except Exception as e:
    raise CustomException(e,sys)