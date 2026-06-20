# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_DynamicClassAttribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __getattr__(self, name):
            if name == 'ham':
                return 'spam'
            return super().__getattr__(name)

    class VA(metaclass=Meta):

        @types.DynamicClassAttribute
        def ham(self):
            return 'eggs'
    should_find_dca = inspect.Attribute('ham', 'data', VA, VA.__dict__['ham'])
    self.assertIn(should_find_dca, inspect.classify_class_attrs(VA))
    should_find_ga = inspect.Attribute('ham', 'data', Meta, 'spam')
    self.assertIn(should_find_ga, inspect.classify_class_attrs(VA))
