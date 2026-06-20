# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMultiMode_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    multimode = statistics.multimode
    self.assertEqual(multimode('aabbbbbbbbcc'), ['b'])
    self.assertEqual(multimode('aabbbbccddddeeffffgg'), ['b', 'd', 'f'])
    self.assertEqual(multimode(''), [])
