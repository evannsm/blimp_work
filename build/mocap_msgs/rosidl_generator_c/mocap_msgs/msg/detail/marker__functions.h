// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#ifndef MOCAP_MSGS__MSG__DETAIL__MARKER__FUNCTIONS_H_
#define MOCAP_MSGS__MSG__DETAIL__MARKER__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "mocap_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "mocap_msgs/msg/detail/marker__struct.h"

/// Initialize msg/Marker message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * mocap_msgs__msg__Marker
 * )) before or use
 * mocap_msgs__msg__Marker__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
bool
mocap_msgs__msg__Marker__init(mocap_msgs__msg__Marker * msg);

/// Finalize msg/Marker message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
void
mocap_msgs__msg__Marker__fini(mocap_msgs__msg__Marker * msg);

/// Create msg/Marker message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * mocap_msgs__msg__Marker__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
mocap_msgs__msg__Marker *
mocap_msgs__msg__Marker__create();

/// Destroy msg/Marker message.
/**
 * It calls
 * mocap_msgs__msg__Marker__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
void
mocap_msgs__msg__Marker__destroy(mocap_msgs__msg__Marker * msg);

/// Check for msg/Marker message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
bool
mocap_msgs__msg__Marker__are_equal(const mocap_msgs__msg__Marker * lhs, const mocap_msgs__msg__Marker * rhs);

/// Copy a msg/Marker message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
bool
mocap_msgs__msg__Marker__copy(
  const mocap_msgs__msg__Marker * input,
  mocap_msgs__msg__Marker * output);

/// Initialize array of msg/Marker messages.
/**
 * It allocates the memory for the number of elements and calls
 * mocap_msgs__msg__Marker__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
bool
mocap_msgs__msg__Marker__Sequence__init(mocap_msgs__msg__Marker__Sequence * array, size_t size);

/// Finalize array of msg/Marker messages.
/**
 * It calls
 * mocap_msgs__msg__Marker__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
void
mocap_msgs__msg__Marker__Sequence__fini(mocap_msgs__msg__Marker__Sequence * array);

/// Create array of msg/Marker messages.
/**
 * It allocates the memory for the array and calls
 * mocap_msgs__msg__Marker__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
mocap_msgs__msg__Marker__Sequence *
mocap_msgs__msg__Marker__Sequence__create(size_t size);

/// Destroy array of msg/Marker messages.
/**
 * It calls
 * mocap_msgs__msg__Marker__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
void
mocap_msgs__msg__Marker__Sequence__destroy(mocap_msgs__msg__Marker__Sequence * array);

/// Check for msg/Marker message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
bool
mocap_msgs__msg__Marker__Sequence__are_equal(const mocap_msgs__msg__Marker__Sequence * lhs, const mocap_msgs__msg__Marker__Sequence * rhs);

/// Copy an array of msg/Marker messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mocap_msgs
bool
mocap_msgs__msg__Marker__Sequence__copy(
  const mocap_msgs__msg__Marker__Sequence * input,
  mocap_msgs__msg__Marker__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MOCAP_MSGS__MSG__DETAIL__MARKER__FUNCTIONS_H_
