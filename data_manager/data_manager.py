from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from utils import s3_handler, imagga_handler
from utils.base import BASE_DATA as bd
import hashlib
db_pass = bd["ATLAS_PASSWORD"]
uri = f"mongodb+srv://amirfazel45:{db_pass}@ccass1.x4qzd4s.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.ccass1


user_data = {}



# TODO get image urls from DB
def get_urls(data):
    hashed_national_code = str(hashlib.sha256(data.encode()).hexdigest())
    db_collection = db.brobankDB
    query = {"national_code": hashed_national_code}

    db_record = db_collection.find_one(query)
    global user_data
    user_data = db_record
    
    keys = [db_record["image1_key"], db_record["image2_key"]]
    print(keys[0], keys[1])
    return keys


def dowload_images(keys, data):
   endpoint_url = bd["ARVAN_CLOUD_ENDPOINT"]
   access_key = bd["ACCESS_KEY"]
   secret_key = bd["SECRET_KEY"]
   bucket_name = bd["BUCKET_NAME"]


   for index, key in enumerate(keys):
       s3_handler.s3_downloader(endpoint_url, access_key, secret_key, bucket_name, key, f'./{data}_img_{index}')
       



# TODO check for face recognition
def check_for_face_detection(data):
    image1_path = f'./{data}_img_1'
    image2_path = f'./{data}_img_2'

    img1_id = imagga_handler.image_has_face(image1_path)
    img2_id = imagga_handler.image_has_face(image2_path)

    return (img1_id, img2_id)



#TODO check for face similarity
def get_similarity(first_id, second_id):
    return imagga_handler.image_similarity(first_id, second_id)

#TODO change status in DB
def change_status(data, status):

    db_collection = db.brobankDB

    filter_query = {"national_id": data}
    operation = {"$set": {"status": status}}

    response = db_collection.update_one(filter_query, operation)

    if response.modified_count == 1:
        return True
    else:
        return False

# TODO send email




if __name__ == '__main__':
    data =  "9931001"
    keys = get_urls(data)
    dowload_images(keys, data) 
    faceID1, faceID2 = check_for_face_detection(data)
    if faceID1 is not None and faceID2 is not None:
        is_similar = get_similarity(faceID1, faceID2)

        if is_similar:
            pass

