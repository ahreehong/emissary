# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getambassador.io/v2/Host.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='getambassador.io/v2/Host.proto',
  package='getambassador.io.v2',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1egetambassador.io/v2/Host.proto\x12\x13getambassador.io.v2\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a\"k8s.io/api/core/v1/generated.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xf8\x03\n\x08HostSpec\x12\x15\n\rambassador_id\x18\x01 \x03(\t\x12\x12\n\ngeneration\x18\x02 \x01(\x05\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x45\n\x08selector\x18\x04 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12;\n\x0c\x61\x63meProvider\x18\x05 \x01(\x0b\x32%.getambassador.io.v2.ACMEProviderSpec\x12;\n\ttlsSecret\x18\x06 \x01(\x0b\x32(.k8s.io.api.core.v1.LocalObjectReference\x12\x39\n\rrequestPolicy\x18\x07 \x01(\x0b\x32\".getambassador.io.v2.RequestPolicy\x12\x37\n\npreviewUrl\x18\x08 \x01(\x0b\x32#.getambassador.io.v2.PreviewURLSpec\x12>\n\ntlsContext\x18\t \x01(\x0b\x32(.k8s.io.api.core.v1.LocalObjectReferenceH\x00\x12-\n\x03tls\x18\n \x01(\x0b\x32\x1e.getambassador.io.v2.TLSConfigH\x00\x42\x0b\n\ttlsConfig\"\xf0\x02\n\nHostStatus\x12K\n\x14tlsCertificateSource\x18\x01 \x01(\x0e\x32-.getambassador.io.v2.HostTLSCertificateSource\x12-\n\x05state\x18\x02 \x01(\x0e\x32\x1e.getambassador.io.v2.HostState\x12\x36\n\x0ephaseCompleted\x18\x03 \x01(\x0e\x32\x1e.getambassador.io.v2.HostPhase\x12\x34\n\x0cphasePending\x18\x04 \x01(\x0e\x32\x1e.getambassador.io.v2.HostPhase\x12\x13\n\x0b\x65rrorReason\x18\x05 \x01(\t\x12\x32\n\x0e\x65rrorTimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0c\x65rrorBackoff\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x8e\x01\n\x10\x41\x43MEProviderSpec\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x42\n\x10privateKeySecret\x18\x03 \x01(\x0b\x32(.k8s.io.api.core.v1.LocalObjectReference\x12\x14\n\x0cregistration\x18\x04 \x01(\t\"\xa7\x02\n\tTLSConfig\x12\x17\n\x0f\x63\x65rt_chain_file\x18\x01 \x01(\t\x12\x18\n\x10private_key_file\x18\x02 \x01(\t\x12\x11\n\tca_secret\x18\x03 \x01(\t\x12\x19\n\x11\x63\x61\x63\x65rt_chain_file\x18\x04 \x01(\t\x12\x16\n\x0e\x61lpn_protocols\x18\x05 \x01(\t\x12\x15\n\rcert_required\x18\x06 \x01(\x08\x12\x17\n\x0fmin_tls_version\x18\x07 \x01(\t\x12\x17\n\x0fmax_tls_version\x18\x08 \x01(\t\x12\x15\n\rcipher_suites\x18\t \x03(\t\x12\x13\n\x0b\x65\x63\x64h_curves\x18\n \x03(\t\x12\x1f\n\x17redirect_cleartext_from\x18\x0b \x01(\x05\x12\x0b\n\x03sni\x18\x0c \x01(\t\"M\n\rRequestPolicy\x12<\n\x08insecure\x18\x01 \x01(\x0b\x32*.getambassador.io.v2.InsecureRequestPolicy\"k\n\x15InsecureRequestPolicy\x12:\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32*.getambassador.io.v2.InsecureRequestAction\x12\x16\n\x0e\x61\x64\x64itionalPort\x18\x02 \x01(\x05\"T\n\x0ePreviewURLSpec\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.getambassador.io.v2.PreviewURLType*F\n\x18HostTLSCertificateSource\x12\x0b\n\x07Unknown\x10\x00\x12\x08\n\x04None\x10\x01\x12\t\n\x05Other\x10\x02\x12\x08\n\x04\x41\x43ME\x10\x03*;\n\tHostState\x12\x0b\n\x07Initial\x10\x00\x12\x0b\n\x07Pending\x10\x01\x12\t\n\x05Ready\x10\x02\x12\t\n\x05\x45rror\x10\x03*|\n\tHostPhase\x12\x06\n\x02NA\x10\x00\x12\x12\n\x0e\x44\x65\x66\x61ultsFilled\x10\x01\x12\x1d\n\x19\x41\x43MEUserPrivateKeyCreated\x10\x02\x12\x16\n\x12\x41\x43MEUserRegistered\x10\x03\x12\x1c\n\x18\x41\x43MECertificateChallenge\x10\x04*<\n\x15InsecureRequestAction\x12\x0c\n\x08Redirect\x10\x00\x12\n\n\x06Reject\x10\x01\x12\t\n\x05Route\x10\x02*\x1a\n\x0ePreviewURLType\x12\x08\n\x04Path\x10\x00\x62\x06proto3')
  ,
  dependencies=[k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2.DESCRIPTOR,k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_HOSTTLSCERTIFICATESOURCE = _descriptor.EnumDescriptor(
  name='HostTLSCertificateSource',
  full_name='getambassador.io.v2.HostTLSCertificateSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='None', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Other', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACME', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1805,
  serialized_end=1875,
)
_sym_db.RegisterEnumDescriptor(_HOSTTLSCERTIFICATESOURCE)

HostTLSCertificateSource = enum_type_wrapper.EnumTypeWrapper(_HOSTTLSCERTIFICATESOURCE)
_HOSTSTATE = _descriptor.EnumDescriptor(
  name='HostState',
  full_name='getambassador.io.v2.HostState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Initial', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pending', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ready', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Error', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1877,
  serialized_end=1936,
)
_sym_db.RegisterEnumDescriptor(_HOSTSTATE)

HostState = enum_type_wrapper.EnumTypeWrapper(_HOSTSTATE)
_HOSTPHASE = _descriptor.EnumDescriptor(
  name='HostPhase',
  full_name='getambassador.io.v2.HostPhase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DefaultsFilled', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACMEUserPrivateKeyCreated', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACMEUserRegistered', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACMECertificateChallenge', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1938,
  serialized_end=2062,
)
_sym_db.RegisterEnumDescriptor(_HOSTPHASE)

HostPhase = enum_type_wrapper.EnumTypeWrapper(_HOSTPHASE)
_INSECUREREQUESTACTION = _descriptor.EnumDescriptor(
  name='InsecureRequestAction',
  full_name='getambassador.io.v2.InsecureRequestAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Redirect', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Reject', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Route', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2064,
  serialized_end=2124,
)
_sym_db.RegisterEnumDescriptor(_INSECUREREQUESTACTION)

InsecureRequestAction = enum_type_wrapper.EnumTypeWrapper(_INSECUREREQUESTACTION)
_PREVIEWURLTYPE = _descriptor.EnumDescriptor(
  name='PreviewURLType',
  full_name='getambassador.io.v2.PreviewURLType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Path', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2126,
  serialized_end=2152,
)
_sym_db.RegisterEnumDescriptor(_PREVIEWURLTYPE)

PreviewURLType = enum_type_wrapper.EnumTypeWrapper(_PREVIEWURLTYPE)
Unknown = 0
globals()['None'] = 1
Other = 2
ACME = 3
Initial = 0
Pending = 1
Ready = 2
Error = 3
NA = 0
DefaultsFilled = 1
ACMEUserPrivateKeyCreated = 2
ACMEUserRegistered = 3
ACMECertificateChallenge = 4
Redirect = 0
Reject = 1
Route = 2
Path = 0



_HOSTSPEC = _descriptor.Descriptor(
  name='HostSpec',
  full_name='getambassador.io.v2.HostSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ambassador_id', full_name='getambassador.io.v2.HostSpec.ambassador_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation', full_name='getambassador.io.v2.HostSpec.generation', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='getambassador.io.v2.HostSpec.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='getambassador.io.v2.HostSpec.selector', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acmeProvider', full_name='getambassador.io.v2.HostSpec.acmeProvider', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tlsSecret', full_name='getambassador.io.v2.HostSpec.tlsSecret', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestPolicy', full_name='getambassador.io.v2.HostSpec.requestPolicy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previewUrl', full_name='getambassador.io.v2.HostSpec.previewUrl', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tlsContext', full_name='getambassador.io.v2.HostSpec.tlsContext', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls', full_name='getambassador.io.v2.HostSpec.tls', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='tlsConfig', full_name='getambassador.io.v2.HostSpec.tlsConfig',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=211,
  serialized_end=715,
)


_HOSTSTATUS = _descriptor.Descriptor(
  name='HostStatus',
  full_name='getambassador.io.v2.HostStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tlsCertificateSource', full_name='getambassador.io.v2.HostStatus.tlsCertificateSource', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='getambassador.io.v2.HostStatus.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phaseCompleted', full_name='getambassador.io.v2.HostStatus.phaseCompleted', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phasePending', full_name='getambassador.io.v2.HostStatus.phasePending', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorReason', full_name='getambassador.io.v2.HostStatus.errorReason', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorTimestamp', full_name='getambassador.io.v2.HostStatus.errorTimestamp', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorBackoff', full_name='getambassador.io.v2.HostStatus.errorBackoff', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=718,
  serialized_end=1086,
)


_ACMEPROVIDERSPEC = _descriptor.Descriptor(
  name='ACMEProviderSpec',
  full_name='getambassador.io.v2.ACMEProviderSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='getambassador.io.v2.ACMEProviderSpec.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='getambassador.io.v2.ACMEProviderSpec.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='privateKeySecret', full_name='getambassador.io.v2.ACMEProviderSpec.privateKeySecret', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registration', full_name='getambassador.io.v2.ACMEProviderSpec.registration', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1089,
  serialized_end=1231,
)


_TLSCONFIG = _descriptor.Descriptor(
  name='TLSConfig',
  full_name='getambassador.io.v2.TLSConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cert_chain_file', full_name='getambassador.io.v2.TLSConfig.cert_chain_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_key_file', full_name='getambassador.io.v2.TLSConfig.private_key_file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ca_secret', full_name='getambassador.io.v2.TLSConfig.ca_secret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacert_chain_file', full_name='getambassador.io.v2.TLSConfig.cacert_chain_file', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alpn_protocols', full_name='getambassador.io.v2.TLSConfig.alpn_protocols', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cert_required', full_name='getambassador.io.v2.TLSConfig.cert_required', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_tls_version', full_name='getambassador.io.v2.TLSConfig.min_tls_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_tls_version', full_name='getambassador.io.v2.TLSConfig.max_tls_version', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cipher_suites', full_name='getambassador.io.v2.TLSConfig.cipher_suites', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ecdh_curves', full_name='getambassador.io.v2.TLSConfig.ecdh_curves', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redirect_cleartext_from', full_name='getambassador.io.v2.TLSConfig.redirect_cleartext_from', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sni', full_name='getambassador.io.v2.TLSConfig.sni', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1234,
  serialized_end=1529,
)


_REQUESTPOLICY = _descriptor.Descriptor(
  name='RequestPolicy',
  full_name='getambassador.io.v2.RequestPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='insecure', full_name='getambassador.io.v2.RequestPolicy.insecure', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1531,
  serialized_end=1608,
)


_INSECUREREQUESTPOLICY = _descriptor.Descriptor(
  name='InsecureRequestPolicy',
  full_name='getambassador.io.v2.InsecureRequestPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='getambassador.io.v2.InsecureRequestPolicy.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additionalPort', full_name='getambassador.io.v2.InsecureRequestPolicy.additionalPort', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1610,
  serialized_end=1717,
)


_PREVIEWURLSPEC = _descriptor.Descriptor(
  name='PreviewURLSpec',
  full_name='getambassador.io.v2.PreviewURLSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='getambassador.io.v2.PreviewURLSpec.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='getambassador.io.v2.PreviewURLSpec.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1719,
  serialized_end=1803,
)

_HOSTSPEC.fields_by_name['selector'].message_type = k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2._LABELSELECTOR
_HOSTSPEC.fields_by_name['acmeProvider'].message_type = _ACMEPROVIDERSPEC
_HOSTSPEC.fields_by_name['tlsSecret'].message_type = k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2._LOCALOBJECTREFERENCE
_HOSTSPEC.fields_by_name['requestPolicy'].message_type = _REQUESTPOLICY
_HOSTSPEC.fields_by_name['previewUrl'].message_type = _PREVIEWURLSPEC
_HOSTSPEC.fields_by_name['tlsContext'].message_type = k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2._LOCALOBJECTREFERENCE
_HOSTSPEC.fields_by_name['tls'].message_type = _TLSCONFIG
_HOSTSPEC.oneofs_by_name['tlsConfig'].fields.append(
  _HOSTSPEC.fields_by_name['tlsContext'])
_HOSTSPEC.fields_by_name['tlsContext'].containing_oneof = _HOSTSPEC.oneofs_by_name['tlsConfig']
_HOSTSPEC.oneofs_by_name['tlsConfig'].fields.append(
  _HOSTSPEC.fields_by_name['tls'])
_HOSTSPEC.fields_by_name['tls'].containing_oneof = _HOSTSPEC.oneofs_by_name['tlsConfig']
_HOSTSTATUS.fields_by_name['tlsCertificateSource'].enum_type = _HOSTTLSCERTIFICATESOURCE
_HOSTSTATUS.fields_by_name['state'].enum_type = _HOSTSTATE
_HOSTSTATUS.fields_by_name['phaseCompleted'].enum_type = _HOSTPHASE
_HOSTSTATUS.fields_by_name['phasePending'].enum_type = _HOSTPHASE
_HOSTSTATUS.fields_by_name['errorTimestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP # type: ignore[attr-defined]
_HOSTSTATUS.fields_by_name['errorBackoff'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION # type: ignore[attr-defined]
_ACMEPROVIDERSPEC.fields_by_name['privateKeySecret'].message_type = k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2._LOCALOBJECTREFERENCE
_REQUESTPOLICY.fields_by_name['insecure'].message_type = _INSECUREREQUESTPOLICY
_INSECUREREQUESTPOLICY.fields_by_name['action'].enum_type = _INSECUREREQUESTACTION
_PREVIEWURLSPEC.fields_by_name['type'].enum_type = _PREVIEWURLTYPE
DESCRIPTOR.message_types_by_name['HostSpec'] = _HOSTSPEC
DESCRIPTOR.message_types_by_name['HostStatus'] = _HOSTSTATUS
DESCRIPTOR.message_types_by_name['ACMEProviderSpec'] = _ACMEPROVIDERSPEC
DESCRIPTOR.message_types_by_name['TLSConfig'] = _TLSCONFIG
DESCRIPTOR.message_types_by_name['RequestPolicy'] = _REQUESTPOLICY
DESCRIPTOR.message_types_by_name['InsecureRequestPolicy'] = _INSECUREREQUESTPOLICY
DESCRIPTOR.message_types_by_name['PreviewURLSpec'] = _PREVIEWURLSPEC
DESCRIPTOR.enum_types_by_name['HostTLSCertificateSource'] = _HOSTTLSCERTIFICATESOURCE
DESCRIPTOR.enum_types_by_name['HostState'] = _HOSTSTATE
DESCRIPTOR.enum_types_by_name['HostPhase'] = _HOSTPHASE
DESCRIPTOR.enum_types_by_name['InsecureRequestAction'] = _INSECUREREQUESTACTION
DESCRIPTOR.enum_types_by_name['PreviewURLType'] = _PREVIEWURLTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HostSpec = _reflection.GeneratedProtocolMessageType('HostSpec', (_message.Message,), {
  'DESCRIPTOR' : _HOSTSPEC,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.HostSpec)
  })
_sym_db.RegisterMessage(HostSpec)

HostStatus = _reflection.GeneratedProtocolMessageType('HostStatus', (_message.Message,), {
  'DESCRIPTOR' : _HOSTSTATUS,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.HostStatus)
  })
_sym_db.RegisterMessage(HostStatus)

ACMEProviderSpec = _reflection.GeneratedProtocolMessageType('ACMEProviderSpec', (_message.Message,), {
  'DESCRIPTOR' : _ACMEPROVIDERSPEC,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.ACMEProviderSpec)
  })
_sym_db.RegisterMessage(ACMEProviderSpec)

TLSConfig = _reflection.GeneratedProtocolMessageType('TLSConfig', (_message.Message,), {
  'DESCRIPTOR' : _TLSCONFIG,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.TLSConfig)
  })
_sym_db.RegisterMessage(TLSConfig)

RequestPolicy = _reflection.GeneratedProtocolMessageType('RequestPolicy', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPOLICY,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.RequestPolicy)
  })
_sym_db.RegisterMessage(RequestPolicy)

InsecureRequestPolicy = _reflection.GeneratedProtocolMessageType('InsecureRequestPolicy', (_message.Message,), {
  'DESCRIPTOR' : _INSECUREREQUESTPOLICY,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.InsecureRequestPolicy)
  })
_sym_db.RegisterMessage(InsecureRequestPolicy)

PreviewURLSpec = _reflection.GeneratedProtocolMessageType('PreviewURLSpec', (_message.Message,), {
  'DESCRIPTOR' : _PREVIEWURLSPEC,
  '__module__' : 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:getambassador.io.v2.PreviewURLSpec)
  })
_sym_db.RegisterMessage(PreviewURLSpec)


# @@protoc_insertion_point(module_scope)
