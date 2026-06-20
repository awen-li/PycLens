# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_str_of_str_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import binascii
    import io

    class octetstring(str):

        def __str__(self):
            return binascii.b2a_hex(self.encode('ascii')).decode('ascii')

        def __repr__(self):
            return self + ' repr'
    o = octetstring('A')
    self.assertEqual(type(o), octetstring)
    self.assertEqual(type(str(o)), str)
    self.assertEqual(type(repr(o)), str)
    self.assertEqual(ord(o), 65)
    self.assertEqual(str(o), '41')
    self.assertEqual(repr(o), 'A repr')
    self.assertEqual(o.__str__(), '41')
    self.assertEqual(o.__repr__(), 'A repr')
