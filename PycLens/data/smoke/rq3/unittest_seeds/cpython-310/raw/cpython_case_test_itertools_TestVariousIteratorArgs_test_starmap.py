# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_starmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in (range(10), range(0), range(100), (7, 11), range(20, 50, 5)):
        for g in (G, I, Ig, S, L, R):
            ss = lzip(s, s)
            self.assertEqual(list(starmap(operator.pow, g(ss))), [x ** x for x in g(s)])
        self.assertRaises(TypeError, starmap, operator.pow, X(ss))
        self.assertRaises(TypeError, starmap, operator.pow, N(ss))
        self.assertRaises(ZeroDivisionError, list, starmap(operator.pow, E(ss)))
