from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from base import BASE_DATA as bd
from utils.s3_handler import arvan_uploader
from utils.adress_generator import get_s3_addresses
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import hashlib
from utils.status import STATUS

with open('./assets/img1.png', "rb") as file:
               print("works")
db_pass = bd["ATLAS_PASSWORD"]
uri = f"mongodb+srv://amirfazel45:{db_pass}@ccass1.x4qzd4s.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.ccass1

endpoint_url= bd["ARVAN_CLOUD_ENDPOINT"]
secret_key = bd["SECRET_KEY"]
access_key = bd["ACCESS_KEY"]
bucket_name = bd["BUCKET_NAME"]

app = Flask(__name__)
CORS(app)

@app.route('/api/register', methods=['POST'])
def register_request():
    user_info = request.get_json()
    file_addresses = get_s3_addresses(user_info)

    img1_key = file_addresses[0][1]
    img2_key = file_addresses[1][1]
    nat_code = user_info["national_code"]

    for file in file_addresses:
            arvan_uploader(endpoint_url, access_key, secret_key, bucket_name, file[0], file[1])
    
    db_data =  {
         "email": user_info["email"],
         "last_name": user_info["last_name"],
         "national_code": hashlib.sha256(nat_code.encode()).hexdigest(),
         "ip_address": user_info["ip_address"],
         "image1_key": img1_key,
         "image2_key": img2_key,
         "status": STATUS.PENDING
    }

    try:
        db.brobankDB.insert_one(db_data)
        res = {"message": "registration done successfully"}
        return jsonify(res), 200
    except Exception as e:
        print(e)
        res = {"message": "registration failed try again in a second..."}
        return jsonify(res), 401



@app.route('/api/check/<national_code>', methods=['GET'])
def check_request(national_code):
    hashed_national_code = str(hashlib.sha256(national_code.encode()).hexdigest())
    db_collection = db.brobankDB
    query = {"national_code": hashed_national_code}

    
    try:
        if db_collection.count_documents(query) == 1:
            query_res = db_collection.find_one(query)
            print(query_res)
            res = {"state": query_res["status"]}
            return jsonify(res), 200
        else:
            res = {'message': 'No account found with this National code'}
            return jsonify(res), 404
    except Exception as e:
        print('error: ',e)
        res = {"message": "something went wrong. try again in a second..."}
        return jsonify(res), 400




if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)