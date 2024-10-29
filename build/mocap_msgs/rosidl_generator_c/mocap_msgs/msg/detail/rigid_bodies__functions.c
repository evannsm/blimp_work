// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mocap_msgs:msg/RigidBodies.idl
// generated code does not contain a copyright notice
#include "mocap_msgs/msg/detail/rigid_bodies__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `rigidbodies`
#include "mocap_msgs/msg/detail/rigid_body__functions.h"

bool
mocap_msgs__msg__RigidBodies__init(mocap_msgs__msg__RigidBodies * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    mocap_msgs__msg__RigidBodies__fini(msg);
    return false;
  }
  // frame_number
  // rigidbodies
  if (!mocap_msgs__msg__RigidBody__Sequence__init(&msg->rigidbodies, 0)) {
    mocap_msgs__msg__RigidBodies__fini(msg);
    return false;
  }
  return true;
}

void
mocap_msgs__msg__RigidBodies__fini(mocap_msgs__msg__RigidBodies * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // frame_number
  // rigidbodies
  mocap_msgs__msg__RigidBody__Sequence__fini(&msg->rigidbodies);
}

bool
mocap_msgs__msg__RigidBodies__are_equal(const mocap_msgs__msg__RigidBodies * lhs, const mocap_msgs__msg__RigidBodies * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // frame_number
  if (lhs->frame_number != rhs->frame_number) {
    return false;
  }
  // rigidbodies
  if (!mocap_msgs__msg__RigidBody__Sequence__are_equal(
      &(lhs->rigidbodies), &(rhs->rigidbodies)))
  {
    return false;
  }
  return true;
}

bool
mocap_msgs__msg__RigidBodies__copy(
  const mocap_msgs__msg__RigidBodies * input,
  mocap_msgs__msg__RigidBodies * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // frame_number
  output->frame_number = input->frame_number;
  // rigidbodies
  if (!mocap_msgs__msg__RigidBody__Sequence__copy(
      &(input->rigidbodies), &(output->rigidbodies)))
  {
    return false;
  }
  return true;
}

mocap_msgs__msg__RigidBodies *
mocap_msgs__msg__RigidBodies__create()
{
  mocap_msgs__msg__RigidBodies * msg = (mocap_msgs__msg__RigidBodies *)malloc(sizeof(mocap_msgs__msg__RigidBodies));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mocap_msgs__msg__RigidBodies));
  bool success = mocap_msgs__msg__RigidBodies__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
mocap_msgs__msg__RigidBodies__destroy(mocap_msgs__msg__RigidBodies * msg)
{
  if (msg) {
    mocap_msgs__msg__RigidBodies__fini(msg);
  }
  free(msg);
}


bool
mocap_msgs__msg__RigidBodies__Sequence__init(mocap_msgs__msg__RigidBodies__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  mocap_msgs__msg__RigidBodies * data = NULL;
  if (size) {
    data = (mocap_msgs__msg__RigidBodies *)calloc(size, sizeof(mocap_msgs__msg__RigidBodies));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mocap_msgs__msg__RigidBodies__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mocap_msgs__msg__RigidBodies__fini(&data[i - 1]);
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
mocap_msgs__msg__RigidBodies__Sequence__fini(mocap_msgs__msg__RigidBodies__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mocap_msgs__msg__RigidBodies__fini(&array->data[i]);
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

mocap_msgs__msg__RigidBodies__Sequence *
mocap_msgs__msg__RigidBodies__Sequence__create(size_t size)
{
  mocap_msgs__msg__RigidBodies__Sequence * array = (mocap_msgs__msg__RigidBodies__Sequence *)malloc(sizeof(mocap_msgs__msg__RigidBodies__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = mocap_msgs__msg__RigidBodies__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
mocap_msgs__msg__RigidBodies__Sequence__destroy(mocap_msgs__msg__RigidBodies__Sequence * array)
{
  if (array) {
    mocap_msgs__msg__RigidBodies__Sequence__fini(array);
  }
  free(array);
}

bool
mocap_msgs__msg__RigidBodies__Sequence__are_equal(const mocap_msgs__msg__RigidBodies__Sequence * lhs, const mocap_msgs__msg__RigidBodies__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mocap_msgs__msg__RigidBodies__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mocap_msgs__msg__RigidBodies__Sequence__copy(
  const mocap_msgs__msg__RigidBodies__Sequence * input,
  mocap_msgs__msg__RigidBodies__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mocap_msgs__msg__RigidBodies);
    mocap_msgs__msg__RigidBodies * data =
      (mocap_msgs__msg__RigidBodies *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mocap_msgs__msg__RigidBodies__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          mocap_msgs__msg__RigidBodies__fini(&data[i]);
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
    if (!mocap_msgs__msg__RigidBodies__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
