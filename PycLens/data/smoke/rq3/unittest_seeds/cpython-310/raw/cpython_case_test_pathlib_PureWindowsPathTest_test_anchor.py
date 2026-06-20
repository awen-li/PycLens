# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_anchor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:').anchor, 'c:')
    self.assertEqual(P('c:a/b').anchor, 'c:')
    self.assertEqual(P('c:/').anchor, 'c:\\')
    self.assertEqual(P('c:/a/b/').anchor, 'c:\\')
    self.assertEqual(P('//a/b').anchor, '\\\\a\\b\\')
    self.assertEqual(P('//a/b/').anchor, '\\\\a\\b\\')
    self.assertEqual(P('//a/b/c/d').anchor, '\\\\a\\b\\')
