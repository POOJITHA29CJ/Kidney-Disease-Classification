from KidneyTumorClassifier import logger
from dataclasses import dataclass
from pathlib import Path
from KidneyTumorClassifier.constants import *
from KidneyTumorClassifier.utils.common import read_yaml,create_directories
import os
import urllib.request as request
import zipfile
import gdown
from KidneyTumorClassifier import logger
from KidneyTumorClassifier.utils.common import get_size
@dataclass(frozen=True) # entity - return type of any function
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path
class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        print(config_filepath)
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        print("hello--------------")
        print(f"Data Ingestion Config: {config}")
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        print(self.config)
    def download_file(self)->str:
        try:
            dataset_url=self.config.source_URL
            zip_download_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to the file {zip_download_dir}")
            file_id=dataset_url.split("/")[-2]
            prefix="https://drive.google.com/uc?/export=downloads&id="
            gdown.download(prefix+file_id,zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} to the file {zip_download_dir}")
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
try:
        config_manager = ConfigurationManager()
        print("poojitha")
        print(config_manager.config)
        print(config_manager.config['artifacts_root'])  # Corrected access
        
        data_ingestion_config = config_manager.get_data_ingestion_config()
        print(data_ingestion_config)
        print("data_injesion has been returned")
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
except Exception as e:
        raise e