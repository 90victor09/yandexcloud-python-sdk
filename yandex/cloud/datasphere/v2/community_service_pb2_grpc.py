# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.datasphere.v2 import community_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__pb2
from yandex.cloud.datasphere.v2 import community_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class CommunityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/Create',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.CreateCommunityRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/Get',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.GetCommunityRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__pb2.Community.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/Update',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.UpdateCommunityRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/Delete',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.DeleteCommunityRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/List',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.ListCommunitiesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.ListCommunitiesResponse.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.CommunityService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class CommunityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Creates community in specified organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns community.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates specified community.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes specified community.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List communities in specified organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Lists access bindings for specified community.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for specified community.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for specified community.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.CreateCommunityRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.GetCommunityRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__pb2.Community.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.UpdateCommunityRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.DeleteCommunityRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.ListCommunitiesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.ListCommunitiesResponse.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v2.CommunityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommunityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/Create',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.CreateCommunityRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/Get',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.GetCommunityRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__pb2.Community.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/Update',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.UpdateCommunityRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/Delete',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.DeleteCommunityRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/List',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.ListCommunitiesRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__service__pb2.ListCommunitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.CommunityService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
