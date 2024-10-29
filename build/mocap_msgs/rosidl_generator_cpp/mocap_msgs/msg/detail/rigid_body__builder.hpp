// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mocap_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__BUILDER_HPP_
#define MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mocap_msgs/msg/detail/rigid_body__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mocap_msgs
{

namespace msg
{

namespace builder
{

class Init_RigidBody_pose
{
public:
  explicit Init_RigidBody_pose(::mocap_msgs::msg::RigidBody & msg)
  : msg_(msg)
  {}
  ::mocap_msgs::msg::RigidBody pose(::mocap_msgs::msg::RigidBody::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mocap_msgs::msg::RigidBody msg_;
};

class Init_RigidBody_markers
{
public:
  explicit Init_RigidBody_markers(::mocap_msgs::msg::RigidBody & msg)
  : msg_(msg)
  {}
  Init_RigidBody_pose markers(::mocap_msgs::msg::RigidBody::_markers_type arg)
  {
    msg_.markers = std::move(arg);
    return Init_RigidBody_pose(msg_);
  }

private:
  ::mocap_msgs::msg::RigidBody msg_;
};

class Init_RigidBody_rigid_body_name
{
public:
  Init_RigidBody_rigid_body_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RigidBody_markers rigid_body_name(::mocap_msgs::msg::RigidBody::_rigid_body_name_type arg)
  {
    msg_.rigid_body_name = std::move(arg);
    return Init_RigidBody_markers(msg_);
  }

private:
  ::mocap_msgs::msg::RigidBody msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mocap_msgs::msg::RigidBody>()
{
  return mocap_msgs::msg::builder::Init_RigidBody_rigid_body_name();
}

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__BUILDER_HPP_
