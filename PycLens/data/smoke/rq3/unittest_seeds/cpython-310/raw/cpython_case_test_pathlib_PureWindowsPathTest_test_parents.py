# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    p = P('z:a/b/')
    par = p.parents
    self.assertEqual(len(par), 2)
    self.assertEqual(par[0], P('z:a'))
    self.assertEqual(par[1], P('z:'))
    self.assertEqual(par[0:1], (P('z:a'),))
    self.assertEqual(par[:-1], (P('z:a'),))
    self.assertEqual(par[:2], (P('z:a'), P('z:')))
    self.assertEqual(par[1:], (P('z:'),))
    self.assertEqual(par[::2], (P('z:a'),))
    self.assertEqual(par[::-1], (P('z:'), P('z:a')))
    self.assertEqual(list(par), [P('z:a'), P('z:')])
    with self.assertRaises(IndexError):
        par[2]
    p = P('z:/a/b/')
    par = p.parents
    self.assertEqual(len(par), 2)
    self.assertEqual(par[0], P('z:/a'))
    self.assertEqual(par[1], P('z:/'))
    self.assertEqual(par[0:1], (P('z:/a'),))
    self.assertEqual(par[0:-1], (P('z:/a'),))
    self.assertEqual(par[:2], (P('z:/a'), P('z:/')))
    self.assertEqual(par[1:], (P('z:/'),))
    self.assertEqual(par[::2], (P('z:/a'),))
    self.assertEqual(par[::-1], (P('z:/'), P('z:/a')))
    self.assertEqual(list(par), [P('z:/a'), P('z:/')])
    with self.assertRaises(IndexError):
        par[2]
    p = P('//a/b/c/d')
    par = p.parents
    self.assertEqual(len(par), 2)
    self.assertEqual(par[0], P('//a/b/c'))
    self.assertEqual(par[1], P('//a/b'))
    self.assertEqual(par[0:1], (P('//a/b/c'),))
    self.assertEqual(par[0:-1], (P('//a/b/c'),))
    self.assertEqual(par[:2], (P('//a/b/c'), P('//a/b')))
    self.assertEqual(par[1:], (P('//a/b'),))
    self.assertEqual(par[::2], (P('//a/b/c'),))
    self.assertEqual(par[::-1], (P('//a/b'), P('//a/b/c')))
    self.assertEqual(list(par), [P('//a/b/c'), P('//a/b')])
    with self.assertRaises(IndexError):
        par[2]
