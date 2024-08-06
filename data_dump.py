import pymongo
import pandas
#connecting to a MongoDB Atlas using url

client = pymongo.MongoClient("mongodb+srv://rajatksingh64:ROCKINGRJ12345@cluster0.owfzau8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database_name="aps"
file_path=r"D:\Downloaded files\aps_failure_training_set1.csv"
collection_name="sensor"

if __name__=="__main__":
   df=pandas.read_csv(file_path)
   print(f"Rows and Columns : {df.shape}")

   #converting dataframe into a json format ,  so we can dump it into a MongoDB
   df.reset_index(drop=True , inplace=True)
   
   