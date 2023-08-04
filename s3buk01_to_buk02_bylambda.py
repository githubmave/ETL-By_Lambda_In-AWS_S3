import json
import boto3
import urllib
from datetime import datetime
import os
def lambda_handler(event,context):
   s3_client = boto3.client('s3')
   response = s3_client.get_object(Bucket='jobbuck',Key='jobsTest02.json')
   contents = response['Body'].read()
   contents=json.loads(contents)

   try:
       for content in contents:
         if not content:
            return None
            print(content)
         else:
              data= json.dumps(content).encode('UTF-8')
              
              s3_client.put_object(Bucket = 'targetjobbuck',Key='jobsTest03.json',Body = data )
   except Exception as err:     
      print(err)


   
