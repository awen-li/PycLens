# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_wrapped_descriptor_inside_classmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BoundWrapper:

        def __init__(self, wrapped):
            self.__wrapped__ = wrapped

        def __call__(self, *args, **kwargs):
            return self.__wrapped__(*args, **kwargs)

    class Wrapper:

        def __init__(self, wrapped):
            self.__wrapped__ = wrapped

        def __get__(self, instance, owner):
            bound_function = self.__wrapped__.__get__(instance, owner)
            return BoundWrapper(bound_function)

    def decorator(wrapped):
        return Wrapper(wrapped)

    class Class:

        @decorator
        @classmethod
        def inner(cls):
            return 'spam'

        @classmethod
        @decorator
        def outer(cls):
            return 'eggs'
    self.assertEqual(Class.inner(), 'spam')
    self.assertEqual(Class.outer(), 'eggs')
    self.assertEqual(Class().inner(), 'spam')
    self.assertEqual(Class().outer(), 'eggs')
