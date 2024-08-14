from sensor.utils import get_coll_as_df
import pandas as pd
import numpy as np
from sensor.config import mongo_client
df = get_coll_as_df("aps" , "sensor")
print(df)