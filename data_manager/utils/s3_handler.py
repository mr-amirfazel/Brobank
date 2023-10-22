import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

def s3_downloader(endpoint_url, access_key, secret_key, bucket_name, object_key, ):
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url='endpoint_url',
            aws_access_key_id='access_key',
            aws_secret_access_key='secret_key'
        )
    except Exception as exc:
        logging.error(exc)
    else:
        try:
            # bucket
            bucket = s3_resource.Bucket('bucket_name')

            object_name = 'object_name.txt'
            download_path = '/the/abs/path/to/file.txt'

            bucket.download_file(
                object_name,
                download_path
            )
        except ClientError as e:
            logging.error(e)
