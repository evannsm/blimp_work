# generated from rosidl_generator_py/resource/_idl.py.em
# with input from mocap_msgs:msg/Marker.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Marker(type):
    """Metaclass of message 'Marker'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'USE_NAME': 0,
        'USE_INDEX': 1,
        'USE_BOTH': 2,
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
                'mocap_msgs.msg.Marker')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__marker
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__marker
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__marker
            cls._TYPE_SUPPORT = module.type_support_msg__msg__marker
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__marker

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'USE_NAME': cls.__constants['USE_NAME'],
            'USE_INDEX': cls.__constants['USE_INDEX'],
            'USE_BOTH': cls.__constants['USE_BOTH'],
        }

    @property
    def USE_NAME(self):
        """Message constant 'USE_NAME'."""
        return Metaclass_Marker.__constants['USE_NAME']

    @property
    def USE_INDEX(self):
        """Message constant 'USE_INDEX'."""
        return Metaclass_Marker.__constants['USE_INDEX']

    @property
    def USE_BOTH(self):
        """Message constant 'USE_BOTH'."""
        return Metaclass_Marker.__constants['USE_BOTH']


class Marker(metaclass=Metaclass_Marker):
    """
    Message class 'Marker'.

    Constants:
      USE_NAME
      USE_INDEX
      USE_BOTH
    """

    __slots__ = [
        '_id_type',
        '_marker_index',
        '_marker_name',
        '_translation',
    ]

    _fields_and_field_types = {
        'id_type': 'int8',
        'marker_index': 'int32',
        'marker_name': 'string',
        'translation': 'geometry_msgs/Point',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.id_type = kwargs.get('id_type', int())
        self.marker_index = kwargs.get('marker_index', int())
        self.marker_name = kwargs.get('marker_name', str())
        from geometry_msgs.msg import Point
        self.translation = kwargs.get('translation', Point())

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
        if self.id_type != other.id_type:
            return False
        if self.marker_index != other.marker_index:
            return False
        if self.marker_name != other.marker_name:
            return False
        if self.translation != other.translation:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def id_type(self):
        """Message field 'id_type'."""
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id_type' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'id_type' field must be an integer in [-128, 127]"
        self._id_type = value

    @builtins.property
    def marker_index(self):
        """Message field 'marker_index'."""
        return self._marker_index

    @marker_index.setter
    def marker_index(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'marker_index' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'marker_index' field must be an integer in [-2147483648, 2147483647]"
        self._marker_index = value

    @builtins.property
    def marker_name(self):
        """Message field 'marker_name'."""
        return self._marker_name

    @marker_name.setter
    def marker_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'marker_name' field must be of type 'str'"
        self._marker_name = value

    @builtins.property
    def translation(self):
        """Message field 'translation'."""
        return self._translation

    @translation.setter
    def translation(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            assert \
                isinstance(value, Point), \
                "The 'translation' field must be a sub message of type 'Point'"
        self._translation = value
