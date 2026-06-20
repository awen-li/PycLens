# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_nonascii_abspath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os_helper.TESTFN_UNDECODABLE and sys.platform not in ('win32', 'darwin'):
        name = os_helper.TESTFN_UNDECODABLE
    elif os_helper.TESTFN_NONASCII:
        name = os_helper.TESTFN_NONASCII
    else:
        self.skipTest('need os_helper.TESTFN_NONASCII')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        with os_helper.temp_cwd(name):
            self.test_abspath()
