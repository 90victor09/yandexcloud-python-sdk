# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/http_router_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.apploadbalancer.v1 import http_router_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__pb2
from yandex.cloud.apploadbalancer.v1 import virtual_host_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9yandex/cloud/apploadbalancer/v1/http_router_service.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x31yandex/cloud/apploadbalancer/v1/http_router.proto\x1a\x32yandex/cloud/apploadbalancer/v1/virtual_host.proto\x1a\x1dyandex/cloud/validation.proto\"4\n\x14GetHttpRouterRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8b\x01\n\x16ListHttpRoutersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"u\n\x17ListHttpRoutersResponse\x12\x41\n\x0chttp_routers\x18\x01 \x03(\x0b\x32+.yandex.cloud.apploadbalancer.v1.HttpRouter\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"7\n\x17\x44\x65leteHttpRouterRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"2\n\x18\x44\x65leteHttpRouterMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\"\x9a\x04\n\x17UpdateHttpRouterRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x34\n\x04name\x18\x03 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x99\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x44.yandex.cloud.apploadbalancer.v1.UpdateHttpRouterRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x43\n\rvirtual_hosts\x18\x06 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.VirtualHost\x12\x44\n\rroute_options\x18\x08 \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptions\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x07\x10\x08\"2\n\x18UpdateHttpRouterMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\"\xe4\x03\n\x17\x43reateHttpRouterRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x34\n\x04name\x18\x02 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x99\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x44.yandex.cloud.apploadbalancer.v1.CreateHttpRouterRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x43\n\rvirtual_hosts\x18\x05 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.VirtualHost\x12\x44\n\rroute_options\x18\x07 \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptions\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x06\x10\x07\"2\n\x18\x43reateHttpRouterMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\"\x85\x01\n\x1fListHttpRouterOperationsRequest\x12$\n\x0ehttp_router_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"r\n ListHttpRouterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9f\t\n\x11HttpRouterService\x12\xa3\x01\n\x03Get\x12\x35.yandex.cloud.apploadbalancer.v1.GetHttpRouterRequest\x1a+.yandex.cloud.apploadbalancer.v1.HttpRouter\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/apploadbalancer/v1/httpRouters/{http_router_id}\x12\xa2\x01\n\x04List\x12\x37.yandex.cloud.apploadbalancer.v1.ListHttpRoutersRequest\x1a\x38.yandex.cloud.apploadbalancer.v1.ListHttpRoutersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/apploadbalancer/v1/httpRouters\x12\xbb\x01\n\x06\x43reate\x12\x38.yandex.cloud.apploadbalancer.v1.CreateHttpRouterRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*&\n\x18\x43reateHttpRouterMetadata\x12\nHttpRouter\x82\xd3\xe4\x93\x02$\"\x1f/apploadbalancer/v1/httpRouters:\x01*\x12\xcc\x01\n\x06Update\x12\x38.yandex.cloud.apploadbalancer.v1.UpdateHttpRouterRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*&\n\x18UpdateHttpRouterMetadata\x12\nHttpRouter\x82\xd3\xe4\x93\x02\x35\x32\x30/apploadbalancer/v1/httpRouters/{http_router_id}:\x01*\x12\xd4\x01\n\x06\x44\x65lete\x12\x38.yandex.cloud.apploadbalancer.v1.DeleteHttpRouterRequest\x1a!.yandex.cloud.operation.Operation\"m\xb2\xd2*1\n\x18\x44\x65leteHttpRouterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x32*0/apploadbalancer/v1/httpRouters/{http_router_id}\x12\xda\x01\n\x0eListOperations\x12@.yandex.cloud.apploadbalancer.v1.ListHttpRouterOperationsRequest\x1a\x41.yandex.cloud.apploadbalancer.v1.ListHttpRouterOperationsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/apploadbalancer/v1/httpRouters/{http_router_id}/operationsBz\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _GETHTTPROUTERREQUEST.fields_by_name['http_router_id']._options = None
  _GETHTTPROUTERREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _LISTHTTPROUTERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_size']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_token']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTHTTPROUTERSREQUEST.fields_by_name['filter']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DELETEHTTPROUTERREQUEST.fields_by_name['http_router_id']._options = None
  _DELETEHTTPROUTERREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEHTTPROUTERREQUEST_LABELSENTRY._options = None
  _UPDATEHTTPROUTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['http_router_id']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['name']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['description']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['labels']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _CREATEHTTPROUTERREQUEST_LABELSENTRY._options = None
  _CREATEHTTPROUTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEHTTPROUTERREQUEST.fields_by_name['folder_id']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEHTTPROUTERREQUEST.fields_by_name['name']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _CREATEHTTPROUTERREQUEST.fields_by_name['description']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEHTTPROUTERREQUEST.fields_by_name['labels']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['http_router_id']._options = None
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _HTTPROUTERSERVICE.methods_by_name['Get']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0022\0220/apploadbalancer/v1/httpRouters/{http_router_id}'
  _HTTPROUTERSERVICE.methods_by_name['List']._options = None
  _HTTPROUTERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/apploadbalancer/v1/httpRouters'
  _HTTPROUTERSERVICE.methods_by_name['Create']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*&\n\030CreateHttpRouterMetadata\022\nHttpRouter\202\323\344\223\002$\"\037/apploadbalancer/v1/httpRouters:\001*'
  _HTTPROUTERSERVICE.methods_by_name['Update']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*&\n\030UpdateHttpRouterMetadata\022\nHttpRouter\202\323\344\223\002520/apploadbalancer/v1/httpRouters/{http_router_id}:\001*'
  _HTTPROUTERSERVICE.methods_by_name['Delete']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteHttpRouterMetadata\022\025google.protobuf.Empty\202\323\344\223\0022*0/apploadbalancer/v1/httpRouters/{http_router_id}'
  _HTTPROUTERSERVICE.methods_by_name['ListOperations']._options = None
  _HTTPROUTERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002=\022;/apploadbalancer/v1/httpRouters/{http_router_id}/operations'
  _globals['_GETHTTPROUTERREQUEST']._serialized_start=366
  _globals['_GETHTTPROUTERREQUEST']._serialized_end=418
  _globals['_LISTHTTPROUTERSREQUEST']._serialized_start=421
  _globals['_LISTHTTPROUTERSREQUEST']._serialized_end=560
  _globals['_LISTHTTPROUTERSRESPONSE']._serialized_start=562
  _globals['_LISTHTTPROUTERSRESPONSE']._serialized_end=679
  _globals['_DELETEHTTPROUTERREQUEST']._serialized_start=681
  _globals['_DELETEHTTPROUTERREQUEST']._serialized_end=736
  _globals['_DELETEHTTPROUTERMETADATA']._serialized_start=738
  _globals['_DELETEHTTPROUTERMETADATA']._serialized_end=788
  _globals['_UPDATEHTTPROUTERREQUEST']._serialized_start=791
  _globals['_UPDATEHTTPROUTERREQUEST']._serialized_end=1329
  _globals['_UPDATEHTTPROUTERREQUEST_LABELSENTRY']._serialized_start=1278
  _globals['_UPDATEHTTPROUTERREQUEST_LABELSENTRY']._serialized_end=1323
  _globals['_UPDATEHTTPROUTERMETADATA']._serialized_start=1331
  _globals['_UPDATEHTTPROUTERMETADATA']._serialized_end=1381
  _globals['_CREATEHTTPROUTERREQUEST']._serialized_start=1384
  _globals['_CREATEHTTPROUTERREQUEST']._serialized_end=1868
  _globals['_CREATEHTTPROUTERREQUEST_LABELSENTRY']._serialized_start=1278
  _globals['_CREATEHTTPROUTERREQUEST_LABELSENTRY']._serialized_end=1323
  _globals['_CREATEHTTPROUTERMETADATA']._serialized_start=1870
  _globals['_CREATEHTTPROUTERMETADATA']._serialized_end=1920
  _globals['_LISTHTTPROUTEROPERATIONSREQUEST']._serialized_start=1923
  _globals['_LISTHTTPROUTEROPERATIONSREQUEST']._serialized_end=2056
  _globals['_LISTHTTPROUTEROPERATIONSRESPONSE']._serialized_start=2058
  _globals['_LISTHTTPROUTEROPERATIONSRESPONSE']._serialized_end=2172
  _globals['_HTTPROUTERSERVICE']._serialized_start=2175
  _globals['_HTTPROUTERSERVICE']._serialized_end=3358
# @@protoc_insertion_point(module_scope)
