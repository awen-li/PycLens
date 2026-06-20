# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_div

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('C:/a/b')
    self.assertEqual(p / 'x/y', P('C:/a/b/x/y'))
    self.assertEqual(p / 'x' / 'y', P('C:/a/b/x/y'))
    self.assertEqual(p / '/x/y', P('C:/x/y'))
    self.assertEqual(p / '/x' / 'y', P('C:/x/y'))
    self.assertEqual(p / 'D:x/y', P('D:x/y'))
    self.assertEqual(p / 'D:' / 'x/y', P('D:x/y'))
    self.assertEqual(p / 'D:/x/y', P('D:/x/y'))
    self.assertEqual(p / 'D:' / '/x/y', P('D:/x/y'))
    self.assertEqual(p / '//host/share/x/y', P('//host/share/x/y'))
    self.assertEqual(p / 'c:x/y', P('C:/a/b/x/y'))
    self.assertEqual(p / 'c:/x/y', P('C:/x/y'))
