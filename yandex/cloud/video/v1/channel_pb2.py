# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/channel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/video/v1/channel.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb2\x01\n\x07\x43hannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.channel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _globals['_CHANNEL']._serialized_start=96
  _globals['_CHANNEL']._serialized_end=274
# @@protoc_insertion_point(module_scope)