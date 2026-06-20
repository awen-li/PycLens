# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unary.py
# case: UnaryOpTestCase_test_bad_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for op in ('+', '-', '~'):
        self.assertRaises(TypeError, eval, op + "b'a'")
        self.assertRaises(TypeError, eval, op + "'a'")
    self.assertRaises(TypeError, eval, '~2j')
    self.assertRaises(TypeError, eval, '~2.0')
