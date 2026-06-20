# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocWithMetaClasses_test_virtualClassAttributeWithTwoMeta

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
    fail1 = fail2 = False
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper(Class1)
    expected_text1 = expected_virtualattribute_pattern2 % __name__
    result1 = output.getvalue().strip()
    self.assertEqual(expected_text1, result1)
    output = StringIO()
    helper = pydoc.Helper(output=output)
    helper(Class2)
    expected_text2 = expected_virtualattribute_pattern3 % __name__
    result2 = output.getvalue().strip()
    self.assertEqual(expected_text2, result2)
