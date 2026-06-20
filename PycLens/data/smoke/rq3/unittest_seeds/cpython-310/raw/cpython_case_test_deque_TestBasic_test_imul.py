# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_imul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in (-10, -1, 0, 1, 2, 10, 1000):
        d = deque()
        d *= n
        self.assertEqual(d, deque())
        self.assertIsNone(d.maxlen)
    for n in (-10, -1, 0, 1, 2, 10, 1000):
        d = deque('a')
        d *= n
        self.assertEqual(d, deque('a' * n))
        self.assertIsNone(d.maxlen)
    for n in (-10, -1, 0, 1, 2, 10, 499, 500, 501, 1000):
        d = deque('a', 500)
        d *= n
        self.assertEqual(d, deque('a' * min(n, 500)))
        self.assertEqual(d.maxlen, 500)
    for n in (-10, -1, 0, 1, 2, 10, 1000):
        d = deque('abcdef')
        d *= n
        self.assertEqual(d, deque('abcdef' * n))
        self.assertIsNone(d.maxlen)
    for n in (-10, -1, 0, 1, 2, 10, 499, 500, 501, 1000):
        d = deque('abcdef', 500)
        d *= n
        self.assertEqual(d, deque(('abcdef' * n)[-500:]))
        self.assertEqual(d.maxlen, 500)
