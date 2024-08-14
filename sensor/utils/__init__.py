import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os , sys

#loading data_frame from mongo db using url 

def get_coll_as_df(database_name:str , collection_name:str)-> pd.DataFrame:
    
    """

    Description :-

    Database_name :str name of database\n
    collection_name:str name of collection\n
    =========================================================

    this function return dataframe as df 

    """
    
    
    
    
    try:
       
       logging.info(f"Reading database{database_name} and collection {collection_name}")
       df =pd.DataFrame(list( mongo_client[database_name][collection_name].find()))
       logging.info(f" columns present inside a dataset {df.columns}")
       if "_id" in df.columns:
           logging.info(f"Droping column _id from dataset")
           df=df.drop("_id"  , axis=1)
       return df
    
    except Exception as e :
        raise SensorException(e , sys)