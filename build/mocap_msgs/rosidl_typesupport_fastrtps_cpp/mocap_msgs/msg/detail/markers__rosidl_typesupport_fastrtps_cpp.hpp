// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from mocap_msgs:msg/Markers.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKERS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKERS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "mocap_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "mocap_msgs/msg/detail/markers__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace mocap_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
cdr_serialize(
  const mocap_msgs::msg::Markers & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  mocap_msgs::msg::Markers & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
get_serialized_size(
  const mocap_msgs::msg::Markers & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
max_serialized_size_Markers(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace mocap_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, mocap_msgs, msg, Markers)();

#ifdef __cplusplus
}
#endif

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKERS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
