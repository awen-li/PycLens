# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_VirtualAttribute_multi_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta1(type):

        def __dir__(cls):
            return ['__class__', '__module__', '__name__', 'one']

        def __getattr__(self, name):
            if name == 'one':
                return 1
            return super().__getattr__(name)

    class Meta2(type):

        def __dir__(cls):
            return ['__class__', '__module__', '__name__', 'two']

        def __getattr__(self, name):
            if name == 'two':
                return 2
            return super().__getattr__(name)

    class Meta3(Meta1, Meta2):

        def __dir__(cls):
            return list(sorted(set(['__class__', '__module__', '__name__', 'three'] + Meta1.__dir__(cls) + Meta2.__dir__(cls))))

        def __getattr__(self, name):
            if name == 'three':
                return 3
            return super().__getattr__(name)

    class Class1(metaclass=Meta1):
        pass

    class Class2(Class1, metaclass=Meta3):
        pass
    should_find1 = inspect.Attribute('one', 'data', Meta1, 1)
    should_find2 = inspect.Attribute('two', 'data', Meta2, 2)
    should_find3 = inspect.Attribute('three', 'data', Meta3, 3)
    cca = inspect.classify_class_attrs(Class2)
    for sf in (should_find1, should_find2, should_find3):
        self.assertIn(sf, cca)
