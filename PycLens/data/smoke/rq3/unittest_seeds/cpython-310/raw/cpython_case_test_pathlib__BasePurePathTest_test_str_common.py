# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_str_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pathstr in ('a', 'a/b', 'a/b/c', '/', '/a/b', '/a/b/c'):
        self._check_str(pathstr, (pathstr,))
    self._check_str('.', ('',))
