import boto3
from datetime import datetime
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")
s3 = boto3.client("s3")

def get_ec2_info():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()

    instance_count = 0
    state_counts = {}

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_count += 1

            state = instance["State"]["Name"]

            if state in state_counts:
                state_counts[state] += 1
            else:
                state_counts[state] = 1

    return instance_count, state_counts

s3_response = s3.list_buckets()
bucket_count = len(s3_response["Buckets"])

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

def get_s3_info():
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    bucket_count = len(response["Buckets"])

    return bucket_count

def save_report(report):
    with open("aws-resource-report.txt", "w") as file:
        file.write(report)

def upload_report():
    s3 = boto3.client("s3")

    bucket_name = "cloud-bootcamp-sidy-lab-2026"
    local_file = "aws-resource-report.txt"
    s3_key = "reports/aws-resource-report.txt"

    s3.upload_file(local_file, bucket_name, s3_key)

try:
    instance_count, state_counts = get_ec2_info()
    bucket_count = get_s3_info()

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
=== AWS CLOUD RESOURCE REPORT ===

Time: {formatted_time}

EC2
---
Total Instances: {instance_count}
"""

    for state, count in state_counts.items():
        report += f"{state}: {count}\n"

    report += f"""
S3
--
Total Buckets: {bucket_count}
"""

    print(report)

    save_report(report)

    upload_report()
    
    print("Report uploaded to S3 successfully!")

except ClientError as error:
    print(f"AWS Error: {error}")
