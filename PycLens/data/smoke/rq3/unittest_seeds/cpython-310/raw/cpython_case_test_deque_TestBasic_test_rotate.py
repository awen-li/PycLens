# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_rotate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = tuple('abcde')
    n = len(s)
    d = deque(s)
    d.rotate(1)
    self.assertEqual(''.join(d), 'eabcd')
    d = deque(s)
    d.rotate(-1)
    self.assertEqual(''.join(d), 'bcdea')
    d.rotate()
    self.assertEqual(tuple(d), s)
    for i in range(n * 3):
        d = deque(s)
        e = deque(d)
        d.rotate(i)
        for j in range(i):
            e.rotate(1)
        self.assertEqual(tuple(d), tuple(e))
        d.rotate(-i)
        self.assertEqual(tuple(d), s)
        e.rotate(n - i)
        self.assertEqual(tuple(e), s)
    for i in range(n * 3):
        d = deque(s)
        e = deque(d)
        d.rotate(-i)
        for j in range(i):
            e.rotate(-1)
        self.assertEqual(tuple(d), tuple(e))
        d.rotate(i)
        self.assertEqual(tuple(d), s)
        e.rotate(i - n)
        self.assertEqual(tuple(e), s)
    d = deque(s)
    e = deque(s)
    e.rotate(BIG + 17)
    dr = d.rotate
    for i in range(BIG + 17):
        dr()
    self.assertEqual(tuple(d), tuple(e))
    self.assertRaises(TypeError, d.rotate, 'x')
    self.assertRaises(TypeError, d.rotate, 1, 10)
    d = deque()
    d.rotate()
    self.assertEqual(d, deque())
