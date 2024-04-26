import grpc
from Proto import master_pb2_grpc
from Proto import master_pb2


ip_address = "7.tcp.eu.ngrok.io:19283"
# port = "9090"

# create a channel
channel = grpc.insecure_channel(ip_address)
# channel = grpc.insecure_channel("{}:{}".format(ip_address, port))

# create a stub
stub = master_pb2_grpc.masterStub(channel)

# create request object
request = master_pb2.PutDataRequest(key="city", value="Dubai")

# make gRPC call
response = stub.putData(request)

print(response)

