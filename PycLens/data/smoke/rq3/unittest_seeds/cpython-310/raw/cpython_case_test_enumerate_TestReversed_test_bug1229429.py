# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_bug1229429

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        pass
    r = f.__reversed__ = object()
    rc = sys.getrefcount(r)
    for i in range(10):
        try:
            reversed(f)
        except TypeError:
            pass
        else:
            self.fail("non-callable __reversed__ didn't raise!")
    self.assertEqual(rc, sys.getrefcount(r))
