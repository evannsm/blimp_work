// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKER__STRUCT_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'translation'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__mocap_msgs__msg__Marker __attribute__((deprecated))
#else
# define DEPRECATED__mocap_msgs__msg__Marker __declspec(deprecated)
#endif

namespace mocap_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Marker_
{
  using Type = Marker_<ContainerAllocator>;

  explicit Marker_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : translation(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id_type = 0;
      this->marker_index = 0l;
      this->marker_name = "";
    }
  }

  explicit Marker_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : marker_name(_alloc),
    translation(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id_type = 0;
      this->marker_index = 0l;
      this->marker_name = "";
    }
  }

  // field types and members
  using _id_type_type =
    int8_t;
  _id_type_type id_type;
  using _marker_index_type =
    int32_t;
  _marker_index_type marker_index;
  using _marker_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _marker_name_type marker_name;
  using _translation_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _translation_type translation;

  // setters for named parameter idiom
  Type & set__id_type(
    const int8_t & _arg)
  {
    this->id_type = _arg;
    return *this;
  }
  Type & set__marker_index(
    const int32_t & _arg)
  {
    this->marker_index = _arg;
    return *this;
  }
  Type & set__marker_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->marker_name = _arg;
    return *this;
  }
  Type & set__translation(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->translation = _arg;
    return *this;
  }

  // constant declarations
  static constexpr int8_t USE_NAME =
    0;
  static constexpr int8_t USE_INDEX =
    1;
  static constexpr int8_t USE_BOTH =
    2;

  // pointer types
  using RawPtr =
    mocap_msgs::msg::Marker_<ContainerAllocator> *;
  using ConstRawPtr =
    const mocap_msgs::msg::Marker_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mocap_msgs::msg::Marker_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mocap_msgs::msg::Marker_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::Marker_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::Marker_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::Marker_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::Marker_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mocap_msgs::msg::Marker_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mocap_msgs::msg::Marker_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mocap_msgs__msg__Marker
    std::shared_ptr<mocap_msgs::msg::Marker_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mocap_msgs__msg__Marker
    std::shared_ptr<mocap_msgs::msg::Marker_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Marker_ & other) const
  {
    if (this->id_type != other.id_type) {
      return false;
    }
    if (this->marker_index != other.marker_index) {
      return false;
    }
    if (this->marker_name != other.marker_name) {
      return false;
    }
    if (this->translation != other.translation) {
      return false;
    }
    return true;
  }
  bool operator!=(const Marker_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Marker_

// alias to use template instance with default allocator
using Marker =
  mocap_msgs::msg::Marker_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr int8_t Marker_<ContainerAllocator>::USE_NAME;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr int8_t Marker_<ContainerAllocator>::USE_INDEX;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr int8_t Marker_<ContainerAllocator>::USE_BOTH;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKER__STRUCT_HPP_
