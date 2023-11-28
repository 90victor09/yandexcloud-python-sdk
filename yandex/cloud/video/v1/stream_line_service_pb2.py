# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/stream_line_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import stream_line_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_stream__line__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/video/v1/stream_line_service.proto\x12\x15yandex.cloud.video.v1\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\'yandex/cloud/video/v1/stream_line.proto\".\n\x14GetStreamLineRequest\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"u\n\x16ListStreamLinesRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x64 \x01(\x03\x12\x12\n\npage_token\x18\x65 \x01(\t\x12\x10\n\x08order_by\x18\x66 \x01(\t\x12\x0e\n\x06\x66ilter\x18g \x01(\t\"k\n\x17ListStreamLinesResponse\x12\x37\n\x0cstream_lines\x18\x01 \x03(\x0b\x32!.yandex.cloud.video.v1.StreamLine\x12\x17\n\x0fnext_page_token\x18\x64 \x01(\t\"\x9f\x04\n\x17\x43reateStreamLineRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x03 \x01(\t\x12;\n\trtmp_push\x18\xe8\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.RTMPPushParamsH\x00\x12\x39\n\x08srt_push\x18\xe9\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.SRTPushParamsH\x00\x12;\n\trtmp_pull\x18\xea\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.RTMPPullParamsH\x00\x12\x39\n\x08srt_pull\x18\xeb\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.SRTPullParamsH\x00\x12\x39\n\x08tcp_pull\x18\xec\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.TCPPullParamsH\x00\x12?\n\x0bmanual_line\x18\xd0\x0f \x01(\x0b\x32\'.yandex.cloud.video.v1.ManualLineParamsH\x01\x12;\n\tauto_line\x18\xd1\x0f \x01(\x0b\x32%.yandex.cloud.video.v1.AutoLineParamsH\x01\x42\x0e\n\x0cinput_paramsB\x12\n\x10line_type_params\"2\n\x18\x43reateStreamLineMetadata\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"\xfe\x03\n\x17UpdateStreamLineRequest\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\r\n\x05title\x18\x03 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x04 \x01(\t\x12;\n\trtmp_push\x18\xe8\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.RTMPPushParamsH\x00\x12\x39\n\x08srt_push\x18\xe9\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.SRTPushParamsH\x00\x12;\n\trtmp_pull\x18\xea\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.RTMPPullParamsH\x00\x12\x39\n\x08srt_pull\x18\xeb\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.SRTPullParamsH\x00\x12\x39\n\x08tcp_pull\x18\xec\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.TCPPullParamsH\x00\x12;\n\trtsp_pull\x18\xee\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.RTSPPullParamsH\x00\x42\x0e\n\x0cinput_params\"2\n\x18UpdateStreamLineMetadata\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"1\n\x17\x44\x65leteStreamLineRequest\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"2\n\x18\x44\x65leteStreamLineMetadata\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"\xb8\x01\n\x18PerformLineActionRequest\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\x12:\n\x08\x61\x63tivate\x18\xe8\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.ActivateActionH\x00\x12>\n\ndeactivate\x18\xe9\x07 \x01(\x0b\x32\'.yandex.cloud.video.v1.DeactivateActionH\x00\x42\x08\n\x06\x61\x63tion\"3\n\x19PerformLineActionMetadata\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"\x10\n\x0eRTMPPushParams\"\x0f\n\rSRTPushParams\"\x1d\n\x0eRTMPPullParams\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1c\n\rSRTPullParams\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1c\n\rTCPPullParams\x12\x0b\n\x03url\x18\x02 \x01(\t\"\x1d\n\x0eRTSPPullParams\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x12\n\x10ManualLineParams\"\x10\n\x0e\x41utoLineParams\"\x10\n\x0e\x41\x63tivateAction\"\x12\n\x10\x44\x65\x61\x63tivateAction\"-\n\x13GetStreamKeyRequest\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"0\n\x16UpdateStreamKeyRequest\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t\"1\n\x17UpdateStreamKeyMetadata\x12\x16\n\x0estream_line_id\x18\x01 \x01(\t2\x89\x08\n\x11StreamLineService\x12W\n\x03Get\x12+.yandex.cloud.video.v1.GetStreamLineRequest\x1a!.yandex.cloud.video.v1.StreamLine\"\x00\x12g\n\x04List\x12-.yandex.cloud.video.v1.ListStreamLinesRequest\x1a..yandex.cloud.video.v1.ListStreamLinesResponse\"\x00\x12\x87\x01\n\x06\x43reate\x12..yandex.cloud.video.v1.CreateStreamLineRequest\x1a!.yandex.cloud.operation.Operation\"*\xb2\xd2*&\n\x18\x43reateStreamLineMetadata\x12\nStreamLine\x12\x87\x01\n\x06Update\x12..yandex.cloud.video.v1.UpdateStreamLineRequest\x1a!.yandex.cloud.operation.Operation\"*\xb2\xd2*&\n\x18UpdateStreamLineMetadata\x12\nStreamLine\x12\x92\x01\n\x06\x44\x65lete\x12..yandex.cloud.video.v1.DeleteStreamLineRequest\x1a!.yandex.cloud.operation.Operation\"5\xb2\xd2*1\n\x18\x44\x65leteStreamLineMetadata\x12\x15google.protobuf.Empty\x12\x90\x01\n\rPerformAction\x12/.yandex.cloud.video.v1.PerformLineActionRequest\x1a!.yandex.cloud.operation.Operation\"+\xb2\xd2*\'\n\x19PerformLineActionMetadata\x12\nStreamLine\x12\x62\n\x0cGetStreamKey\x12*.yandex.cloud.video.v1.GetStreamKeyRequest\x1a$.yandex.cloud.video.v1.PushStreamKey\"\x00\x12\x91\x01\n\x0fUpdateStreamKey\x12-.yandex.cloud.video.v1.UpdateStreamKeyRequest\x1a!.yandex.cloud.operation.Operation\",\xb2\xd2*(\n\x17UpdateStreamKeyMetadata\x12\rPushStreamKeyB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.stream_line_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _STREAMLINESERVICE.methods_by_name['Create']._options = None
  _STREAMLINESERVICE.methods_by_name['Create']._serialized_options = b'\262\322*&\n\030CreateStreamLineMetadata\022\nStreamLine'
  _STREAMLINESERVICE.methods_by_name['Update']._options = None
  _STREAMLINESERVICE.methods_by_name['Update']._serialized_options = b'\262\322*&\n\030UpdateStreamLineMetadata\022\nStreamLine'
  _STREAMLINESERVICE.methods_by_name['Delete']._options = None
  _STREAMLINESERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteStreamLineMetadata\022\025google.protobuf.Empty'
  _STREAMLINESERVICE.methods_by_name['PerformAction']._options = None
  _STREAMLINESERVICE.methods_by_name['PerformAction']._serialized_options = b'\262\322*\'\n\031PerformLineActionMetadata\022\nStreamLine'
  _STREAMLINESERVICE.methods_by_name['UpdateStreamKey']._options = None
  _STREAMLINESERVICE.methods_by_name['UpdateStreamKey']._serialized_options = b'\262\322*(\n\027UpdateStreamKeyMetadata\022\rPushStreamKey'
  _globals['_GETSTREAMLINEREQUEST']._serialized_start=223
  _globals['_GETSTREAMLINEREQUEST']._serialized_end=269
  _globals['_LISTSTREAMLINESREQUEST']._serialized_start=271
  _globals['_LISTSTREAMLINESREQUEST']._serialized_end=388
  _globals['_LISTSTREAMLINESRESPONSE']._serialized_start=390
  _globals['_LISTSTREAMLINESRESPONSE']._serialized_end=497
  _globals['_CREATESTREAMLINEREQUEST']._serialized_start=500
  _globals['_CREATESTREAMLINEREQUEST']._serialized_end=1043
  _globals['_CREATESTREAMLINEMETADATA']._serialized_start=1045
  _globals['_CREATESTREAMLINEMETADATA']._serialized_end=1095
  _globals['_UPDATESTREAMLINEREQUEST']._serialized_start=1098
  _globals['_UPDATESTREAMLINEREQUEST']._serialized_end=1608
  _globals['_UPDATESTREAMLINEMETADATA']._serialized_start=1610
  _globals['_UPDATESTREAMLINEMETADATA']._serialized_end=1660
  _globals['_DELETESTREAMLINEREQUEST']._serialized_start=1662
  _globals['_DELETESTREAMLINEREQUEST']._serialized_end=1711
  _globals['_DELETESTREAMLINEMETADATA']._serialized_start=1713
  _globals['_DELETESTREAMLINEMETADATA']._serialized_end=1763
  _globals['_PERFORMLINEACTIONREQUEST']._serialized_start=1766
  _globals['_PERFORMLINEACTIONREQUEST']._serialized_end=1950
  _globals['_PERFORMLINEACTIONMETADATA']._serialized_start=1952
  _globals['_PERFORMLINEACTIONMETADATA']._serialized_end=2003
  _globals['_RTMPPUSHPARAMS']._serialized_start=2005
  _globals['_RTMPPUSHPARAMS']._serialized_end=2021
  _globals['_SRTPUSHPARAMS']._serialized_start=2023
  _globals['_SRTPUSHPARAMS']._serialized_end=2038
  _globals['_RTMPPULLPARAMS']._serialized_start=2040
  _globals['_RTMPPULLPARAMS']._serialized_end=2069
  _globals['_SRTPULLPARAMS']._serialized_start=2071
  _globals['_SRTPULLPARAMS']._serialized_end=2099
  _globals['_TCPPULLPARAMS']._serialized_start=2101
  _globals['_TCPPULLPARAMS']._serialized_end=2129
  _globals['_RTSPPULLPARAMS']._serialized_start=2131
  _globals['_RTSPPULLPARAMS']._serialized_end=2160
  _globals['_MANUALLINEPARAMS']._serialized_start=2162
  _globals['_MANUALLINEPARAMS']._serialized_end=2180
  _globals['_AUTOLINEPARAMS']._serialized_start=2182
  _globals['_AUTOLINEPARAMS']._serialized_end=2198
  _globals['_ACTIVATEACTION']._serialized_start=2200
  _globals['_ACTIVATEACTION']._serialized_end=2216
  _globals['_DEACTIVATEACTION']._serialized_start=2218
  _globals['_DEACTIVATEACTION']._serialized_end=2236
  _globals['_GETSTREAMKEYREQUEST']._serialized_start=2238
  _globals['_GETSTREAMKEYREQUEST']._serialized_end=2283
  _globals['_UPDATESTREAMKEYREQUEST']._serialized_start=2285
  _globals['_UPDATESTREAMKEYREQUEST']._serialized_end=2333
  _globals['_UPDATESTREAMKEYMETADATA']._serialized_start=2335
  _globals['_UPDATESTREAMKEYMETADATA']._serialized_end=2384
  _globals['_STREAMLINESERVICE']._serialized_start=2387
  _globals['_STREAMLINESERVICE']._serialized_end=3420
# @@protoc_insertion_point(module_scope)
