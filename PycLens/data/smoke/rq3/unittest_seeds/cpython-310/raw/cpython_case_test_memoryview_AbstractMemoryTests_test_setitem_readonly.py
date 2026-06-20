# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_setitem_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not self.ro_type:
        self.skipTest('no read-only type to test')
    b = self.ro_type(self._source)
    oldrefcount = sys.getrefcount(b)
    m = self._view(b)

    def setitem(value):
        m[0] = value
    self.assertRaises(TypeError, setitem, b'a')
    self.assertRaises(TypeError, setitem, 65)
    self.assertRaises(TypeError, setitem, memoryview(b'a'))
    m = None
    self.assertEqual(sys.getrefcount(b), oldrefcount)
