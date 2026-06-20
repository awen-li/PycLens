# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_getbuffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        b = tp(self._source)
        oldrefcount = sys.getrefcount(b)
        m = self._view(b)
        oldviewrefcount = sys.getrefcount(m)
        s = str(m, 'utf-8')
        self._check_contents(tp, b, s.encode('utf-8'))
        self.assertEqual(sys.getrefcount(m), oldviewrefcount)
        m = None
        self.assertEqual(sys.getrefcount(b), oldrefcount)
