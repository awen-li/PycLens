# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_parsing_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError) as cm:
        configparser.ParsingError()
    self.assertEqual(str(cm.exception), "Required argument `source' not given.")
    with self.assertRaises(ValueError) as cm:
        configparser.ParsingError(source='source', filename='filename')
    self.assertEqual(str(cm.exception), "Cannot specify both `filename' and `source'. Use `source'.")
    error = configparser.ParsingError(filename='source')
    self.assertEqual(error.source, 'source')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always', DeprecationWarning)
        self.assertEqual(error.filename, 'source')
        error.filename = 'filename'
        self.assertEqual(error.source, 'filename')
    for warning in w:
        self.assertTrue(warning.category is DeprecationWarning)
