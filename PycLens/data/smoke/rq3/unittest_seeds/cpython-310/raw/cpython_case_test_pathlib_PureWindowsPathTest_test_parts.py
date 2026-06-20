# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_parts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('c:a/b')
    parts = p.parts
    self.assertEqual(parts, ('c:', 'a', 'b'))
    p = P('c:/a/b')
    parts = p.parts
    self.assertEqual(parts, ('c:\\', 'a', 'b'))
    p = P('//a/b/c/d')
    parts = p.parts
    self.assertEqual(parts, ('\\\\a\\b\\', 'c', 'd'))
