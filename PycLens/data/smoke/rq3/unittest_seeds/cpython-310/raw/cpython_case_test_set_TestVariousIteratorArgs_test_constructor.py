# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestVariousIteratorArgs_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cons in (set, frozenset):
        for s in ('123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
            for g in (G, I, Ig, S, L, R):
                self.assertEqual(sorted(cons(g(s)), key=repr), sorted(g(s), key=repr))
            self.assertRaises(TypeError, cons, X(s))
            self.assertRaises(TypeError, cons, N(s))
            self.assertRaises(ZeroDivisionError, cons, E(s))
