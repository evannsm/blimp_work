// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKER__BUILDER_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mocap_msgs/msg/detail/marker__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mocap_msgs
{

namespace msg
{

namespace builder
{

class Init_Marker_translation
{
public:
  explicit Init_Marker_translation(::mocap_msgs::msg::Marker & msg)
  : msg_(msg)
  {}
  ::mocap_msgs::msg::Marker translation(::mocap_msgs::msg::Marker::_translation_type arg)
  {
    msg_.translation = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mocap_msgs::msg::Marker msg_;
};

class Init_Marker_marker_name
{
public:
  explicit Init_Marker_marker_name(::mocap_msgs::msg::Marker & msg)
  : msg_(msg)
  {}
  Init_Marker_translation marker_name(::mocap_msgs::msg::Marker::_marker_name_type arg)
  {
    msg_.marker_name = std::move(arg);
    return Init_Marker_translation(msg_);
  }

private:
  ::mocap_msgs::msg::Marker msg_;
};

class Init_Marker_marker_index
{
public:
  explicit Init_Marker_marker_index(::mocap_msgs::msg::Marker & msg)
  : msg_(msg)
  {}
  Init_Marker_marker_name marker_index(::mocap_msgs::msg::Marker::_marker_index_type arg)
  {
    msg_.marker_index = std::move(arg);
    return Init_Marker_marker_name(msg_);
  }

private:
  ::mocap_msgs::msg::Marker msg_;
};

class Init_Marker_id_type
{
public:
  Init_Marker_id_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Marker_marker_index id_type(::mocap_msgs::msg::Marker::_id_type_type arg)
  {
    msg_.id_type = std::move(arg);
    return Init_Marker_marker_index(msg_);
  }

private:
  ::mocap_msgs::msg::Marker msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mocap_msgs::msg::Marker>()
{
  return mocap_msgs::msg::builder::Init_Marker_id_type();
}

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKER__BUILDER_HPP_
