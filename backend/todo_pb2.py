# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\"[\n\x04todo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64line\x18\x04 \x01(\t\x12\x11\n\tcompleted\x18\x05 \x01(\x08\" \n\x08todoList\x12\x14\n\x05todos\x18\x01 \x03(\x0b\x32\x05.todo\"\x1a\n\ttodoTitle\x12\r\n\x05title\x18\x01 \x01(\t\"\x14\n\x06todoId\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xa6\x01\n\x0btodoService\x12\x19\n\x07\x41\x64\x64todo\x12\x05.todo\x1a\x05.todo\"\x00\x12\x1d\n\x06GetAll\x12\x06.Empty\x1a\t.todoList\"\x00\x12\x1e\n\x07Gettodo\x12\n.todoTitle\x1a\x05.todo\"\x00\x12\x1c\n\nUpdatetodo\x12\x05.todo\x1a\x05.todo\"\x00\x12\x1f\n\nDeletetodo\x12\x07.todoId\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TODO']._serialized_start=14
  _globals['_TODO']._serialized_end=105
  _globals['_TODOLIST']._serialized_start=107
  _globals['_TODOLIST']._serialized_end=139
  _globals['_TODOTITLE']._serialized_start=141
  _globals['_TODOTITLE']._serialized_end=167
  _globals['_TODOID']._serialized_start=169
  _globals['_TODOID']._serialized_end=189
  _globals['_EMPTY']._serialized_start=191
  _globals['_EMPTY']._serialized_end=198
  _globals['_TODOSERVICE']._serialized_start=201
  _globals['_TODOSERVICE']._serialized_end=367
# @@protoc_insertion_point(module_scope)
