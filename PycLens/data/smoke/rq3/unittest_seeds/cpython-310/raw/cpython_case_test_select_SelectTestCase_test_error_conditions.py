# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_select.py
# case: SelectTestCase_test_error_conditions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, select.select, 1, 2, 3)
    self.assertRaises(TypeError, select.select, [self.Nope()], [], [])
    self.assertRaises(TypeError, select.select, [self.Almost()], [], [])
    self.assertRaises(TypeError, select.select, [], [], [], 'not a number')
    self.assertRaises(ValueError, select.select, [], [], [], -1)
