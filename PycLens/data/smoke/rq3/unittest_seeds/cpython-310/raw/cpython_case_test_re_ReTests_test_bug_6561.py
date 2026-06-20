# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_6561

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decimal_digits = ['7', '๘', '０']
    for x in decimal_digits:
        self.assertEqual(re.match('^\\d$', x).group(0), x)
    not_decimal_digits = ['Ⅵ', '〹', '₂', '㊴']
    for x in not_decimal_digits:
        self.assertIsNone(re.match('^\\d$', x))
