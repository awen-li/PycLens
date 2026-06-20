# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestErrorHandling_test_iterable_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in (self.module.nlargest, self.module.nsmallest):
        for s in ('123', '', range(1000), (1, 1.2), range(2000, 2200, 5)):
            for g in (G, I, Ig, L, R):
                self.assertEqual(list(f(2, g(s))), list(f(2, s)))
            self.assertEqual(list(f(2, S(s))), [])
            self.assertRaises(TypeError, f, 2, X(s))
            self.assertRaises(TypeError, f, 2, N(s))
            self.assertRaises(ZeroDivisionError, f, 2, E(s))
