// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mocap_msgs:msg/Markers.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKERS__STRUCT_HPP_
#define MOCAP_MSGS__MSG__DETAIL__MARKERS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'markers'
#include "mocap_msgs/msg/detail/marker__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__mocap_msgs__msg__Markers __attribute__((deprecated))
#else
# define DEPRECATED__mocap_msgs__msg__Markers __declspec(deprecated)
#endif

namespace mocap_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Markers_
{
  using Type = Markers_<ContainerAllocator>;

  explicit Markers_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->frame_number = 0ul;
    }
  }

  explicit Markers_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->frame_number = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _frame_number_type =
    uint32_t;
  _frame_number_type frame_number;
  using _markers_type =
    std::vector<mocap_msgs::msg::Marker_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<mocap_msgs::msg::Marker_<ContainerAllocator>>>;
  _markers_type markers;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__frame_number(
    const uint32_t & _arg)
  {
    this->frame_number = _arg;
    return *this;
  }
  Type & set__markers(
    const std::vector<mocap_msgs::msg::Marker_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<mocap_msgs::msg::Marker_<ContainerAllocator>>> & _arg)
  {
    this->markers = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mocap_msgs::msg::Markers_<ContainerAllocator> *;
  using ConstRawPtr =
    const mocap_msgs::msg::Markers_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mocap_msgs::msg::Markers_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mocap_msgs::msg::Markers_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::Markers_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::Markers_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::Markers_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::Markers_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mocap_msgs::msg::Markers_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mocap_msgs::msg::Markers_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mocap_msgs__msg__Markers
    std::shared_ptr<mocap_msgs::msg::Markers_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mocap_msgs__msg__Markers
    std::shared_ptr<mocap_msgs::msg::Markers_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Markers_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->frame_number != other.frame_number) {
      return false;
    }
    if (this->markers != other.markers) {
      return false;
    }
    return true;
  }
  bool operator!=(const Markers_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Markers_

// alias to use template instance with default allocator
using Markers =
  mocap_msgs::msg::Markers_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKERS__STRUCT_HPP_
