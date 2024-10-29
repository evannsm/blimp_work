// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKER__TRAITS_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "mocap_msgs/msg/detail/marker__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'translation'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace mocap_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Marker & msg,
  std::ostream & out)
{
  out << "{";
  // member: id_type
  {
    out << "id_type: ";
    rosidl_generator_traits::value_to_yaml(msg.id_type, out);
    out << ", ";
  }

  // member: marker_index
  {
    out << "marker_index: ";
    rosidl_generator_traits::value_to_yaml(msg.marker_index, out);
    out << ", ";
  }

  // member: marker_name
  {
    out << "marker_name: ";
    rosidl_generator_traits::value_to_yaml(msg.marker_name, out);
    out << ", ";
  }

  // member: translation
  {
    out << "translation: ";
    to_flow_style_yaml(msg.translation, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Marker & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: id_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "id_type: ";
    rosidl_generator_traits::value_to_yaml(msg.id_type, out);
    out << "\n";
  }

  // member: marker_index
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "marker_index: ";
    rosidl_generator_traits::value_to_yaml(msg.marker_index, out);
    out << "\n";
  }

  // member: marker_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "marker_name: ";
    rosidl_generator_traits::value_to_yaml(msg.marker_name, out);
    out << "\n";
  }

  // member: translation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "translation:\n";
    to_block_style_yaml(msg.translation, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Marker & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace mocap_msgs

namespace rosidl_generator_traits
{

[[deprecated("use mocap_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mocap_msgs::msg::Marker & msg,
  std::ostream & out, size_t indentation = 0)
{
  mocap_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mocap_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const mocap_msgs::msg::Marker & msg)
{
  return mocap_msgs::msg::to_yaml(msg);
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
