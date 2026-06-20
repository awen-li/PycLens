# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_heapify

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for size in list(range(30)) + [20000]:
        heap = [random.random() for dummy in range(size)]
        self.module.heapify(heap)
        self.check_invariant(heap)
    self.assertRaises(TypeError, self.module.heapify, None)
