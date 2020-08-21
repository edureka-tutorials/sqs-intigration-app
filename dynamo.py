import boto3
import os
import requests


dynamo_table = os.environ['dynamo_table']
def write_to_dynamo(first_name, last_name):
    url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    res = requests.get(url)
    region = res.json()['region']
    dynamodb = boto3.client('dynamodb',region_name=region)
    dynamodb.put_item(TableName=dynamo_table, Item={'fuel_level':{'N':last_name},'vehicle_id':{'S':first_name}})
