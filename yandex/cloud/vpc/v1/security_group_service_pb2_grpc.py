# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.vpc.v1 import security_group_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2
from yandex.cloud.vpc.v1 import security_group_service_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2


class SecurityGroupServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/Get',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.GetSecurityGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2.SecurityGroup.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/List',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/Create',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.CreateSecurityGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/Update',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.UpdateRules = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/UpdateRules',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRulesRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.UpdateRule = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/UpdateRule',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRuleRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/Delete',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.DeleteSecurityGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Move = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/Move',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.MoveSecurityGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SecurityGroupService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsResponse.FromString,
        )


class SecurityGroupServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRules(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRule(self, request, context):
    """update rule description or labels
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SecurityGroupServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.GetSecurityGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2.SecurityGroup.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.CreateSecurityGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'UpdateRules': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRules,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRulesRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'UpdateRule': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRule,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRuleRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.DeleteSecurityGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.MoveSecurityGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.vpc.v1.SecurityGroupService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
