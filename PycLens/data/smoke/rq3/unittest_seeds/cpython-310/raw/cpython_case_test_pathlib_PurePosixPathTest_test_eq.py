# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePosixPathTest_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertNotEqual(P('a/b'), P('A/b'))
    self.assertEqual(P('/a'), P('///a'))
    self.assertNotEqual(P('/a'), P('//a'))
