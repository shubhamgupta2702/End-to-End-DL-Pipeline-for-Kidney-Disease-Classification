from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.exception.exception import CustomException
from src.logger.logger import logger
import sys

STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config = data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.unzip_data()
      
  
  
if __name__ == '__main__':
  try:
    logger.log(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.log(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
  except Exception as e:
    logger.error(f"{STAGE_NAME} failed with error: {e}")
    raise CustomException(e,sys)
  