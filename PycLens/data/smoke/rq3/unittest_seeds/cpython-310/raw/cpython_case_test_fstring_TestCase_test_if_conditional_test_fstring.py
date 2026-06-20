# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_if_conditional_test_fstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flag = 0
    if f'{x}':
        flag = 1
    else:
        flag = 2
    self.assertEqual(flag, expected)
