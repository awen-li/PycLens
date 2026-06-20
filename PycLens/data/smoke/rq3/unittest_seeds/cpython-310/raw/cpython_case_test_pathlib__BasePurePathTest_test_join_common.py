# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_join_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('a/b')
    pp = p.joinpath('c')
    self.assertEqual(pp, P('a/b/c'))
    self.assertIs(type(pp), type(p))
    pp = p.joinpath('c', 'd')
    self.assertEqual(pp, P('a/b/c/d'))
    pp = p.joinpath(P('c'))
    self.assertEqual(pp, P('a/b/c'))
    pp = p.joinpath('/c')
    self.assertEqual(pp, P('/c'))
