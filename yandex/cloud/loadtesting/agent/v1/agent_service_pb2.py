# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/agent/v1/agent_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/loadtesting/agent/v1/agent_service.proto\x12!yandex.cloud.loadtesting.agent.v1\x1a\x1cgoogle/api/annotations.proto\"\x96\x02\n\x17\x43laimAgentStatusRequest\x12\x19\n\x11\x61gent_instance_id\x18\x01 \x01(\t\x12Q\n\x06status\x18\x02 \x01(\x0e\x32\x41.yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest.Status\"\x8c\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eREADY_FOR_TEST\x10\x01\x12\x12\n\x0ePREPARING_TEST\x10\x02\x12\x0b\n\x07TESTING\x10\x03\x12\x0f\n\x0bTANK_FAILED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x17\n\x13UPLOADING_ARTIFACTS\x10\x06\"(\n\x18\x43laimAgentStatusResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x32\xe0\x01\n\x0c\x41gentService\x12\xcf\x01\n\x0b\x43laimStatus\x12:.yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest\x1a;.yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusResponse\"G\x82\xd3\xe4\x93\x02\x41\"</loadtesting/agent/v1/agents/{agent_instance_id}/claimStatus:\x01*Bt\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.agent.v1.agent_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agent'
  _AGENTSERVICE.methods_by_name['ClaimStatus']._options = None
  _AGENTSERVICE.methods_by_name['ClaimStatus']._serialized_options = b'\202\323\344\223\002A\"</loadtesting/agent/v1/agents/{agent_instance_id}/claimStatus:\001*'
  _globals['_CLAIMAGENTSTATUSREQUEST']._serialized_start=123
  _globals['_CLAIMAGENTSTATUSREQUEST']._serialized_end=401
  _globals['_CLAIMAGENTSTATUSREQUEST_STATUS']._serialized_start=261
  _globals['_CLAIMAGENTSTATUSREQUEST_STATUS']._serialized_end=401
  _globals['_CLAIMAGENTSTATUSRESPONSE']._serialized_start=403
  _globals['_CLAIMAGENTSTATUSRESPONSE']._serialized_end=443
  _globals['_AGENTSERVICE']._serialized_start=446
  _globals['_AGENTSERVICE']._serialized_end=670
# @@protoc_insertion_point(module_scope)
