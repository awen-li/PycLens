# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_root_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    sep = self.sep
    self.assertEqual(P('').root, '')
    self.assertEqual(P('a/b').root, '')
    self.assertEqual(P('/').root, sep)
    self.assertEqual(P('/a/b').root, sep)
