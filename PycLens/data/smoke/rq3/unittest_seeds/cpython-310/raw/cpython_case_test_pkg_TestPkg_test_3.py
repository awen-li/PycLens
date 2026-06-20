# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkg.py
# case: TestPkg_test_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hier = [('t3', None), ('t3 __init__.py', ''), ('t3 sub', None), ('t3 sub __init__.py', ''), ('t3 sub subsub', None), ('t3 sub subsub __init__.py', 'spam = 1')]
    self.mkhier(hier)
    import t3.sub.subsub
    self.assertEqual(t3.__name__, 't3')
    self.assertEqual(t3.sub.__name__, 't3.sub')
    self.assertEqual(t3.sub.subsub.__name__, 't3.sub.subsub')
