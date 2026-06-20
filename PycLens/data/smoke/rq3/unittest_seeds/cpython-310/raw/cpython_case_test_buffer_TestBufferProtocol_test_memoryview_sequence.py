# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fmt in ('d', 'f'):
        inf = float(1e309)
        ex = array.array(fmt, [1.0, inf, 3.0])
        m = memoryview(ex)
        self.assertIn(1.0, m)
        self.assertIn(1e309, m)
        self.assertIn(3.0, m)
    ex = ndarray(9.0, [], format='f')
    m = memoryview(ex)
    self.assertRaises(TypeError, eval, '9.0 in m', locals())
