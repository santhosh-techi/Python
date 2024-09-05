import boto3
 
def get_bucket_name():
    # Create an S3 client
    s3 = boto3.client('s3')
    # Retrieve bucket name from bucket ARN
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])
# Example usage
get_bucket_name()
