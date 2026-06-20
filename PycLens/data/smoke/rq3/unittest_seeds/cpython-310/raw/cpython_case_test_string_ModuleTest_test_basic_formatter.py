# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_basic_formatter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()
    self.assertEqual(fmt.format('foo'), 'foo')
    self.assertEqual(fmt.format('foo{0}', 'bar'), 'foobar')
    self.assertEqual(fmt.format('foo{1}{0}-{1}', 'bar', 6), 'foo6bar-6')
    self.assertRaises(TypeError, fmt.format)
    self.assertRaises(TypeError, string.Formatter.format)
