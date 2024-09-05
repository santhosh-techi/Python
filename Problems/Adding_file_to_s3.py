import boto3

def create_bucket():
    s3=boto3.client('s3')
    adding=s3.create_bucket(bucket='santhoshsunnytest1')
    responce=bucketresponce['location']

create_bucket()