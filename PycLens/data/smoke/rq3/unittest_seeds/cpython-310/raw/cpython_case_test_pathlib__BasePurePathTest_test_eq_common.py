# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_eq_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('a/b'), P('a/b'))
    self.assertEqual(P('a/b'), P('a', 'b'))
    self.assertNotEqual(P('a/b'), P('a'))
    self.assertNotEqual(P('a/b'), P('/a/b'))
    self.assertNotEqual(P('a/b'), P())
    self.assertNotEqual(P('/a/b'), P('/'))
    self.assertNotEqual(P(), P('/'))
    self.assertNotEqual(P(), '')
    self.assertNotEqual(P(), {})
    self.assertNotEqual(P(), int)
