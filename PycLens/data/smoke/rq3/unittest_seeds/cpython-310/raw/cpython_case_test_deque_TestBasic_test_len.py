# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('ab')
    self.assertEqual(len(d), 2)
    d.popleft()
    self.assertEqual(len(d), 1)
    d.pop()
    self.assertEqual(len(d), 0)
    self.assertRaises(IndexError, d.pop)
    self.assertEqual(len(d), 0)
    d.append('c')
    self.assertEqual(len(d), 1)
    d.appendleft('d')
    self.assertEqual(len(d), 2)
    d.clear()
    self.assertEqual(len(d), 0)
