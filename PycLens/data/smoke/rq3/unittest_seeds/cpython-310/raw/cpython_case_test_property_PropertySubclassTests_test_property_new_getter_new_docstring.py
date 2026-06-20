# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertySubclassTests_test_property_new_getter_new_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo(object):

        @PropertySub
        def spam(self):
            """a docstring"""
            return 1

        @spam.getter
        def spam(self):
            """a new docstring"""
            return 2
    self.assertEqual(Foo.spam.__doc__, 'a new docstring')

    class FooBase(object):

        @PropertySub
        def spam(self):
            """a docstring"""
            return 1

    class Foo2(FooBase):

        @FooBase.spam.getter
        def spam(self):
            """a new docstring"""
            return 2
    self.assertEqual(Foo.spam.__doc__, 'a new docstring')
