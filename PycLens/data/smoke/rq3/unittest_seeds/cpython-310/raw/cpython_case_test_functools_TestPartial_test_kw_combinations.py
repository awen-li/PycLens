# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_kw_combinations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture)
    self.assertEqual(p.keywords, {})
    self.assertEqual(p(), ((), {}))
    self.assertEqual(p(a=1), ((), {'a': 1}))
    p = self.partial(capture, a=1)
    self.assertEqual(p.keywords, {'a': 1})
    self.assertEqual(p(), ((), {'a': 1}))
    self.assertEqual(p(b=2), ((), {'a': 1, 'b': 2}))
    self.assertEqual(p(a=3, b=2), ((), {'a': 3, 'b': 2}))
