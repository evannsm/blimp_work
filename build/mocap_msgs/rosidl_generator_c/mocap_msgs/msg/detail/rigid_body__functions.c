// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mocap_msgs:msg/RigidBody.idl
// generated code does not contain a copyright notice
#include "mocap_msgs/msg/detail/rigid_body__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `rigid_body_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `markers`
#include "mocap_msgs/msg/detail/marker__functions.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
mocap_msgs__msg__RigidBody__init(mocap_msgs__msg__RigidBody * msg)
{
  if (!msg) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__init(&msg->rigid_body_name)) {
    mocap_msgs__msg__RigidBody__fini(msg);
    return false;
  }
  // markers
  if (!mocap_msgs__msg__Marker__Sequence__init(&msg->markers, 0)) {
    mocap_msgs__msg__RigidBody__fini(msg);
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__init(&msg->pose)) {
    mocap_msgs__msg__RigidBody__fini(msg);
    return false;
  }
  return true;
}

void
mocap_msgs__msg__RigidBody__fini(mocap_msgs__msg__RigidBody * msg)
{
  if (!msg) {
    return;
  }
  // rigid_body_name
  rosidl_runtime_c__String__fini(&msg->rigid_body_name);
  // markers
  mocap_msgs__msg__Marker__Sequence__fini(&msg->markers);
  // pose
  geometry_msgs__msg__Pose__fini(&msg->pose);
}

bool
mocap_msgs__msg__RigidBody__are_equal(const mocap_msgs__msg__RigidBody * lhs, const mocap_msgs__msg__RigidBody * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->rigid_body_name), &(rhs->rigid_body_name)))
  {
    return false;
  }
  // markers
  if (!mocap_msgs__msg__Marker__Sequence__are_equal(
      &(lhs->markers), &(rhs->markers)))
  {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  return true;
}

bool
mocap_msgs__msg__RigidBody__copy(
  const mocap_msgs__msg__RigidBody * input,
  mocap_msgs__msg__RigidBody * output)
{
  if (!input || !output) {
    return false;
  }
  // rigid_body_name
  if (!rosidl_runtime_c__String__copy(
      &(input->rigid_body_name), &(output->rigid_body_name)))
  {
    return false;
  }
  // markers
  if (!mocap_msgs__msg__Marker__Sequence__copy(
      &(input->markers), &(output->markers)))
  {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  return true;
}

mocap_msgs__msg__RigidBody *
mocap_msgs__msg__RigidBody__create()
{
  mocap_msgs__msg__RigidBody * msg = (mocap_msgs__msg__RigidBody *)malloc(sizeof(mocap_msgs__msg__RigidBody));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mocap_msgs__msg__RigidBody));
  bool success = mocap_msgs__msg__RigidBody__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
mocap_msgs__msg__RigidBody__destroy(mocap_msgs__msg__RigidBody * msg)
{
  if (msg) {
    mocap_msgs__msg__RigidBody__fini(msg);
  }
  free(msg);
}


bool
mocap_msgs__msg__RigidBody__Sequence__init(mocap_msgs__msg__RigidBody__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  mocap_msgs__msg__RigidBody * data = NULL;
  if (size) {
    data = (mocap_msgs__msg__RigidBody *)calloc(size, sizeof(mocap_msgs__msg__RigidBody));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mocap_msgs__msg__RigidBody__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mocap_msgs__msg__RigidBody__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mocap_msgs__msg__RigidBody__Sequence__fini(mocap_msgs__msg__RigidBody__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mocap_msgs__msg__RigidBody__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mocap_msgs__msg__RigidBody__Sequence *
mocap_msgs__msg__RigidBody__Sequence__create(size_t size)
{
  mocap_msgs__msg__RigidBody__Sequence * array = (mocap_msgs__msg__RigidBody__Sequence *)malloc(sizeof(mocap_msgs__msg__RigidBody__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = mocap_msgs__msg__RigidBody__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
mocap_msgs__msg__RigidBody__Sequence__destroy(mocap_msgs__msg__RigidBody__Sequence * array)
{
  if (array) {
    mocap_msgs__msg__RigidBody__Sequence__fini(array);
  }
  free(array);
}

bool
mocap_msgs__msg__RigidBody__Sequence__are_equal(const mocap_msgs__msg__RigidBody__Sequence * lhs, const mocap_msgs__msg__RigidBody__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mocap_msgs__msg__RigidBody__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mocap_msgs__msg__RigidBody__Sequence__copy(
  const mocap_msgs__msg__RigidBody__Sequence * input,
  mocap_msgs__msg__RigidBody__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mocap_msgs__msg__RigidBody);
    mocap_msgs__msg__RigidBody * data =
      (mocap_msgs__msg__RigidBody *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mocap_msgs__msg__RigidBody__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          mocap_msgs__msg__RigidBody__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mocap_msgs__msg__RigidBody__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
