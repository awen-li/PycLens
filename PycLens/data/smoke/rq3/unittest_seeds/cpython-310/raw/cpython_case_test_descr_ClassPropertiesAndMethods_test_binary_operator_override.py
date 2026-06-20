# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_binary_operator_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class I(int):

        def __repr__(self):
            return 'I(%r)' % int(self)

        def __add__(self, other):
            return I(int(self) + int(other))
        __radd__ = __add__

        def __pow__(self, other, mod=None):
            if mod is None:
                return I(pow(int(self), int(other)))
            else:
                return I(pow(int(self), int(other), int(mod)))

        def __rpow__(self, other, mod=None):
            if mod is None:
                return I(pow(int(other), int(self), mod))
            else:
                return I(pow(int(other), int(self), int(mod)))
    self.assertEqual(repr(I(1) + I(2)), 'I(3)')
    self.assertEqual(repr(I(1) + 2), 'I(3)')
    self.assertEqual(repr(1 + I(2)), 'I(3)')
    self.assertEqual(repr(I(2) ** I(3)), 'I(8)')
    self.assertEqual(repr(2 ** I(3)), 'I(8)')
    self.assertEqual(repr(I(2) ** 3), 'I(8)')
    self.assertEqual(repr(pow(I(2), I(3), I(5))), 'I(3)')

    class S(str):

        def __eq__(self, other):
            return self.lower() == other.lower()
