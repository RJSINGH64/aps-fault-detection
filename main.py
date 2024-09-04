from sensor.logger import logging 
from sensor.exception import SensorException 
import sys , os
from sensor.utils import get_coll_as_df
from sensor.entity.config_entity import DataIngestionConfig , TrainingPipelineConfig  , DataValidationConfig
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation



if __name__=="__main__":
    try :
        training_pipe_config = TrainingPipelineConfig()      # saving dataset inside artifact folder 
        data_ingestion_config = DataIngestionConfig(training_pipe_config)
        print(data_ingestion_config.to_dict()) 
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print("\n Data Ingestion initiated Sucessfully")
        
        

        data_validation_config  = DataValidationConfig(training_pipe_config)
        data_validation = DataValidation(data_validation_config=data_validation_config , data_ingestion_artifact=data_ingestion_artifact)

        data_validation_artifact=data_validation.initiate_data_validation()
    
    
    
    
    except Exception as e:
        print(e)
