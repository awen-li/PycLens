# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: RegressionTests_test_sf_950057

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen1():
        hist.append(0)
        yield 1
        hist.append(1)
        raise AssertionError
        hist.append(2)

    def gen2(x):
        hist.append(3)
        yield 2
        hist.append(4)
    hist = []
    self.assertRaises(AssertionError, list, chain(gen1(), gen2(False)))
    self.assertEqual(hist, [0, 1])
    hist = []
    self.assertRaises(AssertionError, list, chain(gen1(), gen2(True)))
    self.assertEqual(hist, [0, 1])
    hist = []
    self.assertRaises(AssertionError, list, cycle(gen1()))
    self.assertEqual(hist, [0, 1])
