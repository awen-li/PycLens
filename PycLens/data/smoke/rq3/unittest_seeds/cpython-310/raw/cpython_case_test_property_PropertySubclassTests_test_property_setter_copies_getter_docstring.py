# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertySubclassTests_test_property_setter_copies_getter_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo(object):

        def __init__(self):
            self._spam = 1

        @PropertySub
        def spam(self):
            """spam wrapped in property subclass"""
            return self._spam

        @spam.setter
        def spam(self, value):
            """this docstring is ignored"""
            self._spam = value
    foo = Foo()
    self.assertEqual(foo.spam, 1)
    foo.spam = 2
    self.assertEqual(foo.spam, 2)
    self.assertEqual(Foo.spam.__doc__, 'spam wrapped in property subclass')

    class FooSub(Foo):

        @Foo.spam.setter
        def spam(self, value):
            """another ignored docstring"""
            self._spam = 'eggs'
    foosub = FooSub()
    self.assertEqual(foosub.spam, 1)
    foosub.spam = 7
    self.assertEqual(foosub.spam, 'eggs')
    self.assertEqual(FooSub.spam.__doc__, 'spam wrapped in property subclass')
