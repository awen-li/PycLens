# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_multiple_vars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 98
    y = 'abc'
    self.assertEqual(f'{x}{y}', '98abc')
    self.assertEqual(f'X{x}{y}', 'X98abc')
    self.assertEqual(f'{x}X{y}', '98Xabc')
    self.assertEqual(f'{x}{y}X', '98abcX')
    self.assertEqual(f'X{x}Y{y}', 'X98Yabc')
    self.assertEqual(f'X{x}{y}Y', 'X98abcY')
    self.assertEqual(f'{x}X{y}Y', '98XabcY')
    self.assertEqual(f'X{x}Y{y}Z', 'X98YabcZ')
