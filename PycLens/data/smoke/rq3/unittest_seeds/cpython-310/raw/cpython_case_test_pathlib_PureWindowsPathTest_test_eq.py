# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:a/b'), P('c:a/b'))
    self.assertEqual(P('c:a/b'), P('c:', 'a', 'b'))
    self.assertNotEqual(P('c:a/b'), P('d:a/b'))
    self.assertNotEqual(P('c:a/b'), P('c:/a/b'))
    self.assertNotEqual(P('/a/b'), P('c:/a/b'))
    self.assertEqual(P('a/B'), P('A/b'))
    self.assertEqual(P('C:a/B'), P('c:A/b'))
    self.assertEqual(P('//Some/SHARE/a/B'), P('//somE/share/A/b'))
