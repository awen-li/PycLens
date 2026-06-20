# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseTrickyFile_test_unicode_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tricky = support.findfile('cfgparser.3')
    cf = self.newconfig()
    with self.assertRaises(UnicodeDecodeError):
        cf.read(tricky, encoding='ascii')
