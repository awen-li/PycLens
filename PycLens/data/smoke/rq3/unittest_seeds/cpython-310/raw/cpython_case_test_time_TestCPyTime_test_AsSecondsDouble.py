# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestCPyTime_test_AsSecondsDouble

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PyTime_AsSecondsDouble

    def float_converter(ns):
        if abs(ns) % SEC_TO_NS == 0:
            return float(ns // SEC_TO_NS)
        else:
            return float(ns) / SEC_TO_NS
    self.check_int_rounding(lambda ns, rnd: PyTime_AsSecondsDouble(ns), float_converter, NS_TO_SEC)
    for (time_rnd, _) in ROUNDING_MODES:
        with self.assertRaises(TypeError):
            PyTime_AsSecondsDouble(float('nan'))
