# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/node_execution_error_details.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datasphere/v1/node_execution_error_details.proto',
  package='yandex.cloud.datasphere.v1',
  syntax='proto3',
  serialized_options=b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=yandex/cloud/datasphere/v1/node_execution_error_details.proto\x12\x1ayandex.cloud.datasphere.v1\"Y\n\x19NodeExecutionErrorDetails\x12\x12\n\nerror_name\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\ttraceback\x18\x03 \x03(\tBk\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3'
)




_NODEEXECUTIONERRORDETAILS = _descriptor.Descriptor(
  name='NodeExecutionErrorDetails',
  full_name='yandex.cloud.datasphere.v1.NodeExecutionErrorDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_name', full_name='yandex.cloud.datasphere.v1.NodeExecutionErrorDetails.error_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='yandex.cloud.datasphere.v1.NodeExecutionErrorDetails.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traceback', full_name='yandex.cloud.datasphere.v1.NodeExecutionErrorDetails.traceback', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=182,
)

DESCRIPTOR.message_types_by_name['NodeExecutionErrorDetails'] = _NODEEXECUTIONERRORDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeExecutionErrorDetails = _reflection.GeneratedProtocolMessageType('NodeExecutionErrorDetails', (_message.Message,), {
  'DESCRIPTOR' : _NODEEXECUTIONERRORDETAILS,
  '__module__' : 'yandex.cloud.datasphere.v1.node_execution_error_details_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.NodeExecutionErrorDetails)
  })
_sym_db.RegisterMessage(NodeExecutionErrorDetails)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
