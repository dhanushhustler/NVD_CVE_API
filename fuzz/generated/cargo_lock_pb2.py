# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cargo_lock.proto
# Protobuf Python Version: 4.24.0-main
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61rgo_lock.proto\"\xa7\x02\n\tCargoLock\x12$\n\x08packages\x18\x01 \x03(\x0b\x32\x12.CargoLock.Package\x1a\x99\x01\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x06source\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x63hecksum\x18\x04 \x01(\tH\x01\x88\x01\x01\x12+\n\ndependency\x18\x05 \x03(\x0b\x32\x17.CargoLock.DependenciesB\t\n\x07_sourceB\x0b\n\t_checksum\x1aX\n\x0c\x44\x65pendencies\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x07version\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03url\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_versionB\x06\n\x04_urlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cargo_lock_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CARGOLOCK']._serialized_start=21
  _globals['_CARGOLOCK']._serialized_end=316
  _globals['_CARGOLOCK_PACKAGE']._serialized_start=73
  _globals['_CARGOLOCK_PACKAGE']._serialized_end=226
  _globals['_CARGOLOCK_DEPENDENCIES']._serialized_start=228
  _globals['_CARGOLOCK_DEPENDENCIES']._serialized_end=316
# @@protoc_insertion_point(module_scope)