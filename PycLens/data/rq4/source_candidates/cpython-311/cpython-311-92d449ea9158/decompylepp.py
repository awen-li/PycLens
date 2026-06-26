# Source Generated with Decompyle++
# File: cpython-311-92d449ea9158.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = struct.iter_unpack('>IB', bytes(range(1, 11)))
    self.assertEqual(next(it), (16909060, 5))
    self.assertEqual(next(it), (101124105, 10))
    self.assertRaises(StopIteration, next, it)
    self.assertRaises(StopIteration, next, it)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
