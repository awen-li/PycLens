# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_format_keyword_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()
    self.assertEqual(fmt.format('-{arg}-', arg='test'), '-test-')
    self.assertRaises(KeyError, fmt.format, '-{arg}-')
    self.assertEqual(fmt.format('-{self}-', self='test'), '-test-')
    self.assertRaises(KeyError, fmt.format, '-{self}-')
    self.assertEqual(fmt.format('-{format_string}-', format_string='test'), '-test-')
    self.assertRaises(KeyError, fmt.format, '-{format_string}-')
    with self.assertRaisesRegex(TypeError, 'format_string'):
        fmt.format(format_string='-{arg}-', arg='test')
