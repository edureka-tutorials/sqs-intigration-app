import boto3
import os

def write_to_sqs(first_name,last_name):
    client = boto3.client('sqs')
    data = {'firstname':first_name,'lastname':last_name}
    response = client.send_message( QueueUrl=os.environ['Q_URL'], MessageBody=str(data))
    print(response)