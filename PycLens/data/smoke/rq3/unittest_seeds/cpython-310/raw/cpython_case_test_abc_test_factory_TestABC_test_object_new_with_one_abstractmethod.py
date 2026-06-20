# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_object_new_with_one_abstractmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def method_one(self):
            pass
    msg = 'class C with abstract method method_one'
    self.assertRaisesRegex(TypeError, msg, C)
