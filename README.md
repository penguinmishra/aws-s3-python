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

### Setting up the bucket policy
- Create a new bucket from either CLI or console. Give a name to it and create with all default setting.

- Click on the bucket and go to the 'Permissions' tab. Go to Bucket policy section and hit edit.

![Permissions Tab](https://github.com/penguinmishra/aws-s3-python/blob/main/images/1.png)
![Bucket policy](https://github.com/penguinmishra/aws-s3-python/blob/main/images/2.png)

- Put the following policy in it and alter as per below instructions:

```
{
    "Version": "2012-10-17",
    "Id": "Policy1666972480623",
    "Statement": [
        {
            "Sid": "Stmt1666972496898",
            "Effect": "Allow",
            "Principal": {
                "AWS": "<USER_ARN>"
            },
            "Action": [
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:PutObject"
            ],
            "Resource": [
                "<BUCKET_ARN>",
                "<BUCKET_ARN>/*"
            ]
        }
    ]
}

```

- You can see ARN of your bucket in Properties tab under Bucket overview section:

![ARN of the bucket](https://github.com/penguinmishra/aws-s3-python/blob/main/images/3.png)

- Copy that and put these under "Resource" section in above JSON.

- For your principal ARN, go to IAM -> select Users -> select your user -> copy User ARN. Paste it in "Principal" section of above JSON.

![Get IAM User ARN](https://github.com/penguinmishra/aws-s3-python/blob/main/images/5.png)

- This policy enables your user ARN to do "Actions" specified on this bucket (specified by `BUCKET_ARN` in "Resources") and its objects (specified by `/*` in "Resources").
---
### Setting up IAM Users with permissions to access bucket

- The user also need to have permissions to interact with your S3 bucket.
- To do that, go to IAM -> select Users -> select your user -> Go to Permissions tab and click on "Add inline policy".
![Adding inline policy for IAM User](https://github.com/penguinmishra/aws-s3-python/blob/main/images/6.png)

- Inline policies have lifespan for the user's existence and can be done away easily. Alternatively you can create a separate policy by going to Policies in left pane of the IAM page.

- Add following JSON in policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "arn:aws:s3:::*"
        }
    ]
}

```

- Notice an asterick `*` after `arn:aws:s3:::`? This means that you give "Action" permissions to this user on all of your buckets. To make this policy narrower, you can just paste your bucket's ARN from above also.
- Save it. This will apply the policy permissions to your user.
- Now your S3 bucket authorizes your IAM user and your IAM user have all the required permissions.

