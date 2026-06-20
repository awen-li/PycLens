# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_anchor_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    sep = self.sep
    self.assertEqual(P('').anchor, '')
    self.assertEqual(P('a/b').anchor, '')
    self.assertEqual(P('/').anchor, sep)
    self.assertEqual(P('/a/b').anchor, sep)
