# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PyFunctionality_test_py_alternate_formatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = P.Decimal
    localcontext = P.localcontext
    test_values = [('.0e', '1.0', '1e+0'), ('#.0e', '1.0', '1.e+0'), ('.0f', '1.0', '1'), ('#.0f', '1.0', '1.'), ('g', '1.1', '1.1'), ('#g', '1.1', '1.1'), ('.0g', '1', '1'), ('#.0g', '1', '1.'), ('.0%', '1.0', '100%'), ('#.0%', '1.0', '100.%')]
    for (fmt, d, result) in test_values:
        self.assertEqual(format(Decimal(d), fmt), result)
