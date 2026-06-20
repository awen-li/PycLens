# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_heappushpop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = []
    x = self.module.heappushpop(h, 10)
    self.assertEqual((h, x), ([], 10))
    h = [10]
    x = self.module.heappushpop(h, 10.0)
    self.assertEqual((h, x), ([10], 10.0))
    self.assertEqual(type(h[0]), int)
    self.assertEqual(type(x), float)
    h = [10]
    x = self.module.heappushpop(h, 9)
    self.assertEqual((h, x), ([10], 9))
    h = [10]
    x = self.module.heappushpop(h, 11)
    self.assertEqual((h, x), ([11], 10))
