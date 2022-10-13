import os
from ec2_check import ec2_check
from sts_session import sts_session

def report():
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())
            ec2_check()

report()