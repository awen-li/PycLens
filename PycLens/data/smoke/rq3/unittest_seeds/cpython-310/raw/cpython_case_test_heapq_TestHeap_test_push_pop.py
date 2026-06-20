# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_push_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    heap = []
    data = []
    self.check_invariant(heap)
    for i in range(256):
        item = random.random()
        data.append(item)
        self.module.heappush(heap, item)
        self.check_invariant(heap)
    results = []
    while heap:
        item = self.module.heappop(heap)
        self.check_invariant(heap)
        results.append(item)
    data_sorted = data[:]
    data_sorted.sort()
    self.assertEqual(data_sorted, results)
    self.check_invariant(results)
    self.assertRaises(TypeError, self.module.heappush, [])
    try:
        self.assertRaises(TypeError, self.module.heappush, None, None)
        self.assertRaises(TypeError, self.module.heappop, None)
    except AttributeError:
        pass
