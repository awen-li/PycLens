# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_raise_does_not_create_context_chain_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Exception):
        pass

    class B(Exception):
        pass

    class C(Exception):
        pass
    try:
        try:
            raise A
        except A as a_:
            a = a_
            try:
                raise B
            except B as b_:
                b = b_
                try:
                    raise C
                except C as c_:
                    c = c_
                    self.assertIsInstance(a, A)
                    self.assertIsInstance(b, B)
                    self.assertIsInstance(c, C)
                    self.assertIsNone(a.__context__)
                    self.assertIs(b.__context__, a)
                    self.assertIs(c.__context__, b)
                    raise a
    except A as e:
        exc = e
    self.assertIs(exc, a)
    self.assertIs(a.__context__, c)
    self.assertIs(c.__context__, b)
    self.assertIsNone(b.__context__)
