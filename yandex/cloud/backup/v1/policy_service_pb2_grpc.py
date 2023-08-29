# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.backup.v1 import policy_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_policy__pb2
from yandex.cloud.backup.v1 import policy_service_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class PolicyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/List',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListPoliciesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListPoliciesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Create',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.CreatePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Get',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.GetPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__pb2.Policy.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Update',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.UpdatePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Delete',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.DeletePolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Apply = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Apply',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ApplyPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListApplications = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/ListApplications',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListApplicationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListApplicationsResponse.FromString,
                )
        self.Execute = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Execute',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ExecuteRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Revoke = channel.unary_unary(
                '/yandex.cloud.backup.v1.PolicyService/Revoke',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.RevokeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class PolicyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """List [policies](/docs/backup/concepts/policy) of specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create a new policy.

        For detailed information, please see [Creating a backup policy](/docs/backup/operations/policy-vm/create).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get specific policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update specific policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete specific policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Apply(self, request, context):
        """Apply policy to [Compute Cloud instance](/docs/backup/concepts/vm-connection#os).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListApplications(self, request, context):
        """List applied policies using filters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Execute(self, request, context):
        """Run policy on specific Compute Cloud instance. That will create backup
        according selected policy. In order to perform this action, policy should be
        applied to the Compute Cloud instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Revoke(self, request, context):
        """Revoke policy from Compute Cloud instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListPoliciesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListPoliciesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.CreatePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.GetPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__pb2.Policy.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.UpdatePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.DeletePolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Apply': grpc.unary_unary_rpc_method_handler(
                    servicer.Apply,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ApplyPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListApplications': grpc.unary_unary_rpc_method_handler(
                    servicer.ListApplications,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListApplicationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListApplicationsResponse.SerializeToString,
            ),
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ExecuteRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Revoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Revoke,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.RevokeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.backup.v1.PolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PolicyService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/List',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListPoliciesRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListPoliciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Create',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.CreatePolicyRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Get',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.GetPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__pb2.Policy.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Update',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.UpdatePolicyRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Delete',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.DeletePolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Apply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Apply',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ApplyPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListApplications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/ListApplications',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListApplicationsRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ListApplicationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Execute',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.ExecuteRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Revoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.PolicyService/Revoke',
            yandex_dot_cloud_dot_backup_dot_v1_dot_policy__service__pb2.RevokeRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
