# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_metaclass_override_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=self.Meta):
        pass
    marker = object()

    def func(*args, **kwargs):
        return marker
    X = types.new_class('X', (), {'metaclass': func})
    Y = types.new_class('Y', (object,), {'metaclass': func})
    Z = types.new_class('Z', (A,), {'metaclass': func})
    self.assertIs(marker, X)
    self.assertIs(marker, Y)
    self.assertIs(marker, Z)
