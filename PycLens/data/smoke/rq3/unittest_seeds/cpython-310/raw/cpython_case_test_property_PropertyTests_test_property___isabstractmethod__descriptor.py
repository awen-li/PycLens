# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property___isabstractmethod__descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for val in (True, False, [], [1], '', '1'):

        class C(object):

            def foo(self):
                pass
            foo.__isabstractmethod__ = val
            foo = property(foo)
        self.assertIs(C.foo.__isabstractmethod__, bool(val))

    class NotBool(object):

        def __bool__(self):
            raise ValueError()
        __len__ = __bool__
    with self.assertRaises(ValueError):

        class C(object):

            def foo(self):
                pass
            foo.__isabstractmethod__ = NotBool()
            foo = property(foo)
        C.foo.__isabstractmethod__
