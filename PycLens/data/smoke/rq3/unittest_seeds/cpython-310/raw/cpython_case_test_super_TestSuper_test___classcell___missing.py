# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test___classcell___missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            namespace.pop('__classcell__', None)
            return super().__new__(cls, name, bases, namespace)

    class WithoutClassRef(metaclass=Meta):
        pass
    expected_error = '__class__ not set.*__classcell__ propagated'
    with self.assertRaisesRegex(RuntimeError, expected_error):

        class WithClassRef(metaclass=Meta):

            def f(self):
                return __class__
