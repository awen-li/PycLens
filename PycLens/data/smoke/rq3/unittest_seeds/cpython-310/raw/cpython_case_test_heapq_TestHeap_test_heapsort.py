# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_heapsort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for trial in range(100):
        size = random.randrange(50)
        data = [random.randrange(25) for i in range(size)]
        if trial & 1:
            heap = data[:]
            self.module.heapify(heap)
        else:
            heap = []
            for item in data:
                self.module.heappush(heap, item)
        heap_sorted = [self.module.heappop(heap) for i in range(size)]
        self.assertEqual(heap_sorted, sorted(data))
