# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getargspec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertArgSpecEquals(mod.eggs, ['x', 'y'], formatted='(x, y)')
    self.assertArgSpecEquals(mod.spam, ['a', 'b', 'c', 'd', 'e', 'f'], 'g', 'h', (3, 4, 5), '(a, b, c, d=3, e=4, f=5, *g, **h)')
    self.assertRaises(ValueError, self.assertArgSpecEquals, mod2.keyworded, [])
    self.assertRaises(ValueError, self.assertArgSpecEquals, mod2.annotated, [])
    self.assertRaises(ValueError, self.assertArgSpecEquals, mod2.keyword_only_arg, [])
