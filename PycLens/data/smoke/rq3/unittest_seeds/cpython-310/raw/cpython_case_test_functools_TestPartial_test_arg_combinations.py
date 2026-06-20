# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_arg_combinations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture)
    self.assertEqual(p(), ((), {}))
    self.assertEqual(p(1, 2), ((1, 2), {}))
    p = self.partial(capture, 1, 2)
    self.assertEqual(p(), ((1, 2), {}))
    self.assertEqual(p(3, 4), ((1, 2, 3, 4), {}))
