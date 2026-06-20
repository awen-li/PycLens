# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_iadd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('a')
    d += 'bcd'
    self.assertEqual(list(d), list('abcd'))
    d += d
    self.assertEqual(list(d), list('abcdabcd'))
