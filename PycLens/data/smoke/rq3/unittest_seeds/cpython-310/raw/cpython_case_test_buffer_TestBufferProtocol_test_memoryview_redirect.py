# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = ndarray([1.0 * x for x in range(12)], shape=[12], format='d')
    a = array.array('d', [1.0 * x for x in range(12)])
    for x in (nd, a):
        y = ndarray(x, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
        z = ndarray(y, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
        m = memoryview(z)
        self.assertIs(y.obj, x)
        self.assertIs(z.obj, x)
        self.assertIs(m.obj, x)
        self.assertEqual(m, x)
        self.assertEqual(m, y)
        self.assertEqual(m, z)
        self.assertEqual(m[1:3], x[1:3])
        self.assertEqual(m[1:3], y[1:3])
        self.assertEqual(m[1:3], z[1:3])
        del y, z
        self.assertEqual(m[1:3], x[1:3])
