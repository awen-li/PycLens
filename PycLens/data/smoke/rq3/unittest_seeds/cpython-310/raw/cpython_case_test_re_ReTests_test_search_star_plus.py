# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_search_star_plus

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.search('x*', 'axx').span(0), (0, 0))
    self.assertEqual(re.search('x*', 'axx').span(), (0, 0))
    self.assertEqual(re.search('x+', 'axx').span(0), (1, 3))
    self.assertEqual(re.search('x+', 'axx').span(), (1, 3))
    self.assertIsNone(re.search('x', 'aaa'))
    self.assertEqual(re.match('a*', 'xxx').span(0), (0, 0))
    self.assertEqual(re.match('a*', 'xxx').span(), (0, 0))
    self.assertEqual(re.match('x*', 'xxxa').span(0), (0, 3))
    self.assertEqual(re.match('x*', 'xxxa').span(), (0, 3))
    self.assertIsNone(re.match('a+', 'xxx'))
