# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_immutable_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyMeta(type):

        @py_functools.cached_property
        def prop(self):
            return True

    class MyClass(metaclass=MyMeta):
        pass
    with self.assertRaisesRegex(TypeError, "The '__dict__' attribute on 'MyMeta' instance does not support item assignment for caching 'prop' property."):
        MyClass.prop
