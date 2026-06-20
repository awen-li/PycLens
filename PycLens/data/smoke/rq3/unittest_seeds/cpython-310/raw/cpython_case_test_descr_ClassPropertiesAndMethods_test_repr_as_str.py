# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_repr_as_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        pass
    Foo.__repr__ = Foo.__str__
    foo = Foo()
    self.assertRaises(RecursionError, str, foo)
    self.assertRaises(RecursionError, repr, foo)
