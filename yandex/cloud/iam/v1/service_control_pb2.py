# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/service_control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.iam.v1 import resource_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/iam/v1/service_control.proto\x12\x13yandex.cloud.iam.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"yandex/cloud/iam/v1/resource.proto\"\xc0\x02\n\x07Service\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.Resource\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x06status\x18\x04 \x01(\x0e\x32#.yandex.cloud.iam.v1.Service.Status\"\x8a\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03\x12\x0c\n\x08\x45NABLING\x10\x04\x12\x0c\n\x08RESUMING\x10\x05\x12\x0b\n\x07PAUSING\x10\x06\x12\r\n\tDISABLING\x10\x07\x12\t\n\x05\x45RROR\x10\x08\x42V\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.service_control_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _globals['_SERVICE']._serialized_start=136
  _globals['_SERVICE']._serialized_end=456
  _globals['_SERVICE_STATUS']._serialized_start=318
  _globals['_SERVICE_STATUS']._serialized_end=456
# @@protoc_insertion_point(module_scope)