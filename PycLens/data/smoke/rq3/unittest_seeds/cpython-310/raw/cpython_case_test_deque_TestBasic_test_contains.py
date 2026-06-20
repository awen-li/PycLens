# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 200
    d = deque(range(n))
    for i in range(n):
        self.assertTrue(i in d)
    self.assertTrue(n + 1 not in d)
    d = deque(range(n))
    d[n // 2] = MutateCmp(d, False)
    with self.assertRaises(RuntimeError):
        n in d
    d = deque(range(n))
    d[n // 2] = BadCmp()
    with self.assertRaises(RuntimeError):
        n in d
