// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mocap_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mocap_msgs/msg/detail/rigid_body__rosidl_typesupport_introspection_c.h"
#include "mocap_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mocap_msgs/msg/detail/rigid_body__functions.h"
#include "mocap_msgs/msg/detail/rigid_body__struct.h"


// Include directives for member types
// Member `rigid_body_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `markers`
#include "mocap_msgs/msg/marker.h"
// Member `markers`
#include "mocap_msgs/msg/detail/marker__rosidl_typesupport_introspection_c.h"
// Member `pose`
#include "geometry_msgs/msg/pose.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void RigidBody__rosidl_typesupport_introspection_c__RigidBody_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mocap_msgs__msg__RigidBody__init(message_memory);
}

void RigidBody__rosidl_typesupport_introspection_c__RigidBody_fini_function(void * message_memory)
{
  mocap_msgs__msg__RigidBody__fini(message_memory);
}

size_t RigidBody__rosidl_typesupport_introspection_c__size_function__Marker__markers(
  const void * untyped_member)
{
  const mocap_msgs__msg__Marker__Sequence * member =
    (const mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  return member->size;
}

const void * RigidBody__rosidl_typesupport_introspection_c__get_const_function__Marker__markers(
  const void * untyped_member, size_t index)
{
  const mocap_msgs__msg__Marker__Sequence * member =
    (const mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  return &member->data[index];
}

void * RigidBody__rosidl_typesupport_introspection_c__get_function__Marker__markers(
  void * untyped_member, size_t index)
{
  mocap_msgs__msg__Marker__Sequence * member =
    (mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  return &member->data[index];
}

bool RigidBody__rosidl_typesupport_introspection_c__resize_function__Marker__markers(
  void * untyped_member, size_t size)
{
  mocap_msgs__msg__Marker__Sequence * member =
    (mocap_msgs__msg__Marker__Sequence *)(untyped_member);
  mocap_msgs__msg__Marker__Sequence__fini(member);
  return mocap_msgs__msg__Marker__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array[3] = {
  {
    "rigid_body_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__RigidBody, rigid_body_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
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
    offsetof(mocap_msgs__msg__RigidBody, markers),  // bytes offset in struct
    NULL,  // default value
    RigidBody__rosidl_typesupport_introspection_c__size_function__Marker__markers,  // size() function pointer
    RigidBody__rosidl_typesupport_introspection_c__get_const_function__Marker__markers,  // get_const(index) function pointer
    RigidBody__rosidl_typesupport_introspection_c__get_function__Marker__markers,  // get(index) function pointer
    RigidBody__rosidl_typesupport_introspection_c__resize_function__Marker__markers  // resize(index) function pointer
  },
  {
    "pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs__msg__RigidBody, pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_members = {
  "mocap_msgs__msg",  // message namespace
  "RigidBody",  // message name
  3,  // number of fields
  sizeof(mocap_msgs__msg__RigidBody),
  RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array,  // message members
  RigidBody__rosidl_typesupport_introspection_c__RigidBody_init_function,  // function to initialize message memory (memory has to be allocated)
  RigidBody__rosidl_typesupport_introspection_c__RigidBody_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle = {
  0,
  &RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mocap_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mocap_msgs, msg, RigidBody)() {
  RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mocap_msgs, msg, Marker)();
  RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  if (!RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle.typesupport_identifier) {
    RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &RigidBody__rosidl_typesupport_introspection_c__RigidBody_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
