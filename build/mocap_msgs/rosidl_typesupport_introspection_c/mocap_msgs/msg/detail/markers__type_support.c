// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mocap_msgs:msg/Markers.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mocap_msgs/msg/detail/markers__rosidl_typesupport_introspection_c.h"
#include "mocap_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mocap_msgs/msg/detail/markers__functions.h"
#include "mocap_msgs/msg/detail/markers__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `markers`
#include "mocap_msgs/msg/marker.h"
// Member `markers`
#include "mocap_msgs/msg/detail/marker__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mocap_msgs__msg__Markers__init(message_memory);
}

void mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_fini_function(void * message_memory)
{
  mocap_msgs__msg__Markers__fini(message_memory);
}

size_t mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__size_function__Markers__markers(
  const void * untyped_member)
{
  const mocap_msgs__msg__Marker__Sequence * member =
    (const mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  return member->size;
}

const void * mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__get_const_function__Markers__markers(
  const void * untyped_member, size_t index)
{
  const mocap_msgs__msg__Marker__Sequence * member =
    (const mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  return &member->data[index];
}

void * mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__get_function__Markers__markers(
  void * untyped_member, size_t index)
{
  mocap_msgs__msg__Marker__Sequence * member =
    (mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  return &member->data[index];
}

void mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__fetch_function__Markers__markers(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const mocap_msgs__msg__Marker * item =
    ((const mocap_msgs__msg__Marker *)
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__get_const_function__Markers__markers(untyped_member, index));
  mocap_msgs__msg__Marker * value =
    (mocap_msgs__msg__Marker *)(untyped_value);
  *value = *item;
}

void mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__assign_function__Markers__markers(
  void * untyped_member, size_t index, const void * untyped_value)
{
  mocap_msgs__msg__Marker * item =
    ((mocap_msgs__msg__Marker *)
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__get_function__Markers__markers(untyped_member, index));
  const mocap_msgs__msg__Marker * value =
    (const mocap_msgs__msg__Marker *)(untyped_value);
  *item = *value;
}

bool mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__resize_function__Markers__markers(
  void * untyped_member, size_t size)
{
  mocap_msgs__msg__Marker__Sequence * member =
    (mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  mocap_msgs__msg__Marker__Sequence__fini(member);
  return mocap_msgs__msg__Marker__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Markers, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "frame_number",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Markers, frame_number),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "markers",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__Markers, markers),  // bytes offset in struct
    NULL,  // default value
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__size_function__Markers__markers,  // size() function pointer
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__get_const_function__Markers__markers,  // get_const(index) function pointer
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__get_function__Markers__markers,  // get(index) function pointer
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__fetch_function__Markers__markers,  // fetch(index, &value) function pointer
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__assign_function__Markers__markers,  // assign(index, value) function pointer
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__resize_function__Markers__markers  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_members = {
  "mocap_msgs__msg",  // message namespace
  "Markers",  // message name
  3,  // number of fields
  sizeof(mocap_msgs__msg__Markers),
  mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_member_array,  // message members
  mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_init_function,  // function to initialize message memory (memory has to be allocated)
  mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_type_support_handle = {
  0,
  &mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mocap_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mocap_msgs, msg, Markers)() {
  mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mocap_msgs, msg, Marker)();
  if (!mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_type_support_handle.typesupport_identifier) {
    mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mocap_msgs__msg__Markers__rosidl_typesupport_introspection_c__Markers_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
