from sensor.logger import logging 
from sensor.exception import SensorException 
import sys , os
from sensor.utils import get_coll_as_df
from sensor.entity.config_entity import DataIngestionConfig , TrainingPipelineConfig  , DataValidationConfig , DataTransformationConfig , ModelTrainerConfig , ModelEvaluationConfig , ModelPusherConfig
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evalution import ModelEvaluation
from sensor.components.model_pusher import ModelPusher


if __name__=="__main__":
    try :
        # saving dataset inside artifact folder 
        training_pipe_config = TrainingPipelineConfig()      
        
        #Data ingestion
        data_ingestion_config = DataIngestionConfig(training_pipe_config)
        print(data_ingestion_config.to_dict()) 
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(">"*10,"1st pipeline data ingestion initiated  Sucessfully","<"*10)
        #Data validation 
        data_validation_config  = DataValidationConfig(training_pipe_config)
        data_validation = DataValidation(data_validation_config=data_validation_config , data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact=data_validation.initiate_data_validation()
        print(">"*10,"2nd Pipeline Data validation initiated  Sucessfully","<"*10)
        #Data transformation
        data_transformation_config = DataTransformationConfig(training_pipe_config)
        data_transformation=DataTransformation(data_transformation_config=data_transformation_config , data_ingestion_artifact=data_ingestion_artifact)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(">"*10,"3rd Pipeline Data transformation initiated Sucessfully","<"*10)
        #model trainer
        model_trainer_config = ModelTrainerConfig(training_pipe_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config , data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        print(">"*10,"4th Model trainer Initiated Sucessfully","<"*10)
        #model evaluation

        model_eva_config = ModelEvaluationConfig(training_pipeline_config=training_pipe_config)
        model_evalution = ModelEvaluation(model_eval_config=model_eva_config ,
                                          data_ingestion_artifact=data_ingestion_artifact,
                                          data_transformation_artifact=data_transformation_artifact , 
                                          model_trainer_artifact=model_trainer_artifact
                                          )
                                          
        model_evaluation_artifact = model_evalution.initiate_model_evaluation()    
        print(">"*10 , " 5th Pipeline Model Evalution Initiated Sucessfully" , "<"*10)                             
       
        #model pusher
        model_pusher_config = ModelPusherConfig(training_pipeline_config=training_pipe_config)
        model_pusher = ModelPusher(data_transformation_artifact=data_transformation_artifact  , 
                                  model_pusher_config=model_pusher_config , model_trainer_artifact=model_trainer_artifact)
        
        model_pusher_artifact=model_pusher.initiate_model_pusher()
        print(">"*10 , "6th Pipeline Model Pusher initiated " , "<"*10)
        


    except Exception as e:
        raise SensorException(e , sys)
