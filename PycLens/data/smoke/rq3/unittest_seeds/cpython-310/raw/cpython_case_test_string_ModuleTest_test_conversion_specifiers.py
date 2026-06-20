# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_conversion_specifiers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()
    self.assertEqual(fmt.format('-{arg!r}-', arg='test'), "-'test'-")
    self.assertEqual(fmt.format('{0!s}', 'test'), 'test')
    self.assertRaises(ValueError, fmt.format, '{0!h}', 'test')
    self.assertEqual(fmt.format('{0!a}', 42), '42')
    self.assertEqual(fmt.format('{0!a}', string.ascii_letters), "'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    self.assertEqual(fmt.format('{0!a}', chr(255)), "'\\xff'")
    self.assertEqual(fmt.format('{0!a}', chr(256)), "'\\u0100'")
