# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_takewhile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in (range(10), range(0), range(1000), (7, 11), range(2000, 2200, 5)):
        for g in (G, I, Ig, S, L, R):
            tgt = []
            for elem in g(s):
                if not isEven(elem):
                    break
                tgt.append(elem)
            self.assertEqual(list(takewhile(isEven, g(s))), tgt)
        self.assertRaises(TypeError, takewhile, isEven, X(s))
        self.assertRaises(TypeError, takewhile, isEven, N(s))
        self.assertRaises(ZeroDivisionError, list, takewhile(isEven, E(s)))
