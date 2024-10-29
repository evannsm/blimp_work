// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mocap_msgs:msg/ImusInfo.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__STRUCT_HPP_
#define MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__mocap_msgs__msg__ImusInfo __attribute__((deprecated))
#else
# define DEPRECATED__mocap_msgs__msg__ImusInfo __declspec(deprecated)
#endif

namespace mocap_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ImusInfo_
{
  using Type = ImusInfo_<ContainerAllocator>;

  explicit ImusInfo_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->battery_level = 0.0f;
      this->temperature = 0.0f;
    }
  }

  explicit ImusInfo_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->battery_level = 0.0f;
      this->temperature = 0.0f;
    }
  }

  // field types and members
  using _sensor_ids_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _sensor_ids_type sensor_ids;
  using _battery_level_type =
    float;
  _battery_level_type battery_level;
  using _temperature_type =
    float;
  _temperature_type temperature;

  // setters for named parameter idiom
  Type & set__sensor_ids(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->sensor_ids = _arg;
    return *this;
  }
  Type & set__battery_level(
    const float & _arg)
  {
    this->battery_level = _arg;
    return *this;
  }
  Type & set__temperature(
    const float & _arg)
  {
    this->temperature = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mocap_msgs::msg::ImusInfo_<ContainerAllocator> *;
  using ConstRawPtr =
    const mocap_msgs::msg::ImusInfo_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::ImusInfo_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mocap_msgs::msg::ImusInfo_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mocap_msgs__msg__ImusInfo
    std::shared_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mocap_msgs__msg__ImusInfo
    std::shared_ptr<mocap_msgs::msg::ImusInfo_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ImusInfo_ & other) const
  {
    if (this->sensor_ids != other.sensor_ids) {
      return false;
    }
    if (this->battery_level != other.battery_level) {
      return false;
    }
    if (this->temperature != other.temperature) {
      return false;
    }
    return true;
  }
  bool operator!=(const ImusInfo_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ImusInfo_

// alias to use template instance with default allocator
using ImusInfo =
  mocap_msgs::msg::ImusInfo_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace mocap_msgs

#endif  // MOCAP_MSGS__MSG__DETAIL__IMUS_INFO__STRUCT_HPP_
