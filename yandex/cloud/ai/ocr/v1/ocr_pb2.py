# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/ocr/v1/ocr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n yandex/cloud/ai/ocr/v1/ocr.proto\x12\x16yandex.cloud.ai.ocr.v1\";\n\x07Polygon\x12\x30\n\x08vertices\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.ai.ocr.v1.Vertex\"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\"\x90\x01\n\x0eTextAnnotation\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12-\n\x06\x62locks\x18\x03 \x03(\x0b\x32\x1d.yandex.cloud.ai.ocr.v1.Block\x12\x30\n\x08\x65ntities\x18\x04 \x03(\x0b\x32\x1e.yandex.cloud.ai.ocr.v1.Entity\"$\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\xd9\x01\n\x05\x42lock\x12\x35\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x1f.yandex.cloud.ai.ocr.v1.Polygon\x12+\n\x05lines\x18\x02 \x03(\x0b\x32\x1c.yandex.cloud.ai.ocr.v1.Line\x12\x41\n\tlanguages\x18\x03 \x03(\x0b\x32..yandex.cloud.ai.ocr.v1.Block.DetectedLanguage\x1a)\n\x10\x44\x65tectedLanguage\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\"H\n\x0b\x41lternative\x12\x0c\n\x04text\x18\x01 \x01(\t\x12+\n\x05words\x18\x02 \x03(\x0b\x32\x1c.yandex.cloud.ai.ocr.v1.Word\"x\n\x04Line\x12\x35\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x1f.yandex.cloud.ai.ocr.v1.Polygon\x12\x39\n\x0c\x61lternatives\x18\x02 \x03(\x0b\x32#.yandex.cloud.ai.ocr.v1.Alternative\"a\n\x04Word\x12\x35\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x1f.yandex.cloud.ai.ocr.v1.Polygon\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0c\x65ntity_index\x18\x03 \x01(\x03\x42\\\n\x1ayandex.cloud.api.ai.ocr.v1Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/ocr/v1;ocrb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.ocr.v1.ocr_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.ai.ocr.v1Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/ocr/v1;ocr'
  _globals['_POLYGON']._serialized_start=60
  _globals['_POLYGON']._serialized_end=119
  _globals['_VERTEX']._serialized_start=121
  _globals['_VERTEX']._serialized_end=151
  _globals['_TEXTANNOTATION']._serialized_start=154
  _globals['_TEXTANNOTATION']._serialized_end=298
  _globals['_ENTITY']._serialized_start=300
  _globals['_ENTITY']._serialized_end=336
  _globals['_BLOCK']._serialized_start=339
  _globals['_BLOCK']._serialized_end=556
  _globals['_BLOCK_DETECTEDLANGUAGE']._serialized_start=515
  _globals['_BLOCK_DETECTEDLANGUAGE']._serialized_end=556
  _globals['_ALTERNATIVE']._serialized_start=558
  _globals['_ALTERNATIVE']._serialized_end=630
  _globals['_LINE']._serialized_start=632
  _globals['_LINE']._serialized_end=752
  _globals['_WORD']._serialized_start=754
  _globals['_WORD']._serialized_end=851
# @@protoc_insertion_point(module_scope)
