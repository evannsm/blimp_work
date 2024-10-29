// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKER__TRAITS_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKER__TRAITS_HPP_

#include "mocap_msgs/msg/detail/marker__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'translation'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const mocap_msgs::msg::Marker & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: id_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "id_type: ";
    value_to_yaml(msg.id_type, out);
    out << "\n";
  }

  // member: marker_index
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "marker_index: ";
    value_to_yaml(msg.marker_index, out);
    out << "\n";
  }

  // member: marker_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "marker_name: ";
    value_to_yaml(msg.marker_name, out);
    out << "\n";
  }

  // member: translation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "translation:\n";
    to_yaml(msg.translation, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const mocap_msgs::msg::Marker & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<mocap_msgs::msg::Marker>()
{
  return "mocap_msgs::msg::Marker";
}

template<>
inline const char * name<mocap_msgs::msg::Marker>()
{
  return "mocap_msgs/msg/Marker";
}

template<>
struct has_fixed_size<mocap_msgs::msg::Marker>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<mocap_msgs::msg::Marker>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<mocap_msgs::msg::Marker>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKER__TRAITS_HPP_
