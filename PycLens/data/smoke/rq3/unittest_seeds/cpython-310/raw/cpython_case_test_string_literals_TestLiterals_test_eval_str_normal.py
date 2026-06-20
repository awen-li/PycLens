# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_str_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval(" 'x' "), 'x')
    self.assertEqual(eval(" '\\x01' "), chr(1))
    self.assertEqual(eval(" '\x01' "), chr(1))
    self.assertEqual(eval(" '\\x81' "), chr(129))
    self.assertEqual(eval(" '\x81' "), chr(129))
    self.assertEqual(eval(" '\\u1881' "), chr(6273))
    self.assertEqual(eval(" 'ᢁ' "), chr(6273))
    self.assertEqual(eval(" '\\U0001d120' "), chr(119072))
    self.assertEqual(eval(" '𝄠' "), chr(119072))
