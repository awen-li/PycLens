# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_enum_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Konstants = self.Konstants
    self.assertFormatIsValue('{}', Konstants.TAU)
    self.assertFormatIsValue('{:}', Konstants.TAU)
    self.assertFormatIsValue('{:20}', Konstants.TAU)
    self.assertFormatIsValue('{:^20}', Konstants.TAU)
    self.assertFormatIsValue('{:>20}', Konstants.TAU)
    self.assertFormatIsValue('{:<20}', Konstants.TAU)
    self.assertFormatIsValue('{:n}', Konstants.TAU)
    self.assertFormatIsValue('{:5.2}', Konstants.TAU)
    self.assertFormatIsValue('{:f}', Konstants.TAU)
