# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_literals_with_leading_zeroes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for arg in ['077787', '0xj', '0x.', '0e', '090000000000000', '080000000000000', '000000000000009', '000000000000008', '0b42', '0BADCAFE', '0o123456789', '0b1.1', '0o4.2', '0b101j', '0o153j', '0b100e1', '0o777e1', '0777', '000777', '000000000000007']:
        self.assertRaises(SyntaxError, eval, arg)
    self.assertEqual(eval('0xff'), 255)
    self.assertEqual(eval('0777.'), 777)
    self.assertEqual(eval('0777.0'), 777)
    self.assertEqual(eval('000000000000000000000000000000000000000000000000000777e0'), 777)
    self.assertEqual(eval('0777e1'), 7770)
    self.assertEqual(eval('0e0'), 0)
    self.assertEqual(eval('0000e-012'), 0)
    self.assertEqual(eval('09.5'), 9.5)
    self.assertEqual(eval('0777j'), 777j)
    self.assertEqual(eval('000'), 0)
    self.assertEqual(eval('00j'), 0j)
    self.assertEqual(eval('00.0'), 0)
    self.assertEqual(eval('0e3'), 0)
    self.assertEqual(eval('090000000000000.'), 90000000000000.0)
    self.assertEqual(eval('090000000000000.0000000000000000000000'), 90000000000000.0)
    self.assertEqual(eval('090000000000000e0'), 90000000000000.0)
    self.assertEqual(eval('090000000000000e-0'), 90000000000000.0)
    self.assertEqual(eval('090000000000000j'), 90000000000000j)
    self.assertEqual(eval('000000000000008.'), 8.0)
    self.assertEqual(eval('000000000000009.'), 9.0)
    self.assertEqual(eval('0b101010'), 42)
    self.assertEqual(eval('-0b000000000010'), -2)
    self.assertEqual(eval('0o777'), 511)
    self.assertEqual(eval('-0o0000010'), -8)
