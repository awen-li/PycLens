# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_serializing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = struct.calcsize('i')
    a = array.array('i', [1, 2, 3, 4, 5])
    m = memoryview(a)
    buf = io.BytesIO(m)
    b = bytearray(5 * size)
    buf.readinto(b)
    self.assertEqual(m.tobytes(), b)
    size = struct.calcsize('L')
    nd = ndarray(list(range(12)), shape=[2, 3, 2], format='L')
    m = memoryview(nd)
    buf = io.BytesIO(m)
    b = bytearray(2 * 3 * 2 * size)
    buf.readinto(b)
    self.assertEqual(m.tobytes(), b)
