# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self):
            self.i = 0

        def __call__(self):
            i = self.i
            self.i = i + 1
            if i > 100:
                raise IndexError
            return i
    self.check_iterator(iter(C(), 10), list(range(10)), pickle=False)
