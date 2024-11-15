// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from mocap_msgs:msg/ImusInfo.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "mocap_msgs/msg/detail/imus_info__struct.hpp"
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

void ImusInfo_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) mocap_msgs::msg::ImusInfo(_init);
}

void ImusInfo_fini_function(void * message_memory)
{
  auto typed_message = static_cast<mocap_msgs::msg::ImusInfo *>(message_memory);
  typed_message->~ImusInfo();
}

size_t size_function__ImusInfo__sensor_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ImusInfo__sensor_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__ImusInfo__sensor_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__ImusInfo__sensor_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__ImusInfo__sensor_ids(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__ImusInfo__sensor_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__ImusInfo__sensor_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__ImusInfo__sensor_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ImusInfo_message_member_array[3] = {
  {
    "sensor_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::ImusInfo, sensor_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__ImusInfo__sensor_ids,  // size() function pointer
    get_const_function__ImusInfo__sensor_ids,  // get_const(index) function pointer
    get_function__ImusInfo__sensor_ids,  // get(index) function pointer
    fetch_function__ImusInfo__sensor_ids,  // fetch(index, &value) function pointer
    assign_function__ImusInfo__sensor_ids,  // assign(index, value) function pointer
    resize_function__ImusInfo__sensor_ids  // resize(index) function pointer
  },
  {
    "battery_level",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::ImusInfo, battery_level),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "temperature",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mocap_msgs::msg::ImusInfo, temperature),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ImusInfo_message_members = {
  "mocap_msgs::msg",  // message namespace
  "ImusInfo",  // message name
  3,  // number of fields
  sizeof(mocap_msgs::msg::ImusInfo),
  ImusInfo_message_member_array,  // message members
  ImusInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  ImusInfo_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ImusInfo_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ImusInfo_message_members,
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
get_message_type_support_handle<mocap_msgs::msg::ImusInfo>()
{
  return &::mocap_msgs::msg::rosidl_typesupport_introspection_cpp::ImusInfo_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, mocap_msgs, msg, ImusInfo)() {
  return &::mocap_msgs::msg::rosidl_typesupport_introspection_cpp::ImusInfo_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
