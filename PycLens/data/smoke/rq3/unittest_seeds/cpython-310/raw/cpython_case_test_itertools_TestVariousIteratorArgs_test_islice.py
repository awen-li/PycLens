# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_islice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('12345', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            self.assertEqual(list(islice(g(s), 1, None, 2)), list(g(s))[1::2])
        self.assertRaises(TypeError, islice, X(s), 10)
        self.assertRaises(TypeError, islice, N(s), 10)
        self.assertRaises(ZeroDivisionError, list, islice(E(s), 10))
