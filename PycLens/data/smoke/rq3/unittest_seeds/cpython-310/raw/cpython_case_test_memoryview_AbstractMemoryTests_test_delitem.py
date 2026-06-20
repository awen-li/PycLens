# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        b = tp(self._source)
        m = self._view(b)
        with self.assertRaises(TypeError):
            del m[1]
        with self.assertRaises(TypeError):
            del m[1:4]
