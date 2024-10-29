// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mocap_msgs:msg/Markers.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKERS__TRAITS_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKERS__TRAITS_HPP_

#include "mocap_msgs/msg/detail/markers__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'markers'
#include "mocap_msgs/msg/detail/marker__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const mocap_msgs::msg::Markers & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_yaml(msg.header, out, indentation + 2);
  }

  // member: frame_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "frame_number: ";
    value_to_yaml(msg.frame_number, out);
    out << "\n";
  }

  // member: markers
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.markers.size() == 0) {
      out << "markers: []\n";
    } else {
      out << "markers:\n";
      for (auto item : msg.markers) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const mocap_msgs::msg::Markers & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<mocap_msgs::msg::Markers>()
{
  return "mocap_msgs::msg::Markers";
}

template<>
inline const char * name<mocap_msgs::msg::Markers>()
{
  return "mocap_msgs/msg/Markers";
}

template<>
struct has_fixed_size<mocap_msgs::msg::Markers>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<mocap_msgs::msg::Markers>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<mocap_msgs::msg::Markers>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKERS__TRAITS_HPP_
