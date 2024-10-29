// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mocap_msgs:msg/ImusInfo.idl
// generated code does not contain a copyright notice
#include "mocap_msgs/msg/detail/imus_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `sensor_ids`
#include "rosidl_runtime_c/string_functions.h"

bool
mocap_msgs__msg__ImusInfo__init(mocap_msgs__msg__ImusInfo * msg)
{
  if (!msg) {
    return false;
  }
  // sensor_ids
  if (!rosidl_runtime_c__String__Sequence__init(&msg->sensor_ids, 0)) {
    mocap_msgs__msg__ImusInfo__fini(msg);
    return false;
  }
  // battery_level
  // temperature
  return true;
}

void
mocap_msgs__msg__ImusInfo__fini(mocap_msgs__msg__ImusInfo * msg)
{
  if (!msg) {
    return;
  }
  // sensor_ids
  rosidl_runtime_c__String__Sequence__fini(&msg->sensor_ids);
  // battery_level
  // temperature
}

bool
mocap_msgs__msg__ImusInfo__are_equal(const mocap_msgs__msg__ImusInfo * lhs, const mocap_msgs__msg__ImusInfo * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sensor_ids
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->sensor_ids), &(rhs->sensor_ids)))
  {
    return false;
  }
  // battery_level
  if (lhs->battery_level != rhs->battery_level) {
    return false;
  }
  // temperature
  if (lhs->temperature != rhs->temperature) {
    return false;
  }
  return true;
}

bool
mocap_msgs__msg__ImusInfo__copy(
  const mocap_msgs__msg__ImusInfo * input,
  mocap_msgs__msg__ImusInfo * output)
{
  if (!input || !output) {
    return false;
  }
  // sensor_ids
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->sensor_ids), &(output->sensor_ids)))
  {
    return false;
  }
  // battery_level
  output->battery_level = input->battery_level;
  // temperature
  output->temperature = input->temperature;
  return true;
}

mocap_msgs__msg__ImusInfo *
mocap_msgs__msg__ImusInfo__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mocap_msgs__msg__ImusInfo * msg = (mocap_msgs__msg__ImusInfo *)allocator.allocate(sizeof(mocap_msgs__msg__ImusInfo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mocap_msgs__msg__ImusInfo));
  bool success = mocap_msgs__msg__ImusInfo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mocap_msgs__msg__ImusInfo__destroy(mocap_msgs__msg__ImusInfo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mocap_msgs__msg__ImusInfo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mocap_msgs__msg__ImusInfo__Sequence__init(mocap_msgs__msg__ImusInfo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mocap_msgs__msg__ImusInfo * data = NULL;

  if (size) {
    data = (mocap_msgs__msg__ImusInfo *)allocator.zero_allocate(size, sizeof(mocap_msgs__msg__ImusInfo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mocap_msgs__msg__ImusInfo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mocap_msgs__msg__ImusInfo__fini(&data[i - 1]);
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
mocap_msgs__msg__ImusInfo__Sequence__fini(mocap_msgs__msg__ImusInfo__Sequence * array)
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
      mocap_msgs__msg__ImusInfo__fini(&array->data[i]);
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

mocap_msgs__msg__ImusInfo__Sequence *
mocap_msgs__msg__ImusInfo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mocap_msgs__msg__ImusInfo__Sequence * array = (mocap_msgs__msg__ImusInfo__Sequence *)allocator.allocate(sizeof(mocap_msgs__msg__ImusInfo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mocap_msgs__msg__ImusInfo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mocap_msgs__msg__ImusInfo__Sequence__destroy(mocap_msgs__msg__ImusInfo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mocap_msgs__msg__ImusInfo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mocap_msgs__msg__ImusInfo__Sequence__are_equal(const mocap_msgs__msg__ImusInfo__Sequence * lhs, const mocap_msgs__msg__ImusInfo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mocap_msgs__msg__ImusInfo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mocap_msgs__msg__ImusInfo__Sequence__copy(
  const mocap_msgs__msg__ImusInfo__Sequence * input,
  mocap_msgs__msg__ImusInfo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mocap_msgs__msg__ImusInfo);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mocap_msgs__msg__ImusInfo * data =
      (mocap_msgs__msg__ImusInfo *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mocap_msgs__msg__ImusInfo__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mocap_msgs__msg__ImusInfo__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mocap_msgs__msg__ImusInfo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
