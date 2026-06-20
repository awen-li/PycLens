# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_empty_format_specifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 'test'
    self.assertEqual(f'{x}', 'test')
    self.assertEqual(f'{x:}', 'test')
    self.assertEqual(f'{x!s:}', 'test')
    self.assertEqual(f'{x!r:}', "'test'")
