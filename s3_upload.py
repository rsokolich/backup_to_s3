import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_aws(local_file, bucket, s3_file=None):
    """Upload a file to an S3 bucket
    :param local_file: File to upload
    :param bucket: Bucket to upload to
    :param s3_file: S3 object name. If not specified then filename is used
    :return: True if file was uploaded, else False
    """
    # If S3 object name was not specidied, use file_name
    if s3_file is None:
        s3_file = local_file
    
    if local_file != "":
        print("Uploading " + local_file + " to S3..." )

    # Upload the file
    s3 = boto3.client('s3') 
    try:
        s3.upload_file (local_file, bucket, s3_file,
        ExtraArgs={'StorageClass': 'DEEP_ARCHIVE'}) # Choose storage class; e.g STANDARD, STANDARD_IA, REDUCED_REDUNDANCY or DEEP_ARCHIVE.
        print ("Upload Successful")
        return True
    except FileNotFoundError:
        print ("The local Zip file was not found, upload to S3 failed.")
        return False
    except NoCredentialsError:
        print ("Credentials not available, upload to S3 failed.")
        return False