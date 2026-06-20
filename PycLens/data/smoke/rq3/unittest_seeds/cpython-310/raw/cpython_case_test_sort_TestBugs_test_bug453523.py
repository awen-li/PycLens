# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestBugs_test_bug453523

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __lt__(self, other):
            if L and random.random() < 0.75:
                L.pop()
            else:
                L.append(3)
            return random.random() < 0.5
    L = [C() for i in range(50)]
    self.assertRaises(ValueError, L.sort)
