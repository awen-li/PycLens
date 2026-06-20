# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_readfp_deprecation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sio = io.StringIO('\n        [section]\n        option = value\n        ')
    parser = configparser.ConfigParser()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always', DeprecationWarning)
        parser.readfp(sio, filename='StringIO')
    for warning in w:
        self.assertTrue(warning.category is DeprecationWarning)
    self.assertEqual(len(parser), 2)
    self.assertEqual(parser['section']['option'], 'value')
