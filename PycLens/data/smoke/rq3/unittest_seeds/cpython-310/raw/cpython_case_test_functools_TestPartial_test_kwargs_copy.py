# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_kwargs_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'a': 3}
    p = self.partial(capture, **d)
    self.assertEqual(p(), ((), {'a': 3}))
    d['a'] = 5
    self.assertEqual(p(), ((), {'a': 3}))
