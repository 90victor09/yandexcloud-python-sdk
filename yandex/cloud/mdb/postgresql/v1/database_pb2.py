# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/postgresql/v1/database.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/mdb/postgresql/v1/database.proto\x12\x1eyandex.cloud.mdb.postgresql.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xee\x01\n\x08\x44\x61tabase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x12\n\nlc_collate\x18\x04 \x01(\t\x12\x10\n\x08lc_ctype\x18\x05 \x01(\t\x12=\n\nextensions\x18\x06 \x03(\x0b\x32).yandex.cloud.mdb.postgresql.v1.Extension\x12\x13\n\x0btemplate_db\x18\x07 \x01(\t\x12\x37\n\x13\x64\x65letion_protection\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"*\n\tExtension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xeb\x02\n\x0c\x44\x61tabaseSpec\x12,\n\x04name\x18\x01 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12,\n\x05owner\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12+\n\nlc_collate\x18\x03 \x01(\tB\x17\xf2\xc7\x31\x13|[a-zA-Z_]+.UTF-8|C\x12)\n\x08lc_ctype\x18\x04 \x01(\tB\x17\xf2\xc7\x31\x13|[a-zA-Z_]+.UTF-8|C\x12=\n\nextensions\x18\x05 \x03(\x0b\x32).yandex.cloud.mdb.postgresql.v1.Extension\x12/\n\x0btemplate_db\x18\x06 \x01(\tB\x1a\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x37\n\x13\x64\x65letion_protection\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValueBs\n\"yandex.cloud.api.mdb.postgresql.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.postgresql.v1.database_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"yandex.cloud.api.mdb.postgresql.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresql'
  _DATABASESPEC.fields_by_name['name']._options = None
  _DATABASESPEC.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _DATABASESPEC.fields_by_name['owner']._options = None
  _DATABASESPEC.fields_by_name['owner']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _DATABASESPEC.fields_by_name['lc_collate']._options = None
  _DATABASESPEC.fields_by_name['lc_collate']._serialized_options = b'\362\3071\023|[a-zA-Z_]+.UTF-8|C'
  _DATABASESPEC.fields_by_name['lc_ctype']._options = None
  _DATABASESPEC.fields_by_name['lc_ctype']._serialized_options = b'\362\3071\023|[a-zA-Z_]+.UTF-8|C'
  _DATABASESPEC.fields_by_name['template_db']._options = None
  _DATABASESPEC.fields_by_name['template_db']._serialized_options = b'\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_DATABASE']._serialized_start=145
  _globals['_DATABASE']._serialized_end=383
  _globals['_EXTENSION']._serialized_start=385
  _globals['_EXTENSION']._serialized_end=427
  _globals['_DATABASESPEC']._serialized_start=430
  _globals['_DATABASESPEC']._serialized_end=793
# @@protoc_insertion_point(module_scope)
