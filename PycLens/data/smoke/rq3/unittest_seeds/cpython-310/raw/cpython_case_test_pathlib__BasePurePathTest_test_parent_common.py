# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_parent_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('a/b/c')
    self.assertEqual(p.parent, P('a/b'))
    self.assertEqual(p.parent.parent, P('a'))
    self.assertEqual(p.parent.parent.parent, P())
    self.assertEqual(p.parent.parent.parent.parent, P())
    p = P('/a/b/c')
    self.assertEqual(p.parent, P('/a/b'))
    self.assertEqual(p.parent.parent, P('/a'))
    self.assertEqual(p.parent.parent.parent, P('/'))
    self.assertEqual(p.parent.parent.parent.parent, P('/'))
