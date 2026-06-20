# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, reversed)
    self.assertRaises(TypeError, reversed, [], 'extra')
