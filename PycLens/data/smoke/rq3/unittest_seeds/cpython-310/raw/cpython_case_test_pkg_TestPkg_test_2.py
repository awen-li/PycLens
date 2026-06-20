# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t2', None), ('t2 __init__.py', "'doc for t2'"), ('t2 sub', None), ('t2 sub __init__.py', ''), ('t2 sub subsub', None), ('t2 sub subsub __init__.py', 'spam = 1')]
    self.mkhier(hier)
    import t2.sub
    import t2.sub.subsub
    self.assertEqual(t2.__name__, 't2')
    self.assertEqual(t2.sub.__name__, 't2.sub')
    self.assertEqual(t2.sub.subsub.__name__, 't2.sub.subsub')
    s = "\n            import t2\n            from t2 import *\n            self.assertEqual(dir(), ['self', 'sub', 't2'])\n            "
    self.run_code(s)
    from t2 import sub
    from t2.sub import subsub
    from t2.sub.subsub import spam
    self.assertEqual(sub.__name__, 't2.sub')
    self.assertEqual(subsub.__name__, 't2.sub.subsub')
    self.assertEqual(sub.subsub.__name__, 't2.sub.subsub')
    for name in ['spam', 'sub', 'subsub', 't2']:
        self.assertTrue(locals()['name'], 'Failed to import %s' % name)
    import t2.sub
    import t2.sub.subsub
    self.assertEqual(t2.__name__, 't2')
    self.assertEqual(t2.sub.__name__, 't2.sub')
    self.assertEqual(t2.sub.subsub.__name__, 't2.sub.subsub')
    s = "\n            from t2 import *\n            self.assertEqual(dir(), ['self', 'sub'])\n            "
    self.run_code(s)
