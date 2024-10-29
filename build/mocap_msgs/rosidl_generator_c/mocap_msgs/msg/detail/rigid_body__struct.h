// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mocap_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__STRUCT_H_
#define MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'rigid_body_name'
#include "rosidl_runtime_c/string.h"
// Member 'markers'
#include "mocap_msgs/msg/detail/marker__struct.h"
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in msg/RigidBody in the package mocap_msgs.
typedef struct mocap_msgs__msg__RigidBody
{
  rosidl_runtime_c__String rigid_body_name;
  mocap_msgs__msg__Marker__Sequence markers;
  geometry_msgs__msg__Pose pose;
} mocap_msgs__msg__RigidBody;

// Struct for a sequence of mocap_msgs__msg__RigidBody.
typedef struct mocap_msgs__msg__RigidBody__Sequence
{
  mocap_msgs__msg__RigidBody * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mocap_msgs__msg__RigidBody__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__STRUCT_H_
