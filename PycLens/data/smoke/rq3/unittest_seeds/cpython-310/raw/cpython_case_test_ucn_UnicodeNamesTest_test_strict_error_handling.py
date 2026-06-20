# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_strict_error_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(UnicodeError, str, b'\\N{blah}', 'unicode-escape', 'strict')
    self.assertRaises(UnicodeError, str, bytes('\\N{%s}' % ('x' * 100000), 'ascii'), 'unicode-escape', 'strict')
    self.assertRaises(UnicodeError, str, b'\\N{SPACE', 'unicode-escape', 'strict')
    self.assertRaises(UnicodeError, str, b'\\NSPACE', 'unicode-escape', 'strict')
