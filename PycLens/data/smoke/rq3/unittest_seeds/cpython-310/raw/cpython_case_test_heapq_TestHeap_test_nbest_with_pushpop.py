# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_nbest_with_pushpop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.randrange(2000) for i in range(1000)]
    heap = data[:10]
    self.module.heapify(heap)
    for item in data[10:]:
        self.module.heappushpop(heap, item)
    self.assertEqual(list(self.heapiter(heap)), sorted(data)[-10:])
    self.assertEqual(self.module.heappushpop([], 'x'), 'x')
