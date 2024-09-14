from sensor.pipeline.batch_prediction import start_batch_prediction 

file_path =r"E:\PYTHON PROJECTS\V-S Code Projects\app_fault_detection\aps_failure_training_set1.csv"

if __name__=="__main__":
    try :
        
        Batch_output=start_batch_prediction(input_file_path=file_path)
        print(">"*15," Current Prediction is " , ">"*15)
        print(">"*15,Batch_output,"<"*15)
    
    except Exception as e:
        raise SensorException(e , sys)
