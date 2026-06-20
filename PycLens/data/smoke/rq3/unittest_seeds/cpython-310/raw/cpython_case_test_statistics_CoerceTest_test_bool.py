# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: CoerceTest_test_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for T in (int, float, Fraction, Decimal):
        self.assertIs(statistics._coerce(T, bool), T)

        class MyClass(T):
            pass
        self.assertIs(statistics._coerce(MyClass, bool), MyClass)
