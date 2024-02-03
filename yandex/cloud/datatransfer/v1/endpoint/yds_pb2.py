# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/yds.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import parsers_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_parsers__pb2
from yandex.cloud.datatransfer.v1.endpoint import serializers_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_serializers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/datatransfer/v1/endpoint/yds.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x33yandex/cloud/datatransfer/v1/endpoint/parsers.proto\x1a\x37yandex/cloud/datatransfer/v1/endpoint/serializers.proto\"\xe0\x02\n\tYDSSource\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x08 \x01(\t\x12T\n\x10supported_codecs\x18\t \x03(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.YdsCompressionCodec\x12=\n\x06parser\x18\n \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Parser\x12\x18\n\x10\x61llow_ttl_rewind\x18\x0b \x01(\x08\x12\x10\n\x08\x65ndpoint\x18\x14 \x01(\t\x12\x11\n\tsubnet_id\x18\x1e \x01(\t\x12\x17\n\x0fsecurity_groups\x18\" \x03(\t\x12\x10\n\x08\x63onsumer\x18# \x01(\tJ\x04\x08\x03\x10\x08J\x04\x08\x0c\x10\x14J\x04\x08\x15\x10\x1eJ\x04\x08\x1f\x10\"\"\xfd\x01\n\tYDSTarget\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\x12\x15\n\rsave_tx_order\x18\x04 \x01(\x08\x12\x45\n\nserializer\x18\x08 \x01(\x0b\x32\x31.yandex.cloud.datatransfer.v1.endpoint.Serializer\x12\x10\n\x08\x65ndpoint\x18\x14 \x01(\t\x12\x11\n\tsubnet_id\x18\x1e \x01(\t\x12\x17\n\x0fsecurity_groups\x18\" \x03(\tJ\x04\x08\x05\x10\x08J\x04\x08\t\x10\x14J\x04\x08\x15\x10\x1eJ\x04\x08\x1f\x10\"*\x9b\x01\n\x13YdsCompressionCodec\x12%\n!YDS_COMPRESSION_CODEC_UNSPECIFIED\x10\x00\x12\x1d\n\x19YDS_COMPRESSION_CODEC_RAW\x10\x01\x12\x1e\n\x1aYDS_COMPRESSION_CODEC_GZIP\x10\x02\x12\x1e\n\x1aYDS_COMPRESSION_CODEC_ZSTD\x10\x04\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.yds_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_YDSCOMPRESSIONCODEC']._serialized_start=812
  _globals['_YDSCOMPRESSIONCODEC']._serialized_end=967
  _globals['_YDSSOURCE']._serialized_start=201
  _globals['_YDSSOURCE']._serialized_end=553
  _globals['_YDSTARGET']._serialized_start=556
  _globals['_YDSTARGET']._serialized_end=809
# @@protoc_insertion_point(module_scope)
