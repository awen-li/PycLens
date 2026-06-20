# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ConvertTest_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = statistics._convert(Fraction(71), int)
    self.check_exact_equal(x, 71)

    class MyInt(int):
        pass
    x = statistics._convert(Fraction(17), MyInt)
    self.check_exact_equal(x, MyInt(17))
