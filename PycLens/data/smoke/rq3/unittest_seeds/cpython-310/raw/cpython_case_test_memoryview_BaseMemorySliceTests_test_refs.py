# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: BaseMemorySliceTests_test_refs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        m = memoryview(tp(self._source))
        oldrefcount = sys.getrefcount(m)
        m[1:2]
        self.assertEqual(sys.getrefcount(m), oldrefcount)
