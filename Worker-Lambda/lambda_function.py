import json
# import boto3
import math
import grpc
from Proto import master_pb2_grpc
from Proto import master_pb2

def lambda_handler(event, context):
    bucket_name = event["data_bucket_name"]
    filenames = event["filenames"]

    print("Bucket name: {}".format(bucket_name))
    print("Filenames {}".format(filenames))

    ip_address = "7.tcp.eu.ngrok.io:19283"

    # create a channel
    channel = grpc.insecure_channel(ip_address)
    
    # create a stub
    stub = master_pb2_grpc.masterStub(channel)

    # create request object
    request = master_pb2.PutDataRequest(key="city", value="Dubai")

    # make gRPC call
    response = stub.putData(request)

    print(response)
