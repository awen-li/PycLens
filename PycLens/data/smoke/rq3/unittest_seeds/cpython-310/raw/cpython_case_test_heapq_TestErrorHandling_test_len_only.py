# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestErrorHandling_test_len_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in (self.module.heapify, self.module.heappop):
        self.assertRaises((TypeError, AttributeError), f, LenOnly())
    for f in (self.module.heappush, self.module.heapreplace):
        self.assertRaises((TypeError, AttributeError), f, LenOnly(), 10)
    for f in (self.module.nlargest, self.module.nsmallest):
        self.assertRaises(TypeError, f, 2, LenOnly())
