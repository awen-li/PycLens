# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_groupby

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in (range(10), range(0), range(1000), (7, 11), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            self.assertEqual([k for (k, sb) in groupby(g(s))], list(g(s)))
        self.assertRaises(TypeError, groupby, X(s))
        self.assertRaises(TypeError, groupby, N(s))
        self.assertRaises(ZeroDivisionError, list, groupby(E(s)))
