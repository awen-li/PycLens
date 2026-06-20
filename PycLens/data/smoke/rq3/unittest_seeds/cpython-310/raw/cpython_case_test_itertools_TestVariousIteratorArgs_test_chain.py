# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_chain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            self.assertEqual(list(chain(g(s))), list(g(s)))
            self.assertEqual(list(chain(g(s), g(s))), list(g(s)) + list(g(s)))
        self.assertRaises(TypeError, list, chain(X(s)))
        self.assertRaises(TypeError, list, chain(N(s)))
        self.assertRaises(ZeroDivisionError, list, chain(E(s)))
