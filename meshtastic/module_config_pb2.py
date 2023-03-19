# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/module_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emeshtastic/module_config.proto\"\x95\x17\n\x0cModuleConfig\x12(\n\x04mqtt\x18\x01 \x01(\x0b\x32\x18.ModuleConfig.MQTTConfigH\x00\x12,\n\x06serial\x18\x02 \x01(\x0b\x32\x1a.ModuleConfig.SerialConfigH\x00\x12I\n\x15\x65xternal_notification\x18\x03 \x01(\x0b\x32(.ModuleConfig.ExternalNotificationConfigH\x00\x12\x39\n\rstore_forward\x18\x04 \x01(\x0b\x32 .ModuleConfig.StoreForwardConfigH\x00\x12\x33\n\nrange_test\x18\x05 \x01(\x0b\x32\x1d.ModuleConfig.RangeTestConfigH\x00\x12\x32\n\ttelemetry\x18\x06 \x01(\x0b\x32\x1d.ModuleConfig.TelemetryConfigH\x00\x12;\n\x0e\x63\x61nned_message\x18\x07 \x01(\x0b\x32!.ModuleConfig.CannedMessageConfigH\x00\x12*\n\x05\x61udio\x18\x08 \x01(\x0b\x32\x19.ModuleConfig.AudioConfigH\x00\x12=\n\x0fremote_hardware\x18\t \x01(\x0b\x32\".ModuleConfig.RemoteHardwareConfigH\x00\x1a\x84\x01\n\nMQTTConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x1a\n\x12\x65ncryption_enabled\x18\x05 \x01(\x08\x12\x14\n\x0cjson_enabled\x18\x06 \x01(\x08\x1a\'\n\x14RemoteHardwareConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x1a\xd9\x02\n\x0b\x41udioConfig\x12\x16\n\x0e\x63odec2_enabled\x18\x01 \x01(\x08\x12\x0f\n\x07ptt_pin\x18\x02 \x01(\r\x12\x35\n\x07\x62itrate\x18\x03 \x01(\x0e\x32$.ModuleConfig.AudioConfig.Audio_Baud\x12\x0e\n\x06i2s_ws\x18\x04 \x01(\r\x12\x0e\n\x06i2s_sd\x18\x05 \x01(\r\x12\x0f\n\x07i2s_din\x18\x06 \x01(\r\x12\x0f\n\x07i2s_sck\x18\x07 \x01(\r\"\xa7\x01\n\nAudio_Baud\x12\x12\n\x0e\x43ODEC2_DEFAULT\x10\x00\x12\x0f\n\x0b\x43ODEC2_3200\x10\x01\x12\x0f\n\x0b\x43ODEC2_2400\x10\x02\x12\x0f\n\x0b\x43ODEC2_1600\x10\x03\x12\x0f\n\x0b\x43ODEC2_1400\x10\x04\x12\x0f\n\x0b\x43ODEC2_1300\x10\x05\x12\x0f\n\x0b\x43ODEC2_1200\x10\x06\x12\x0e\n\nCODEC2_700\x10\x07\x12\x0f\n\x0b\x43ODEC2_700B\x10\x08\x1a\x9b\x04\n\x0cSerialConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0c\n\x04\x65\x63ho\x18\x02 \x01(\x08\x12\x0b\n\x03rxd\x18\x03 \x01(\r\x12\x0b\n\x03txd\x18\x04 \x01(\r\x12\x34\n\x04\x62\x61ud\x18\x05 \x01(\x0e\x32&.ModuleConfig.SerialConfig.Serial_Baud\x12\x0f\n\x07timeout\x18\x06 \x01(\r\x12\x34\n\x04mode\x18\x07 \x01(\x0e\x32&.ModuleConfig.SerialConfig.Serial_Mode\"\x8a\x02\n\x0bSerial_Baud\x12\x10\n\x0c\x42\x41UD_DEFAULT\x10\x00\x12\x0c\n\x08\x42\x41UD_110\x10\x01\x12\x0c\n\x08\x42\x41UD_300\x10\x02\x12\x0c\n\x08\x42\x41UD_600\x10\x03\x12\r\n\tBAUD_1200\x10\x04\x12\r\n\tBAUD_2400\x10\x05\x12\r\n\tBAUD_4800\x10\x06\x12\r\n\tBAUD_9600\x10\x07\x12\x0e\n\nBAUD_19200\x10\x08\x12\x0e\n\nBAUD_38400\x10\t\x12\x0e\n\nBAUD_57600\x10\n\x12\x0f\n\x0b\x42\x41UD_115200\x10\x0b\x12\x0f\n\x0b\x42\x41UD_230400\x10\x0c\x12\x0f\n\x0b\x42\x41UD_460800\x10\r\x12\x0f\n\x0b\x42\x41UD_576000\x10\x0e\x12\x0f\n\x0b\x42\x41UD_921600\x10\x0f\"H\n\x0bSerial_Mode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06SIMPLE\x10\x01\x12\t\n\x05PROTO\x10\x02\x12\x0b\n\x07TEXTMSG\x10\x03\x12\x08\n\x04NMEA\x10\x04\x1a\xce\x02\n\x1a\x45xternalNotificationConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x11\n\toutput_ms\x18\x02 \x01(\r\x12\x0e\n\x06output\x18\x03 \x01(\r\x12\x14\n\x0coutput_vibra\x18\x08 \x01(\r\x12\x15\n\routput_buzzer\x18\t \x01(\r\x12\x0e\n\x06\x61\x63tive\x18\x04 \x01(\x08\x12\x15\n\ralert_message\x18\x05 \x01(\x08\x12\x1b\n\x13\x61lert_message_vibra\x18\n \x01(\x08\x12\x1c\n\x14\x61lert_message_buzzer\x18\x0b \x01(\x08\x12\x12\n\nalert_bell\x18\x06 \x01(\x08\x12\x18\n\x10\x61lert_bell_vibra\x18\x0c \x01(\x08\x12\x19\n\x11\x61lert_bell_buzzer\x18\r \x01(\x08\x12\x0f\n\x07use_pwm\x18\x07 \x01(\x08\x12\x13\n\x0bnag_timeout\x18\x0e \x01(\r\x1a\x84\x01\n\x12StoreForwardConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x11\n\theartbeat\x18\x02 \x01(\x08\x12\x0f\n\x07records\x18\x03 \x01(\r\x12\x1a\n\x12history_return_max\x18\x04 \x01(\r\x12\x1d\n\x15history_return_window\x18\x05 \x01(\r\x1a@\n\x0fRangeTestConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0e\n\x06sender\x18\x02 \x01(\r\x12\x0c\n\x04save\x18\x03 \x01(\x08\x1a\x86\x02\n\x0fTelemetryConfig\x12\x1e\n\x16\x64\x65vice_update_interval\x18\x01 \x01(\r\x12#\n\x1b\x65nvironment_update_interval\x18\x02 \x01(\r\x12\'\n\x1f\x65nvironment_measurement_enabled\x18\x03 \x01(\x08\x12\"\n\x1a\x65nvironment_screen_enabled\x18\x04 \x01(\x08\x12&\n\x1e\x65nvironment_display_fahrenheit\x18\x05 \x01(\x08\x12\x1b\n\x13\x61ir_quality_enabled\x18\x06 \x01(\x08\x12\x1c\n\x14\x61ir_quality_interval\x18\x07 \x01(\r\x1a\xb5\x04\n\x13\x43\x61nnedMessageConfig\x12\x17\n\x0frotary1_enabled\x18\x01 \x01(\x08\x12\x19\n\x11inputbroker_pin_a\x18\x02 \x01(\r\x12\x19\n\x11inputbroker_pin_b\x18\x03 \x01(\r\x12\x1d\n\x15inputbroker_pin_press\x18\x04 \x01(\r\x12N\n\x14inputbroker_event_cw\x18\x05 \x01(\x0e\x32\x30.ModuleConfig.CannedMessageConfig.InputEventChar\x12O\n\x15inputbroker_event_ccw\x18\x06 \x01(\x0e\x32\x30.ModuleConfig.CannedMessageConfig.InputEventChar\x12Q\n\x17inputbroker_event_press\x18\x07 \x01(\x0e\x32\x30.ModuleConfig.CannedMessageConfig.InputEventChar\x12\x17\n\x0fupdown1_enabled\x18\x08 \x01(\x08\x12\x0f\n\x07\x65nabled\x18\t \x01(\x08\x12\x1a\n\x12\x61llow_input_source\x18\n \x01(\t\x12\x11\n\tsend_bell\x18\x0b \x01(\x08\"c\n\x0eInputEventChar\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02UP\x10\x11\x12\x08\n\x04\x44OWN\x10\x12\x12\x08\n\x04LEFT\x10\x13\x12\t\n\x05RIGHT\x10\x14\x12\n\n\x06SELECT\x10\n\x12\x08\n\x04\x42\x41\x43K\x10\x1b\x12\n\n\x06\x43\x41NCEL\x10\x18\x42\x11\n\x0fpayload_variantBg\n\x13\x63om.geeksville.meshB\x12ModuleConfigProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')



_MODULECONFIG = DESCRIPTOR.message_types_by_name['ModuleConfig']
_MODULECONFIG_MQTTCONFIG = _MODULECONFIG.nested_types_by_name['MQTTConfig']
_MODULECONFIG_REMOTEHARDWARECONFIG = _MODULECONFIG.nested_types_by_name['RemoteHardwareConfig']
_MODULECONFIG_AUDIOCONFIG = _MODULECONFIG.nested_types_by_name['AudioConfig']
_MODULECONFIG_SERIALCONFIG = _MODULECONFIG.nested_types_by_name['SerialConfig']
_MODULECONFIG_EXTERNALNOTIFICATIONCONFIG = _MODULECONFIG.nested_types_by_name['ExternalNotificationConfig']
_MODULECONFIG_STOREFORWARDCONFIG = _MODULECONFIG.nested_types_by_name['StoreForwardConfig']
_MODULECONFIG_RANGETESTCONFIG = _MODULECONFIG.nested_types_by_name['RangeTestConfig']
_MODULECONFIG_TELEMETRYCONFIG = _MODULECONFIG.nested_types_by_name['TelemetryConfig']
_MODULECONFIG_CANNEDMESSAGECONFIG = _MODULECONFIG.nested_types_by_name['CannedMessageConfig']
_MODULECONFIG_AUDIOCONFIG_AUDIO_BAUD = _MODULECONFIG_AUDIOCONFIG.enum_types_by_name['Audio_Baud']
_MODULECONFIG_SERIALCONFIG_SERIAL_BAUD = _MODULECONFIG_SERIALCONFIG.enum_types_by_name['Serial_Baud']
_MODULECONFIG_SERIALCONFIG_SERIAL_MODE = _MODULECONFIG_SERIALCONFIG.enum_types_by_name['Serial_Mode']
_MODULECONFIG_CANNEDMESSAGECONFIG_INPUTEVENTCHAR = _MODULECONFIG_CANNEDMESSAGECONFIG.enum_types_by_name['InputEventChar']
ModuleConfig = _reflection.GeneratedProtocolMessageType('ModuleConfig', (_message.Message,), {

  'MQTTConfig' : _reflection.GeneratedProtocolMessageType('MQTTConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_MQTTCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.MQTTConfig)
    })
  ,

  'RemoteHardwareConfig' : _reflection.GeneratedProtocolMessageType('RemoteHardwareConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_REMOTEHARDWARECONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.RemoteHardwareConfig)
    })
  ,

  'AudioConfig' : _reflection.GeneratedProtocolMessageType('AudioConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_AUDIOCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.AudioConfig)
    })
  ,

  'SerialConfig' : _reflection.GeneratedProtocolMessageType('SerialConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_SERIALCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.SerialConfig)
    })
  ,

  'ExternalNotificationConfig' : _reflection.GeneratedProtocolMessageType('ExternalNotificationConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_EXTERNALNOTIFICATIONCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.ExternalNotificationConfig)
    })
  ,

  'StoreForwardConfig' : _reflection.GeneratedProtocolMessageType('StoreForwardConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_STOREFORWARDCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.StoreForwardConfig)
    })
  ,

  'RangeTestConfig' : _reflection.GeneratedProtocolMessageType('RangeTestConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_RANGETESTCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.RangeTestConfig)
    })
  ,

  'TelemetryConfig' : _reflection.GeneratedProtocolMessageType('TelemetryConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_TELEMETRYCONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.TelemetryConfig)
    })
  ,

  'CannedMessageConfig' : _reflection.GeneratedProtocolMessageType('CannedMessageConfig', (_message.Message,), {
    'DESCRIPTOR' : _MODULECONFIG_CANNEDMESSAGECONFIG,
    '__module__' : 'meshtastic.module_config_pb2'
    # @@protoc_insertion_point(class_scope:ModuleConfig.CannedMessageConfig)
    })
  ,
  'DESCRIPTOR' : _MODULECONFIG,
  '__module__' : 'meshtastic.module_config_pb2'
  # @@protoc_insertion_point(class_scope:ModuleConfig)
  })
_sym_db.RegisterMessage(ModuleConfig)
_sym_db.RegisterMessage(ModuleConfig.MQTTConfig)
_sym_db.RegisterMessage(ModuleConfig.RemoteHardwareConfig)
_sym_db.RegisterMessage(ModuleConfig.AudioConfig)
_sym_db.RegisterMessage(ModuleConfig.SerialConfig)
_sym_db.RegisterMessage(ModuleConfig.ExternalNotificationConfig)
_sym_db.RegisterMessage(ModuleConfig.StoreForwardConfig)
_sym_db.RegisterMessage(ModuleConfig.RangeTestConfig)
_sym_db.RegisterMessage(ModuleConfig.TelemetryConfig)
_sym_db.RegisterMessage(ModuleConfig.CannedMessageConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\022ModuleConfigProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _MODULECONFIG._serialized_start=35
  _MODULECONFIG._serialized_end=3000
  _MODULECONFIG_MQTTCONFIG._serialized_start=547
  _MODULECONFIG_MQTTCONFIG._serialized_end=679
  _MODULECONFIG_REMOTEHARDWARECONFIG._serialized_start=681
  _MODULECONFIG_REMOTEHARDWARECONFIG._serialized_end=720
  _MODULECONFIG_AUDIOCONFIG._serialized_start=723
  _MODULECONFIG_AUDIOCONFIG._serialized_end=1068
  _MODULECONFIG_AUDIOCONFIG_AUDIO_BAUD._serialized_start=901
  _MODULECONFIG_AUDIOCONFIG_AUDIO_BAUD._serialized_end=1068
  _MODULECONFIG_SERIALCONFIG._serialized_start=1071
  _MODULECONFIG_SERIALCONFIG._serialized_end=1610
  _MODULECONFIG_SERIALCONFIG_SERIAL_BAUD._serialized_start=1270
  _MODULECONFIG_SERIALCONFIG_SERIAL_BAUD._serialized_end=1536
  _MODULECONFIG_SERIALCONFIG_SERIAL_MODE._serialized_start=1538
  _MODULECONFIG_SERIALCONFIG_SERIAL_MODE._serialized_end=1610
  _MODULECONFIG_EXTERNALNOTIFICATIONCONFIG._serialized_start=1613
  _MODULECONFIG_EXTERNALNOTIFICATIONCONFIG._serialized_end=1947
  _MODULECONFIG_STOREFORWARDCONFIG._serialized_start=1950
  _MODULECONFIG_STOREFORWARDCONFIG._serialized_end=2082
  _MODULECONFIG_RANGETESTCONFIG._serialized_start=2084
  _MODULECONFIG_RANGETESTCONFIG._serialized_end=2148
  _MODULECONFIG_TELEMETRYCONFIG._serialized_start=2151
  _MODULECONFIG_TELEMETRYCONFIG._serialized_end=2413
  _MODULECONFIG_CANNEDMESSAGECONFIG._serialized_start=2416
  _MODULECONFIG_CANNEDMESSAGECONFIG._serialized_end=2981
  _MODULECONFIG_CANNEDMESSAGECONFIG_INPUTEVENTCHAR._serialized_start=2882
  _MODULECONFIG_CANNEDMESSAGECONFIG_INPUTEVENTCHAR._serialized_end=2981
# @@protoc_insertion_point(module_scope)
