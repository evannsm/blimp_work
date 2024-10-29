// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mocap_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__STRUCT_HPP_
#define MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'markers'
#include "mocap_msgs/msg/detail/marker__struct.hpp"
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__mocap_msgs__msg__RigidBody __attribute__((deprecated))
#else
# define DEPRECATED__mocap_msgs__msg__RigidBody __declspec(deprecated)
#endif

namespace mocap_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RigidBody_
{
  using Type = RigidBody_<ContainerAllocator>;

  explicit RigidBody_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rigid_body_name = "";
    }
  }

  explicit RigidBody_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rigid_body_name(_alloc),
    pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rigid_body_name = "";
    }
  }

  // field types and members
  using _rigid_body_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _rigid_body_name_type rigid_body_name;
  using _markers_type =
    std::vector<mocap_msgs::msg::Marker_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<mocap_msgs::msg::Marker_<ContainerAllocator>>>;
  _markers_type markers;
  using _pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _pose_type pose;

  // setters for named parameter idiom
  Type & set__rigid_body_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->rigid_body_name = _arg;
    return *this;
  }
  Type & set__markers(
    const std::vector<mocap_msgs::msg::Marker_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<mocap_msgs::msg::Marker_<ContainerAllocator>>> & _arg)
  {
    this->markers = _arg;
    return *this;
  }
  Type & set__pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mocap_msgs::msg::RigidBody_<ContainerAllocator> *;
  using ConstRawPtr =
    const mocap_msgs::msg::RigidBody_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::RigidBody_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::RigidBody_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mocap_msgs__msg__RigidBody
    std::shared_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mocap_msgs__msg__RigidBody
    std::shared_ptr<mocap_msgs::msg::RigidBody_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RigidBody_ & other) const
  {
    if (this->rigid_body_name != other.rigid_body_name) {
      return false;
    }
    if (this->markers != other.markers) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    return true;
  }
  bool operator!=(const RigidBody_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RigidBody_

// alias to use template instance with default allocator
using RigidBody =
  mocap_msgs::msg::RigidBody_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__RIGID_BODY__STRUCT_HPP_
