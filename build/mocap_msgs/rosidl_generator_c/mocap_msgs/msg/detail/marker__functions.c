// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mocap_msgs:msg/Marker.idl
// generated code does not contain a copyright notice
#include "mocap_msgs/msg/detail/marker__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `marker_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `translation`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
mocap_msgs__msg__Marker__init(mocap_msgs__msg__Marker * msg)
{
  if (!msg) {
    return false;
  }
  // id_type
  // marker_index
  // marker_name
  if (!rosidl_runtime_c__String__init(&msg->marker_name)) {
    mocap_msgs__msg__Marker__fini(msg);
    return false;
  }
  // translation
  if (!geometry_msgs__msg__Point__init(&msg->translation)) {
    mocap_msgs__msg__Marker__fini(msg);
    return false;
  }
  return true;
}

void
mocap_msgs__msg__Marker__fini(mocap_msgs__msg__Marker * msg)
{
  if (!msg) {
    return;
  }
  // id_type
  // marker_index
  // marker_name
  rosidl_runtime_c__String__fini(&msg->marker_name);
  // translation
  geometry_msgs__msg__Point__fini(&msg->translation);
}

bool
mocap_msgs__msg__Marker__are_equal(const mocap_msgs__msg__Marker * lhs, const mocap_msgs__msg__Marker * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id_type
  if (lhs->id_type != rhs->id_type) {
    return false;
  }
  // marker_index
  if (lhs->marker_index != rhs->marker_index) {
    return false;
  }
  // marker_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->marker_name), &(rhs->marker_name)))
  {
    return false;
  }
  // translation
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->translation), &(rhs->translation)))
  {
    return false;
  }
  return true;
}

bool
mocap_msgs__msg__Marker__copy(
  const mocap_msgs__msg__Marker * input,
  mocap_msgs__msg__Marker * output)
{
  if (!input || !output) {
    return false;
  }
  // id_type
  output->id_type = input->id_type;
  // marker_index
  output->marker_index = input->marker_index;
  // marker_name
  if (!rosidl_runtime_c__String__copy(
      &(input->marker_name), &(output->marker_name)))
  {
    return false;
  }
  // translation
  if (!geometry_msgs__msg__Point__copy(
      &(input->translation), &(output->translation)))
  {
    return false;
  }
  return true;
}

mocap_msgs__msg__Marker *
mocap_msgs__msg__Marker__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mocap_msgs__msg__Marker * msg = (mocap_msgs__msg__Marker *)allocator.allocate(sizeof(mocap_msgs__msg__Marker), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mocap_msgs__msg__Marker));
  bool success = mocap_msgs__msg__Marker__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mocap_msgs__msg__Marker__destroy(mocap_msgs__msg__Marker * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mocap_msgs__msg__Marker__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mocap_msgs__msg__Marker__Sequence__init(mocap_msgs__msg__Marker__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mocap_msgs__msg__Marker * data = NULL;

  if (size) {
    data = (mocap_msgs__msg__Marker *)allocator.zero_allocate(size, sizeof(mocap_msgs__msg__Marker), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mocap_msgs__msg__Marker__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mocap_msgs__msg__Marker__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mocap_msgs__msg__Marker__Sequence__fini(mocap_msgs__msg__Marker__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mocap_msgs__msg__Marker__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mocap_msgs__msg__Marker__Sequence *
mocap_msgs__msg__Marker__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mocap_msgs__msg__Marker__Sequence * array = (mocap_msgs__msg__Marker__Sequence *)allocator.allocate(sizeof(mocap_msgs__msg__Marker__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mocap_msgs__msg__Marker__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mocap_msgs__msg__Marker__Sequence__destroy(mocap_msgs__msg__Marker__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mocap_msgs__msg__Marker__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mocap_msgs__msg__Marker__Sequence__are_equal(const mocap_msgs__msg__Marker__Sequence * lhs, const mocap_msgs__msg__Marker__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mocap_msgs__msg__Marker__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mocap_msgs__msg__Marker__Sequence__copy(
  const mocap_msgs__msg__Marker__Sequence * input,
  mocap_msgs__msg__Marker__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mocap_msgs__msg__Marker);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mocap_msgs__msg__Marker * data =
      (mocap_msgs__msg__Marker *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mocap_msgs__msg__Marker__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mocap_msgs__msg__Marker__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mocap_msgs__msg__Marker__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
