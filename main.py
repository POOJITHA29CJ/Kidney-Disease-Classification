from KidneyTumorClassifier import logger
from KidneyTumorClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME="Data Ingestion Stage"
print(STAGE_NAME)
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e