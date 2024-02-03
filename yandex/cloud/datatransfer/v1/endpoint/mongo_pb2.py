# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/mongo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/datatransfer/v1/endpoint/mongo.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\"\x8a\x01\n\x0eOnPremiseMongo\x12\r\n\x05hosts\x18\x01 \x03(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12\x13\n\x0breplica_set\x18\x05 \x01(\t\x12@\n\x08tls_mode\x18\x06 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSModeJ\x04\x08\x03\x10\x05\"\xee\x01\n\x16MongoConnectionOptions\x12\x18\n\x0emdb_cluster_id\x18\x01 \x01(\tH\x00\x12K\n\non_premise\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.datatransfer.v1.endpoint.OnPremiseMongoH\x00\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x13\n\x0b\x61uth_source\x18\x05 \x01(\tB\t\n\x07\x61\x64\x64ress\"\x82\x01\n\x0fMongoConnection\x12[\n\x12\x63onnection_options\x18\x03 \x01(\x0b\x32=.yandex.cloud.datatransfer.v1.endpoint.MongoConnectionOptionsH\x00\x42\x0c\n\nconnectionJ\x04\x08\x01\x10\x03\"A\n\x0fMongoCollection\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x02 \x01(\t\"\xd6\x02\n\x0bMongoSource\x12J\n\nconnection\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.MongoConnection\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12K\n\x0b\x63ollections\x18\x06 \x03(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.MongoCollection\x12T\n\x14\x65xcluded_collections\x18\x07 \x03(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.MongoCollection\x12 \n\x18secondary_preferred_mode\x18\x08 \x01(\x08\x12\x17\n\x0fsecurity_groups\x18\x0b \x03(\tJ\x04\x08\x03\x10\x06J\x04\x08\t\x10\x0b\"\xeb\x01\n\x0bMongoTarget\x12J\n\nconnection\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.MongoConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12L\n\x0e\x63leanup_policy\x18\x06 \x01(\x0e\x32\x34.yandex.cloud.datatransfer.v1.endpoint.CleanupPolicy\x12\x11\n\tsubnet_id\x18\x07 \x01(\t\x12\x17\n\x0fsecurity_groups\x18\x08 \x03(\tJ\x04\x08\x03\x10\x06\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.mongo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_ONPREMISEMONGO']._serialized_start=145
  _globals['_ONPREMISEMONGO']._serialized_end=283
  _globals['_MONGOCONNECTIONOPTIONS']._serialized_start=286
  _globals['_MONGOCONNECTIONOPTIONS']._serialized_end=524
  _globals['_MONGOCONNECTION']._serialized_start=527
  _globals['_MONGOCONNECTION']._serialized_end=657
  _globals['_MONGOCOLLECTION']._serialized_start=659
  _globals['_MONGOCOLLECTION']._serialized_end=724
  _globals['_MONGOSOURCE']._serialized_start=727
  _globals['_MONGOSOURCE']._serialized_end=1069
  _globals['_MONGOTARGET']._serialized_start=1072
  _globals['_MONGOTARGET']._serialized_end=1307
# @@protoc_insertion_point(module_scope)
