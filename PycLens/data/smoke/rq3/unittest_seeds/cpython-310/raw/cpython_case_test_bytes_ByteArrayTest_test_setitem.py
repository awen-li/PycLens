# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray([1, 2, 3])
    b[1] = 100
    self.assertEqual(b, bytearray([1, 100, 3]))
    b[-1] = 200
    self.assertEqual(b, bytearray([1, 100, 200]))
    b[0] = Indexable(10)
    self.assertEqual(b, bytearray([10, 100, 200]))
    try:
        b[3] = 0
        self.fail("Didn't raise IndexError")
    except IndexError:
        pass
    try:
        b[-10] = 0
        self.fail("Didn't raise IndexError")
    except IndexError:
        pass
    try:
        b[0] = 256
        self.fail("Didn't raise ValueError")
    except ValueError:
        pass
    try:
        b[0] = Indexable(-1)
        self.fail("Didn't raise ValueError")
    except ValueError:
        pass
    try:
        b[0] = None
        self.fail("Didn't raise TypeError")
    except TypeError:
        pass
