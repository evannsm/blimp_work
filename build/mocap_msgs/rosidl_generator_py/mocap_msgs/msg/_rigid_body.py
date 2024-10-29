# generated from rosidl_generator_py/resource/_idl.py.em
# with input from mocap_msgs:msg/RigidBody.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RigidBody(type):
    """Metaclass of message 'RigidBody'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mocap_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mocap_msgs.msg.RigidBody')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__rigid_body
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__rigid_body
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__rigid_body
            cls._TYPE_SUPPORT = module.type_support_msg__msg__rigid_body
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__rigid_body

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

            from mocap_msgs.msg import Marker
            if Marker.__class__._TYPE_SUPPORT is None:
                Marker.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RigidBody(metaclass=Metaclass_RigidBody):
    """Message class 'RigidBody'."""

    __slots__ = [
        '_rigid_body_name',
        '_markers',
        '_pose',
    ]

    _fields_and_field_types = {
        'rigid_body_name': 'string',
        'markers': 'sequence<mocap_msgs/Marker>',
        'pose': 'geometry_msgs/Pose',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['mocap_msgs', 'msg'], 'Marker')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.rigid_body_name = kwargs.get('rigid_body_name', str())
        self.markers = kwargs.get('markers', [])
        from geometry_msgs.msg import Pose
        self.pose = kwargs.get('pose', Pose())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.rigid_body_name != other.rigid_body_name:
            return False
        if self.markers != other.markers:
            return False
        if self.pose != other.pose:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def rigid_body_name(self):
        """Message field 'rigid_body_name'."""
        return self._rigid_body_name

    @rigid_body_name.setter
    def rigid_body_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'rigid_body_name' field must be of type 'str'"
        self._rigid_body_name = value

    @builtins.property
    def markers(self):
        """Message field 'markers'."""
        return self._markers

    @markers.setter
    def markers(self, value):
        if __debug__:
            from mocap_msgs.msg import Marker
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, Marker) for v in value) and
                 True), \
                "The 'markers' field must be a set or sequence and each value of type 'Marker'"
        self._markers = value

    @builtins.property
    def pose(self):
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'pose' field must be a sub message of type 'Pose'"
        self._pose = value
