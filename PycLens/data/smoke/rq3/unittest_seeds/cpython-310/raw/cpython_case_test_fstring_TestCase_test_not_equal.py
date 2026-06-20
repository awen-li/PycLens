# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_not_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(f'{3 != 4}', 'True')
    self.assertEqual(f'{3 != 4:}', 'True')
    self.assertEqual(f'{3 != 4!s}', 'True')
    self.assertEqual(f'{3 != 4!s:.3}', 'Tru')
