// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mocap_msgs:msg/Markers.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKERS__BUILDER_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKERS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mocap_msgs/msg/detail/markers__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mocap_msgs
{

namespace msg
{

namespace builder
{

class Init_Markers_markers
{
public:
  explicit Init_Markers_markers(::mocap_msgs::msg::Markers & msg)
  : msg_(msg)
  {}
  ::mocap_msgs::msg::Markers markers(::mocap_msgs::msg::Markers::_markers_type arg)
  {
    msg_.markers = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mocap_msgs::msg::Markers msg_;
};

class Init_Markers_frame_number
{
public:
  explicit Init_Markers_frame_number(::mocap_msgs::msg::Markers & msg)
  : msg_(msg)
  {}
  Init_Markers_markers frame_number(::mocap_msgs::msg::Markers::_frame_number_type arg)
  {
    msg_.frame_number = std::move(arg);
    return Init_Markers_markers(msg_);
  }

private:
  ::mocap_msgs::msg::Markers msg_;
};

class Init_Markers_header
{
public:
  Init_Markers_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Markers_frame_number header(::mocap_msgs::msg::Markers::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Markers_frame_number(msg_);
  }

private:
  ::mocap_msgs::msg::Markers msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mocap_msgs::msg::Markers>()
{
  return mocap_msgs::msg::builder::Init_Markers_header();
}

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKERS__BUILDER_HPP_
