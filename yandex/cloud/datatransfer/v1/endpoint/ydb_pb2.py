# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/ydb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/datatransfer/v1/endpoint/ydb.proto\x12%yandex.cloud.datatransfer.v1.endpoint\"\xd0\x01\n\tYdbSource\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\r\n\x05paths\x18\x05 \x03(\t\x12\x1a\n\x12service_account_id\x18\x06 \x01(\t\x12\x11\n\tsubnet_id\x18\x1e \x01(\t\x12\x16\n\x0esa_key_content\x18! \x01(\t\x12\x17\n\x0fsecurity_groups\x18\" \x03(\t\x12\x1e\n\x16\x63hangefeed_custom_name\x18# \x01(\tJ\x04\x08\x03\x10\x05J\x04\x08\x07\x10\x1eJ\x04\x08\x1f\x10!\"\x83\x03\n\tYdbTarget\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\n \x01(\t\x12\x1a\n\x12service_account_id\x18\x0b \x01(\t\x12O\n\x0e\x63leanup_policy\x18\x15 \x01(\x0e\x32\x37.yandex.cloud.datatransfer.v1.endpoint.YdbCleanupPolicy\x12\x11\n\tsubnet_id\x18\x1e \x01(\t\x12\x16\n\x0esa_key_content\x18  \x01(\t\x12\x17\n\x0fsecurity_groups\x18! \x03(\t\x12 \n\x18is_table_column_oriented\x18\" \x01(\x08\x12Y\n\x13\x64\x65\x66\x61ult_compression\x18# \x01(\x0e\x32<.yandex.cloud.datatransfer.v1.endpoint.YdbDefaultCompressionJ\x04\x08\x03\x10\nJ\x04\x08\x0c\x10\x15J\x04\x08\x16\x10\x1eJ\x04\x08\x1f\x10 *t\n\x10YdbCleanupPolicy\x12\"\n\x1eYDB_CLEANUP_POLICY_UNSPECIFIED\x10\x00\x12\x1f\n\x1bYDB_CLEANUP_POLICY_DISABLED\x10\x01\x12\x1b\n\x17YDB_CLEANUP_POLICY_DROP\x10\x02*\x87\x01\n\x15YdbDefaultCompression\x12\'\n#YDB_DEFAULT_COMPRESSION_UNSPECIFIED\x10\x00\x12$\n YDB_DEFAULT_COMPRESSION_DISABLED\x10\x01\x12\x1f\n\x1bYDB_DEFAULT_COMPRESSION_LZ4\x10\x02\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.ydb_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_YDBCLEANUPPOLICY']._serialized_start=691
  _globals['_YDBCLEANUPPOLICY']._serialized_end=807
  _globals['_YDBDEFAULTCOMPRESSION']._serialized_start=810
  _globals['_YDBDEFAULTCOMPRESSION']._serialized_end=945
  _globals['_YDBSOURCE']._serialized_start=91
  _globals['_YDBSOURCE']._serialized_end=299
  _globals['_YDBTARGET']._serialized_start=302
  _globals['_YDBTARGET']._serialized_end=689
# @@protoc_insertion_point(module_scope)
