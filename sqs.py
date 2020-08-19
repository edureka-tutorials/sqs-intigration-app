import boto3
import os
import requests

def write_to_sqs(first_name,last_name):
    url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    res = requests.get(url)
    region = res.json()['region']
    client = boto3.client('sqs',region_name=region)
    data = {'firstname':first_name,'lastname':last_name}
    response = client.send_message( QueueUrl=os.environ['Q_URL'], MessageBody=str(data))
    print(response)
