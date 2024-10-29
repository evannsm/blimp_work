// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mocap_msgs:msg/ImusInfo.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__TRAITS_HPP_
#define MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__TRAITS_HPP_

#include "mocap_msgs/msg/detail/imus_info__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const mocap_msgs::msg::ImusInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sensor_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.sensor_ids.size() == 0) {
      out << "sensor_ids: []\n";
    } else {
      out << "sensor_ids:\n";
      for (auto item : msg.sensor_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: battery_level
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "battery_level: ";
    value_to_yaml(msg.battery_level, out);
    out << "\n";
  }

  // member: temperature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature: ";
    value_to_yaml(msg.temperature, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const mocap_msgs::msg::ImusInfo & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<mocap_msgs::msg::ImusInfo>()
{
  return "mocap_msgs::msg::ImusInfo";
}

template<>
inline const char * name<mocap_msgs::msg::ImusInfo>()
{
  return "mocap_msgs/msg/ImusInfo";
}

template<>
struct has_fixed_size<mocap_msgs::msg::ImusInfo>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<mocap_msgs::msg::ImusInfo>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<mocap_msgs::msg::ImusInfo>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__TRAITS_HPP_
