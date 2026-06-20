# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ExceptionContextTestCase_test_missing_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = configparser.ConfigParser()
    parser.read_string('\n        [Paths]\n        home_dir: /Users\n        ')
    with self.assertRaises(configparser.NoSectionError) as cm:
        parser.options('test')
    self.assertIs(cm.exception.__suppress_context__, True)
