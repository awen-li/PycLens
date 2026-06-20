# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_glob_dotdot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P(BASE)
    self.assertEqual(set(p.glob('..')), {P(BASE, '..')})
    self.assertEqual(set(p.glob('dirA/../file*')), {P(BASE, 'dirA/../fileA')})
    self.assertEqual(set(p.glob('../xyzzy')), set())
