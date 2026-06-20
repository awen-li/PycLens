# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_arg_combinations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.a.nothing(), ((self.a,), {}))
    self.assertEqual(self.a.nothing(5), ((self.a, 5), {}))
    self.assertEqual(self.a.nothing(c=6), ((self.a,), {'c': 6}))
    self.assertEqual(self.a.nothing(5, c=6), ((self.a, 5), {'c': 6}))
    self.assertEqual(self.a.positional(), ((self.a, 1), {}))
    self.assertEqual(self.a.positional(5), ((self.a, 1, 5), {}))
    self.assertEqual(self.a.positional(c=6), ((self.a, 1), {'c': 6}))
    self.assertEqual(self.a.positional(5, c=6), ((self.a, 1, 5), {'c': 6}))
    self.assertEqual(self.a.keywords(), ((self.a,), {'a': 2}))
    self.assertEqual(self.a.keywords(5), ((self.a, 5), {'a': 2}))
    self.assertEqual(self.a.keywords(c=6), ((self.a,), {'a': 2, 'c': 6}))
    self.assertEqual(self.a.keywords(5, c=6), ((self.a, 5), {'a': 2, 'c': 6}))
    self.assertEqual(self.a.both(), ((self.a, 3), {'b': 4}))
    self.assertEqual(self.a.both(5), ((self.a, 3, 5), {'b': 4}))
    self.assertEqual(self.a.both(c=6), ((self.a, 3), {'b': 4, 'c': 6}))
    self.assertEqual(self.a.both(5, c=6), ((self.a, 3, 5), {'b': 4, 'c': 6}))
    self.assertEqual(self.A.both(self.a, 5, c=6), ((self.a, 3, 5), {'b': 4, 'c': 6}))
    self.assertEqual(self.a.spec_keywords(), ((self.a,), {'self': 1, 'func': 2}))
