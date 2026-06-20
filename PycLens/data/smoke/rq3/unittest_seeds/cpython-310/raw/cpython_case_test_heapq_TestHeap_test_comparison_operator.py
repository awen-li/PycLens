# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_comparison_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def hsort(data, comp):
        data = [comp(x) for x in data]
        self.module.heapify(data)
        return [self.module.heappop(data).x for i in range(len(data))]

    class LT:

        def __init__(self, x):
            self.x = x

        def __lt__(self, other):
            return self.x > other.x

    class LE:

        def __init__(self, x):
            self.x = x

        def __le__(self, other):
            return self.x >= other.x
    data = [random.random() for i in range(100)]
    target = sorted(data, reverse=True)
    self.assertEqual(hsort(data, LT), target)
    self.assertRaises(TypeError, data, LE)
