from KidneyTumorClassifier.config.configuration import ConfigurationManager
from KidneyTumorClassifier.components.data_ingestion import DataIngestion
from KidneyTumorClassifier import logger
from KidneyTumorClassifier.entity.config_entity import DataIngestionConfig
STAGE_NAME="Data Ingestion Stage"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
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
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e