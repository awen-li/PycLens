# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_VirtualAttribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __dir__(cls):
            return ['__class__', '__module__', '__name__', 'BOOM']

        def __getattr__(self, name):
            if name == 'BOOM':
                return 42
            return super().__getattr(name)

    class Class(metaclass=Meta):
        pass
    should_find = inspect.Attribute('BOOM', 'data', Meta, 42)
    self.assertIn(should_find, inspect.classify_class_attrs(Class))
