import os, boto3, json

def ec2_check(accountid):
    privateip = ""
    instacename = ""

    organizations = boto3.client('organizations')
    org_response = organizations.describe_account(
        AccountId=accountid
    )

    org_json = json.dumps(org_response, indent=4, sort_keys=True, default=str)

    org_database = json.loads(org_json)

    accountname = org_database['Account']['Name']
    
    print(accountid+","+accountname)
    if privateip != "":
        os.system("aws ec2 describe-instances --filter 'Name=network-interface.addresses.private-ip-address,Values="+privateip+" --query 'Reservations[].Instances[].{InstanceId:InstanceId,PrivateIP:PrivateIpAddress,Tag:Tags}'")

    if  instacename != "":
        os.system("aws ec2 describe-instances --filter 'Name=tag:Name,Values='"+instacename+" --query 'Reservations[].Instances[].{InstanceId:InstanceId,PrivateIP:PrivateIpAddress,Tag:Tags}'")