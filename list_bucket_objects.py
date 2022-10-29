import boto3

BUCKET_NAME = 'mybucket'

session = boto3.Session(profile_name='default') # specify profile you use
s3 = session.resource('s3')

# list all object keys
listObjSummary = s3.Bucket(BUCKET_NAME).objects.all()

for obj in listObjSummary:
    print(obj.key)

print('Done')
