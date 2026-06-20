# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property_setname_on_property_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class pro(property):

        def __new__(typ, *args, **kwargs):
            return 'abcdef'

    class A:
        pass
    p = property.__new__(pro)
    p.__set_name__(A, 1)
    np = p.getter(lambda self: 1)
