import json
import boto3
import pandas as pd
import grpc
from Proto import master_pb2_grpc
from Proto import master_pb2

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event["data_bucket_name"]
    filenames = event["filenames"]

    print("Bucket name: {}".format(bucket_name))
    print("Filenames {}".format(filenames))

    ip_address = "0.tcp.eu.ngrok.io:19523"

    # create a channel
    channel = grpc.insecure_channel(ip_address)
    
    # create a stub
    stub = master_pb2_grpc.masterStub(channel)

    # iterate through files
    for filename in filenames:
        print("Reading file: ", filename)
        obj = s3_client.get_object(Bucket=bucket_name, Key=filename)
        df = pd.read_csv(obj['Body'])
        df.columns = ["date_time", "col_1", "col_2", "col_3"]
        
        # iterate through rows
        print("Iterating through rows")
        for i in range(len(df)):
            row = df.iloc[i]
            key = row["date_time"]
            value = {
                "col_1": float(row["col_1"]),
                "col_2": float(row["col_2"]),
                "col_3": float(row["col_3"])
            }

            value_json = json.dumps(value)

            # create request object
            request = master_pb2.PutDataRequest(key=key, value=value_json)

            # make gRPC call
            response = stub.putData(request)
