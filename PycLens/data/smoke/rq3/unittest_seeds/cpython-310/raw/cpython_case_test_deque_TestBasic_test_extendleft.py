# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_extendleft

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('a')
    self.assertRaises(TypeError, d.extendleft, 1)
    d.extendleft('bcd')
    self.assertEqual(list(d), list(reversed('abcd')))
    d.extendleft(d)
    self.assertEqual(list(d), list('abcddcba'))
    d = deque()
    d.extendleft(range(1000))
    self.assertEqual(list(d), list(reversed(range(1000))))
    self.assertRaises(SyntaxError, d.extendleft, fail())
