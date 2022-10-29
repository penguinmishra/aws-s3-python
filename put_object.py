import boto3

BUCKET_NAME = 'mybucket'
FILE_NAME = 'C:/Users/rahulmishra/Desktop/cute_puppies.jpg'

# used in uploading file. rb = read bytes
data = open(FILE_NAME, 'rb')

session = boto3.Session(profile_name='default') # specify profile you use
s3 = session.resource('s3')

# ContentType is optional.
# if not provided, defaults to binary/octet-stream in bucket
# key would be the file name in s3.
s3.Bucket(BUCKET_NAME).put_object(Key='new_cute_puppies.jpg', Body=data, ContentType='image/jpeg')

print('Done')