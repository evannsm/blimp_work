// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mocap_msgs/msg/detail/marker__rosidl_typesupport_introspection_c.h"
#include "mocap_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mocap_msgs/msg/detail/marker__functions.h"
#include "mocap_msgs/msg/detail/marker__struct.h"


// Include directives for member types
// Member `marker_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `translation`
#include "geometry_msgs/msg/point.h"
// Member `translation`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mocap_msgs__msg__Marker__init(message_memory);
}

void mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_fini_function(void * message_memory)
{
  mocap_msgs__msg__Marker__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_member_array[4] = {
  {
    "id_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Marker, id_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "marker_index",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Marker, marker_index),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "marker_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Marker, marker_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "translation",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Marker, translation),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_members = {
  "mocap_msgs__msg",  // message namespace
  "Marker",  // message name
  4,  // number of fields
  sizeof(mocap_msgs__msg__Marker),
  mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_member_array,  // message members
  mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_init_function,  // function to initialize message memory (memory has to be allocated)
  mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_type_support_handle = {
  0,
  &mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mocap_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mocap_msgs, msg, Marker)() {
  mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_type_support_handle.typesupport_identifier) {
    mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mocap_msgs__msg__Marker__rosidl_typesupport_introspection_c__Marker_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
