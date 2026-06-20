# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestBugs_test_undetected_mutation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memorywaster = []
    for i in range(20):

        def mutating_cmp(x, y):
            L.append(3)
            L.pop()
            return (x > y) - (x < y)
        L = [1, 2]
        self.assertRaises(ValueError, L.sort, key=cmp_to_key(mutating_cmp))

        def mutating_cmp(x, y):
            L.append(3)
            del L[:]
            return (x > y) - (x < y)
        self.assertRaises(ValueError, L.sort, key=cmp_to_key(mutating_cmp))
        memorywaster = [memorywaster]
