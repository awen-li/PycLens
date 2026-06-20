# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestErrorHandling_test_comparison_operator_modifiying_heap_two_heaps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class h(int):

        def __lt__(self, o):
            list2.clear()
            return NotImplemented

    class g(int):

        def __lt__(self, o):
            list1.clear()
            return NotImplemented
    (list1, list2) = ([], [])
    self.module.heappush(list1, h(0))
    self.module.heappush(list2, g(0))
    self.assertRaises((IndexError, RuntimeError), self.module.heappush, list1, g(1))
    self.assertRaises((IndexError, RuntimeError), self.module.heappush, list2, h(1))
