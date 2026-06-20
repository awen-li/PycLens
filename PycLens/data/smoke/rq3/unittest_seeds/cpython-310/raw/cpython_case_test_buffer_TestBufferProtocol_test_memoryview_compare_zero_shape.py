# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_zero_shape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd1 = ndarray([900, 961], shape=[0], format='@h')
    nd2 = ndarray([-900, -961], shape=[0], format='@h')
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
    nd1 = ndarray([900, 961], shape=[0], format='= h0c')
    nd2 = ndarray([-900, -961], shape=[0], format='@   i')
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
