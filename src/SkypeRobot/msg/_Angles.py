"""autogenerated by genpy from SkypeRobot/Angles.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Angles(genpy.Message):
  _md5sum = "961f4b7ebde630ec3d43d34559d7d4da"
  _type = "SkypeRobot/Angles"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int16    TrackedNum
int16	 HeadH
int16    HeadV
int16    ShoulderSpin
int16    ShoulderElbowXLeft
int16    ShoulderElbowYLeft
int16    ElbowSpinLeft
int16    ShoulderElbowWristLeft
int16    WristSpinLeft
int16    ElbowWristHandLeft
int16    ShoulderElbowXRight
int16    ShoulderElbowYRight
int16    ElbowSpinRight
int16    ShoulderElbowWristRight
int16    WristSpinRight
int16    ElbowWristHandRight
int16    HandXLeft
int16    HandYLeft
int16    HandXRight
int16    HandYRight

"""
  __slots__ = ['TrackedNum','HeadH','HeadV','ShoulderSpin','ShoulderElbowXLeft','ShoulderElbowYLeft','ElbowSpinLeft','ShoulderElbowWristLeft','WristSpinLeft','ElbowWristHandLeft','ShoulderElbowXRight','ShoulderElbowYRight','ElbowSpinRight','ShoulderElbowWristRight','WristSpinRight','ElbowWristHandRight','HandXLeft','HandYLeft','HandXRight','HandYRight']
  _slot_types = ['int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       TrackedNum,HeadH,HeadV,ShoulderSpin,ShoulderElbowXLeft,ShoulderElbowYLeft,ElbowSpinLeft,ShoulderElbowWristLeft,WristSpinLeft,ElbowWristHandLeft,ShoulderElbowXRight,ShoulderElbowYRight,ElbowSpinRight,ShoulderElbowWristRight,WristSpinRight,ElbowWristHandRight,HandXLeft,HandYLeft,HandXRight,HandYRight

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Angles, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.TrackedNum is None:
        self.TrackedNum = 0
      if self.HeadH is None:
        self.HeadH = 0
      if self.HeadV is None:
        self.HeadV = 0
      if self.ShoulderSpin is None:
        self.ShoulderSpin = 0
      if self.ShoulderElbowXLeft is None:
        self.ShoulderElbowXLeft = 0
      if self.ShoulderElbowYLeft is None:
        self.ShoulderElbowYLeft = 0
      if self.ElbowSpinLeft is None:
        self.ElbowSpinLeft = 0
      if self.ShoulderElbowWristLeft is None:
        self.ShoulderElbowWristLeft = 0
      if self.WristSpinLeft is None:
        self.WristSpinLeft = 0
      if self.ElbowWristHandLeft is None:
        self.ElbowWristHandLeft = 0
      if self.ShoulderElbowXRight is None:
        self.ShoulderElbowXRight = 0
      if self.ShoulderElbowYRight is None:
        self.ShoulderElbowYRight = 0
      if self.ElbowSpinRight is None:
        self.ElbowSpinRight = 0
      if self.ShoulderElbowWristRight is None:
        self.ShoulderElbowWristRight = 0
      if self.WristSpinRight is None:
        self.WristSpinRight = 0
      if self.ElbowWristHandRight is None:
        self.ElbowWristHandRight = 0
      if self.HandXLeft is None:
        self.HandXLeft = 0
      if self.HandYLeft is None:
        self.HandYLeft = 0
      if self.HandXRight is None:
        self.HandXRight = 0
      if self.HandYRight is None:
        self.HandYRight = 0
    else:
      self.TrackedNum = 0
      self.HeadH = 0
      self.HeadV = 0
      self.ShoulderSpin = 0
      self.ShoulderElbowXLeft = 0
      self.ShoulderElbowYLeft = 0
      self.ElbowSpinLeft = 0
      self.ShoulderElbowWristLeft = 0
      self.WristSpinLeft = 0
      self.ElbowWristHandLeft = 0
      self.ShoulderElbowXRight = 0
      self.ShoulderElbowYRight = 0
      self.ElbowSpinRight = 0
      self.ShoulderElbowWristRight = 0
      self.WristSpinRight = 0
      self.ElbowWristHandRight = 0
      self.HandXLeft = 0
      self.HandYLeft = 0
      self.HandXRight = 0
      self.HandYRight = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_20h.pack(_x.TrackedNum, _x.HeadH, _x.HeadV, _x.ShoulderSpin, _x.ShoulderElbowXLeft, _x.ShoulderElbowYLeft, _x.ElbowSpinLeft, _x.ShoulderElbowWristLeft, _x.WristSpinLeft, _x.ElbowWristHandLeft, _x.ShoulderElbowXRight, _x.ShoulderElbowYRight, _x.ElbowSpinRight, _x.ShoulderElbowWristRight, _x.WristSpinRight, _x.ElbowWristHandRight, _x.HandXLeft, _x.HandYLeft, _x.HandXRight, _x.HandYRight))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.TrackedNum, _x.HeadH, _x.HeadV, _x.ShoulderSpin, _x.ShoulderElbowXLeft, _x.ShoulderElbowYLeft, _x.ElbowSpinLeft, _x.ShoulderElbowWristLeft, _x.WristSpinLeft, _x.ElbowWristHandLeft, _x.ShoulderElbowXRight, _x.ShoulderElbowYRight, _x.ElbowSpinRight, _x.ShoulderElbowWristRight, _x.WristSpinRight, _x.ElbowWristHandRight, _x.HandXLeft, _x.HandYLeft, _x.HandXRight, _x.HandYRight,) = _struct_20h.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_20h.pack(_x.TrackedNum, _x.HeadH, _x.HeadV, _x.ShoulderSpin, _x.ShoulderElbowXLeft, _x.ShoulderElbowYLeft, _x.ElbowSpinLeft, _x.ShoulderElbowWristLeft, _x.WristSpinLeft, _x.ElbowWristHandLeft, _x.ShoulderElbowXRight, _x.ShoulderElbowYRight, _x.ElbowSpinRight, _x.ShoulderElbowWristRight, _x.WristSpinRight, _x.ElbowWristHandRight, _x.HandXLeft, _x.HandYLeft, _x.HandXRight, _x.HandYRight))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.TrackedNum, _x.HeadH, _x.HeadV, _x.ShoulderSpin, _x.ShoulderElbowXLeft, _x.ShoulderElbowYLeft, _x.ElbowSpinLeft, _x.ShoulderElbowWristLeft, _x.WristSpinLeft, _x.ElbowWristHandLeft, _x.ShoulderElbowXRight, _x.ShoulderElbowYRight, _x.ElbowSpinRight, _x.ShoulderElbowWristRight, _x.WristSpinRight, _x.ElbowWristHandRight, _x.HandXLeft, _x.HandYLeft, _x.HandXRight, _x.HandYRight,) = _struct_20h.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_20h = struct.Struct("<20h")
