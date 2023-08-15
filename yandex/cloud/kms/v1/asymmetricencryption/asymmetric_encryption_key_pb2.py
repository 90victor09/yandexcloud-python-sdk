# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto',
  package='yandex.cloud.kms.v1.asymmetricencryption',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kms',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nHyandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto\x12(yandex.cloud.kms.v1.asymmetricencryption\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc1\x04\n\x17\x41symmetricEncryptionKey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12]\n\x06labels\x18\x06 \x03(\x0b\x32M.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.LabelsEntry\x12X\n\x06status\x18\x07 \x01(\x0e\x32H.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.Status\x12\x65\n\x14\x65ncryption_algorithm\x18\x08 \x01(\x0e\x32G.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionAlgorithm\x12\x1b\n\x13\x64\x65letion_protection\x18\t \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03*\xad\x01\n\x1d\x41symmetricEncryptionAlgorithm\x12/\n+ASYMMETRIC_ENCRYPTION_ALGORITHM_UNSPECIFIED\x10\x00\x12\x1d\n\x19RSA_2048_ENC_OAEP_SHA_256\x10\x01\x12\x1d\n\x19RSA_3072_ENC_OAEP_SHA_256\x10\x02\x12\x1d\n\x19RSA_4096_ENC_OAEP_SHA_256\x10\x03\x42k\n\x17yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kmsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ASYMMETRICENCRYPTIONALGORITHM = _descriptor.EnumDescriptor(
  name='AsymmetricEncryptionAlgorithm',
  full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASYMMETRIC_ENCRYPTION_ALGORITHM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RSA_2048_ENC_OAEP_SHA_256', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RSA_3072_ENC_OAEP_SHA_256', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RSA_4096_ENC_OAEP_SHA_256', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=732,
  serialized_end=905,
)
_sym_db.RegisterEnumDescriptor(_ASYMMETRICENCRYPTIONALGORITHM)

AsymmetricEncryptionAlgorithm = enum_type_wrapper.EnumTypeWrapper(_ASYMMETRICENCRYPTIONALGORITHM)
ASYMMETRIC_ENCRYPTION_ALGORITHM_UNSPECIFIED = 0
RSA_2048_ENC_OAEP_SHA_256 = 1
RSA_3072_ENC_OAEP_SHA_256 = 2
RSA_4096_ENC_OAEP_SHA_256 = 3


_ASYMMETRICENCRYPTIONKEY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=657,
  serialized_end=729,
)
_sym_db.RegisterEnumDescriptor(_ASYMMETRICENCRYPTIONKEY_STATUS)


_ASYMMETRICENCRYPTIONKEY_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=655,
)

_ASYMMETRICENCRYPTIONKEY = _descriptor.Descriptor(
  name='AsymmetricEncryptionKey',
  full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encryption_algorithm', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.encryption_algorithm', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deletion_protection', full_name='yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.deletion_protection', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ASYMMETRICENCRYPTIONKEY_LABELSENTRY, ],
  enum_types=[
    _ASYMMETRICENCRYPTIONKEY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=729,
)

_ASYMMETRICENCRYPTIONKEY_LABELSENTRY.containing_type = _ASYMMETRICENCRYPTIONKEY
_ASYMMETRICENCRYPTIONKEY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASYMMETRICENCRYPTIONKEY.fields_by_name['labels'].message_type = _ASYMMETRICENCRYPTIONKEY_LABELSENTRY
_ASYMMETRICENCRYPTIONKEY.fields_by_name['status'].enum_type = _ASYMMETRICENCRYPTIONKEY_STATUS
_ASYMMETRICENCRYPTIONKEY.fields_by_name['encryption_algorithm'].enum_type = _ASYMMETRICENCRYPTIONALGORITHM
_ASYMMETRICENCRYPTIONKEY_STATUS.containing_type = _ASYMMETRICENCRYPTIONKEY
DESCRIPTOR.message_types_by_name['AsymmetricEncryptionKey'] = _ASYMMETRICENCRYPTIONKEY
DESCRIPTOR.enum_types_by_name['AsymmetricEncryptionAlgorithm'] = _ASYMMETRICENCRYPTIONALGORITHM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AsymmetricEncryptionKey = _reflection.GeneratedProtocolMessageType('AsymmetricEncryptionKey', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ASYMMETRICENCRYPTIONKEY_LABELSENTRY,
    '__module__' : 'yandex.cloud.kms.v1.asymmetricencryption.asymmetric_encryption_key_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ASYMMETRICENCRYPTIONKEY,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricencryption.asymmetric_encryption_key_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey)
  })
_sym_db.RegisterMessage(AsymmetricEncryptionKey)
_sym_db.RegisterMessage(AsymmetricEncryptionKey.LabelsEntry)


DESCRIPTOR._options = None
_ASYMMETRICENCRYPTIONKEY_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)