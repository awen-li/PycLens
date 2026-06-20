# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_as_uri

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    with self.assertRaises(ValueError):
        P('/a/b').as_uri()
    with self.assertRaises(ValueError):
        P('c:a/b').as_uri()
    self.assertEqual(P('c:/').as_uri(), 'file:///c:/')
    self.assertEqual(P('c:/a/b.c').as_uri(), 'file:///c:/a/b.c')
    self.assertEqual(P('c:/a/b%#c').as_uri(), 'file:///c:/a/b%25%23c')
    self.assertEqual(P('c:/a/bé').as_uri(), 'file:///c:/a/b%C3%A9')
    self.assertEqual(P('//some/share/').as_uri(), 'file://some/share/')
    self.assertEqual(P('//some/share/a/b.c').as_uri(), 'file://some/share/a/b.c')
    self.assertEqual(P('//some/share/a/b%#cé').as_uri(), 'file://some/share/a/b%25%23c%C3%A9')
