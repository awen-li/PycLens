# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_maxlen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, deque, 'abc', -1)
    self.assertRaises(ValueError, deque, 'abc', -2)
    it = iter(range(10))
    d = deque(it, maxlen=3)
    self.assertEqual(list(it), [])
    self.assertEqual(repr(d), 'deque([7, 8, 9], maxlen=3)')
    self.assertEqual(list(d), [7, 8, 9])
    self.assertEqual(d, deque(range(10), 3))
    d.append(10)
    self.assertEqual(list(d), [8, 9, 10])
    d.appendleft(7)
    self.assertEqual(list(d), [7, 8, 9])
    d.extend([10, 11])
    self.assertEqual(list(d), [9, 10, 11])
    d.extendleft([8, 7])
    self.assertEqual(list(d), [7, 8, 9])
    d = deque(range(200), maxlen=10)
    d.append(d)
    self.assertEqual(repr(d)[-30:], ', 198, 199, [...]], maxlen=10)')
    d = deque(range(10), maxlen=None)
    self.assertEqual(repr(d), 'deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])')
