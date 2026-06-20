# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_str_subclass_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_str_subclass('')
    self._check_str_subclass('.')
    self._check_str_subclass('a')
    self._check_str_subclass('a/b.txt')
    self._check_str_subclass('/a/b.txt')
