import json
import boto3
import math

def lambda_handler(event, context):
    bucket_name = event["data_bucket_name"]
    filenames = event["filenames"]

    print("Bucket name: {}".format(bucket_name))
    print("Filenames {}".format(filenames))