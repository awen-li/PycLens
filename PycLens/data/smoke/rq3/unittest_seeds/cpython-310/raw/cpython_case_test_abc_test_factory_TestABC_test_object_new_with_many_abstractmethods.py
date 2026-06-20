# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_object_new_with_many_abstractmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def method_one(self):
            pass

        @abc.abstractmethod
        def method_two(self):
            pass
    msg = 'class C with abstract methods method_one, method_two'
    self.assertRaisesRegex(TypeError, msg, C)
