# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/triggers/v1/predicate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/serverless/triggers/v1/predicate.proto\x12#yandex.cloud.serverless.triggers.v1\x1a\x1dyandex/cloud/validation.proto\"\xc5\x01\n\tPredicate\x12J\n\rand_predicate\x18\x02 \x01(\x0b\x32\x31.yandex.cloud.serverless.triggers.v1.AndPredicateH\x00\x12Y\n\x15\x66ield_value_predicate\x18\x04 \x01(\x0b\x32\x38.yandex.cloud.serverless.triggers.v1.FieldValuePredicateH\x00\x42\x11\n\tpredicate\x12\x04\xc0\xc1\x31\x01\"Q\n\x0c\x41ndPredicate\x12\x41\n\tpredicate\x18\x01 \x03(\x0b\x32..yandex.cloud.serverless.triggers.v1.Predicate\"s\n\x13\x46ieldValuePredicate\x12\x18\n\nfield_path\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0f\n\x05\x65xact\x18\x03 \x01(\tH\x00\x12\x10\n\x06prefix\x18\x08 \x01(\tH\x00\x12\x10\n\x06suffix\x18\t \x01(\tH\x00\x42\r\n\x05value\x12\x04\xc0\xc1\x31\x01\x42{\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.triggers.v1.predicate_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggers'
  _PREDICATE.oneofs_by_name['predicate']._options = None
  _PREDICATE.oneofs_by_name['predicate']._serialized_options = b'\300\3011\001'
  _FIELDVALUEPREDICATE.oneofs_by_name['value']._options = None
  _FIELDVALUEPREDICATE.oneofs_by_name['value']._serialized_options = b'\300\3011\001'
  _FIELDVALUEPREDICATE.fields_by_name['field_path']._options = None
  _FIELDVALUEPREDICATE.fields_by_name['field_path']._serialized_options = b'\350\3071\001'
  _globals['_PREDICATE']._serialized_start=124
  _globals['_PREDICATE']._serialized_end=321
  _globals['_ANDPREDICATE']._serialized_start=323
  _globals['_ANDPREDICATE']._serialized_end=404
  _globals['_FIELDVALUEPREDICATE']._serialized_start=406
  _globals['_FIELDVALUEPREDICATE']._serialized_end=521
# @@protoc_insertion_point(module_scope)
