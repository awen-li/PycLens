# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(string.whitespace, ' \t\n\r\x0b\x0c')
    self.assertEqual(string.ascii_lowercase, 'abcdefghijklmnopqrstuvwxyz')
    self.assertEqual(string.ascii_uppercase, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    self.assertEqual(string.ascii_letters, string.ascii_lowercase + string.ascii_uppercase)
    self.assertEqual(string.digits, '0123456789')
    self.assertEqual(string.hexdigits, string.digits + 'abcdefABCDEF')
    self.assertEqual(string.octdigits, '01234567')
    self.assertEqual(string.punctuation, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    self.assertEqual(string.printable, string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace)
