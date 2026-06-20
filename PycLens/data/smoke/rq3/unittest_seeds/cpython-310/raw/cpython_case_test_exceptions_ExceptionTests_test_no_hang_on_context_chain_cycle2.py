# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_no_hang_on_context_chain_cycle2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Exception):
        pass

    class B(Exception):
        pass

    class C(Exception):
        pass
    with self.assertRaises(C) as cm:
        try:
            raise A()
        except A as _a:
            a = _a
            try:
                raise B()
            except B as _b:
                b = _b
                try:
                    raise C()
                except C as _c:
                    c = _c
                    a.__context__ = c
                    raise c
    self.assertIs(cm.exception, c)
    self.assertIs(c.__context__, b)
    self.assertIs(b.__context__, a)
    self.assertIs(a.__context__, c)
