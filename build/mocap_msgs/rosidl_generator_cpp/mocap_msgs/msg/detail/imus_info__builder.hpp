// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mocap_msgs:msg/ImusInfo.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__BUILDER_HPP_
#define MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mocap_msgs/msg/detail/imus_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mocap_msgs
{

namespace msg
{

namespace builder
{

class Init_ImusInfo_temperature
{
public:
  explicit Init_ImusInfo_temperature(::mocap_msgs::msg::ImusInfo & msg)
  : msg_(msg)
  {}
  ::mocap_msgs::msg::ImusInfo temperature(::mocap_msgs::msg::ImusInfo::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mocap_msgs::msg::ImusInfo msg_;
};

class Init_ImusInfo_battery_level
{
public:
  explicit Init_ImusInfo_battery_level(::mocap_msgs::msg::ImusInfo & msg)
  : msg_(msg)
  {}
  Init_ImusInfo_temperature battery_level(::mocap_msgs::msg::ImusInfo::_battery_level_type arg)
  {
    msg_.battery_level = std::move(arg);
    return Init_ImusInfo_temperature(msg_);
  }

private:
  ::mocap_msgs::msg::ImusInfo msg_;
};

class Init_ImusInfo_sensor_ids
{
public:
  Init_ImusInfo_sensor_ids()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImusInfo_battery_level sensor_ids(::mocap_msgs::msg::ImusInfo::_sensor_ids_type arg)
  {
    msg_.sensor_ids = std::move(arg);
    return Init_ImusInfo_battery_level(msg_);
  }

private:
  ::mocap_msgs::msg::ImusInfo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mocap_msgs::msg::ImusInfo>()
{
  return mocap_msgs::msg::builder::Init_ImusInfo_sensor_ids();
}

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__BUILDER_HPP_
