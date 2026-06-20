# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ConvertTest_test_inf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for INF in (float('inf'), Decimal('inf')):
        for inf in (INF, -INF):
            x = statistics._convert(inf, type(inf))
            self.check_exact_equal(x, inf)
