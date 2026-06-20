# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        x = math.exp(-1000000000)
    except:
        self.fail('underflowing exp() should not have raised an exception')
    if x != 0:
        self.fail('underflowing exp() should have returned 0')
    try:
        x = math.exp(1000000000)
    except OverflowError:
        pass
    else:
        self.fail("overflowing exp() didn't trigger OverflowError")
    try:
        x = math.sqrt(-1.0)
    except ValueError:
        pass
    else:
        self.fail("sqrt(-1) didn't raise ValueError")
