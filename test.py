import grpc
from Proto import master_pb2_grpc
from Proto import master_pb2


ip_address = "localhost"
port = "9090"

# create a channel
channel = grpc.insecure_channel("{}:{}".format(ip_address, port))

# create a stub
stub = master_pb2_grpc.masterStub(channel)

# create request object
request = master_pb2.PutDataRequest(key="City", value="Maribor")

# make gRPC call
response = stub.putData(request)

print(response)
# print("Response code:", response.response_code)
# print("Response message:", response.response_message)

