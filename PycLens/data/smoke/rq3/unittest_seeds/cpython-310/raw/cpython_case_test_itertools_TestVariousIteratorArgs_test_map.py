# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in (range(10), range(0), range(100), (7, 11), range(20, 50, 5)):
        for g in (G, I, Ig, S, L, R):
            self.assertEqual(list(map(onearg, g(s))), [onearg(x) for x in g(s)])
            self.assertEqual(list(map(operator.pow, g(s), g(s))), [x ** x for x in g(s)])
        self.assertRaises(TypeError, map, onearg, X(s))
        self.assertRaises(TypeError, map, onearg, N(s))
        self.assertRaises(ZeroDivisionError, list, map(onearg, E(s)))
