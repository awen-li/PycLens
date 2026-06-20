# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 200
    d = deque(range(n))
    for i in range(n):
        d[i] = 10 * i
    self.assertEqual(list(d), [10 * i for i in range(n)])
    l = list(d)
    for i in range(1 - n, 0, -1):
        d[i] = 7 * i
        l[i] = 7 * i
    self.assertEqual(list(d), l)
