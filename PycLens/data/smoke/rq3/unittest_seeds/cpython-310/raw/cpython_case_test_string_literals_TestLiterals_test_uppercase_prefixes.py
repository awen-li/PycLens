# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_uppercase_prefixes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval(" B'x' "), b'x')
    self.assertEqual(eval(" R'\\x01' "), '\\x01')
    self.assertEqual(eval(" BR'\\x01' "), b'\\x01')
    self.assertEqual(eval(" F'{1+1}' "), f'{1 + 1}')
    self.assertEqual(eval(" U'\\U0001d120' "), u'𝄠')
