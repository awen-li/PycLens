# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_compress

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        n = len(s)
        for g in (G, I, Ig, S, L, R):
            self.assertEqual(list(compress(g(s), repeat(1))), list(g(s)))
        self.assertRaises(TypeError, compress, X(s), repeat(1))
        self.assertRaises(TypeError, compress, N(s), repeat(1))
        self.assertRaises(ZeroDivisionError, list, compress(E(s), repeat(1)))
