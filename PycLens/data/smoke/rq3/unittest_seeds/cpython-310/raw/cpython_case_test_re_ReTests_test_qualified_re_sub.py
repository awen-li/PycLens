# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_qualified_re_sub

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.sub('a', 'b', 'aaaaa'), 'bbbbb')
    self.assertEqual(re.sub('a', 'b', 'aaaaa', 1), 'baaaa')
    self.assertEqual(re.sub('a', 'b', 'aaaaa', count=1), 'baaaa')
