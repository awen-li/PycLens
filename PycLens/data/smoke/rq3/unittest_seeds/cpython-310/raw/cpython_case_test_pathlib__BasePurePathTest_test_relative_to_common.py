# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_relative_to_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('a/b')
    self.assertRaises(TypeError, p.relative_to)
    self.assertRaises(TypeError, p.relative_to, b'a')
    self.assertEqual(p.relative_to(P()), P('a/b'))
    self.assertEqual(p.relative_to(''), P('a/b'))
    self.assertEqual(p.relative_to(P('a')), P('b'))
    self.assertEqual(p.relative_to('a'), P('b'))
    self.assertEqual(p.relative_to('a/'), P('b'))
    self.assertEqual(p.relative_to(P('a/b')), P())
    self.assertEqual(p.relative_to('a/b'), P())
    self.assertEqual(p.relative_to('a', 'b'), P())
    self.assertRaises(ValueError, p.relative_to, P('c'))
    self.assertRaises(ValueError, p.relative_to, P('a/b/c'))
    self.assertRaises(ValueError, p.relative_to, P('a/c'))
    self.assertRaises(ValueError, p.relative_to, P('/a'))
    p = P('/a/b')
    self.assertEqual(p.relative_to(P('/')), P('a/b'))
    self.assertEqual(p.relative_to('/'), P('a/b'))
    self.assertEqual(p.relative_to(P('/a')), P('b'))
    self.assertEqual(p.relative_to('/a'), P('b'))
    self.assertEqual(p.relative_to('/a/'), P('b'))
    self.assertEqual(p.relative_to(P('/a/b')), P())
    self.assertEqual(p.relative_to('/a/b'), P())
    self.assertRaises(ValueError, p.relative_to, P('/c'))
    self.assertRaises(ValueError, p.relative_to, P('/a/b/c'))
    self.assertRaises(ValueError, p.relative_to, P('/a/c'))
    self.assertRaises(ValueError, p.relative_to, P())
    self.assertRaises(ValueError, p.relative_to, '')
    self.assertRaises(ValueError, p.relative_to, P('a'))
