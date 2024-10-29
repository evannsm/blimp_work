// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mocap_msgs:msg/RigidBodies.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__RIGID_BODIES__TRAITS_HPP_
#define MOCAP_MSGS__MSG__DETAIL__RIGID_BODIES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "mocap_msgs/msg/detail/rigid_bodies__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'rigidbodies'
#include "mocap_msgs/msg/detail/rigid_body__traits.hpp"

namespace mocap_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RigidBodies & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: frame_number
  {
    out << "frame_number: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_number, out);
    out << ", ";
  }

  // member: rigidbodies
  {
    if (msg.rigidbodies.size() == 0) {
      out << "rigidbodies: []";
    } else {
      out << "rigidbodies: [";
      size_t pending_items = msg.rigidbodies.size();
      for (auto item : msg.rigidbodies) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RigidBodies & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: frame_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "frame_number: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_number, out);
    out << "\n";
  }

  // member: rigidbodies
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.rigidbodies.size() == 0) {
      out << "rigidbodies: []\n";
    } else {
      out << "rigidbodies:\n";
      for (auto item : msg.rigidbodies) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RigidBodies & msg, bool use_flow_style = false)
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
  const mocap_msgs::msg::RigidBodies & msg,
  std::ostream & out, size_t indentation = 0)
{
  mocap_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mocap_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const mocap_msgs::msg::RigidBodies & msg)
{
  return mocap_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<mocap_msgs::msg::RigidBodies>()
{
  return "mocap_msgs::msg::RigidBodies";
}

template<>
inline const char * name<mocap_msgs::msg::RigidBodies>()
{
  return "mocap_msgs/msg/RigidBodies";
}

template<>
struct has_fixed_size<mocap_msgs::msg::RigidBodies>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<mocap_msgs::msg::RigidBodies>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<mocap_msgs::msg::RigidBodies>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MOCAP_MSGS__MSG__DETAIL__RIGID_BODIES__TRAITS_HPP_
