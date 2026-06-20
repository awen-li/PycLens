# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_mangling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def f(self, __a=42, /):
            return __a

        def f2(self, __a=42, /, __b=43):
            return (__a, __b)

        def f3(self, __a=42, /, __b=43, *, __c=44):
            return (__a, __b, __c)
    self.assertEqual(X().f(), 42)
    self.assertEqual(X().f2(), (42, 43))
    self.assertEqual(X().f3(), (42, 43, 44))
