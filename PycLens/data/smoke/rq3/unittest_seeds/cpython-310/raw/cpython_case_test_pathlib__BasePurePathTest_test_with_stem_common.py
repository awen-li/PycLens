# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_with_stem_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('a/b').with_stem('d'), P('a/d'))
    self.assertEqual(P('/a/b').with_stem('d'), P('/a/d'))
    self.assertEqual(P('a/b.py').with_stem('d'), P('a/d.py'))
    self.assertEqual(P('/a/b.py').with_stem('d'), P('/a/d.py'))
    self.assertEqual(P('/a/b.tar.gz').with_stem('d'), P('/a/d.gz'))
    self.assertEqual(P('a/Dot ending.').with_stem('d'), P('a/d'))
    self.assertEqual(P('/a/Dot ending.').with_stem('d'), P('/a/d'))
    self.assertRaises(ValueError, P('').with_stem, 'd')
    self.assertRaises(ValueError, P('.').with_stem, 'd')
    self.assertRaises(ValueError, P('/').with_stem, 'd')
    self.assertRaises(ValueError, P('a/b').with_stem, '')
    self.assertRaises(ValueError, P('a/b').with_stem, '/c')
    self.assertRaises(ValueError, P('a/b').with_stem, 'c/')
    self.assertRaises(ValueError, P('a/b').with_stem, 'c/d')
