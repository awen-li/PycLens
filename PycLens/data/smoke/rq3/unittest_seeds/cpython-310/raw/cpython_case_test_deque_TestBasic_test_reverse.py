# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_reverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 500
    data = [random.random() for i in range(n)]
    for i in range(n):
        d = deque(data[:i])
        r = d.reverse()
        self.assertEqual(list(d), list(reversed(data[:i])))
        self.assertIs(r, None)
        d.reverse()
        self.assertEqual(list(d), data[:i])
    self.assertRaises(TypeError, d.reverse, 1)
