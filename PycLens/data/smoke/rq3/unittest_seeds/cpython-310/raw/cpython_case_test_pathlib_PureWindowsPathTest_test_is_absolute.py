# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_is_absolute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertFalse(P().is_absolute())
    self.assertFalse(P('a').is_absolute())
    self.assertFalse(P('a/b/').is_absolute())
    self.assertFalse(P('/').is_absolute())
    self.assertFalse(P('/a').is_absolute())
    self.assertFalse(P('/a/b/').is_absolute())
    self.assertFalse(P('c:').is_absolute())
    self.assertFalse(P('c:a').is_absolute())
    self.assertFalse(P('c:a/b/').is_absolute())
    self.assertTrue(P('c:/').is_absolute())
    self.assertTrue(P('c:/a').is_absolute())
    self.assertTrue(P('c:/a/b/').is_absolute())
    self.assertTrue(P('//a/b').is_absolute())
    self.assertTrue(P('//a/b/').is_absolute())
    self.assertTrue(P('//a/b/c').is_absolute())
    self.assertTrue(P('//a/b/c/d').is_absolute())
