import json
import boto3
import math


# splits files into chunks
def split_filenames(filenames, num_chunks):
    chunk_size = math.ceil(len(filenames) / num_chunks)
    return [filenames[i:i+chunk_size] for i in range(0, len(filenames), chunk_size)]


# invokes subsequent lambda and passes filenames as parameter
def invoked_subsequent_lambda(lambda_name, s3_bucket_name, filenames):
    lambda_client = boto3.client('lambda')
    payload = json.dumps({"data_bucket_name": s3_bucket_name, "filenames": filenames})

    print(payload)
    
    response = lambda_client.invoke(
        FunctionName=lambda_name,
        InvocationType="Event",
        Payload=payload)
    
    return response


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # extract event parameters
    bucket_name = event["data_bucket_name"]
    num_lambdas = event["num_lambdas"]
    subsequent_lambda_name = event["subsequent_lambda_name"]

    response_bucket = s3.list_objects_v2(Bucket=bucket_name)
    filenames = [obj['Key'] for obj in response_bucket['Contents']]

    print("Number of Lambdas: {}".format(num_lambdas))

    # split filenames into subsets (chunks) for each subsequent Lambda
    filenames_chunks = split_filenames(filenames, num_lambdas)

    # invoke subsequent lambdas
    for filenames_subset in filenames_chunks:
        invoked_subsequent_lambda(subsequent_lambda_name, bucket_name, filenames_subset)
    
    return {
        "statusCode": 200,
        "body": json.dumps("Workload distribution completed successfully")
    }

    
    # # iterate through all objects in bucket
    # for obj in response_bucket["Contents"]:
    #     response_object = s3.get_object(Bucket=bucket_name, Key=obj["Key"])
    #     body = response_object["Body"]
    #     text = body.read().decode("utf-8")

    #     # print name and body of object
    #     print("File: {}, Text: {}".format(obj["Key"], text))

    #     # add to queue => node_id|bucket_name|object_name
    #     response_queue = sqs.send_message(QueueUrl=queue_url, MessageBody="{}|{}|{}".format(i % num_lambdas + 1, bucket_name, obj["Key"]))
    #     i += 1


if __name__ == "__main__":
    event = {"data_bucket_name": "thesis-test-db", 
             "num_lambdas" : 4,
             "subsequent_lambda_name": "WorkerTest"}
    context = 0
    lambda_handler(event, context)

