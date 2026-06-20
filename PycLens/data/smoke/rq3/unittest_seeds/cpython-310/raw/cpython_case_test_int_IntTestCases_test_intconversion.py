# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_intconversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ClassicMissingMethods:
        pass
    self.assertRaises(TypeError, int, ClassicMissingMethods())

    class MissingMethods(object):
        pass
    self.assertRaises(TypeError, int, MissingMethods())

    class Foo0:

        def __int__(self):
            return 42
    self.assertEqual(int(Foo0()), 42)

    class Classic:
        pass
    for base in (object, Classic):

        class IntOverridesTrunc(base):

            def __int__(self):
                return 42

            def __trunc__(self):
                return -12
        self.assertEqual(int(IntOverridesTrunc()), 42)

        class JustTrunc(base):

            def __trunc__(self):
                return 42
        self.assertEqual(int(JustTrunc()), 42)

        class ExceptionalTrunc(base):

            def __trunc__(self):
                1 / 0
        with self.assertRaises(ZeroDivisionError):
            int(ExceptionalTrunc())
        for trunc_result_base in (object, Classic):

            class Index(trunc_result_base):

                def __index__(self):
                    return 42

            class TruncReturnsNonInt(base):

                def __trunc__(self):
                    return Index()
            self.assertEqual(int(TruncReturnsNonInt()), 42)

            class Intable(trunc_result_base):

                def __int__(self):
                    return 42

            class TruncReturnsNonIndex(base):

                def __trunc__(self):
                    return Intable()
            self.assertEqual(int(TruncReturnsNonInt()), 42)

            class NonIntegral(trunc_result_base):

                def __trunc__(self):
                    return NonIntegral()

            class TruncReturnsNonIntegral(base):

                def __trunc__(self):
                    return NonIntegral()
            try:
                int(TruncReturnsNonIntegral())
            except TypeError as e:
                self.assertEqual(str(e), '__trunc__ returned non-Integral (type NonIntegral)')
            else:
                self.fail('Failed to raise TypeError with %s' % ((base, trunc_result_base),))

            class BadInt(trunc_result_base):

                def __int__(self):
                    return 42.0

            class TruncReturnsBadInt(base):

                def __trunc__(self):
                    return BadInt()
            with self.assertRaises(TypeError):
                int(TruncReturnsBadInt())
