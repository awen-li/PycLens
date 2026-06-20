# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ops = [operator.lt, operator.gt, operator.le, operator.ge]
    x = Object(1)
    y = Object(1)
    a = weakref.ref(x)
    b = weakref.ref(y)
    for op in ops:
        self.assertRaises(TypeError, op, a, b)
    del x, y
    gc.collect()
    for op in ops:
        self.assertRaises(TypeError, op, a, b)
