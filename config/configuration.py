import os
import dotenv 
from pymongo import MongoClient 


# Loading the enviroment varible, where I have the
# database URL

dotenv.load_dotenv()
DBURL = os.getenv("URL")

if not (DBURL):
    raise ValueError("Please, provide an URL")

# MongoDB instance

client = MongoClient(DBURL)
db = client.get_database()
first_collection = db["first"]