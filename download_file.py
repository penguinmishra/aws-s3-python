import boto3

BUCKET_NAME = 'mybucket'

# the file should exist in bucket.
# If not, you'd get 403 : forbidden error
FILE_KEY_NAME = 'cute_puppies.jpg'

session = boto3.Session(profile_name='default') # specify profile you use
s3 = session.resource('s3')

# FILE_NAME: file in bucket that needs to be downloaded.
# second argument: name of the file and path on local system where it needs to be downloaded to.
s3.Bucket(BUCKET_NAME).download_file(FILE_KEY_NAME, 'C:/Users/rahulmishra/Desktop/my_custom_file_name.jpg')

print('Done')