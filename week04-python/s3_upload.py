import boto3

s3 = boto3.client("s3")

bucket_name = "cloud-bootcamp-sidy-lab-2026"

local_file = "boto3-test.txt"
s3_key = "boto3-test.txt"

s3.upload_file(local_file, bucket_name, s3_key)

print("Upload successful!")