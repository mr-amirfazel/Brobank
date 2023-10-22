from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import sys
sys.path.append('../')
from base import BASE_DATA as bd
import hashlib
db_pass = bd["ATLAS_PASSWORD"]
uri = f"mongodb+srv://amirfazel45:{db_pass}@ccass1.x4qzd4s.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.ccass1


data =  "9931001"
keys = ["", ""]


# TODO get image urls from DB
def get_urls():
    global keys
    hashed_national_code = str(hashlib.sha256(data.encode()).hexdigest())
    db_collection = db.brobankDB
    query = {"national_code": hashed_national_code}

    db_record = db_collection.find_one(query)

    keys = [db_record["image1_key"], db_record["image2_key"]]
    print(keys[0], keys[1])


# TODO get images from s3
def dowload_images():
   pass



# TODO check for face recognition


#TODO check for face similarity

#TODO change status in DB

# TODO send email

get_urls()


if __name__ == '__main__':
    pass