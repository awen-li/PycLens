# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___class___new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_class = None

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            nonlocal test_class
            self = super().__new__(cls, name, bases, namespace)
            test_class = self.f()
            return self

    class A(metaclass=Meta):

        @staticmethod
        def f():
            return __class__
    self.assertIs(test_class, A)
