import boto3

s3 = boto3.client("s3")

bucket_name = "cloud-bootcamp-sidy-lab-2026"

s3_key = "boto3-test.txt"
local_file = "downloaded-test.txt"

s3.download_file(bucket_name, s3_key, local_file)

print("Download successful!")