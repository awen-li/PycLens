# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: StrTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '-' * size
    sf = '%s' % (s,)
    self.assertTrue(s == sf)
    del sf
    sf = '..%s..' % (s,)
    self.assertEqual(len(sf), len(s) + 4)
    self.assertTrue(sf.startswith('..-'))
    self.assertTrue(sf.endswith('-..'))
    del s, sf
    size //= 2
    edge = '-' * size
    s = ''.join([edge, '%s', edge])
    del edge
    s = s % '...'
    self.assertEqual(len(s), size * 2 + 3)
    self.assertEqual(s.count('.'), 3)
    self.assertEqual(s.count('-'), size * 2)
