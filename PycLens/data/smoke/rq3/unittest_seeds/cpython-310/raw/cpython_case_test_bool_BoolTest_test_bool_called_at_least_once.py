# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_bool_called_at_least_once

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __init__(self):
            self.count = 0

        def __bool__(self):
            self.count += 1
            return True

    def f(x):
        if x or True:
            pass
    x = X()
    f(x)
    self.assertGreaterEqual(x.count, 1)
