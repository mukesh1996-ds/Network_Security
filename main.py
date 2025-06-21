from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transfromation import DataTransformation
from networksecurity.entity.config_entity import DataTransformationConfig
import os,sys
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig


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

        logging.info("Data Tranformation Started")
        data_transfromation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transfromation_config)
        data_transformation_artifacts = data_transformation.initiate_data_transformation()
        print(data_transformation_artifacts)
        logging.info("Data Transformation Completed")

        logging.info("Model Trainer Started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,
                                   data_transformation_artifact=data_transformation_artifacts)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model Training Completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)