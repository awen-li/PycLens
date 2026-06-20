# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestErrorHandling_test_heappop_mutating_heap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    heap = []
    heap.extend((SideEffectLT(i, heap) for i in range(200)))
    with self.assertRaises((IndexError, RuntimeError)):
        self.module.heappop(heap)
