# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0emessages.proto\x1a\x0cnanopb.proto\"\x86\x03\n\x0b\x44\x61taMessage\x12\n\n\x02id\x18\x01 \x02(\r\x12\x15\n\rsample_number\x18\x02 \x02(\r\x12\x11\n\tunix_time\x18\x03 \x02(\r\x12\x17\n\x0funix_time_nsecs\x18\x04 \x02(\r\x12\x18\n\x10time_uncertainty\x18\x05 \x02(\r\x12\x0f\n\x07\x44\x61ta_01\x18\x06 \x02(\x02\x12\x0f\n\x07\x44\x61ta_02\x18\x07 \x01(\x02\x12\x0f\n\x07\x44\x61ta_03\x18\x08 \x01(\x02\x12\x0f\n\x07\x44\x61ta_04\x18\t \x01(\x02\x12\x0f\n\x07\x44\x61ta_05\x18\n \x01(\x02\x12\x0f\n\x07\x44\x61ta_06\x18\x0b \x01(\x02\x12\x0f\n\x07\x44\x61ta_07\x18\x0c \x01(\x02\x12\x0f\n\x07\x44\x61ta_08\x18\r \x01(\x02\x12\x0f\n\x07\x44\x61ta_09\x18\x0e \x01(\x02\x12\x0f\n\x07\x44\x61ta_10\x18\x0f \x01(\x02\x12\x0f\n\x07\x44\x61ta_11\x18\x10 \x01(\x02\x12\x0f\n\x07\x44\x61ta_12\x18\x11 \x01(\x02\x12\x0f\n\x07\x44\x61ta_13\x18\x12 \x01(\x02\x12\x0f\n\x07\x44\x61ta_14\x18\x13 \x01(\x02\x12\x0f\n\x07\x44\x61ta_15\x18\x14 \x01(\x02\x12\x0f\n\x07\x44\x61ta_16\x18\x15 \x01(\x02\"\xf5\x07\n\x12\x44\x65scriptionMessage\x12\n\n\x02id\x18\x01 \x02(\r\x12\x1a\n\x0bSensor_name\x18\x02 \x02(\tB\x05\x92?\x02\x08(\x12>\n\x10\x44\x65scription_Type\x18\x03 \x02(\x0e\x32$.DescriptionMessage.DESCRIPTION_TYPE\x12\x1a\n\x0bstr_Data_01\x18\x04 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_02\x18\x05 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_03\x18\x06 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_04\x18\x07 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_05\x18\x08 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_06\x18\t \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_07\x18\n \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_08\x18\x0b \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_09\x18\x0c \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_10\x18\r \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_11\x18\x0e \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_12\x18\x0f \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_13\x18\x10 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_14\x18\x11 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_15\x18\x12 \x01(\tB\x05\x92?\x02\x08(\x12\x1a\n\x0bstr_Data_16\x18\x13 \x01(\tB\x05\x92?\x02\x08(\x12\x11\n\tf_Data_01\x18\x14 \x01(\x02\x12\x11\n\tf_Data_02\x18\x15 \x01(\x02\x12\x11\n\tf_Data_03\x18\x16 \x01(\x02\x12\x11\n\tf_Data_04\x18\x17 \x01(\x02\x12\x11\n\tf_Data_05\x18\x18 \x01(\x02\x12\x11\n\tf_Data_06\x18\x19 \x01(\x02\x12\x11\n\tf_Data_07\x18\x1a \x01(\x02\x12\x11\n\tf_Data_08\x18\x1b \x01(\x02\x12\x11\n\tf_Data_09\x18\x1c \x01(\x02\x12\x11\n\tf_Data_10\x18\x1d \x01(\x02\x12\x11\n\tf_Data_11\x18\x1e \x01(\x02\x12\x11\n\tf_Data_12\x18\x1f \x01(\x02\x12\x11\n\tf_Data_13\x18  \x01(\x02\x12\x11\n\tf_Data_14\x18! \x01(\x02\x12\x11\n\tf_Data_15\x18\" \x01(\x02\x12\x11\n\tf_Data_16\x18# \x01(\x02\"\x86\x01\n\x10\x44\x45SCRIPTION_TYPE\x12\x15\n\x11PHYSICAL_QUANTITY\x10\x00\x12\x08\n\x04UNIT\x10\x01\x12\x14\n\x10UNCERTAINTY_TYPE\x10\x02\x12\x0e\n\nRESOLUTION\x10\x03\x12\r\n\tMIN_SCALE\x10\x04\x12\r\n\tMAX_SCALE\x10\x05\x12\r\n\tHIERARCHY\x10\x06')
  ,
  dependencies=[nanopb__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DESCRIPTIONMESSAGE_DESCRIPTION_TYPE = _descriptor.EnumDescriptor(
  name='DESCRIPTION_TYPE',
  full_name='DescriptionMessage.DESCRIPTION_TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_QUANTITY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNCERTAINTY_TYPE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOLUTION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_SCALE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_SCALE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIERARCHY', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1305,
  serialized_end=1439,
)
_sym_db.RegisterEnumDescriptor(_DESCRIPTIONMESSAGE_DESCRIPTION_TYPE)


_DATAMESSAGE = _descriptor.Descriptor(
  name='DataMessage',
  full_name='DataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DataMessage.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_number', full_name='DataMessage.sample_number', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unix_time', full_name='DataMessage.unix_time', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unix_time_nsecs', full_name='DataMessage.unix_time_nsecs', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_uncertainty', full_name='DataMessage.time_uncertainty', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_01', full_name='DataMessage.Data_01', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_02', full_name='DataMessage.Data_02', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_03', full_name='DataMessage.Data_03', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_04', full_name='DataMessage.Data_04', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_05', full_name='DataMessage.Data_05', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_06', full_name='DataMessage.Data_06', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_07', full_name='DataMessage.Data_07', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_08', full_name='DataMessage.Data_08', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_09', full_name='DataMessage.Data_09', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_10', full_name='DataMessage.Data_10', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_11', full_name='DataMessage.Data_11', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_12', full_name='DataMessage.Data_12', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_13', full_name='DataMessage.Data_13', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_14', full_name='DataMessage.Data_14', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_15', full_name='DataMessage.Data_15', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data_16', full_name='DataMessage.Data_16', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=423,
)


_DESCRIPTIONMESSAGE = _descriptor.Descriptor(
  name='DescriptionMessage',
  full_name='DescriptionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DescriptionMessage.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sensor_name', full_name='DescriptionMessage.Sensor_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='Description_Type', full_name='DescriptionMessage.Description_Type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_Data_01', full_name='DescriptionMessage.str_Data_01', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_02', full_name='DescriptionMessage.str_Data_02', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_03', full_name='DescriptionMessage.str_Data_03', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_04', full_name='DescriptionMessage.str_Data_04', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_05', full_name='DescriptionMessage.str_Data_05', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_06', full_name='DescriptionMessage.str_Data_06', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_07', full_name='DescriptionMessage.str_Data_07', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_08', full_name='DescriptionMessage.str_Data_08', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_09', full_name='DescriptionMessage.str_Data_09', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_10', full_name='DescriptionMessage.str_Data_10', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_11', full_name='DescriptionMessage.str_Data_11', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_12', full_name='DescriptionMessage.str_Data_12', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_13', full_name='DescriptionMessage.str_Data_13', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_14', full_name='DescriptionMessage.str_Data_14', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_15', full_name='DescriptionMessage.str_Data_15', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='str_Data_16', full_name='DescriptionMessage.str_Data_16', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))),
    _descriptor.FieldDescriptor(
      name='f_Data_01', full_name='DescriptionMessage.f_Data_01', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_02', full_name='DescriptionMessage.f_Data_02', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_03', full_name='DescriptionMessage.f_Data_03', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_04', full_name='DescriptionMessage.f_Data_04', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_05', full_name='DescriptionMessage.f_Data_05', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_06', full_name='DescriptionMessage.f_Data_06', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_07', full_name='DescriptionMessage.f_Data_07', index=25,
      number=26, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_08', full_name='DescriptionMessage.f_Data_08', index=26,
      number=27, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_09', full_name='DescriptionMessage.f_Data_09', index=27,
      number=28, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_10', full_name='DescriptionMessage.f_Data_10', index=28,
      number=29, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_11', full_name='DescriptionMessage.f_Data_11', index=29,
      number=30, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_12', full_name='DescriptionMessage.f_Data_12', index=30,
      number=31, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_13', full_name='DescriptionMessage.f_Data_13', index=31,
      number=32, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_14', full_name='DescriptionMessage.f_Data_14', index=32,
      number=33, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_15', full_name='DescriptionMessage.f_Data_15', index=33,
      number=34, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f_Data_16', full_name='DescriptionMessage.f_Data_16', index=34,
      number=35, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DESCRIPTIONMESSAGE_DESCRIPTION_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=1439,
)

_DESCRIPTIONMESSAGE.fields_by_name['Description_Type'].enum_type = _DESCRIPTIONMESSAGE_DESCRIPTION_TYPE
_DESCRIPTIONMESSAGE_DESCRIPTION_TYPE.containing_type = _DESCRIPTIONMESSAGE
DESCRIPTOR.message_types_by_name['DataMessage'] = _DATAMESSAGE
DESCRIPTOR.message_types_by_name['DescriptionMessage'] = _DESCRIPTIONMESSAGE

DataMessage = _reflection.GeneratedProtocolMessageType('DataMessage', (_message.Message,), dict(
  DESCRIPTOR = _DATAMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:DataMessage)
  ))
_sym_db.RegisterMessage(DataMessage)

DescriptionMessage = _reflection.GeneratedProtocolMessageType('DescriptionMessage', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIPTIONMESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:DescriptionMessage)
  ))
_sym_db.RegisterMessage(DescriptionMessage)


_DESCRIPTIONMESSAGE.fields_by_name['Sensor_name'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['Sensor_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_01'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_01']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_02'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_02']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_03'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_03']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_04'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_04']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_05'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_05']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_06'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_06']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_07'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_07']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_08'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_08']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_09'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_09']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_10'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_10']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_11'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_11']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_12'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_12']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_13'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_13']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_14'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_14']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_15'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_15']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_16'].has_options = True
_DESCRIPTIONMESSAGE.fields_by_name['str_Data_16']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\002\010('))
# @@protoc_insertion_point(module_scope)
