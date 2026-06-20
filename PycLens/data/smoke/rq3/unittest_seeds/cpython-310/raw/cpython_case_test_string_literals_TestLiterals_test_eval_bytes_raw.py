# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_bytes_raw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval(" br'x' "), b'x')
    self.assertEqual(eval(" rb'x' "), b'x')
    self.assertEqual(eval(" br'\\x01' "), b'\\' + b'x01')
    self.assertEqual(eval(" rb'\\x01' "), b'\\' + b'x01')
    self.assertEqual(eval(" br'\x01' "), byte(1))
    self.assertEqual(eval(" rb'\x01' "), byte(1))
    self.assertEqual(eval(" br'\\x81' "), b'\\' + b'x81')
    self.assertEqual(eval(" rb'\\x81' "), b'\\' + b'x81')
    self.assertRaises(SyntaxError, eval, " br'\x81' ")
    self.assertRaises(SyntaxError, eval, " rb'\x81' ")
    self.assertEqual(eval(" br'\\u1881' "), b'\\' + b'u1881')
    self.assertEqual(eval(" rb'\\u1881' "), b'\\' + b'u1881')
    self.assertRaises(SyntaxError, eval, " br'ᢁ' ")
    self.assertRaises(SyntaxError, eval, " rb'ᢁ' ")
    self.assertEqual(eval(" br'\\U0001d120' "), b'\\' + b'U0001d120')
    self.assertEqual(eval(" rb'\\U0001d120' "), b'\\' + b'U0001d120')
    self.assertRaises(SyntaxError, eval, " br'𝄠' ")
    self.assertRaises(SyntaxError, eval, " rb'𝄠' ")
    self.assertRaises(SyntaxError, eval, " bb'' ")
    self.assertRaises(SyntaxError, eval, " rr'' ")
    self.assertRaises(SyntaxError, eval, " brr'' ")
    self.assertRaises(SyntaxError, eval, " bbr'' ")
    self.assertRaises(SyntaxError, eval, " rrb'' ")
    self.assertRaises(SyntaxError, eval, " rbb'' ")
