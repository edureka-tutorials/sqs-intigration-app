import boto3
import os


dynamo_table = os.environ['dynamo_table']
def write_to_dynamo(first_name, last_name):
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName=dynamo_table, Item={'fuel_level':{'N':last_name},'vehicle_id':{'S':first_name}})