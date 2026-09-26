import boto3

s3 = boto3.client("s3")

bucket_name = "cloud-bootcamp-sidy-lab-2026"

response = s3.list_objects_v2(Bucket=bucket_name)

print(f"=== OBJECTS IN {bucket_name} ===")

for object in response.get("Contents", []):
    print(f"Object: {object['Key']}")