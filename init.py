import boto3
from botocore.exceptions import NoCredentialsError

# Create an S3 client
s3 = boto3.client('s3')

def upload_to_s3(file_name, bucket, object_name=None):
    try:
        if object_name is None:
            object_name = file_name
        s3.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded successfully.")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except NoCredentialsError:
        print("Credentials not available.")

# Example usage: Uploading captured image
file_name = 'frame.jpg','ap.jpg'  # Image from your classifier
bucket_name = 'objectclassifier'
upload_to_s3(file_name, bucket_name)
