# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_sectionproxy_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = configparser.ConfigParser()
    parser.read_string('\n            [section]\n            key = value\n        ')
    self.assertEqual(repr(parser['section']), '<Section: section>')
