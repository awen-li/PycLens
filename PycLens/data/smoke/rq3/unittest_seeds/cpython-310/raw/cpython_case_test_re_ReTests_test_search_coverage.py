# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_search_coverage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.search('\\s(b)', ' b').group(1), 'b')
    self.assertEqual(re.search('a\\s', 'a ').group(0), 'a ')
