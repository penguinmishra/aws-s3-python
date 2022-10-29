import boto3

# btw, there is not concept of 'folder' or 'directory' in s3.

FOLDER_NAME = 'outer_folder/inner_folder/'
BUCKET_NAME = 'mybucket'

session = boto3.Session(profile_name='default') # specify profile you use
s3 = session.resource('s3')

# create new key.
s3.Bucket(BUCKET_NAME).put_object(Key=FOLDER_NAME)