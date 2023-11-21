# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/video.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!yandex/cloud/video/v1/video.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8f\x04\n\x05Video\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x05 \x01(\t\x12\x38\n\x06status\x18\x06 \x01(\x0e\x32(.yandex.cloud.video.v1.Video.VideoStatus\x12\x37\n\x04tusd\x18\xe8\x07 \x01(\x0b\x32&.yandex.cloud.video.v1.VideoTUSDSourceH\x00\x12H\n\rpublic_access\x18\xd0\x0f \x01(\x0b\x32..yandex.cloud.video.v1.VideoPublicAccessRightsH\x01\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"t\n\x0bVideoStatus\x12\x1c\n\x18VIDEO_STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eWAIT_UPLOADING\x10\x01\x12\x0e\n\nPROCESSING\x10\x04\x12\t\n\x05READY\x10\x05\x12\r\n\tPUBLISHED\x10\x06\x12\t\n\x05\x45RROR\x10\x07\x42\x08\n\x06sourceB\x0f\n\raccess_rights\"\x1e\n\x0fVideoTUSDSource\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x19\n\x17VideoPublicAccessRightsB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.video_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _globals['_VIDEO']._serialized_start=94
  _globals['_VIDEO']._serialized_end=621
  _globals['_VIDEO_VIDEOSTATUS']._serialized_start=478
  _globals['_VIDEO_VIDEOSTATUS']._serialized_end=594
  _globals['_VIDEOTUSDSOURCE']._serialized_start=623
  _globals['_VIDEOTUSDSOURCE']._serialized_end=653
  _globals['_VIDEOPUBLICACCESSRIGHTS']._serialized_start=655
  _globals['_VIDEOPUBLICACCESSRIGHTS']._serialized_end=680
# @@protoc_insertion_point(module_scope)
