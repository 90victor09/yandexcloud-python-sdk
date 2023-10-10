# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/disk_placement_group_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import disk_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2
from yandex.cloud.compute.v1 import disk_placement_group_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__placement__group__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/compute/v1/disk_placement_group_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a\"yandex/cloud/compute/v1/disk.proto\x1a\x32yandex/cloud/compute/v1/disk_placement_group.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"M\n\x1cGetDiskPlacementGroupRequest\x12-\n\x17\x64isk_placement_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xb8\x01\n\x1eListDiskPlacementGroupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x86\x01\n\x1fListDiskPlacementGroupsResponse\x12J\n\x15\x64isk_placement_groups\x18\x01 \x03(\x0b\x32+.yandex.cloud.compute.v1.DiskPlacementGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xd8\x04\n\x1f\x43reateDiskPlacementGroupRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x99\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x44.yandex.cloud.compute.v1.CreateDiskPlacementGroupRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x1d\n\x07zone_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12Y\n\x19spread_placement_strategy\x18\x06 \x01(\x0b\x32\x34.yandex.cloud.compute.v1.DiskSpreadPlacementStrategyH\x00\x12_\n\x1cpartition_placement_strategy\x18\x07 \x01(\x0b\x32\x37.yandex.cloud.compute.v1.DiskPartitionPlacementStrategyH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1a\n\x12placement_strategy\x12\x04\xc0\xc1\x31\x01\"C\n CreateDiskPlacementGroupMetadata\x12\x1f\n\x17\x64isk_placement_group_id\x18\x01 \x01(\t\"\xa0\x03\n\x1fUpdateDiskPlacementGroupRequest\x12-\n\x17\x64isk_placement_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x99\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x44.yandex.cloud.compute.v1.UpdateDiskPlacementGroupRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"C\n UpdateDiskPlacementGroupMetadata\x12\x1f\n\x17\x64isk_placement_group_id\x18\x01 \x01(\t\"P\n\x1f\x44\x65leteDiskPlacementGroupRequest\x12-\n\x17\x64isk_placement_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"C\n DeleteDiskPlacementGroupMetadata\x12\x1f\n\x17\x64isk_placement_group_id\x18\x01 \x01(\t\"\x91\x01\n\"ListDiskPlacementGroupDisksRequest\x12-\n\x17\x64isk_placement_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"l\n#ListDiskPlacementGroupDisksResponse\x12,\n\x05\x64isks\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.compute.v1.Disk\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x96\x01\n\'ListDiskPlacementGroupOperationsRequest\x12-\n\x17\x64isk_placement_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"z\n(ListDiskPlacementGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x95\x11\n\x19\x44iskPlacementGroupService\x12\xac\x01\n\x03Get\x12\x35.yandex.cloud.compute.v1.GetDiskPlacementGroupRequest\x1a+.yandex.cloud.compute.v1.DiskPlacementGroup\"A\x82\xd3\xe4\x93\x02;\x12\x39/compute/v1/diskPlacementGroups/{disk_placement_group_id}\x12\xa2\x01\n\x04List\x12\x37.yandex.cloud.compute.v1.ListDiskPlacementGroupsRequest\x1a\x38.yandex.cloud.compute.v1.ListDiskPlacementGroupsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/compute/v1/diskPlacementGroups\x12\xcb\x01\n\x06\x43reate\x12\x38.yandex.cloud.compute.v1.CreateDiskPlacementGroupRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*6\n CreateDiskPlacementGroupMetadata\x12\x12\x44iskPlacementGroup\x82\xd3\xe4\x93\x02$\"\x1f/compute/v1/diskPlacementGroups:\x01*\x12\xe5\x01\n\x06Update\x12\x38.yandex.cloud.compute.v1.UpdateDiskPlacementGroupRequest\x1a!.yandex.cloud.operation.Operation\"~\xb2\xd2*6\n UpdateDiskPlacementGroupMetadata\x12\x12\x44iskPlacementGroup\x82\xd3\xe4\x93\x02>29/compute/v1/diskPlacementGroups/{disk_placement_group_id}:\x01*\x12\xe5\x01\n\x06\x44\x65lete\x12\x38.yandex.cloud.compute.v1.DeleteDiskPlacementGroupRequest\x1a!.yandex.cloud.operation.Operation\"~\xb2\xd2*9\n DeleteDiskPlacementGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02;*9/compute/v1/diskPlacementGroups/{disk_placement_group_id}\x12\xcf\x01\n\tListDisks\x12;.yandex.cloud.compute.v1.ListDiskPlacementGroupDisksRequest\x1a<.yandex.cloud.compute.v1.ListDiskPlacementGroupDisksResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/compute/v1/diskPlacementGroups/{disk_placement_group_id}/disks\x12\xe3\x01\n\x0eListOperations\x12@.yandex.cloud.compute.v1.ListDiskPlacementGroupOperationsRequest\x1a\x41.yandex.cloud.compute.v1.ListDiskPlacementGroupOperationsResponse\"L\x82\xd3\xe4\x93\x02\x46\x12\x44/compute/v1/diskPlacementGroups/{disk_placement_group_id}/operations\x12\xbf\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/compute/v1/diskPlacementGroups/{resource_id}:listAccessBindings\x12\xfe\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x96\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x44\"?/compute/v1/diskPlacementGroups/{resource_id}:setAccessBindings:\x01*\x12\x8a\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x9c\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02G\"B/compute/v1/diskPlacementGroups/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.disk_placement_group_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _GETDISKPLACEMENTGROUPREQUEST.fields_by_name['disk_placement_group_id']._options = None
  _GETDISKPLACEMENTGROUPREQUEST.fields_by_name['disk_placement_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['folder_id']._options = None
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['filter']._options = None
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['order_by']._options = None
  _LISTDISKPLACEMENTGROUPSREQUEST.fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _CREATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEDISKPLACEMENTGROUPREQUEST.oneofs_by_name['placement_strategy']._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST.oneofs_by_name['placement_strategy']._serialized_options = b'\300\3011\001'
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['folder_id']._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['name']._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['description']._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['labels']._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['zone_id']._options = None
  _CREATEDISKPLACEMENTGROUPREQUEST.fields_by_name['zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY._options = None
  _UPDATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['disk_placement_group_id']._options = None
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['disk_placement_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['name']._options = None
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['description']._options = None
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['labels']._options = None
  _UPDATEDISKPLACEMENTGROUPREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _DELETEDISKPLACEMENTGROUPREQUEST.fields_by_name['disk_placement_group_id']._options = None
  _DELETEDISKPLACEMENTGROUPREQUEST.fields_by_name['disk_placement_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDISKPLACEMENTGROUPDISKSREQUEST.fields_by_name['disk_placement_group_id']._options = None
  _LISTDISKPLACEMENTGROUPDISKSREQUEST.fields_by_name['disk_placement_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDISKPLACEMENTGROUPDISKSREQUEST.fields_by_name['page_size']._options = None
  _LISTDISKPLACEMENTGROUPDISKSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTDISKPLACEMENTGROUPDISKSREQUEST.fields_by_name['page_token']._options = None
  _LISTDISKPLACEMENTGROUPDISKSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTDISKPLACEMENTGROUPOPERATIONSREQUEST.fields_by_name['disk_placement_group_id']._options = None
  _LISTDISKPLACEMENTGROUPOPERATIONSREQUEST.fields_by_name['disk_placement_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDISKPLACEMENTGROUPOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTDISKPLACEMENTGROUPOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTDISKPLACEMENTGROUPOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTDISKPLACEMENTGROUPOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Get']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002;\0229/compute/v1/diskPlacementGroups/{disk_placement_group_id}'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['List']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/compute/v1/diskPlacementGroups'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Create']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*6\n CreateDiskPlacementGroupMetadata\022\022DiskPlacementGroup\202\323\344\223\002$\"\037/compute/v1/diskPlacementGroups:\001*'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Update']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*6\n UpdateDiskPlacementGroupMetadata\022\022DiskPlacementGroup\202\323\344\223\002>29/compute/v1/diskPlacementGroups/{disk_placement_group_id}:\001*'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Delete']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*9\n DeleteDiskPlacementGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\002;*9/compute/v1/diskPlacementGroups/{disk_placement_group_id}'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['ListDisks']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['ListDisks']._serialized_options = b'\202\323\344\223\002A\022?/compute/v1/diskPlacementGroups/{disk_placement_group_id}/disks'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['ListOperations']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002F\022D/compute/v1/diskPlacementGroups/{disk_placement_group_id}/operations'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['ListAccessBindings']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002B\022@/compute/v1/diskPlacementGroups/{resource_id}:listAccessBindings'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['SetAccessBindings']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002D\"?/compute/v1/diskPlacementGroups/{resource_id}:setAccessBindings:\001*'
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _DISKPLACEMENTGROUPSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002G\"B/compute/v1/diskPlacementGroups/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETDISKPLACEMENTGROUPREQUEST']._serialized_start=378
  _globals['_GETDISKPLACEMENTGROUPREQUEST']._serialized_end=455
  _globals['_LISTDISKPLACEMENTGROUPSREQUEST']._serialized_start=458
  _globals['_LISTDISKPLACEMENTGROUPSREQUEST']._serialized_end=642
  _globals['_LISTDISKPLACEMENTGROUPSRESPONSE']._serialized_start=645
  _globals['_LISTDISKPLACEMENTGROUPSRESPONSE']._serialized_end=779
  _globals['_CREATEDISKPLACEMENTGROUPREQUEST']._serialized_start=782
  _globals['_CREATEDISKPLACEMENTGROUPREQUEST']._serialized_end=1382
  _globals['_CREATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_start=1309
  _globals['_CREATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_end=1354
  _globals['_CREATEDISKPLACEMENTGROUPMETADATA']._serialized_start=1384
  _globals['_CREATEDISKPLACEMENTGROUPMETADATA']._serialized_end=1451
  _globals['_UPDATEDISKPLACEMENTGROUPREQUEST']._serialized_start=1454
  _globals['_UPDATEDISKPLACEMENTGROUPREQUEST']._serialized_end=1870
  _globals['_UPDATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_start=1309
  _globals['_UPDATEDISKPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_end=1354
  _globals['_UPDATEDISKPLACEMENTGROUPMETADATA']._serialized_start=1872
  _globals['_UPDATEDISKPLACEMENTGROUPMETADATA']._serialized_end=1939
  _globals['_DELETEDISKPLACEMENTGROUPREQUEST']._serialized_start=1941
  _globals['_DELETEDISKPLACEMENTGROUPREQUEST']._serialized_end=2021
  _globals['_DELETEDISKPLACEMENTGROUPMETADATA']._serialized_start=2023
  _globals['_DELETEDISKPLACEMENTGROUPMETADATA']._serialized_end=2090
  _globals['_LISTDISKPLACEMENTGROUPDISKSREQUEST']._serialized_start=2093
  _globals['_LISTDISKPLACEMENTGROUPDISKSREQUEST']._serialized_end=2238
  _globals['_LISTDISKPLACEMENTGROUPDISKSRESPONSE']._serialized_start=2240
  _globals['_LISTDISKPLACEMENTGROUPDISKSRESPONSE']._serialized_end=2348
  _globals['_LISTDISKPLACEMENTGROUPOPERATIONSREQUEST']._serialized_start=2351
  _globals['_LISTDISKPLACEMENTGROUPOPERATIONSREQUEST']._serialized_end=2501
  _globals['_LISTDISKPLACEMENTGROUPOPERATIONSRESPONSE']._serialized_start=2503
  _globals['_LISTDISKPLACEMENTGROUPOPERATIONSRESPONSE']._serialized_end=2625
  _globals['_DISKPLACEMENTGROUPSERVICE']._serialized_start=2628
  _globals['_DISKPLACEMENTGROUPSERVICE']._serialized_end=4825
# @@protoc_insertion_point(module_scope)
