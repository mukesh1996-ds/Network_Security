from networksecurity.components.data_ingestion import DataIngestion
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
        print(dataingestionartifacts)
    except Exception as e:
        raise NetworkSecurityException(e,sys)