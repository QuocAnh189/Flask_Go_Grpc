# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: countries.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'countries.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63ountries.proto\x12\tcountries\"\x1e\n\x0e\x43ountryRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"h\n\x0f\x43ountryResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nalpha2Code\x18\x02 \x01(\t\x12\x12\n\nalpha3Code\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61pital\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t2L\n\x07\x43ountry\x12\x41\n\x06search\x12\x19.countries.CountryRequest\x1a\x1a.countries.CountryResponse\"\x00\x42\x12Z\x10server/countriesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'countries_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\020server/countries'
  _globals['_COUNTRYREQUEST']._serialized_start=30
  _globals['_COUNTRYREQUEST']._serialized_end=60
  _globals['_COUNTRYRESPONSE']._serialized_start=62
  _globals['_COUNTRYRESPONSE']._serialized_end=166
  _globals['_COUNTRY']._serialized_start=168
  _globals['_COUNTRY']._serialized_end=244
# @@protoc_insertion_point(module_scope)
