// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mocap_msgs:msg/RigidBodies.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__RIGID_BODIES__STRUCT_H_
#define MOCAP_MSGS__MSG__DETAIL__RIGID_BODIES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'rigidbodies'
#include "mocap_msgs/msg/detail/rigid_body__struct.h"

/// Struct defined in msg/RigidBodies in the package mocap_msgs.
typedef struct mocap_msgs__msg__RigidBodies
{
  std_msgs__msg__Header header;
  uint32_t frame_number;
  mocap_msgs__msg__RigidBody__Sequence rigidbodies;
} mocap_msgs__msg__RigidBodies;

// Struct for a sequence of mocap_msgs__msg__RigidBodies.
typedef struct mocap_msgs__msg__RigidBodies__Sequence
{
  mocap_msgs__msg__RigidBodies * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mocap_msgs__msg__RigidBodies__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOCAP_MSGS__MSG__DETAIL__RIGID_BODIES__STRUCT_H_
