# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestVariousIteratorArgs_test_product

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        self.assertRaises(TypeError, product, X(s))
        self.assertRaises(TypeError, product, N(s))
        self.assertRaises(ZeroDivisionError, product, E(s))
