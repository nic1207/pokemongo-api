# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/UpgradePokemonMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/UpgradePokemonMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nCPOGOProtos/Networking/Requests/Messages/UpgradePokemonMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"+\n\x15UpgradePokemonMessage\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPGRADEPOKEMONMESSAGE = _descriptor.Descriptor(
  name='UpgradePokemonMessage',
  full_name='POGOProtos.Networking.Requests.Messages.UpgradePokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Networking.Requests.Messages.UpgradePokemonMessage.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['UpgradePokemonMessage'] = _UPGRADEPOKEMONMESSAGE

UpgradePokemonMessage = _reflection.GeneratedProtocolMessageType('UpgradePokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADEPOKEMONMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.UpgradePokemonMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.UpgradePokemonMessage)
  ))
_sym_db.RegisterMessage(UpgradePokemonMessage)


# @@protoc_insertion_point(module_scope)
