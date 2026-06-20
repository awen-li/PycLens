# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_setstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.partial(signature)
    f.__setstate__((capture, (1,), dict(a=10), dict(attr=[])))
    self.assertEqual(signature(f), (capture, (1,), dict(a=10), dict(attr=[])))
    self.assertEqual(f(2, b=20), ((1, 2), {'a': 10, 'b': 20}))
    f.__setstate__((capture, (1,), dict(a=10), None))
    self.assertEqual(signature(f), (capture, (1,), dict(a=10), {}))
    self.assertEqual(f(2, b=20), ((1, 2), {'a': 10, 'b': 20}))
    f.__setstate__((capture, (1,), None, None))
    self.assertEqual(f(2, b=20), ((1, 2), {'b': 20}))
    self.assertEqual(f(2), ((1, 2), {}))
    self.assertEqual(f(), ((1,), {}))
    f.__setstate__((capture, (), {}, None))
    self.assertEqual(signature(f), (capture, (), {}, {}))
    self.assertEqual(f(2, b=20), ((2,), {'b': 20}))
    self.assertEqual(f(2), ((2,), {}))
    self.assertEqual(f(), ((), {}))
