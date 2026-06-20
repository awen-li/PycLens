# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_issubclass_bad_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass
    with self.assertRaises(TypeError):
        issubclass({}, A)
    with self.assertRaises(TypeError):
        issubclass(42, A)

    class C:
        __mro__ = 42
    with self.assertRaises(TypeError):
        issubclass(C(), A)
    bogus_subclasses = [None, lambda x: [], lambda : 42, lambda : [42]]
    for (i, func) in enumerate(bogus_subclasses):

        class S(metaclass=abc_ABCMeta):
            __subclasses__ = func
        with self.subTest(i=i):
            with self.assertRaises(TypeError):
                issubclass(int, S)
    exc_msg = 'exception from __subclasses__'

    def raise_exc():
        raise Exception(exc_msg)

    class S(metaclass=abc_ABCMeta):
        __subclasses__ = raise_exc
    with self.assertRaisesRegex(Exception, exc_msg):
        issubclass(int, S)
