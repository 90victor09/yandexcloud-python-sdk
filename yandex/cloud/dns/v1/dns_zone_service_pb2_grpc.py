# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.dns.v1 import dns_zone_pb2 as yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2
from yandex.cloud.dns.v1 import dns_zone_service_pb2 as yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class DnsZoneServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/Get',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.GetDnsZoneRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2.DnsZone.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/List',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZonesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZonesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/Create',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.CreateDnsZoneRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/Update',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpdateDnsZoneRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/Delete',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.DeleteDnsZoneRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetRecordSet = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/GetRecordSet',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.GetDnsZoneRecordSetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2.RecordSet.FromString,
                )
        self.ListRecordSets = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/ListRecordSets',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneRecordSetsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneRecordSetsResponse.FromString,
                )
        self.UpdateRecordSets = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/UpdateRecordSets',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpdateRecordSetsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpsertRecordSets = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/UpsertRecordSets',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpsertRecordSetsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneOperationsResponse.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.dns.v1.DnsZoneService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class DnsZoneServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecordSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRecordSets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRecordSets(self, request, context):
        """Method with strict control for changing zone state. Returns error when deleted record is not found, found record
        with matched type and name but different ttl or value, or on attempt to add record with existing name and type.
        Deletions come first so if record with same name and type is present in both lists then existing record will be
        deleted and new one added.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpsertRecordSets(self, request, context):
        """Method without strict control for changing zone state. Do not returns error when deleted record is not found.
        Delete records that match all specified fields which allows to delete only specified records from record set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DnsZoneServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.GetDnsZoneRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2.DnsZone.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZonesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZonesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.CreateDnsZoneRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpdateDnsZoneRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.DeleteDnsZoneRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetRecordSet': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecordSet,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.GetDnsZoneRecordSetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2.RecordSet.SerializeToString,
            ),
            'ListRecordSets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRecordSets,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneRecordSetsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneRecordSetsResponse.SerializeToString,
            ),
            'UpdateRecordSets': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRecordSets,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpdateRecordSetsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpsertRecordSets': grpc.unary_unary_rpc_method_handler(
                    servicer.UpsertRecordSets,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpsertRecordSetsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneOperationsResponse.SerializeToString,
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
            'yandex.cloud.dns.v1.DnsZoneService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DnsZoneService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/Get',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.GetDnsZoneRequest.SerializeToString,
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2.DnsZone.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/List',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZonesRequest.SerializeToString,
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZonesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/Create',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.CreateDnsZoneRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/Update',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpdateDnsZoneRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/Delete',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.DeleteDnsZoneRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecordSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/GetRecordSet',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.GetDnsZoneRecordSetRequest.SerializeToString,
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2.RecordSet.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRecordSets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/ListRecordSets',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneRecordSetsRequest.SerializeToString,
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneRecordSetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRecordSets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/UpdateRecordSets',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpdateRecordSetsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpsertRecordSets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/UpsertRecordSets',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.UpsertRecordSetsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/ListOperations',
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__service__pb2.ListDnsZoneOperationsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/ListAccessBindings',
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/SetAccessBindings',
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.dns.v1.DnsZoneService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
