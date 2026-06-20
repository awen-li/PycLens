# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_str_format_differences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'a': 'string', 0: 'integer'}
    a = 0
    self.assertEqual(f'{d[0]}', 'integer')
    self.assertEqual(f"{d['a']}", 'string')
    self.assertEqual(f'{d[a]}', 'integer')
    self.assertEqual('{d[a]}'.format(d=d), 'string')
    self.assertEqual('{d[0]}'.format(d=d), 'integer')
