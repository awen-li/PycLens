# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_basic_examples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture, 1, 2, a=10, b=20)
    self.assertTrue(callable(p))
    self.assertEqual(p(3, 4, b=30, c=40), ((1, 2, 3, 4), dict(a=10, b=30, c=40)))
    p = self.partial(map, lambda x: x * 10)
    self.assertEqual(list(p([1, 2, 3, 4])), [10, 20, 30, 40])
