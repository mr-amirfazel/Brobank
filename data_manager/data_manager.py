from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from utils import s3_handler, imagga_handler, mail_gun_handler, rabbit_consume
from utils.base import BASE_DATA as bd
from utils.status import STATUS
import hashlib
db_pass = bd["ATLAS_PASSWORD"]
uri = f"mongodb+srv://amirfazel45:{db_pass}@ccass1.x4qzd4s.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.ccass1


user_data = {}

# TODO get the national ID from RABBITMQ
def get_national_code():
    try:
        national_code = rabbit_consume.consume_data(bd["RABBITMQ_URL"])
        return national_code
    except Exception as e:
        print(e)

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
       s3_handler.s3_downloader(endpoint_url, access_key, secret_key, bucket_name, key, f'./{data}_img_{index+1}.png')
       



def check_for_face_detection(data):
    image1_path = f'./{data}_img_1.png'
    image2_path = f'./{data}_img_2.png'

    img1_id = imagga_handler.image_has_face(image1_path)
    img2_id = imagga_handler.image_has_face(image2_path)

    return (img1_id, img2_id)



def get_similarity(first_id, second_id):
    return imagga_handler.image_similarity(first_id, second_id)

def change_status(data, status):
    hashed_national_code = str(hashlib.sha256(data.encode()).hexdigest())

    db_collection = db.brobankDB

    filter_query = {"national_code": hashed_national_code}
    operation = {"$set": {"status": status}}

    response = db_collection.update_one(filter_query, operation)

    if response.modified_count == 1:
        print("uh huh")
        return True
    else:
        return False

def send_email():
    email = user_data["email"]
    last_name = user_data["last_name"]
    subject = "BROBANK Registeration request"
    text = f"dear {last_name}, your registeration at brobank was approved, you are now ready to apply for next steps..."

    mail_gun_handler.mailgun_send(last_name, email, subject, text)




if __name__ == '__main__':
    data =  "9931001"
    keys = get_urls(data)
    dowload_images(keys, data) 
    faceID1, faceID2 = check_for_face_detection(data)
    print(faceID1, faceID2)
    if faceID1 is not None and faceID2 is not None:
        print('theres face')
        is_similar = get_similarity(faceID1, faceID2)

        if is_similar:
            print('accept')
            change_status(data,STATUS.APPROVED)
            # send_email()
        else:
            print('reject')
            change_status(data, STATUS.REJECTED)
    else:
        print('no face')
        change_status(data, STATUS.REJECTED)

