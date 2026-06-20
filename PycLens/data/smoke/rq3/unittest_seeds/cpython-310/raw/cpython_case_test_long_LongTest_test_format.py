# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in special:
        self.check_format_1(x)
    for i in range(10):
        for lenx in range(1, MAXDIGITS + 1):
            x = self.getran(lenx)
            self.check_format_1(x)
