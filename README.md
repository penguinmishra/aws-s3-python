# s3-aws-python

## About
Demo of setting up AWS S3 bucket and uploading, downloading and listing file(s) with Python SDK boto3.

### Configuring aws credentials
- Install AWS CLI v2
- Run `aws configure` from your terminal.
- Enter your IAM user's aws_access_key_id, aws_secret_access_key, default region. You may skip Default output format and press enter.
- Your should have a ~/.aws directory created for you where these values live. For windows, the directory is under C:\Users\username\.aws
- Never show or share these credentials with anyone and keep them a secret.

---

### Way the code in this repo works
- The code does not have the aws_access_key_id and aws_secret_access_key hardcoded in them. The AWS SDK for python boto3 looks for these credentials in various places in an order. This order can be seen [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials).

---

###