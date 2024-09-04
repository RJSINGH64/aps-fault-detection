import pymongo 
import pandas 
from dataclasses import dataclass 
import json 
import os



@dataclass 

class Environment_variable() :
    pymongo_url :str = os.getenv("mongo_url")


env_var = Environment_variable()
mongo_client = pymongo.MongoClient(env_var.pymongo_url)
TARGET_COLUMN="class"

