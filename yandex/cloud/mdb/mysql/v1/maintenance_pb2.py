# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1/maintenance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/mdb/mysql/v1/maintenance.proto\x12\x19yandex.cloud.mdb.mysql.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xc4\x01\n\x11MaintenanceWindow\x12\x46\n\x07\x61nytime\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mysql.v1.AnytimeMaintenanceWindowH\x00\x12W\n\x19weekly_maintenance_window\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.mysql.v1.WeeklyMaintenanceWindowH\x00\x42\x0e\n\x06policy\x12\x04\xc0\xc1\x31\x01\"\x1a\n\x18\x41nytimeMaintenanceWindow\"\xde\x01\n\x17WeeklyMaintenanceWindow\x12G\n\x03\x64\x61y\x18\x01 \x01(\x0e\x32:.yandex.cloud.mdb.mysql.v1.WeeklyMaintenanceWindow.WeekDay\x12\x16\n\x04hour\x18\x02 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x31-24\"b\n\x07WeekDay\x12\x18\n\x14WEEK_DAY_UNSPECIFIED\x10\x00\x12\x07\n\x03MON\x10\x01\x12\x07\n\x03TUE\x10\x02\x12\x07\n\x03WED\x10\x03\x12\x07\n\x03THU\x10\x04\x12\x07\n\x03\x46RI\x10\x05\x12\x07\n\x03SAT\x10\x06\x12\x07\n\x03SUN\x10\x07\"b\n\x14MaintenanceOperation\x12\x17\n\x04info\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x31\n\rdelayed_until\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampBd\n\x1dyandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mysql.v1.maintenance_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035yandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysql'
  _MAINTENANCEWINDOW.oneofs_by_name['policy']._options = None
  _MAINTENANCEWINDOW.oneofs_by_name['policy']._serialized_options = b'\300\3011\001'
  _WEEKLYMAINTENANCEWINDOW.fields_by_name['hour']._options = None
  _WEEKLYMAINTENANCEWINDOW.fields_by_name['hour']._serialized_options = b'\372\3071\0041-24'
  _MAINTENANCEOPERATION.fields_by_name['info']._options = None
  _MAINTENANCEOPERATION.fields_by_name['info']._serialized_options = b'\212\3101\005<=256'
  _globals['_MAINTENANCEWINDOW']._serialized_start=139
  _globals['_MAINTENANCEWINDOW']._serialized_end=335
  _globals['_ANYTIMEMAINTENANCEWINDOW']._serialized_start=337
  _globals['_ANYTIMEMAINTENANCEWINDOW']._serialized_end=363
  _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_start=366
  _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_end=588
  _globals['_WEEKLYMAINTENANCEWINDOW_WEEKDAY']._serialized_start=490
  _globals['_WEEKLYMAINTENANCEWINDOW_WEEKDAY']._serialized_end=588
  _globals['_MAINTENANCEOPERATION']._serialized_start=590
  _globals['_MAINTENANCEOPERATION']._serialized_end=688
# @@protoc_insertion_point(module_scope)
