import boto3

print("=== AWS PYTHON AUTOMATION ===")
print(f"Boto3 version: {boto3.__version__}")

sts = boto3.client("sts")

identity = sts.get_caller_identity()

print()
print("Successfully connected to AWS!")
print(f"Account: {identity['Account']}")
print(f"ARN: {identity['Arn']}")