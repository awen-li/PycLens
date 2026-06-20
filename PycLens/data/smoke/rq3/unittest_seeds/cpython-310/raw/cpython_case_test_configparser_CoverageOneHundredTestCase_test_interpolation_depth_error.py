# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_interpolation_depth_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    error = configparser.InterpolationDepthError('option', 'section', 'rawval')
    self.assertEqual(error.args, ('option', 'section', 'rawval'))
    self.assertEqual(error.option, 'option')
    self.assertEqual(error.section, 'section')
