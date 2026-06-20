# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_accumulate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = [1, 2, 3, 4, 5]
    r = [1, 3, 6, 10, 15]
    n = len(s)
    for g in (G, I, Ig, L, R):
        self.assertEqual(list(accumulate(g(s))), r)
    self.assertEqual(list(accumulate(S(s))), [])
    self.assertRaises(TypeError, accumulate, X(s))
    self.assertRaises(TypeError, accumulate, N(s))
    self.assertRaises(ZeroDivisionError, list, accumulate(E(s)))
