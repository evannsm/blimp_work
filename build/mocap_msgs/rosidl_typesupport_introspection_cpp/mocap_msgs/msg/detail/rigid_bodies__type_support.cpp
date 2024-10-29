// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from mocap_msgs:msg/RigidBodies.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "mocap_msgs/msg/detail/rigid_bodies__struct.hpp"
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

void RigidBodies_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) mocap_msgs::msg::RigidBodies(_init);
}

void RigidBodies_fini_function(void * message_memory)
{
  auto typed_message = static_cast<mocap_msgs::msg::RigidBodies *>(message_memory);
  typed_message->~RigidBodies();
}

size_t size_function__RigidBodies__rigidbodies(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<mocap_msgs::msg::RigidBody> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RigidBodies__rigidbodies(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<mocap_msgs::msg::RigidBody> *>(untyped_member);
  return &member[index];
}

void * get_function__RigidBodies__rigidbodies(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<mocap_msgs::msg::RigidBody> *>(untyped_member);
  return &member[index];
}

void fetch_function__RigidBodies__rigidbodies(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const mocap_msgs::msg::RigidBody *>(
    get_const_function__RigidBodies__rigidbodies(untyped_member, index));
  auto & value = *reinterpret_cast<mocap_msgs::msg::RigidBody *>(untyped_value);
  value = item;
}

void assign_function__RigidBodies__rigidbodies(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<mocap_msgs::msg::RigidBody *>(
    get_function__RigidBodies__rigidbodies(untyped_member, index));
  const auto & value = *reinterpret_cast<const mocap_msgs::msg::RigidBody *>(untyped_value);
  item = value;
}

void resize_function__RigidBodies__rigidbodies(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<mocap_msgs::msg::RigidBody> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RigidBodies_message_member_array[3] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::RigidBodies, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
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
    offsetof(mocap_msgs::msg::RigidBodies, frame_number),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "rigidbodies",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<mocap_msgs::msg::RigidBody>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::RigidBodies, rigidbodies),  // bytes offset in struct
    nullptr,  // default value
    size_function__RigidBodies__rigidbodies,  // size() function pointer
    get_const_function__RigidBodies__rigidbodies,  // get_const(index) function pointer
    get_function__RigidBodies__rigidbodies,  // get(index) function pointer
    fetch_function__RigidBodies__rigidbodies,  // fetch(index, &value) function pointer
    assign_function__RigidBodies__rigidbodies,  // assign(index, value) function pointer
    resize_function__RigidBodies__rigidbodies  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RigidBodies_message_members = {
  "mocap_msgs::msg",  // message namespace
  "RigidBodies",  // message name
  3,  // number of fields
  sizeof(mocap_msgs::msg::RigidBodies),
  RigidBodies_message_member_array,  // message members
  RigidBodies_init_function,  // function to initialize message memory (memory has to be allocated)
  RigidBodies_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RigidBodies_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RigidBodies_message_members,
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
get_message_type_support_handle<mocap_msgs::msg::RigidBodies>()
{
  return &::mocap_msgs::msg::rosidl_typesupport_introspection_cpp::RigidBodies_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, mocap_msgs, msg, RigidBodies)() {
  return &::mocap_msgs::msg::rosidl_typesupport_introspection_cpp::RigidBodies_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
