# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_bitop_identities

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in special:
        self.check_bitop_identities_1(x)
    digits = range(1, MAXDIGITS + 1)
    for lenx in digits:
        x = self.getran(lenx)
        self.check_bitop_identities_1(x)
        for leny in digits:
            y = self.getran(leny)
            self.check_bitop_identities_2(x, y)
            self.check_bitop_identities_3(x, y, self.getran((lenx + leny) // 2))
