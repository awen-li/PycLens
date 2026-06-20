# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_725149

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('(a)(?:(?=(b)*)c)*', 'abb').groups(), ('a', None))
    self.assertEqual(re.match('(a)((?!(b)*))*', 'abb').groups(), ('a', None, None))
