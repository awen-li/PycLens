# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def g(obj):
        return 'base'

    class A:
        pass

    class C(A):
        pass

    class B(A):
        pass

    class D(C, B):
        pass

    def g_A(a):
        return 'A'

    def g_B(b):
        return 'B'
    g.register(A, g_A)
    g.register(B, g_B)
    self.assertEqual(g(A()), 'A')
    self.assertEqual(g(B()), 'B')
    self.assertEqual(g(C()), 'A')
    self.assertEqual(g(D()), 'B')
