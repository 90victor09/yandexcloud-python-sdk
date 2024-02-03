# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/transfer_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.datatransfer.v1 import transfer_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_transfer__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/datatransfer/v1/transfer_service.proto\x12\x1cyandex.cloud.datatransfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a+yandex/cloud/datatransfer/v1/transfer.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\"\xb1\x03\n\x15\x43reateTransferRequest\x12\x11\n\tsource_id\x18\x01 \x01(\t\x12\x11\n\ttarget_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tfolder_id\x18\x04 \x01(\t\x12\x36\n\x07runtime\x18\x05 \x01(\x0b\x32%.yandex.cloud.datatransfer.v1.Runtime\x12\x38\n\x04type\x18\x06 \x01(\x0e\x32*.yandex.cloud.datatransfer.v1.TransferType\x12\x0c\n\x04name\x18\x07 \x01(\t\x12O\n\x06labels\x18\x08 \x03(\x0b\x32?.yandex.cloud.datatransfer.v1.CreateTransferRequest.LabelsEntry\x12\x44\n\x0etransformation\x18\n \x01(\x0b\x32,.yandex.cloud.datatransfer.v1.Transformation\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\t\x10\n\"-\n\x16\x43reateTransferMetadata\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\"\x84\x03\n\x15UpdateTransferRequest\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x36\n\x07runtime\x18\x03 \x01(\x0b\x32%.yandex.cloud.datatransfer.v1.Runtime\x12\x0c\n\x04name\x18\x04 \x01(\t\x12/\n\x0bupdate_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12O\n\x06labels\x18\x06 \x03(\x0b\x32?.yandex.cloud.datatransfer.v1.UpdateTransferRequest.LabelsEntry\x12\x44\n\x0etransformation\x18\x08 \x01(\x0b\x32,.yandex.cloud.datatransfer.v1.Transformation\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x07\x10\x08\"-\n\x16UpdateTransferMetadata\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\",\n\x15\x44\x65leteTransferRequest\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\"-\n\x16\x44\x65leteTransferMetadata\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\"V\n\x14ListTransfersRequest\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\tJ\x04\x08\x01\x10\x02\"k\n\x15ListTransfersResponse\x12\x39\n\ttransfers\x18\x01 \x03(\x0b\x32&.yandex.cloud.datatransfer.v1.Transfer\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\")\n\x12GetTransferRequest\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\"0\n\x19\x44\x65\x61\x63tivateTransferRequest\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\"1\n\x1a\x44\x65\x61\x63tivateTransferMetadata\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\".\n\x17\x41\x63tivateTransferRequest\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t\"/\n\x18\x41\x63tivateTransferMetadata\x12\x13\n\x0btransfer_id\x18\x01 \x01(\t2\xdd\t\n\x0fTransferService\x12\x9f\x01\n\x06\x43reate\x12\x33.yandex.cloud.datatransfer.v1.CreateTransferRequest\x1a!.yandex.cloud.operation.Operation\"=\xb2\xd2*\"\n\x16\x43reateTransferMetadata\x12\x08Transfer\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/transfer:\x01*\x12\xad\x01\n\x06Update\x12\x33.yandex.cloud.datatransfer.v1.UpdateTransferRequest\x1a!.yandex.cloud.operation.Operation\"K\xb2\xd2*\"\n\x16UpdateTransferMetadata\x12\x08Transfer\x82\xd3\xe4\x93\x02\x1f\x32\x1a/v1/transfer/{transfer_id}:\x01*\x12\xb7\x01\n\x06\x44\x65lete\x12\x33.yandex.cloud.datatransfer.v1.DeleteTransferRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*/\n\x16\x44\x65leteTransferMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/transfer/{transfer_id}\x12\x97\x01\n\x04List\x12\x32.yandex.cloud.datatransfer.v1.ListTransfersRequest\x1a\x33.yandex.cloud.datatransfer.v1.ListTransfersResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/transfers/list/{folder_id}\x12\x83\x01\n\x03Get\x12\x30.yandex.cloud.datatransfer.v1.GetTransferRequest\x1a&.yandex.cloud.datatransfer.v1.Transfer\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/transfer/{transfer_id}\x12\xd1\x01\n\nDeactivate\x12\x37.yandex.cloud.datatransfer.v1.DeactivateTransferRequest\x1a!.yandex.cloud.operation.Operation\"g\xb2\xd2*3\n\x1a\x44\x65\x61\x63tivateTransferMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02*\"%/v1/transfer/{transfer_id}:deactivate:\x01*\x12\xc9\x01\n\x08\x41\x63tivate\x12\x35.yandex.cloud.datatransfer.v1.ActivateTransferRequest\x1a!.yandex.cloud.operation.Operation\"c\xb2\xd2*1\n\x18\x41\x63tivateTransferMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02(\"#/v1/transfer/{transfer_id}:activate:\x01*Bq\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransferb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.transfer_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransfer'
  _CREATETRANSFERREQUEST_LABELSENTRY._options = None
  _CREATETRANSFERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATETRANSFERREQUEST_LABELSENTRY._options = None
  _UPDATETRANSFERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _TRANSFERSERVICE.methods_by_name['Create']._options = None
  _TRANSFERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\"\n\026CreateTransferMetadata\022\010Transfer\202\323\344\223\002\021\"\014/v1/transfer:\001*'
  _TRANSFERSERVICE.methods_by_name['Update']._options = None
  _TRANSFERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\"\n\026UpdateTransferMetadata\022\010Transfer\202\323\344\223\002\0372\032/v1/transfer/{transfer_id}:\001*'
  _TRANSFERSERVICE.methods_by_name['Delete']._options = None
  _TRANSFERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*/\n\026DeleteTransferMetadata\022\025google.protobuf.Empty\202\323\344\223\002\034*\032/v1/transfer/{transfer_id}'
  _TRANSFERSERVICE.methods_by_name['List']._options = None
  _TRANSFERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002 \022\036/v1/transfers/list/{folder_id}'
  _TRANSFERSERVICE.methods_by_name['Get']._options = None
  _TRANSFERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\034\022\032/v1/transfer/{transfer_id}'
  _TRANSFERSERVICE.methods_by_name['Deactivate']._options = None
  _TRANSFERSERVICE.methods_by_name['Deactivate']._serialized_options = b'\262\322*3\n\032DeactivateTransferMetadata\022\025google.protobuf.Empty\202\323\344\223\002*\"%/v1/transfer/{transfer_id}:deactivate:\001*'
  _TRANSFERSERVICE.methods_by_name['Activate']._options = None
  _TRANSFERSERVICE.methods_by_name['Activate']._serialized_options = b'\262\322*1\n\030ActivateTransferMetadata\022\025google.protobuf.Empty\202\323\344\223\002(\"#/v1/transfer/{transfer_id}:activate:\001*'
  _globals['_CREATETRANSFERREQUEST']._serialized_start=269
  _globals['_CREATETRANSFERREQUEST']._serialized_end=702
  _globals['_CREATETRANSFERREQUEST_LABELSENTRY']._serialized_start=651
  _globals['_CREATETRANSFERREQUEST_LABELSENTRY']._serialized_end=696
  _globals['_CREATETRANSFERMETADATA']._serialized_start=704
  _globals['_CREATETRANSFERMETADATA']._serialized_end=749
  _globals['_UPDATETRANSFERREQUEST']._serialized_start=752
  _globals['_UPDATETRANSFERREQUEST']._serialized_end=1140
  _globals['_UPDATETRANSFERREQUEST_LABELSENTRY']._serialized_start=651
  _globals['_UPDATETRANSFERREQUEST_LABELSENTRY']._serialized_end=696
  _globals['_UPDATETRANSFERMETADATA']._serialized_start=1142
  _globals['_UPDATETRANSFERMETADATA']._serialized_end=1187
  _globals['_DELETETRANSFERREQUEST']._serialized_start=1189
  _globals['_DELETETRANSFERREQUEST']._serialized_end=1233
  _globals['_DELETETRANSFERMETADATA']._serialized_start=1235
  _globals['_DELETETRANSFERMETADATA']._serialized_end=1280
  _globals['_LISTTRANSFERSREQUEST']._serialized_start=1282
  _globals['_LISTTRANSFERSREQUEST']._serialized_end=1368
  _globals['_LISTTRANSFERSRESPONSE']._serialized_start=1370
  _globals['_LISTTRANSFERSRESPONSE']._serialized_end=1477
  _globals['_GETTRANSFERREQUEST']._serialized_start=1479
  _globals['_GETTRANSFERREQUEST']._serialized_end=1520
  _globals['_DEACTIVATETRANSFERREQUEST']._serialized_start=1522
  _globals['_DEACTIVATETRANSFERREQUEST']._serialized_end=1570
  _globals['_DEACTIVATETRANSFERMETADATA']._serialized_start=1572
  _globals['_DEACTIVATETRANSFERMETADATA']._serialized_end=1621
  _globals['_ACTIVATETRANSFERREQUEST']._serialized_start=1623
  _globals['_ACTIVATETRANSFERREQUEST']._serialized_end=1669
  _globals['_ACTIVATETRANSFERMETADATA']._serialized_start=1671
  _globals['_ACTIVATETRANSFERMETADATA']._serialized_end=1718
  _globals['_TRANSFERSERVICE']._serialized_start=1721
  _globals['_TRANSFERSERVICE']._serialized_end=2966
# @@protoc_insertion_point(module_scope)
