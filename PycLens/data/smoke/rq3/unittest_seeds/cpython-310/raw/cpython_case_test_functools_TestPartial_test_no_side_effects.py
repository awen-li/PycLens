# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_no_side_effects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture, 0, a=1)
    (args1, kw1) = p(1, b=2)
    self.assertTrue(args1 == (0, 1) and kw1 == {'a': 1, 'b': 2})
    (args2, kw2) = p()
    self.assertTrue(args2 == (0,) and kw2 == {'a': 1})
