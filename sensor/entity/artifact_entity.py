from dataclasses import dataclass
@dataclass
class DataIngestionArtifact:

     feature_store_file_path:str
     train_file_path :str
     test_file_path :str


class DataValidationArtifact:
     
     def __init__(self , report_file_path:str):
     
         self.report_file_path=report_file_path
     

class DataTransformationArtifact:
   pass

class ModelTrainerArtifact:
   pass
 
class ModelEvaluationArtifact:

   pass
class ModelPusherArtifact:
   pass