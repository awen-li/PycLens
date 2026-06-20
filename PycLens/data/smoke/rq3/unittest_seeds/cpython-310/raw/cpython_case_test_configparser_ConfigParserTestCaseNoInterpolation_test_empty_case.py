# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseNoInterpolation_test_empty_case

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    self.assertIsNone(cf.read_string(''))
