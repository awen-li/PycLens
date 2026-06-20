# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque(range(100))
    self.assertEqual(len(d), 100)
    d.clear()
    self.assertEqual(len(d), 0)
    self.assertEqual(list(d), [])
    d.clear()
    self.assertEqual(list(d), [])
