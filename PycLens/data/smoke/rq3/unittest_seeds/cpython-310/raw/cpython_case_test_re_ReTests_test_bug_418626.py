# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_418626

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('.*?c', 10000 * 'ab' + 'cd').end(0), 20001)
    self.assertEqual(re.match('.*?cd', 5000 * 'ab' + 'c' + 5000 * 'ab' + 'cde').end(0), 20003)
    self.assertEqual(re.match('.*?cd', 20000 * 'abc' + 'de').end(0), 60001)
    self.assertEqual(re.search('(a|b)*?c', 10000 * 'ab' + 'cd').end(0), 20001)
