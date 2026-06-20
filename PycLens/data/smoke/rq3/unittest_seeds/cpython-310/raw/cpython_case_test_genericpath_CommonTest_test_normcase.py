# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_normcase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    normcase = self.pathmodule.normcase
    for p in ['FoO/./BaR', b'FoO/./BaR']:
        p = normcase(p)
        self.assertEqual(p, normcase(p))
    self.assertEqual(normcase(''), '')
    self.assertEqual(normcase(b''), b'')
    for path in (None, True, 0, 2.5, [], bytearray(b''), {'o', 'o'}):
        self.assertRaises(TypeError, normcase, path)
