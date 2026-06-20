# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_getfilesystemencoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fs_encoding = sys.getfilesystemencoding()
    if sys.platform == 'darwin':
        expected = 'utf-8'
    else:
        expected = None
    self.check_fsencoding(fs_encoding, expected)
