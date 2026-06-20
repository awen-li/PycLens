# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_id_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    L = []
    for i in range(10):
        L.insert(len(L) // 2, Empty())
    for a in L:
        for b in L:
            self.assertEqual(a == b, id(a) == id(b), 'a=%r, b=%r' % (a, b))
