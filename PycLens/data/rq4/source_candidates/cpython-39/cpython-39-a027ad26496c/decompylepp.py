# Source Generated with Decompyle++
# File: cpython-39-a027ad26496c.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()
    state = memio.__getstate__()
    self.assertEqual(len(state), 128)
    bytearray(state[0])
    self.assertIsInstance(state[1], int)
    if state[2] is not None:
        self.assertIsInstance(state[2], dict)
    memio.close()
    self.assertRaises(ValueError, memio.__getstate__)

if __name__ == '__main__':
    __pybcsec_seed__()
