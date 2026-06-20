# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_nsmallest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [(random.randrange(2000), i) for i in range(1000)]
    for f in (None, lambda x: x[0] * 547 % 2000):
        for n in (0, 1, 2, 10, 100, 400, 999, 1000, 1100):
            self.assertEqual(list(self.module.nsmallest(n, data)), sorted(data)[:n])
            self.assertEqual(list(self.module.nsmallest(n, data, key=f)), sorted(data, key=f)[:n])
