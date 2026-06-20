# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ExceptionContextTestCase_test_missing_section

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = configparser.ConfigParser()
    with self.assertRaises(configparser.NoSectionError) as cm:
        config.set('Section1', 'an_int', '15')
    self.assertIs(cm.exception.__suppress_context__, True)
