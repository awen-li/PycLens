# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_filterfalse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in (range(10), range(0), range(1000), (7, 11), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            self.assertEqual(list(filterfalse(isEven, g(s))), [x for x in g(s) if isOdd(x)])
        self.assertRaises(TypeError, filterfalse, isEven, X(s))
        self.assertRaises(TypeError, filterfalse, isEven, N(s))
        self.assertRaises(ZeroDivisionError, list, filterfalse(isEven, E(s)))
