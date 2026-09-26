import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

print("=== EC2 INSTANCE INVENTORY ===")

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        name = "No Name"

        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]

        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]
        state = instance["State"]["Name"]

        private_ip = instance.get("PrivateIpAddress", "None")
        public_ip = instance.get("PublicIpAddress", "None")

        print()
        print(f"Name: {name}")
        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")
        print(f"State: {state}")
        print(f"Private IP: {private_ip}")
        print(f"Public IP: {public_ip}")