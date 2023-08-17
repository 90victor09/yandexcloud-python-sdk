# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/kms/v1/symmetric_key_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.kms.v1 import symmetric_key_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/kms/v1/symmetric_key_service.proto\x12\x13yandex.cloud.kms.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\'yandex/cloud/kms/v1/symmetric_key.proto\"\xc4\x03\n\x19\x43reateSymmetricKeyRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x17\n\x04name\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\x87\x01\n\x06labels\x18\x04 \x03(\x0b\x32:.yandex.cloud.kms.v1.CreateSymmetricKeyRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x42\n\x11\x64\x65\x66\x61ult_algorithm\x18\x05 \x01(\x0e\x32\'.yandex.cloud.kms.v1.SymmetricAlgorithm\x12\x32\n\x0frotation_period\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1b\n\x13\x64\x65letion_protection\x18\x07 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x1a\x43reateSymmetricKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x1a\n\x12primary_version_id\x18\x02 \x01(\t\"6\n\x16GetSymmetricKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"y\n\x18ListSymmetricKeysRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"e\n\x19ListSymmetricKeysResponse\x12/\n\x04keys\x18\x01 \x03(\x0b\x32!.yandex.cloud.kms.v1.SymmetricKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"}\n\x1fListSymmetricKeyVersionsRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"{\n ListSymmetricKeyVersionsResponse\x12>\n\x0ckey_versions\x18\x01 \x03(\x0b\x32(.yandex.cloud.kms.v1.SymmetricKeyVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb2\x04\n\x19UpdateSymmetricKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x17\n\x04name\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1f\n\x0b\x64\x65scription\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\x38\n\x06status\x18\x05 \x01(\x0e\x32(.yandex.cloud.kms.v1.SymmetricKey.Status\x12\x87\x01\n\x06labels\x18\x06 \x03(\x0b\x32:.yandex.cloud.kms.v1.UpdateSymmetricKeyRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x42\n\x11\x64\x65\x66\x61ult_algorithm\x18\x07 \x01(\x0e\x32\'.yandex.cloud.kms.v1.SymmetricAlgorithm\x12\x32\n\x0frotation_period\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1b\n\x13\x64\x65letion_protection\x18\t \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\",\n\x1aUpdateSymmetricKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"9\n\x19\x44\x65leteSymmetricKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\",\n\x1a\x44\x65leteSymmetricKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"f\n$SetPrimarySymmetricKeyVersionRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nversion_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"K\n%SetPrimarySymmetricKeyVersionMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\"9\n\x19RotateSymmetricKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"L\n\x1aRotateSymmetricKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x1e\n\x16new_primary_version_id\x18\x02 \x01(\t\"\xa2\x01\n-ScheduleSymmetricKeyVersionDestructionRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nversion_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\x0epending_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x84\x01\n.ScheduleSymmetricKeyVersionDestructionMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12.\n\ndestroy_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"m\n+CancelSymmetricKeyVersionDestructionRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nversion_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"R\n,CancelSymmetricKeyVersionDestructionMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\"\x7f\n!ListSymmetricKeyOperationsRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"t\n\"ListSymmetricKeyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf6\x14\n\x13SymmetricKeyService\x12\xa2\x01\n\x06\x43reate\x12..yandex.cloud.kms.v1.CreateSymmetricKeyRequest\x1a!.yandex.cloud.operation.Operation\"E\xb2\xd2**\n\x1a\x43reateSymmetricKeyMetadata\x12\x0cSymmetricKey\x82\xd3\xe4\x93\x02\x11\"\x0c/kms/v1/keys:\x01*\x12t\n\x03Get\x12+.yandex.cloud.kms.v1.GetSymmetricKeyRequest\x1a!.yandex.cloud.kms.v1.SymmetricKey\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/kms/v1/keys/{key_id}\x12{\n\x04List\x12-.yandex.cloud.kms.v1.ListSymmetricKeysRequest\x1a..yandex.cloud.kms.v1.ListSymmetricKeysResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/kms/v1/keys\x12\xa3\x01\n\x0cListVersions\x12\x34.yandex.cloud.kms.v1.ListSymmetricKeyVersionsRequest\x1a\x35.yandex.cloud.kms.v1.ListSymmetricKeyVersionsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/kms/v1/keys/{key_id}/versions\x12\xab\x01\n\x06Update\x12..yandex.cloud.kms.v1.UpdateSymmetricKeyRequest\x1a!.yandex.cloud.operation.Operation\"N\xb2\xd2**\n\x1aUpdateSymmetricKeyMetadata\x12\x0cSymmetricKey\x82\xd3\xe4\x93\x02\x1a\x32\x15/kms/v1/keys/{key_id}:\x01*\x12\xa8\x01\n\x06\x44\x65lete\x12..yandex.cloud.kms.v1.DeleteSymmetricKeyRequest\x1a!.yandex.cloud.operation.Operation\"K\xb2\xd2**\n\x1a\x44\x65leteSymmetricKeyMetadata\x12\x0cSymmetricKey\x82\xd3\xe4\x93\x02\x17*\x15/kms/v1/keys/{key_id}\x12\xde\x01\n\x11SetPrimaryVersion\x12\x39.yandex.cloud.kms.v1.SetPrimarySymmetricKeyVersionRequest\x1a!.yandex.cloud.operation.Operation\"k\xb2\xd2*5\n%SetPrimarySymmetricKeyVersionMetadata\x12\x0cSymmetricKey\x82\xd3\xe4\x93\x02,\"\'/kms/v1/keys/{key_id}:setPrimaryVersion:\x01*\x12\x8a\x02\n\x1aScheduleVersionDestruction\x12\x42.yandex.cloud.kms.v1.ScheduleSymmetricKeyVersionDestructionRequest\x1a!.yandex.cloud.operation.Operation\"\x84\x01\xb2\xd2*E\n.ScheduleSymmetricKeyVersionDestructionMetadata\x12\x13SymmetricKeyVersion\x82\xd3\xe4\x93\x02\x35\"0/kms/v1/keys/{key_id}:scheduleVersionDestruction:\x01*\x12\x82\x02\n\x18\x43\x61ncelVersionDestruction\x12@.yandex.cloud.kms.v1.CancelSymmetricKeyVersionDestructionRequest\x1a!.yandex.cloud.operation.Operation\"\x80\x01\xb2\xd2*C\n,CancelSymmetricKeyVersionDestructionMetadata\x12\x13SymmetricKeyVersion\x82\xd3\xe4\x93\x02\x33\"./kms/v1/keys/{key_id}:cancelVersionDestruction:\x01*\x12\xaf\x01\n\x06Rotate\x12..yandex.cloud.kms.v1.RotateSymmetricKeyRequest\x1a!.yandex.cloud.operation.Operation\"R\xb2\xd2**\n\x1aRotateSymmetricKeyMetadata\x12\x0cSymmetricKey\x82\xd3\xe4\x93\x02\x1e\"\x1c/kms/v1/keys/{key_id}:rotate\x12\xab\x01\n\x0eListOperations\x12\x36.yandex.cloud.kms.v1.ListSymmetricKeyOperationsRequest\x1a\x37.yandex.cloud.kms.v1.ListSymmetricKeyOperationsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /kms/v1/keys/{key_id}/operations\x12\xac\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/kms/v1/keys/{resource_id}:listAccessBindings\x12\xdb\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"t\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x31\",/kms/v1/keys/{resource_id}:setAccessBindings:\x01*\x12\xe7\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"z\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x34\"//kms/v1/keys/{resource_id}:updateAccessBindings:\x01*BV\n\x17yandex.cloud.api.kms.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1;kmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.kms.v1.symmetric_key_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.kms.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1;kms'
  _CREATESYMMETRICKEYREQUEST_LABELSENTRY._options = None
  _CREATESYMMETRICKEYREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATESYMMETRICKEYREQUEST.fields_by_name['folder_id']._options = None
  _CREATESYMMETRICKEYREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATESYMMETRICKEYREQUEST.fields_by_name['name']._options = None
  _CREATESYMMETRICKEYREQUEST.fields_by_name['name']._serialized_options = b'\212\3101\005<=100'
  _CREATESYMMETRICKEYREQUEST.fields_by_name['description']._options = None
  _CREATESYMMETRICKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _CREATESYMMETRICKEYREQUEST.fields_by_name['labels']._options = None
  _CREATESYMMETRICKEYREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _GETSYMMETRICKEYREQUEST.fields_by_name['key_id']._options = None
  _GETSYMMETRICKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSYMMETRICKEYSREQUEST.fields_by_name['folder_id']._options = None
  _LISTSYMMETRICKEYSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSYMMETRICKEYSREQUEST.fields_by_name['page_size']._options = None
  _LISTSYMMETRICKEYSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSYMMETRICKEYSREQUEST.fields_by_name['page_token']._options = None
  _LISTSYMMETRICKEYSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTSYMMETRICKEYVERSIONSREQUEST.fields_by_name['key_id']._options = None
  _LISTSYMMETRICKEYVERSIONSREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSYMMETRICKEYVERSIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTSYMMETRICKEYVERSIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSYMMETRICKEYVERSIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTSYMMETRICKEYVERSIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _UPDATESYMMETRICKEYREQUEST_LABELSENTRY._options = None
  _UPDATESYMMETRICKEYREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['key_id']._options = None
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['update_mask']._options = None
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['update_mask']._serialized_options = b'\350\3071\001'
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['name']._options = None
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['name']._serialized_options = b'\212\3101\005<=100'
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['description']._options = None
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['labels']._options = None
  _UPDATESYMMETRICKEYREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _DELETESYMMETRICKEYREQUEST.fields_by_name['key_id']._options = None
  _DELETESYMMETRICKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _SETPRIMARYSYMMETRICKEYVERSIONREQUEST.fields_by_name['key_id']._options = None
  _SETPRIMARYSYMMETRICKEYVERSIONREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _SETPRIMARYSYMMETRICKEYVERSIONREQUEST.fields_by_name['version_id']._options = None
  _SETPRIMARYSYMMETRICKEYVERSIONREQUEST.fields_by_name['version_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ROTATESYMMETRICKEYREQUEST.fields_by_name['key_id']._options = None
  _ROTATESYMMETRICKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['key_id']._options = None
  _SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['version_id']._options = None
  _SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['version_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CANCELSYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['key_id']._options = None
  _CANCELSYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CANCELSYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['version_id']._options = None
  _CANCELSYMMETRICKEYVERSIONDESTRUCTIONREQUEST.fields_by_name['version_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSYMMETRICKEYOPERATIONSREQUEST.fields_by_name['key_id']._options = None
  _LISTSYMMETRICKEYOPERATIONSREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSYMMETRICKEYOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTSYMMETRICKEYOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSYMMETRICKEYOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTSYMMETRICKEYOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _SYMMETRICKEYSERVICE.methods_by_name['Create']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['Create']._serialized_options = b'\262\322**\n\032CreateSymmetricKeyMetadata\022\014SymmetricKey\202\323\344\223\002\021\"\014/kms/v1/keys:\001*'
  _SYMMETRICKEYSERVICE.methods_by_name['Get']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\027\022\025/kms/v1/keys/{key_id}'
  _SYMMETRICKEYSERVICE.methods_by_name['List']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\016\022\014/kms/v1/keys'
  _SYMMETRICKEYSERVICE.methods_by_name['ListVersions']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['ListVersions']._serialized_options = b'\202\323\344\223\002 \022\036/kms/v1/keys/{key_id}/versions'
  _SYMMETRICKEYSERVICE.methods_by_name['Update']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['Update']._serialized_options = b'\262\322**\n\032UpdateSymmetricKeyMetadata\022\014SymmetricKey\202\323\344\223\002\0322\025/kms/v1/keys/{key_id}:\001*'
  _SYMMETRICKEYSERVICE.methods_by_name['Delete']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322**\n\032DeleteSymmetricKeyMetadata\022\014SymmetricKey\202\323\344\223\002\027*\025/kms/v1/keys/{key_id}'
  _SYMMETRICKEYSERVICE.methods_by_name['SetPrimaryVersion']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['SetPrimaryVersion']._serialized_options = b'\262\322*5\n%SetPrimarySymmetricKeyVersionMetadata\022\014SymmetricKey\202\323\344\223\002,\"\'/kms/v1/keys/{key_id}:setPrimaryVersion:\001*'
  _SYMMETRICKEYSERVICE.methods_by_name['ScheduleVersionDestruction']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['ScheduleVersionDestruction']._serialized_options = b'\262\322*E\n.ScheduleSymmetricKeyVersionDestructionMetadata\022\023SymmetricKeyVersion\202\323\344\223\0025\"0/kms/v1/keys/{key_id}:scheduleVersionDestruction:\001*'
  _SYMMETRICKEYSERVICE.methods_by_name['CancelVersionDestruction']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['CancelVersionDestruction']._serialized_options = b'\262\322*C\n,CancelSymmetricKeyVersionDestructionMetadata\022\023SymmetricKeyVersion\202\323\344\223\0023\"./kms/v1/keys/{key_id}:cancelVersionDestruction:\001*'
  _SYMMETRICKEYSERVICE.methods_by_name['Rotate']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['Rotate']._serialized_options = b'\262\322**\n\032RotateSymmetricKeyMetadata\022\014SymmetricKey\202\323\344\223\002\036\"\034/kms/v1/keys/{key_id}:rotate'
  _SYMMETRICKEYSERVICE.methods_by_name['ListOperations']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002\"\022 /kms/v1/keys/{key_id}/operations'
  _SYMMETRICKEYSERVICE.methods_by_name['ListAccessBindings']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002/\022-/kms/v1/keys/{resource_id}:listAccessBindings'
  _SYMMETRICKEYSERVICE.methods_by_name['SetAccessBindings']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\0021\",/kms/v1/keys/{resource_id}:setAccessBindings:\001*'
  _SYMMETRICKEYSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _SYMMETRICKEYSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\0024\"//kms/v1/keys/{resource_id}:updateAccessBindings:\001*'
  _globals['_CREATESYMMETRICKEYREQUEST']._serialized_start=382
  _globals['_CREATESYMMETRICKEYREQUEST']._serialized_end=834
  _globals['_CREATESYMMETRICKEYREQUEST_LABELSENTRY']._serialized_start=789
  _globals['_CREATESYMMETRICKEYREQUEST_LABELSENTRY']._serialized_end=834
  _globals['_CREATESYMMETRICKEYMETADATA']._serialized_start=836
  _globals['_CREATESYMMETRICKEYMETADATA']._serialized_end=908
  _globals['_GETSYMMETRICKEYREQUEST']._serialized_start=910
  _globals['_GETSYMMETRICKEYREQUEST']._serialized_end=964
  _globals['_LISTSYMMETRICKEYSREQUEST']._serialized_start=966
  _globals['_LISTSYMMETRICKEYSREQUEST']._serialized_end=1087
  _globals['_LISTSYMMETRICKEYSRESPONSE']._serialized_start=1089
  _globals['_LISTSYMMETRICKEYSRESPONSE']._serialized_end=1190
  _globals['_LISTSYMMETRICKEYVERSIONSREQUEST']._serialized_start=1192
  _globals['_LISTSYMMETRICKEYVERSIONSREQUEST']._serialized_end=1317
  _globals['_LISTSYMMETRICKEYVERSIONSRESPONSE']._serialized_start=1319
  _globals['_LISTSYMMETRICKEYVERSIONSRESPONSE']._serialized_end=1442
  _globals['_UPDATESYMMETRICKEYREQUEST']._serialized_start=1445
  _globals['_UPDATESYMMETRICKEYREQUEST']._serialized_end=2007
  _globals['_UPDATESYMMETRICKEYREQUEST_LABELSENTRY']._serialized_start=789
  _globals['_UPDATESYMMETRICKEYREQUEST_LABELSENTRY']._serialized_end=834
  _globals['_UPDATESYMMETRICKEYMETADATA']._serialized_start=2009
  _globals['_UPDATESYMMETRICKEYMETADATA']._serialized_end=2053
  _globals['_DELETESYMMETRICKEYREQUEST']._serialized_start=2055
  _globals['_DELETESYMMETRICKEYREQUEST']._serialized_end=2112
  _globals['_DELETESYMMETRICKEYMETADATA']._serialized_start=2114
  _globals['_DELETESYMMETRICKEYMETADATA']._serialized_end=2158
  _globals['_SETPRIMARYSYMMETRICKEYVERSIONREQUEST']._serialized_start=2160
  _globals['_SETPRIMARYSYMMETRICKEYVERSIONREQUEST']._serialized_end=2262
  _globals['_SETPRIMARYSYMMETRICKEYVERSIONMETADATA']._serialized_start=2264
  _globals['_SETPRIMARYSYMMETRICKEYVERSIONMETADATA']._serialized_end=2339
  _globals['_ROTATESYMMETRICKEYREQUEST']._serialized_start=2341
  _globals['_ROTATESYMMETRICKEYREQUEST']._serialized_end=2398
  _globals['_ROTATESYMMETRICKEYMETADATA']._serialized_start=2400
  _globals['_ROTATESYMMETRICKEYMETADATA']._serialized_end=2476
  _globals['_SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONREQUEST']._serialized_start=2479
  _globals['_SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONREQUEST']._serialized_end=2641
  _globals['_SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONMETADATA']._serialized_start=2644
  _globals['_SCHEDULESYMMETRICKEYVERSIONDESTRUCTIONMETADATA']._serialized_end=2776
  _globals['_CANCELSYMMETRICKEYVERSIONDESTRUCTIONREQUEST']._serialized_start=2778
  _globals['_CANCELSYMMETRICKEYVERSIONDESTRUCTIONREQUEST']._serialized_end=2887
  _globals['_CANCELSYMMETRICKEYVERSIONDESTRUCTIONMETADATA']._serialized_start=2889
  _globals['_CANCELSYMMETRICKEYVERSIONDESTRUCTIONMETADATA']._serialized_end=2971
  _globals['_LISTSYMMETRICKEYOPERATIONSREQUEST']._serialized_start=2973
  _globals['_LISTSYMMETRICKEYOPERATIONSREQUEST']._serialized_end=3100
  _globals['_LISTSYMMETRICKEYOPERATIONSRESPONSE']._serialized_start=3102
  _globals['_LISTSYMMETRICKEYOPERATIONSRESPONSE']._serialized_end=3218
  _globals['_SYMMETRICKEYSERVICE']._serialized_start=3221
  _globals['_SYMMETRICKEYSERVICE']._serialized_end=5899
# @@protoc_insertion_point(module_scope)
