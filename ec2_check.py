import os, boto3

def ec2_check(accountid):
    
    os.system("aws ec2 describe-instances --filter 'Name=tag:Environment,Values=Staging' --query 'Reservations[].Instances[].{InstanceId:InstanceId,PrivateIP:PrivateIpAddress,Tag:Tags}'")

    return