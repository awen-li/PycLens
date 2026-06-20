# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __init__(self, foo):
            self.foo = foo

        def __copy__(self):
            return C(self.foo)
    x = C(42)
    y = copy.copy(x)
    self.assertEqual(y.__class__, x.__class__)
    self.assertEqual(y.foo, x.foo)
