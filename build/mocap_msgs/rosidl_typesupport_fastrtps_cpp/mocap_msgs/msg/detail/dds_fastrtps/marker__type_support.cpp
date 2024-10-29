// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice
#include "mocap_msgs/msg/detail/marker__rosidl_typesupport_fastrtps_cpp.hpp"
#include "mocap_msgs/msg/detail/marker__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace geometry_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const geometry_msgs::msg::Point &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  geometry_msgs::msg::Point &);
size_t get_serialized_size(
  const geometry_msgs::msg::Point &,
  size_t current_alignment);
size_t
max_serialized_size_Point(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace geometry_msgs


namespace mocap_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
cdr_serialize(
  const mocap_msgs::msg::Marker & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: id_type
  cdr << ros_message.id_type;
  // Member: marker_index
  cdr << ros_message.marker_index;
  // Member: marker_name
  cdr << ros_message.marker_name;
  // Member: translation
  geometry_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.translation,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  mocap_msgs::msg::Marker & ros_message)
{
  // Member: id_type
  cdr >> ros_message.id_type;

  // Member: marker_index
  cdr >> ros_message.marker_index;

  // Member: marker_name
  cdr >> ros_message.marker_name;

  // Member: translation
  geometry_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.translation);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
get_serialized_size(
  const mocap_msgs::msg::Marker & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: id_type
  {
    size_t item_size = sizeof(ros_message.id_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: marker_index
  {
    size_t item_size = sizeof(ros_message.marker_index);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: marker_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.marker_name.size() + 1);
  // Member: translation

  current_alignment +=
    geometry_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.translation, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mocap_msgs
max_serialized_size_Marker(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: id_type
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: marker_index
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: marker_name
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: translation
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        geometry_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_Point(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _Marker__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const mocap_msgs::msg::Marker *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Marker__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<mocap_msgs::msg::Marker *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Marker__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const mocap_msgs::msg::Marker *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Marker__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_Marker(full_bounded, 0);
}

static message_type_support_callbacks_t _Marker__callbacks = {
  "mocap_msgs::msg",
  "Marker",
  _Marker__cdr_serialize,
  _Marker__cdr_deserialize,
  _Marker__get_serialized_size,
  _Marker__max_serialized_size
};

static rosidl_message_type_support_t _Marker__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Marker__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace mocap_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_mocap_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<mocap_msgs::msg::Marker>()
{
  return &mocap_msgs::msg::typesupport_fastrtps_cpp::_Marker__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, mocap_msgs, msg, Marker)() {
  return &mocap_msgs::msg::typesupport_fastrtps_cpp::_Marker__handle;
}

#ifdef __cplusplus
}
#endif
