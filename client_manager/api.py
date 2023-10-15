from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from base import BASE_DATA as bd
from s3_handler import arvan_uploader
from utils.adress_generator import get_s3_addresses


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

    for file in file_addresses:
            arvan_uploader(endpoint_url, access_key, secret_key, bucket_name, file[0], file[1])
    

    res = {'message': 'successfully changed'}
    return jsonify(res), 200

@app.route('/api/check/<request_id>', methods=['GET'])
def check_request(request_id):
    res = {'message': 'successfully changed the request situation'}
    return jsonify(res), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)