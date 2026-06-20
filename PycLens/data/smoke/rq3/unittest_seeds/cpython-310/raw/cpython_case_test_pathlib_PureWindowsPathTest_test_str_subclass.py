# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_str_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_str_subclass('c:')
    self._check_str_subclass('c:a')
    self._check_str_subclass('c:a\\b.txt')
    self._check_str_subclass('c:\\')
    self._check_str_subclass('c:\\a')
    self._check_str_subclass('c:\\a\\b.txt')
    self._check_str_subclass('\\\\some\\share')
    self._check_str_subclass('\\\\some\\share\\a')
    self._check_str_subclass('\\\\some\\share\\a\\b.txt')
