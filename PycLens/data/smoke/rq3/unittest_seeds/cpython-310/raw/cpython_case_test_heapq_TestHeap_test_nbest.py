# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_nbest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.randrange(2000) for i in range(1000)]
    heap = data[:10]
    self.module.heapify(heap)
    for item in data[10:]:
        if item > heap[0]:
            self.module.heapreplace(heap, item)
    self.assertEqual(list(self.heapiter(heap)), sorted(data)[-10:])
    self.assertRaises(TypeError, self.module.heapreplace, None)
    self.assertRaises(TypeError, self.module.heapreplace, None, None)
    self.assertRaises(IndexError, self.module.heapreplace, [], None)
