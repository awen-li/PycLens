# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_drive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:').drive, 'c:')
    self.assertEqual(P('c:a/b').drive, 'c:')
    self.assertEqual(P('c:/').drive, 'c:')
    self.assertEqual(P('c:/a/b/').drive, 'c:')
    self.assertEqual(P('//a/b').drive, '\\\\a\\b')
    self.assertEqual(P('//a/b/').drive, '\\\\a\\b')
    self.assertEqual(P('//a/b/c/d').drive, '\\\\a\\b')
