# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: composer_lock.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13\x63omposer_lock.proto"\xe9\x04\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x06source\x18\x03 \x01(\x0b\x32\x07.Source\x12\x1b\n\x04\x64ist\x18\x04 \x01(\x0b\x32\r.Distribution\x12&\n\x07require\x18\x05 \x03(\x0b\x32\x15.Package.RequireEntry\x12-\n\x0brequire_dev\x18\x06 \x03(\x0b\x32\x18.Package.RequireDevEntry\x12\x0b\n\x03\x62in\x18\x07 \x03(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12(\n\x08\x61utoload\x18\t \x03(\x0b\x32\x16.Package.AutoloadEntry\x12\x18\n\x10notification_url\x18\n \x01(\t\x12\x0f\n\x07license\x18\x0b \x03(\t\x12\x18\n\x07\x61uthors\x18\x0c \x03(\x0b\x32\x07.Author\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\t\x12&\n\x07support\x18\x0e \x03(\x0b\x32\x15.Package.SupportEntry\x12\x19\n\x07\x66unding\x18\x0f \x03(\x0b\x32\x08.Funding\x12\x0c\n\x04time\x18\x10 \x01(\t\x1a.\n\x0cRequireEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fRequireDevEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rAutoloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0cSupportEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"6\n\x06Source\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t"L\n\x0c\x44istribution\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12\x0e\n\x06shasum\x18\x04 \x01(\t"3\n\x06\x41uthor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t"$\n\x07\x46unding\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t"\x93\x04\n\x0c\x43omposerLock\x12\x14\n\x0c\x63ontent_hash\x18\x01 \x01(\t\x12\x1a\n\x08packages\x18\x02 \x03(\x0b\x32\x08.Package\x12\x1e\n\x0cpackages_dev\x18\x03 \x03(\x0b\x32\x08.Package\x12\x0f\n\x07\x61liases\x18\x04 \x03(\t\x12\x19\n\x11minimum_stability\x18\x05 \x01(\t\x12:\n\x0fstability_flags\x18\x06 \x03(\x0b\x32!.ComposerLock.StabilityFlagsEntry\x12\x15\n\rprefer_stable\x18\x07 \x01(\x08\x12\x15\n\rprefer_lowest\x18\x08 \x01(\x08\x12-\n\x08platform\x18\t \x03(\x0b\x32\x1b.ComposerLock.PlatformEntry\x12\x34\n\x0cplatform_dev\x18\n \x03(\x0b\x32\x1e.ComposerLock.PlatformDevEntry\x12\x1a\n\x12plugin_api_version\x18\x0b \x01(\t\x1a\x35\n\x13StabilityFlagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rPlatformEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10PlatformDevEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "composer_lock_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS is False:
    DESCRIPTOR._options = None
    _globals["_PACKAGE_REQUIREENTRY"]._options = None
    _globals["_PACKAGE_REQUIREENTRY"]._serialized_options = b"8\001"
    _globals["_PACKAGE_REQUIREDEVENTRY"]._options = None
    _globals["_PACKAGE_REQUIREDEVENTRY"]._serialized_options = b"8\001"
    _globals["_PACKAGE_AUTOLOADENTRY"]._options = None
    _globals["_PACKAGE_AUTOLOADENTRY"]._serialized_options = b"8\001"
    _globals["_PACKAGE_SUPPORTENTRY"]._options = None
    _globals["_PACKAGE_SUPPORTENTRY"]._serialized_options = b"8\001"
    _globals["_COMPOSERLOCK_STABILITYFLAGSENTRY"]._options = None
    _globals["_COMPOSERLOCK_STABILITYFLAGSENTRY"]._serialized_options = b"8\001"
    _globals["_COMPOSERLOCK_PLATFORMENTRY"]._options = None
    _globals["_COMPOSERLOCK_PLATFORMENTRY"]._serialized_options = b"8\001"
    _globals["_COMPOSERLOCK_PLATFORMDEVENTRY"]._options = None
    _globals["_COMPOSERLOCK_PLATFORMDEVENTRY"]._serialized_options = b"8\001"
    _globals["_PACKAGE"]._serialized_start = 24
    _globals["_PACKAGE"]._serialized_end = 641
    _globals["_PACKAGE_REQUIREENTRY"]._serialized_start = 447
    _globals["_PACKAGE_REQUIREENTRY"]._serialized_end = 493
    _globals["_PACKAGE_REQUIREDEVENTRY"]._serialized_start = 495
    _globals["_PACKAGE_REQUIREDEVENTRY"]._serialized_end = 544
    _globals["_PACKAGE_AUTOLOADENTRY"]._serialized_start = 546
    _globals["_PACKAGE_AUTOLOADENTRY"]._serialized_end = 593
    _globals["_PACKAGE_SUPPORTENTRY"]._serialized_start = 595
    _globals["_PACKAGE_SUPPORTENTRY"]._serialized_end = 641
    _globals["_SOURCE"]._serialized_start = 643
    _globals["_SOURCE"]._serialized_end = 697
    _globals["_DISTRIBUTION"]._serialized_start = 699
    _globals["_DISTRIBUTION"]._serialized_end = 775
    _globals["_AUTHOR"]._serialized_start = 777
    _globals["_AUTHOR"]._serialized_end = 828
    _globals["_FUNDING"]._serialized_start = 830
    _globals["_FUNDING"]._serialized_end = 866
    _globals["_COMPOSERLOCK"]._serialized_start = 869
    _globals["_COMPOSERLOCK"]._serialized_end = 1400
    _globals["_COMPOSERLOCK_STABILITYFLAGSENTRY"]._serialized_start = 1246
    _globals["_COMPOSERLOCK_STABILITYFLAGSENTRY"]._serialized_end = 1299
    _globals["_COMPOSERLOCK_PLATFORMENTRY"]._serialized_start = 1301
    _globals["_COMPOSERLOCK_PLATFORMENTRY"]._serialized_end = 1348
    _globals["_COMPOSERLOCK_PLATFORMDEVENTRY"]._serialized_start = 1350
    _globals["_COMPOSERLOCK_PLATFORMDEVENTRY"]._serialized_end = 1400
# @@protoc_insertion_point(module_scope)