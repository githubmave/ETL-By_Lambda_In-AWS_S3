import json
import boto3
import urllib
from datetime import datetime
import os
def lambda_handler(event,context):
   s3_client = boto3.client('s3')
   response = s3_client.get_object(Bucket='jobbuck',Key='jobsTest02.json')
   data=response['Body'].read()
   contents=json.loads()
   print(data)
   # bucket_name = event['Records'][0]['s3']['bucket']['name']
   #  key = event['Records'][0]['s3']['object']['key']
   #  key = urllib.parse.unquote_plus(key,encoding='utf-8')
   #  message = 'hey this file got uploaded' + key + 'to this bucket' + bucket_name
   #  print(message)
   #  response = s3_client.get_object(Bucket=bucket_name,Key = key)
   #  contents = response["Body"].read().decode()
   #  contents =json.loads(contents)
   #  for content in contents:
   #      print(content['_id'])
   #      print(content['title'])
# def uploads3(s3_client,,):
