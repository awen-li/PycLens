# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePosixPathTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('//a')
    pp = p.joinpath('b')
    self.assertEqual(pp, P('//a/b'))
    pp = P('/a').joinpath('//c')
    self.assertEqual(pp, P('//c'))
    pp = P('//a').joinpath('/c')
    self.assertEqual(pp, P('/c'))
