# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_setstate_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.partial(signature)
    f.__setstate__((capture, MyTuple((1,)), MyDict(a=10), None))
    s = signature(f)
    self.assertEqual(s, (capture, (1,), dict(a=10), {}))
    self.assertIs(type(s[1]), tuple)
    self.assertIs(type(s[2]), dict)
    r = f()
    self.assertEqual(r, ((1,), {'a': 10}))
    self.assertIs(type(r[0]), tuple)
    self.assertIs(type(r[1]), dict)
    f.__setstate__((capture, BadTuple((1,)), {}, None))
    s = signature(f)
    self.assertEqual(s, (capture, (1,), {}, {}))
    self.assertIs(type(s[1]), tuple)
    r = f(2)
    self.assertEqual(r, ((1, 2), {}))
    self.assertIs(type(r[0]), tuple)
