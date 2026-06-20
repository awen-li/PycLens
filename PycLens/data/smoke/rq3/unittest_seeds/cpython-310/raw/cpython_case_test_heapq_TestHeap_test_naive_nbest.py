# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_naive_nbest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.randrange(2000) for i in range(1000)]
    heap = []
    for item in data:
        self.module.heappush(heap, item)
        if len(heap) > 10:
            self.module.heappop(heap)
    heap.sort()
    self.assertEqual(heap, sorted(data)[-10:])
