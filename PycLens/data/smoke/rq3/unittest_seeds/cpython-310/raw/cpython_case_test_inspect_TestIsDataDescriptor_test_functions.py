# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestIsDataDescriptor_test_functions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test(object):

        def instance_method(self):
            pass

        @classmethod
        def class_method(cls):
            pass

        @staticmethod
        def static_method():
            pass

    def function():
        pass
    a_lambda = lambda : None
    self.assertFalse(inspect.isdatadescriptor(Test().instance_method), 'a instance method is not a data descriptor')
    self.assertFalse(inspect.isdatadescriptor(Test().class_method), 'a class method is not a data descriptor')
    self.assertFalse(inspect.isdatadescriptor(Test().static_method), 'a static method is not a data descriptor')
    self.assertFalse(inspect.isdatadescriptor(function), 'a function is not a data descriptor')
    self.assertFalse(inspect.isdatadescriptor(a_lambda), 'a lambda is not a data descriptor')
