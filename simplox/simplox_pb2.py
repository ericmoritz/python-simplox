# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='simplox.proto',
  package='simplox',
  serialized_pb='\n\rsimplox.proto\x12\x07simplox\"E\n\x0cMultiRequest\x12\"\n\x08requests\x18\x01 \x03(\x0b\x32\x10.simplox.Request\x12\x11\n\tbatch_key\x18\x02 \x01(\x0c\"~\n\x07Request\x12\x0b\n\x03url\x18\x01 \x02(\x0c\x12\x13\n\x06method\x18\x02 \x01(\x0c:\x03get\x12 \n\x07headers\x18\x03 \x03(\x0b\x32\x0f.simplox.Header\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x05 \x01(\x0c\x12\x0b\n\x03key\x18\x06 \x01(\x0c\"$\n\x06Header\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x9d\x01\n\x08Response\x12\x0e\n\x06status\x18\x01 \x02(\x0c\x12\x0b\n\x03url\x18\x02 \x02(\x0c\x12 \n\x07headers\x18\x03 \x03(\x0b\x32\x0f.simplox.Header\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c\x12\x0b\n\x03key\x18\x05 \x01(\x0c\x12\x14\n\x0crequest_time\x18\x06 \x01(\r\x12\x0e\n\x06method\x18\x07 \x01(\x0c\x12\x11\n\tbatch_key\x18\x08 \x01(\x0c')




_MULTIREQUEST = descriptor.Descriptor(
  name='MultiRequest',
  full_name='simplox.MultiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='requests', full_name='simplox.MultiRequest.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='batch_key', full_name='simplox.MultiRequest.batch_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=26,
  serialized_end=95,
)


_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='simplox.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='url', full_name='simplox.Request.url', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method', full_name='simplox.Request.method', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value="get",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='headers', full_name='simplox.Request.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content_type', full_name='simplox.Request.content_type', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='body', full_name='simplox.Request.body', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='simplox.Request.key', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=97,
  serialized_end=223,
)


_HEADER = descriptor.Descriptor(
  name='Header',
  full_name='simplox.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='simplox.Header.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='simplox.Header.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=225,
  serialized_end=261,
)


_RESPONSE = descriptor.Descriptor(
  name='Response',
  full_name='simplox.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='simplox.Response.status', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='simplox.Response.url', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='headers', full_name='simplox.Response.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='body', full_name='simplox.Response.body', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='simplox.Response.key', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_time', full_name='simplox.Response.request_time', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method', full_name='simplox.Response.method', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='batch_key', full_name='simplox.Response.batch_key', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=264,
  serialized_end=421,
)

_MULTIREQUEST.fields_by_name['requests'].message_type = _REQUEST
_REQUEST.fields_by_name['headers'].message_type = _HEADER
_RESPONSE.fields_by_name['headers'].message_type = _HEADER
DESCRIPTOR.message_types_by_name['MultiRequest'] = _MULTIREQUEST
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

class MultiRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MULTIREQUEST
  
  # @@protoc_insertion_point(class_scope:simplox.MultiRequest)

class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST
  
  # @@protoc_insertion_point(class_scope:simplox.Request)

class Header(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADER
  
  # @@protoc_insertion_point(class_scope:simplox.Header)

class Response(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE
  
  # @@protoc_insertion_point(class_scope:simplox.Response)

# @@protoc_insertion_point(module_scope)
