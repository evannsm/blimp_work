// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mocap_msgs:msg/ImusInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mocap_msgs/msg/detail/imus_info__rosidl_typesupport_introspection_c.h"
#include "mocap_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mocap_msgs/msg/detail/imus_info__functions.h"
#include "mocap_msgs/msg/detail/imus_info__struct.h"


// Include directives for member types
// Member `sensor_ids`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mocap_msgs__msg__ImusInfo__init(message_memory);
}

void ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_fini_function(void * message_memory)
{
  mocap_msgs__msg__ImusInfo__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_member_array[3] = {
  {
    "sensor_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__ImusInfo, sensor_ids),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "battery_level",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__ImusInfo, battery_level),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "temperature",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__ImusInfo, temperature),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_members = {
  "mocap_msgs__msg",  // message namespace
  "ImusInfo",  // message name
  3,  // number of fields
  sizeof(mocap_msgs__msg__ImusInfo),
  ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_member_array,  // message members
  ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_type_support_handle = {
  0,
  &ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mocap_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mocap_msgs, msg, ImusInfo)() {
  if (!ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_type_support_handle.typesupport_identifier) {
    ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ImusInfo__rosidl_typesupport_introspection_c__ImusInfo_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
