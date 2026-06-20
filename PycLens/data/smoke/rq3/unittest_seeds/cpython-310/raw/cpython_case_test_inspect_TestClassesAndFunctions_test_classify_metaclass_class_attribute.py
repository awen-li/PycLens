# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_metaclass_class_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):
        fish = 'slap'

        def __dir__(self):
            return ['__class__', '__module__', '__name__', 'fish']

    class Class(metaclass=Meta):
        pass
    should_find = inspect.Attribute('fish', 'data', Meta, 'slap')
    self.assertIn(should_find, inspect.classify_class_attrs(Class))
