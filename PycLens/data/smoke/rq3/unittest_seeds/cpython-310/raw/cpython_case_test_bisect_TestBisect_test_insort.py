# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_insort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from random import shuffle
    mod = self.module
    keyfunc = abs
    data = list(range(-10, 11)) + list(range(-20, 20, 2))
    shuffle(data)
    target = []
    for x in data:
        mod.insort_left(target, x, key=keyfunc)
        self.assertEqual(sorted(target, key=keyfunc), target)
    target = []
    for x in data:
        mod.insort_right(target, x, key=keyfunc)
        self.assertEqual(sorted(target, key=keyfunc), target)
