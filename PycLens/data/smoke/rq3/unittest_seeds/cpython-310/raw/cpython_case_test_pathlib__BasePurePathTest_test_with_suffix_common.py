# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_with_suffix_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('a/b').with_suffix('.gz'), P('a/b.gz'))
    self.assertEqual(P('/a/b').with_suffix('.gz'), P('/a/b.gz'))
    self.assertEqual(P('a/b.py').with_suffix('.gz'), P('a/b.gz'))
    self.assertEqual(P('/a/b.py').with_suffix('.gz'), P('/a/b.gz'))
    self.assertEqual(P('a/b.py').with_suffix(''), P('a/b'))
    self.assertEqual(P('/a/b').with_suffix(''), P('/a/b'))
    self.assertRaises(ValueError, P('').with_suffix, '.gz')
    self.assertRaises(ValueError, P('.').with_suffix, '.gz')
    self.assertRaises(ValueError, P('/').with_suffix, '.gz')
    self.assertRaises(ValueError, P('a/b').with_suffix, 'gz')
    self.assertRaises(ValueError, P('a/b').with_suffix, '/')
    self.assertRaises(ValueError, P('a/b').with_suffix, '.')
    self.assertRaises(ValueError, P('a/b').with_suffix, '/.gz')
    self.assertRaises(ValueError, P('a/b').with_suffix, 'c/d')
    self.assertRaises(ValueError, P('a/b').with_suffix, '.c/.d')
    self.assertRaises(ValueError, P('a/b').with_suffix, './.d')
    self.assertRaises(ValueError, P('a/b').with_suffix, '.d/.')
    self.assertRaises(ValueError, P('a/b').with_suffix, (self.flavour.sep, 'd'))
