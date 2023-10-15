import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
# Configure logging
def arvan_uploader(endpoint_url, access_key, secret_key, bucket_name, file_address, image_key):
    
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
            bucket = s3_resource.Bucket(bucket_name)
            file_path = file_address
            object_name = image_key

            with open(file_path, "rb") as file:
                bucket.put_object(
                    ACL='private',
                    Body=file,
                    Key=object_name
                )


        except ClientError as e:
            logging.error(e)