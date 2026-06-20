# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_toreadonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        b = tp(self._source)
        m = self._view(b)
        mm = m.toreadonly()
        self.assertTrue(mm.readonly)
        self.assertTrue(memoryview(mm).readonly)
        self.assertEqual(mm.tolist(), m.tolist())
        mm.release()
        m.tolist()
