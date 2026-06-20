# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_writable_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tp = self.ro_type
    if tp is None:
        self.skipTest('no read-only type to test')
    b = tp(self._source)
    m = self._view(b)
    i = io.BytesIO(b'ZZZZ')
    self.assertRaises(TypeError, i.readinto, m)
