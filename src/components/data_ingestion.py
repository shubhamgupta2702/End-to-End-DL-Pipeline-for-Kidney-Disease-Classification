import zipfile
import os
import sys
import gdown
from src.logger.logger import logger
from src.exception.exception import CustomException
from src.utils.utils import get_size
from src.entity.entity import DataIngestionConfig

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.config = config
    
  def download_data(self):
    """Function to download data from google drive"""
    try:
      dataset_url = self.config.source_URL
      zip_download_dir = self.config.local_data_file_path
      os.makedirs(self.config.root_dir, exist_ok=True)
      logger.info(f"Downloading data from {dataset_url} to {zip_download_dir}")
      
      file_id = dataset_url.split('/')[-2]
      prefix_url = 'https://drive.google.com/uc?id='
      complete_url = prefix_url + file_id
      gdown.download(complete_url, zip_download_dir)
      logger.info(f'Downloaded data from {dataset_url} to {zip_download_dir}')
      
    except Exception as e:
      logger.error(f"Error downloading data from {dataset_url} to {zip_download_dir}: {e}")
      raise CustomException(e, sys)
    
  def unzip_data(self):
    """Function to unzip data"""
    try:
      unzip_dir = self.config.unzip_dir
      os.makedirs(unzip_dir, exist_ok=True)
      with zipfile.ZipFile(self.config.local_data_file_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)
      logger.info(f"Unzipped data from {self.config.local_data_file_path} to {unzip_dir}")
      
    except Exception as e:
      logger.error(f"Error unzipping data from {self.config.local_data_file_path} to {unzip_dir}: {e}")
      raise CustomException(e, sys)