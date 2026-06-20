# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___class___mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_class = None

    class Meta(type):

        def mro(self):
            self.__dict__['f']()
            return super().mro()

    class A(metaclass=Meta):

        def f():
            nonlocal test_class
            test_class = __class__
    self.assertIs(test_class, A)
