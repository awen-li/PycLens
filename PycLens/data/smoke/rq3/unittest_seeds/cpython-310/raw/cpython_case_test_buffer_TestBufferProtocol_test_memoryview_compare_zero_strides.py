# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_zero_strides

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd1 = ndarray([900, 900, 900, 900], shape=[4], format='@L')
    nd2 = ndarray([900], shape=[4], strides=[0], format='L')
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
    nd1 = ndarray([(900, 900)] * 4, shape=[4], format='@ Li')
    nd2 = ndarray([(900, 900)], shape=[4], strides=[0], format='!L  h')
    v = memoryview(nd1)
    w = memoryview(nd2)
    self.assertEqual(v, nd1)
    self.assertEqual(w, nd2)
    self.assertEqual(v, nd2)
    self.assertEqual(w, nd1)
    self.assertEqual(v, w)
