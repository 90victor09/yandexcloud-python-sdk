# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/app_token_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/datasphere/v1/app_token_service.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"(\n\x17\x41ppTokenValidateRequest\x12\r\n\x05token\x18\x01 \x01(\t2\x9e\x01\n\x0f\x41ppTokenService\x12\x8a\x01\n\x08Validate\x12\x33.yandex.cloud.datasphere.v1.AppTokenValidateRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+\")/datasphere/v1/appTokens/{token}:validateBk\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v1.app_token_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere'
  _APPTOKENSERVICE.methods_by_name['Validate']._options = None
  _APPTOKENSERVICE.methods_by_name['Validate']._serialized_options = b'\202\323\344\223\002+\")/datasphere/v1/appTokens/{token}:validate'
  _globals['_APPTOKENVALIDATEREQUEST']._serialized_start=141
  _globals['_APPTOKENVALIDATEREQUEST']._serialized_end=181
  _globals['_APPTOKENSERVICE']._serialized_start=184
  _globals['_APPTOKENSERVICE']._serialized_end=342
# @@protoc_insertion_point(module_scope)
