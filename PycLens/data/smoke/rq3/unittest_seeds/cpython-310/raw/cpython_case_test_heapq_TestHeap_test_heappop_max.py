# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_heappop_max

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = [3, 2]
    self.assertEqual(self.module._heappop_max(h), 3)
    self.assertEqual(self.module._heappop_max(h), 2)
