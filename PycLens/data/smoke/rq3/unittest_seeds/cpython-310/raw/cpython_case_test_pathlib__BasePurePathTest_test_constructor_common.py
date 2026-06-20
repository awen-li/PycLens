# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_constructor_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('a')
    self.assertIsInstance(p, P)
    P('a', 'b', 'c')
    P('/a', 'b', 'c')
    P('a/b/c')
    P('/a/b/c')
    P(FakePath('a/b/c'))
    self.assertEqual(P(P('a')), P('a'))
    self.assertEqual(P(P('a'), 'b'), P('a/b'))
    self.assertEqual(P(P('a'), P('b')), P('a/b'))
    self.assertEqual(P(P('a'), P('b'), P('c')), P(FakePath('a/b/c')))
