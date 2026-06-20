# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_contextmanager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        b = tp(self._source)
        m = self._view(b)
        with m as cm:
            self.assertIs(cm, m)
        self._check_released(m, tp)
        m = self._view(b)
        with m:
            m.release()
