# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 500
    d = deque(range(n))
    self.assertRaises(IndexError, d.__delitem__, -n - 1)
    self.assertRaises(IndexError, d.__delitem__, n)
    for i in range(n):
        self.assertEqual(len(d), n - i)
        j = random.randrange(-len(d), len(d))
        val = d[j]
        self.assertIn(val, d)
        del d[j]
        self.assertNotIn(val, d)
    self.assertEqual(len(d), 0)
