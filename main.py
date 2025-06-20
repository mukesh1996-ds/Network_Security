from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import os,sys


if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingstion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifacts = data_ingstion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifacts)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifacts,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)
        

        

    except Exception as e:
        raise NetworkSecurityException(e,sys)