import os, boto3

def ec2_check(accountid):

    privateip = ""
    instacename = ""

    if privateip != "":
        os.system("aws ec2 describe-instances --filter 'Name=network-interface.addresses.private-ip-address,Values="+privateip+" --query 'Reservations[].Instances[].{InstanceId:InstanceId,PrivateIP:PrivateIpAddress,Tag:Tags}'")

    if  instacename != "":
        os.system("aws ec2 describe-instances --filter 'Name=tag:Name,Values='"+instacename+" --query 'Reservations[].Instances[].{InstanceId:InstanceId,PrivateIP:PrivateIpAddress,Tag:Tags}'")