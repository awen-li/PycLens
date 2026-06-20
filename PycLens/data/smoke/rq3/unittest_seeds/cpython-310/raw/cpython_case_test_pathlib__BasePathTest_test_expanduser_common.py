# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_expanduser_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('~')
    self.assertEqual(p.expanduser(), P(os.path.expanduser('~')))
    p = P('foo')
    self.assertEqual(p.expanduser(), p)
    p = P('/~')
    self.assertEqual(p.expanduser(), p)
    p = P('../~')
    self.assertEqual(p.expanduser(), p)
    p = P(P('').absolute().anchor) / '~'
    self.assertEqual(p.expanduser(), p)
