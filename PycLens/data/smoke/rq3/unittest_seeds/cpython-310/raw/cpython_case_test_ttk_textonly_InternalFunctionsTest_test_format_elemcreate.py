# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_format_elemcreate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(ttk._format_elemcreate(None), (None, ()))
    self.assertRaises(IndexError, ttk._format_elemcreate, 'image')
    self.assertEqual(ttk._format_elemcreate('image', False, 'test'), ('test ', ()))
    self.assertEqual(ttk._format_elemcreate('image', False, 'test', ('', 'a')), ('test {} a', ()))
    self.assertEqual(ttk._format_elemcreate('image', False, 'test', ('a', 'b', 'c')), ('test {a b} c', ()))
    self.assertEqual(ttk._format_elemcreate('image', False, 'test', ('a', 'b'), a='x'), ('test a b', ('-a', 'x')))
    self.assertEqual(ttk._format_elemcreate('image', True, 'test', ('a', 'b', 'c', 'd'), x=[2, 3]), ('{test {a b c} d}', '-x {2 3}'))
    self.assertRaises(ValueError, ttk._format_elemcreate, 'vsapi')
    self.assertEqual(ttk._format_elemcreate('vsapi', False, 'a', 'b'), ('a b ', ()))
    self.assertEqual(ttk._format_elemcreate('vsapi', False, 'a', 'b', ('a', 'b', 'c')), ('a b {a b} c', ()))
    self.assertEqual(ttk._format_elemcreate('vsapi', False, 'a', 'b', ('a', 'b'), opt='x'), ('a b a b', ('-opt', 'x')))
    self.assertEqual(ttk._format_elemcreate('vsapi', True, 'a', 'b', ('a', 'b', [1, 2]), opt='x'), ('{a b {a b} {1 2}}', '-opt x'))
    self.assertRaises(IndexError, ttk._format_elemcreate, 'from')
    self.assertEqual(ttk._format_elemcreate('from', False, 'a'), ('a', ()))
    self.assertEqual(ttk._format_elemcreate('from', False, 'a', 'b'), ('a', ('b',)))
    self.assertEqual(ttk._format_elemcreate('from', True, 'a', 'b'), ('{a}', 'b'))
