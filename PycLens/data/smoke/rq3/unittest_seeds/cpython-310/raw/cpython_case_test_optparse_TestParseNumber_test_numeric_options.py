# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestParseNumber_test_numeric_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-n', '42', '-l', '0x20'], {'n': 42, 'l': 32}, [])
    self.assertParseOK(['-n', '0b0101', '-l010'], {'n': 5, 'l': 8}, [])
    self.assertParseFail(['-n008'], "option -n: invalid integer value: '008'")
    self.assertParseFail(['-l0b0123'], "option -l: invalid integer value: '0b0123'")
    self.assertParseFail(['-l', '0x12x'], "option -l: invalid integer value: '0x12x'")
