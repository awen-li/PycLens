# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_insort_keynotNone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = []
    y = {'a': 2, 'b': 1}
    for f in (self.module.insort_left, self.module.insort_right):
        self.assertRaises(TypeError, f, x, y, key='b')
