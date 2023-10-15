import boto3
import logging
from botocore.exceptions import ClientError
from PIL import Image
from base import BASE_DATA

# Configure logging
logging.basicConfig(level=logging.INFO)
endpoint_url= BASE_DATA.ARVAN_CLOUD_ENDPOINT
secret_key = BASE_DATA.SECRET_KEY
access_key = BASE_DATA.ACCESS_KEY

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
       bucket = s3_resource.Bucket('9931099')
       file_path = './file.txt'
       object_name = 'eyeIeye.txt'

       with open(file_path, "rb") as file:
           bucket.put_object(
               ACL='private',
               Body=file,
               Key=object_name
           )


   except ClientError as e:
       logging.error(e)

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
       bucket = s3_resource.Bucket("9931099")

       object_name = 'file.txt'
       download_path = './filee.txt'

       bucket.download_file(
           object_name,
           download_path
       )
   except ClientError as e:
       logging.error(e)



