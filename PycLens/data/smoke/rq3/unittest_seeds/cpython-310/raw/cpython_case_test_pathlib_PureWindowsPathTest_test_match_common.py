# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_match_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertTrue(P('c:/b.py').match('/*.py'))
    self.assertTrue(P('c:/b.py').match('c:*.py'))
    self.assertTrue(P('c:/b.py').match('c:/*.py'))
    self.assertFalse(P('d:/b.py').match('c:/*.py'))
    self.assertFalse(P('b.py').match('/*.py'))
    self.assertFalse(P('b.py').match('c:*.py'))
    self.assertFalse(P('b.py').match('c:/*.py'))
    self.assertFalse(P('c:b.py').match('/*.py'))
    self.assertFalse(P('c:b.py').match('c:/*.py'))
    self.assertFalse(P('/b.py').match('c:*.py'))
    self.assertFalse(P('/b.py').match('c:/*.py'))
    self.assertTrue(P('//some/share/a.py').match('/*.py'))
    self.assertTrue(P('//some/share/a.py').match('//some/share/*.py'))
    self.assertFalse(P('//other/share/a.py').match('//some/share/*.py'))
    self.assertFalse(P('//some/share/a/b.py').match('//some/share/*.py'))
    self.assertTrue(P('B.py').match('b.PY'))
    self.assertTrue(P('c:/a/B.Py').match('C:/A/*.pY'))
    self.assertTrue(P('//Some/Share/B.Py').match('//somE/sharE/*.pY'))
