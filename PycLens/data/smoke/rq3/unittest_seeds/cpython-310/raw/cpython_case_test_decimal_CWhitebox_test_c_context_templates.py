# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_context_templates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(C.BasicContext._traps, C.DecIEEEInvalidOperation | C.DecDivisionByZero | C.DecOverflow | C.DecUnderflow | C.DecClamped)
    self.assertEqual(C.DefaultContext._traps, C.DecIEEEInvalidOperation | C.DecDivisionByZero | C.DecOverflow)
