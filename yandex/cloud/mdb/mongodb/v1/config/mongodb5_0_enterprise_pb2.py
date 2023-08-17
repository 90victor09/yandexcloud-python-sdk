# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/config/mongodb5_0_enterprise.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>yandex/cloud/mdb/mongodb/v1/config/mongodb5_0_enterprise.proto\x12\"yandex.cloud.mdb.mongodb.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xdd\x11\n\x1aMongodConfig5_0_enterprise\x12W\n\x07storage\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage\x12n\n\x13operation_profiling\x18\x02 \x01(\x0b\x32Q.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.OperationProfiling\x12S\n\x03net\x18\x03 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Network\x12Y\n\x08security\x18\x04 \x01(\x0b\x32G.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Security\x12Z\n\taudit_log\x18\x05 \x01(\x0b\x32G.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.AuditLog\x12\x62\n\rset_parameter\x18\x06 \x01(\x0b\x32K.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.SetParameter\x1a\xdb\x06\n\x07Storage\x12\x66\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32Q.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger\x12_\n\x07journal\x18\x02 \x01(\x0b\x32N.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.Journal\x1a\xba\x04\n\nWiredTiger\x12u\n\rengine_config\x18\x01 \x01(\x0b\x32^.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.EngineConfig\x12}\n\x11\x63ollection_config\x18\x02 \x01(\x0b\x32\x62.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.CollectionConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xf0\x01\n\x10\x43ollectionConfig\x12\x87\x01\n\x10\x62lock_compressor\x18\x01 \x01(\x0e\x32m.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.CollectionConfig.Compressor\"R\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06SNAPPY\x10\x02\x12\x08\n\x04ZLIB\x10\x03\x12\x08\n\x04ZSTD\x10\x04\x1aJ\n\x07Journal\x12?\n\x0f\x63ommit_interval\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x31-500\x1a\xf7\x01\n\x12OperationProfiling\x12\x64\n\x04mode\x18\x01 \x01(\x0e\x32V.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\x1a\xad\x02\n\x08Security\x12\x35\n\x11\x65nable_encryption\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12Z\n\x04kmip\x18\x02 \x01(\x0b\x32L.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Security.KMIP\x1a\x8d\x01\n\x04KMIP\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12)\n\x04port\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x11\n\tserver_ca\x18\x03 \x01(\t\x12\x1a\n\x12\x63lient_certificate\x18\x04 \x01(\t\x12\x16\n\x0ekey_identifier\x18\x05 \x01(\t\x1aU\n\x08\x41uditLog\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x39\n\x15runtime_configuration\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1aO\n\x0cSetParameter\x12?\n\x1b\x61udit_authorization_success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xd9\x07\n\x1cMongoCfgConfig5_0_enterprise\x12Y\n\x07storage\x18\x01 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage\x12p\n\x13operation_profiling\x18\x02 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.OperationProfiling\x12U\n\x03net\x18\x03 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Network\x1a\xc0\x02\n\x07Storage\x12h\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage.WiredTiger\x1a\xca\x01\n\nWiredTiger\x12w\n\rengine_config\x18\x01 \x01(\x0b\x32`.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage.WiredTiger.EngineConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xf9\x01\n\x12OperationProfiling\x12\x66\n\x04mode\x18\x01 \x01(\x0e\x32X.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xc9\x01\n\x1aMongosConfig5_0_enterprise\x12S\n\x03net\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise.Network\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xa6\x02\n\x1dMongodConfigSet5_0_enterprise\x12X\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise\"\xae\x02\n\x1fMongoCfgConfigSet5_0_enterprise\x12Z\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise\x12U\n\x0buser_config\x18\x02 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise\x12X\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise\"\xa6\x02\n\x1dMongosConfigSet5_0_enterprise\x12X\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterpriseBx\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodb'
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL.fields_by_name['commit_interval']._options = None
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL.fields_by_name['commit_interval']._serialized_options = b'\372\3071\0051-500'
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGODCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGODCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOSCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOSCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MONGODCONFIG5_0_ENTERPRISE']._serialized_start=166
  _globals['_MONGODCONFIG5_0_ENTERPRISE']._serialized_end=2435
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE']._serialized_start=766
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE']._serialized_end=1625
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_start=979
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_end=1549
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=1239
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=1306
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_start=1309
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_end=1549
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_start=1467
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_end=1549
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL']._serialized_start=1551
  _globals['_MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL']._serialized_end=1625
  _globals['_MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING']._serialized_start=1628
  _globals['_MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING']._serialized_end=1875
  _globals['_MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_start=1816
  _globals['_MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_end=1875
  _globals['_MONGODCONFIG5_0_ENTERPRISE_NETWORK']._serialized_start=1877
  _globals['_MONGODCONFIG5_0_ENTERPRISE_NETWORK']._serialized_end=1963
  _globals['_MONGODCONFIG5_0_ENTERPRISE_SECURITY']._serialized_start=1966
  _globals['_MONGODCONFIG5_0_ENTERPRISE_SECURITY']._serialized_end=2267
  _globals['_MONGODCONFIG5_0_ENTERPRISE_SECURITY_KMIP']._serialized_start=2126
  _globals['_MONGODCONFIG5_0_ENTERPRISE_SECURITY_KMIP']._serialized_end=2267
  _globals['_MONGODCONFIG5_0_ENTERPRISE_AUDITLOG']._serialized_start=2269
  _globals['_MONGODCONFIG5_0_ENTERPRISE_AUDITLOG']._serialized_end=2354
  _globals['_MONGODCONFIG5_0_ENTERPRISE_SETPARAMETER']._serialized_start=2356
  _globals['_MONGODCONFIG5_0_ENTERPRISE_SETPARAMETER']._serialized_end=2435
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE']._serialized_start=2438
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE']._serialized_end=3423
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE']._serialized_start=2763
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE']._serialized_end=3083
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_start=2881
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_end=3083
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=1239
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=1306
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING']._serialized_start=3086
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING']._serialized_end=3335
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_start=1816
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_end=1875
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK']._serialized_start=1877
  _globals['_MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK']._serialized_end=1963
  _globals['_MONGOSCONFIG5_0_ENTERPRISE']._serialized_start=3426
  _globals['_MONGOSCONFIG5_0_ENTERPRISE']._serialized_end=3627
  _globals['_MONGOSCONFIG5_0_ENTERPRISE_NETWORK']._serialized_start=1877
  _globals['_MONGOSCONFIG5_0_ENTERPRISE_NETWORK']._serialized_end=1963
  _globals['_MONGODCONFIGSET5_0_ENTERPRISE']._serialized_start=3630
  _globals['_MONGODCONFIGSET5_0_ENTERPRISE']._serialized_end=3924
  _globals['_MONGOCFGCONFIGSET5_0_ENTERPRISE']._serialized_start=3927
  _globals['_MONGOCFGCONFIGSET5_0_ENTERPRISE']._serialized_end=4229
  _globals['_MONGOSCONFIGSET5_0_ENTERPRISE']._serialized_start=4232
  _globals['_MONGOSCONFIGSET5_0_ENTERPRISE']._serialized_end=4526
# @@protoc_insertion_point(module_scope)
