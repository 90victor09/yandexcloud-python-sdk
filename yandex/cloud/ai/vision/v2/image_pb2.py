# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/vision/v2/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ai/vision/v2/image.proto',
  package='yandex.cloud.ai.vision.v2',
  syntax='proto3',
  serialized_options=b'\n\035yandex.cloud.api.ai.vision.v2ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v2;vision',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%yandex/cloud/ai/vision/v2/image.proto\x12\x19yandex.cloud.ai.vision.v2\"\xa5\x01\n\x05Image\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12>\n\nimage_type\x18\x02 \x01(\x0e\x32*.yandex.cloud.ai.vision.v2.Image.ImageType\":\n\tImageType\x12\x1a\n\x16IMAGE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04JPEG\x10\x01\x12\x07\n\x03PNG\x10\x02\x42\r\n\x0bImageSourceBe\n\x1dyandex.cloud.api.ai.vision.v2ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v2;visionb\x06proto3'
)



_IMAGE_IMAGETYPE = _descriptor.EnumDescriptor(
  name='ImageType',
  full_name='yandex.cloud.ai.vision.v2.Image.ImageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMAGE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPEG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PNG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=219,
)
_sym_db.RegisterEnumDescriptor(_IMAGE_IMAGETYPE)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='yandex.cloud.ai.vision.v2.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='yandex.cloud.ai.vision.v2.Image.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_type', full_name='yandex.cloud.ai.vision.v2.Image.image_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMAGE_IMAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ImageSource', full_name='yandex.cloud.ai.vision.v2.Image.ImageSource',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=69,
  serialized_end=234,
)

_IMAGE.fields_by_name['image_type'].enum_type = _IMAGE_IMAGETYPE
_IMAGE_IMAGETYPE.containing_type = _IMAGE
_IMAGE.oneofs_by_name['ImageSource'].fields.append(
  _IMAGE.fields_by_name['content'])
_IMAGE.fields_by_name['content'].containing_oneof = _IMAGE.oneofs_by_name['ImageSource']
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'yandex.cloud.ai.vision.v2.image_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v2.Image)
  })
_sym_db.RegisterMessage(Image)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)