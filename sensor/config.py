import pandas as pd
import pymongo
import json
from dataclasses import dataclass
import os,sys

# provide mongodb url to connect python to mongodb
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"
