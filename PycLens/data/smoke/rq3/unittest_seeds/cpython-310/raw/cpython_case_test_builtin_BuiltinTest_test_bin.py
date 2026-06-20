# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_bin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(bin(0), '0b0')
    self.assertEqual(bin(1), '0b1')
    self.assertEqual(bin(-1), '-0b1')
    self.assertEqual(bin(2 ** 65), '0b1' + '0' * 65)
    self.assertEqual(bin(2 ** 65 - 1), '0b' + '1' * 65)
    self.assertEqual(bin(-2 ** 65), '-0b1' + '0' * 65)
    self.assertEqual(bin(-(2 ** 65 - 1)), '-0b' + '1' * 65)
