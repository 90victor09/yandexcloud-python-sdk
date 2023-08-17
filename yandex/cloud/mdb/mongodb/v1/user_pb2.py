# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/mdb/mongodb/v1/user.proto\x12\x1byandex.cloud.mdb.mongodb.v1\x1a\x1dyandex/cloud/validation.proto\"f\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12<\n\x0bpermissions\x18\x03 \x03(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Permission\"2\n\nPermission\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12\r\n\x05roles\x18\x02 \x03(\t\"\x96\x01\n\x08UserSpec\x12+\n\x04name\x18\x01 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12<\n\x0bpermissions\x18\x03 \x03(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.PermissionBj\n\x1fyandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037yandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodb'
  _USERSPEC.fields_by_name['name']._options = None
  _USERSPEC.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _USERSPEC.fields_by_name['password']._options = None
  _USERSPEC.fields_by_name['password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _globals['_USER']._serialized_start=102
  _globals['_USER']._serialized_end=204
  _globals['_PERMISSION']._serialized_start=206
  _globals['_PERMISSION']._serialized_end=256
  _globals['_USERSPEC']._serialized_start=259
  _globals['_USERSPEC']._serialized_end=409
# @@protoc_insertion_point(module_scope)
