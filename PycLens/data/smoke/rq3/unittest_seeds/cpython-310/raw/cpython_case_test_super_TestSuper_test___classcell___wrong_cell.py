# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___classcell___wrong_cell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            cls = super().__new__(cls, name, bases, namespace)
            B = type('B', (), namespace)
            return cls
    with self.assertRaises(TypeError):

        class A(metaclass=Meta):

            def f(self):
                return __class__
