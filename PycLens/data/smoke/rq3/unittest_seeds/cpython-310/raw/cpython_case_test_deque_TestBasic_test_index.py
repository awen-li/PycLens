# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in (1, 2, 30, 40, 200):
        d = deque(range(n))
        for i in range(n):
            self.assertEqual(d.index(i), i)
        with self.assertRaises(ValueError):
            d.index(n + 1)
        d = deque(range(n))
        d[n // 2] = MutateCmp(d, False)
        with self.assertRaises(RuntimeError):
            d.index(n)
        d = deque(range(n))
        d[n // 2] = BadCmp()
        with self.assertRaises(RuntimeError):
            d.index(n)
    elements = 'ABCDEFGHI'
    nonelement = 'Z'
    d = deque(elements * 2)
    s = list(elements * 2)
    for start in range(-5 - len(s) * 2, 5 + len(s) * 2):
        for stop in range(-5 - len(s) * 2, 5 + len(s) * 2):
            for element in elements + 'Z':
                try:
                    target = s.index(element, start, stop)
                except ValueError:
                    with self.assertRaises(ValueError):
                        d.index(element, start, stop)
                else:
                    self.assertEqual(d.index(element, start, stop), target)
    d = deque(range(0, 10000, 10))
    for step in range(100):
        i = d.index(8500, 700)
        self.assertEqual(d[i], 8500)
        d.rotate()
