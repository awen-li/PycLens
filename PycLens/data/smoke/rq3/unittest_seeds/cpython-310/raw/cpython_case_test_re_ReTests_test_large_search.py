# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_large_search

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'a' * size
    m = re.search('$', s)
    self.assertIsNotNone(m)
    self.assertEqual(m.start(), size)
    self.assertEqual(m.end(), size)
