# Source Generated with Decompyle++
# File: cpython-313-a5402b3d060a.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    instance = MockFileInput()
    fileinput._state = instance
    fileinput.close()
    self.assertExactlyOneInvocation(instance, 'close')
    self.assertIsNone(fileinput._state)

if __name__ == '__main__':
    None()
return None
# WARNING: Decompyle incomplete
