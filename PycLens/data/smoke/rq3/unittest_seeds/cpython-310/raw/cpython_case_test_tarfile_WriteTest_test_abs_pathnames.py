# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_abs_pathnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform == 'win32':
        self._test_pathname('C:\\foo', 'foo')
    else:
        self._test_pathname('/foo', 'foo')
        self._test_pathname('///foo', 'foo')
