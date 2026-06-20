# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_parent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('z:a/b/c')
    self.assertEqual(p.parent, P('z:a/b'))
    self.assertEqual(p.parent.parent, P('z:a'))
    self.assertEqual(p.parent.parent.parent, P('z:'))
    self.assertEqual(p.parent.parent.parent.parent, P('z:'))
    p = P('z:/a/b/c')
    self.assertEqual(p.parent, P('z:/a/b'))
    self.assertEqual(p.parent.parent, P('z:/a'))
    self.assertEqual(p.parent.parent.parent, P('z:/'))
    self.assertEqual(p.parent.parent.parent.parent, P('z:/'))
    p = P('//a/b/c/d')
    self.assertEqual(p.parent, P('//a/b/c'))
    self.assertEqual(p.parent.parent, P('//a/b'))
    self.assertEqual(p.parent.parent.parent, P('//a/b'))
