# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestExtendAddTypes_test_filetype_notfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(os_helper.TESTFN)
    self.assertParseFail(['--file', os_helper.TESTFN, '-afoo'], '%s: not a regular file' % os_helper.TESTFN)
