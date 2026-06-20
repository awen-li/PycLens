# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_with_name_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('a/b').with_name('d.xml'), P('a/d.xml'))
    self.assertEqual(P('/a/b').with_name('d.xml'), P('/a/d.xml'))
    self.assertEqual(P('a/b.py').with_name('d.xml'), P('a/d.xml'))
    self.assertEqual(P('/a/b.py').with_name('d.xml'), P('/a/d.xml'))
    self.assertEqual(P('a/Dot ending.').with_name('d.xml'), P('a/d.xml'))
    self.assertEqual(P('/a/Dot ending.').with_name('d.xml'), P('/a/d.xml'))
    self.assertRaises(ValueError, P('').with_name, 'd.xml')
    self.assertRaises(ValueError, P('.').with_name, 'd.xml')
    self.assertRaises(ValueError, P('/').with_name, 'd.xml')
    self.assertRaises(ValueError, P('a/b').with_name, '')
    self.assertRaises(ValueError, P('a/b').with_name, '/c')
    self.assertRaises(ValueError, P('a/b').with_name, 'c/')
    self.assertRaises(ValueError, P('a/b').with_name, 'c/d')
