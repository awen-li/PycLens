# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_issue22668

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('H', [256, 256, 256, 256])
    x = memoryview(a)
    m = x.cast('B')
    b = m.cast('H')
    c = b[0:2]
    d = memoryview(b)
    del b
    self.assertEqual(c[0], 256)
    self.assertEqual(d[0], 256)
    self.assertEqual(c.format, 'H')
    self.assertEqual(d.format, 'H')
    _ = m.cast('I')
    self.assertEqual(c[0], 256)
    self.assertEqual(d[0], 256)
    self.assertEqual(c.format, 'H')
    self.assertEqual(d.format, 'H')
