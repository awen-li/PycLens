# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_is_relative_to_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('a/b')
    self.assertRaises(TypeError, p.is_relative_to)
    self.assertRaises(TypeError, p.is_relative_to, b'a')
    self.assertTrue(p.is_relative_to(P()))
    self.assertTrue(p.is_relative_to(''))
    self.assertTrue(p.is_relative_to(P('a')))
    self.assertTrue(p.is_relative_to('a/'))
    self.assertTrue(p.is_relative_to(P('a/b')))
    self.assertTrue(p.is_relative_to('a/b'))
    self.assertTrue(p.is_relative_to('a', 'b'))
    self.assertFalse(p.is_relative_to(P('c')))
    self.assertFalse(p.is_relative_to(P('a/b/c')))
    self.assertFalse(p.is_relative_to(P('a/c')))
    self.assertFalse(p.is_relative_to(P('/a')))
    p = P('/a/b')
    self.assertTrue(p.is_relative_to(P('/')))
    self.assertTrue(p.is_relative_to('/'))
    self.assertTrue(p.is_relative_to(P('/a')))
    self.assertTrue(p.is_relative_to('/a'))
    self.assertTrue(p.is_relative_to('/a/'))
    self.assertTrue(p.is_relative_to(P('/a/b')))
    self.assertTrue(p.is_relative_to('/a/b'))
    self.assertFalse(p.is_relative_to(P('/c')))
    self.assertFalse(p.is_relative_to(P('/a/b/c')))
    self.assertFalse(p.is_relative_to(P('/a/c')))
    self.assertFalse(p.is_relative_to(P()))
    self.assertFalse(p.is_relative_to(''))
    self.assertFalse(p.is_relative_to(P('a')))
