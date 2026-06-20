# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_bytes_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval(" b'x' "), b'x')
    self.assertEqual(eval(" b'\\x01' "), byte(1))
    self.assertEqual(eval(" b'\x01' "), byte(1))
    self.assertEqual(eval(" b'\\x81' "), byte(129))
    self.assertRaises(SyntaxError, eval, " b'\x81' ")
    self.assertEqual(eval(" br'\\u1881' "), b'\\' + b'u1881')
    self.assertRaises(SyntaxError, eval, " b'ᢁ' ")
    self.assertEqual(eval(" br'\\U0001d120' "), b'\\' + b'U0001d120')
    self.assertRaises(SyntaxError, eval, " b'𝄠' ")
