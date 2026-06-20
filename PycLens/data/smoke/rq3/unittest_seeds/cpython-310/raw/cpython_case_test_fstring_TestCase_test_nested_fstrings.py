# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_nested_fstrings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    y = 5
    self.assertEqual(f"{f'{0}' * 3}", '000')
    self.assertEqual(f"{f'{y}' * 3}", '555')
