# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseNoInterpolation_test_none_as_default_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CustomConfigParser(configparser.ConfigParser):
        _DEFAULT_INTERPOLATION = None
    cf = CustomConfigParser()
    cf.read_string(self.ini)
    self.assertMatchesIni(cf)
