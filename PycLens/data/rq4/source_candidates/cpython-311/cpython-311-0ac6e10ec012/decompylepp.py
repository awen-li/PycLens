# Source Generated with Decompyle++
# File: cpython-311-0ac6e10ec012.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO((b'abc', b'd', b'efg'))
    bufio = self.tp(rawio)
    self.assertEqual(b'a', bufio.read(1))
    self.assertEqual(b'bc', bufio.read1())
    self.assertEqual(b'd', bufio.read1())
    self.assertEqual(b'efg', bufio.read1(-1))
    self.assertEqual(rawio._reads, 3)
    self.assertEqual(b'', bufio.read1())
    self.assertEqual(rawio._reads, 4)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
if None:
    pass
