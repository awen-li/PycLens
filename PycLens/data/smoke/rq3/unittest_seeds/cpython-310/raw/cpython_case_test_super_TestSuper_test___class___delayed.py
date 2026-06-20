# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___class___delayed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_namespace = None

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            nonlocal test_namespace
            test_namespace = namespace
            return None

    class A(metaclass=Meta):

        @staticmethod
        def f():
            return __class__
    self.assertIs(A, None)
    B = type('B', (), test_namespace)
    self.assertIs(B.f(), B)
