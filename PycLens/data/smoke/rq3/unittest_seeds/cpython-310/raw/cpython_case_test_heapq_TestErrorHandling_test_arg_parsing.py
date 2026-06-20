# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestErrorHandling_test_arg_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in (self.module.heapify, self.module.heappop, self.module.heappush, self.module.heapreplace, self.module.nlargest, self.module.nsmallest):
        self.assertRaises((TypeError, AttributeError), f, 10)
