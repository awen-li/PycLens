# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePosixPathTest_test_is_absolute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertFalse(P().is_absolute())
    self.assertFalse(P('a').is_absolute())
    self.assertFalse(P('a/b/').is_absolute())
    self.assertTrue(P('/').is_absolute())
    self.assertTrue(P('/a').is_absolute())
    self.assertTrue(P('/a/b/').is_absolute())
    self.assertTrue(P('//a').is_absolute())
    self.assertTrue(P('//a/b').is_absolute())
