# import json
# import requests
from aifc import Error
import boto3
import logging

# pdf_file = open('./CC_HW1.pdf', 'rb')
# data = {"name": "fazel", "lastName": "koozegar"}

# resp = requests.post(
#     'http://192.168.1.33:5000/api/test',
#     data= {'json_payload': json.dumps(data)},
#     files={'pdf_file' : ('file.pdf', pdf_file, 'application/pdf'),}
# )

# print(resp.status_code)
# print(resp.json()["message"])

# bytes_data = b'14'
# string_data = bytes_data.decode('utf-8')

# print(bytes_data)
# print(str(bytes_data))
# print(string_data)
BASE_DATA = {
    "ACCESS_KEY": "91ba6d98-079f-4601-939f-30ef872d084f",
    "SECRET_KEY": "277d66a89d2893a8f5e8a5b0dc50d0b023735aad39c32114d81d937b01a4f969",
    "ARVAN_CLOUD_ENDPOINT": "https://s3.ir-thr-at1.arvanstorage.com/",
    "BUCKET_NAME": "ccass1",
    "ATLAS_PASSWORD": "CCAss1_DBaas",
    "IMAGGA_API_KEY": "acc_c1493563a636108",
    "IMAGGA_API_SECRET": "82e6ea554b92076f1c0a3f7f7edd1aa9",
    "MAILGUN_API_KEY": "61835523e9c19e11262b9ebb9b15c79d-8c9e82ec-1678aac1",
    "RABBITMQ_URL": "amqps://seuumisc:rKJKzpOFICHQ8384CAhDDvLMrrMH_l3w@shark.rmq.cloudamqp.com/seuumisc:5672"
}


def s3_downloader(endpoint_url, access_key, secret_key, bucket_name, object_key, image_name):
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
    except Exception as exc:
        logging.error(exc)
    else:
        try:
            # bucket
            bucket = s3_resource.Bucket(bucket_name)

            object_name = object_key
            download_path = image_name

            bucket.download_file(
                object_name,
                download_path
            )
        except Error as e:
            logging.error(e)

s3_downloader(BASE_DATA["ARVAN_CLOUD_ENDPOINT"], BASE_DATA["ACCESS_KEY"], BASE_DATA["SECRET_KEY"], BASE_DATA["BUCKET_NAME"], "9931021_img1.png", './9931021_img_1.png')