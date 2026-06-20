# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_maxlen_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = iter(range(100))
    deque(it, maxlen=0)
    self.assertEqual(list(it), [])
    it = iter(range(100))
    d = deque(maxlen=0)
    d.extend(it)
    self.assertEqual(list(it), [])
    it = iter(range(100))
    d = deque(maxlen=0)
    d.extendleft(it)
    self.assertEqual(list(it), [])
