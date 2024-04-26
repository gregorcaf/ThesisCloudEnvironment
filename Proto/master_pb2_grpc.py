# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Proto import master_pb2 as Proto_dot_master__pb2


class masterStub(object):
    """option java_multiple_files = true;
    option java_package = "si.mlimedija.proto";

    import "google/protobuf/any.proto";

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.putData = channel.unary_unary(
                '/master/putData',
                request_serializer=Proto_dot_master__pb2.PutDataRequest.SerializeToString,
                response_deserializer=Proto_dot_master__pb2.PutDataResponse.FromString,
                )
        self.getData = channel.unary_unary(
                '/master/getData',
                request_serializer=Proto_dot_master__pb2.GetDataRequest.SerializeToString,
                response_deserializer=Proto_dot_master__pb2.GetDataResponse.FromString,
                )


class masterServicer(object):
    """option java_multiple_files = true;
    option java_package = "si.mlimedija.proto";

    import "google/protobuf/any.proto";

    """

    def putData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_masterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'putData': grpc.unary_unary_rpc_method_handler(
                    servicer.putData,
                    request_deserializer=Proto_dot_master__pb2.PutDataRequest.FromString,
                    response_serializer=Proto_dot_master__pb2.PutDataResponse.SerializeToString,
            ),
            'getData': grpc.unary_unary_rpc_method_handler(
                    servicer.getData,
                    request_deserializer=Proto_dot_master__pb2.GetDataRequest.FromString,
                    response_serializer=Proto_dot_master__pb2.GetDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'master', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class master(object):
    """option java_multiple_files = true;
    option java_package = "si.mlimedija.proto";

    import "google/protobuf/any.proto";

    """

    @staticmethod
    def putData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/master/putData',
            Proto_dot_master__pb2.PutDataRequest.SerializeToString,
            Proto_dot_master__pb2.PutDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/master/getData',
            Proto_dot_master__pb2.GetDataRequest.SerializeToString,
            Proto_dot_master__pb2.GetDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)