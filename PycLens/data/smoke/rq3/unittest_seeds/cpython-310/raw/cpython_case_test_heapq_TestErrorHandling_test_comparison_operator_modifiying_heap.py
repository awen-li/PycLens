# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestErrorHandling_test_comparison_operator_modifiying_heap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EvilClass(int):

        def __lt__(self, o):
            heap.clear()
            return NotImplemented
    heap = []
    self.module.heappush(heap, EvilClass(0))
    self.assertRaises(IndexError, self.module.heappushpop, heap, 1)
