# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_enum_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Directional = self.Directional
    self.assertFormatIsValue('{}', Directional.WEST)
    self.assertFormatIsValue('{:}', Directional.WEST)
    self.assertFormatIsValue('{:20}', Directional.WEST)
    self.assertFormatIsValue('{:^20}', Directional.WEST)
    self.assertFormatIsValue('{:>20}', Directional.WEST)
    self.assertFormatIsValue('{:<20}', Directional.WEST)
