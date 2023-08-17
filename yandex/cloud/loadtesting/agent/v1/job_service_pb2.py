# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/agent/v1/job_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/loadtesting/agent/v1/job_service.proto\x12!yandex.cloud.loadtesting.agent.v1\x1a\x1cgoogle/api/annotations.proto\"\xe4\x02\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\t\x12\x35\n\x04\x61mmo\x18\x03 \x01(\x0b\x32\'.yandex.cloud.loadtesting.agent.v1.File\x12\x1c\n\x14logging_log_group_id\x18\x04 \x01(\t\x12\x43\n\ttest_data\x18\x05 \x01(\x0b\x32\x30.yandex.cloud.loadtesting.agent.v1.StorageObject\x12\x46\n\x0c\x64\x61ta_payload\x18\x06 \x03(\x0b\x32\x30.yandex.cloud.loadtesting.agent.v1.TestDataEntry\x12_\n\x18\x61rtifact_upload_settings\x18\x07 \x01(\x0b\x32=.yandex.cloud.loadtesting.agent.v1.TestArtifactUploadSettings\"%\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"O\n\rStorageObject\x12\x1d\n\x15object_storage_bucket\x18\x01 \x01(\t\x12\x1f\n\x17object_storage_filename\x18\x02 \x01(\t\"}\n\rTestDataEntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cis_transient\x18\x02 \x01(\x08\x12H\n\x0estorage_object\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.loadtesting.agent.v1.StorageObject\"\x8c\x01\n\x1aTestArtifactUploadSettings\x12\x15\n\routput_bucket\x18\x01 \x01(\t\x12\x13\n\x0boutput_name\x18\x02 \x01(\t\x12\x12\n\nis_archive\x18\x03 \x01(\x08\x12\x16\n\x0e\x66ilter_include\x18\x04 \x03(\t\x12\x16\n\x0e\x66ilter_exclude\x18\x05 \x03(\t\"3\n\x13GetJobTransientFile\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"W\n\rGetJobRequest\x12\x1b\n\x13\x63ompute_instance_id\x18\x01 \x01(\t\x12\x19\n\x11\x61gent_instance_id\x18\x02 \x01(\t\x12\x0e\n\x06job_id\x18\x03 \x01(\t\"\xe9\x02\n\x15\x43laimJobStatusRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12R\n\x06status\x18\x02 \x01(\x0e\x32\x42.yandex.cloud.loadtesting.agent.v1.ClaimJobStatusRequest.JobStatus\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"\xdc\x01\n\tJobStatus\x12\x1a\n\x16JOB_STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPOST_PROCESS\x10\x01\x12\r\n\tINITIATED\x10\x02\x12\r\n\tPREPARING\x10\x03\x12\r\n\tNOT_FOUND\x10\x04\x12\x0b\n\x07RUNNING\x10\x05\x12\r\n\tFINISHING\x10\x06\x12\x0c\n\x08\x46INISHED\x10\x07\x12\x0b\n\x07STOPPED\x10\x08\x12\n\n\x06\x46\x41ILED\x10\t\x12\x0f\n\x0b\x41UTOSTOPPED\x10\n\x12 \n\x1cWAITING_FOR_A_COMMAND_TO_RUN\x10\x0b\"&\n\x16\x43laimJobStatusResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\"\"\n\x10JobSignalRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\xc9\x01\n\x11JobSignalResponse\x12K\n\x06signal\x18\x01 \x01(\x0e\x32;.yandex.cloud.loadtesting.agent.v1.JobSignalResponse.Signal\x12\x15\n\rwait_duration\x18\x02 \x01(\x01\x12\x0e\n\x06run_in\x18\x03 \x01(\x01\"@\n\x06Signal\x12\x16\n\x12SIGNAL_UNSPECIFIED\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x08\n\x04WAIT\x10\x02\x12\n\n\x06RUN_IN\x10\x03\x32\xfb\x05\n\nJobService\x12\xbe\x01\n\x0b\x43laimStatus\x12\x38.yandex.cloud.loadtesting.agent.v1.ClaimJobStatusRequest\x1a\x39.yandex.cloud.loadtesting.agent.v1.ClaimJobStatusResponse\":\x82\xd3\xe4\x93\x02\x34\"//loadtesting/agent/v1/jobs/{job_id}/claimStatus:\x01*\x12\xc7\x01\n\x03Get\x12\x30.yandex.cloud.loadtesting.agent.v1.GetJobRequest\x1a&.yandex.cloud.loadtesting.agent.v1.Job\"f\x82\xd3\xe4\x93\x02`\x12\x37/loadtesting/agent/v1/agents/{agent_instance_id}/getJobZ%\x12#/loadtesting/agent/v1/jobs/{job_id}\x12\xad\x01\n\tGetSignal\x12\x33.yandex.cloud.loadtesting.agent.v1.JobSignalRequest\x1a\x34.yandex.cloud.loadtesting.agent.v1.JobSignalResponse\"5\x82\xd3\xe4\x93\x02/\x12-/loadtesting/agent/v1/jobs/{job_id}/getSignal\x12\xb1\x01\n\x10GetTransientFile\x12\x36.yandex.cloud.loadtesting.agent.v1.GetJobTransientFile\x1a\'.yandex.cloud.loadtesting.agent.v1.File\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/loadtesting/agent/v1/jobs/{job_id}/getTransientFileBt\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.agent.v1.job_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agent'
  _JOBSERVICE.methods_by_name['ClaimStatus']._options = None
  _JOBSERVICE.methods_by_name['ClaimStatus']._serialized_options = b'\202\323\344\223\0024\"//loadtesting/agent/v1/jobs/{job_id}/claimStatus:\001*'
  _JOBSERVICE.methods_by_name['Get']._options = None
  _JOBSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002`\0227/loadtesting/agent/v1/agents/{agent_instance_id}/getJobZ%\022#/loadtesting/agent/v1/jobs/{job_id}'
  _JOBSERVICE.methods_by_name['GetSignal']._options = None
  _JOBSERVICE.methods_by_name['GetSignal']._serialized_options = b'\202\323\344\223\002/\022-/loadtesting/agent/v1/jobs/{job_id}/getSignal'
  _JOBSERVICE.methods_by_name['GetTransientFile']._options = None
  _JOBSERVICE.methods_by_name['GetTransientFile']._serialized_options = b'\202\323\344\223\0026\0224/loadtesting/agent/v1/jobs/{job_id}/getTransientFile'
  _globals['_JOB']._serialized_start=121
  _globals['_JOB']._serialized_end=477
  _globals['_FILE']._serialized_start=479
  _globals['_FILE']._serialized_end=516
  _globals['_STORAGEOBJECT']._serialized_start=518
  _globals['_STORAGEOBJECT']._serialized_end=597
  _globals['_TESTDATAENTRY']._serialized_start=599
  _globals['_TESTDATAENTRY']._serialized_end=724
  _globals['_TESTARTIFACTUPLOADSETTINGS']._serialized_start=727
  _globals['_TESTARTIFACTUPLOADSETTINGS']._serialized_end=867
  _globals['_GETJOBTRANSIENTFILE']._serialized_start=869
  _globals['_GETJOBTRANSIENTFILE']._serialized_end=920
  _globals['_GETJOBREQUEST']._serialized_start=922
  _globals['_GETJOBREQUEST']._serialized_end=1009
  _globals['_CLAIMJOBSTATUSREQUEST']._serialized_start=1012
  _globals['_CLAIMJOBSTATUSREQUEST']._serialized_end=1373
  _globals['_CLAIMJOBSTATUSREQUEST_JOBSTATUS']._serialized_start=1153
  _globals['_CLAIMJOBSTATUSREQUEST_JOBSTATUS']._serialized_end=1373
  _globals['_CLAIMJOBSTATUSRESPONSE']._serialized_start=1375
  _globals['_CLAIMJOBSTATUSRESPONSE']._serialized_end=1413
  _globals['_JOBSIGNALREQUEST']._serialized_start=1415
  _globals['_JOBSIGNALREQUEST']._serialized_end=1449
  _globals['_JOBSIGNALRESPONSE']._serialized_start=1452
  _globals['_JOBSIGNALRESPONSE']._serialized_end=1653
  _globals['_JOBSIGNALRESPONSE_SIGNAL']._serialized_start=1589
  _globals['_JOBSIGNALRESPONSE_SIGNAL']._serialized_end=1653
  _globals['_JOBSERVICE']._serialized_start=1656
  _globals['_JOBSERVICE']._serialized_end=2419
# @@protoc_insertion_point(module_scope)
