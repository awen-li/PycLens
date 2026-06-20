# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 200
    d = deque(range(n))
    l = list(range(n))
    for i in range(n):
        d.popleft()
        l.pop(0)
        if random.random() < 0.5:
            d.append(i)
            l.append(i)
        for j in range(1 - len(l), len(l)):
            assert d[j] == l[j]
    d = deque('superman')
    self.assertEqual(d[0], 's')
    self.assertEqual(d[-1], 'n')
    d = deque()
    self.assertRaises(IndexError, d.__getitem__, 0)
    self.assertRaises(IndexError, d.__getitem__, -1)
