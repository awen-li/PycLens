# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_leading_trailing_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(f'{3}', '3')
    self.assertEqual(f'{3}', '3')
    self.assertEqual(f'{3}', '3')
    self.assertEqual(f'{3}', '3')
    self.assertEqual(f'expr={ {x: y for (x, y) in [(1, 2)]}}', 'expr={1: 2}')
    self.assertEqual(f'expr={ {x: y for (x, y) in [(1, 2)]}}', 'expr={1: 2}')
