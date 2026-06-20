# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_duplicate_option_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    error = configparser.DuplicateOptionError('section', 'option')
    self.assertEqual(error.section, 'section')
    self.assertEqual(error.option, 'option')
    self.assertEqual(error.source, None)
    self.assertEqual(error.lineno, None)
    self.assertEqual(error.args, ('section', 'option', None, None))
    self.assertEqual(str(error), "Option 'option' in section 'section' already exists")
