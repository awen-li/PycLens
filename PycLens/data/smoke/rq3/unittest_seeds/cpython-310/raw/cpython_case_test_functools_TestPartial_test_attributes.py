# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture, 1, 2, a=10, b=20)
    self.assertEqual(p.func, capture)
    self.assertEqual(p.args, (1, 2))
    self.assertEqual(p.keywords, dict(a=10, b=20))
