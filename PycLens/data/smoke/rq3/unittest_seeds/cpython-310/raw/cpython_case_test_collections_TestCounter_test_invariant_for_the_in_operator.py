# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_invariant_for_the_in_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter(a=10, b=-2, c=0)
    for elem in c:
        self.assertTrue(elem in c)
        self.assertIn(elem, c)
