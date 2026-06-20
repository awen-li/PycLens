# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorPickleTestCase_test_attrgetter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    attrgetter = self.module.attrgetter

    class A:
        pass
    a = A()
    a.x = 'X'
    a.y = 'Y'
    a.z = 'Z'
    a.t = A()
    a.t.u = A()
    a.t.u.v = 'V'
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            f = attrgetter('x')
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
            f = attrgetter('x', 'y', 'z')
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
            f = attrgetter('t.u.v')
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
