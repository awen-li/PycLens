# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_auto_numbering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = string.Formatter()
    self.assertEqual(fmt.format('foo{}{}', 'bar', 6), 'foo{}{}'.format('bar', 6))
    self.assertEqual(fmt.format('foo{1}{num}{1}', None, 'bar', num=6), 'foo{1}{num}{1}'.format(None, 'bar', num=6))
    self.assertEqual(fmt.format('{:^{}}', 'bar', 6), '{:^{}}'.format('bar', 6))
    self.assertEqual(fmt.format('{:^{}} {}', 'bar', 6, 'X'), '{:^{}} {}'.format('bar', 6, 'X'))
    self.assertEqual(fmt.format('{:^{pad}}{}', 'foo', 'bar', pad=6), '{:^{pad}}{}'.format('foo', 'bar', pad=6))
    with self.assertRaises(ValueError):
        fmt.format('foo{1}{}', 'bar', 6)
    with self.assertRaises(ValueError):
        fmt.format('foo{}{1}', 'bar', 6)
