# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_parents_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('a/b/c')
    par = p.parents
    self.assertEqual(len(par), 3)
    self.assertEqual(par[0], P('a/b'))
    self.assertEqual(par[1], P('a'))
    self.assertEqual(par[2], P('.'))
    self.assertEqual(par[-1], P('.'))
    self.assertEqual(par[-2], P('a'))
    self.assertEqual(par[-3], P('a/b'))
    self.assertEqual(par[0:1], (P('a/b'),))
    self.assertEqual(par[:2], (P('a/b'), P('a')))
    self.assertEqual(par[:-1], (P('a/b'), P('a')))
    self.assertEqual(par[1:], (P('a'), P('.')))
    self.assertEqual(par[::2], (P('a/b'), P('.')))
    self.assertEqual(par[::-1], (P('.'), P('a'), P('a/b')))
    self.assertEqual(list(par), [P('a/b'), P('a'), P('.')])
    with self.assertRaises(IndexError):
        par[-4]
    with self.assertRaises(IndexError):
        par[3]
    with self.assertRaises(TypeError):
        par[0] = p
    p = P('/a/b/c')
    par = p.parents
    self.assertEqual(len(par), 3)
    self.assertEqual(par[0], P('/a/b'))
    self.assertEqual(par[1], P('/a'))
    self.assertEqual(par[2], P('/'))
    self.assertEqual(par[-1], P('/'))
    self.assertEqual(par[-2], P('/a'))
    self.assertEqual(par[-3], P('/a/b'))
    self.assertEqual(par[0:1], (P('/a/b'),))
    self.assertEqual(par[:2], (P('/a/b'), P('/a')))
    self.assertEqual(par[:-1], (P('/a/b'), P('/a')))
    self.assertEqual(par[1:], (P('/a'), P('/')))
    self.assertEqual(par[::2], (P('/a/b'), P('/')))
    self.assertEqual(par[::-1], (P('/'), P('/a'), P('/a/b')))
    self.assertEqual(list(par), [P('/a/b'), P('/a'), P('/')])
    with self.assertRaises(IndexError):
        par[-4]
    with self.assertRaises(IndexError):
        par[3]
