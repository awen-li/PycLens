# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_expand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('(?P<first>first) (?P<second>second)', 'first second').expand('\\2 \\1 \\g<second> \\g<first>'), 'second first second first')
    self.assertEqual(re.match('(?P<first>first)|(?P<second>second)', 'first').expand('\\2 \\g<second>'), ' ')
