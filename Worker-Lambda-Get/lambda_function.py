import json
import boto3
import pandas as pd
import grpc
from Proto import master_pb2_grpc
from Proto import master_pb2

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event["data_bucket_name"]
    filename = event["filename"]

    # read keys (testing purposes)
    print("Reading file: ", filename)
    obj = s3_client.get_object(Bucket=bucket_name, Key=filename)
    df_keys = pd.read_csv(obj['Body'])
    df_keys.columns = ["date_time"]

    ip_address = "0.tcp.eu.ngrok.io:11276"

    # create a channel
    channel = grpc.insecure_channel(ip_address)

    # create a stub
    stub = master_pb2_grpc.masterStub(channel)

    rows = []

    # iterate through keys
    print("Iterating through rows")
    for i in range(len(df_keys)):
        key = df_keys.iloc[i]["date_time"]

        # prepare gRPC request
        request = master_pb2.GetDataRequest(key="continent")
    
        # make gRPC call
        response = stub.getData(request)
    
        # retrieve value from response
        value = response.value
        
        # to json
        data = json.loads(value)
        data["date_time"] = key

        rows.append(data)

    df_get = pd.DataFrame(rows)
    df_get = df_get[['date_time', 'col_1', 'col_2', 'col_3']]

    print("Start sorting")

    sorted_df = df_get.sort_values(by=['date_time'], ascending=True)

    print("End sorting")
    
    


    



