# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_str_raw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval(" r'x' "), 'x')
    self.assertEqual(eval(" r'\\x01' "), '\\' + 'x01')
    self.assertEqual(eval(" r'\x01' "), chr(1))
    self.assertEqual(eval(" r'\\x81' "), '\\' + 'x81')
    self.assertEqual(eval(" r'\x81' "), chr(129))
    self.assertEqual(eval(" r'\\u1881' "), '\\' + 'u1881')
    self.assertEqual(eval(" r'ᢁ' "), chr(6273))
    self.assertEqual(eval(" r'\\U0001d120' "), '\\' + 'U0001d120')
    self.assertEqual(eval(" r'𝄠' "), chr(119072))
