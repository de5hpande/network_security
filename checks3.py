import boto3

# Ensure correct region
s3_client = boto3.client('s3', region_name='us-east-1')

# List objects
try:
    response = s3_client.list_objects_v2(Bucket='networksecuritys3')
    print(response)
except s3_client.exceptions.NoSuchBucket:
    print("The specified bucket does not exist.")
