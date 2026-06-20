# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: OperatorsTest_test_explicit_reverse_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(complex.__radd__(3j, 4.0), complex(4.0, 3.0))
    self.assertEqual(float.__rsub__(3.0, 1), -2.0)
