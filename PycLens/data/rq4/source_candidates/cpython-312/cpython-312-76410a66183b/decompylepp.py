# Source Generated with Decompyle++
# File: cpython-312-76410a66183b.pyc (Python 3.12)

__pybcsec_seed__ =     self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not os.getuid() != 0 and HAVE_WHEEL_GROUP:
        self.assertRaises(OSError, os.setregid, 0, 0)
    self.assertRaises(TypeError, os.setregid, 'not an int', 0)
    self.assertRaises(TypeError, os.setregid, 0, 'not an int')
    self.assertRaises(OverflowError, os.setregid, self.GID_OVERFLOW, 0)
    self.assertRaises(OverflowError, os.setregid, 0, self.GID_OVERFLOW)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
