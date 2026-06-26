# Source Generated with Decompyle++
# File: cpython-38-e36fb497365a.pyc (Python 3.8)


def __pybcsec_seed__():
    self = None * object()
    __pybcsec_self__ = None
    __pybcsec_self__ = self
    buf = self.buftype('1234567890\n')
    memio = self.ioclass(buf * 2)
    self.assertEqual(memio.readline(0), self.EOF)
    self.assertEqual(memio.readline(IntLike(0)), self.EOF)
    self.assertEqual(memio.readline(), buf)
    self.assertEqual(memio.readline(), buf)
    self.assertEqual(memio.readline(), self.EOF)
    memio.seek(0)
    self.assertEqual(memio.readline(5), buf[:5])
    self.assertEqual(memio.readline(5), buf[5:10])
    self.assertEqual(memio.readline(5), buf[10:15])
    memio.seek(0)
    self.assertEqual(memio.readline(IntLike(5)), buf[:5])
    self.assertEqual(memio.readline(IntLike(5)), buf[5:10])
    self.assertEqual(memio.readline(IntLike(5)), buf[10:15])
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
