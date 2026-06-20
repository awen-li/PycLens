# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamicclassattribute.py
# case: PropertySubclassTests_test_docstring_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo(object):

        @PropertySub
        def spam(self):
            """spam wrapped in DynamicClassAttribute subclass"""
            return 1
    self.assertEqual(Foo.__dict__['spam'].__doc__, 'spam wrapped in DynamicClassAttribute subclass')
