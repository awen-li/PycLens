# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_mul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('abc')
    self.assertEqual(d * -5, deque())
    self.assertEqual(d * 0, deque())
    self.assertEqual(d * 1, deque('abc'))
    self.assertEqual(d * 2, deque('abcabc'))
    self.assertEqual(d * 3, deque('abcabcabc'))
    self.assertIsNot(d * 1, d)
    self.assertEqual(deque() * 0, deque())
    self.assertEqual(deque() * 1, deque())
    self.assertEqual(deque() * 5, deque())
    self.assertEqual(-5 * d, deque())
    self.assertEqual(0 * d, deque())
    self.assertEqual(1 * d, deque('abc'))
    self.assertEqual(2 * d, deque('abcabc'))
    self.assertEqual(3 * d, deque('abcabcabc'))
    d = deque('abc', maxlen=5)
    self.assertEqual(d * -5, deque())
    self.assertEqual(d * 0, deque())
    self.assertEqual(d * 1, deque('abc'))
    self.assertEqual(d * 2, deque('bcabc'))
    self.assertEqual(d * 30, deque('bcabc'))
