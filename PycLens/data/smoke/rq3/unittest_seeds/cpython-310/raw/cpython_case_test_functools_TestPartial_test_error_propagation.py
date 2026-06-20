# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_error_propagation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(x, y):
        x / y
    self.assertRaises(ZeroDivisionError, self.partial(f, 1, 0))
    self.assertRaises(ZeroDivisionError, self.partial(f, 1), 0)
    self.assertRaises(ZeroDivisionError, self.partial(f), 1, 0)
    self.assertRaises(ZeroDivisionError, self.partial(f, y=0), 1)
