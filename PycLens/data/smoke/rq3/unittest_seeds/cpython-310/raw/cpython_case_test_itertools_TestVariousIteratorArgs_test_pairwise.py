# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_pairwise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            seq = list(g(s))
            expected = list(zip(seq, seq[1:]))
            actual = list(pairwise(g(s)))
            self.assertEqual(actual, expected)
        self.assertRaises(TypeError, pairwise, X(s))
        self.assertRaises(TypeError, pairwise, N(s))
        self.assertRaises(ZeroDivisionError, list, pairwise(E(s)))
