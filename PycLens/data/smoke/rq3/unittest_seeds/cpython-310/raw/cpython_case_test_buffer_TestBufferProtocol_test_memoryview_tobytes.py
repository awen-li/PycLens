# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_tobytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = (-529, 576, -625, 676, -729)
    nd = ndarray(t, shape=[5], format='@h')
    m = memoryview(nd)
    self.assertEqual(m, nd)
    self.assertEqual(m.tobytes(), nd.tobytes())
    nd = ndarray([t], shape=[1], format='>hQiLl')
    m = memoryview(nd)
    self.assertEqual(m, nd)
    self.assertEqual(m.tobytes(), nd.tobytes())
    nd = ndarray([t for _ in range(12)], shape=[2, 2, 3], format='=hQiLl')
    m = memoryview(nd)
    self.assertEqual(m, nd)
    self.assertEqual(m.tobytes(), nd.tobytes())
    nd = ndarray([t for _ in range(120)], shape=[5, 2, 2, 3, 2], format='<hQiLl')
    m = memoryview(nd)
    self.assertEqual(m, nd)
    self.assertEqual(m.tobytes(), nd.tobytes())
    if ctypes:

        class BEPoint(ctypes.BigEndianStructure):
            _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]
        point = BEPoint(100, 200)
        a = memoryview(point)
        self.assertEqual(a.tobytes(), bytes(point))
