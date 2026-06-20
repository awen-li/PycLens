# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        b = tp(self._source)
        m = self._view(b)
        L = []

        def callback(wr, b=b):
            L.append(b)
        wr = weakref.ref(m, callback)
        self.assertIs(wr(), m)
        del m
        test.support.gc_collect()
        self.assertIs(wr(), None)
        self.assertIs(L[0], b)
