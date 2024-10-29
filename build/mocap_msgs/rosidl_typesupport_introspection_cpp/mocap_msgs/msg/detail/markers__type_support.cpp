// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from mocap_msgs:msg/Markers.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "mocap_msgs/msg/detail/markers__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace mocap_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Markers_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) mocap_msgs::msg::Markers(_init);
}

void Markers_fini_function(void * message_memory)
{
  auto typed_message = static_cast<mocap_msgs::msg::Markers *>(message_memory);
  typed_message->~Markers();
}

size_t size_function__Markers__markers(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<mocap_msgs::msg::Marker> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Markers__markers(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<mocap_msgs::msg::Marker> *>(untyped_member);
  return &member[index];
}

void * get_function__Markers__markers(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<mocap_msgs::msg::Marker> *>(untyped_member);
  return &member[index];
}

void resize_function__Markers__markers(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<mocap_msgs::msg::Marker> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Markers_message_member_array[3] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::Markers, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "frame_number",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::Markers, frame_number),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "markers",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<mocap_msgs::msg::Marker>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::Markers, markers),  // bytes offset in struct
    nullptr,  // default value
    size_function__Markers__markers,  // size() function pointer
    get_const_function__Markers__markers,  // get_const(index) function pointer
    get_function__Markers__markers,  // get(index) function pointer
    resize_function__Markers__markers  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Markers_message_members = {
  "mocap_msgs::msg",  // message namespace
  "Markers",  // message name
  3,  // number of fields
  sizeof(mocap_msgs::msg::Markers),
  Markers_message_member_array,  // message members
  Markers_init_function,  // function to initialize message memory (memory has to be allocated)
  Markers_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Markers_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Markers_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace mocap_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<mocap_msgs::msg::Markers>()
{
  return &::mocap_msgs::msg::rosidl_typesupport_introspection_cpp::Markers_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, mocap_msgs, msg, Markers)() {
  return &::mocap_msgs::msg::rosidl_typesupport_introspection_cpp::Markers_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
