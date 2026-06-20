# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque(range(200))
    e = eval(repr(d))
    self.assertEqual(list(d), list(e))
    d.append(d)
    self.assertEqual(repr(d)[-20:], '7, 198, 199, [...]])')
